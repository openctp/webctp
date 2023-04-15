import logging
import uuid

from typing import Callable
from openctp import thostmduserapi as mdapi
from constants import CallError
from constants import MdConstant as Constant
from utils import CTPObjectHelper, GlobalConfig


class MdClient(mdapi.CThostFtdcMdSpi):

    def __init__(self, user_id, password):
        super().__init__()
        self._front_address: str = GlobalConfig.MdFrontAddress
        logging.debug(f"Md front_address: {self._front_address}")
        self._broker_id: str = GlobalConfig.BrokerID
        # If user_id not provided in the login message, then use a uuid instead.
        self._user_id: str = user_id or str(uuid.uuid4())
        self._password: str = password
        self._rsp_callback: Callable[[dict[str, any]], None] = None
        self._api: mdapi.CThostFtdcMdApi = None
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
            self._rsp_callback(response)
    
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
            self.login()
    
    def create_api(self) -> mdapi.CThostFtdcMdApi:
        con_file_path = GlobalConfig.get_con_file_path("md" + self._user_id)
        self._api: mdapi.CThostFtdcMdApi = mdapi.CThostFtdcMdApi.CreateFtdcMdApi(con_file_path)
        self._api.RegisterSpi(self)
        self._api.RegisterFront(self._front_address)
        return self._api
    
    def OnFrontConnected(self):
        logging.info("Md client connected")
        # TODO: 这样做有个bug，在出现配置错误的时候出现了疯狂的断连重连，然后每次自动重连都会做一次登陆操作，需要处理这种情况
        # 配置错误指，如使用了openctp的库去连接simnow的行情服务器，这种情况下会出现疯狂的断连重连
        self.login()
    
    def OnFrontDisconnected(self, nReason):
        logging.info(f"Md client disconnected, error_code={nReason}")
    
    def login(self):
        logging.info(f"start to login for {self._user_id}")
        req = mdapi.CThostFtdcReqUserLoginField()
        req.BrokerID = ""
        req.UserID = "" 
        req.Password = ""
        return self._api.ReqUserLogin(req, 0)
    
    def OnRspUserLogin(self, pRspUserLogin: mdapi.CThostFtdcRspUserLoginField, pRspInfo: mdapi.CThostFtdcRspInfoField, nRequestID, bIsLast):
        if pRspInfo is None or pRspInfo.ErrorID == 0:
            logging.info("Md client login success")
        else:
            logging.info("Md client login failed, please try again")
        
        response = CTPObjectHelper.build_response_dict(Constant.OnRspUserLogin, pRspInfo, nRequestID, bIsLast)
        response[Constant.RspUserLogin] = {
            "BrokerID": pRspUserLogin.BrokerID,
            "CZCETime": pRspUserLogin.CZCETime,
            "DCETime": pRspUserLogin.DCETime,
            "FFEXTime": pRspUserLogin.FFEXTime,
            "FrontID": pRspUserLogin.FrontID,
            "INETime": pRspUserLogin.INETime,
            "LoginTime": pRspUserLogin.LoginTime,
            "MaxOrderRef": pRspUserLogin.MaxOrderRef,
            "SessionID": pRspUserLogin.SessionID,
            "SHFETime": pRspUserLogin.SHFETime,
            "SystemName": pRspUserLogin.SystemName,
            "SysVersion": pRspUserLogin.SysVersion,
            "TradingDay": pRspUserLogin.TradingDay,
            "UserID": pRspUserLogin.UserID
        }
        self._rsp_callback(response)
    
    def subscribeMarketData(self, request: dict[str, any]) -> None:
        instrumentIds = request[Constant.Instruments]
        instrumentIds = list(map(lambda i: i.encode(), instrumentIds))
        logging.debug(f"subscribe data for {instrumentIds}")
        ret = self._api.SubscribeMarketData(instrumentIds, len(instrumentIds))
        self.method_called(Constant.OnRspSubMarketData, ret)
    
    def OnRspSubMarketData(self, pSpecificInstrument: mdapi.CThostFtdcSpecificInstrumentField, pRspInfo, nRequestID, bIsLast):
        response = CTPObjectHelper.build_response_dict(Constant.OnRspSubMarketData, pRspInfo, nRequestID, bIsLast)
        if pSpecificInstrument:
            response[Constant.SpecificInstrument] = {"InstrumentID" : pSpecificInstrument.InstrumentID}
        self._rsp_callback(response)
    
    def OnRtnDepthMarketData(self, pDepthMarketData: mdapi.CThostFtdcDepthMarketDataField):
        depthData = CTPObjectHelper.object_to_dict(pDepthMarketData, mdapi.CThostFtdcDepthMarketDataField)
        response = {
            Constant.MessageType: Constant.OnRtnDepthMarketData,
            Constant.DepthMarketData: depthData
        }
        self._rsp_callback(response)

    # unsubscribe market data
    def unSubscribeMarketData(self, request: dict[str, any]) -> int:
        instrumentIds = request[Constant.InstrumentID]
        instrumentIds = list(map(lambda i: i.encode(), instrumentIds))
        logging.debug(f"unsubscribe data for {instrumentIds}")
        ret = self._api.UnSubscribeMarketData(instrumentIds, len(instrumentIds))
        self.method_called(Constant.OnRspUnSubMarketData, ret)

    # OnRspUnSubMarketData from CThostFtdcMdSpi
    def OnRspUnSubMarketData(self, pSpecificInstrument: mdapi.CThostFtdcSpecificInstrumentField, pRspInfo, nRequestID, bIsLast):
        logging.debug(f"recv unsub market data")
        response = CTPObjectHelper.build_response_dict(Constant.OnRspUnSubMarketData, pRspInfo, nRequestID, bIsLast)
        if pSpecificInstrument:
            response[Constant.SpecificInstrument] = {"InstrumentID" : pSpecificInstrument.InstrumentID}
        self._rsp_callback(response)
