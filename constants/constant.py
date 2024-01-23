class CommonConstant(object):
    MessageType = "MsgType"
    RspInfo = "RspInfo"
    RequestID = "RequestID"
    IsLast = "IsLast"

    OnRspUserLogin = "RspUserLogin"

    ReqUserLogin = "ReqUserLogin"
    RspUserLogin = "RspUserLogin"


class MdConstant(CommonConstant):

    # MessageType
    OnRspSubMarketData = "RspSubMarketData"
    OnRspUnSubMarketData = "RspUnSubMarketData"

    # RtnMessageType
    OnRtnDepthMarketData = "RtnDepthMarketData"

    # Request Field
    InstrumentID = "InstrumentID"

    # Response Field
    SpecificInstrument = "SpecificInstrument"
    DepthMarketData = "DepthMarketData"


class TdConstant(CommonConstant):

    # MessageType
    OnRspUserLogin = "RspUserLogin"
    OnRspAuthenticate = "RspAuthenticate"
    OnRspQryInstrument = "RspQryInstrument"
    OnRspQryExchange = "RspQryExchange"
    OnRspQryProduct = "RspQryProduct"
    OnRspQryDepthMarketData = "RspQryDepthMarketData"
    OnRspQryInvestorPositionDetail = "RspQryInvestorPositionDetail"
    OnRspQryExchangeMarginRate = "RspQryExchangeMarginRate"
    OnRspQryInstrumentOrderCommRate = "RspQryInstrumentOrderCommRate"
    OnRspQryOptionInstrTradeCost = "RspQryOptionInstrTradeCost"
    OnRspQryOptionInstrCommRate = "RspQryOptionInstrCommRate"
    OnRspUserPasswordUpdate = "RspUserPasswordUpdate"
    OnRspOrderInsert = "RspOrderInsert"
    OnErrRtnOrderInsert = "ErrRtnOrderInsert"
    OnRtnOrder = "RtnOrder"
    OnRtnTrade = "RtnTrade"
    OnRspOrderAction = "RspOrderAction"
    OnErrRtnOrderAction = "ErrRtnOrderAction"
    OnRspQryMaxOrderVolume = "RspQryMaxOrderVolume"
    OnRspQryOrder = "RspQryOrder"
    OnRspQryTrade = "RspQryTrade"
    OnRspQryInvestorPosition = "RspQryInvestorPosition"
    OnRspQryTradingAccount = "RspQryTradingAccount"
    OnRspQryInvestor = "RspQryInvestor"
    OnRspQryTradingCode = "RspQryTradingCode"
    OnRspQryInstrumentMarginRate = "RspQryInstrumentMarginRate"
    OnRspQryInstrumentCommissionRate = "RspQryInstrumentCommissionRate"

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
    QryTrade = "QryTrade"
    QryInvestorPosition = "QryInvestorPosition"
    QryTradingAccount = "QryTradingAccount"
    QryInvestor = "QryInvestor"
    QryTradingCode = "QryTradingCode"
    QryInstrumentMarginRate = "QryInstrumentMarginRate"
    QryInstrumentCommissionRate = "QryInstrumentCommissionRate"

    # ResponseField
    Instrument = "Instrument"
    Order = "Order"
    Trade = "Trade"
    OrderAction = "OrderAction"
    Exchange = "Exchange"
    Product = "Product"
    InvestorPositionDetail = "InvestorPositionDetail"
    ExchangeMarginRate = "ExchangeMarginRate"
    InstrumentOrderCommRate = "InstrumentOrderCommRate"
    OptionInstrTradeCost = "OptionInstrTradeCost"
    OptionInstrCommRate = "OptionInstrCommRate"
    DepthMarketData = "DepthMarketData"
    InvestorPosition = "InvestorPosition"
    TradingAccount = "TradingAccount"
    Investor = "Investor"
    TradingCode = "TradingCode"
    InstrumentMarginRate = "InstrumentMarginRate"
    InstrumentCommissionRate = "InstrumentCommissionRate"

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
    ReqQryTrade = "ReqQryTrade"
    ReqQryInvestorPosition = "ReqQryInvestorPosition"
    ReqQryTradingAccount = "ReqQryTradingAccount"
    ReqQryInvestor = "ReqQryInvestor"
    ReqQryTradingCode = "ReqQryTradingCode"
    ReqQryInstrumentMarginRate = "ReqQryInstrumentMarginRate"
    ReqQryInstrumentCommissionRate = "ReqQryInstrumentCommissionRate"
