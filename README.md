# webctp
webctp是一个基于[ctpapi-python](https://github.com/openctp/openctp/tree/master/ctpapi-python)开发的提供websocket接口的CTP服务。
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
[交易服务协议文档](./docs/td_protocol.md)

[行情服务协议文档](./docs/md_protocol.md)
# 开发说明
TODO
