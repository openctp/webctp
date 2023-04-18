import logging

from typing import Callable
from openctp import thosttraderapi as tdapi
from constants import CallError
from constants import TdConstant as Constant
from utils import CTPObjectHelper, GlobalConfig


class TdClient(tdapi.CThostFtdcTraderSpi):
    
    def __init__(self, user_id, password):
        super().__init__()
        self._front_address:str = GlobalConfig.TdFrontAddress
        self._broker_id:str = GlobalConfig.BrokerID
        self._auth_code:str = GlobalConfig.AuthCode
        self._app_id:str = GlobalConfig.AppID
        self._user_id:str = user_id
        self._password: str = password
        logging.debug(f"Td front_address: {self._front_address}, broker_id: {self._broker_id}, auth_code: {self._auth_code}, app_id: {self._app_id}, user_id: {self._user_id}")
        self._rsp_callback: Callable[[dict[str, any]], None] = None
        self._api: tdapi.CThostFtdcTraderApi = None
        self._connected: bool = False
    
    @property
    def rsp_callback(self) -> Callable[[dict[str, any]], None]:
        return self._rsp_callback

    @rsp_callback.setter
    def rsp_callback(self, callback: Callable[[dict[str, any]], None]):
        self._rsp_callback = callback
    
    def method_called(self, msg_type: str, ret: int):
        if ret != 0:
            response = CTPObjectHelper.build_response_dict(msg_type)
            response[Constant.RspInfo] = CallError.get_rsp_info(ret)
            self.rsp_callback(response)
    
    def release(self) -> None:
        self._api.RegisterSpi(None)
        self._api.Release()
        self._api = None
        self._connected = False

    def connect(self) -> None:
        """Not thread-safe"""
        if not self._connected:
            self.create_api()
            self._api.Init()
            self._connected = True
        else:
            self.authenticate()
    
    def create_api(self) -> tdapi.CThostFtdcTraderApi:
        con_file_path = GlobalConfig.get_con_file_path("td" + self._user_id)
        self._api: tdapi.CThostFtdcTraderApi = tdapi.CThostFtdcTraderApi.CreateFtdcTraderApi(con_file_path)
        self._api.RegisterSpi(self)
        self._api.SubscribePrivateTopic(tdapi.THOST_TERT_QUICK)
        self._api.SubscribePublicTopic(tdapi.THOST_TERT_QUICK)
        self._api.RegisterFront(self._front_address)
        return self._api

    def OnFrontConnected(self):
        """called when connect success"""
        logging.info("Td client connected")
        self.authenticate()

    def OnFrontDisconnected(self, nReason):
        """called when connection broken"""
        logging.info(f"Td client disconnected, error_code={nReason}")

    def authenticate(self):
        req = tdapi.CThostFtdcReqAuthenticateField()
        req.BrokerID = self._broker_id
        req.UserID = self._user_id
        req.AppID = self._app_id
        req.AuthCode = self._auth_code
        self._api.ReqAuthenticate(req, 0)

    def OnRspAuthenticate(self, pRspAuthenticateField: tdapi.CThostFtdcRspAuthenticateField,
                          pRspInfo: tdapi.CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        """called when authenticate success"""
        if pRspInfo is None or pRspInfo.ErrorID == 0:
            logging.info("authenticate success, start to login")
            self.login()
        else:
            logging.info("authenticate failed, please try again")
            self.processConnectResult(Constant.OnRspAuthenticate, pRspInfo)

    def login(self):
        req = tdapi.CThostFtdcReqUserLoginField()
        req.BrokerID = self._broker_id
        req.UserID = self._user_id
        req.Password = self._password
        req.UserProductInfo = "openctp"
        self._api.ReqUserLogin(req, 0)

    def OnRspUserLogin(self, pRspUserLogin: tdapi.CThostFtdcRspUserLoginField, pRspInfo: tdapi.CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        """called when login responds"""
        if pRspInfo is None or pRspInfo.ErrorID == 0:
            logging.info("loging success, start to confirm settlement info")
            self.settlementConfirm()
            self.processConnectResult(Constant.OnRspUserLogin, pRspInfo, pRspUserLogin)
        else:
            self.processConnectResult(Constant.OnRspUserLogin, pRspInfo)
            logging.info("login failed, please try again")
    
    def settlementConfirm(self):
        req = tdapi.CThostFtdcSettlementInfoConfirmField()
        req.BrokerID = self._broker_id
        req.InvestorID = self._user_id
        self._api.ReqSettlementInfoConfirm(req, 0)
    
    def OnRspQrySettlementInfoConfirm(self, pSettlementInfoConfirm: tdapi.CThostFtdcSettlementInfoConfirmField, pRspInfo: tdapi.CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        logging.info("confirm settlement info success")
        if pRspInfo is not None:
            logging.info(f"settlemnt confirm rsp info, ErrorID: {pRspInfo.ErrorID}, ErrorMsg: {pRspInfo.ErrorMsg}")
    
    def processConnectResult(self, messageType: str, pRspInfo: tdapi.CThostFtdcRspInfoField, pRspUserLogin: tdapi.CThostFtdcRspUserLoginField = None):
        response = CTPObjectHelper.build_response_dict(messageType, pRspInfo, 0, True)
        if pRspUserLogin:
            response[Constant.RspUserLogin] = {
                "TradingDay": pRspUserLogin.TradingDay,
                "LoginTime": pRspUserLogin.LoginTime,
                "BrokerID": pRspUserLogin.BrokerID,
                "UserID": pRspUserLogin.UserID,
                "SystemName": pRspUserLogin.SystemName,
                "FrontID": pRspUserLogin.FrontID,
                "SessionID": pRspUserLogin.SessionID,
                "MaxOrderRef": pRspUserLogin.MaxOrderRef,
                "SHFETime": pRspUserLogin.SHFETime,
                "DCETime": pRspUserLogin.DCETime,
                "CZCETime": pRspUserLogin.CZCETime,
                "FFEXTime": pRspUserLogin.FFEXTime,
                "INETime": pRspUserLogin.INETime
            }

        self.rsp_callback(response)
    
    def reqQryInstrument(self, request: dict[str, any]) -> int:
        req, requestId = CTPObjectHelper.extract_request(request, Constant.QryInstrument, tdapi.CThostFtdcQryInstrumentField)
        ret = self._api.ReqQryInstrument(req, requestId)
        self.method_called(Constant.OnRspQryInstrument, ret)
    
    def OnRspQryInstrument(self, pInstrument: tdapi.CThostFtdcInstrumentField, pRspInfo: tdapi.CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        response = CTPObjectHelper.build_response_dict(Constant.OnRspQryInstrument, pRspInfo, nRequestID, bIsLast)
        instrument = {}
        if pInstrument:
            instrument = {
                "InstrumentID": pInstrument.InstrumentID,
                "ExchangeID": pInstrument.ExchangeID,
                "InstrumentName": pInstrument.InstrumentName,
                "ExchangeInstID": pInstrument.ExchangeInstID,
                "ProductID": pInstrument.ProductID,
                "ProductClass": pInstrument.ProductClass,
                "DeliveryYear": pInstrument.DeliveryYear,
                "DeliveryMonth": pInstrument.DeliveryMonth,
                "MaxMarketOrderVolume": pInstrument.MaxMarketOrderVolume,
                "MinMarketOrderVolume": pInstrument.MinMarketOrderVolume,
                "MaxLimitOrderVolume": pInstrument.MaxLimitOrderVolume,
                "MinLimitOrderVolume": pInstrument.MinLimitOrderVolume,
                "VolumeMultiple": pInstrument.VolumeMultiple,
                "PriceTick": pInstrument.PriceTick,
                "CreateDate": pInstrument.CreateDate,
                "OpenDate": pInstrument.OpenDate,
                "ExpireDate": pInstrument.ExpireDate,
                "StartDelivDate": pInstrument.StartDelivDate,
                "EndDelivDate": pInstrument.EndDelivDate,
                "InstLifePhase": pInstrument.InstLifePhase,
                "IsTrading": pInstrument.IsTrading,
                "PositionType": pInstrument.PositionType,
                "PositionDateType": pInstrument.PositionDateType,
                "LongMarginRatio": pInstrument.LongMarginRatio,
                "ShortMarginRatio": pInstrument.ShortMarginRatio,
                "MaxMarginSideAlgorithm": pInstrument.MaxMarginSideAlgorithm,
                "UnderlyingInstrID": pInstrument.UnderlyingInstrID,
                "StrikePrice": pInstrument.StrikePrice,
                "OptionsType": pInstrument.OptionsType,
                "UnderlyingMultiple": pInstrument.UnderlyingMultiple,
                "CombinationType": pInstrument.CombinationType
            }
        response[Constant.Instrument] = instrument
        self.rsp_callback(response)

    # ReqUserPasswordUpdate
    def reqUserPasswordUpdate(self, request: dict[str, any]) -> None:
        req, requestId = CTPObjectHelper.extract_request(request, Constant.UserPasswordUpdate, tdapi.CThostFtdcUserPasswordUpdateField)
        ret = self._api.ReqUserPasswordUpdate(req, requestId)
        self.method_called(Constant.OnRspUserPasswordUpdate, ret)
    
    def OnRspUserPassowrdUpdate(self, pUserPasswordUpdate: tdapi.CThostFtdcUserPasswordUpdateField, pRspInfo: tdapi.CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        response = CTPObjectHelper.build_response_dict(Constant.OnRspUserPasswordUpdate, pRspInfo, nRequestID, bIsLast)
        userPasswordUpdate = None
        if pUserPasswordUpdate:
            userPasswordUpdate = {
                "BrokerID": pUserPasswordUpdate.BrokerID,
                "UserID": pUserPasswordUpdate.UserID,
                "OldPassword": pUserPasswordUpdate.OldPassword,
                "NewPassword": pUserPasswordUpdate.NewPassword
            }
        response[Constant.UserPasswordUpdate] = userPasswordUpdate
        self.rsp_callback(response)

    def reqOrderInsert(self, request: dict[str, any]) -> None:
        req, requestId = CTPObjectHelper.extract_request(request, Constant.InputOrder, tdapi.CThostFtdcInputOrderField)
        ret = self._api.ReqOrderInsert(req, requestId)
        self.method_called(Constant.OnRspOrderInsert, ret)
    
    def OnRspOrderInsert(self, pInputOrder: tdapi.CThostFtdcInputOrderField, pRspInfo: tdapi.CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        response = CTPObjectHelper.build_response_dict(Constant.OnRspOrderInsert, pRspInfo, nRequestID, bIsLast)
        inputOrder = None
        if pInputOrder:
            inputOrder = {
                "BrokerID": pInputOrder.BrokerID,
                "InvestorID": pInputOrder.InvestorID,
                "OrderRef": pInputOrder.OrderRef,
                "UserID": pInputOrder.UserID,
                "OrderPriceType": pInputOrder.OrderPriceType,
                "Direction": pInputOrder.Direction,
                "CombOffsetFlag": pInputOrder.CombOffsetFlag,
                "CombHedgeFlag": pInputOrder.CombHedgeFlag,
                "LimitPrice": pInputOrder.LimitPrice,
                "VolumeTotalOriginal": pInputOrder.VolumeTotalOriginal,
                "TimeCondition": pInputOrder.TimeCondition,
                "GTDDate": pInputOrder.GTDDate,
                "VolumeCondition": pInputOrder.VolumeCondition,
                "MinVolume": pInputOrder.MinVolume,
                "ContingentCondition": pInputOrder.ContingentCondition,
                "StopPrice": pInputOrder.StopPrice,
                "ForceCloseReason": pInputOrder.ForceCloseReason,
                "IsAutoSuspend": pInputOrder.IsAutoSuspend,
                "BusinessUnit": pInputOrder.BusinessUnit,
                "RequestID": pInputOrder.RequestID,
                "UserForceClose": pInputOrder.UserForceClose,
                "IsSwapOrder": pInputOrder.IsSwapOrder,
                "ExchangeID": pInputOrder.ExchangeID,
                "InvestUnitID": pInputOrder.InvestUnitID,
                "AccountID": pInputOrder.AccountID,
                "CurrencyID": pInputOrder.CurrencyID,
                "ClientID": pInputOrder.ClientID,
                "MacAddress": pInputOrder.MacAddress,
                "InstrumentID": pInputOrder.InstrumentID,
                "IPAddress": pInputOrder.IPAddress
            }
        response[Constant.InputOrder] = inputOrder
        self.rsp_callback(response)
    
    def OnErrRtnOrderInsert(self, pInputOrder: tdapi.CThostFtdcInputOrderField, pRspInfo: tdapi.CThostFtdcRspInfoField):
        response = CTPObjectHelper.build_response_dict(Constant.OnErrRtnOrderInsert, pRspInfo)
        inputOrder = None
        if pInputOrder:
            inputOrder = {
                "BrokerID": pInputOrder.BrokerID,
                "InvestorID": pInputOrder.InvestorID,
                "OrderRef": pInputOrder.OrderRef,
                "UserID": pInputOrder.UserID,
                "OrderPriceType": pInputOrder.OrderPriceType,
                "Direction": pInputOrder.Direction,
                "CombOffsetFlag": pInputOrder.CombOffsetFlag,
                "CombHedgeFlag": pInputOrder.CombHedgeFlag,
                "LimitPrice": pInputOrder.LimitPrice,
                "VolumeTotalOriginal": pInputOrder.VolumeTotalOriginal,
                "TimeCondition": pInputOrder.TimeCondition,
                "GTDDate": pInputOrder.GTDDate,
                "VolumeCondition": pInputOrder.VolumeCondition,
                "MinVolume": pInputOrder.MinVolume,
                "ContingentCondition": pInputOrder.ContingentCondition,
                "StopPrice": pInputOrder.StopPrice,
                "ForceCloseReason": pInputOrder.ForceCloseReason,
                "IsAutoSuspend": pInputOrder.IsAutoSuspend,
                "BusinessUnit": pInputOrder.BusinessUnit,
                "RequestID": pInputOrder.RequestID,
                "UserForceClose": pInputOrder.UserForceClose,
                "IsSwapOrder": pInputOrder.IsSwapOrder,
                "ExchangeID": pInputOrder.ExchangeID,
                "InvestUnitID": pInputOrder.InvestUnitID,
                "AccountID": pInputOrder.AccountID,
                "CurrencyID": pInputOrder.CurrencyID,
                "ClientID": pInputOrder.ClientID,
                "MacAddress": pInputOrder.MacAddress,
                "InstrumentID": pInputOrder.InstrumentID,
                "IPAddress": pInputOrder.IPAddress
            }
        response[Constant.InputOrder] = inputOrder
        self.rsp_callback(response)
    
    def OnRtnOrder(self, pOrder: tdapi.CThostFtdcOrderField):
        response = CTPObjectHelper.build_response_dict(Constant.OnRtnOrder)
        order = None
        if pOrder:
            order = {
                "BrokerID": pOrder.BrokerID,
                "InvestorID": pOrder.InvestorID,
                "OrderRef": pOrder.OrderRef,
                "UserID": pOrder.UserID,
                "OrderPriceType": pOrder.OrderPriceType,
                "Direction": pOrder.Direction,
                "CombOffsetFlag": pOrder.CombOffsetFlag,
                "CombHedgeFlag": pOrder.CombHedgeFlag,
                "LimitPrice": pOrder.LimitPrice,
                "VolumeTotalOriginal": pOrder.VolumeTotalOriginal,
                "TimeCondition": pOrder.TimeCondition,
                "GTDDate": pOrder.GTDDate,
                "VolumeCondition": pOrder.VolumeCondition,
                "MinVolume": pOrder.MinVolume,
                "ContingentCondition": pOrder.ContingentCondition,
                "StopPrice": pOrder.StopPrice,
                "ForceCloseReason": pOrder.ForceCloseReason,
                "IsAutoSuspend": pOrder.IsAutoSuspend,
                "BusinessUnit": pOrder.BusinessUnit,
                "RequestID": pOrder.RequestID,
                "OrderLocalID": pOrder.OrderLocalID,
                "ExchangeID": pOrder.ExchangeID,
                "ParticipantID": pOrder.ParticipantID,
                "ClientID": pOrder.ClientID,
                "TraderID": pOrder.TraderID,
                "InstallID": pOrder.InstallID,
                "OrderSubmitStatus": pOrder.OrderSubmitStatus,
                "NotifySequence": pOrder.NotifySequence,
                "TradingDay": pOrder.TradingDay,
                "SettlementID": pOrder.SettlementID,
                "OrderSysID": pOrder.OrderSysID,
                "OrderSource": pOrder.OrderSource,
                "OrderStatus": pOrder.OrderStatus,
                "OrderType": pOrder.OrderType,
                "VolumeTraded": pOrder.VolumeTraded,
                "VolumeTotal": pOrder.VolumeTotal,
                "InsertDate": pOrder.InsertDate,
                "InsertTime": pOrder.InsertTime,
                "ActiveTime": pOrder.ActiveTime,
                "SuspendTime": pOrder.SuspendTime,
                "UpdateTime": pOrder.UpdateTime,
                "CancelTime": pOrder.CancelTime,
                "ActiveTraderID": pOrder.ActiveTraderID,
                "ClearingPartID": pOrder.ClearingPartID,
                "SequenceNo": pOrder.SequenceNo,
                "FrontID": pOrder.FrontID,
                "SessionID": pOrder.SessionID,
                "UserProductInfo": pOrder.UserProductInfo,
                "StatusMsg": pOrder.StatusMsg,
                "UserForceClose": pOrder.UserForceClose,
                "ActiveUserID": pOrder.ActiveUserID,
                "BrokerOrderSeq": pOrder.BrokerOrderSeq,
                "RelativeOrderSysID": pOrder.RelativeOrderSysID,
                "ZCETotalTradedVolume": pOrder.ZCETotalTradedVolume,
                "IsSwapOrder": pOrder.IsSwapOrder,
                "BranchID": pOrder.BranchID,
                "InvestUnitID": pOrder.InvestUnitID,
                "AccountID": pOrder.AccountID,
                "CurrencyID": pOrder.CurrencyID,
                "MacAddress": pOrder.MacAddress,
                "InstrumentID": pOrder.InstrumentID,
                "ExchangeInstID": pOrder.ExchangeInstID,
                "IPAddress": pOrder.IPAddress
            }
        response[Constant.Order] = order
        self.rsp_callback(response)
    
    def OnRtnTrade(self, pTrade: tdapi.CThostFtdcTradeField):
        response = CTPObjectHelper.build_response_dict(Constant.OnRtnTrade)
        trade = None
        if pTrade:
            trade = {
                "BrokerID": pTrade.BrokerID,
                "InvestorID": pTrade.InvestorID,
                "OrderRef": pTrade.OrderRef,
                "UserID": pTrade.UserID,
                "ExchangeID": pTrade.ExchangeID,
                "TradeID": pTrade.TradeID,
                "Direction": pTrade.Direction,
                "OrderSysID": pTrade.OrderSysID,
                "ParticipantID": pTrade.ParticipantID,
                "ClientID": pTrade.ClientID,
                "TradingRole": pTrade.TradingRole,
                "OffsetFlag": pTrade.OffsetFlag,
                "HedgeFlag": pTrade.HedgeFlag,
                "Price": pTrade.Price,
                "Volume": pTrade.Volume,
                "TradeDate": pTrade.TradeDate,
                "TradeTime": pTrade.TradeTime,
                "TradeType": pTrade.TradeType,
                "PriceSource": pTrade.PriceSource,
                "TraderID": pTrade.TraderID,
                "OrderLocalID": pTrade.OrderLocalID,
                "ClearingPartID": pTrade.ClearingPartID,
                "BusinessUnit": pTrade.BusinessUnit,
                "SequenceNo": pTrade.SequenceNo,
                "TradingDay": pTrade.TradingDay,
                "SettlementID": pTrade.SettlementID,
                "BrokerOrderSeq": pTrade.BrokerOrderSeq,
                "TradeSource": pTrade.TradeSource,
                "InvestUnitID": pTrade.InvestUnitID,
                "InstrumentID": pTrade.InstrumentID,
                "ExchangeInstID": pTrade.ExchangeInstID,
            }
        response[Constant.Trade] = trade
        self.rsp_callback(response)
    
    def reqOrderAction(self, request: dict[str, any]) -> None:
        req, requestId = CTPObjectHelper.extract_request(request, Constant.InputOrderAction, tdapi.CThostFtdcInputOrderActionField)
        ret = self._api.ReqOrderAction(req, requestId)
        self.method_called(Constant.OnRspOrderAction, ret)

    def OnRspOrderAction(self, pInputOrderAction: tdapi.CThostFtdcInputOrderActionField, pRspInfo: tdapi.CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        response = CTPObjectHelper.build_response_dict(Constant.OnRspOrderAction)
        inputOrderAction = None
        if pInputOrderAction:
            inputOrderAction = {
                "BrokerID": pInputOrderAction.BrokerID,
                "InvestorID": pInputOrderAction.InvestorID,
                "OrderActionRef": pInputOrderAction.OrderActionRef,
                "OrderRef": pInputOrderAction.OrderRef,
                "RequestID": pInputOrderAction.RequestID,
                "FrontID": pInputOrderAction.FrontID,
                "SessionID": pInputOrderAction.SessionID,
                "ExchangeID": pInputOrderAction.ExchangeID,
                "OrderSysID": pInputOrderAction.OrderSysID,
                "ActionFlag": pInputOrderAction.ActionFlag,
                "LimitPrice": pInputOrderAction.LimitPrice,
                "VolumeChange": pInputOrderAction.VolumeChange,
                "UserID": pInputOrderAction.UserID,
                "InvestUnitID": pInputOrderAction.InvestUnitID,
                "MacAddress": pInputOrderAction.MacAddress,
                "InstrumentID": pInputOrderAction.InstrumentID,
                "IPAddress": pInputOrderAction.IPAddress
            }
        response[Constant.InputOrderAction] = inputOrderAction
        self.rsp_callback(response)
    
    def OnErrRtnOrderAction(self, pOrderAction: tdapi.CThostFtdcOrderActionField, pRspInfo: tdapi.CThostFtdcRspInfoField):
        response = CTPObjectHelper.build_response_dict(Constant.OnErrRtnOrderAction)
        orderAction = None
        if pOrderAction:
            orderAction = {
                "BrokerID": pOrderAction.BrokerID,
                "InvestorID": pOrderAction.InvestorID,
                "OrderActionRef": pOrderAction.OrderActionRef,
                "OrderRef": pOrderAction.OrderRef,
                "RequestID": pOrderAction.RequestID,
                "FrontID": pOrderAction.FrontID,
                "SessionID": pOrderAction.SessionID,
                "ExchangeID": pOrderAction.ExchangeID,
                "OrderSysID": pOrderAction.OrderSysID,
                "ActionFlag": pOrderAction.ActionFlag,
                "LimitPrice": pOrderAction.LimitPrice,
                "VolumeChange": pOrderAction.VolumeChange,
                "ActionDate": pOrderAction.ActionDate,
                "ActionTime": pOrderAction.ActionTime,
                "TraderID": pOrderAction.TraderID,
                "InstallID": pOrderAction.InstallID,
                "OrderLocalID": pOrderAction.OrderLocalID,
                "ActionLocalID": pOrderAction.ActionLocalID,
                "ParticipantID": pOrderAction.ParticipantID,
                "ClientID": pOrderAction.ClientID,
                "BusinessUnit": pOrderAction.BusinessUnit,
                "OrderActionStatus": pOrderAction.OrderActionStatus,
                "UserID": pOrderAction.UserID,
                "StatusMsg": pOrderAction.StatusMsg,
                "BranchID": pOrderAction.BranchID,
                "InvestUnitID": pOrderAction.InvestUnitID,
                "MacAddress": pOrderAction.MacAddress,
                "InstrumentID": pOrderAction.InstrumentID,
                "IPAddress": pOrderAction.IPAddress
            }
        response[Constant.OrderAction] = orderAction
        self.rsp_callback(response)
