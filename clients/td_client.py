import logging

from typing import Callable
from openctp import thosttraderapi as tdapi
from constants import CallError
from constants import TdConstant as Constant
from utils import CTPObjectHelper, GlobalConfig, math_helper


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

        self._rsp_callback(response)
    
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
        self._rsp_callback(response)

    def ReqQryExchange(self, request: dict[str, any]) -> int:
        req, requestId = CTPObjectHelper.extract_request(request, Constant.QryExchange, tdapi.CThostFtdcQryExchangeField)
        ret = self._api.ReqQryExchange(req, requestId)
        self.method_called(Constant.OnRspQryExchange, ret)
    
    def OnRspQryExchange(self, pExchange: tdapi.CThostFtdcExchangeField, pRspInfo: tdapi.CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        response = CTPObjectHelper.build_response_dict(Constant.OnRspQryExchange, pRspInfo, nRequestID, bIsLast)
        result = {}
        if pExchange:
            result = {
                "ExchangeID": pExchange.ExchangeID,
                "ExchangeName": pExchange.ExchangeName.encode('unicode-escape').decode(),
                "ExchangeProperty": pExchange.ExchangeProperty
                }
        response[Constant.QryExchange] = result
        self._rsp_callback(response)

    def ReqQryProduct(self, request: dict[str, any]) -> int:
        req, requestId = CTPObjectHelper.extract_request(request, Constant.QryProduct, tdapi.CThostFtdcQryProductField)
        ret = self._api.ReqQryProduct(req, requestId)
        self.method_called(Constant.OnRspQryProduct, ret)
    
    def OnRspQryProduct(self, pProduct: tdapi.CThostFtdcProductField, pRspInfo: tdapi.CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        response = CTPObjectHelper.build_response_dict(Constant.OnRspQryProduct, pRspInfo, nRequestID, bIsLast)
        result = {}
        if pProduct:
            result = {
                "CloseDealType": pProduct.CloseDealType,
                "ExchangeID": pProduct.ExchangeID,
                "ExchangeProductID": pProduct.ExchangeProductID,
                "MaxLimitOrderVolume": pProduct.MaxLimitOrderVolume,
                "MaxMarketOrderVolume": pProduct.MaxMarketOrderVolume,
                "MinLimitOrderVolume": pProduct.MinLimitOrderVolume,
                "MinMarketOrderVolume": pProduct.MinMarketOrderVolume,
                "MortgageFundUseRange": pProduct.MortgageFundUseRange,
                "OpenLimitControlLevel": pProduct.OpenLimitControlLevel,
                "OrderFreqControlLevel": pProduct.OrderFreqControlLevel,
                "PositionDateType": pProduct.PositionDateType,
                "PositionType": pProduct.PositionType,
                "PriceTick": pProduct.PriceTick,
                "ProductClass": pProduct.ProductClass,
                "ProductID": pProduct.ProductID,
                "ProductName": pProduct.ProductName,
                "TradeCurrencyID": pProduct.TradeCurrencyID,
                "UnderlyingMultiple": pProduct.UnderlyingMultiple,
                "VolumeMultiple": pProduct.VolumeMultiple,
                "reserve1": pProduct.reserve1,
                "reserve2": pProduct.reserve2
                }
        response[Constant.QryProduct] = result
        self._rsp_callback(response)

    def ReqQryDepthMarketData(self, request: dict[str, any]) -> int:
        req, requestId = CTPObjectHelper.extract_request(request, Constant.QryDepthMarketData, tdapi.CThostFtdcQryDepthMarketDataField)
        ret = self._api.ReqQryDepthMarketData(req, requestId)
        self.method_called(Constant.OnRspQryDepthMarketData, ret)
    
    def OnRspQryDepthMarketData(self, pDepthMarketData: tdapi.CThostFtdcDepthMarketDataField, pRspInfo: tdapi.CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        response = CTPObjectHelper.build_response_dict(Constant.OnRspQryDepthMarketData, pRspInfo, nRequestID, bIsLast)
        result = {}
        if pDepthMarketData:
            result = {
                "ActionDay": pDepthMarketData.ActionDay,
                "AskPrice1": math_helper.adjust_price(pDepthMarketData.AskPrice1),
                "AskPrice2": math_helper.adjust_price(pDepthMarketData.AskPrice2),
                "AskPrice3": math_helper.adjust_price(pDepthMarketData.AskPrice3),
                "AskPrice4": math_helper.adjust_price(pDepthMarketData.AskPrice4),
                "AskPrice5": math_helper.adjust_price(pDepthMarketData.AskPrice5),
                "AskVolume1": pDepthMarketData.AskVolume1,
                "AskVolume2": pDepthMarketData.AskVolume2,
                "AskVolume3": pDepthMarketData.AskVolume3,
                "AskVolume4": pDepthMarketData.AskVolume4,
                "AskVolume5": pDepthMarketData.AskVolume5,
                "AveragePrice": math_helper.adjust_price(pDepthMarketData.AveragePrice),
                "BandingLowerPrice": math_helper.adjust_price(pDepthMarketData.BandingLowerPrice),
                "BandingUpperPrice": math_helper.adjust_price(pDepthMarketData.BandingUpperPrice),
                "BidPrice1": math_helper.adjust_price(pDepthMarketData.BidPrice1),
                "BidPrice2": math_helper.adjust_price(pDepthMarketData.BidPrice2),
                "BidPrice3": math_helper.adjust_price(pDepthMarketData.BidPrice3),
                "BidPrice4": math_helper.adjust_price(pDepthMarketData.BidPrice4),
                "BidPrice5": math_helper.adjust_price(pDepthMarketData.BidPrice5),
                "BidVolume1": pDepthMarketData.BidVolume1,
                "BidVolume2": pDepthMarketData.BidVolume2,
                "BidVolume3": pDepthMarketData.BidVolume3,
                "BidVolume4": pDepthMarketData.BidVolume4,
                "BidVolume5": pDepthMarketData.BidVolume5,
                "ClosePrice": math_helper.adjust_price(pDepthMarketData.ClosePrice),
                "CurrDelta": pDepthMarketData.CurrDelta,
                "ExchangeID": pDepthMarketData.ExchangeID,
                "ExchangeInstID": pDepthMarketData.ExchangeInstID,
                "HighestPrice": math_helper.adjust_price(pDepthMarketData.HighestPrice),
                "InstrumentID": pDepthMarketData.InstrumentID,
                "LastPrice": math_helper.adjust_price(pDepthMarketData.LastPrice),
                "LowerLimitPrice": math_helper.adjust_price(pDepthMarketData.LowerLimitPrice),
                "LowestPrice": math_helper.adjust_price(pDepthMarketData.LowestPrice),
                "OpenInterest": pDepthMarketData.OpenInterest,
                "OpenPrice": math_helper.adjust_price(pDepthMarketData.OpenPrice),
                "PreClosePrice": math_helper.adjust_price(pDepthMarketData.PreClosePrice),
                "PreDelta": pDepthMarketData.PreDelta,
                "PreOpenInterest": pDepthMarketData.PreOpenInterest,
                "PreSettlementPrice": pDepthMarketData.PreSettlementPrice,
                "SettlementPrice": math_helper.adjust_price(pDepthMarketData.SettlementPrice),
                "TradingDay": pDepthMarketData.TradingDay,
                "Turnover": pDepthMarketData.Turnover,
                "UpdateMillisec": pDepthMarketData.UpdateMillisec,
                "UpdateTime": pDepthMarketData.UpdateTime,
                "UpperLimitPrice": math_helper.adjust_price(pDepthMarketData.UpperLimitPrice),
                "Volume": pDepthMarketData.Volume,
                "reserve1": pDepthMarketData.reserve1,
                "reserve2": pDepthMarketData.reserve2
                }
        response[Constant.QryDepthMarketData] = result
        self._rsp_callback(response)

    def ReqQryInvestorPositionDetail(self, request: dict[str, any]) -> int:
        req, requestId = CTPObjectHelper.extract_request(request, Constant.QryInvestorPositionDetail, tdapi.CThostFtdcQryInvestorPositionDetailField)
        ret = self._api.ReqQryInvestorPositionDetail(req, requestId)
        self.method_called(Constant.OnRspQryInvestorPositionDetail, ret)
    
    def OnRspQryInvestorPositionDetail(self, pQryInvestorPositionDetail: tdapi.CThostFtdcInvestorPositionDetailField, pRspInfo: tdapi.CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        response = CTPObjectHelper.build_response_dict(Constant.OnRspQryInvestorPositionDetail, pRspInfo, nRequestID, bIsLast)
        result = {}
        if pQryInvestorPositionDetail:
            result = {
                "BrokerID": pQryInvestorPositionDetail.BrokerID,
                "CloseAmount": pQryInvestorPositionDetail.CloseAmount,
                "CloseProfitByDate": pQryInvestorPositionDetail.CloseProfitByDate,
                "CloseProfitByTrade": pQryInvestorPositionDetail.CloseProfitByTrade,
                "CloseVolume": pQryInvestorPositionDetail.CloseVolume,
                "CombInstrumentID": pQryInvestorPositionDetail.CombInstrumentID,
                "Direction": pQryInvestorPositionDetail.Direction,
                "ExchMargin": pQryInvestorPositionDetail.ExchMargin,
                "ExchangeID": pQryInvestorPositionDetail.ExchangeID,
                "HedgeFlag": pQryInvestorPositionDetail.HedgeFlag,
                "InstrumentID": pQryInvestorPositionDetail.InstrumentID,
                "InvestUnitID": pQryInvestorPositionDetail.InvestUnitID,
                "InvestorID": pQryInvestorPositionDetail.InvestorID,
                "LastSettlementPrice": pQryInvestorPositionDetail.LastSettlementPrice,
                "Margin": pQryInvestorPositionDetail.Margin,
                "MarginRateByMoney": pQryInvestorPositionDetail.MarginRateByMoney,
                "MarginRateByVolume": pQryInvestorPositionDetail.MarginRateByVolume,
                "OpenDate": pQryInvestorPositionDetail.OpenDate,
                "OpenPrice": pQryInvestorPositionDetail.OpenPrice,
                "PositionProfitByDate": pQryInvestorPositionDetail.PositionProfitByDate,
                "PositionProfitByTrade": pQryInvestorPositionDetail.PositionProfitByTrade,
                "SettlementID": pQryInvestorPositionDetail.SettlementID,
                "SettlementPrice": pQryInvestorPositionDetail.SettlementPrice,
                "SpecPosiType": pQryInvestorPositionDetail.SpecPosiType,
                "TimeFirstVolume": pQryInvestorPositionDetail.TimeFirstVolume,
                "TradeID": pQryInvestorPositionDetail.TradeID,
                "TradeType": pQryInvestorPositionDetail.TradeType,
                "TradingDay": pQryInvestorPositionDetail.TradingDay,
                "Volume": pQryInvestorPositionDetail.Volume,
                "reserve1": pQryInvestorPositionDetail.reserve1,
                "reserve2": pQryInvestorPositionDetail.reserve2
                }
        response[Constant.QryInvestorPositionDetail] = result
        self._rsp_callback(response)

    def ReqQryExchangeMarginRate(self, request: dict[str, any]) -> int:
        req, requestId = CTPObjectHelper.extract_request(request, Constant.QryExchangeMarginRate, tdapi.CThostFtdcQryExchangeMarginRateField)
        ret = self._api.ReqQryExchangeMarginRate(req, requestId)
        self.method_called(Constant.OnRspQryExchangeMarginRate, ret)
    
    def OnRspQryExchangeMarginRate(self, pQryExchangeMarginRate: tdapi.CThostFtdcExchangeMarginRateField, pRspInfo: tdapi.CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        response = CTPObjectHelper.build_response_dict(Constant.OnRspQryExchangeMarginRate, pRspInfo, nRequestID, bIsLast)
        result = {}
        if pQryExchangeMarginRate:
            result = {
                "BrokerID": pQryExchangeMarginRate.BrokerID,
                "ExchangeID": pQryExchangeMarginRate.ExchangeID,
                "HedgeFlag": pQryExchangeMarginRate.HedgeFlag,
                "InstrumentID": pQryExchangeMarginRate.InstrumentID,
                "LongMarginRatioByMoney": pQryExchangeMarginRate.LongMarginRatioByMoney,
                "LongMarginRatioByVolume": pQryExchangeMarginRate.LongMarginRatioByVolume,
                "ShortMarginRatioByMoney": pQryExchangeMarginRate.ShortMarginRatioByMoney,
                "ShortMarginRatioByVolume": pQryExchangeMarginRate.ShortMarginRatioByVolume,
                "reserve1": pQryExchangeMarginRate.reserve1
                }
        response[Constant.QryExchangeMarginRate] = result
        self._rsp_callback(response)

    def ReqQryInstrumentOrderCommRate(self, request: dict[str, any]) -> int:
        req, requestId = CTPObjectHelper.extract_request(request, Constant.QryInstrumentOrderCommRate, tdapi.CThostFtdcQryInstrumentOrderCommRateField)
        ret = self._api.ReqQryInstrumentOrderCommRate(req, requestId)
        self.method_called(Constant.OnRspQryInstrumentOrderCommRate, ret)
    
    def OnRspQryInstrumentOrderCommRate(self, pInstrumentOrderCommRate: tdapi.CThostFtdcInstrumentOrderCommRateField, pRspInfo: tdapi.CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        response = CTPObjectHelper.build_response_dict(Constant.OnRspQryInstrumentOrderCommRate, pRspInfo, nRequestID, bIsLast)
        result = {}
        if pInstrumentOrderCommRate:
            result = {
                "BrokerID": pInstrumentOrderCommRate.BrokerID,
                "ExchangeID": pInstrumentOrderCommRate.ExchangeID,
                "HedgeFlag": pInstrumentOrderCommRate.HedgeFlag,
                "InstrumentID": pInstrumentOrderCommRate.InstrumentID,
                "InvestUnitID": pInstrumentOrderCommRate.InvestUnitID,
                "InvestorID": pInstrumentOrderCommRate.InvestorID,
                "InvestorRange": pInstrumentOrderCommRate.InvestorRange,
                "OrderActionCommByTrade": pInstrumentOrderCommRate.OrderActionCommByTrade,
                "OrderActionCommByVolume": pInstrumentOrderCommRate.OrderActionCommByVolume,
                "OrderCommByTrade": pInstrumentOrderCommRate.OrderCommByTrade,
                "OrderCommByVolume": pInstrumentOrderCommRate.OrderCommByVolume,
                "reserve1": pInstrumentOrderCommRate.reserve1
                }
        response[Constant.QryInstrumentOrderCommRate] = result
        self._rsp_callback(response)

    def ReqQryOptionInstrTradeCost(self, request: dict[str, any]) -> int:
        req, requestId = CTPObjectHelper.extract_request(request, Constant.QryOptionInstrTradeCost, tdapi.CThostFtdcQryOptionInstrTradeCostField)
        ret = self._api.ReqQryOptionInstrTradeCost(req, requestId)
        self.method_called(Constant.OnRspQryOptionInstrTradeCost, ret)
    
    def OnRspQryOptionInstrTradeCost(self, pOptionInstrTradeCost: tdapi.CThostFtdcOptionInstrTradeCostField, pRspInfo: tdapi.CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        response = CTPObjectHelper.build_response_dict(Constant.OnRspQryOptionInstrTradeCost, pRspInfo, nRequestID, bIsLast)
        result = {}
        if pOptionInstrTradeCost:
            result = {
                "BrokerID": pOptionInstrTradeCost.BrokerID,
                "ExchFixedMargin": pOptionInstrTradeCost.ExchFixedMargin,
                "ExchMiniMargin": pOptionInstrTradeCost.ExchMiniMargin,
                "ExchangeID": pOptionInstrTradeCost.ExchangeID,
                "FixedMargin": pOptionInstrTradeCost.FixedMargin,
                "HedgeFlag": pOptionInstrTradeCost.HedgeFlag,
                "InstrumentID": pOptionInstrTradeCost.InstrumentID,
                "InvestUnitID": pOptionInstrTradeCost.InvestUnitID,
                "InvestorID": pOptionInstrTradeCost.InvestorID,
                "MiniMargin": pOptionInstrTradeCost.MiniMargin,
                "Royalty": pOptionInstrTradeCost.Royalty,
                "reserve1": pOptionInstrTradeCost.reserve1
                }
        response[Constant.QryOptionInstrTradeCost] = result
        self._rsp_callback(response)

    def ReqQryOptionInstrCommRate(self, request: dict[str, any]) -> int:
        req, requestId = CTPObjectHelper.extract_request(request, Constant.QryOptionInstrCommRate, tdapi.CThostFtdcQryOptionInstrCommRateField)
        ret = self._api.ReqQryOptionInstrCommRate(req, requestId)
        self.method_called(Constant.OnRspQryOptionInstrCommRate, ret)
    
    def OnRspQryOptionInstrCommRate(self, pQryOptionInstrCommRate: tdapi.CThostFtdcQryOptionInstrCommRateField, pRspInfo: tdapi.CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        response = CTPObjectHelper.build_response_dict(Constant.OnRspQryOptionInstrCommRate, pRspInfo, nRequestID, bIsLast)
        result = {}
        if pQryOptionInstrCommRate:
            result = {
                "BrokerID": pQryOptionInstrCommRate.BrokerID,
                "ExchangeID": pQryOptionInstrCommRate.ExchangeID,
                "InstrumentID": pQryOptionInstrCommRate.InstrumentID,
                "InvestUnitID": pQryOptionInstrCommRate.InvestUnitID,
                "InvestorID": pQryOptionInstrCommRate.InvestorID,
                "reserve1": pQryOptionInstrCommRate.reserve1
                }
        response[Constant.QryOptionInstrCommRate] = result
        self._rsp_callback(response)

