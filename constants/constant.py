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
    ReqUserPasswordUpdate = "ReqUserPasswordUpdate"
    OnRspUserPasswordUpdate = "OnRspUserPasswordUpdate"
    ReqOrderInsert = "ReqOrderInsert"
    OnRspOrderInsert = "OnRspOrderInsert"
    OnErrRtnOrderInsert = "OnErrRtnOrderInsert"
    OnRtnOrder = "OnRtnOrder"
    OnRtnTrade = "OnRtnTrade"
    ReqOrderAction = "ReqOrderAction"
    OnRspOrderAction = "OnRspOrderAction"
    OnErrRtnOrderAction = "OnErrRtnOrderAction"
    ReqQryMaxOrderVolume = "ReqQryMaxOrderVolume"
    OnRspQryMaxOrderVolume = "OnRspQryMaxOrderVolume"
    ReqQryOrder = "ReqQryOrder"
    OnRspQryOrder = "OnRspQryOrder"

    # RequestField
    QryInstrument = "QryInstrument"
    UserPasswordUpdate = "UserPasswordUpdate"
    InputOrder = "InputOrder"
    InputOrderAction = "InputOrderAction"
    QryMaxOrderVolume = "QryMaxOrderVolume"
    QryOrder = "QryOrder"

    # ResponseField
    Instrument = "Instrument"
    Order = "Order"
    Trade = "Trade"
    OrderAction = "OrderAction"
