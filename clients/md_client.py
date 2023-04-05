import logging

from typing import Callable
from openctp import thostmduserapi as mdapi

from utils import CTPObjectHelper, GlobalConfig


class Constant(object):
    OnRspUserLogin = "OnRspUserLogin"
    OnRspSubMarketData = "OnRspSubMarketData"
    OnRspUnSubMarketData = "OnRspUnSubMarketData"

    OnRtnDepthMarketData = "OnRtnDepthMarketData"

    RspUserLogin = "RspUserLogin"
    SpecificInstrument = "SpecificInstrument"
    DepthMarketData = "DepthMarketData"

    Instruments = "InstrumentID"


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
    def rsp_callback(self, callback: Callable[[dict[str, any]], None]):
        self._rsp_callback = callback
    
    def release(self) -> None:
        self._api.Release()
        self._api = None
        self._connected = False
    
    def connect(self) -> None:
        if not self._connected:
            logging.info(f"not connect start to connect {self._front_address}")
            self._api: mdapi.CThostFtdcMdApi = mdapi.CThostFtdcMdApi.CreateFtdcMdApi()
            self._api.RegisterSpi(self)
            self._api.RegisterFront(self._front_address)
            self._api.Init()
            self._connected = True
        else:
            self.login()
    
    def OnFrontConnected(self):
        logging.info("Md client connected")
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
    
    def subscribeMarketData(self, request: dict[str, any]) -> int:
        instrumentIds = request[Constant.Instruments]
        instrumentIds = list(map(lambda i: i.encode(), instrumentIds))
        logging.debug(f"subscribe data for {instrumentIds}")
        return self._api.SubscribeMarketData(instrumentIds, len(instrumentIds))
    
    def OnRspSubMarketData(self, pSpecificInstrument: mdapi.CThostFtdcSpecificInstrumentField, pRspInfo, nRequestID, bIsLast):
        response = CTPObjectHelper.build_response_dict(Constant.OnRspSubMarketData, pRspInfo, nRequestID, bIsLast)
        if pSpecificInstrument:
            response[Constant.SpecificInstrument] = pSpecificInstrument.InstrumentID
        self._rsp_callback(response)
    
    def OnRtnDepthMarketData(self, pDepthMarketData: mdapi.CThostFtdcDepthMarketDataField):
        logging.debug(f"recv market data")
        response = {
            "MsgType": Constant.OnRtnDepthMarketData,
            Constant.DepthMarketData: {
                "ActionDay": pDepthMarketData.ActionDay,
                "AskPrice1": pDepthMarketData.AskPrice1
            }
        }
        self._rsp_callback(response)

    # unsubscribe market data
    def unsubscribeMarketData(self, request: dict[str, any]) -> int:
        instrumentIds = request[Constant.Instruments]
        instrumentIds = list(map(lambda i: i.encode(), instrumentIds))
        logging.debug(f"unsubscribe data for {instrumentIds}")
        return self._api.UnSubscribeMarketData(instrumentIds, len(instrumentIds))

    # OnRspUnSubMarketData from CThostFtdcMdSpi
    def OnRspUnSubMarketData(self, pSpecificInstrument: mdapi.CThostFtdcSpecificInstrumentField, pRspInfo, nRequestID, bIsLast):
        logging.debug(f"recv unsub market data")
        response = CTPObjectHelper.build_response_dict(Constant.OnRspUnSubMarketData, pRspInfo, nRequestID, bIsLast)
        if pSpecificInstrument:
            response[Constant.SpecificInstrument] = pSpecificInstrument.InstrumentID
        self._rsp_callback(response)
