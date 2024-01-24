# webctp

webctp是一个基于 [openctp-ctp](https://github.com/openctp/openctp-ctp-python) 开发的提供websocket接口的CTP服务。

# 安装及运行

## 环境搭建

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
   Port: 8081         # the listening port, default 8080
   Host: 0.0.0.0      # the bind ip address, default 0.0.0.0
   LogLevel: INFO     # NOTSET, DEBUG, INFO, WARN, ERROR, CRITICAL
   ```

## 运行

```bash
# 启动交易服务
$ python main.py --config=config_td.yaml --app_type=td
# 启动行情服务
$ python main.py --config=config_md.yaml --app_type=md
```

## 请求示例

TODO: 添加postman的请求样例

### Apifox 示例

<details>
<summary>交易登录</summary>

![](docs/img/td_login.png)
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
  "RequestID": 1  # login无需该字段
}

# 响应
{
    "MsgType": "{rsp_of_method}",
    "RspInfo": {
        "ErrorID": 0,
        "ErrorMsg": "OK"
    }
    "IsLast": true,
    "RequestID": 1,   # login无该字段
    "{response_filed}": {response_body}  # 具体参见详细文档
}
```

### 部分通用错误码说明

```bash
ErrorID="-400" ErrorMsg="参数有误"
ErrorID="-401" ErrorMsg="未登录"
ErrorID="-404" ErrorMsg="Webctp还未实现该方法"
ErrorID="-1" ErrorMsg="CTP:请求失败"
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
