# webctp
webctp是一个基于 [openctp-ctp](https://github.com/openctp/openctp-ctp-python) 开发的提供websocket接口的CTP服务。
# 安装及运行
## 环境搭建
```bash
# 安装依赖
pip install -r requirements.txt

# 安装ctpapi
# 从[ctpapi-python](https://github.com/openctp/openctp/tree/master/ctpapi-python)选择对应的版本复制到openctp目录下
```
## 运行
```bash
# Windows
# 启动交易服务
python main.py --config=config.yaml --app_type=td
# 启动行情服务
python main.py --config=config.yaml --app_type=md

# Linux
# 启动交易服务
LD_LIBRARY_PATH=./openctp python main.py --config=config.yaml --app_type=td
# 启动行情服务
LD_LIBRARY_PATH=./openctp python main.py --config=config.yaml --app_type=md
```
## 请求示例
TODO: 添加postman的请求样例
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
* 由于精力有限，只进行了SimNow/TTS模拟平台的简单的测试，请自行充分测试后再接入生产环境。
* 使用webctp进行实盘交易的后果完全有使用者自行承担。
