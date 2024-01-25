* [登录](#登录)
* [订阅行情](#订阅行情)
* [取消订阅行情](#取消订阅行情)
* [行情推送](#行情推送)

### 登录

#### 请求

行情登录不需要UserID和Password，但是建议提供UserID来作为con file的名称，否则会用随机的uuid作为con file的名称

```json
{
  "MsgType": "ReqUserLogin",
  "ReqUserLogin": {
    "UserID": "028742",
    "Password": "123456"
  }
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
    "BrokerID": "",
    "UserID": "",
    "TradingDay": "20230318",
    "SystemName": "MdServer"
  }
}
```

### 订阅行情

#### 请求

```json
{
  "MsgType": "SubscribeMarketData",
  "InstrumentID": [
    "au2305",
    "rb2305",
    "TA305"
  ]
}
```

#### 应答

```json
{
  "MsgType": "RspSubscribeMarketData",
  "SpecificInstrument": {
    "InstrumentID": "au2305"
  },
  "RspInfo": {
    "ErrorID": 0,
    "ErrorMsg": ""
  },
  "RequestID": 0,
  "IsLast": true
}
```

### 取消订阅行情

#### 请求

```json
{
  "MsgType": "UnSubscribeMarketData",
  "InstrumentID": [
    "au2305",
    "rb2305",
    "TA305"
  ]
}
```

#### 应答

```json
{
  "MsgType": "RspUnSubscribeMarketData",
  "SpecificInstrument": {
    "InstrumentID": "au2305"
  },
  "RspInfo": {
    "ErrorID": 0,
    "ErrorMsg": ""
  },
  "RequestID": 0,
  "IsLast": true
}
```

### 行情推送

```json
{
  "MsgType": "RtnDepthMarketData",
  "DepthMarketData": {
    "ActionDay": "20230410",
    "AskPrice1": 5535.000000000001,
    "AskPrice2": 0.0,
    "AskPrice3": 0.0,
    "AskPrice4": 0.0,
    "AskPrice5": 0.0,
    "AskVolume1": 114,
    "AskVolume2": 0,
    "AskVolume3": 0,
    "AskVolume4": 0,
    "AskVolume5": 0,
    "AveragePrice": 82908.07260063748,
    "BandingLowerPrice": 0.0,
    "BandingUpperPrice": 0.0,
    "BidPrice1": 5534.000000000001,
    "BidPrice2": 0.0,
    "BidPrice3": 0.0,
    "BidPrice4": 0.0,
    "BidPrice5": 0.0,
    "BidVolume1": 23,
    "BidVolume2": 0,
    "BidVolume3": 0,
    "BidVolume4": 0,
    "BidVolume5": 0,
    "ClosePrice": 0.0,
    "CurrDelta": 0.0,
    "ExchangeID": "",
    "ExchangeInstID": "",
    "HighestPrice": 5537.000000000001,
    "InstrumentID": "ag2306",
    "LastPrice": 5534.000000000001,
    "LowerLimitPrice": 5045.0,
    "LowestPrice": 5518.000000000001,
    "OpenInterest": 614690.0,
    "OpenPrice": 5531.0,
    "PreClosePrice": 5528.0,
    "PreDelta": 0.0,
    "PreOpenInterest": 613692.0,
    "PreSettlementPrice": 5544.0,
    "SettlementPrice": 0.0,
    "TradingDay": "20230411",
    "Turnover": 3511571415.0,
    "UpdateMillisec": 0,
    "UpdateTime": "21:10:58",
    "UpperLimitPrice": 6042.0,
    "Volume": 42355,
    "reserve1": "",
    "reserve2": ""
  }
}
```
