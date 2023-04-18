### 登录
```json
# 请求
{
  "MsgType": "ReqUserLogin",
  "ReqUserLogin":{
    "UserID":"028742",
    "Password":"123456"
  }
}

# 应答
{
  "MsgType": "OnRspUserLogin",
  "RspInfo":{
    "ErrorID":0,
    "ErrorMsg":"成功"
  },
  "RspUserLogin":{
    "UserID":"028742",
    "BrokerID":"9999",
    "FrontID":1,
    "SessionID":1000000,
    "MaxOrderRef":"1",
    "SystemName":"TdServer",
    "TradingDay":"20230318"
  }
}
```
### 查询期权合约手续费

```json
{
  "MsgType": "ReqQryOptionInstrCommRate",
  "OnRspQryOptionInstrTradeCost": {
      "BrokerID": "9999",
      "InvestorID": "028742",
      "InstrumentID": "m2309-C-3000"
  },
  "RequestID": 0
}

{
    "MsgType": "OnRspQryOptionInstrCommRate",
    "RspInfo": null,
    "RequestID": 3,
    "IsLast": true,
    "QryOptionInstrCommRate": {}
}
```

### 

### 查询期权交易成本 

```json
{
  "MsgType": "ReqQryOptionInstrTradeCost",
  "QryOptionInstrTradeCost": {
      "BrokerID": "9999",
      "InvestorID": "028742",
      "InstrumentID": "m2309-C-3000",
      "HedgeFlag":"1",
      "InputPrice":123.2,
      "UnderlyingPrice" : 0
  },
  "RequestID": 0
}

{
    "MsgType": "OnRspQryOptionInstrTradeCost",
    "RspInfo": null,
    "IsLast": true,
    "QryOptionInstrTradeCost": {}
}
```

### 

### 查询报单手续费 

### 

```json
{
  "MsgType": "ReqQryInstrumentOrderCommRate",
  "QryInstrumentOrderCommRate": {
      "BrokerID": "9999",
      "InvestorID": "028742",
      "InstrumentID": "m2309-C-3000"
  },
  "RequestID": 0
}

{
    "MsgType": "OnRspQryInstrumentOrderCommRate",
    "RspInfo": null,
    "IsLast": true,
    "QryInstrumentOrderCommRate": {}
}
```

### 

### 查询交易所保证金率 

### 

```json
{
  "MsgType": "ReqQryExchangeMarginRate",
  "QryExchangeMarginRate": {
      "BrokerID": "9999",
      "InvestorID": "028742",
      "InstrumentID": "m2309",
      "ExchangeID": "DCE"
  },
  "RequestID": 0
}

{
    "MsgType": "OnRspQryExchangeMarginRate",
    "RspInfo": null,
    "IsLast": true,
    "QryExchangeMarginRate": {}
}
```

### 

### 查询投资者持仓明细 

### 

```json
{
  "MsgType": "ReqQryInvestorPositionDetail",
  "QryInvestorPositionDetail": {
      "BrokerID": "9999",
      "InstrumentID": "m2309",
      "ExchangeID": "DCE"
  },
  "RequestID": 0
}

{
    "MsgType": "OnRspQryExchangeMarginRate",
    "RspInfo": null,
    "IsLast": true,
    "QryExchangeMarginRate": {}
}
```

### 

### 查询行情 

### 

