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
# 调用结果
{
  "MsgType": "ReqUserLogin",
  "Ret": 0
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
  "MsgType": "ReqQryInstrument",
  "Ret": 0
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