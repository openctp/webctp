import logging

from typing import Callable
from openctp import thostmduserapi as mdapi

from utils import CTPObjectHelper, GlobalConfig


class MessageType(object):
    OnRspUserLogin = "OnRspUserLogin"


class MdClient(mdapi.CThostFtdcMdSpi):

    def __init__(self, user_id, password):
        super().__init__()
        self._front_address: str = GlobalConfig.MdFrontAddress
        self._broker_id: str = GlobalConfig.BrokerID
        self._user_id: str = user_id
        self._password: str = password
        self._rsp_callback: Callable[[dict[str, any]], None] = None
        self._api: mdapi.CThostFtdcMdApi = None
        self._connected: bool = False
    
    @property
    def rsp_callback(self) -> Callable[[dict[str, any]], None]:
        return self._rsp_callback

    @rsp_callback.setter
    def set_rsp_callback(self, callback: Callable[[dict[str, any]], None]):
        self._rsp_callback = self._rsp_callback
    
    def release(self) -> None:
        self._api.Release()
        self._api = None
        self._connected = False
    
    def connect(self) -> None:
        if not self._connected:
            self._api: mdapi.CThostFtdcMdApi = mdapi.CThostFtdcMdApi.CreateFtdcMdApi()
            self._api.RegisterSpi(self)
            self._api.RegisterFront(self._front_address)
            self._api.Init()
            self._connected = True
        else:
            self.login()
    
    def OnFrontConnected(self):
        logging.info("Md client connected")
    
    def OnFrontDisconnected(self, nReason):
        logging.info(f"Md client disconnected, error_code={nReason}")
    
    def login(self):
        req = mdapi.CThostFtdcReqUserLoginField()
        req.BrokerID = self._broker_id
        req.UserID = self._user_id
        req.Password = self._password
        self._api.ReqUserLogin(req, 0)
    
    def OnRspUserLogin(self, pRspUserLogin: mdapi.CThostFtdcRspUserLoginField, pRspInfo: mdapi.CThostFtdcRspInfoField, nRequestID, bIsLast):
        if pRspInfo is None or pRspInfo.ErrorID == 0:
            logging.info("Md client login success")
        else:
            logging.info("Md client login failed, please try again")
        
        response = CTPObjectHelper.build_response_dict(MessageType.OnRspUserLogin, pRspInfo, nRequestID, bIsLast)
        response["RspUserLogin"] = CTPObjectHelper.object_to_dict(pRspUserLogin)
        self._rsp_callback(response)