```json
{
  "MsgType": "ReqQryDepthMarketData",
  "QryDepthMarketData": {
      "InstrumentID": "m2309",
      "ExchangeID": "DCE"
  },
  "RequestID": 0
}

{
    "MsgType": "OnRspQryDepthMarketData",
    "RspInfo": null,
    "QryDepthMarketData": {
        "ActionDay": "20230413",
        "AskPrice1": 21520.0,
        "AskPrice2": 1.7976931348623157e+308,
        "AskPrice3": 1.7976931348623157e+308,
        "AskPrice4": 1.7976931348623157e+308,
        "AskPrice5": 1.7976931348623157e+308,
        "AskVolume1": 1,
        "AskVolume2": 0,
        "AskVolume3": 0,
        "AskVolume4": 0,
        "AskVolume5": 0,
        "AveragePrice": 106977.77777777778,
        "BandingLowerPrice": 6.92492106609455e-310,
        "BandingUpperPrice": 6.92493101914975e-310,
        "BidPrice1": 21460.0,
        "BidPrice2": 1.7976931348623157e+308,
        "BidPrice3": 1.7976931348623157e+308,
        "BidPrice4": 1.7976931348623157e+308,
        "BidPrice5": 1.7976931348623157e+308,
        "BidVolume1": 1,
        "BidVolume2": 0,
        "BidVolume3": 0,
        "BidVolume4": 0,
        "BidVolume5": 0,
        "ClosePrice": 1.7976931348623157e+308,
        "CurrDelta": 1.7976931348623157e+308,
        "ExchangeID": "SHFE",
        "ExchangeInstID": "",
        "HighestPrice": 21505.0,
        "InstrumentID": "X\u0002\fz\u007f",
        "LastPrice": 21505.0,
        "LowerLimitPrice": 19630.0,
        "LowestPrice": 21320.0,
        "OpenInterest": 67.0,
        "OpenPrice": 21320.0,
        "PreClosePrice": 21110.0,
        "PreDelta": 0.0,
        "PreOpenInterest": 72.0,
        "PreSettlementPrice": 21110.0,
        "SettlementPrice": 1.7976931348623157e+308,
        "TradingDay": "20230414",
        "Turnover": 962800.0,
        "UpdateMillisec": 500,
        "UpdateTime": "22:08:58",
        "UpperLimitPrice": 22585.0,
        "Volume": 9,
        "reserve1": "zn2402",
        "reserve2": "zn2402"
    }
}
```

### 

### 查询产品

```json
{
  "MsgType": "ReqQryProduct",
  "QryProduct": {
    "ProductID": "m2309"
  },
  "RequestID": 0
}

{
    "MsgType": "OnRspQryProduct",
    "RspInfo": null,
    "QryProduct": {
        "CloseDealType": "0",
        "ExchangeID": "DCE",
        "ExchangeProductID": "",
        "MaxLimitOrderVolume": 1000,
        "MaxMarketOrderVolume": 1000,
        "MinLimitOrderVolume": 1,
        "MinMarketOrderVolume": 1,
        "MortgageFundUseRange": "0",
        "OpenLimitControlLevel": "\u0000",
        "OrderFreqControlLevel": "\udc9c",
        "PositionDateType": "2",
        "PositionType": "2",
        "PriceTick": 1.0,
        "ProductClass": "1",
        "ProductID": "\u0006",
        "ProductName": "\u9ec4\u5927\u8c462\u53f7",
        "TradeCurrencyID": "CNY",
        "UnderlyingMultiple": 1.7976931348623157e+308,
        "VolumeMultiple": 10,
        "reserve1": "b",
        "reserve2": ""
    }
}
```

### 



### 查询交易所

```json
{
  "MsgType": "ReqQryExchange",
  "QryExchange": {
    "ExchangeID": "DCE"
  },
  "RequestID": 0
}

{
    "MsgType": "OnRspQryExchange",
    "RspInfo": null,
    "IsLast": true,
    "QryExchange": {
        "ExchangeID": "DCE",
        "ExchangeName": "\u5927\u8fde\u5546\u54c1\u4ea4\u6613\u6240",
        "ExchangeProperty": "1"
    }
}
```
### 查询合约
```json
{
  "MsgType": "ReqQryInstrument",
  "QryInstrument": {
    "ExchangeID": "",
    "ExchangeInstID": "",
    "InstrumentID": "",
    "ProductID": ""
  },
  "RequestID": 0
}

{
  "MsgType": "OnRspQryInstrument",
  "Instrument": {
    "CombinationType": "",
    "CreateDate": "",
    "DeliveryMonth": 0,
    "DeliveryYear": 0,
    "EndDelivDate": "",
    "ExchangeID": "",
    "ExchangeInstID": "",
    "ExpireDate": "",
    "InstLifePhase": "",
    "InstrumentID": "",
    "InstrumentName": "",
    "IsTrading": 0,
    "LongMarginRatio": 1.0,
    "MaxLimitOrderVolume": 0,
    "MaxMarginSideAlgorithm": "",
    "MaxMarketOrderVolume": 0,
    "MinLimitOrderVolume": 0,
    "MinMarketOrderVolume": 0,
    "OpenDate": "",
    "OptionsType": "",
    "PositionDateType": "",
    "PositionType": "",
    "PriceTick": 1.0,
    "ProductClass": "",
    "ProductID": "",
    "ShortMarginRatio": 1.0,
    "StartDelivDate": "",
    "StrikePrice": 1.0,
    "UnderlyingInstrID": "",
    "UnderlyingMultiple": 1.0,
    "VolumeMultiple": 0
  },
  "RspInfo": {
    "ErrorID": 0,
    "ErrorMsg": ""
  },
  "RequestID": 0,
  "IsLast": false
}
```