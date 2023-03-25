import time
from typing import Callable
from pydantic import dataclasses
from openctp import thosttraderapi as tdapi

@dataclasses
class ServerConfig(object):

    brokerId: str = ""
    appId: str = ""
    authCode: str = ""


class TdClient(tdapi.CThostFtdcTraderSpi):
    
    def __init__(self, userId: str, password: str):
        super().__init__()
        self._user_id = userId
        self._password = password
        self._server_config: ServerConfig = ServerConfig()
        self._rsp_callback: Callable[[dict[str, any], dict[str, any], int, bool], None] = None
        # TODO: save in a specified directory
        self._api: tdapi.CThostFtdcTraderApi = tdapi.CThostFtdcTraderApi.CreateFtdcTraderApi(userId)
    
    @property
    def rsp_callback(self) -> Callable[[dict[str, any]], None]:
        return self._rsp_callback

    @rsp_callback.setter
    def set_rsp_callback(self, callback: Callable[[dict[str, any]], None]):
        self._rsp_callback = callback

    def connect(self) -> None:
        pass

    def reqQryInstrument(self, request: dict[str, any], requestId: int) -> int:
        req = tdapi.CThostFtdcQryInstrumentField()
        req.ExchangeID = request.get("ExchangeID") or ""
        req.ExchangeInstID = request.get("ExchangeInstID") or ""
        req.InstrumentID = request.get("InstrumentID") or ""
        req.ProductID = request.get("ProductID") or ""
        return self._api.ReqQryInstrument(req, requestId)
    
    def OnRspQryInstrument(self, pInstrument: tdapi.CThostFtdcInstrumentField, pRspInfo: tdapi.CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        data = {
            "ExchangeID": pInstrument.ExchangeID
        }
        rsp = {}
        self._rsp_callback(data, rsp, nRequestID, bIsLast)
