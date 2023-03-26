import time
from typing import Callable
from openctp import thosttraderapi as tdapi

from utils.config import TdConfig
from utils.ctp_object_helper import CTPObjectHelper


class TdClient(tdapi.CThostFtdcTraderSpi):
    
    def __init__(self, con_file_path: str):
        super().__init__()
        self._server_address = TdConfig.TdFrontAddress
        self._broker_id = TdConfig.BrokerID
        self._auth_code = TdConfig.AuthCode
        self._app_id = TdConfig.AppID
        self._rsp_callback: Callable[[dict[str, any], dict[str, any], int, bool], None] = None
        self._api: tdapi.CThostFtdcTraderApi = tdapi.CThostFtdcTraderApi.CreateFtdcTraderApi(con_file_path)
    
    @property
    def rsp_callback(self) -> Callable[[dict[str, any]], None]:
        return self._rsp_callback

    @rsp_callback.setter
    def set_rsp_callback(self, callback: Callable[[dict[str, any]], None]):
        self._rsp_callback = callback

    def connect(self, param: dict[str, any], requestId: int) -> None:
        pass

    def reqQryInstrument(self, param: dict[str, any], requestId: int) -> int:
        req = tdapi.CThostFtdcQryInstrumentField()
        CTPObjectHelper.dict_to_object(param, req)
        return self._api.ReqQryInstrument(req, requestId)
    
    def OnRspQryInstrument(self, pInstrument: tdapi.CThostFtdcInstrumentField, pRspInfo: tdapi.CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        data = CTPObjectHelper.object_to_dict(pInstrument)
        rsp = CTPObjectHelper.object_to_dict(pRspInfo)
        self._rsp_callback(data, rsp, nRequestID, bIsLast)
