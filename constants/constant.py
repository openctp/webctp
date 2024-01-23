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
    OnRspQryExchange = "OnRspQryExchange"
    OnRspQryProduct = "OnRspQryProduct"
    OnRspQryDepthMarketData = "OnRspQryDepthMarketData"
    OnRspQryInvestorPositionDetail = "OnRspQryInvestorPositionDetail"
    OnRspQryExchangeMarginRate = "OnRspQryExchangeMarginRate"
    OnRspQryInstrumentOrderCommRate = "OnRspQryInstrumentOrderCommRate"
    OnRspQryOptionInstrTradeCost = "OnRspQryOptionInstrTradeCost"
    OnRspQryOptionInstrCommRate = "OnRspQryOptionInstrCommRate"
    OnRspUserPasswordUpdate = "OnRspUserPasswordUpdate"
    OnRspOrderInsert = "OnRspOrderInsert"
    OnErrRtnOrderInsert = "OnErrRtnOrderInsert"
    OnRtnOrder = "OnRtnOrder"
    OnRtnTrade = "OnRtnTrade"
    OnRspOrderAction = "OnRspOrderAction"
    OnErrRtnOrderAction = "OnErrRtnOrderAction"
    OnRspQryMaxOrderVolume = "OnRspQryMaxOrderVolume"
    OnRspQryOrder = "OnRspQryOrder"
    OnRspQryTrade = "OnRspQryTrade"
    OnRspQryInvestorPosition = "OnRspQryInvestorPosition"
    OnRspQryTradingAccount = "OnRspQryTradingAccount"
    OnRspQryInvestor = "OnRspQryInvestor"
    OnRspQryTradingCode = "OnRspQryTradingCode"
    OnRspQryInstrumentMarginRate = "OnRspQryInstrumentMarginRate"
    OnRspQryInstrumentCommissionRate = "OnRspQryInstrumentCommissionRate"

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
