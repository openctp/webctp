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
    OnRspUserPasswordUpdate = "OnRspUserPasswordUpdate"
    OnRspOrderInsert = "OnRspOrderInsert"
    OnErrRtnOrderInsert = "OnErrRtnOrderInsert"
    OnRtnOrder = "OnRtnOrder"
    OnRtnTrade = "OnRtnTrade"
    OnRspOrderAction = "OnRspOrderAction"
    OnErrRtnOrderAction = "OnErrRtnOrderAction"
    OnRspQryMaxOrderVolume = "OnRspQryMaxOrderVolume"
    OnRspQryOrder = "OnRspQryOrder"

    # RequestField
    QryInstrument = "QryInstrument"
    QryExchange = "QryExchange"
    QryProduct = "QryProduct"
    QryDepthMarketData = "QryDepthMarketData"
    QryInvestorPositionDetail = "QryInvestorPositionDetail"
    QryExchangeMarginRate = "QryExchangeMarginRate"
    QryInstrumentOrderCommRate = "QryInstrumentOrderCommRate"
    QryOptionInstrTradeCost = "QryOptionInstrTradeCost"
    QryOptionInstrCommRate = "QryOptionInstrCommRate"
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
    OnRspQryExchange = "OnRspQryExchange"
    OnRspQryProduct = "OnRspQryProduct"
    OnRspQryDepthMarketData = "OnRspQryDepthMarketData"
    OnRspQryInvestorPositionDetail = "OnRspQryInvestorPositionDetail"
    OnRspQryExchangeMarginRate = "OnRspQryExchangeMarginRate"
    OnRspQryInstrumentOrderCommRate = "OnRspQryInstrumentOrderCommRate"
    OnRspQryOptionInstrTradeCost = "OnRspQryOptionInstrTradeCost"
    OnRspQryOptionInstrCommRate = "OnRspQryOptionInstrCommRate"

    # RequestMethod
    ReqQryInstrument = "ReqQryInstrument"
    ReqQryExchange = "ReqQryExchange"
    ReqQryProduct = "ReqQryProduct"
    ReqQryDepthMarketData = "ReqQryDepthMarketData"
    ReqQryInvestorPositionDetail = "ReqQryInvestorPositionDetail"
    ReqQryExchangeMarginRate = "ReqQryExchangeMarginRate"
    ReqQryInstrumentOrderCommRate = "ReqQryInstrumentOrderCommRate"
    ReqQryOptionInstrTradeCost = "ReqQryOptionInstrTradeCost"
    ReqQryOptionInstrCommRate = "ReqQryOptionInstrCommRate"
    ReqUserPasswordUpdate = "ReqUserPasswordUpdate"
    ReqOrderInsert = "ReqOrderInsert"
    ReqOrderAction = "ReqOrderAction"
    ReqQryMaxOrderVolume = "ReqQryMaxOrderVolume"
    ReqQryOrder = "ReqQryOrder"
