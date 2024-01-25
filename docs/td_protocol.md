* [登录](#登录)
* [请求查询成交](#请求查询成交)
* [请求查询投资者持仓](#请求查询投资者持仓)
* [请求查询资金账户](#请求查询资金账户)
* [请求查询投资者](#请求查询投资者)
* [请求查询交易编码](#请求查询交易编码)
* [查询合约保证金率](#查询合约保证金率)
* [请求查询合约手续费率](#请求查询合约手续费率)
* [查询期权合约手续费](#查询期权合约手续费)
* [查询期权交易成本](#查询期权交易成本)
* [查询报单手续费率](#查询报单手续费率)
* [查询交易所保证金率](#查询交易所保证金率)
* [查询投资者持仓明细](#查询投资者持仓明细)
* [查询行情](#查询行情)
* [查询产品](#查询产品)
* [查询交易所](#查询交易所)
* [查询合约](#查询合约)
* [查询报单](#查询报单)
* [查询最大报单数量](#查询最大报单数量)
* [用户口令变更](#用户口令变更)
* [报单录入限价单](#报单录入限价单)
* [报单撤销](#报单撤销)
* [报单通知](#报单通知)
* [报单操作错误通](#报单操作错误通知)

### 登录

#### 请求

```json
{
  "MsgType": "ReqUserLogin",
  "ReqUserLogin": {
    "UserID": "028742",
    "Password": "123456"
  },
  "RequestID": 0
}
```

#### 应答

```json
{
  "MsgType": "RspUserLogin",
  "RspInfo": {
    "ErrorID": 0,
    "ErrorMsg": "成功"
  },
  "RspUserLogin": {
    "UserID": "028742",
    "BrokerID": "9999",
    "FrontID": 1,
    "SessionID": 1000000,
    "MaxOrderRef": "1",
    "SystemName": "TdServer",
    "TradingDay": "20230318"
  }
}
```

### 请求查询成交

#### 请求

```json
{
  "MsgType": "ReqQryTrade",
  "QryTrade": {
    "BrokerID": "9999",
    "InvestorID": "028742",
    "ExchangeID": "DCE"
  },
  "RequestID": 0
}
```

#### 应答

```json
{
  "MsgType": "RspQryTrade",
  "RspInfo": null,
  "IsLast": true,
  "Trade": null
}
```

### 请求查询投资者持仓

#### 请求

```json
{
  "MsgType": "ReqQryInvestorPosition",
  "QryInvestorPosition": {
    "BrokerID": "9999",
    "InvestorID": "028742",
    "ExchangeID": "DCE"
  },
  "RequestID": 0
}
```

#### 应答

```json
{
  "MsgType": "RspQryInvestorPosition",
  "RspInfo": null,
  "IsLast": true,
  "InvestorPosition": {
    "AbandonFrozen": 0,
    "BrokerID": "9999",
    "CashIn": 0.0,
    "CloseAmount": 0.0,
    "CloseProfit": 0.0,
    "CloseProfitByDate": 0.0,
    "CloseProfitByTrade": 0.0,
    "CloseVolume": 0,
    "CombLongFrozen": 0,
    "CombPosition": 0,
    "CombShortFrozen": 0,
    "Commission": 0.0,
    "ExchangeID": "INE",
    "ExchangeMargin": 583236.0,
    "FrozenCash": 0.0,
    "FrozenCommission": 0.0,
    "FrozenMargin": 0.0,
    "HedgeFlag": "1",
    "InstrumentID": "",
    "InvestUnitID": "",
    "InvestorID": "028742",
    "LongFrozen": 0,
    "LongFrozenAmount": 0.0,
    "MarginRateByMoney": 0.0,
    "MarginRateByVolume": 0.0,
    "OpenAmount": 0.0,
    "OpenCost": 3440900.0,
    "OpenVolume": 0,
    "PosiDirection": "2",
    "Position": 6,
    "PositionCost": 3430800.0,
    "PositionCostOffset": 0.0,
    "PositionDate": "2",
    "PositionProfit": -86400.00000000047,
    "PreMargin": 0.0,
    "PreSettlementPrice": 571.8,
    "SettlementID": 1,
    "SettlementPrice": 557.4,
    "ShortFrozen": 0,
    "ShortFrozenAmount": 0.0,
    "StrikeFrozen": 0,
    "StrikeFrozenAmount": 0.0,
    "TasPosition": 0,
    "TasPositionCost": 0.0,
    "TodayPosition": 0,
    "TradingDay": "20230421",
    "UseMargin": 583236.0,
    "YdPosition": 6,
    "YdStrikeFrozen": 0
  }
}
```

### 请求查询资金账户

#### 请求

```json
{
  "MsgType": "ReqQryTradingAccount",
  "QryTradingAccount": {
    "BrokerID": "9999",
    "InvestorID": "028742"
  },
  "RequestID": 0
}
```

#### 应答

```json
{
  "MsgType": "RspQryTradingAccount",
  "RspInfo": null,
  "IsLast": true,
  "TradingAccount": {
    "AccountID": "028742",
    "Available": 19070563.89,
    "Balance": 19653799.89,
    "BizType": "\u0000",
    "BrokerID": "9999",
    "CashIn": 0.0,
    "CloseProfit": 0.0,
    "Commission": 0.0,
    "Credit": 0.0,
    "CurrMargin": 583236.0,
    "CurrencyID": "CNY",
    "DeliveryMargin": 0.0,
    "Deposit": 0.0,
    "ExchangeDeliveryMargin": 0.0,
    "ExchangeMargin": 583236.0,
    "FrozenCash": 0.0,
    "FrozenCommission": 0.0,
    "FrozenMargin": 0.0,
    "FrozenSwap": 0.0,
    "FundMortgageAvailable": 0.0,
    "FundMortgageIn": 0.0,
    "FundMortgageOut": 0.0,
    "Interest": 0.0,
    "InterestBase": 0.0,
    "Mortgage": 0.0,
    "MortgageableFund": 19070563.89,
    "PositionProfit": -88800.0,
    "PreBalance": 19742599.89,
    "PreCredit": 0.0,
    "PreDeposit": 19742599.89,
    "PreFundMortgageIn": 0.0,
    "PreFundMortgageOut": 0.0,
    "PreMargin": 583236.0,
    "PreMortgage": 0.0,
    "RemainSwap": 0.0,
    "Reserve": 0.0,
    "ReserveBalance": 0.0,
    "SettlementID": 1,
    "SpecProductCloseProfit": 0.0,
    "SpecProductCommission": 0.0,
    "SpecProductExchangeMargin": 0.0,
    "SpecProductFrozenCommission": 0.0,
    "SpecProductFrozenMargin": 0.0,
    "SpecProductMargin": 0.0,
    "SpecProductPositionProfit": 0.0,
    "SpecProductPositionProfitByAlg": 0.0,
    "TradingDay": "20230421",
    "Withdraw": 0.0,
    "WithdrawQuota": 15256451.112000002
  }
}
```

### 请求查询投资者

#### 请求

```json
{
  "MsgType": "ReqQryInvestor",
  "QryInvestor": {
    "BrokerID": "9999",
    "InvestorID": "028742"
  },
  "RequestID": 0
}
```

#### 应答

```json
{
  "MsgType": "RspQryInvestor",
  "RspInfo": null,
  "IsLast": true,
  "QryInvestor": {
    "Address": "",
    "BrokerID": "9999",
    "CommModelID": "",
    "IdentifiedCardNo": "990287421111111195",
    "IdentifiedCardType": "1",
    "InvestorGroupID": "",
    "InvestorID": "028742",
    "InvestorName": "\u72c2\u4eba",
    "IsActive": 1,
    "MarginModelID": "",
    "Mobile": "",
    "OpenDate": "20150825",
    "Telephone": "15866668888"
  }
}
```

### 请求查询交易编码

#### 请求

```json
{
  "MsgType": "ReqQryTradingCode",
  "QryTradingCode": {
    "BrokerID": "9999",
    "InvestorID": "028742",
    "ExchangeID": "DCE"
  },
  "RequestID": 0
}
```

#### 应答

```json
{
  "MsgType": "RspQryTradingCode",
  "RspInfo": null,
  "IsLast": true,
  "QryTradingCode": {
    "BizType": "\udcb0",
    "BranchID": "",
    "BrokerID": "9999",
    "ClientID": "9999028742",
    "ClientIDType": "1",
    "ExchangeID": "DCE",
    "InvestUnitID": "",
    "InvestorID": "028742",
    "IsActive": 1
  }
}
```

### 查询合约保证金率

#### 请求

```json
{
  "MsgType": "ReqQryInstrumentMarginRate",
  "QryInstrumentMarginRate": {
    "BrokerID": "9999",
    "InvestorID": "028742",
    "InstrumentID": "m2309-C-3000"
  },
  "RequestID": 0
}
```

#### 应答

```json
{
  "MsgType": "RspQryInstrumentMarginRate",
  "RspInfo": null,
  "IsLast": true,
  "QryInstrumentMarginRate": {
    "BrokerID": "9999",
    "ExchangeID": "",
    "HedgeFlag": "1",
    "InstrumentID": "",
    "InvestUnitID": "",
    "InvestorID": "028742",
    "InvestorRange": "1",
    "IsRelative": 0,
    "LongMarginRatioByMoney": 0.17,
    "LongMarginRatioByVolume": 0.0,
    "ShortMarginRatioByMoney": 0.17,
    "ShortMarginRatioByVolume": 0.0
  }
}
```

### 请求查询合约手续费率

#### 请求

```json
{
  "MsgType": "ReqQryInstrumentCommissionRate",
  "QryInstrumentCommissionRate": {
    "BrokerID": "9999",
    "InvestorID": "028742",
    "InstrumentID": "m2309-C-3000"
  },
  "RequestID": 0
}
```

#### 应答

```json
{
  "MsgType": "RspQryInstrumentCommissionRate",
  "RspInfo": null,
  "IsLast": true,
  "QryInstrumentCommissionRate": {
    "BizType": "\u0000",
    "BrokerID": "9999",
    "CloseRatioByMoney": 0.0,
    "CloseRatioByVolume": 20.0,
    "CloseTodayRatioByMoney": 0.0,
    "CloseTodayRatioByVolume": 0.0,
    "ExchangeID": "",
    "InstrumentID": "",
    "InvestUnitID": "",
    "InvestorID": "00000000",
    "InvestorRange": "1",
    "OpenRatioByMoney": 0.0,
    "OpenRatioByVolume": 20.0
  }
}
```

### 查询期权合约手续费

#### 请求

```json
{
  "MsgType": "ReqQryOptionInstrCommRate",
  "RspQryOptionInstrTradeCost": {
    "BrokerID": "9999",
    "InvestorID": "028742",
    "InstrumentID": "m2309-C-3000"
  },
  "RequestID": 0
}
```

#### 应答

```json
{
  "MsgType": "RspQryOptionInstrCommRate",
  "RspInfo": null,
  "RequestID": 3,
  "IsLast": true,
  "QryOptionInstrCommRate": {}
}
```

### 查询期权交易成本

#### 请求

```json
{
  "MsgType": "ReqQryOptionInstrTradeCost",
  "QryOptionInstrTradeCost": {
    "BrokerID": "9999",
    "InvestorID": "028742",
    "InstrumentID": "m2309-C-3000",
    "HedgeFlag": "1",
    "InputPrice": 123.2,
    "UnderlyingPrice": 0
  },
  "RequestID": 0
}
```

#### 应答

```json
{
  "MsgType": "RspQryOptionInstrTradeCost",
  "RspInfo": null,
  "IsLast": true,
  "QryOptionInstrTradeCost": {}
}
```

### 查询报单手续费率

#### 请求

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
```

#### 应答

```json
{
  "MsgType": "RspQryInstrumentOrderCommRate",
  "RspInfo": null,
  "IsLast": true,
  "QryInstrumentOrderCommRate": {}
}
```

### 查询交易所保证金率

#### 请求

```json
{
  "MsgType": "ReqQryExchangeMarginRate",
  "QryExchangeMarginRate": {
    "BrokerID": "9999",
    "InstrumentID": "m2309",
    "ExchangeID": "DCE"
  },
  "RequestID": 0
}
```

#### 应答

```json
{
  "MsgType": "RspQryExchangeMarginRate",
  "RspInfo": null,
  "IsLast": true,
  "QryExchangeMarginRate": {}
}
```

### 查询投资者持仓明细

#### 请求

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
```

#### 应答

```json
{
  "MsgType": "RspQryExchangeMarginRate",
  "RspInfo": null,
  "IsLast": true,
  "QryExchangeMarginRate": {}
}
```

### 查询行情

#### 请求

```json
{
  "MsgType": "ReqQryDepthMarketData",
  "QryDepthMarketData": {
    "InstrumentID": "m2309",
    "ExchangeID": "DCE"
  },
  "RequestID": 0
}
```

#### 应答

```json
{
  "MsgType": "RspQryDepthMarketData",
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

### 查询产品

#### 请求

```json
{
  "MsgType": "ReqQryProduct",
  "QryProduct": {
    "ProductID": "m2309"
  },
  "RequestID": 0
}
```

#### 应答

```json
{
  "MsgType": "RspQryProduct",
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

### 查询交易所

#### 请求

```json
{
  "MsgType": "ReqQryExchange",
  "QryExchange": {
    "ExchangeID": "DCE"
  },
  "RequestID": 0
}
```

#### 应答

```json
{
  "MsgType": "RspQryExchange",
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

#### 请求

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
```

#### 应答

```json
{
  "MsgType": "RspQryInstrument",
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

### 查询报单

#### 请求

```json
{
  "MsgType": "ReqQryOrder",
  "QryOrder": {
    "InvestorID": "209025",
    "InstrumentID": "ss2407"
  },
  "RequestID": 0
}
```

#### 应答

```json
{
  "MsgType": "RspQryOrder",
  "RspInfo": null,
  "IsLast": true,
  "Order": {
    "BrokerID": "9999",
    "InvestorID": "209025",
    "OrderRef": "1",
    "UserID": "209025",
    "OrderPriceType": "2",
    "Direction": "0",
    "CombOffsetFlag": "0",
    "CombHedgeFlag": "1",
    "LimitPrice": 14265.0,
    "VolumeTotalOriginal": 1,
    "TimeCondition": "3",
    "GTDDate": "",
    "VolumeCondition": "1",
    "MinVolume": 1,
    "ContingentCondition": "1",
    "StopPrice": 0.0,
    "ForceCloseReason": "0",
    "IsAutoSuspend": 0,
    "BusinessUnit": "9999xc6",
    "RequestID": 0,
    "OrderLocalID": "       26119",
    "ExchangeID": "SHFE",
    "ParticipantID": "9999",
    "ClientID": "9999209003",
    "TraderID": "9999xc6",
    "InstallID": 1,
    "OrderSubmitStatus": "0",
    "NotifySequence": 0,
    "TradingDay": "20240126",
    "SettlementID": 1,
    "OrderSysID": "       46792",
    "OrderSource": "0",
    "OrderStatus": "0",
    "OrderType": "0",
    "VolumeTraded": 1,
    "VolumeTotal": 0,
    "InsertDate": "20240125",
    "InsertTime": "21:45:48",
    "ActiveTime": "",
    "SuspendTime": "",
    "UpdateTime": "",
    "CancelTime": "",
    "ActiveTraderID": "9999xc6",
    "ClearingPartID": "",
    "SequenceNo": 32807,
    "FrontID": 3,
    "SessionID": 1653223221,
    "UserProductInfo": "TickTrader",
    "StatusMsg": "全部成交报单已提交",
    "UserForceClose": 0,
    "ActiveUserID": "",
    "BrokerOrderSeq": 134843,
    "RelativeOrderSysID": "",
    "ZCETotalTradedVolume": 0,
    "IsSwapOrder": 0,
    "BranchID": "",
    "InvestUnitID": "",
    "AccountID": "",
    "CurrencyID": "",
    "MacAddress": "",
    "InstrumentID": "ss2407",
    "ExchangeInstID": "ss2407",
    "IPAddress": ""
  }
}
```

### 查询最大报单数量

#### 请求

```json
{
  "MsgType": "ReqQryMaxOrderVolume",
  "QryMaxOrderVolume": {
    "BrokerID": "9999",
    "InvestorID": "209025",
    "InstrumentID": "ss2407"
  },
  "RequestID": 0
}
```

#### 应答

```json
{
  "MsgType": "RspQryMaxOrderVolume",
  "RspInfo": {
    "ErrorID": 0,
    "ErrorMsg": "CTP:正确"
  },
  "IsLast": true,
  "QryMaxOrderVolume": {
    "BrokerID": "9999",
    "InvestorID": "209025",
    "InstrumentID": "ss2407",
    "ExchangeID": "",
    "InvestUnitID": "",
    "MaxVolume": 0,
    "Direction": "",
    "OffsetFlag": "",
    "HedgeFlag": ""
  }
}
```

### 用户口令变更

变更完成后，需要等一会儿才会生效

#### 请求

```json
{
  "MsgType": "ReqUserPasswordUpdate",
  "UserPasswordUpdate": {
    "BrokerID": "9999",
    "UserID": "209025",
    "OldPassword": "************",
    "NewPassword": "************"
  },
  "RequestID": 0
}
```

#### 应答

```json
{
  "MsgType": "RspUserPasswordUpdate",
  "RspInfo": {
    "ErrorID": 0,
    "ErrorMsg": "CTP:正确"
  },
  "IsLast": true,
  "UserPasswordUpdate": {
    "BrokerID": "9999",
    "UserID": "209025",
    "OldPassword": "******",
    "NewPassword": "******"
  }
}
```

### 报单录入（限价单）

#### 请求

```json
{
  "MsgType": "ReqInputOrder",
  "RequestID": 0,
  "InputOrder": {
    "BrokerID": "9999",
    "InvestorID": "209025",
    "ExchangeID": "SHFE",
    "InstrumentID": "ss2407",
    "LimitPrice": 14000,
    "OrderPriceType": "2",
    "Direction": "0",
    "CombOffsetFlag": "0",
    "CombHedgeFlag": "1",
    "VolumeTotalOriginal": 1,
    "TimeCondition": "3",
    "VolumeCondition": "1",
    "ContingentCondition": "1",
    "ForceCloseReason": "0",
    "IsAutoSuspend": 0,
    "IsSwapOrder": 0
  }
}
```

#### 应答

成功时，会有报单通知；失败时，会有应答

```json
{
  "MsgType": "RspOrderInsert",
  "RspInfo": {
    "ErrorID": 16,
    "ErrorMsg": "CTP:找不到合约"
  },
  "IsLast": true,
  "InputOrder": {
    "BrokerID": "9999",
    "InvestorID": "209025",
    "OrderRef": "",
    "UserID": "",
    "OrderPriceType": "2",
    "Direction": "0",
    "CombOffsetFlag": "0",
    "CombHedgeFlag": "1",
    "LimitPrice": 14000.0,
    "VolumeTotalOriginal": 1,
    "TimeCondition": "3",
    "GTDDate": "",
    "VolumeCondition": "1",
    "MinVolume": 0,
    "ContingentCondition": "1",
    "StopPrice": 0.0,
    "ForceCloseReason": "0",
    "IsAutoSuspend": 0,
    "BusinessUnit": "",
    "RequestID": 0,
    "UserForceClose": 0,
    "IsSwapOrder": 0,
    "ExchangeID": "",
    "InvestUnitID": "",
    "AccountID": "",
    "CurrencyID": "",
    "ClientID": "",
    "MacAddress": "",
    "InstrumentID": "ss2407000",
    "IPAddress": ""
  }
}
```

### 报单撤销

#### 请求

```json
{
  "MsgType": "ReqOrderAction",
  "RequestID": 0,
  "InputOrderAction": {
    "BrokerID": "9999",
    "InvestorID": "209025",
    "UserID": "209025",
    "ExchangeID": "SHFE",
    "InstrumentID": "ss2407",
    "ActionFlag": "0",
    "OrderSysID": "      100128"
  }
}
```

#### 应答

```json
{
  "MsgType": "RspOrderAction",
  "RspInfo": {
    "ErrorID": 25,
    "ErrorMsg": "CTP:撤单找不到相应报单"
  },
  "IsLast": true,
  "InputOrderAction": {
    "BrokerID": "9999",
    "InvestorID": "209025",
    "OrderActionRef": 0,
    "OrderRef": "",
    "RequestID": 0,
    "FrontID": 0,
    "SessionID": 0,
    "ExchangeID": "SHFE",
    "OrderSysID": " 11     1001281",
    "ActionFlag": "0",
    "LimitPrice": 0.0,
    "VolumeChange": 0,
    "UserID": "209025",
    "InvestUnitID": "",
    "MacAddress": "",
    "InstrumentID": "ss2407",
    "IPAddress": ""
  }
}
```

### 报单通知

```json
{
  "MsgType": "RtnOrder",
  "RspInfo": null,
  "Order": {
    "BrokerID": "9999",
    "InvestorID": "209025",
    "OrderRef": "           1",
    "UserID": "209025",
    "OrderPriceType": "2",
    "Direction": "0",
    "CombOffsetFlag": "0",
    "CombHedgeFlag": "1",
    "LimitPrice": 14000.0,
    "VolumeTotalOriginal": 1,
    "TimeCondition": "3",
    "GTDDate": "",
    "VolumeCondition": "1",
    "MinVolume": 0,
    "ContingentCondition": "1",
    "StopPrice": 0.0,
    "ForceCloseReason": "0",
    "IsAutoSuspend": 0,
    "BusinessUnit": "9999xc6",
    "RequestID": 0,
    "OrderLocalID": "       72524",
    "ExchangeID": "SHFE",
    "ParticipantID": "9999",
    "ClientID": "9999209003",
    "TraderID": "9999xc6",
    "InstallID": 1,
    "OrderSubmitStatus": "0",
    "NotifySequence": 0,
    "TradingDay": "20240126",
    "SettlementID": 1,
    "OrderSysID": "",
    "OrderSource": "0",
    "OrderStatus": "a",
    "OrderType": "0",
    "VolumeTraded": 0,
    "VolumeTotal": 1,
    "InsertDate": "20240125",
    "InsertTime": "23:33:29",
    "ActiveTime": "",
    "SuspendTime": "",
    "UpdateTime": "",
    "CancelTime": "",
    "ActiveTraderID": "",
    "ClearingPartID": "",
    "SequenceNo": 0,
    "FrontID": 1,
    "SessionID": 2129811508,
    "UserProductInfo": "",
    "StatusMsg": "报单已提交",
    "UserForceClose": 0,
    "ActiveUserID": "",
    "BrokerOrderSeq": 308670,
    "RelativeOrderSysID": "",
    "ZCETotalTradedVolume": 0,
    "IsSwapOrder": 0,
    "BranchID": "",
    "InvestUnitID": "",
    "AccountID": "",
    "CurrencyID": "",
    "MacAddress": "",
    "InstrumentID": "ss2407",
    "ExchangeInstID": "ss2407",
    "IPAddress": ""
  }
}
```

### 报单操作错误通知

```json
{
  "MsgType": "ErrRtnOrderAction",
  "RspInfo": {
    "ErrorID": 25,
    "ErrorMsg": "CTP:撤单找不到相应报单"
  },
  "OrderAction": {
    "BrokerID": "9999",
    "InvestorID": "209025",
    "OrderActionRef": 0,
    "OrderRef": "",
    "RequestID": 0,
    "FrontID": 0,
    "SessionID": 0,
    "ExchangeID": "SHFE",
    "OrderSysID": "     100128",
    "ActionFlag": "0",
    "LimitPrice": 0.0,
    "VolumeChange": 0,
    "ActionDate": "",
    "ActionTime": "",
    "TraderID": "",
    "InstallID": 0,
    "OrderLocalID": "",
    "ActionLocalID": "",
    "ParticipantID": "",
    "ClientID": "",
    "BusinessUnit": "",
    "OrderActionStatus": "0",
    "UserID": "209025",
    "StatusMsg": "",
    "BranchID": "",
    "InvestUnitID": "",
    "MacAddress": "",
    "InstrumentID": "ss2407",
    "IPAddress": ""
  }
}
```
