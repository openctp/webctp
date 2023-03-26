import time
import logging

from typing import Callable
from openctp import thosttraderapi as tdapi

from utils.config import TdConfig
from utils.ctp_object_helper import CTPObjectHelper


class TdClient(tdapi.CThostFtdcTraderSpi):
    
    def __init__(self, user_id:str, password: str, con_file_path: str):
        super().__init__()
        self._front_address:str = TdConfig.TdFrontAddress
        self._broker_id:str = TdConfig.BrokerID
        self._auth_code:str = TdConfig.AuthCode
        self._app_id:str = TdConfig.AppID
        self._user_id:str = user_id
        self._password: str = password
        self._rsp_callback: Callable[[dict[str, any]], None] = None
        self._api: tdapi.CThostFtdcTraderApi = tdapi.CThostFtdcTraderApi.CreateFtdcTraderApi(con_file_path)
    
    @property
    def rsp_callback(self) -> Callable[[dict[str, any]], None]:
        return self._rsp_callback

    @rsp_callback.setter
    def set_rsp_callback(self, callback: Callable[[dict[str, any]], None]):
        self._rsp_callback = callback
    
    def release(self) -> None:
        self._api.Release()

    def connect(self) -> None:
        self._api.RegisterSpi(self)
        self._api.SubscribePrivateTopic(tdapi.THOST_TERT_QUICK)
        self._api.SubscribePublicTopic(tdapi.THOST_TERT_QUICK)
        self._api.RegisterFront(self._front_address)
        self._api.Init()

    def OnFrontConnected(self):
        """called when connect success"""
        logging.info("OnFrontConnected")
        self.authenticate()

    def OnFrontDisconnected(self, nReason):
        """called when connection broken"""
        logging.info(f"Front disconnect, error_code={nReason}")

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
        if pRspInfo is not None:
            logging.info(f"authenticate rsp info, ErrorID: {pRspInfo.ErrorID}, ErrorMsg: {pRspInfo.ErrorMsg}")

        if pRspInfo is None or pRspInfo.ErrorID == 0:
            logging.info("authenticate success, start to login")
            self.login()
        else:
            logging.info("authenticate failed, please try again")
            self.processConnectResult("OnRspAuthenticate", pRspInfo)

    def login(self):
        req = tdapi.CThostFtdcReqUserLoginField()
        req.BrokerID = self._broker_id
        req.UserID = self._user_id
        req.Password = self._password
        req.UserProductInfo = "openctp"
        self._api.ReqUserLogin(req, 0)

    def OnRspUserLogin(self, pRspUserLogin: tdapi.CThostFtdcRspUserLoginField, pRspInfo: tdapi.CThostFtdcRspInfoField,
                       nRequestID: int, bIsLast: bool):
        """called when login responds"""
        if pRspInfo is not None:
            logging.info(f"login rsp info, ErrorID: {pRspInfo.ErrorID}, ErrorMsg: {pRspInfo.ErrorMsg}")

        if pRspInfo is None or pRspInfo.ErrorID == 0:
            logging.info("loging success, start to confirm settlement info")
            self.settlementConfirm()
            self.processConnectResult("OnRspUserLogin", pRspInfo, pRspUserLogin)
        else:
            self.processConnectResult("OnRspUserLogin", pRspInfo)
            logging.info("login failed, please try again")
    
    def settlementConfirm(self):
        req = tdapi.CThostFtdcQrySettlementInfoConfirmField()
        req.BrokerID = self._broker_id
        req.InvestorID = self._user_id
        self._api.ReqSettlementInfoConfirm(req, 0)
    
    def OnRspQrySettlementInfoConfirm(self, pSettlementInfoConfirm: tdapi.CThostFtdcSettlementInfoConfirmField, pRspInfo: tdapi.CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        logging.info("confirm settlement info success")
        if pRspInfo is not None:
            logging.info(f"settlemnt confirm rsp info, ErrorID: {pRspInfo.ErrorID}, ErrorMsg: {pRspInfo.ErrorMsg}")
    
    def processConnectResult(self, messageType: str, pRspInfo: tdapi.CThostFtdcRspInfoField, pRspUserLogin: tdapi.CThostFtdcRspUserLoginField = None):
        data = CTPObjectHelper.object_to_dict(pRspUserLogin) if pRspUserLogin else {}
        rsp = CTPObjectHelper.object_to_dict(pRspInfo) if pRspInfo else {}
        self._rsp_callback({
            "MessageType": messageType,
            "RspInfo": rsp,
            "RspUserLogin": data
        })

    def reqQryInstrument(self, request: dict[str, any], requestId: int) -> int:
        req = tdapi.CThostFtdcQryInstrumentField()
        CTPObjectHelper.dict_to_object(request["QryInstrument"], req)
        return self._api.ReqQryInstrument(req, requestId)
    
    def OnRspQryInstrument(self, pInstrument: tdapi.CThostFtdcInstrumentField, pRspInfo: tdapi.CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        data = CTPObjectHelper.object_to_dict(pInstrument)
        rsp = CTPObjectHelper.object_to_dict(pRspInfo)
        self._rsp_callback({
            "Instrument": data,
            "RspInfo": rsp,
            "RequestID": nRequestID,
            "IsLast": bIsLast
        })
