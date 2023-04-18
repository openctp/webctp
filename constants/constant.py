class CommonConstant(object):
    MessageType = "MsgType"
    RspInfo = "RspInfo"
    RequestID = "RequestID"
    IsLast = "IsLast"

    OnRspUserLogin = "OnRspUserLogin"

    ReqUserLogin = "ReqUserLogin"
    RspUserLogin = "RspUserLogin"


class MdConstant(CommonConstant):

    # MessageType
    OnRspSubMarketData = "OnRspSubMarketData"
    OnRspUnSubMarketData = "OnRspUnSubMarketData"

    # RtnMessageType
    OnRtnDepthMarketData = "OnRtnDepthMarketData"

    # Request Field
    InstrumentID = "InstrumentID"

    # Response Field
    SpecificInstrument = "SpecificInstrument"
    DepthMarketData = "DepthMarketData"


class TdConstant(CommonConstant):

    # MessageType
    OnRspUserLogin = "OnRspUserLogin"
    OnRspAuthenticate = "OnRspAuthenticate"
    OnRspQryInstrument = "OnRspQryInstrument"
    OnRspOrderInsert = "OnRspOrderInsert"

    # RequestField
    QryInstrument = "QryInstrument"

    # ResponseField
    Instrument = "Instrument"
