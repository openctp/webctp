# webctp

webctp是一个基于 [openctp-ctp](https://github.com/openctp/openctp-ctp-python) 开发的提供websocket接口的CTP服务。

---

* [安装及运行](#安装及运行)
    * [环境搭建](#环境搭建)
    * [运行](#运行)
* [请求示例](#请求示例)
* [协议](#协议)
    * [通用协议格式](#通用协议格式)
    * [部分通用错误码说明](#部分通用错误码说明)
* [开发说明](#开发说明)
* [其他说明](#其他说明)

---

## 安装及运行

### 环境搭建

1. 准备Python环境(3.10, 其他版本未测试)
2. 克隆 webctp
   ```bash
   $ git clone https://github.com/openctp/webctp.git
   $ cd webctp
   ```
3. 安装依赖库
   ```bash
   $ pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple --trusted-host=pypi.tuna.tsinghua.edu.cn
   ```
   > :pushpin: 默认使用 openctp-ctp 6.7.2.*, 可通过 requirements.txt 进行修改。

4. 自定义配置文件  
   参考示例 config.example.yaml
   > :pushpin: 示例中行情和交易前置地址，默认配置的是 SimNow 7x24 环境， 更多 SimNow
   环境参考 [openctp环境监控](http://121.37.80.177:50080/index.html)，可根据需要变更为其他支持CTPAPI(官方实现)的柜台环境。

   创建自己的行情配置 config_md.yaml :
   ```yaml 
   TdFrontAddress: tcp://180.168.146.187:10130 # 交易前置地址
   MdFrontAddress: tcp://180.168.146.187:10131 # 行情前置地址
   BrokerID: "9999"
   AuthCode: "0000000000000000"
   AppID: simnow_client_test
   Port: 8080         # the listening port, default 8080
   Host: 0.0.0.0      # the bind ip address, default 0.0.0.0
   LogLevel: INFO     # NOTSET, DEBUG, INFO, WARN, ERROR, CRITICAL
   ```
   创建自己的交易配置 config_td.yaml :
   ```yaml 
   TdFrontAddress: tcp://180.168.146.187:10130 # 交易前置地址
   MdFrontAddress: tcp://180.168.146.187:10131 # 行情前置地址
   BrokerID: "9999"
   AuthCode: "0000000000000000"
   AppID: simnow_client_test
   Port: 8081         # the listening port, default 8081
   Host: 0.0.0.0      # the bind ip address, default 0.0.0.0
   LogLevel: INFO     # NOTSET, DEBUG, INFO, WARN, ERROR, CRITICAL
   ```

### 运行

```bash
# 启动交易服务
$ python main.py --config=config_td.yaml --app_type=td
# 启动行情服务
$ python main.py --config=config_md.yaml --app_type=md
```

## 请求示例

TODO: 添加postman的请求样例

### Apifox 示例（部分）

示例是基于 [SimNow 电信1环境](http://121.37.80.177:50080/report/Simnow7x24%BB%B7%BE%B3-%B5%E7%D0%C5process%D0%D0%C7%E9.html),
不同环境的数据存在差异，以下示例数据未必可全部通过, 根据环境调整即可。

<details>
<summary>登录</summary>

<img width="900" alt="login" src="https://github.com/openctp/webctp/assets/17944025/de9f2cd4-d3eb-4b6d-b150-d274cf4d1a01">
</details>

<details>
<summary>请求查询成交</summary>

<img width="973" alt="qry_trade" src="https://github.com/openctp/webctp/assets/17944025/a754788d-5eaa-429f-81bb-d444502ee89a">
</details>

<details>
<summary>请求查询投资者持仓</summary>

<img width="978" alt="qry_investor_position" src="https://github.com/openctp/webctp/assets/17944025/e219ccdd-d48b-4567-bbb2-6a3aa2c68ae2">
</details>

<details>
<summary>请求查询资金账户</summary>

<img width="976" alt="qry_trading_account" src="https://github.com/openctp/webctp/assets/17944025/42858761-c3fe-411c-9af7-fd248c238a77">
</details>

<details>
<summary>请求查询投资者</summary>

<img width="977" alt="qry_investor" src="https://github.com/openctp/webctp/assets/17944025/d8a7cb1f-a997-48e7-ad77-81d5f261c880">
</details>

<details>
<summary>请求查询交易编码</summary>

<img width="975" alt="qry_trading_code" src="https://github.com/openctp/webctp/assets/17944025/ee46abc5-8481-4643-98a1-e6d923e003e8">
</details>

<details>
<summary>查询合约保证金率</summary>

<img width="973" alt="qry_instrument_margin_rate" src="https://github.com/openctp/webctp/assets/17944025/96707a3f-4fef-4118-aa46-373968dac3fa">
</details>

<details>
<summary>请求查询合约手续费率</summary>

<img width="975" alt="qry_instrument_commission_rate" src="https://github.com/openctp/webctp/assets/17944025/b5e84d60-bfb9-4efd-8e4b-e50bd2e3873d">
</details>

<details>
<summary>查询期权合约手续费</summary>

</details>

<details>
<summary>查询期权交易成本</summary>

</details>

<details>
<summary>查询报单手续费率</summary>

</details>

<details>
<summary>查询交易所保证金率</summary>

<img width="976" alt="qry_exchange_margin_rate" src="https://github.com/openctp/webctp/assets/17944025/2b790cc3-8521-4713-92cb-b9a2cf1f2a48">
</details>

<details>
<summary>查询投资者持仓明细</summary>

<img width="977" alt="qry_investor_position_detail" src="https://github.com/openctp/webctp/assets/17944025/8bef07b8-5024-4499-b6a7-aa754b1d69cd">
</details>

<details>
<summary>查询行情</summary>

<img width="974" alt="qry_depth_market_data" src="https://github.com/openctp/webctp/assets/17944025/1efe7bca-7166-4c22-8d4a-750054890d6a">
</details>

<details>
<summary>查询产品</summary>

<img width="977" alt="qry_product" src="https://github.com/openctp/webctp/assets/17944025/398fc449-a6b4-487e-a62c-37314d0cee52">
</details>

<details>
<summary>查询交易所</summary>

<img width="974" alt="qry_exchange" src="https://github.com/openctp/webctp/assets/17944025/24ac101d-fadb-48e8-b0e2-8698ec802f84">
</details>

<details>
<summary>查询合约</summary>

<img width="979" alt="qry_instrument" src="https://github.com/openctp/webctp/assets/17944025/12860cda-aa82-44ce-a05b-4f666c27b3ab">
</details>

<details>
<summary>查询报单</summary>

<img width="897" alt="qr_order" src="https://github.com/openctp/webctp/assets/17944025/faad7bbb-f5fa-40c3-a4b8-f74334d3bc2a">
</details>

<details>
<summary>查询最大报单数量</summary>

<img width="898" alt="qry_max_order_volume" src="https://github.com/openctp/webctp/assets/17944025/dbb71d38-55c9-472c-9ad7-58280d894292">
</details>

<details>
<summary>用户口令变更</summary>

<img width="899" alt="update_password" src="https://github.com/openctp/webctp/assets/17944025/3c3fa526-acf0-407c-9975-488f5c2c446d">
</details>

<details>
<summary>报单录入（限价单）</summary>

<img width="900" alt="order_insert" src="https://github.com/openctp/webctp/assets/17944025/5d7edf22-e15b-4f38-9aef-6341f2d2b165">
</details>

<details>
<summary>报单撤销</summary>

<img width="898" alt="order_action" src="https://github.com/openctp/webctp/assets/17944025/a0f8117a-ec7a-4793-854e-54595c8ba885">
</details>

## 协议

### 通用协议格式

``` python
# 请求
{
  "MsgType": "{method_name}",
  "{request_field}": {
    "filed1": {value1},
    "...": "...",
    "fieldn": {valuen}
  },
  "RequestID": 1
}

# 响应
{
    "MsgType": "{rsp_of_method}",
    "RspInfo": {
        "ErrorID": 0,
        "ErrorMsg": "OK"
    },
    "IsLast": true,
    "RequestID": 1
    "{response_filed}": {response_body}  # 具体参见详细文档
}
```

### 部分通用错误码说明

```bash
ErrorID="-400" ErrorMsg="参数有误"
ErrorID="-401" ErrorMsg="未登录"
ErrorID="-404" ErrorMsg="Webctp还未实现该方法"
ErrorID="-1" ErrorMsg="CTP:请求失败"
ErrorID="-2" ErrorMsg="CTP:未处理请求超过许可数"
ErrorID="-3" ErrorMsg="CTP:每秒发送请求数超过许可数"
ErrorID="0" ErrorMsg="CTP:正确"
ErrorID="1" ErrorMsg="CTP:不在已同步状态"
ErrorID="2" ErrorMsg="CTP:会话信息不一致"
ErrorID="3" ErrorMsg="CTP:不合法的登录"
ErrorID="4" ErrorMsg="CTP:用户不活跃"
ErrorID="5" ErrorMsg="CTP:重复的登录"
ErrorID="6" ErrorMsg="CTP:还没有登录"
ErrorID="7" ErrorMsg="CTP:还没有初始化"
ErrorID="8" ErrorMsg="CTP:前置不活跃"
ErrorID="9" ErrorMsg="CTP:无此权限"
ErrorID="10" ErrorMsg="CTP:修改别人的口令"
ErrorID="11" ErrorMsg="CTP:找不到该用户"
ErrorID="12" ErrorMsg="CTP:找不到该经纪公司"
ErrorID="13" ErrorMsg="CTP:找不到投资者"
ErrorID="14" ErrorMsg="CTP:原口令不匹配"
ErrorID="15" ErrorMsg="CTP:报单字段有误"
ErrorID="16" ErrorMsg="CTP:找不到合约"
```

### 详细接口文档

[交易服务协议文档](./docs/td_protocol.md)

[行情服务协议文档](./docs/md_protocol.md)

# 开发说明

TODO

# 其他说明

* 由于精力有限，只进行了SimNow平台的简单的测试，请自行充分测试后再接入生产环境。
* 使用webctp进行实盘交易的后果完全有使用者自行承担。
