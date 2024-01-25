from pydantic import BaseModel, Field


class WebCTPRequest(BaseModel):
    MsgType: str
    RequestID: int


class ReqUserLoginField(BaseModel):
    """用户登录请求"""

    TradingDay: str = Field("", title="交易日")
    BrokerID: str = Field("", title="经纪公司代码")
    UserID: str = Field("", title="用户代码")
    Password: str = Field("", title="密码")
    UserProductInfo: str = Field("", title="用户端产品信息")
    InterfaceProductInfo: str = Field("", title="接口端产品信息")
    ProtocolInfo: str = Field("", title="协议信息")
    MacAddress: str = Field("", title="Mac地址")
    OneTimePassword: str = Field("", title="动态密码")
    reserve1: str = Field("", title="保留的无效字段")
    LoginRemark: str = Field("", title="登录备注")
    ClientIPPort: int = Field(0, title="终端IP端口")
    ClientIPAddress: str = Field("", title="终端IP地址")


class WebCTPReqUserLogin(WebCTPRequest):
    ReqUserLogin: ReqUserLoginField = Field(title="用户登录请求")


class UserLogoutField(BaseModel):
    """用户登出请求"""

    BrokerID: str = Field("", title="经纪公司代码")
    UserID: str = Field("", title="用户代码")


class WebCTPReqUserLogout(WebCTPRequest):
    UserLogout: UserLogoutField = Field(title="用户登出请求")


class ForceUserLogoutField(BaseModel):
    """强制交易员退出"""

    BrokerID: str = Field("", title="经纪公司代码")
    UserID: str = Field("", title="用户代码")


class WebCTPReqForceUserLogout(WebCTPRequest):
    ForceUserLogout: ForceUserLogoutField = Field(title="强制交易员退出")


class ReqAuthenticateField(BaseModel):
    """客户端认证请求"""

    BrokerID: str = Field("", title="经纪公司代码")
    UserID: str = Field("", title="用户代码")
    UserProductInfo: str = Field("", title="用户端产品信息")
    AuthCode: str = Field("", title="认证码")
    AppID: str = Field("", title="App代码")


class WebCTPReqAuthenticate(WebCTPRequest):
    ReqAuthenticate: ReqAuthenticateField = Field(title="客户端认证请求")


class AuthenticationInfoField(BaseModel):
    """客户端认证信息"""

    BrokerID: str = Field("", title="经纪公司代码")
    UserID: str = Field("", title="用户代码")
    UserProductInfo: str = Field("", title="用户端产品信息")
    AuthInfo: str = Field("", title="认证信息")
    IsResult: int = Field(0, title="是否为认证结果")
    AppID: str = Field("", title="App代码")
    AppType: str = Field("", title="App类型")
    reserve1: str = Field("", title="保留的无效字段")
    ClientIPAddress: str = Field("", title="终端IP地址")


class WebCTPReqAuthenticationInfo(WebCTPRequest):
    AuthenticationInfo: AuthenticationInfoField = Field(title="客户端认证信息")


class TransferHeaderField(BaseModel):
    """银期转帐报文头"""

    Version: str = Field("", title="版本号，常量，1.0")
    TradeCode: str = Field("", title="交易代码，必填")
    TradeDate: str = Field("", title="交易日期，必填，格式：yyyymmdd")
    TradeTime: str = Field("", title="交易时间，必填，格式：hhmmss")
    TradeSerial: str = Field("", title="发起方流水号，N/A")
    FutureID: str = Field("", title="期货公司代码，必填")
    BankID: str = Field("", title="银行代码，根据查询银行得到，必填")
    BankBrchID: str = Field("", title="银行分中心代码，根据查询银行得到，必填")
    OperNo: str = Field("", title="操作员，N/A")
    DeviceID: str = Field("", title="交易设备类型，N/A")
    RecordNum: str = Field("", title="记录数，N/A")
    SessionID: int = Field(0, title="会话编号，N/A")
    RequestID: int = Field(0, title="请求编号，N/A")


class WebCTPReqTransferHeader(WebCTPRequest):
    TransferHeader: TransferHeaderField = Field(title="银期转帐报文头")


class TransferBankToFutureReqField(BaseModel):
    """银行资金转期货请求，TradeCode=202001"""

    FutureAccount: str = Field("", title="期货资金账户")
    FuturePwdFlag: str = Field("", title="密码标志")
    FutureAccPwd: str = Field("", title="密码")
    TradeAmt: float = Field(0.0, title="转账金额")
    CustFee: float = Field(0.0, title="客户手续费")
    CurrencyCode: str = Field("", title="币种：RMB-人民币 USD-美圆 HKD-港元")


class WebCTPReqTransferBankToFutureReq(WebCTPRequest):
    TransferBankToFutureReq: TransferBankToFutureReqField = Field(
        title="银行资金转期货请求，TradeCode=202001")


class TransferBankToFutureRspField(BaseModel):
    """银行资金转期货请求响应"""

    RetCode: str = Field("", title="响应代码")
    RetInfo: str = Field("", title="响应信息")
    FutureAccount: str = Field("", title="资金账户")
    TradeAmt: float = Field(0.0, title="转帐金额")
    CustFee: float = Field(0.0, title="应收客户手续费")
    CurrencyCode: str = Field("", title="币种")


class WebCTPReqTransferBankToFutureRsp(WebCTPRequest):
    TransferBankToFutureRsp: TransferBankToFutureRspField = Field(
        title="银行资金转期货请求响应")


class TransferFutureToBankReqField(BaseModel):
    """期货资金转银行请求，TradeCode=202002"""

    FutureAccount: str = Field("", title="期货资金账户")
    FuturePwdFlag: str = Field("", title="密码标志")
    FutureAccPwd: str = Field("", title="密码")
    TradeAmt: float = Field(0.0, title="转账金额")
    CustFee: float = Field(0.0, title="客户手续费")
    CurrencyCode: str = Field("", title="币种：RMB-人民币 USD-美圆 HKD-港元")


class WebCTPReqTransferFutureToBankReq(WebCTPRequest):
    TransferFutureToBankReq: TransferFutureToBankReqField = Field(
        title="期货资金转银行请求，TradeCode=202002")


class TransferFutureToBankRspField(BaseModel):
    """期货资金转银行请求响应"""

    RetCode: str = Field("", title="响应代码")
    RetInfo: str = Field("", title="响应信息")
    FutureAccount: str = Field("", title="资金账户")
    TradeAmt: float = Field(0.0, title="转帐金额")
    CustFee: float = Field(0.0, title="应收客户手续费")
    CurrencyCode: str = Field("", title="币种")


class WebCTPReqTransferFutureToBankRsp(WebCTPRequest):
    TransferFutureToBankRsp: TransferFutureToBankRspField = Field(
        title="期货资金转银行请求响应")


class TransferQryBankReqField(BaseModel):
    """查询银行资金请求，TradeCode=204002"""

    FutureAccount: str = Field("", title="期货资金账户")
    FuturePwdFlag: str = Field("", title="密码标志")
    FutureAccPwd: str = Field("", title="密码")
    CurrencyCode: str = Field("", title="币种：RMB-人民币 USD-美圆 HKD-港元")


class WebCTPReqTransferQryBankReq(WebCTPRequest):
    TransferQryBankReq: TransferQryBankReqField = Field(
        title="查询银行资金请求，TradeCode=204002")


class TransferQryBankRspField(BaseModel):
    """查询银行资金请求响应"""

    RetCode: str = Field("", title="响应代码")
    RetInfo: str = Field("", title="响应信息")
    FutureAccount: str = Field("", title="资金账户")
    TradeAmt: float = Field(0.0, title="银行余额")
    UseAmt: float = Field(0.0, title="银行可用余额")
    FetchAmt: float = Field(0.0, title="银行可取余额")
    CurrencyCode: str = Field("", title="币种")


class WebCTPReqTransferQryBankRsp(WebCTPRequest):
    TransferQryBankRsp: TransferQryBankRspField = Field(
        title="查询银行资金请求响应")


class TransferQryDetailReqField(BaseModel):
    """查询银行交易明细请求，TradeCode=204999"""

    FutureAccount: str = Field("", title="期货资金账户")


class WebCTPReqTransferQryDetailReq(WebCTPRequest):
    TransferQryDetailReq: TransferQryDetailReqField = Field(
        title="查询银行交易明细请求，TradeCode=204999")


class TransferQryDetailRspField(BaseModel):
    """查询银行交易明细请求响应"""

    TradeDate: str = Field("", title="交易日期")
    TradeTime: str = Field("", title="交易时间")
    TradeCode: str = Field("", title="交易代码")
    FutureSerial: int = Field(0, title="期货流水号")
    FutureID: str = Field("", title="期货公司代码")
    FutureAccount: str = Field("", title="资金帐号")
    BankSerial: int = Field(0, title="银行流水号")
    BankID: str = Field("", title="银行代码")
    BankBrchID: str = Field("", title="银行分中心代码")
    BankAccount: str = Field("", title="银行账号")
    CertCode: str = Field("", title="证件号码")
    CurrencyCode: str = Field("", title="货币代码")
    TxAmount: float = Field(0.0, title="发生金额")
    Flag: str = Field("", title="有效标志")


class WebCTPReqTransferQryDetailRsp(WebCTPRequest):
    TransferQryDetailRsp: TransferQryDetailRspField = Field(
        title="查询银行交易明细请求响应")


class ExchangeField(BaseModel):
    """交易所"""

    ExchangeID: str = Field("", title="交易所代码")
    ExchangeName: str = Field("", title="交易所名称")
    ExchangeProperty: str = Field("", title="交易所属性")


class WebCTPReqExchange(WebCTPRequest):
    Exchange: ExchangeField = Field(title="交易所")


class ProductField(BaseModel):
    """产品"""

    reserve1: str = Field("", title="保留的无效字段")
    ProductName: str = Field("", title="产品名称")
    ExchangeID: str = Field("", title="交易所代码")
    ProductClass: str = Field("", title="产品类型")
    VolumeMultiple: int = Field(0, title="合约数量乘数")
    PriceTick: float = Field(0.0, title="最小变动价位")
    MaxMarketOrderVolume: int = Field(0, title="市价单最大下单量")
    MinMarketOrderVolume: int = Field(0, title="市价单最小下单量")
    MaxLimitOrderVolume: int = Field(0, title="限价单最大下单量")
    MinLimitOrderVolume: int = Field(0, title="限价单最小下单量")
    PositionType: str = Field("", title="持仓类型")
    PositionDateType: str = Field("", title="持仓日期类型")
    CloseDealType: str = Field("", title="平仓处理类型")
    TradeCurrencyID: str = Field("", title="交易币种类型")
    MortgageFundUseRange: str = Field("", title="质押资金可用范围")
    reserve2: str = Field("", title="保留的无效字段")
    UnderlyingMultiple: float = Field(0.0, title="合约基础商品乘数")
    ProductID: str = Field("", title="产品代码")
    ExchangeProductID: str = Field("", title="交易所产品代码")
    OpenLimitControlLevel: str = Field("", title="开仓量限制粒度")
    OrderFreqControlLevel: str = Field("", title="报单频率控制粒度")


class WebCTPReqProduct(WebCTPRequest):
    Product: ProductField = Field(title="产品")


class InstrumentField(BaseModel):
    """合约"""

    reserve1: str = Field("", title="保留的无效字段")
    ExchangeID: str = Field("", title="交易所代码")
    InstrumentName: str = Field("", title="合约名称")
    reserve2: str = Field("", title="保留的无效字段")
    reserve3: str = Field("", title="保留的无效字段")
    ProductClass: str = Field("", title="产品类型")
    DeliveryYear: int = Field(0, title="交割年份")
    DeliveryMonth: int = Field(0, title="交割月")
    MaxMarketOrderVolume: int = Field(0, title="市价单最大下单量")
    MinMarketOrderVolume: int = Field(0, title="市价单最小下单量")
    MaxLimitOrderVolume: int = Field(0, title="限价单最大下单量")
    MinLimitOrderVolume: int = Field(0, title="限价单最小下单量")
    VolumeMultiple: int = Field(0, title="合约数量乘数")
    PriceTick: float = Field(0.0, title="最小变动价位")
    CreateDate: str = Field("", title="创建日")
    OpenDate: str = Field("", title="上市日")
    ExpireDate: str = Field("", title="到期日")
    StartDelivDate: str = Field("", title="开始交割日")
    EndDelivDate: str = Field("", title="结束交割日")
    InstLifePhase: str = Field("", title="合约生命周期状态")
    IsTrading: int = Field(0, title="当前是否交易")
    PositionType: str = Field("", title="持仓类型")
    PositionDateType: str = Field("", title="持仓日期类型")
    LongMarginRatio: float = Field(0.0, title="多头保证金率")
    ShortMarginRatio: float = Field(0.0, title="空头保证金率")
    MaxMarginSideAlgorithm: str = Field("", title="是否使用大额单边保证金算法")
    reserve4: str = Field("", title="保留的无效字段")
    StrikePrice: float = Field(0.0, title="执行价")
    OptionsType: str = Field("", title="期权类型")
    UnderlyingMultiple: float = Field(0.0, title="合约基础商品乘数")
    CombinationType: str = Field("", title="组合类型")
    InstrumentID: str = Field("", title="合约代码")
    ExchangeInstID: str = Field("", title="合约在交易所的代码")
    ProductID: str = Field("", title="产品代码")
    UnderlyingInstrID: str = Field("", title="基础商品代码")


class WebCTPReqInstrument(WebCTPRequest):
    Instrument: InstrumentField = Field(title="合约")


class BrokerField(BaseModel):
    """经纪公司"""

    BrokerID: str = Field("", title="经纪公司代码")
    BrokerAbbr: str = Field("", title="经纪公司简称")
    BrokerName: str = Field("", title="经纪公司名称")
    IsActive: int = Field(0, title="是否活跃")


class WebCTPReqBroker(WebCTPRequest):
    Broker: BrokerField = Field(title="经纪公司")


class TraderField(BaseModel):
    """交易所交易员"""

    ExchangeID: str = Field("", title="交易所代码")
    TraderID: str = Field("", title="交易所交易员代码")
    ParticipantID: str = Field("", title="会员代码")
    Password: str = Field("", title="密码")
    InstallCount: int = Field(0, title="安装数量")
    BrokerID: str = Field("", title="经纪公司代码")
    OrderCancelAlg: str = Field("", title="撤单时选择席位算法")
    TradeInstallCount: int = Field(0, title="交易报盘安装数量")
    MDInstallCount: int = Field(0, title="行情报盘安装数量")


class WebCTPReqTrader(WebCTPRequest):
    Trader: TraderField = Field(title="交易所交易员")


class InvestorField(BaseModel):
    """投资者"""

    InvestorID: str = Field("", title="投资者代码")
    BrokerID: str = Field("", title="经纪公司代码")
    InvestorGroupID: str = Field("", title="投资者分组代码")
    InvestorName: str = Field("", title="投资者名称")
    IdentifiedCardType: str = Field("", title="证件类型")
    IdentifiedCardNo: str = Field("", title="证件号码")
    IsActive: int = Field(0, title="是否活跃")
    Telephone: str = Field("", title="联系电话")
    Address: str = Field("", title="通讯地址")
    OpenDate: str = Field("", title="开户日期")
    Mobile: str = Field("", title="手机")
    CommModelID: str = Field("", title="手续费率模板代码")
    MarginModelID: str = Field("", title="保证金率模板代码")
    IsOrderFreq: str = Field("", title="是否频率控制")
    IsOpenVolLimit: str = Field("", title="是否开仓限制")


class WebCTPReqInvestor(WebCTPRequest):
    Investor: InvestorField = Field(title="投资者")


class TradingCodeField(BaseModel):
    """交易编码"""

    InvestorID: str = Field("", title="投资者代码")
    BrokerID: str = Field("", title="经纪公司代码")
    ExchangeID: str = Field("", title="交易所代码")
    ClientID: str = Field("", title="客户代码")
    IsActive: int = Field(0, title="是否活跃")
    ClientIDType: str = Field("", title="交易编码类型")
    BranchID: str = Field("", title="营业部编号")
    BizType: str = Field("", title="业务类型")
    InvestUnitID: str = Field("", title="投资单元代码")


class WebCTPReqTradingCode(WebCTPRequest):
    TradingCode: TradingCodeField = Field(title="交易编码")


class PartBrokerField(BaseModel):
    """会员编码和经纪公司编码对照表"""

    BrokerID: str = Field("", title="经纪公司代码")
    ExchangeID: str = Field("", title="交易所代码")
    ParticipantID: str = Field("", title="会员代码")
    IsActive: int = Field(0, title="是否活跃")


class WebCTPReqPartBroker(WebCTPRequest):
    PartBroker: PartBrokerField = Field(title="会员编码和经纪公司编码对照表")


class SuperUserField(BaseModel):
    """管理用户"""

    UserID: str = Field("", title="用户代码")
    UserName: str = Field("", title="用户名称")
    Password: str = Field("", title="密码")
    IsActive: int = Field(0, title="是否活跃")


class WebCTPReqSuperUser(WebCTPRequest):
    SuperUser: SuperUserField = Field(title="管理用户")


class SuperUserFunctionField(BaseModel):
    """管理用户功能权限"""

    UserID: str = Field("", title="用户代码")
    FunctionCode: str = Field("", title="功能代码")


class WebCTPReqSuperUserFunction(WebCTPRequest):
    SuperUserFunction: SuperUserFunctionField = Field(title="管理用户功能权限")


class InvestorGroupField(BaseModel):
    """投资者组"""

    BrokerID: str = Field("", title="经纪公司代码")
    InvestorGroupID: str = Field("", title="投资者分组代码")
    InvestorGroupName: str = Field("", title="投资者分组名称")


class WebCTPReqInvestorGroup(WebCTPRequest):
    InvestorGroup: InvestorGroupField = Field(title="投资者组")


class TradingAccountField(BaseModel):
    """资金账户"""

    BrokerID: str = Field("", title="经纪公司代码")
    AccountID: str = Field("", title="投资者帐号")
    PreMortgage: float = Field(0.0, title="上次质押金额")
    PreCredit: float = Field(0.0, title="上次信用额度")
    PreDeposit: float = Field(0.0, title="上次存款额")
    PreBalance: float = Field(0.0, title="上次结算准备金")
    PreMargin: float = Field(0.0, title="上次占用的保证金")
    InterestBase: float = Field(0.0, title="利息基数")
    Interest: float = Field(0.0, title="利息收入")
    Deposit: float = Field(0.0, title="入金金额")
    Withdraw: float = Field(0.0, title="出金金额")
    FrozenMargin: float = Field(0.0, title="冻结的保证金")
    FrozenCash: float = Field(0.0, title="冻结的资金")
    FrozenCommission: float = Field(0.0, title="冻结的手续费")
    CurrMargin: float = Field(0.0, title="当前保证金总额")
    CashIn: float = Field(0.0, title="资金差额")
    Commission: float = Field(0.0, title="手续费")
    CloseProfit: float = Field(0.0, title="平仓盈亏")
    PositionProfit: float = Field(0.0, title="持仓盈亏")
    Balance: float = Field(0.0, title="期货结算准备金")
    Available: float = Field(0.0, title="可用资金")
    WithdrawQuota: float = Field(0.0, title="可取资金")
    Reserve: float = Field(0.0, title="基本准备金")
    TradingDay: str = Field("", title="交易日")
    SettlementID: int = Field(0, title="结算编号")
    Credit: float = Field(0.0, title="信用额度")
    Mortgage: float = Field(0.0, title="质押金额")
    ExchangeMargin: float = Field(0.0, title="交易所保证金")
    DeliveryMargin: float = Field(0.0, title="投资者交割保证金")
    ExchangeDeliveryMargin: float = Field(0.0, title="交易所交割保证金")
    ReserveBalance: float = Field(0.0, title="保底期货结算准备金")
    CurrencyID: str = Field("", title="币种代码")
    PreFundMortgageIn: float = Field(0.0, title="上次货币质入金额")
    PreFundMortgageOut: float = Field(0.0, title="上次货币质出金额")
    FundMortgageIn: float = Field(0.0, title="货币质入金额")
    FundMortgageOut: float = Field(0.0, title="货币质出金额")
    FundMortgageAvailable: float = Field(0.0, title="货币质押余额")
    MortgageableFund: float = Field(0.0, title="可质押货币金额")
    SpecProductMargin: float = Field(0.0, title="特殊产品占用保证金")
    SpecProductFrozenMargin: float = Field(0.0, title="特殊产品冻结保证金")
    SpecProductCommission: float = Field(0.0, title="特殊产品手续费")
    SpecProductFrozenCommission: float = Field(0.0, title="特殊产品冻结手续费")
    SpecProductPositionProfit: float = Field(0.0, title="特殊产品持仓盈亏")
    SpecProductCloseProfit: float = Field(0.0, title="特殊产品平仓盈亏")
    SpecProductPositionProfitByAlg: float = Field(0.0,
                                                  title="根据持仓盈亏算法计算的特殊产品持仓盈亏")
    SpecProductExchangeMargin: float = Field(0.0, title="特殊产品交易所保证金")
    BizType: str = Field("", title="业务类型")
    FrozenSwap: float = Field(0.0, title="延时换汇冻结金额")
    RemainSwap: float = Field(0.0, title="剩余换汇额度")


class WebCTPReqTradingAccount(WebCTPRequest):
    TradingAccount: TradingAccountField = Field(title="资金账户")


class InvestorPositionField(BaseModel):
    """投资者持仓"""

    reserve1: str = Field("", title="保留的无效字段")
    BrokerID: str = Field("", title="经纪公司代码")
    InvestorID: str = Field("", title="投资者代码")
    PosiDirection: str = Field("", title="持仓多空方向")
    HedgeFlag: str = Field("", title="投机套保标志")
    PositionDate: str = Field("", title="持仓日期")
    YdPosition: int = Field(0, title="上日持仓")
    Position: int = Field(0, title="今日持仓")
    LongFrozen: int = Field(0, title="多头冻结")
    ShortFrozen: int = Field(0, title="空头冻结")
    LongFrozenAmount: float = Field(0.0, title="开仓冻结金额")
    ShortFrozenAmount: float = Field(0.0, title="开仓冻结金额")
    OpenVolume: int = Field(0, title="开仓量")
    CloseVolume: int = Field(0, title="平仓量")
    OpenAmount: float = Field(0.0, title="开仓金额")
    CloseAmount: float = Field(0.0, title="平仓金额")
    PositionCost: float = Field(0.0, title="持仓成本")
    PreMargin: float = Field(0.0, title="上次占用的保证金")
    UseMargin: float = Field(0.0, title="占用的保证金")
    FrozenMargin: float = Field(0.0, title="冻结的保证金")
    FrozenCash: float = Field(0.0, title="冻结的资金")
    FrozenCommission: float = Field(0.0, title="冻结的手续费")
    CashIn: float = Field(0.0, title="资金差额")
    Commission: float = Field(0.0, title="手续费")
    CloseProfit: float = Field(0.0, title="平仓盈亏")
    PositionProfit: float = Field(0.0, title="持仓盈亏")
    PreSettlementPrice: float = Field(0.0, title="上次结算价")
    SettlementPrice: float = Field(0.0, title="本次结算价")
    TradingDay: str = Field("", title="交易日")
    SettlementID: int = Field(0, title="结算编号")
    OpenCost: float = Field(0.0, title="开仓成本")
    ExchangeMargin: float = Field(0.0, title="交易所保证金")
    CombPosition: int = Field(0, title="组合成交形成的持仓")
    CombLongFrozen: int = Field(0, title="组合多头冻结")
    CombShortFrozen: int = Field(0, title="组合空头冻结")
    CloseProfitByDate: float = Field(0.0, title="逐日盯市平仓盈亏")
    CloseProfitByTrade: float = Field(0.0, title="逐笔对冲平仓盈亏")
    TodayPosition: int = Field(0, title="今日持仓")
    MarginRateByMoney: float = Field(0.0, title="保证金率")
    MarginRateByVolume: float = Field(0.0, title="保证金率(按手数)")
    StrikeFrozen: int = Field(0, title="执行冻结")
    StrikeFrozenAmount: float = Field(0.0, title="执行冻结金额")
    AbandonFrozen: int = Field(0, title="放弃执行冻结")
    ExchangeID: str = Field("", title="交易所代码")
    YdStrikeFrozen: int = Field(0, title="执行冻结的昨仓")
    InvestUnitID: str = Field("", title="投资单元代码")
    PositionCostOffset: float = Field(0.0, title="持仓成本差值")
    TasPosition: int = Field(0, title="tas持仓手数")
    TasPositionCost: float = Field(0.0, title="tas持仓成本")
    InstrumentID: str = Field("", title="合约代码")


class WebCTPReqInvestorPosition(WebCTPRequest):
    InvestorPosition: InvestorPositionField = Field(title="投资者持仓")


class InstrumentMarginRateField(BaseModel):
    """合约保证金率"""

    reserve1: str = Field("", title="保留的无效字段")
    InvestorRange: str = Field("", title="投资者范围")
    BrokerID: str = Field("", title="经纪公司代码")
    InvestorID: str = Field("", title="投资者代码")
    HedgeFlag: str = Field("", title="投机套保标志")
    LongMarginRatioByMoney: float = Field(0.0, title="多头保证金率")
    LongMarginRatioByVolume: float = Field(0.0, title="多头保证金费")
    ShortMarginRatioByMoney: float = Field(0.0, title="空头保证金率")
    ShortMarginRatioByVolume: float = Field(0.0, title="空头保证金费")
    IsRelative: int = Field(0, title="是否相对交易所收取")
    ExchangeID: str = Field("", title="交易所代码")
    InvestUnitID: str = Field("", title="投资单元代码")
    InstrumentID: str = Field("", title="合约代码")


class WebCTPReqInstrumentMarginRate(WebCTPRequest):
    InstrumentMarginRate: InstrumentMarginRateField = Field(
        title="合约保证金率")


class InstrumentCommissionRateField(BaseModel):
    """合约手续费率"""

    reserve1: str = Field("", title="保留的无效字段")
    InvestorRange: str = Field("", title="投资者范围")
    BrokerID: str = Field("", title="经纪公司代码")
    InvestorID: str = Field("", title="投资者代码")
    OpenRatioByMoney: float = Field(0.0, title="开仓手续费率")
    OpenRatioByVolume: float = Field(0.0, title="开仓手续费")
    CloseRatioByMoney: float = Field(0.0, title="平仓手续费率")
    CloseRatioByVolume: float = Field(0.0, title="平仓手续费")
    CloseTodayRatioByMoney: float = Field(0.0, title="平今手续费率")
    CloseTodayRatioByVolume: float = Field(0.0, title="平今手续费")
    ExchangeID: str = Field("", title="交易所代码")
    BizType: str = Field("", title="业务类型")
    InvestUnitID: str = Field("", title="投资单元代码")
    InstrumentID: str = Field("", title="合约代码")


class WebCTPReqInstrumentCommissionRate(WebCTPRequest):
    InstrumentCommissionRate: InstrumentCommissionRateField = Field(
        title="合约手续费率")


class DepthMarketDataField(BaseModel):
    """深度行情"""

    TradingDay: str = Field("", title="交易日")
    reserve1: str = Field("", title="保留的无效字段")
    ExchangeID: str = Field("", title="交易所代码")
    reserve2: str = Field("", title="保留的无效字段")
    LastPrice: float = Field(0.0, title="最新价")
    PreSettlementPrice: float = Field(0.0, title="上次结算价")
    PreClosePrice: float = Field(0.0, title="昨收盘")
    PreOpenInterest: float = Field(0.0, title="昨持仓量")
    OpenPrice: float = Field(0.0, title="今开盘")
    HighestPrice: float = Field(0.0, title="最高价")
    LowestPrice: float = Field(0.0, title="最低价")
    Volume: int = Field(0, title="数量")
    Turnover: float = Field(0.0, title="成交金额")
    OpenInterest: float = Field(0.0, title="持仓量")
    ClosePrice: float = Field(0.0, title="今收盘")
    SettlementPrice: float = Field(0.0, title="本次结算价")
    UpperLimitPrice: float = Field(0.0, title="涨停板价")
    LowerLimitPrice: float = Field(0.0, title="跌停板价")
    PreDelta: float = Field(0.0, title="昨虚实度")
    CurrDelta: float = Field(0.0, title="今虚实度")
    UpdateTime: str = Field("", title="最后修改时间")
    UpdateMillisec: int = Field(0, title="最后修改毫秒")
    BidPrice1: float = Field(0.0, title="申买价一")
    BidVolume1: int = Field(0, title="申买量一")
    AskPrice1: float = Field(0.0, title="申卖价一")
    AskVolume1: int = Field(0, title="申卖量一")
    BidPrice2: float = Field(0.0, title="申买价二")
    BidVolume2: int = Field(0, title="申买量二")
    AskPrice2: float = Field(0.0, title="申卖价二")
    AskVolume2: int = Field(0, title="申卖量二")
    BidPrice3: float = Field(0.0, title="申买价三")
    BidVolume3: int = Field(0, title="申买量三")
    AskPrice3: float = Field(0.0, title="申卖价三")
    AskVolume3: int = Field(0, title="申卖量三")
    BidPrice4: float = Field(0.0, title="申买价四")
    BidVolume4: int = Field(0, title="申买量四")
    AskPrice4: float = Field(0.0, title="申卖价四")
    AskVolume4: int = Field(0, title="申卖量四")
    BidPrice5: float = Field(0.0, title="申买价五")
    BidVolume5: int = Field(0, title="申买量五")
    AskPrice5: float = Field(0.0, title="申卖价五")
    AskVolume5: int = Field(0, title="申卖量五")
    AveragePrice: float = Field(0.0, title="当日均价")
    ActionDay: str = Field("", title="业务日期")
    InstrumentID: str = Field("", title="合约代码")
    ExchangeInstID: str = Field("", title="合约在交易所的代码")
    BandingUpperPrice: float = Field(0.0, title="上带价")
    BandingLowerPrice: float = Field(0.0, title="下带价")


class WebCTPReqDepthMarketData(WebCTPRequest):
    DepthMarketData: DepthMarketDataField = Field(title="深度行情")


class InstrumentTradingRightField(BaseModel):
    """投资者合约交易权限"""

    reserve1: str = Field("", title="保留的无效字段")
    InvestorRange: str = Field("", title="投资者范围")
    BrokerID: str = Field("", title="经纪公司代码")
    InvestorID: str = Field("", title="投资者代码")
    TradingRight: str = Field("", title="交易权限")
    InstrumentID: str = Field("", title="合约代码")


class WebCTPReqInstrumentTradingRight(WebCTPRequest):
    InstrumentTradingRight: InstrumentTradingRightField = Field(
        title="投资者合约交易权限")


class BrokerUserField(BaseModel):
    """经纪公司用户"""

    BrokerID: str = Field("", title="经纪公司代码")
    UserID: str = Field("", title="用户代码")
    UserName: str = Field("", title="用户名称")
    UserType: str = Field("", title="用户类型")
    IsActive: int = Field(0, title="是否活跃")
    IsUsingOTP: int = Field(0, title="是否使用令牌")
    IsAuthForce: int = Field(0, title="是否强制终端认证")


class WebCTPReqBrokerUser(WebCTPRequest):
    BrokerUser: BrokerUserField = Field(title="经纪公司用户")


class BrokerUserPasswordField(BaseModel):
    """经纪公司用户口令"""

    BrokerID: str = Field("", title="经纪公司代码")
    UserID: str = Field("", title="用户代码")
    Password: str = Field("", title="密码")
    LastUpdateTime: str = Field("", title="上次修改时间")
    LastLoginTime: str = Field("", title="上次登陆时间")
    ExpireDate: str = Field("", title="密码过期时间")
    WeakExpireDate: str = Field("", title="弱密码过期时间")


class WebCTPReqBrokerUserPassword(WebCTPRequest):
    BrokerUserPassword: BrokerUserPasswordField = Field(
        title="经纪公司用户口令")


class BrokerUserFunctionField(BaseModel):
    """经纪公司用户功能权限"""

    BrokerID: str = Field("", title="经纪公司代码")
    UserID: str = Field("", title="用户代码")
    BrokerFunctionCode: str = Field("", title="经纪公司功能代码")


class WebCTPReqBrokerUserFunction(WebCTPRequest):
    BrokerUserFunction: BrokerUserFunctionField = Field(
        title="经纪公司用户功能权限")


class TraderOfferField(BaseModel):
    """交易所交易员报盘机"""

    ExchangeID: str = Field("", title="交易所代码")
    TraderID: str = Field("", title="交易所交易员代码")
    ParticipantID: str = Field("", title="会员代码")
    Password: str = Field("", title="密码")
    InstallID: int = Field(0, title="安装编号")
    OrderLocalID: str = Field("", title="本地报单编号")
    TraderConnectStatus: str = Field("", title="交易所交易员连接状态")
    ConnectRequestDate: str = Field("", title="发出连接请求的日期")
    ConnectRequestTime: str = Field("", title="发出连接请求的时间")
    LastReportDate: str = Field("", title="上次报告日期")
    LastReportTime: str = Field("", title="上次报告时间")
    ConnectDate: str = Field("", title="完成连接日期")
    ConnectTime: str = Field("", title="完成连接时间")
    StartDate: str = Field("", title="启动日期")
    StartTime: str = Field("", title="启动时间")
    TradingDay: str = Field("", title="交易日")
    BrokerID: str = Field("", title="经纪公司代码")
    MaxTradeID: str = Field("", title="本席位最大成交编号")
    MaxOrderMessageReference: str = Field("", title="本席位最大报单备拷")
    OrderCancelAlg: str = Field("", title="撤单时选择席位算法")


class WebCTPReqTraderOffer(WebCTPRequest):
    TraderOffer: TraderOfferField = Field(title="交易所交易员报盘机")


class SettlementInfoField(BaseModel):
    """投资者结算结果"""

    TradingDay: str = Field("", title="交易日")
    SettlementID: int = Field(0, title="结算编号")
    BrokerID: str = Field("", title="经纪公司代码")
    InvestorID: str = Field("", title="投资者代码")
    SequenceNo: int = Field(0, title="序号")
    Content: str = Field("", title="消息正文")
    AccountID: str = Field("", title="投资者帐号")
    CurrencyID: str = Field("", title="币种代码")


class WebCTPReqSettlementInfo(WebCTPRequest):
    SettlementInfo: SettlementInfoField = Field(title="投资者结算结果")


class InstrumentMarginRateAdjustField(BaseModel):
    """合约保证金率调整"""

    reserve1: str = Field("", title="保留的无效字段")
    InvestorRange: str = Field("", title="投资者范围")
    BrokerID: str = Field("", title="经纪公司代码")
    InvestorID: str = Field("", title="投资者代码")
    HedgeFlag: str = Field("", title="投机套保标志")
    LongMarginRatioByMoney: float = Field(0.0, title="多头保证金率")
    LongMarginRatioByVolume: float = Field(0.0, title="多头保证金费")
    ShortMarginRatioByMoney: float = Field(0.0, title="空头保证金率")
    ShortMarginRatioByVolume: float = Field(0.0, title="空头保证金费")
    IsRelative: int = Field(0, title="是否相对交易所收取")
    InstrumentID: str = Field("", title="合约代码")


class WebCTPReqInstrumentMarginRateAdjust(WebCTPRequest):
    InstrumentMarginRateAdjust: InstrumentMarginRateAdjustField = Field(
        title="合约保证金率调整")


class ExchangeMarginRateField(BaseModel):
    """交易所保证金率"""

    BrokerID: str = Field("", title="经纪公司代码")
    reserve1: str = Field("", title="保留的无效字段")
    HedgeFlag: str = Field("", title="投机套保标志")
    LongMarginRatioByMoney: float = Field(0.0, title="多头保证金率")
    LongMarginRatioByVolume: float = Field(0.0, title="多头保证金费")
    ShortMarginRatioByMoney: float = Field(0.0, title="空头保证金率")
    ShortMarginRatioByVolume: float = Field(0.0, title="空头保证金费")
    ExchangeID: str = Field("", title="交易所代码")
    InstrumentID: str = Field("", title="合约代码")


class WebCTPReqExchangeMarginRate(WebCTPRequest):
    ExchangeMarginRate: ExchangeMarginRateField = Field(title="交易所保证金率")


class ExchangeMarginRateAdjustField(BaseModel):
    """交易所保证金率调整"""

    BrokerID: str = Field("", title="经纪公司代码")
    reserve1: str = Field("", title="保留的无效字段")
    HedgeFlag: str = Field("", title="投机套保标志")
    LongMarginRatioByMoney: float = Field(0.0,
                                          title="跟随交易所投资者多头保证金率")
    LongMarginRatioByVolume: float = Field(0.0,
                                           title="跟随交易所投资者多头保证金费")
    ShortMarginRatioByMoney: float = Field(0.0,
                                           title="跟随交易所投资者空头保证金率")
    ShortMarginRatioByVolume: float = Field(0.0,
                                            title="跟随交易所投资者空头保证金费")
    ExchLongMarginRatioByMoney: float = Field(0.0, title="交易所多头保证金率")
    ExchLongMarginRatioByVolume: float = Field(0.0, title="交易所多头保证金费")
    ExchShortMarginRatioByMoney: float = Field(0.0, title="交易所空头保证金率")
    ExchShortMarginRatioByVolume: float = Field(0.0,
                                                title="交易所空头保证金费")
    NoLongMarginRatioByMoney: float = Field(0.0,
                                            title="不跟随交易所投资者多头保证金率")
    NoLongMarginRatioByVolume: float = Field(0.0,
                                             title="不跟随交易所投资者多头保证金费")
    NoShortMarginRatioByMoney: float = Field(0.0,
                                             title="不跟随交易所投资者空头保证金率")
    NoShortMarginRatioByVolume: float = Field(0.0,
                                              title="不跟随交易所投资者空头保证金费")
    InstrumentID: str = Field("", title="合约代码")


class WebCTPReqExchangeMarginRateAdjust(WebCTPRequest):
    ExchangeMarginRateAdjust: ExchangeMarginRateAdjustField = Field(
        title="交易所保证金率调整")


class ExchangeRateField(BaseModel):
    """汇率"""

    BrokerID: str = Field("", title="经纪公司代码")
    FromCurrencyID: str = Field("", title="源币种")
    FromCurrencyUnit: float = Field(0.0, title="源币种单位数量")
    ToCurrencyID: str = Field("", title="目标币种")
    ExchangeRate: float = Field(0.0, title="汇率")


class WebCTPReqExchangeRate(WebCTPRequest):
    ExchangeRate: ExchangeRateField = Field(title="汇率")


class SettlementRefField(BaseModel):
    """结算引用"""

    TradingDay: str = Field("", title="交易日")
    SettlementID: int = Field(0, title="结算编号")


class WebCTPReqSettlementRef(WebCTPRequest):
    SettlementRef: SettlementRefField = Field(title="结算引用")


class CurrentTimeField(BaseModel):
    """当前时间"""

    CurrDate: str = Field("", title="当前交易日")
    CurrTime: str = Field("", title="当前时间")
    CurrMillisec: int = Field(0, title="当前时间（毫秒）")
    ActionDay: str = Field("", title="自然日期")


class WebCTPReqCurrentTime(WebCTPRequest):
    CurrentTime: CurrentTimeField = Field(title="当前时间")


class CommPhaseField(BaseModel):
    """通讯阶段"""

    TradingDay: str = Field("", title="交易日")
    CommPhaseNo: int = Field(0, title="通讯时段编号")
    SystemID: str = Field("", title="系统编号")


class WebCTPReqCommPhase(WebCTPRequest):
    CommPhase: CommPhaseField = Field(title="通讯阶段")


class LoginInfoField(BaseModel):
    """登录信息"""

    FrontID: int = Field(0, title="前置编号")
    SessionID: int = Field(0, title="会话编号")
    BrokerID: str = Field("", title="经纪公司代码")
    UserID: str = Field("", title="用户代码")
    LoginDate: str = Field("", title="登录日期")
    LoginTime: str = Field("", title="登录时间")
    reserve1: str = Field("", title="保留的无效字段")
    UserProductInfo: str = Field("", title="用户端产品信息")
    InterfaceProductInfo: str = Field("", title="接口端产品信息")
    ProtocolInfo: str = Field("", title="协议信息")
    SystemName: str = Field("", title="系统名称")
    PasswordDeprecated: str = Field("", title="密码,已弃用")
    MaxOrderRef: str = Field("", title="最大报单引用")
    SHFETime: str = Field("", title="上期所时间")
    DCETime: str = Field("", title="大商所时间")
    CZCETime: str = Field("", title="郑商所时间")
    FFEXTime: str = Field("", title="中金所时间")
    MacAddress: str = Field("", title="Mac地址")
    OneTimePassword: str = Field("", title="动态密码")
    INETime: str = Field("", title="能源中心时间")
    IsQryControl: int = Field(0, title="查询时是否需要流控")
    LoginRemark: str = Field("", title="登录备注")
    Password: str = Field("", title="密码")
    IPAddress: str = Field("", title="IP地址")


class WebCTPReqLoginInfo(WebCTPRequest):
    LoginInfo: LoginInfoField = Field(title="登录信息")


class LogoutAllField(BaseModel):
    """登录信息"""

    FrontID: int = Field(0, title="前置编号")
    SessionID: int = Field(0, title="会话编号")
    SystemName: str = Field("", title="系统名称")


class WebCTPReqLogoutAll(WebCTPRequest):
    LogoutAll: LogoutAllField = Field(title="登录信息")


class FrontStatusField(BaseModel):
    """前置状态"""

    FrontID: int = Field(0, title="前置编号")
    LastReportDate: str = Field("", title="上次报告日期")
    LastReportTime: str = Field("", title="上次报告时间")
    IsActive: int = Field(0, title="是否活跃")


class WebCTPReqFrontStatus(WebCTPRequest):
    FrontStatus: FrontStatusField = Field(title="前置状态")


class UserPasswordUpdateField(BaseModel):
    """用户口令变更"""

    BrokerID: str = Field("", title="经纪公司代码")
    UserID: str = Field("", title="用户代码")
    OldPassword: str = Field("", title="原来的口令")
    NewPassword: str = Field("", title="新的口令")


class WebCTPReqUserPasswordUpdate(WebCTPRequest):
    UserPasswordUpdate: UserPasswordUpdateField = Field(title="用户口令变更")


class InputOrderField(BaseModel):
    """输入报单"""

    BrokerID: str = Field("", title="经纪公司代码")
    InvestorID: str = Field("", title="投资者代码")
    reserve1: str = Field("", title="保留的无效字段")
    OrderRef: str = Field("", title="报单引用")
    UserID: str = Field("", title="用户代码")
    OrderPriceType: str = Field("", title="报单价格条件")
    Direction: str = Field("", title="买卖方向")
    CombOffsetFlag: str = Field("", title="组合开平标志")
    CombHedgeFlag: str = Field("", title="组合投机套保标志")
    LimitPrice: float = Field(0.0, title="价格")
    VolumeTotalOriginal: int = Field(0, title="数量")
    TimeCondition: str = Field("", title="有效期类型")
    GTDDate: str = Field("", title="GTD日期")
    VolumeCondition: str = Field("", title="成交量类型")
    MinVolume: int = Field(0, title="最小成交量")
    ContingentCondition: str = Field("", title="触发条件")
    StopPrice: float = Field(0.0, title="止损价")
    ForceCloseReason: str = Field("", title="强平原因")
    IsAutoSuspend: int = Field(0, title="自动挂起标志")
    BusinessUnit: str = Field("", title="业务单元")
    RequestID: int = Field(0, title="请求编号")
    UserForceClose: int = Field(0, title="用户强评标志")
    IsSwapOrder: int = Field(0, title="互换单标志")
    ExchangeID: str = Field("", title="交易所代码")
    InvestUnitID: str = Field("", title="投资单元代码")
    AccountID: str = Field("", title="资金账号")
    CurrencyID: str = Field("", title="币种代码")
    ClientID: str = Field("", title="交易编码")
    reserve2: str = Field("", title="保留的无效字段")
    MacAddress: str = Field("", title="Mac地址")
    InstrumentID: str = Field("", title="合约代码")
    IPAddress: str = Field("", title="IP地址")


class WebCTPReqOrderInsert(WebCTPRequest):
    InputOrder: InputOrderField = Field(title="输入报单")


class OrderField(BaseModel):
    """报单"""

    BrokerID: str = Field("", title="经纪公司代码")
    InvestorID: str = Field("", title="投资者代码")
    reserve1: str = Field("", title="保留的无效字段")
    OrderRef: str = Field("", title="报单引用")
    UserID: str = Field("", title="用户代码")
    OrderPriceType: str = Field("", title="报单价格条件")
    Direction: str = Field("", title="买卖方向")
    CombOffsetFlag: str = Field("", title="组合开平标志")
    CombHedgeFlag: str = Field("", title="组合投机套保标志")
    LimitPrice: float = Field(0.0, title="价格")
    VolumeTotalOriginal: int = Field(0, title="数量")
    TimeCondition: str = Field("", title="有效期类型")
    GTDDate: str = Field("", title="GTD日期")
    VolumeCondition: str = Field("", title="成交量类型")
    MinVolume: int = Field(0, title="最小成交量")
    ContingentCondition: str = Field("", title="触发条件")
    StopPrice: float = Field(0.0, title="止损价")
    ForceCloseReason: str = Field("", title="强平原因")
    IsAutoSuspend: int = Field(0, title="自动挂起标志")
    BusinessUnit: str = Field("", title="业务单元")
    RequestID: int = Field(0, title="请求编号")
    OrderLocalID: str = Field("", title="本地报单编号")
    ExchangeID: str = Field("", title="交易所代码")
    ParticipantID: str = Field("", title="会员代码")
    ClientID: str = Field("", title="客户代码")
    reserve2: str = Field("", title="保留的无效字段")
    TraderID: str = Field("", title="交易所交易员代码")
    InstallID: int = Field(0, title="安装编号")
    OrderSubmitStatus: str = Field("", title="报单提交状态")
    NotifySequence: int = Field(0, title="报单提示序号")
    TradingDay: str = Field("", title="交易日")
    SettlementID: int = Field(0, title="结算编号")
    OrderSysID: str = Field("", title="报单编号")
    OrderSource: str = Field("", title="报单来源")
    OrderStatus: str = Field("", title="报单状态")
    OrderType: str = Field("", title="报单类型")
    VolumeTraded: int = Field(0, title="今成交数量")
    VolumeTotal: int = Field(0, title="剩余数量")
    InsertDate: str = Field("", title="报单日期")
    InsertTime: str = Field("", title="委托时间")
    ActiveTime: str = Field("", title="激活时间")
    SuspendTime: str = Field("", title="挂起时间")
    UpdateTime: str = Field("", title="最后修改时间")
    CancelTime: str = Field("", title="撤销时间")
    ActiveTraderID: str = Field("", title="最后修改交易所交易员代码")
    ClearingPartID: str = Field("", title="结算会员编号")
    SequenceNo: int = Field(0, title="序号")
    FrontID: int = Field(0, title="前置编号")
    SessionID: int = Field(0, title="会话编号")
    UserProductInfo: str = Field("", title="用户端产品信息")
    StatusMsg: str = Field("", title="状态信息")
    UserForceClose: int = Field(0, title="用户强评标志")
    ActiveUserID: str = Field("", title="操作用户代码")
    BrokerOrderSeq: int = Field(0, title="经纪公司报单编号")
    RelativeOrderSysID: str = Field("", title="相关报单")
    ZCETotalTradedVolume: int = Field(0, title="郑商所成交数量")
    IsSwapOrder: int = Field(0, title="互换单标志")
    BranchID: str = Field("", title="营业部编号")
    InvestUnitID: str = Field("", title="投资单元代码")
    AccountID: str = Field("", title="资金账号")
    CurrencyID: str = Field("", title="币种代码")
    reserve3: str = Field("", title="保留的无效字段")
    MacAddress: str = Field("", title="Mac地址")
    InstrumentID: str = Field("", title="合约代码")
    ExchangeInstID: str = Field("", title="合约在交易所的代码")
    IPAddress: str = Field("", title="IP地址")


class WebCTPReqOrder(WebCTPRequest):
    Order: OrderField = Field(title="报单")


class ExchangeOrderField(BaseModel):
    """交易所报单"""

    OrderPriceType: str = Field("", title="报单价格条件")
    Direction: str = Field("", title="买卖方向")
    CombOffsetFlag: str = Field("", title="组合开平标志")
    CombHedgeFlag: str = Field("", title="组合投机套保标志")
    LimitPrice: float = Field(0.0, title="价格")
    VolumeTotalOriginal: int = Field(0, title="数量")
    TimeCondition: str = Field("", title="有效期类型")
    GTDDate: str = Field("", title="GTD日期")
    VolumeCondition: str = Field("", title="成交量类型")
    MinVolume: int = Field(0, title="最小成交量")
    ContingentCondition: str = Field("", title="触发条件")
    StopPrice: float = Field(0.0, title="止损价")
    ForceCloseReason: str = Field("", title="强平原因")
    IsAutoSuspend: int = Field(0, title="自动挂起标志")
    BusinessUnit: str = Field("", title="业务单元")
    RequestID: int = Field(0, title="请求编号")
    OrderLocalID: str = Field("", title="本地报单编号")
    ExchangeID: str = Field("", title="交易所代码")
    ParticipantID: str = Field("", title="会员代码")
    ClientID: str = Field("", title="客户代码")
    reserve1: str = Field("", title="保留的无效字段")
    TraderID: str = Field("", title="交易所交易员代码")
    InstallID: int = Field(0, title="安装编号")
    OrderSubmitStatus: str = Field("", title="报单提交状态")
    NotifySequence: int = Field(0, title="报单提示序号")
    TradingDay: str = Field("", title="交易日")
    SettlementID: int = Field(0, title="结算编号")
    OrderSysID: str = Field("", title="报单编号")
    OrderSource: str = Field("", title="报单来源")
    OrderStatus: str = Field("", title="报单状态")
    OrderType: str = Field("", title="报单类型")
    VolumeTraded: int = Field(0, title="今成交数量")
    VolumeTotal: int = Field(0, title="剩余数量")
    InsertDate: str = Field("", title="报单日期")
    InsertTime: str = Field("", title="委托时间")
    ActiveTime: str = Field("", title="激活时间")
    SuspendTime: str = Field("", title="挂起时间")
    UpdateTime: str = Field("", title="最后修改时间")
    CancelTime: str = Field("", title="撤销时间")
    ActiveTraderID: str = Field("", title="最后修改交易所交易员代码")
    ClearingPartID: str = Field("", title="结算会员编号")
    SequenceNo: int = Field(0, title="序号")
    BranchID: str = Field("", title="营业部编号")
    reserve2: str = Field("", title="保留的无效字段")
    MacAddress: str = Field("", title="Mac地址")
    ExchangeInstID: str = Field("", title="合约在交易所的代码")
    IPAddress: str = Field("", title="IP地址")


class WebCTPReqExchangeOrder(WebCTPRequest):
    ExchangeOrder: ExchangeOrderField = Field(title="交易所报单")


class ExchangeOrderInsertErrorField(BaseModel):
    """交易所报单插入失败"""

    ExchangeID: str = Field("", title="交易所代码")
    ParticipantID: str = Field("", title="会员代码")
    TraderID: str = Field("", title="交易所交易员代码")
    InstallID: int = Field(0, title="安装编号")
    OrderLocalID: str = Field("", title="本地报单编号")
    ErrorID: int = Field(0, title="错误代码")
    ErrorMsg: str = Field("", title="错误信息")


class WebCTPReqExchangeOrderInsertError(WebCTPRequest):
    ExchangeOrderInsertError: ExchangeOrderInsertErrorField = Field(
        title="交易所报单插入失败")


class InputOrderActionField(BaseModel):
    """输入报单操作"""

    BrokerID: str = Field("", title="经纪公司代码")
    InvestorID: str = Field("", title="投资者代码")
    OrderActionRef: int = Field(0, title="报单操作引用")
    OrderRef: str = Field("", title="报单引用")
    RequestID: int = Field(0, title="请求编号")
    FrontID: int = Field(0, title="前置编号")
    SessionID: int = Field(0, title="会话编号")
    ExchangeID: str = Field("", title="交易所代码")
    OrderSysID: str = Field("", title="报单编号")
    ActionFlag: str = Field("", title="操作标志")
    LimitPrice: float = Field(0.0, title="价格")
    VolumeChange: int = Field(0, title="数量变化")
    UserID: str = Field("", title="用户代码")
    reserve1: str = Field("", title="保留的无效字段")
    InvestUnitID: str = Field("", title="投资单元代码")
    reserve2: str = Field("", title="保留的无效字段")
    MacAddress: str = Field("", title="Mac地址")
    InstrumentID: str = Field("", title="合约代码")
    IPAddress: str = Field("", title="IP地址")


# class WebCTPReqInputOrderAction(WebCTPRequest):
#     InputOrderAction: InputOrderActionField = Field(title="输入报单操作")


# class OrderActionField(BaseModel):
#     """报单操作"""
#
#     BrokerID: str = Field("", title="经纪公司代码")
#     InvestorID: str = Field("", title="投资者代码")
#     OrderActionRef: int = Field(0, title="报单操作引用")
#     OrderRef: str = Field("", title="报单引用")
#     RequestID: int = Field(0, title="请求编号")
#     FrontID: int = Field(0, title="前置编号")
#     SessionID: int = Field(0, title="会话编号")
#     ExchangeID: str = Field("", title="交易所代码")
#     OrderSysID: str = Field("", title="报单编号")
#     ActionFlag: str = Field("", title="操作标志")
#     LimitPrice: float = Field(0.0, title="价格")
#     VolumeChange: int = Field(0, title="数量变化")
#     ActionDate: str = Field("", title="操作日期")
#     ActionTime: str = Field("", title="操作时间")
#     TraderID: str = Field("", title="交易所交易员代码")
#     InstallID: int = Field(0, title="安装编号")
#     OrderLocalID: str = Field("", title="本地报单编号")
#     ActionLocalID: str = Field("", title="操作本地编号")
#     ParticipantID: str = Field("", title="会员代码")
#     ClientID: str = Field("", title="客户代码")
#     BusinessUnit: str = Field("", title="业务单元")
#     OrderActionStatus: str = Field("", title="报单操作状态")
#     UserID: str = Field("", title="用户代码")
#     StatusMsg: str = Field("", title="状态信息")
#     reserve1: str = Field("", title="保留的无效字段")
#     BranchID: str = Field("", title="营业部编号")
#     InvestUnitID: str = Field("", title="投资单元代码")
#     reserve2: str = Field("", title="保留的无效字段")
#     MacAddress: str = Field("", title="Mac地址")
#     InstrumentID: str = Field("", title="合约代码")
#     IPAddress: str = Field("", title="IP地址")


class WebCTPReqOrderAction(WebCTPRequest):
    InputOrderAction: InputOrderActionField = Field(title="报单操作")


class ExchangeOrderActionField(BaseModel):
    """交易所报单操作"""

    ExchangeID: str = Field("", title="交易所代码")
    OrderSysID: str = Field("", title="报单编号")
    ActionFlag: str = Field("", title="操作标志")
    LimitPrice: float = Field(0.0, title="价格")
    VolumeChange: int = Field(0, title="数量变化")
    ActionDate: str = Field("", title="操作日期")
    ActionTime: str = Field("", title="操作时间")
    TraderID: str = Field("", title="交易所交易员代码")
    InstallID: int = Field(0, title="安装编号")
    OrderLocalID: str = Field("", title="本地报单编号")
    ActionLocalID: str = Field("", title="操作本地编号")
    ParticipantID: str = Field("", title="会员代码")
    ClientID: str = Field("", title="客户代码")
    BusinessUnit: str = Field("", title="业务单元")
    OrderActionStatus: str = Field("", title="报单操作状态")
    UserID: str = Field("", title="用户代码")
    BranchID: str = Field("", title="营业部编号")
    reserve1: str = Field("", title="保留的无效字段")
    MacAddress: str = Field("", title="Mac地址")
    IPAddress: str = Field("", title="IP地址")


class WebCTPReqExchangeOrderAction(WebCTPRequest):
    ExchangeOrderAction: ExchangeOrderActionField = Field(
        title="交易所报单操作")


class ExchangeOrderActionErrorField(BaseModel):
    """交易所报单操作失败"""

    ExchangeID: str = Field("", title="交易所代码")
    OrderSysID: str = Field("", title="报单编号")
    TraderID: str = Field("", title="交易所交易员代码")
    InstallID: int = Field(0, title="安装编号")
    OrderLocalID: str = Field("", title="本地报单编号")
    ActionLocalID: str = Field("", title="操作本地编号")
    ErrorID: int = Field(0, title="错误代码")
    ErrorMsg: str = Field("", title="错误信息")


class WebCTPReqExchangeOrderActionError(WebCTPRequest):
    ExchangeOrderActionError: ExchangeOrderActionErrorField = Field(
        title="交易所报单操作失败")


class ExchangeTradeField(BaseModel):
    """交易所成交"""

    ExchangeID: str = Field("", title="交易所代码")
    TradeID: str = Field("", title="成交编号")
    Direction: str = Field("", title="买卖方向")
    OrderSysID: str = Field("", title="报单编号")
    ParticipantID: str = Field("", title="会员代码")
    ClientID: str = Field("", title="客户代码")
    TradingRole: str = Field("", title="交易角色")
    reserve1: str = Field("", title="保留的无效字段")
    OffsetFlag: str = Field("", title="开平标志")
    HedgeFlag: str = Field("", title="投机套保标志")
    Price: float = Field(0.0, title="价格")
    Volume: int = Field(0, title="数量")
    TradeDate: str = Field("", title="成交时期")
    TradeTime: str = Field("", title="成交时间")
    TradeType: str = Field("", title="成交类型")
    PriceSource: str = Field("", title="成交价来源")
    TraderID: str = Field("", title="交易所交易员代码")
    OrderLocalID: str = Field("", title="本地报单编号")
    ClearingPartID: str = Field("", title="结算会员编号")
    BusinessUnit: str = Field("", title="业务单元")
    SequenceNo: int = Field(0, title="序号")
    TradeSource: str = Field("", title="成交来源")
    ExchangeInstID: str = Field("", title="合约在交易所的代码")


class WebCTPReqExchangeTrade(WebCTPRequest):
    ExchangeTrade: ExchangeTradeField = Field(title="交易所成交")


class TradeField(BaseModel):
    """成交"""

    BrokerID: str = Field("", title="经纪公司代码")
    InvestorID: str = Field("", title="投资者代码")
    reserve1: str = Field("", title="保留的无效字段")
    OrderRef: str = Field("", title="报单引用")
    UserID: str = Field("", title="用户代码")
    ExchangeID: str = Field("", title="交易所代码")
    TradeID: str = Field("", title="成交编号")
    Direction: str = Field("", title="买卖方向")
    OrderSysID: str = Field("", title="报单编号")
    ParticipantID: str = Field("", title="会员代码")
    ClientID: str = Field("", title="客户代码")
    TradingRole: str = Field("", title="交易角色")
    reserve2: str = Field("", title="保留的无效字段")
    OffsetFlag: str = Field("", title="开平标志")
    HedgeFlag: str = Field("", title="投机套保标志")
    Price: float = Field(0.0, title="价格")
    Volume: int = Field(0, title="数量")
    TradeDate: str = Field("", title="成交时期")
    TradeTime: str = Field("", title="成交时间")
    TradeType: str = Field("", title="成交类型")
    PriceSource: str = Field("", title="成交价来源")
    TraderID: str = Field("", title="交易所交易员代码")
    OrderLocalID: str = Field("", title="本地报单编号")
    ClearingPartID: str = Field("", title="结算会员编号")
    BusinessUnit: str = Field("", title="业务单元")
    SequenceNo: int = Field(0, title="序号")
    TradingDay: str = Field("", title="交易日")
    SettlementID: int = Field(0, title="结算编号")
    BrokerOrderSeq: int = Field(0, title="经纪公司报单编号")
    TradeSource: str = Field("", title="成交来源")
    InvestUnitID: str = Field("", title="投资单元代码")
    InstrumentID: str = Field("", title="合约代码")
    ExchangeInstID: str = Field("", title="合约在交易所的代码")


class WebCTPReqTrade(WebCTPRequest):
    Trade: TradeField = Field(title="成交")


class UserSessionField(BaseModel):
    """用户会话"""

    FrontID: int = Field(0, title="前置编号")
    SessionID: int = Field(0, title="会话编号")
    BrokerID: str = Field("", title="经纪公司代码")
    UserID: str = Field("", title="用户代码")
    LoginDate: str = Field("", title="登录日期")
    LoginTime: str = Field("", title="登录时间")
    reserve1: str = Field("", title="保留的无效字段")
    UserProductInfo: str = Field("", title="用户端产品信息")
    InterfaceProductInfo: str = Field("", title="接口端产品信息")
    ProtocolInfo: str = Field("", title="协议信息")
    MacAddress: str = Field("", title="Mac地址")
    LoginRemark: str = Field("", title="登录备注")
    IPAddress: str = Field("", title="IP地址")


class WebCTPReqUserSession(WebCTPRequest):
    UserSession: UserSessionField = Field(title="用户会话")


class QueryMaxOrderVolumeField(BaseModel):
    """查询最大报单数量"""

    BrokerID: str = Field("", title="经纪公司代码")
    InvestorID: str = Field("", title="投资者代码")
    InstrumentID: str = Field("", title="合约代码")
    Direction: str = Field("", title="买卖方向")
    OffsetFlag: str = Field("", title="开平标志")
    HedgeFlag: str = Field("", title="投机套保标志")
    MaxVolume: int = Field(0, title="最大允许报单数量")
    ExchangeID: str = Field("", title="交易所代码")
    InvestUnitID: str = Field("", title="投资单元代码")


class WebCTPReqQueryMaxOrderVolume(WebCTPRequest):
    QueryMaxOrderVolume: QueryMaxOrderVolumeField = Field(
        title="查询最大报单数量")


class SettlementInfoConfirmField(BaseModel):
    """投资者结算结果确认信息"""

    BrokerID: str = Field("", title="经纪公司代码")
    InvestorID: str = Field("", title="投资者代码")
    ConfirmDate: str = Field("", title="确认日期")
    ConfirmTime: str = Field("", title="确认时间")
    SettlementID: int = Field(0, title="结算编号")
    AccountID: str = Field("", title="投资者帐号")
    CurrencyID: str = Field("", title="币种代码")


class WebCTPReqSettlementInfoConfirm(WebCTPRequest):
    SettlementInfoConfirm: SettlementInfoConfirmField = Field(
        title="投资者结算结果确认信息")


class SyncDepositField(BaseModel):
    """出入金同步"""

    DepositSeqNo: str = Field("", title="出入金流水号")
    BrokerID: str = Field("", title="经纪公司代码")
    InvestorID: str = Field("", title="投资者代码")
    Deposit: float = Field(0.0, title="入金金额")
    IsForce: int = Field(0, title="是否强制进行")
    CurrencyID: str = Field("", title="币种代码")
    IsFromSopt: int = Field(0, title="是否是个股期权内转")
    TradingPassword: str = Field("", title="资金密码")


class WebCTPReqSyncDeposit(WebCTPRequest):
    SyncDeposit: SyncDepositField = Field(title="出入金同步")


class SyncFundMortgageField(BaseModel):
    """货币质押同步"""

    MortgageSeqNo: str = Field("", title="货币质押流水号")
    BrokerID: str = Field("", title="经纪公司代码")
    InvestorID: str = Field("", title="投资者代码")
    FromCurrencyID: str = Field("", title="源币种")
    MortgageAmount: float = Field(0.0, title="质押金额")
    ToCurrencyID: str = Field("", title="目标币种")


class WebCTPReqSyncFundMortgage(WebCTPRequest):
    SyncFundMortgage: SyncFundMortgageField = Field(title="货币质押同步")


class BrokerSyncField(BaseModel):
    """经纪公司同步"""

    BrokerID: str = Field("", title="经纪公司代码")


class WebCTPReqBrokerSync(WebCTPRequest):
    BrokerSync: BrokerSyncField = Field(title="经纪公司同步")


class SyncingInvestorField(BaseModel):
    """正在同步中的投资者"""

    InvestorID: str = Field("", title="投资者代码")
    BrokerID: str = Field("", title="经纪公司代码")
    InvestorGroupID: str = Field("", title="投资者分组代码")
    InvestorName: str = Field("", title="投资者名称")
    IdentifiedCardType: str = Field("", title="证件类型")
    IdentifiedCardNo: str = Field("", title="证件号码")
    IsActive: int = Field(0, title="是否活跃")
    Telephone: str = Field("", title="联系电话")
    Address: str = Field("", title="通讯地址")
    OpenDate: str = Field("", title="开户日期")
    Mobile: str = Field("", title="手机")
    CommModelID: str = Field("", title="手续费率模板代码")
    MarginModelID: str = Field("", title="保证金率模板代码")
    IsOrderFreq: str = Field("", title="是否频率控制")
    IsOpenVolLimit: str = Field("", title="是否开仓限制")


class WebCTPReqSyncingInvestor(WebCTPRequest):
    SyncingInvestor: SyncingInvestorField = Field(title="正在同步中的投资者")


class SyncingTradingCodeField(BaseModel):
    """正在同步中的交易代码"""

    InvestorID: str = Field("", title="投资者代码")
    BrokerID: str = Field("", title="经纪公司代码")
    ExchangeID: str = Field("", title="交易所代码")
    ClientID: str = Field("", title="客户代码")
    IsActive: int = Field(0, title="是否活跃")
    ClientIDType: str = Field("", title="交易编码类型")


class WebCTPReqSyncingTradingCode(WebCTPRequest):
    SyncingTradingCode: SyncingTradingCodeField = Field(
        title="正在同步中的交易代码")


class SyncingInvestorGroupField(BaseModel):
    """正在同步中的投资者分组"""

    BrokerID: str = Field("", title="经纪公司代码")
    InvestorGroupID: str = Field("", title="投资者分组代码")
    InvestorGroupName: str = Field("", title="投资者分组名称")


class WebCTPReqSyncingInvestorGroup(WebCTPRequest):
    SyncingInvestorGroup: SyncingInvestorGroupField = Field(
        title="正在同步中的投资者分组")


class SyncingTradingAccountField(BaseModel):
    """正在同步中的交易账号"""

    BrokerID: str = Field("", title="经纪公司代码")
    AccountID: str = Field("", title="投资者帐号")
    PreMortgage: float = Field(0.0, title="上次质押金额")
    PreCredit: float = Field(0.0, title="上次信用额度")
    PreDeposit: float = Field(0.0, title="上次存款额")
    PreBalance: float = Field(0.0, title="上次结算准备金")
    PreMargin: float = Field(0.0, title="上次占用的保证金")
    InterestBase: float = Field(0.0, title="利息基数")
    Interest: float = Field(0.0, title="利息收入")
    Deposit: float = Field(0.0, title="入金金额")
    Withdraw: float = Field(0.0, title="出金金额")
    FrozenMargin: float = Field(0.0, title="冻结的保证金")
    FrozenCash: float = Field(0.0, title="冻结的资金")
    FrozenCommission: float = Field(0.0, title="冻结的手续费")
    CurrMargin: float = Field(0.0, title="当前保证金总额")
    CashIn: float = Field(0.0, title="资金差额")
    Commission: float = Field(0.0, title="手续费")
    CloseProfit: float = Field(0.0, title="平仓盈亏")
    PositionProfit: float = Field(0.0, title="持仓盈亏")
    Balance: float = Field(0.0, title="期货结算准备金")
    Available: float = Field(0.0, title="可用资金")
    WithdrawQuota: float = Field(0.0, title="可取资金")
    Reserve: float = Field(0.0, title="基本准备金")
    TradingDay: str = Field("", title="交易日")
    SettlementID: int = Field(0, title="结算编号")
    Credit: float = Field(0.0, title="信用额度")
    Mortgage: float = Field(0.0, title="质押金额")
    ExchangeMargin: float = Field(0.0, title="交易所保证金")
    DeliveryMargin: float = Field(0.0, title="投资者交割保证金")
    ExchangeDeliveryMargin: float = Field(0.0, title="交易所交割保证金")
    ReserveBalance: float = Field(0.0, title="保底期货结算准备金")
    CurrencyID: str = Field("", title="币种代码")
    PreFundMortgageIn: float = Field(0.0, title="上次货币质入金额")
    PreFundMortgageOut: float = Field(0.0, title="上次货币质出金额")
    FundMortgageIn: float = Field(0.0, title="货币质入金额")
    FundMortgageOut: float = Field(0.0, title="货币质出金额")
    FundMortgageAvailable: float = Field(0.0, title="货币质押余额")
    MortgageableFund: float = Field(0.0, title="可质押货币金额")
    SpecProductMargin: float = Field(0.0, title="特殊产品占用保证金")
    SpecProductFrozenMargin: float = Field(0.0, title="特殊产品冻结保证金")
    SpecProductCommission: float = Field(0.0, title="特殊产品手续费")
    SpecProductFrozenCommission: float = Field(0.0, title="特殊产品冻结手续费")
    SpecProductPositionProfit: float = Field(0.0, title="特殊产品持仓盈亏")
    SpecProductCloseProfit: float = Field(0.0, title="特殊产品平仓盈亏")
    SpecProductPositionProfitByAlg: float = Field(0.0,
                                                  title="根据持仓盈亏算法计算的特殊产品持仓盈亏")
    SpecProductExchangeMargin: float = Field(0.0, title="特殊产品交易所保证金")
    FrozenSwap: float = Field(0.0, title="延时换汇冻结金额")
    RemainSwap: float = Field(0.0, title="剩余换汇额度")


class WebCTPReqSyncingTradingAccount(WebCTPRequest):
    SyncingTradingAccount: SyncingTradingAccountField = Field(
        title="正在同步中的交易账号")


class SyncingInvestorPositionField(BaseModel):
    """正在同步中的投资者持仓"""

    reserve1: str = Field("", title="保留的无效字段")
    BrokerID: str = Field("", title="经纪公司代码")
    InvestorID: str = Field("", title="投资者代码")
    PosiDirection: str = Field("", title="持仓多空方向")
    HedgeFlag: str = Field("", title="投机套保标志")
    PositionDate: str = Field("", title="持仓日期")
    YdPosition: int = Field(0, title="上日持仓")
    Position: int = Field(0, title="今日持仓")
    LongFrozen: int = Field(0, title="多头冻结")
    ShortFrozen: int = Field(0, title="空头冻结")
    LongFrozenAmount: float = Field(0.0, title="开仓冻结金额")
    ShortFrozenAmount: float = Field(0.0, title="开仓冻结金额")
    OpenVolume: int = Field(0, title="开仓量")
    CloseVolume: int = Field(0, title="平仓量")
    OpenAmount: float = Field(0.0, title="开仓金额")
    CloseAmount: float = Field(0.0, title="平仓金额")
    PositionCost: float = Field(0.0, title="持仓成本")
    PreMargin: float = Field(0.0, title="上次占用的保证金")
    UseMargin: float = Field(0.0, title="占用的保证金")
    FrozenMargin: float = Field(0.0, title="冻结的保证金")
    FrozenCash: float = Field(0.0, title="冻结的资金")
    FrozenCommission: float = Field(0.0, title="冻结的手续费")
    CashIn: float = Field(0.0, title="资金差额")
    Commission: float = Field(0.0, title="手续费")
    CloseProfit: float = Field(0.0, title="平仓盈亏")
    PositionProfit: float = Field(0.0, title="持仓盈亏")
    PreSettlementPrice: float = Field(0.0, title="上次结算价")
    SettlementPrice: float = Field(0.0, title="本次结算价")
    TradingDay: str = Field("", title="交易日")
    SettlementID: int = Field(0, title="结算编号")
    OpenCost: float = Field(0.0, title="开仓成本")
    ExchangeMargin: float = Field(0.0, title="交易所保证金")
    CombPosition: int = Field(0, title="组合成交形成的持仓")
    CombLongFrozen: int = Field(0, title="组合多头冻结")
    CombShortFrozen: int = Field(0, title="组合空头冻结")
    CloseProfitByDate: float = Field(0.0, title="逐日盯市平仓盈亏")
    CloseProfitByTrade: float = Field(0.0, title="逐笔对冲平仓盈亏")
    TodayPosition: int = Field(0, title="今日持仓")
    MarginRateByMoney: float = Field(0.0, title="保证金率")
    MarginRateByVolume: float = Field(0.0, title="保证金率(按手数)")
    StrikeFrozen: int = Field(0, title="执行冻结")
    StrikeFrozenAmount: float = Field(0.0, title="执行冻结金额")
    AbandonFrozen: int = Field(0, title="放弃执行冻结")
    ExchangeID: str = Field("", title="交易所代码")
    YdStrikeFrozen: int = Field(0, title="执行冻结的昨仓")
    InvestUnitID: str = Field("", title="投资单元代码")
    PositionCostOffset: float = Field(0.0, title="持仓成本差值")
    TasPosition: int = Field(0, title="tas持仓手数")
    TasPositionCost: float = Field(0.0, title="tas持仓成本")
    InstrumentID: str = Field("", title="合约代码")


class WebCTPReqSyncingInvestorPosition(WebCTPRequest):
    SyncingInvestorPosition: SyncingInvestorPositionField = Field(
        title="正在同步中的投资者持仓")


class SyncingInstrumentMarginRateField(BaseModel):
    """正在同步中的合约保证金率"""

    reserve1: str = Field("", title="保留的无效字段")
    InvestorRange: str = Field("", title="投资者范围")
    BrokerID: str = Field("", title="经纪公司代码")
    InvestorID: str = Field("", title="投资者代码")
    HedgeFlag: str = Field("", title="投机套保标志")
    LongMarginRatioByMoney: float = Field(0.0, title="多头保证金率")
    LongMarginRatioByVolume: float = Field(0.0, title="多头保证金费")
    ShortMarginRatioByMoney: float = Field(0.0, title="空头保证金率")
    ShortMarginRatioByVolume: float = Field(0.0, title="空头保证金费")
    IsRelative: int = Field(0, title="是否相对交易所收取")
    InstrumentID: str = Field("", title="合约代码")


class WebCTPReqSyncingInstrumentMarginRate(WebCTPRequest):
    SyncingInstrumentMarginRate: SyncingInstrumentMarginRateField = Field(
        title="正在同步中的合约保证金率")


class SyncingInstrumentCommissionRateField(BaseModel):
    """正在同步中的合约手续费率"""

    reserve1: str = Field("", title="保留的无效字段")
    InvestorRange: str = Field("", title="投资者范围")
    BrokerID: str = Field("", title="经纪公司代码")
    InvestorID: str = Field("", title="投资者代码")
    OpenRatioByMoney: float = Field(0.0, title="开仓手续费率")
    OpenRatioByVolume: float = Field(0.0, title="开仓手续费")
    CloseRatioByMoney: float = Field(0.0, title="平仓手续费率")
    CloseRatioByVolume: float = Field(0.0, title="平仓手续费")
    CloseTodayRatioByMoney: float = Field(0.0, title="平今手续费率")
    CloseTodayRatioByVolume: float = Field(0.0, title="平今手续费")
    InstrumentID: str = Field("", title="合约代码")


class WebCTPReqSyncingInstrumentCommissionRate(WebCTPRequest):
    SyncingInstrumentCommissionRate: SyncingInstrumentCommissionRateField = Field(
        title="正在同步中的合约手续费率")


class SyncingInstrumentTradingRightField(BaseModel):
    """正在同步中的合约交易权限"""

    reserve1: str = Field("", title="保留的无效字段")
    InvestorRange: str = Field("", title="投资者范围")
    BrokerID: str = Field("", title="经纪公司代码")
    InvestorID: str = Field("", title="投资者代码")
    TradingRight: str = Field("", title="交易权限")
    InstrumentID: str = Field("", title="合约代码")


class WebCTPReqSyncingInstrumentTradingRight(WebCTPRequest):
    SyncingInstrumentTradingRight: SyncingInstrumentTradingRightField = Field(
        title="正在同步中的合约交易权限")


class QryOrderField(BaseModel):
    """查询报单"""

    BrokerID: str = Field("", title="经纪公司代码")
    InvestorID: str = Field("", title="投资者代码")
    reserve1: str = Field("", title="保留的无效字段")
    ExchangeID: str = Field("", title="交易所代码")
    OrderSysID: str = Field("", title="报单编号")
    InsertTimeStart: str = Field("", title="开始时间")
    InsertTimeEnd: str = Field("", title="结束时间")
    InvestUnitID: str = Field("", title="投资单元代码")
    InstrumentID: str = Field("", title="合约代码")


class WebCTPReqQryOrder(WebCTPRequest):
    QryOrder: QryOrderField = Field(title="查询报单")


class QryTradeField(BaseModel):
    """查询成交"""

    BrokerID: str = Field("", title="经纪公司代码")
    InvestorID: str = Field("", title="投资者代码")
    reserve1: str = Field("", title="保留的无效字段")
    ExchangeID: str = Field("", title="交易所代码")
    TradeID: str = Field("", title="成交编号")
    TradeTimeStart: str = Field("", title="开始时间")
    TradeTimeEnd: str = Field("", title="结束时间")
    InvestUnitID: str = Field("", title="投资单元代码")
    InstrumentID: str = Field("", title="合约代码")


class WebCTPReqQryTrade(WebCTPRequest):
    QryTrade: QryTradeField = Field(title="查询成交")


class QryInvestorPositionField(BaseModel):
    """查询投资者持仓"""

    BrokerID: str = Field("", title="经纪公司代码")
    InvestorID: str = Field("", title="投资者代码")
    reserve1: str = Field("", title="保留的无效字段")
    ExchangeID: str = Field("", title="交易所代码")
    InvestUnitID: str = Field("", title="投资单元代码")
    InstrumentID: str = Field("", title="合约代码")


class WebCTPReqQryInvestorPosition(WebCTPRequest):
    QryInvestorPosition: QryInvestorPositionField = Field(
        title="查询投资者持仓")


class QryTradingAccountField(BaseModel):
    """查询资金账户"""

    BrokerID: str = Field("", title="经纪公司代码")
    InvestorID: str = Field("", title="投资者代码")
    CurrencyID: str = Field("", title="币种代码")
    BizType: str = Field("", title="业务类型")
    AccountID: str = Field("", title="投资者帐号")


class WebCTPReqQryTradingAccount(WebCTPRequest):
    QryTradingAccount: QryTradingAccountField = Field(title="查询资金账户")


class QryInvestorField(BaseModel):
    """查询投资者"""

    BrokerID: str = Field("", title="经纪公司代码")
    InvestorID: str = Field("", title="投资者代码")


class WebCTPReqQryInvestor(WebCTPRequest):
    QryInvestor: QryInvestorField = Field(title="查询投资者")


class QryTradingCodeField(BaseModel):
    """查询交易编码"""

    BrokerID: str = Field("", title="经纪公司代码")
    InvestorID: str = Field("", title="投资者代码")
    ExchangeID: str = Field("", title="交易所代码")
    ClientID: str = Field("", title="客户代码")
    ClientIDType: str = Field("", title="交易编码类型")
    InvestUnitID: str = Field("", title="投资单元代码")


class WebCTPReqQryTradingCode(WebCTPRequest):
    QryTradingCode: QryTradingCodeField = Field(title="查询交易编码")


class QryInvestorGroupField(BaseModel):
    """查询投资者组"""

    BrokerID: str = Field("", title="经纪公司代码")


class WebCTPReqQryInvestorGroup(WebCTPRequest):
    QryInvestorGroup: QryInvestorGroupField = Field(title="查询投资者组")


class QryInstrumentMarginRateField(BaseModel):
    """查询合约保证金率"""

    BrokerID: str = Field("", title="经纪公司代码")
    InvestorID: str = Field("", title="投资者代码")
    reserve1: str = Field("", title="保留的无效字段")
    HedgeFlag: str = Field("", title="投机套保标志")
    ExchangeID: str = Field("", title="交易所代码")
    InvestUnitID: str = Field("", title="投资单元代码")
    InstrumentID: str = Field("", title="合约代码")


class WebCTPReqQryInstrumentMarginRate(WebCTPRequest):
    QryInstrumentMarginRate: QryInstrumentMarginRateField = Field(
        title="查询合约保证金率")


class QryInstrumentCommissionRateField(BaseModel):
    """查询手续费率"""

    BrokerID: str = Field("", title="经纪公司代码")
    InvestorID: str = Field("", title="投资者代码")
    reserve1: str = Field("", title="保留的无效字段")
    ExchangeID: str = Field("", title="交易所代码")
    InvestUnitID: str = Field("", title="投资单元代码")
    InstrumentID: str = Field("", title="合约代码")


class WebCTPReqQryInstrumentCommissionRate(WebCTPRequest):
    QryInstrumentCommissionRate: QryInstrumentCommissionRateField = Field(
        title="查询手续费率")


class QryInstrumentTradingRightField(BaseModel):
    """查询合约交易权限"""

    BrokerID: str = Field("", title="经纪公司代码")
    InvestorID: str = Field("", title="投资者代码")
    reserve1: str = Field("", title="保留的无效字段")
    InstrumentID: str = Field("", title="合约代码")


class WebCTPReqQryInstrumentTradingRight(WebCTPRequest):
    QryInstrumentTradingRight: QryInstrumentTradingRightField = Field(
        title="查询合约交易权限")


class QryBrokerField(BaseModel):
    """查询经纪公司"""

    BrokerID: str = Field("", title="经纪公司代码")


class WebCTPReqQryBroker(WebCTPRequest):
    QryBroker: QryBrokerField = Field(title="查询经纪公司")


class QryTraderField(BaseModel):
    """查询交易员"""

    ExchangeID: str = Field("", title="交易所代码")
    ParticipantID: str = Field("", title="会员代码")
    TraderID: str = Field("", title="交易所交易员代码")


class WebCTPReqQryTrader(WebCTPRequest):
    QryTrader: QryTraderField = Field(title="查询交易员")


class QrySuperUserFunctionField(BaseModel):
    """查询管理用户功能权限"""

    UserID: str = Field("", title="用户代码")


class WebCTPReqQrySuperUserFunction(WebCTPRequest):
    QrySuperUserFunction: QrySuperUserFunctionField = Field(
        title="查询管理用户功能权限")


class QryUserSessionField(BaseModel):
    """查询用户会话"""

    FrontID: int = Field(0, title="前置编号")
    SessionID: int = Field(0, title="会话编号")
    BrokerID: str = Field("", title="经纪公司代码")
    UserID: str = Field("", title="用户代码")


class WebCTPReqQryUserSession(WebCTPRequest):
    QryUserSession: QryUserSessionField = Field(title="查询用户会话")


class QryPartBrokerField(BaseModel):
    """查询经纪公司会员代码"""

    ExchangeID: str = Field("", title="交易所代码")
    BrokerID: str = Field("", title="经纪公司代码")
    ParticipantID: str = Field("", title="会员代码")


class WebCTPReqQryPartBroker(WebCTPRequest):
    QryPartBroker: QryPartBrokerField = Field(title="查询经纪公司会员代码")


class QryFrontStatusField(BaseModel):
    """查询前置状态"""

    FrontID: int = Field(0, title="前置编号")


class WebCTPReqQryFrontStatus(WebCTPRequest):
    QryFrontStatus: QryFrontStatusField = Field(title="查询前置状态")


class QryExchangeOrderField(BaseModel):
    """查询交易所报单"""

    ParticipantID: str = Field("", title="会员代码")
    ClientID: str = Field("", title="客户代码")
    reserve1: str = Field("", title="保留的无效字段")
    ExchangeID: str = Field("", title="交易所代码")
    TraderID: str = Field("", title="交易所交易员代码")
    ExchangeInstID: str = Field("", title="合约在交易所的代码")


class WebCTPReqQryExchangeOrder(WebCTPRequest):
    QryExchangeOrder: QryExchangeOrderField = Field(title="查询交易所报单")


class QryOrderActionField(BaseModel):
    """查询报单操作"""

    BrokerID: str = Field("", title="经纪公司代码")
    InvestorID: str = Field("", title="投资者代码")
    ExchangeID: str = Field("", title="交易所代码")


class WebCTPReqQryOrderAction(WebCTPRequest):
    QryOrderAction: QryOrderActionField = Field(title="查询报单操作")


class QryExchangeOrderActionField(BaseModel):
    """查询交易所报单操作"""

    ParticipantID: str = Field("", title="会员代码")
    ClientID: str = Field("", title="客户代码")
    ExchangeID: str = Field("", title="交易所代码")
    TraderID: str = Field("", title="交易所交易员代码")


class WebCTPReqQryExchangeOrderAction(WebCTPRequest):
    QryExchangeOrderAction: QryExchangeOrderActionField = Field(
        title="查询交易所报单操作")


class QrySuperUserField(BaseModel):
    """查询管理用户"""

    UserID: str = Field("", title="用户代码")


class WebCTPReqQrySuperUser(WebCTPRequest):
    QrySuperUser: QrySuperUserField = Field(title="查询管理用户")


class QryExchangeField(BaseModel):
    """查询交易所"""

    ExchangeID: str = Field("", title="交易所代码")


class WebCTPReqQryExchange(WebCTPRequest):
    QryExchange: QryExchangeField = Field(title="查询交易所")


class QryProductField(BaseModel):
    """查询产品"""

    reserve1: str = Field("", title="保留的无效字段")
    ProductClass: str = Field("", title="产品类型")
    ExchangeID: str = Field("", title="交易所代码")
    ProductID: str = Field("", title="产品代码")


class WebCTPReqQryProduct(WebCTPRequest):
    QryProduct: QryProductField = Field(title="查询产品")


class QryInstrumentField(BaseModel):
    """查询合约"""

    reserve1: str = Field("", title="保留的无效字段")
    ExchangeID: str = Field("", title="交易所代码")
    reserve2: str = Field("", title="保留的无效字段")
    reserve3: str = Field("", title="保留的无效字段")
    InstrumentID: str = Field("", title="合约代码")
    ExchangeInstID: str = Field("", title="合约在交易所的代码")
    ProductID: str = Field("", title="产品代码")


class WebCTPReqQryInstrument(WebCTPRequest):
    QryInstrument: QryInstrumentField = Field(title="查询合约")


class QryDepthMarketDataField(BaseModel):
    """查询行情"""

    reserve1: str = Field("", title="保留的无效字段")
    ExchangeID: str = Field("", title="交易所代码")
    InstrumentID: str = Field("", title="合约代码")


class WebCTPReqQryDepthMarketData(WebCTPRequest):
    QryDepthMarketData: QryDepthMarketDataField = Field(title="查询行情")


class QryBrokerUserField(BaseModel):
    """查询经纪公司用户"""

    BrokerID: str = Field("", title="经纪公司代码")
    UserID: str = Field("", title="用户代码")


class WebCTPReqQryBrokerUser(WebCTPRequest):
    QryBrokerUser: QryBrokerUserField = Field(title="查询经纪公司用户")


class QryBrokerUserFunctionField(BaseModel):
    """查询经纪公司用户权限"""

    BrokerID: str = Field("", title="经纪公司代码")
    UserID: str = Field("", title="用户代码")


class WebCTPReqQryBrokerUserFunction(WebCTPRequest):
    QryBrokerUserFunction: QryBrokerUserFunctionField = Field(
        title="查询经纪公司用户权限")


class QryTraderOfferField(BaseModel):
    """查询交易员报盘机"""

    ExchangeID: str = Field("", title="交易所代码")
    ParticipantID: str = Field("", title="会员代码")
    TraderID: str = Field("", title="交易所交易员代码")


class WebCTPReqQryTraderOffer(WebCTPRequest):
    QryTraderOffer: QryTraderOfferField = Field(title="查询交易员报盘机")


class QrySyncDepositField(BaseModel):
    """查询出入金流水"""

    BrokerID: str = Field("", title="经纪公司代码")
    DepositSeqNo: str = Field("", title="出入金流水号")


class WebCTPReqQrySyncDeposit(WebCTPRequest):
    QrySyncDeposit: QrySyncDepositField = Field(title="查询出入金流水")


class QrySettlementInfoField(BaseModel):
    """查询投资者结算结果"""

    BrokerID: str = Field("", title="经纪公司代码")
    InvestorID: str = Field("", title="投资者代码")
    TradingDay: str = Field("", title="交易日")
    AccountID: str = Field("", title="投资者帐号")
    CurrencyID: str = Field("", title="币种代码")


class WebCTPReqQrySettlementInfo(WebCTPRequest):
    QrySettlementInfo: QrySettlementInfoField = Field(
        title="查询投资者结算结果")


class QryExchangeMarginRateField(BaseModel):
    """查询交易所保证金率"""

    BrokerID: str = Field("", title="经纪公司代码")
    reserve1: str = Field("", title="保留的无效字段")
    HedgeFlag: str = Field("", title="投机套保标志")
    ExchangeID: str = Field("", title="交易所代码")
    InstrumentID: str = Field("", title="合约代码")


class WebCTPReqQryExchangeMarginRate(WebCTPRequest):
    QryExchangeMarginRate: QryExchangeMarginRateField = Field(
        title="查询交易所保证金率")


class QryExchangeMarginRateAdjustField(BaseModel):
    """查询交易所调整保证金率"""

    BrokerID: str = Field("", title="经纪公司代码")
    reserve1: str = Field("", title="保留的无效字段")
    HedgeFlag: str = Field("", title="投机套保标志")
    InstrumentID: str = Field("", title="合约代码")


class WebCTPReqQryExchangeMarginRateAdjust(WebCTPRequest):
    QryExchangeMarginRateAdjust: QryExchangeMarginRateAdjustField = Field(
        title="查询交易所调整保证金率")


class QryExchangeRateField(BaseModel):
    """查询汇率"""

    BrokerID: str = Field("", title="经纪公司代码")
    FromCurrencyID: str = Field("", title="源币种")
    ToCurrencyID: str = Field("", title="目标币种")


class WebCTPReqQryExchangeRate(WebCTPRequest):
    QryExchangeRate: QryExchangeRateField = Field(title="查询汇率")


class QrySyncFundMortgageField(BaseModel):
    """查询货币质押流水"""

    BrokerID: str = Field("", title="经纪公司代码")
    MortgageSeqNo: str = Field("", title="货币质押流水号")


class WebCTPReqQrySyncFundMortgage(WebCTPRequest):
    QrySyncFundMortgage: QrySyncFundMortgageField = Field(
        title="查询货币质押流水")


class QryHisOrderField(BaseModel):
    """查询报单"""

    BrokerID: str = Field("", title="经纪公司代码")
    InvestorID: str = Field("", title="投资者代码")
    reserve1: str = Field("", title="保留的无效字段")
    ExchangeID: str = Field("", title="交易所代码")
    OrderSysID: str = Field("", title="报单编号")
    InsertTimeStart: str = Field("", title="开始时间")
    InsertTimeEnd: str = Field("", title="结束时间")
    TradingDay: str = Field("", title="交易日")
    SettlementID: int = Field(0, title="结算编号")
    InstrumentID: str = Field("", title="合约代码")


class WebCTPReqQryHisOrder(WebCTPRequest):
    QryHisOrder: QryHisOrderField = Field(title="查询报单")


class OptionInstrMiniMarginField(BaseModel):
    """当前期权合约最小保证金"""

    reserve1: str = Field("", title="保留的无效字段")
    InvestorRange: str = Field("", title="投资者范围")
    BrokerID: str = Field("", title="经纪公司代码")
    InvestorID: str = Field("", title="投资者代码")
    MinMargin: float = Field(0.0, title="单位（手）期权合约最小保证金")
    ValueMethod: str = Field("", title="取值方式")
    IsRelative: int = Field(0, title="是否跟随交易所收取")
    InstrumentID: str = Field("", title="合约代码")


class WebCTPReqOptionInstrMiniMargin(WebCTPRequest):
    OptionInstrMiniMargin: OptionInstrMiniMarginField = Field(
        title="当前期权合约最小保证金")


class OptionInstrMarginAdjustField(BaseModel):
    """当前期权合约保证金调整系数"""

    reserve1: str = Field("", title="保留的无效字段")
    InvestorRange: str = Field("", title="投资者范围")
    BrokerID: str = Field("", title="经纪公司代码")
    InvestorID: str = Field("", title="投资者代码")
    SShortMarginRatioByMoney: float = Field(0.0,
                                            title="投机空头保证金调整系数")
    SShortMarginRatioByVolume: float = Field(0.0,
                                             title="投机空头保证金调整系数")
    HShortMarginRatioByMoney: float = Field(0.0,
                                            title="保值空头保证金调整系数")
    HShortMarginRatioByVolume: float = Field(0.0,
                                             title="保值空头保证金调整系数")
    AShortMarginRatioByMoney: float = Field(0.0,
                                            title="套利空头保证金调整系数")
    AShortMarginRatioByVolume: float = Field(0.0,
                                             title="套利空头保证金调整系数")
    IsRelative: int = Field(0, title="是否跟随交易所收取")
    MShortMarginRatioByMoney: float = Field(0.0,
                                            title="做市商空头保证金调整系数")
    MShortMarginRatioByVolume: float = Field(0.0,
                                             title="做市商空头保证金调整系数")
    InstrumentID: str = Field("", title="合约代码")


class WebCTPReqOptionInstrMarginAdjust(WebCTPRequest):
    OptionInstrMarginAdjust: OptionInstrMarginAdjustField = Field(
        title="当前期权合约保证金调整系数")


class OptionInstrCommRateField(BaseModel):
    """当前期权合约手续费的详细内容"""

    reserve1: str = Field("", title="保留的无效字段")
    InvestorRange: str = Field("", title="投资者范围")
    BrokerID: str = Field("", title="经纪公司代码")
    InvestorID: str = Field("", title="投资者代码")
    OpenRatioByMoney: float = Field(0.0, title="开仓手续费率")
    OpenRatioByVolume: float = Field(0.0, title="开仓手续费")
    CloseRatioByMoney: float = Field(0.0, title="平仓手续费率")
    CloseRatioByVolume: float = Field(0.0, title="平仓手续费")
    CloseTodayRatioByMoney: float = Field(0.0, title="平今手续费率")
    CloseTodayRatioByVolume: float = Field(0.0, title="平今手续费")
    StrikeRatioByMoney: float = Field(0.0, title="执行手续费率")
    StrikeRatioByVolume: float = Field(0.0, title="执行手续费")
    ExchangeID: str = Field("", title="交易所代码")
    InvestUnitID: str = Field("", title="投资单元代码")
    InstrumentID: str = Field("", title="合约代码")


class WebCTPReqOptionInstrCommRate(WebCTPRequest):
    OptionInstrCommRate: OptionInstrCommRateField = Field(
        title="当前期权合约手续费的详细内容")


class OptionInstrTradeCostField(BaseModel):
    """期权交易成本"""

    BrokerID: str = Field("", title="经纪公司代码")
    InvestorID: str = Field("", title="投资者代码")
    reserve1: str = Field("", title="保留的无效字段")
    HedgeFlag: str = Field("", title="投机套保标志")
    FixedMargin: float = Field(0.0, title="期权合约保证金不变部分")
    MiniMargin: float = Field(0.0, title="期权合约最小保证金")
    Royalty: float = Field(0.0, title="期权合约权利金")
    ExchFixedMargin: float = Field(0.0, title="交易所期权合约保证金不变部分")
    ExchMiniMargin: float = Field(0.0, title="交易所期权合约最小保证金")
    ExchangeID: str = Field("", title="交易所代码")
    InvestUnitID: str = Field("", title="投资单元代码")
    InstrumentID: str = Field("", title="合约代码")


class WebCTPReqOptionInstrTradeCost(WebCTPRequest):
    OptionInstrTradeCost: OptionInstrTradeCostField = Field(
        title="期权交易成本")


class QryOptionInstrTradeCostField(BaseModel):
    """期权交易成本查询"""

    BrokerID: str = Field("", title="经纪公司代码")
    InvestorID: str = Field("", title="投资者代码")
    reserve1: str = Field("", title="保留的无效字段")
    HedgeFlag: str = Field("", title="投机套保标志")
    InputPrice: float = Field(0.0, title="期权合约报价")
    UnderlyingPrice: float = Field(0.0, title="标的价格,填0则用昨结算价")
    ExchangeID: str = Field("", title="交易所代码")
    InvestUnitID: str = Field("", title="投资单元代码")
    InstrumentID: str = Field("", title="合约代码")


class WebCTPReqQryOptionInstrTradeCost(WebCTPRequest):
    QryOptionInstrTradeCost: QryOptionInstrTradeCostField = Field(
        title="期权交易成本查询")


class QryOptionInstrCommRateField(BaseModel):
    """期权手续费率查询"""

    BrokerID: str = Field("", title="经纪公司代码")
    InvestorID: str = Field("", title="投资者代码")
    reserve1: str = Field("", title="保留的无效字段")
    ExchangeID: str = Field("", title="交易所代码")
    InvestUnitID: str = Field("", title="投资单元代码")
    InstrumentID: str = Field("", title="合约代码")


class WebCTPReqQryOptionInstrCommRate(WebCTPRequest):
    QryOptionInstrCommRate: QryOptionInstrCommRateField = Field(
        title="期权手续费率查询")


class IndexPriceField(BaseModel):
    """股指现货指数"""

    BrokerID: str = Field("", title="经纪公司代码")
    reserve1: str = Field("", title="保留的无效字段")
    ClosePrice: float = Field(0.0, title="指数现货收盘价")
    InstrumentID: str = Field("", title="合约代码")


class WebCTPReqIndexPrice(WebCTPRequest):
    IndexPrice: IndexPriceField = Field(title="股指现货指数")


class InputExecOrderField(BaseModel):
    """输入的执行宣告"""

    BrokerID: str = Field("", title="经纪公司代码")
    InvestorID: str = Field("", title="投资者代码")
    reserve1: str = Field("", title="保留的无效字段")
    ExecOrderRef: str = Field("", title="执行宣告引用")
    UserID: str = Field("", title="用户代码")
    Volume: int = Field(0, title="数量")
    RequestID: int = Field(0, title="请求编号")
    BusinessUnit: str = Field("", title="业务单元")
    OffsetFlag: str = Field("", title="开平标志")
    HedgeFlag: str = Field("", title="投机套保标志")
    ActionType: str = Field("", title="执行类型")
    PosiDirection: str = Field("", title="保留头寸申请的持仓方向")
    ReservePositionFlag: str = Field("",
                                     title="期权行权后是否保留期货头寸的标记,该字段已废弃")
    CloseFlag: str = Field("", title="期权行权后生成的头寸是否自动平仓")
    ExchangeID: str = Field("", title="交易所代码")
    InvestUnitID: str = Field("", title="投资单元代码")
    AccountID: str = Field("", title="资金账号")
    CurrencyID: str = Field("", title="币种代码")
    ClientID: str = Field("", title="交易编码")
    reserve2: str = Field("", title="保留的无效字段")
    MacAddress: str = Field("", title="Mac地址")
    InstrumentID: str = Field("", title="合约代码")
    IPAddress: str = Field("", title="IP地址")


class WebCTPReqInputExecOrder(WebCTPRequest):
    InputExecOrder: InputExecOrderField = Field(title="输入的执行宣告")


class InputExecOrderActionField(BaseModel):
    """输入执行宣告操作"""

    BrokerID: str = Field("", title="经纪公司代码")
    InvestorID: str = Field("", title="投资者代码")
    ExecOrderActionRef: int = Field(0, title="执行宣告操作引用")
    ExecOrderRef: str = Field("", title="执行宣告引用")
    RequestID: int = Field(0, title="请求编号")
    FrontID: int = Field(0, title="前置编号")
    SessionID: int = Field(0, title="会话编号")
    ExchangeID: str = Field("", title="交易所代码")
    ExecOrderSysID: str = Field("", title="执行宣告操作编号")
    ActionFlag: str = Field("", title="操作标志")
    UserID: str = Field("", title="用户代码")
    reserve1: str = Field("", title="保留的无效字段")
    InvestUnitID: str = Field("", title="投资单元代码")
    reserve2: str = Field("", title="保留的无效字段")
    MacAddress: str = Field("", title="Mac地址")
    InstrumentID: str = Field("", title="合约代码")
    IPAddress: str = Field("", title="IP地址")


class WebCTPReqInputExecOrderAction(WebCTPRequest):
    InputExecOrderAction: InputExecOrderActionField = Field(
        title="输入执行宣告操作")


class ExecOrderField(BaseModel):
    """执行宣告"""

    BrokerID: str = Field("", title="经纪公司代码")
    InvestorID: str = Field("", title="投资者代码")
    reserve1: str = Field("", title="保留的无效字段")
    ExecOrderRef: str = Field("", title="执行宣告引用")
    UserID: str = Field("", title="用户代码")
    Volume: int = Field(0, title="数量")
    RequestID: int = Field(0, title="请求编号")
    BusinessUnit: str = Field("", title="业务单元")
    OffsetFlag: str = Field("", title="开平标志")
    HedgeFlag: str = Field("", title="投机套保标志")
    ActionType: str = Field("", title="执行类型")
    PosiDirection: str = Field("", title="保留头寸申请的持仓方向")
    ReservePositionFlag: str = Field("",
                                     title="期权行权后是否保留期货头寸的标记,该字段已废弃")
    CloseFlag: str = Field("", title="期权行权后生成的头寸是否自动平仓")
    ExecOrderLocalID: str = Field("", title="本地执行宣告编号")
    ExchangeID: str = Field("", title="交易所代码")
    ParticipantID: str = Field("", title="会员代码")
    ClientID: str = Field("", title="客户代码")
    reserve2: str = Field("", title="保留的无效字段")
    TraderID: str = Field("", title="交易所交易员代码")
    InstallID: int = Field(0, title="安装编号")
    OrderSubmitStatus: str = Field("", title="执行宣告提交状态")
    NotifySequence: int = Field(0, title="报单提示序号")
    TradingDay: str = Field("", title="交易日")
    SettlementID: int = Field(0, title="结算编号")
    ExecOrderSysID: str = Field("", title="执行宣告编号")
    InsertDate: str = Field("", title="报单日期")
    InsertTime: str = Field("", title="插入时间")
    CancelTime: str = Field("", title="撤销时间")
    ExecResult: str = Field("", title="执行结果")
    ClearingPartID: str = Field("", title="结算会员编号")
    SequenceNo: int = Field(0, title="序号")
    FrontID: int = Field(0, title="前置编号")
    SessionID: int = Field(0, title="会话编号")
    UserProductInfo: str = Field("", title="用户端产品信息")
    StatusMsg: str = Field("", title="状态信息")
    ActiveUserID: str = Field("", title="操作用户代码")
    BrokerExecOrderSeq: int = Field(0, title="经纪公司报单编号")
    BranchID: str = Field("", title="营业部编号")
    InvestUnitID: str = Field("", title="投资单元代码")
    AccountID: str = Field("", title="资金账号")
    CurrencyID: str = Field("", title="币种代码")
    reserve3: str = Field("", title="保留的无效字段")
    MacAddress: str = Field("", title="Mac地址")
    InstrumentID: str = Field("", title="合约代码")
    ExchangeInstID: str = Field("", title="合约在交易所的代码")
    IPAddress: str = Field("", title="IP地址")


class WebCTPReqExecOrder(WebCTPRequest):
    ExecOrder: ExecOrderField = Field(title="执行宣告")


class ExecOrderActionField(BaseModel):
    """执行宣告操作"""

    BrokerID: str = Field("", title="经纪公司代码")
    InvestorID: str = Field("", title="投资者代码")
    ExecOrderActionRef: int = Field(0, title="执行宣告操作引用")
    ExecOrderRef: str = Field("", title="执行宣告引用")
    RequestID: int = Field(0, title="请求编号")
    FrontID: int = Field(0, title="前置编号")
    SessionID: int = Field(0, title="会话编号")
    ExchangeID: str = Field("", title="交易所代码")
    ExecOrderSysID: str = Field("", title="执行宣告操作编号")
    ActionFlag: str = Field("", title="操作标志")
    ActionDate: str = Field("", title="操作日期")
    ActionTime: str = Field("", title="操作时间")
    TraderID: str = Field("", title="交易所交易员代码")
    InstallID: int = Field(0, title="安装编号")
    ExecOrderLocalID: str = Field("", title="本地执行宣告编号")
    ActionLocalID: str = Field("", title="操作本地编号")
    ParticipantID: str = Field("", title="会员代码")
    ClientID: str = Field("", title="客户代码")
    BusinessUnit: str = Field("", title="业务单元")
    OrderActionStatus: str = Field("", title="报单操作状态")
    UserID: str = Field("", title="用户代码")
    ActionType: str = Field("", title="执行类型")
    StatusMsg: str = Field("", title="状态信息")
    reserve1: str = Field("", title="保留的无效字段")
    BranchID: str = Field("", title="营业部编号")
    InvestUnitID: str = Field("", title="投资单元代码")
    reserve2: str = Field("", title="保留的无效字段")
    MacAddress: str = Field("", title="Mac地址")
    InstrumentID: str = Field("", title="合约代码")
    IPAddress: str = Field("", title="IP地址")


class WebCTPReqExecOrderAction(WebCTPRequest):
    ExecOrderAction: ExecOrderActionField = Field(title="执行宣告操作")


class QryExecOrderField(BaseModel):
    """执行宣告查询"""

    BrokerID: str = Field("", title="经纪公司代码")
    InvestorID: str = Field("", title="投资者代码")
    reserve1: str = Field("", title="保留的无效字段")
    ExchangeID: str = Field("", title="交易所代码")
    ExecOrderSysID: str = Field("", title="执行宣告编号")
    InsertTimeStart: str = Field("", title="开始时间")
    InsertTimeEnd: str = Field("", title="结束时间")
    InstrumentID: str = Field("", title="合约代码")


class WebCTPReqQryExecOrder(WebCTPRequest):
    QryExecOrder: QryExecOrderField = Field(title="执行宣告查询")


class ExchangeExecOrderField(BaseModel):
    """交易所执行宣告信息"""

    Volume: int = Field(0, title="数量")
    RequestID: int = Field(0, title="请求编号")
    BusinessUnit: str = Field("", title="业务单元")
    OffsetFlag: str = Field("", title="开平标志")
    HedgeFlag: str = Field("", title="投机套保标志")
    ActionType: str = Field("", title="执行类型")
    PosiDirection: str = Field("", title="保留头寸申请的持仓方向")
    ReservePositionFlag: str = Field("",
                                     title="期权行权后是否保留期货头寸的标记,该字段已废弃")
    CloseFlag: str = Field("", title="期权行权后生成的头寸是否自动平仓")
    ExecOrderLocalID: str = Field("", title="本地执行宣告编号")
    ExchangeID: str = Field("", title="交易所代码")
    ParticipantID: str = Field("", title="会员代码")
    ClientID: str = Field("", title="客户代码")
    reserve1: str = Field("", title="保留的无效字段")
    TraderID: str = Field("", title="交易所交易员代码")
    InstallID: int = Field(0, title="安装编号")
    OrderSubmitStatus: str = Field("", title="执行宣告提交状态")
    NotifySequence: int = Field(0, title="报单提示序号")
    TradingDay: str = Field("", title="交易日")
    SettlementID: int = Field(0, title="结算编号")
    ExecOrderSysID: str = Field("", title="执行宣告编号")
    InsertDate: str = Field("", title="报单日期")
    InsertTime: str = Field("", title="插入时间")
    CancelTime: str = Field("", title="撤销时间")
    ExecResult: str = Field("", title="执行结果")
    ClearingPartID: str = Field("", title="结算会员编号")
    SequenceNo: int = Field(0, title="序号")
    BranchID: str = Field("", title="营业部编号")
    reserve2: str = Field("", title="保留的无效字段")
    MacAddress: str = Field("", title="Mac地址")
    ExchangeInstID: str = Field("", title="合约在交易所的代码")
    IPAddress: str = Field("", title="IP地址")


class WebCTPReqExchangeExecOrder(WebCTPRequest):
    ExchangeExecOrder: ExchangeExecOrderField = Field(
        title="交易所执行宣告信息")


class QryExchangeExecOrderField(BaseModel):
    """交易所执行宣告查询"""

    ParticipantID: str = Field("", title="会员代码")
    ClientID: str = Field("", title="客户代码")
    reserve1: str = Field("", title="保留的无效字段")
    ExchangeID: str = Field("", title="交易所代码")
    TraderID: str = Field("", title="交易所交易员代码")
    ExchangeInstID: str = Field("", title="合约在交易所的代码")


class WebCTPReqQryExchangeExecOrder(WebCTPRequest):
    QryExchangeExecOrder: QryExchangeExecOrderField = Field(
        title="交易所执行宣告查询")


class QryExecOrderActionField(BaseModel):
    """执行宣告操作查询"""

    BrokerID: str = Field("", title="经纪公司代码")
    InvestorID: str = Field("", title="投资者代码")
    ExchangeID: str = Field("", title="交易所代码")


class WebCTPReqQryExecOrderAction(WebCTPRequest):
    QryExecOrderAction: QryExecOrderActionField = Field(
        title="执行宣告操作查询")


class ExchangeExecOrderActionField(BaseModel):
    """交易所执行宣告操作"""

    ExchangeID: str = Field("", title="交易所代码")
    ExecOrderSysID: str = Field("", title="执行宣告操作编号")
    ActionFlag: str = Field("", title="操作标志")
    ActionDate: str = Field("", title="操作日期")
    ActionTime: str = Field("", title="操作时间")
    TraderID: str = Field("", title="交易所交易员代码")
    InstallID: int = Field(0, title="安装编号")
    ExecOrderLocalID: str = Field("", title="本地执行宣告编号")
    ActionLocalID: str = Field("", title="操作本地编号")
    ParticipantID: str = Field("", title="会员代码")
    ClientID: str = Field("", title="客户代码")
    BusinessUnit: str = Field("", title="业务单元")
    OrderActionStatus: str = Field("", title="报单操作状态")
    UserID: str = Field("", title="用户代码")
    ActionType: str = Field("", title="执行类型")
    BranchID: str = Field("", title="营业部编号")
    reserve1: str = Field("", title="保留的无效字段")
    MacAddress: str = Field("", title="Mac地址")
    reserve2: str = Field("", title="保留的无效字段")
    Volume: int = Field(0, title="数量")
    IPAddress: str = Field("", title="IP地址")
    ExchangeInstID: str = Field("", title="合约在交易所的代码")


class WebCTPReqExchangeExecOrderAction(WebCTPRequest):
    ExchangeExecOrderAction: ExchangeExecOrderActionField = Field(
        title="交易所执行宣告操作")


class QryExchangeExecOrderActionField(BaseModel):
    """交易所执行宣告操作查询"""

    ParticipantID: str = Field("", title="会员代码")
    ClientID: str = Field("", title="客户代码")
    ExchangeID: str = Field("", title="交易所代码")
    TraderID: str = Field("", title="交易所交易员代码")


class WebCTPReqQryExchangeExecOrderAction(WebCTPRequest):
    QryExchangeExecOrderAction: QryExchangeExecOrderActionField = Field(
        title="交易所执行宣告操作查询")


class ErrExecOrderField(BaseModel):
    """错误执行宣告"""

    BrokerID: str = Field("", title="经纪公司代码")
    InvestorID: str = Field("", title="投资者代码")
    reserve1: str = Field("", title="保留的无效字段")
    ExecOrderRef: str = Field("", title="执行宣告引用")
    UserID: str = Field("", title="用户代码")
    Volume: int = Field(0, title="数量")
    RequestID: int = Field(0, title="请求编号")
    BusinessUnit: str = Field("", title="业务单元")
    OffsetFlag: str = Field("", title="开平标志")
    HedgeFlag: str = Field("", title="投机套保标志")
    ActionType: str = Field("", title="执行类型")
    PosiDirection: str = Field("", title="保留头寸申请的持仓方向")
    ReservePositionFlag: str = Field("",
                                     title="期权行权后是否保留期货头寸的标记,该字段已废弃")
    CloseFlag: str = Field("", title="期权行权后生成的头寸是否自动平仓")
    ExchangeID: str = Field("", title="交易所代码")
    InvestUnitID: str = Field("", title="投资单元代码")
    AccountID: str = Field("", title="资金账号")
    CurrencyID: str = Field("", title="币种代码")
    ClientID: str = Field("", title="交易编码")
    reserve2: str = Field("", title="保留的无效字段")
    MacAddress: str = Field("", title="Mac地址")
    ErrorID: int = Field(0, title="错误代码")
    ErrorMsg: str = Field("", title="错误信息")
    InstrumentID: str = Field("", title="合约代码")
    IPAddress: str = Field("", title="IP地址")


class WebCTPReqErrExecOrder(WebCTPRequest):
    ErrExecOrder: ErrExecOrderField = Field(title="错误执行宣告")


class QryErrExecOrderField(BaseModel):
    """查询错误执行宣告"""

    BrokerID: str = Field("", title="经纪公司代码")
    InvestorID: str = Field("", title="投资者代码")


class WebCTPReqQryErrExecOrder(WebCTPRequest):
    QryErrExecOrder: QryErrExecOrderField = Field(title="查询错误执行宣告")


class ErrExecOrderActionField(BaseModel):
    """错误执行宣告操作"""

    BrokerID: str = Field("", title="经纪公司代码")
    InvestorID: str = Field("", title="投资者代码")
    ExecOrderActionRef: int = Field(0, title="执行宣告操作引用")
    ExecOrderRef: str = Field("", title="执行宣告引用")
    RequestID: int = Field(0, title="请求编号")
    FrontID: int = Field(0, title="前置编号")
    SessionID: int = Field(0, title="会话编号")
    ExchangeID: str = Field("", title="交易所代码")
    ExecOrderSysID: str = Field("", title="执行宣告操作编号")
    ActionFlag: str = Field("", title="操作标志")
    UserID: str = Field("", title="用户代码")
    reserve1: str = Field("", title="保留的无效字段")
    InvestUnitID: str = Field("", title="投资单元代码")
    reserve2: str = Field("", title="保留的无效字段")
    MacAddress: str = Field("", title="Mac地址")
    ErrorID: int = Field(0, title="错误代码")
    ErrorMsg: str = Field("", title="错误信息")
    InstrumentID: str = Field("", title="合约代码")
    IPAddress: str = Field("", title="IP地址")


class WebCTPReqErrExecOrderAction(WebCTPRequest):
    ErrExecOrderAction: ErrExecOrderActionField = Field(
        title="错误执行宣告操作")


class QryErrExecOrderActionField(BaseModel):
    """查询错误执行宣告操作"""

    BrokerID: str = Field("", title="经纪公司代码")
    InvestorID: str = Field("", title="投资者代码")


class WebCTPReqQryErrExecOrderAction(WebCTPRequest):
    QryErrExecOrderAction: QryErrExecOrderActionField = Field(
        title="查询错误执行宣告操作")


class OptionInstrTradingRightField(BaseModel):
    """投资者期权合约交易权限"""

    reserve1: str = Field("", title="保留的无效字段")
    InvestorRange: str = Field("", title="投资者范围")
    BrokerID: str = Field("", title="经纪公司代码")
    InvestorID: str = Field("", title="投资者代码")
    Direction: str = Field("", title="买卖方向")
    TradingRight: str = Field("", title="交易权限")
    InstrumentID: str = Field("", title="合约代码")


class WebCTPReqOptionInstrTradingRight(WebCTPRequest):
    OptionInstrTradingRight: OptionInstrTradingRightField = Field(
        title="投资者期权合约交易权限")


class QryOptionInstrTradingRightField(BaseModel):
    """查询期权合约交易权限"""

    BrokerID: str = Field("", title="经纪公司代码")
    InvestorID: str = Field("", title="投资者代码")
    reserve1: str = Field("", title="保留的无效字段")
    Direction: str = Field("", title="买卖方向")
    InstrumentID: str = Field("", title="合约代码")


class WebCTPReqQryOptionInstrTradingRight(WebCTPRequest):
    QryOptionInstrTradingRight: QryOptionInstrTradingRightField = Field(
        title="查询期权合约交易权限")


class InputForQuoteField(BaseModel):
    """输入的询价"""

    BrokerID: str = Field("", title="经纪公司代码")
    InvestorID: str = Field("", title="投资者代码")
    reserve1: str = Field("", title="保留的无效字段")
    ForQuoteRef: str = Field("", title="询价引用")
    UserID: str = Field("", title="用户代码")
    ExchangeID: str = Field("", title="交易所代码")
    InvestUnitID: str = Field("", title="投资单元代码")
    reserve2: str = Field("", title="保留的无效字段")
    MacAddress: str = Field("", title="Mac地址")
    InstrumentID: str = Field("", title="合约代码")
    IPAddress: str = Field("", title="IP地址")


class WebCTPReqInputForQuote(WebCTPRequest):
    InputForQuote: InputForQuoteField = Field(title="输入的询价")


class ForQuoteField(BaseModel):
    """询价"""

    BrokerID: str = Field("", title="经纪公司代码")
    InvestorID: str = Field("", title="投资者代码")
    reserve1: str = Field("", title="保留的无效字段")
    ForQuoteRef: str = Field("", title="询价引用")
    UserID: str = Field("", title="用户代码")
    ForQuoteLocalID: str = Field("", title="本地询价编号")
    ExchangeID: str = Field("", title="交易所代码")
    ParticipantID: str = Field("", title="会员代码")
    ClientID: str = Field("", title="客户代码")
    reserve2: str = Field("", title="保留的无效字段")
    TraderID: str = Field("", title="交易所交易员代码")
    InstallID: int = Field(0, title="安装编号")
    InsertDate: str = Field("", title="报单日期")
    InsertTime: str = Field("", title="插入时间")
    ForQuoteStatus: str = Field("", title="询价状态")
    FrontID: int = Field(0, title="前置编号")
    SessionID: int = Field(0, title="会话编号")
    StatusMsg: str = Field("", title="状态信息")
    ActiveUserID: str = Field("", title="操作用户代码")
    BrokerForQutoSeq: int = Field(0, title="经纪公司询价编号")
    InvestUnitID: str = Field("", title="投资单元代码")
    reserve3: str = Field("", title="保留的无效字段")
    MacAddress: str = Field("", title="Mac地址")
    InstrumentID: str = Field("", title="合约代码")
    ExchangeInstID: str = Field("", title="合约在交易所的代码")
    IPAddress: str = Field("", title="IP地址")


class WebCTPReqForQuote(WebCTPRequest):
    ForQuote: ForQuoteField = Field(title="询价")


class QryForQuoteField(BaseModel):
    """询价查询"""

    BrokerID: str = Field("", title="经纪公司代码")
    InvestorID: str = Field("", title="投资者代码")
    reserve1: str = Field("", title="保留的无效字段")
    ExchangeID: str = Field("", title="交易所代码")
    InsertTimeStart: str = Field("", title="开始时间")
    InsertTimeEnd: str = Field("", title="结束时间")
    InvestUnitID: str = Field("", title="投资单元代码")
    InstrumentID: str = Field("", title="合约代码")


class WebCTPReqQryForQuote(WebCTPRequest):
    QryForQuote: QryForQuoteField = Field(title="询价查询")


class ExchangeForQuoteField(BaseModel):
    """交易所询价信息"""

    ForQuoteLocalID: str = Field("", title="本地询价编号")
    ExchangeID: str = Field("", title="交易所代码")
    ParticipantID: str = Field("", title="会员代码")
    ClientID: str = Field("", title="客户代码")
    reserve1: str = Field("", title="保留的无效字段")
    TraderID: str = Field("", title="交易所交易员代码")
    InstallID: int = Field(0, title="安装编号")
    InsertDate: str = Field("", title="报单日期")
    InsertTime: str = Field("", title="插入时间")
    ForQuoteStatus: str = Field("", title="询价状态")
    reserve2: str = Field("", title="保留的无效字段")
    MacAddress: str = Field("", title="Mac地址")
    ExchangeInstID: str = Field("", title="合约在交易所的代码")
    IPAddress: str = Field("", title="IP地址")


class WebCTPReqExchangeForQuote(WebCTPRequest):
    ExchangeForQuote: ExchangeForQuoteField = Field(title="交易所询价信息")


class QryExchangeForQuoteField(BaseModel):
    """交易所询价查询"""

    ParticipantID: str = Field("", title="会员代码")
    ClientID: str = Field("", title="客户代码")
    reserve1: str = Field("", title="保留的无效字段")
    ExchangeID: str = Field("", title="交易所代码")
    TraderID: str = Field("", title="交易所交易员代码")
    ExchangeInstID: str = Field("", title="合约在交易所的代码")


class WebCTPReqQryExchangeForQuote(WebCTPRequest):
    QryExchangeForQuote: QryExchangeForQuoteField = Field(
        title="交易所询价查询")


class InputQuoteField(BaseModel):
    """输入的报价"""

    BrokerID: str = Field("", title="经纪公司代码")
    InvestorID: str = Field("", title="投资者代码")
    reserve1: str = Field("", title="保留的无效字段")
    QuoteRef: str = Field("", title="报价引用")
    UserID: str = Field("", title="用户代码")
    AskPrice: float = Field(0.0, title="卖价格")
    BidPrice: float = Field(0.0, title="买价格")
    AskVolume: int = Field(0, title="卖数量")
    BidVolume: int = Field(0, title="买数量")
    RequestID: int = Field(0, title="请求编号")
    BusinessUnit: str = Field("", title="业务单元")
    AskOffsetFlag: str = Field("", title="卖开平标志")
    BidOffsetFlag: str = Field("", title="买开平标志")
    AskHedgeFlag: str = Field("", title="卖投机套保标志")
    BidHedgeFlag: str = Field("", title="买投机套保标志")
    AskOrderRef: str = Field("", title="衍生卖报单引用")
    BidOrderRef: str = Field("", title="衍生买报单引用")
    ForQuoteSysID: str = Field("", title="应价编号")
    ExchangeID: str = Field("", title="交易所代码")
    InvestUnitID: str = Field("", title="投资单元代码")
    ClientID: str = Field("", title="交易编码")
    reserve2: str = Field("", title="保留的无效字段")
    MacAddress: str = Field("", title="Mac地址")
    InstrumentID: str = Field("", title="合约代码")
    IPAddress: str = Field("", title="IP地址")
    ReplaceSysID: str = Field("", title="被顶单编号")
    TimeCondition: str = Field("", title="有效期类型")


class WebCTPReqInputQuote(WebCTPRequest):
    InputQuote: InputQuoteField = Field(title="输入的报价")


class InputQuoteActionField(BaseModel):
    """输入报价操作"""

    BrokerID: str = Field("", title="经纪公司代码")
    InvestorID: str = Field("", title="投资者代码")
    QuoteActionRef: int = Field(0, title="报价操作引用")
    QuoteRef: str = Field("", title="报价引用")
    RequestID: int = Field(0, title="请求编号")
    FrontID: int = Field(0, title="前置编号")
    SessionID: int = Field(0, title="会话编号")
    ExchangeID: str = Field("", title="交易所代码")
    QuoteSysID: str = Field("", title="报价操作编号")
    ActionFlag: str = Field("", title="操作标志")
    UserID: str = Field("", title="用户代码")
    reserve1: str = Field("", title="保留的无效字段")
    InvestUnitID: str = Field("", title="投资单元代码")
    ClientID: str = Field("", title="交易编码")
    reserve2: str = Field("", title="保留的无效字段")
    MacAddress: str = Field("", title="Mac地址")
    InstrumentID: str = Field("", title="合约代码")
    IPAddress: str = Field("", title="IP地址")


class WebCTPReqInputQuoteAction(WebCTPRequest):
    InputQuoteAction: InputQuoteActionField = Field(title="输入报价操作")


class QuoteField(BaseModel):
    """报价"""

    BrokerID: str = Field("", title="经纪公司代码")
    InvestorID: str = Field("", title="投资者代码")
    reserve1: str = Field("", title="保留的无效字段")
    QuoteRef: str = Field("", title="报价引用")
    UserID: str = Field("", title="用户代码")
    AskPrice: float = Field(0.0, title="卖价格")
    BidPrice: float = Field(0.0, title="买价格")
    AskVolume: int = Field(0, title="卖数量")
    BidVolume: int = Field(0, title="买数量")
    RequestID: int = Field(0, title="请求编号")
    BusinessUnit: str = Field("", title="业务单元")
    AskOffsetFlag: str = Field("", title="卖开平标志")
    BidOffsetFlag: str = Field("", title="买开平标志")
    AskHedgeFlag: str = Field("", title="卖投机套保标志")
    BidHedgeFlag: str = Field("", title="买投机套保标志")
    QuoteLocalID: str = Field("", title="本地报价编号")
    ExchangeID: str = Field("", title="交易所代码")
    ParticipantID: str = Field("", title="会员代码")
    ClientID: str = Field("", title="客户代码")
    reserve2: str = Field("", title="保留的无效字段")
    TraderID: str = Field("", title="交易所交易员代码")
    InstallID: int = Field(0, title="安装编号")
    NotifySequence: int = Field(0, title="报价提示序号")
    OrderSubmitStatus: str = Field("", title="报价提交状态")
    TradingDay: str = Field("", title="交易日")
    SettlementID: int = Field(0, title="结算编号")
    QuoteSysID: str = Field("", title="报价编号")
    InsertDate: str = Field("", title="报单日期")
    InsertTime: str = Field("", title="插入时间")
    CancelTime: str = Field("", title="撤销时间")
    QuoteStatus: str = Field("", title="报价状态")
    ClearingPartID: str = Field("", title="结算会员编号")
    SequenceNo: int = Field(0, title="序号")
    AskOrderSysID: str = Field("", title="卖方报单编号")
    BidOrderSysID: str = Field("", title="买方报单编号")
    FrontID: int = Field(0, title="前置编号")
    SessionID: int = Field(0, title="会话编号")
    UserProductInfo: str = Field("", title="用户端产品信息")
    StatusMsg: str = Field("", title="状态信息")
    ActiveUserID: str = Field("", title="操作用户代码")
    BrokerQuoteSeq: int = Field(0, title="经纪公司报价编号")
    AskOrderRef: str = Field("", title="衍生卖报单引用")
    BidOrderRef: str = Field("", title="衍生买报单引用")
    ForQuoteSysID: str = Field("", title="应价编号")
    BranchID: str = Field("", title="营业部编号")
    InvestUnitID: str = Field("", title="投资单元代码")
    AccountID: str = Field("", title="资金账号")
    CurrencyID: str = Field("", title="币种代码")
    reserve3: str = Field("", title="保留的无效字段")
    MacAddress: str = Field("", title="Mac地址")
    InstrumentID: str = Field("", title="合约代码")
    ExchangeInstID: str = Field("", title="合约在交易所的代码")
    IPAddress: str = Field("", title="IP地址")
    ReplaceSysID: str = Field("", title="被顶单编号")
    TimeCondition: str = Field("", title="有效期类型")


class WebCTPReqQuote(WebCTPRequest):
    Quote: QuoteField = Field(title="报价")


class QuoteActionField(BaseModel):
    """报价操作"""

    BrokerID: str = Field("", title="经纪公司代码")
    InvestorID: str = Field("", title="投资者代码")
    QuoteActionRef: int = Field(0, title="报价操作引用")
    QuoteRef: str = Field("", title="报价引用")
    RequestID: int = Field(0, title="请求编号")
    FrontID: int = Field(0, title="前置编号")
    SessionID: int = Field(0, title="会话编号")
    ExchangeID: str = Field("", title="交易所代码")
    QuoteSysID: str = Field("", title="报价操作编号")
    ActionFlag: str = Field("", title="操作标志")
    ActionDate: str = Field("", title="操作日期")
    ActionTime: str = Field("", title="操作时间")
    TraderID: str = Field("", title="交易所交易员代码")
    InstallID: int = Field(0, title="安装编号")
    QuoteLocalID: str = Field("", title="本地报价编号")
    ActionLocalID: str = Field("", title="操作本地编号")
    ParticipantID: str = Field("", title="会员代码")
    ClientID: str = Field("", title="客户代码")
    BusinessUnit: str = Field("", title="业务单元")
    OrderActionStatus: str = Field("", title="报单操作状态")
    UserID: str = Field("", title="用户代码")
    StatusMsg: str = Field("", title="状态信息")
    reserve1: str = Field("", title="保留的无效字段")
    BranchID: str = Field("", title="营业部编号")
    InvestUnitID: str = Field("", title="投资单元代码")
    reserve2: str = Field("", title="保留的无效字段")
    MacAddress: str = Field("", title="Mac地址")
    InstrumentID: str = Field("", title="合约代码")
    IPAddress: str = Field("", title="IP地址")


class WebCTPReqQuoteAction(WebCTPRequest):
    QuoteAction: QuoteActionField = Field(title="报价操作")


class QryQuoteField(BaseModel):
    """报价查询"""

    BrokerID: str = Field("", title="经纪公司代码")
    InvestorID: str = Field("", title="投资者代码")
    reserve1: str = Field("", title="保留的无效字段")
    ExchangeID: str = Field("", title="交易所代码")
    QuoteSysID: str = Field("", title="报价编号")
    InsertTimeStart: str = Field("", title="开始时间")
    InsertTimeEnd: str = Field("", title="结束时间")
    InvestUnitID: str = Field("", title="投资单元代码")
    InstrumentID: str = Field("", title="合约代码")


class WebCTPReqQryQuote(WebCTPRequest):
    QryQuote: QryQuoteField = Field(title="报价查询")


class ExchangeQuoteField(BaseModel):
    """交易所报价信息"""

    AskPrice: float = Field(0.0, title="卖价格")
    BidPrice: float = Field(0.0, title="买价格")
    AskVolume: int = Field(0, title="卖数量")
    BidVolume: int = Field(0, title="买数量")
    RequestID: int = Field(0, title="请求编号")
    BusinessUnit: str = Field("", title="业务单元")
    AskOffsetFlag: str = Field("", title="卖开平标志")
    BidOffsetFlag: str = Field("", title="买开平标志")
    AskHedgeFlag: str = Field("", title="卖投机套保标志")
    BidHedgeFlag: str = Field("", title="买投机套保标志")
    QuoteLocalID: str = Field("", title="本地报价编号")
    ExchangeID: str = Field("", title="交易所代码")
    ParticipantID: str = Field("", title="会员代码")
    ClientID: str = Field("", title="客户代码")
    reserve1: str = Field("", title="保留的无效字段")
    TraderID: str = Field("", title="交易所交易员代码")
    InstallID: int = Field(0, title="安装编号")
    NotifySequence: int = Field(0, title="报价提示序号")
    OrderSubmitStatus: str = Field("", title="报价提交状态")
    TradingDay: str = Field("", title="交易日")
    SettlementID: int = Field(0, title="结算编号")
    QuoteSysID: str = Field("", title="报价编号")
    InsertDate: str = Field("", title="报单日期")
    InsertTime: str = Field("", title="插入时间")
    CancelTime: str = Field("", title="撤销时间")
    QuoteStatus: str = Field("", title="报价状态")
    ClearingPartID: str = Field("", title="结算会员编号")
    SequenceNo: int = Field(0, title="序号")
    AskOrderSysID: str = Field("", title="卖方报单编号")
    BidOrderSysID: str = Field("", title="买方报单编号")
    ForQuoteSysID: str = Field("", title="应价编号")
    BranchID: str = Field("", title="营业部编号")
    reserve2: str = Field("", title="保留的无效字段")
    MacAddress: str = Field("", title="Mac地址")
    ExchangeInstID: str = Field("", title="合约在交易所的代码")
    IPAddress: str = Field("", title="IP地址")
    TimeCondition: str = Field("", title="有效期类型")


class WebCTPReqExchangeQuote(WebCTPRequest):
    ExchangeQuote: ExchangeQuoteField = Field(title="交易所报价信息")


class QryExchangeQuoteField(BaseModel):
    """交易所报价查询"""

    ParticipantID: str = Field("", title="会员代码")
    ClientID: str = Field("", title="客户代码")
    reserve1: str = Field("", title="保留的无效字段")
    ExchangeID: str = Field("", title="交易所代码")
    TraderID: str = Field("", title="交易所交易员代码")
    ExchangeInstID: str = Field("", title="合约在交易所的代码")


class WebCTPReqQryExchangeQuote(WebCTPRequest):
    QryExchangeQuote: QryExchangeQuoteField = Field(title="交易所报价查询")


class QryQuoteActionField(BaseModel):
    """报价操作查询"""

    BrokerID: str = Field("", title="经纪公司代码")
    InvestorID: str = Field("", title="投资者代码")
    ExchangeID: str = Field("", title="交易所代码")


class WebCTPReqQryQuoteAction(WebCTPRequest):
    QryQuoteAction: QryQuoteActionField = Field(title="报价操作查询")


class ExchangeQuoteActionField(BaseModel):
    """交易所报价操作"""

    ExchangeID: str = Field("", title="交易所代码")
    QuoteSysID: str = Field("", title="报价操作编号")
    ActionFlag: str = Field("", title="操作标志")
    ActionDate: str = Field("", title="操作日期")
    ActionTime: str = Field("", title="操作时间")
    TraderID: str = Field("", title="交易所交易员代码")
    InstallID: int = Field(0, title="安装编号")
    QuoteLocalID: str = Field("", title="本地报价编号")
    ActionLocalID: str = Field("", title="操作本地编号")
    ParticipantID: str = Field("", title="会员代码")
    ClientID: str = Field("", title="客户代码")
    BusinessUnit: str = Field("", title="业务单元")
    OrderActionStatus: str = Field("", title="报单操作状态")
    UserID: str = Field("", title="用户代码")
    reserve1: str = Field("", title="保留的无效字段")
    MacAddress: str = Field("", title="Mac地址")
    IPAddress: str = Field("", title="IP地址")


class WebCTPReqExchangeQuoteAction(WebCTPRequest):
    ExchangeQuoteAction: ExchangeQuoteActionField = Field(
        title="交易所报价操作")


class QryExchangeQuoteActionField(BaseModel):
    """交易所报价操作查询"""

    ParticipantID: str = Field("", title="会员代码")
    ClientID: str = Field("", title="客户代码")
    ExchangeID: str = Field("", title="交易所代码")
    TraderID: str = Field("", title="交易所交易员代码")


class WebCTPReqQryExchangeQuoteAction(WebCTPRequest):
    QryExchangeQuoteAction: QryExchangeQuoteActionField = Field(
        title="交易所报价操作查询")


class OptionInstrDeltaField(BaseModel):
    """期权合约delta值"""

    reserve1: str = Field("", title="保留的无效字段")
    InvestorRange: str = Field("", title="投资者范围")
    BrokerID: str = Field("", title="经纪公司代码")
    InvestorID: str = Field("", title="投资者代码")
    Delta: float = Field(0.0, title="Delta值")
    InstrumentID: str = Field("", title="合约代码")


class WebCTPReqOptionInstrDelta(WebCTPRequest):
    OptionInstrDelta: OptionInstrDeltaField = Field(title="期权合约delta值")


class ForQuoteRspField(BaseModel):
    """发给做市商的询价请求"""

    TradingDay: str = Field("", title="交易日")
    reserve1: str = Field("", title="保留的无效字段")
    ForQuoteSysID: str = Field("", title="询价编号")
    ForQuoteTime: str = Field("", title="询价时间")
    ActionDay: str = Field("", title="业务日期")
    ExchangeID: str = Field("", title="交易所代码")
    InstrumentID: str = Field("", title="合约代码")


class WebCTPReqForQuoteRsp(WebCTPRequest):
    ForQuoteRsp: ForQuoteRspField = Field(title="发给做市商的询价请求")


class StrikeOffsetField(BaseModel):
    """当前期权合约执行偏移值的详细内容"""

    reserve1: str = Field("", title="保留的无效字段")
    InvestorRange: str = Field("", title="投资者范围")
    BrokerID: str = Field("", title="经纪公司代码")
    InvestorID: str = Field("", title="投资者代码")
    Offset: float = Field(0.0, title="执行偏移值")
    OffsetType: str = Field("", title="执行偏移类型")
    InstrumentID: str = Field("", title="合约代码")


class WebCTPReqStrikeOffset(WebCTPRequest):
    StrikeOffset: StrikeOffsetField = Field(
        title="当前期权合约执行偏移值的详细内容")


class QryStrikeOffsetField(BaseModel):
    """期权执行偏移值查询"""

    BrokerID: str = Field("", title="经纪公司代码")
    InvestorID: str = Field("", title="投资者代码")
    reserve1: str = Field("", title="保留的无效字段")
    InstrumentID: str = Field("", title="合约代码")


class WebCTPReqQryStrikeOffset(WebCTPRequest):
    QryStrikeOffset: QryStrikeOffsetField = Field(title="期权执行偏移值查询")


class InputBatchOrderActionField(BaseModel):
    """输入批量报单操作"""

    BrokerID: str = Field("", title="经纪公司代码")
    InvestorID: str = Field("", title="投资者代码")
    OrderActionRef: int = Field(0, title="报单操作引用")
    RequestID: int = Field(0, title="请求编号")
    FrontID: int = Field(0, title="前置编号")
    SessionID: int = Field(0, title="会话编号")
    ExchangeID: str = Field("", title="交易所代码")
    UserID: str = Field("", title="用户代码")
    InvestUnitID: str = Field("", title="投资单元代码")
    reserve1: str = Field("", title="保留的无效字段")
    MacAddress: str = Field("", title="Mac地址")
    IPAddress: str = Field("", title="IP地址")


class WebCTPReqInputBatchOrderAction(WebCTPRequest):
    InputBatchOrderAction: InputBatchOrderActionField = Field(
        title="输入批量报单操作")


class BatchOrderActionField(BaseModel):
    """批量报单操作"""

    BrokerID: str = Field("", title="经纪公司代码")
    InvestorID: str = Field("", title="投资者代码")
    OrderActionRef: int = Field(0, title="报单操作引用")
    RequestID: int = Field(0, title="请求编号")
    FrontID: int = Field(0, title="前置编号")
    SessionID: int = Field(0, title="会话编号")
    ExchangeID: str = Field("", title="交易所代码")
    ActionDate: str = Field("", title="操作日期")
    ActionTime: str = Field("", title="操作时间")
    TraderID: str = Field("", title="交易所交易员代码")
    InstallID: int = Field(0, title="安装编号")
    ActionLocalID: str = Field("", title="操作本地编号")
    ParticipantID: str = Field("", title="会员代码")
    ClientID: str = Field("", title="客户代码")
    BusinessUnit: str = Field("", title="业务单元")
    OrderActionStatus: str = Field("", title="报单操作状态")
    UserID: str = Field("", title="用户代码")
    StatusMsg: str = Field("", title="状态信息")
    InvestUnitID: str = Field("", title="投资单元代码")
    reserve1: str = Field("", title="保留的无效字段")
    MacAddress: str = Field("", title="Mac地址")
    IPAddress: str = Field("", title="IP地址")


class WebCTPReqBatchOrderAction(WebCTPRequest):
    BatchOrderAction: BatchOrderActionField = Field(title="批量报单操作")


class ExchangeBatchOrderActionField(BaseModel):
    """交易所批量报单操作"""

    ExchangeID: str = Field("", title="交易所代码")
    ActionDate: str = Field("", title="操作日期")
    ActionTime: str = Field("", title="操作时间")
    TraderID: str = Field("", title="交易所交易员代码")
    InstallID: int = Field(0, title="安装编号")
    ActionLocalID: str = Field("", title="操作本地编号")
    ParticipantID: str = Field("", title="会员代码")
    ClientID: str = Field("", title="客户代码")
    BusinessUnit: str = Field("", title="业务单元")
    OrderActionStatus: str = Field("", title="报单操作状态")
    UserID: str = Field("", title="用户代码")
    reserve1: str = Field("", title="保留的无效字段")
    MacAddress: str = Field("", title="Mac地址")
    IPAddress: str = Field("", title="IP地址")


class WebCTPReqExchangeBatchOrderAction(WebCTPRequest):
    ExchangeBatchOrderAction: ExchangeBatchOrderActionField = Field(
        title="交易所批量报单操作")


class QryBatchOrderActionField(BaseModel):
    """查询批量报单操作"""

    BrokerID: str = Field("", title="经纪公司代码")
    InvestorID: str = Field("", title="投资者代码")
    ExchangeID: str = Field("", title="交易所代码")


class WebCTPReqQryBatchOrderAction(WebCTPRequest):
    QryBatchOrderAction: QryBatchOrderActionField = Field(
        title="查询批量报单操作")


class CombInstrumentGuardField(BaseModel):
    """组合合约安全系数"""

    BrokerID: str = Field("", title="经纪公司代码")
    reserve1: str = Field("", title="保留的无效字段")
    GuarantRatio: float = Field(0.0, title="")
    ExchangeID: str = Field("", title="交易所代码")
    InstrumentID: str = Field("", title="合约代码")


class WebCTPReqCombInstrumentGuard(WebCTPRequest):
    CombInstrumentGuard: CombInstrumentGuardField = Field(
        title="组合合约安全系数")


class QryCombInstrumentGuardField(BaseModel):
    """组合合约安全系数查询"""

    BrokerID: str = Field("", title="经纪公司代码")
    reserve1: str = Field("", title="保留的无效字段")
    ExchangeID: str = Field("", title="交易所代码")
    InstrumentID: str = Field("", title="合约代码")


class WebCTPReqQryCombInstrumentGuard(WebCTPRequest):
    QryCombInstrumentGuard: QryCombInstrumentGuardField = Field(
        title="组合合约安全系数查询")


class InputCombActionField(BaseModel):
    """输入的申请组合"""

    BrokerID: str = Field("", title="经纪公司代码")
    InvestorID: str = Field("", title="投资者代码")
    reserve1: str = Field("", title="保留的无效字段")
    CombActionRef: str = Field("", title="组合引用")
    UserID: str = Field("", title="用户代码")
    Direction: str = Field("", title="买卖方向")
    Volume: int = Field(0, title="数量")
    CombDirection: str = Field("", title="组合指令方向")
    HedgeFlag: str = Field("", title="投机套保标志")
    ExchangeID: str = Field("", title="交易所代码")
    reserve2: str = Field("", title="保留的无效字段")
    MacAddress: str = Field("", title="Mac地址")
    InvestUnitID: str = Field("", title="投资单元代码")
    FrontID: int = Field(0, title="前置编号")
    SessionID: int = Field(0, title="会话编号")
    InstrumentID: str = Field("", title="合约代码")
    IPAddress: str = Field("", title="IP地址")


class WebCTPReqInputCombAction(WebCTPRequest):
    InputCombAction: InputCombActionField = Field(title="输入的申请组合")


class CombActionField(BaseModel):
    """申请组合"""

    BrokerID: str = Field("", title="经纪公司代码")
    InvestorID: str = Field("", title="投资者代码")
    reserve1: str = Field("", title="保留的无效字段")
    CombActionRef: str = Field("", title="组合引用")
    UserID: str = Field("", title="用户代码")
    Direction: str = Field("", title="买卖方向")
    Volume: int = Field(0, title="数量")
    CombDirection: str = Field("", title="组合指令方向")
    HedgeFlag: str = Field("", title="投机套保标志")
    ActionLocalID: str = Field("", title="本地申请组合编号")
    ExchangeID: str = Field("", title="交易所代码")
    ParticipantID: str = Field("", title="会员代码")
    ClientID: str = Field("", title="客户代码")
    reserve2: str = Field("", title="保留的无效字段")
    TraderID: str = Field("", title="交易所交易员代码")
    InstallID: int = Field(0, title="安装编号")
    ActionStatus: str = Field("", title="组合状态")
    NotifySequence: int = Field(0, title="报单提示序号")
    TradingDay: str = Field("", title="交易日")
    SettlementID: int = Field(0, title="结算编号")
    SequenceNo: int = Field(0, title="序号")
    FrontID: int = Field(0, title="前置编号")
    SessionID: int = Field(0, title="会话编号")
    UserProductInfo: str = Field("", title="用户端产品信息")
    StatusMsg: str = Field("", title="状态信息")
    reserve3: str = Field("", title="保留的无效字段")
    MacAddress: str = Field("", title="Mac地址")
    ComTradeID: str = Field("", title="组合编号")
    BranchID: str = Field("", title="营业部编号")
    InvestUnitID: str = Field("", title="投资单元代码")
    InstrumentID: str = Field("", title="合约代码")
    ExchangeInstID: str = Field("", title="合约在交易所的代码")
    IPAddress: str = Field("", title="IP地址")


class WebCTPReqCombAction(WebCTPRequest):
    CombAction: CombActionField = Field(title="申请组合")


class QryCombActionField(BaseModel):
    """申请组合查询"""

    BrokerID: str = Field("", title="经纪公司代码")
    InvestorID: str = Field("", title="投资者代码")
    reserve1: str = Field("", title="保留的无效字段")
    ExchangeID: str = Field("", title="交易所代码")
    InvestUnitID: str = Field("", title="投资单元代码")
    InstrumentID: str = Field("", title="合约代码")


class WebCTPReqQryCombAction(WebCTPRequest):
    QryCombAction: QryCombActionField = Field(title="申请组合查询")


class ExchangeCombActionField(BaseModel):
    """交易所申请组合信息"""

    Direction: str = Field("", title="买卖方向")
    Volume: int = Field(0, title="数量")
    CombDirection: str = Field("", title="组合指令方向")
    HedgeFlag: str = Field("", title="投机套保标志")
    ActionLocalID: str = Field("", title="本地申请组合编号")
    ExchangeID: str = Field("", title="交易所代码")
    ParticipantID: str = Field("", title="会员代码")
    ClientID: str = Field("", title="客户代码")
    reserve1: str = Field("", title="保留的无效字段")
    TraderID: str = Field("", title="交易所交易员代码")
    InstallID: int = Field(0, title="安装编号")
    ActionStatus: str = Field("", title="组合状态")
    NotifySequence: int = Field(0, title="报单提示序号")
    TradingDay: str = Field("", title="交易日")
    SettlementID: int = Field(0, title="结算编号")
    SequenceNo: int = Field(0, title="序号")
    reserve2: str = Field("", title="保留的无效字段")
    MacAddress: str = Field("", title="Mac地址")
    ComTradeID: str = Field("", title="组合编号")
    BranchID: str = Field("", title="营业部编号")
    ExchangeInstID: str = Field("", title="合约在交易所的代码")
    IPAddress: str = Field("", title="IP地址")


class WebCTPReqExchangeCombAction(WebCTPRequest):
    ExchangeCombAction: ExchangeCombActionField = Field(
        title="交易所申请组合信息")


class QryExchangeCombActionField(BaseModel):
    """交易所申请组合查询"""

    ParticipantID: str = Field("", title="会员代码")
    ClientID: str = Field("", title="客户代码")
    reserve1: str = Field("", title="保留的无效字段")
    ExchangeID: str = Field("", title="交易所代码")
    TraderID: str = Field("", title="交易所交易员代码")
    ExchangeInstID: str = Field("", title="合约在交易所的代码")


class WebCTPReqQryExchangeCombAction(WebCTPRequest):
    QryExchangeCombAction: QryExchangeCombActionField = Field(
        title="交易所申请组合查询")


class ProductExchRateField(BaseModel):
    """产品报价汇率"""

    reserve1: str = Field("", title="保留的无效字段")
    QuoteCurrencyID: str = Field("", title="报价币种类型")
    ExchangeRate: float = Field(0.0, title="汇率")
    ExchangeID: str = Field("", title="交易所代码")
    ProductID: str = Field("", title="产品代码")


class WebCTPReqProductExchRate(WebCTPRequest):
    ProductExchRate: ProductExchRateField = Field(title="产品报价汇率")


class QryProductExchRateField(BaseModel):
    """产品报价汇率查询"""

    reserve1: str = Field("", title="保留的无效字段")
    ExchangeID: str = Field("", title="交易所代码")
    ProductID: str = Field("", title="产品代码")


class WebCTPReqQryProductExchRate(WebCTPRequest):
    QryProductExchRate: QryProductExchRateField = Field(
        title="产品报价汇率查询")


class QryForQuoteParamField(BaseModel):
    """查询询价价差参数"""

    BrokerID: str = Field("", title="经纪公司代码")
    reserve1: str = Field("", title="保留的无效字段")
    ExchangeID: str = Field("", title="交易所代码")
    InstrumentID: str = Field("", title="合约代码")


class WebCTPReqQryForQuoteParam(WebCTPRequest):
    QryForQuoteParam: QryForQuoteParamField = Field(title="查询询价价差参数")


class ForQuoteParamField(BaseModel):
    """询价价差参数"""

    BrokerID: str = Field("", title="经纪公司代码")
    reserve1: str = Field("", title="保留的无效字段")
    ExchangeID: str = Field("", title="交易所代码")
    LastPrice: float = Field(0.0, title="最新价")
    PriceInterval: float = Field(0.0, title="价差")
    InstrumentID: str = Field("", title="合约代码")


class WebCTPReqForQuoteParam(WebCTPRequest):
    ForQuoteParam: ForQuoteParamField = Field(title="询价价差参数")


class MMOptionInstrCommRateField(BaseModel):
    """当前做市商期权合约手续费的详细内容"""

    reserve1: str = Field("", title="保留的无效字段")
    InvestorRange: str = Field("", title="投资者范围")
    BrokerID: str = Field("", title="经纪公司代码")
    InvestorID: str = Field("", title="投资者代码")
    OpenRatioByMoney: float = Field(0.0, title="开仓手续费率")
    OpenRatioByVolume: float = Field(0.0, title="开仓手续费")
    CloseRatioByMoney: float = Field(0.0, title="平仓手续费率")
    CloseRatioByVolume: float = Field(0.0, title="平仓手续费")
    CloseTodayRatioByMoney: float = Field(0.0, title="平今手续费率")
    CloseTodayRatioByVolume: float = Field(0.0, title="平今手续费")
    StrikeRatioByMoney: float = Field(0.0, title="执行手续费率")
    StrikeRatioByVolume: float = Field(0.0, title="执行手续费")
    InstrumentID: str = Field("", title="合约代码")


class WebCTPReqMMOptionInstrCommRate(WebCTPRequest):
    MMOptionInstrCommRate: MMOptionInstrCommRateField = Field(
        title="当前做市商期权合约手续费的详细内容")


class QryMMOptionInstrCommRateField(BaseModel):
    """做市商期权手续费率查询"""

    BrokerID: str = Field("", title="经纪公司代码")
    InvestorID: str = Field("", title="投资者代码")
    reserve1: str = Field("", title="保留的无效字段")
    InstrumentID: str = Field("", title="合约代码")


class WebCTPReqQryMMOptionInstrCommRate(WebCTPRequest):
    QryMMOptionInstrCommRate: QryMMOptionInstrCommRateField = Field(
        title="做市商期权手续费率查询")


class MMInstrumentCommissionRateField(BaseModel):
    """做市商合约手续费率"""

    reserve1: str = Field("", title="保留的无效字段")
    InvestorRange: str = Field("", title="投资者范围")
    BrokerID: str = Field("", title="经纪公司代码")
    InvestorID: str = Field("", title="投资者代码")
    OpenRatioByMoney: float = Field(0.0, title="开仓手续费率")
    OpenRatioByVolume: float = Field(0.0, title="开仓手续费")
    CloseRatioByMoney: float = Field(0.0, title="平仓手续费率")
    CloseRatioByVolume: float = Field(0.0, title="平仓手续费")
    CloseTodayRatioByMoney: float = Field(0.0, title="平今手续费率")
    CloseTodayRatioByVolume: float = Field(0.0, title="平今手续费")
    InstrumentID: str = Field("", title="合约代码")


class WebCTPReqMMInstrumentCommissionRate(WebCTPRequest):
    MMInstrumentCommissionRate: MMInstrumentCommissionRateField = Field(
        title="做市商合约手续费率")


class QryMMInstrumentCommissionRateField(BaseModel):
    """查询做市商合约手续费率"""

    BrokerID: str = Field("", title="经纪公司代码")
    InvestorID: str = Field("", title="投资者代码")
    reserve1: str = Field("", title="保留的无效字段")
    InstrumentID: str = Field("", title="合约代码")


class WebCTPReqQryMMInstrumentCommissionRate(WebCTPRequest):
    QryMMInstrumentCommissionRate: QryMMInstrumentCommissionRateField = Field(
        title="查询做市商合约手续费率")


class InstrumentOrderCommRateField(BaseModel):
    """当前报单手续费的详细内容"""

    reserve1: str = Field("", title="保留的无效字段")
    InvestorRange: str = Field("", title="投资者范围")
    BrokerID: str = Field("", title="经纪公司代码")
    InvestorID: str = Field("", title="投资者代码")
    HedgeFlag: str = Field("", title="投机套保标志")
    OrderCommByVolume: float = Field(0.0, title="报单手续费")
    OrderActionCommByVolume: float = Field(0.0, title="撤单手续费")
    ExchangeID: str = Field("", title="交易所代码")
    InvestUnitID: str = Field("", title="投资单元代码")
    InstrumentID: str = Field("", title="合约代码")
    OrderCommByTrade: float = Field(0.0, title="报单手续费")
    OrderActionCommByTrade: float = Field(0.0, title="撤单手续费")


class WebCTPReqInstrumentOrderCommRate(WebCTPRequest):
    InstrumentOrderCommRate: InstrumentOrderCommRateField = Field(
        title="当前报单手续费的详细内容")


class QryInstrumentOrderCommRateField(BaseModel):
    """报单手续费率查询"""

    BrokerID: str = Field("", title="经纪公司代码")
    InvestorID: str = Field("", title="投资者代码")
    reserve1: str = Field("", title="保留的无效字段")
    InstrumentID: str = Field("", title="合约代码")


class WebCTPReqQryInstrumentOrderCommRate(WebCTPRequest):
    QryInstrumentOrderCommRate: QryInstrumentOrderCommRateField = Field(
        title="报单手续费率查询")


class TradeParamField(BaseModel):
    """交易参数"""

    BrokerID: str = Field("", title="经纪公司代码")
    TradeParamID: str = Field("", title="参数代码")
    TradeParamValue: str = Field("", title="参数代码值")
    Memo: str = Field("", title="备注")


class WebCTPReqTradeParam(WebCTPRequest):
    TradeParam: TradeParamField = Field(title="交易参数")


class InstrumentMarginRateULField(BaseModel):
    """合约保证金率调整"""

    reserve1: str = Field("", title="保留的无效字段")
    InvestorRange: str = Field("", title="投资者范围")
    BrokerID: str = Field("", title="经纪公司代码")
    InvestorID: str = Field("", title="投资者代码")
    HedgeFlag: str = Field("", title="投机套保标志")
    LongMarginRatioByMoney: float = Field(0.0, title="多头保证金率")
    LongMarginRatioByVolume: float = Field(0.0, title="多头保证金费")
    ShortMarginRatioByMoney: float = Field(0.0, title="空头保证金率")
    ShortMarginRatioByVolume: float = Field(0.0, title="空头保证金费")
    InstrumentID: str = Field("", title="合约代码")


class WebCTPReqInstrumentMarginRateUL(WebCTPRequest):
    InstrumentMarginRateUL: InstrumentMarginRateULField = Field(
        title="合约保证金率调整")


class FutureLimitPosiParamField(BaseModel):
    """期货持仓限制参数"""

    InvestorRange: str = Field("", title="投资者范围")
    BrokerID: str = Field("", title="经纪公司代码")
    InvestorID: str = Field("", title="投资者代码")
    reserve1: str = Field("", title="保留的无效字段")
    SpecOpenVolume: int = Field(0, title="当日投机开仓数量限制")
    ArbiOpenVolume: int = Field(0, title="当日套利开仓数量限制")
    OpenVolume: int = Field(0, title="当日投机+套利开仓数量限制")
    ProductID: str = Field("", title="产品代码")


class WebCTPReqFutureLimitPosiParam(WebCTPRequest):
    FutureLimitPosiParam: FutureLimitPosiParamField = Field(
        title="期货持仓限制参数")


class LoginForbiddenIPField(BaseModel):
    """禁止登录IP"""

    reserve1: str = Field("", title="保留的无效字段")
    IPAddress: str = Field("", title="IP地址")


class WebCTPReqLoginForbiddenIP(WebCTPRequest):
    LoginForbiddenIP: LoginForbiddenIPField = Field(title="禁止登录IP")


class IPListField(BaseModel):
    """IP列表"""

    reserve1: str = Field("", title="保留的无效字段")
    IsWhite: int = Field(0, title="是否白名单")
    IPAddress: str = Field("", title="IP地址")


class WebCTPReqIPList(WebCTPRequest):
    IPList: IPListField = Field(title="IP列表")


class InputOptionSelfCloseField(BaseModel):
    """输入的期权自对冲"""

    BrokerID: str = Field("", title="经纪公司代码")
    InvestorID: str = Field("", title="投资者代码")
    reserve1: str = Field("", title="保留的无效字段")
    OptionSelfCloseRef: str = Field("", title="期权自对冲引用")
    UserID: str = Field("", title="用户代码")
    Volume: int = Field(0, title="数量")
    RequestID: int = Field(0, title="请求编号")
    BusinessUnit: str = Field("", title="业务单元")
    HedgeFlag: str = Field("", title="投机套保标志")
    OptSelfCloseFlag: str = Field("", title="期权行权的头寸是否自对冲")
    ExchangeID: str = Field("", title="交易所代码")
    InvestUnitID: str = Field("", title="投资单元代码")
    AccountID: str = Field("", title="资金账号")
    CurrencyID: str = Field("", title="币种代码")
    ClientID: str = Field("", title="交易编码")
    reserve2: str = Field("", title="保留的无效字段")
    MacAddress: str = Field("", title="Mac地址")
    InstrumentID: str = Field("", title="合约代码")
    IPAddress: str = Field("", title="IP地址")


class WebCTPReqInputOptionSelfClose(WebCTPRequest):
    InputOptionSelfClose: InputOptionSelfCloseField = Field(
        title="输入的期权自对冲")


class InputOptionSelfCloseActionField(BaseModel):
    """输入期权自对冲操作"""

    BrokerID: str = Field("", title="经纪公司代码")
    InvestorID: str = Field("", title="投资者代码")
    OptionSelfCloseActionRef: int = Field(0, title="期权自对冲操作引用")
    OptionSelfCloseRef: str = Field("", title="期权自对冲引用")
    RequestID: int = Field(0, title="请求编号")
    FrontID: int = Field(0, title="前置编号")
    SessionID: int = Field(0, title="会话编号")
    ExchangeID: str = Field("", title="交易所代码")
    OptionSelfCloseSysID: str = Field("", title="期权自对冲操作编号")
    ActionFlag: str = Field("", title="操作标志")
    UserID: str = Field("", title="用户代码")
    reserve1: str = Field("", title="保留的无效字段")
    InvestUnitID: str = Field("", title="投资单元代码")
    reserve2: str = Field("", title="保留的无效字段")
    MacAddress: str = Field("", title="Mac地址")
    InstrumentID: str = Field("", title="合约代码")
    IPAddress: str = Field("", title="IP地址")


class WebCTPReqInputOptionSelfCloseAction(WebCTPRequest):
    InputOptionSelfCloseAction: InputOptionSelfCloseActionField = Field(
        title="输入期权自对冲操作")


class OptionSelfCloseField(BaseModel):
    """期权自对冲"""

    BrokerID: str = Field("", title="经纪公司代码")
    InvestorID: str = Field("", title="投资者代码")
    reserve1: str = Field("", title="保留的无效字段")
    OptionSelfCloseRef: str = Field("", title="期权自对冲引用")
    UserID: str = Field("", title="用户代码")
    Volume: int = Field(0, title="数量")
    RequestID: int = Field(0, title="请求编号")
    BusinessUnit: str = Field("", title="业务单元")
    HedgeFlag: str = Field("", title="投机套保标志")
    OptSelfCloseFlag: str = Field("", title="期权行权的头寸是否自对冲")
    OptionSelfCloseLocalID: str = Field("", title="本地期权自对冲编号")
    ExchangeID: str = Field("", title="交易所代码")
    ParticipantID: str = Field("", title="会员代码")
    ClientID: str = Field("", title="客户代码")
    reserve2: str = Field("", title="保留的无效字段")
    TraderID: str = Field("", title="交易所交易员代码")
    InstallID: int = Field(0, title="安装编号")
    OrderSubmitStatus: str = Field("", title="期权自对冲提交状态")
    NotifySequence: int = Field(0, title="报单提示序号")
    TradingDay: str = Field("", title="交易日")
    SettlementID: int = Field(0, title="结算编号")
    OptionSelfCloseSysID: str = Field("", title="期权自对冲编号")
    InsertDate: str = Field("", title="报单日期")
    InsertTime: str = Field("", title="插入时间")
    CancelTime: str = Field("", title="撤销时间")
    ExecResult: str = Field("", title="自对冲结果")
    ClearingPartID: str = Field("", title="结算会员编号")
    SequenceNo: int = Field(0, title="序号")
    FrontID: int = Field(0, title="前置编号")
    SessionID: int = Field(0, title="会话编号")
    UserProductInfo: str = Field("", title="用户端产品信息")
    StatusMsg: str = Field("", title="状态信息")
    ActiveUserID: str = Field("", title="操作用户代码")
    BrokerOptionSelfCloseSeq: int = Field(0, title="经纪公司报单编号")
    BranchID: str = Field("", title="营业部编号")
    InvestUnitID: str = Field("", title="投资单元代码")
    AccountID: str = Field("", title="资金账号")
    CurrencyID: str = Field("", title="币种代码")
    reserve3: str = Field("", title="保留的无效字段")
    MacAddress: str = Field("", title="Mac地址")
    InstrumentID: str = Field("", title="合约代码")
    ExchangeInstID: str = Field("", title="合约在交易所的代码")
    IPAddress: str = Field("", title="IP地址")


class WebCTPReqOptionSelfClose(WebCTPRequest):
    OptionSelfClose: OptionSelfCloseField = Field(title="期权自对冲")


class OptionSelfCloseActionField(BaseModel):
    """期权自对冲操作"""

    BrokerID: str = Field("", title="经纪公司代码")
    InvestorID: str = Field("", title="投资者代码")
    OptionSelfCloseActionRef: int = Field(0, title="期权自对冲操作引用")
    OptionSelfCloseRef: str = Field("", title="期权自对冲引用")
    RequestID: int = Field(0, title="请求编号")
    FrontID: int = Field(0, title="前置编号")
    SessionID: int = Field(0, title="会话编号")
    ExchangeID: str = Field("", title="交易所代码")
    OptionSelfCloseSysID: str = Field("", title="期权自对冲操作编号")
    ActionFlag: str = Field("", title="操作标志")
    ActionDate: str = Field("", title="操作日期")
    ActionTime: str = Field("", title="操作时间")
    TraderID: str = Field("", title="交易所交易员代码")
    InstallID: int = Field(0, title="安装编号")
    OptionSelfCloseLocalID: str = Field("", title="本地期权自对冲编号")
    ActionLocalID: str = Field("", title="操作本地编号")
    ParticipantID: str = Field("", title="会员代码")
    ClientID: str = Field("", title="客户代码")
    BusinessUnit: str = Field("", title="业务单元")
    OrderActionStatus: str = Field("", title="报单操作状态")
    UserID: str = Field("", title="用户代码")
    StatusMsg: str = Field("", title="状态信息")
    reserve1: str = Field("", title="保留的无效字段")
    BranchID: str = Field("", title="营业部编号")
    InvestUnitID: str = Field("", title="投资单元代码")
    reserve2: str = Field("", title="保留的无效字段")
    MacAddress: str = Field("", title="Mac地址")
    InstrumentID: str = Field("", title="合约代码")
    IPAddress: str = Field("", title="IP地址")


class WebCTPReqOptionSelfCloseAction(WebCTPRequest):
    OptionSelfCloseAction: OptionSelfCloseActionField = Field(
        title="期权自对冲操作")


class QryOptionSelfCloseField(BaseModel):
    """期权自对冲查询"""

    BrokerID: str = Field("", title="经纪公司代码")
    InvestorID: str = Field("", title="投资者代码")
    reserve1: str = Field("", title="保留的无效字段")
    ExchangeID: str = Field("", title="交易所代码")
    OptionSelfCloseSysID: str = Field("", title="期权自对冲编号")
    InsertTimeStart: str = Field("", title="开始时间")
    InsertTimeEnd: str = Field("", title="结束时间")
    InstrumentID: str = Field("", title="合约代码")


class WebCTPReqQryOptionSelfClose(WebCTPRequest):
    QryOptionSelfClose: QryOptionSelfCloseField = Field(title="期权自对冲查询")


class ExchangeOptionSelfCloseField(BaseModel):
    """交易所期权自对冲信息"""

    Volume: int = Field(0, title="数量")
    RequestID: int = Field(0, title="请求编号")
    BusinessUnit: str = Field("", title="业务单元")
    HedgeFlag: str = Field("", title="投机套保标志")
    OptSelfCloseFlag: str = Field("", title="期权行权的头寸是否自对冲")
    OptionSelfCloseLocalID: str = Field("", title="本地期权自对冲编号")
    ExchangeID: str = Field("", title="交易所代码")
    ParticipantID: str = Field("", title="会员代码")
    ClientID: str = Field("", title="客户代码")
    reserve1: str = Field("", title="保留的无效字段")
    TraderID: str = Field("", title="交易所交易员代码")
    InstallID: int = Field(0, title="安装编号")
    OrderSubmitStatus: str = Field("", title="期权自对冲提交状态")
    NotifySequence: int = Field(0, title="报单提示序号")
    TradingDay: str = Field("", title="交易日")
    SettlementID: int = Field(0, title="结算编号")
    OptionSelfCloseSysID: str = Field("", title="期权自对冲编号")
    InsertDate: str = Field("", title="报单日期")
    InsertTime: str = Field("", title="插入时间")
    CancelTime: str = Field("", title="撤销时间")
    ExecResult: str = Field("", title="自对冲结果")
    ClearingPartID: str = Field("", title="结算会员编号")
    SequenceNo: int = Field(0, title="序号")
    BranchID: str = Field("", title="营业部编号")
    reserve2: str = Field("", title="保留的无效字段")
    MacAddress: str = Field("", title="Mac地址")
    ExchangeInstID: str = Field("", title="合约在交易所的代码")
    IPAddress: str = Field("", title="IP地址")


class WebCTPReqExchangeOptionSelfClose(WebCTPRequest):
    ExchangeOptionSelfClose: ExchangeOptionSelfCloseField = Field(
        title="交易所期权自对冲信息")


class QryOptionSelfCloseActionField(BaseModel):
    """期权自对冲操作查询"""

    BrokerID: str = Field("", title="经纪公司代码")
    InvestorID: str = Field("", title="投资者代码")
    ExchangeID: str = Field("", title="交易所代码")


class WebCTPReqQryOptionSelfCloseAction(WebCTPRequest):
    QryOptionSelfCloseAction: QryOptionSelfCloseActionField = Field(
        title="期权自对冲操作查询")


class ExchangeOptionSelfCloseActionField(BaseModel):
    """交易所期权自对冲操作"""

    ExchangeID: str = Field("", title="交易所代码")
    OptionSelfCloseSysID: str = Field("", title="期权自对冲操作编号")
    ActionFlag: str = Field("", title="操作标志")
    ActionDate: str = Field("", title="操作日期")
    ActionTime: str = Field("", title="操作时间")
    TraderID: str = Field("", title="交易所交易员代码")
    InstallID: int = Field(0, title="安装编号")
    OptionSelfCloseLocalID: str = Field("", title="本地期权自对冲编号")
    ActionLocalID: str = Field("", title="操作本地编号")
    ParticipantID: str = Field("", title="会员代码")
    ClientID: str = Field("", title="客户代码")
    BusinessUnit: str = Field("", title="业务单元")
    OrderActionStatus: str = Field("", title="报单操作状态")
    UserID: str = Field("", title="用户代码")
    BranchID: str = Field("", title="营业部编号")
    reserve1: str = Field("", title="保留的无效字段")
    MacAddress: str = Field("", title="Mac地址")
    reserve2: str = Field("", title="保留的无效字段")
    OptSelfCloseFlag: str = Field("", title="期权行权的头寸是否自对冲")
    IPAddress: str = Field("", title="IP地址")
    ExchangeInstID: str = Field("", title="合约在交易所的代码")


class WebCTPReqExchangeOptionSelfCloseAction(WebCTPRequest):
    ExchangeOptionSelfCloseAction: ExchangeOptionSelfCloseActionField = Field(
        title="交易所期权自对冲操作")


class SyncDelaySwapField(BaseModel):
    """延时换汇同步"""

    DelaySwapSeqNo: str = Field("", title="换汇流水号")
    BrokerID: str = Field("", title="经纪公司代码")
    InvestorID: str = Field("", title="投资者代码")
    FromCurrencyID: str = Field("", title="源币种")
    FromAmount: float = Field(0.0, title="源金额")
    FromFrozenSwap: float = Field(0.0, title="源换汇冻结金额(可用冻结)")
    FromRemainSwap: float = Field(0.0, title="源剩余换汇额度(可提冻结)")
    ToCurrencyID: str = Field("", title="目标币种")
    ToAmount: float = Field(0.0, title="目标金额")
    IsManualSwap: int = Field(0, title="是否手工换汇")
    IsAllRemainSetZero: int = Field(0,
                                    title="是否将所有外币的剩余换汇额度设置为0")


class WebCTPReqSyncDelaySwap(WebCTPRequest):
    SyncDelaySwap: SyncDelaySwapField = Field(title="延时换汇同步")


class QrySyncDelaySwapField(BaseModel):
    """查询延时换汇同步"""

    BrokerID: str = Field("", title="经纪公司代码")
    DelaySwapSeqNo: str = Field("", title="延时换汇流水号")


class WebCTPReqQrySyncDelaySwap(WebCTPRequest):
    QrySyncDelaySwap: QrySyncDelaySwapField = Field(title="查询延时换汇同步")


class InvestUnitField(BaseModel):
    """投资单元"""

    BrokerID: str = Field("", title="经纪公司代码")
    InvestorID: str = Field("", title="投资者代码")
    InvestUnitID: str = Field("", title="投资单元代码")
    InvestorUnitName: str = Field("", title="投资者单元名称")
    InvestorGroupID: str = Field("", title="投资者分组代码")
    CommModelID: str = Field("", title="手续费率模板代码")
    MarginModelID: str = Field("", title="保证金率模板代码")
    AccountID: str = Field("", title="资金账号")
    CurrencyID: str = Field("", title="币种代码")


class WebCTPReqInvestUnit(WebCTPRequest):
    InvestUnit: InvestUnitField = Field(title="投资单元")


class QryInvestUnitField(BaseModel):
    """查询投资单元"""

    BrokerID: str = Field("", title="经纪公司代码")
    InvestorID: str = Field("", title="投资者代码")
    InvestUnitID: str = Field("", title="投资单元代码")


class WebCTPReqQryInvestUnit(WebCTPRequest):
    QryInvestUnit: QryInvestUnitField = Field(title="查询投资单元")


class SecAgentCheckModeField(BaseModel):
    """二级代理商资金校验模式"""

    InvestorID: str = Field("", title="投资者代码")
    BrokerID: str = Field("", title="经纪公司代码")
    CurrencyID: str = Field("", title="币种")
    BrokerSecAgentID: str = Field("", title="境外中介机构资金帐号")
    CheckSelfAccount: int = Field(0, title="是否需要校验自己的资金账户")


class WebCTPReqSecAgentCheckMode(WebCTPRequest):
    SecAgentCheckMode: SecAgentCheckModeField = Field(
        title="二级代理商资金校验模式")


class SecAgentTradeInfoField(BaseModel):
    """二级代理商信息"""

    BrokerID: str = Field("", title="经纪公司代码")
    BrokerSecAgentID: str = Field("", title="境外中介机构资金帐号")
    InvestorID: str = Field("", title="投资者代码")
    LongCustomerName: str = Field("", title="二级代理商姓名")


class WebCTPReqSecAgentTradeInfo(WebCTPRequest):
    SecAgentTradeInfo: SecAgentTradeInfoField = Field(title="二级代理商信息")


class MarketDataField(BaseModel):
    """市场行情"""

    TradingDay: str = Field("", title="交易日")
    reserve1: str = Field("", title="保留的无效字段")
    ExchangeID: str = Field("", title="交易所代码")
    reserve2: str = Field("", title="保留的无效字段")
    LastPrice: float = Field(0.0, title="最新价")
    PreSettlementPrice: float = Field(0.0, title="上次结算价")
    PreClosePrice: float = Field(0.0, title="昨收盘")
    PreOpenInterest: float = Field(0.0, title="昨持仓量")
    OpenPrice: float = Field(0.0, title="今开盘")
    HighestPrice: float = Field(0.0, title="最高价")
    LowestPrice: float = Field(0.0, title="最低价")
    Volume: int = Field(0, title="数量")
    Turnover: float = Field(0.0, title="成交金额")
    OpenInterest: float = Field(0.0, title="持仓量")
    ClosePrice: float = Field(0.0, title="今收盘")
    SettlementPrice: float = Field(0.0, title="本次结算价")
    UpperLimitPrice: float = Field(0.0, title="涨停板价")
    LowerLimitPrice: float = Field(0.0, title="跌停板价")
    PreDelta: float = Field(0.0, title="昨虚实度")
    CurrDelta: float = Field(0.0, title="今虚实度")
    UpdateTime: str = Field("", title="最后修改时间")
    UpdateMillisec: int = Field(0, title="最后修改毫秒")
    ActionDay: str = Field("", title="业务日期")
    InstrumentID: str = Field("", title="合约代码")
    ExchangeInstID: str = Field("", title="合约在交易所的代码")


class WebCTPReqMarketData(WebCTPRequest):
    MarketData: MarketDataField = Field(title="市场行情")


class MarketDataBaseField(BaseModel):
    """行情基础属性"""

    TradingDay: str = Field("", title="交易日")
    PreSettlementPrice: float = Field(0.0, title="上次结算价")
    PreClosePrice: float = Field(0.0, title="昨收盘")
    PreOpenInterest: float = Field(0.0, title="昨持仓量")
    PreDelta: float = Field(0.0, title="昨虚实度")


class WebCTPReqMarketDataBase(WebCTPRequest):
    MarketDataBase: MarketDataBaseField = Field(title="行情基础属性")


class MarketDataStaticField(BaseModel):
    """行情静态属性"""

    OpenPrice: float = Field(0.0, title="今开盘")
    HighestPrice: float = Field(0.0, title="最高价")
    LowestPrice: float = Field(0.0, title="最低价")
    ClosePrice: float = Field(0.0, title="今收盘")
    UpperLimitPrice: float = Field(0.0, title="涨停板价")
    LowerLimitPrice: float = Field(0.0, title="跌停板价")
    SettlementPrice: float = Field(0.0, title="本次结算价")
    CurrDelta: float = Field(0.0, title="今虚实度")


class WebCTPReqMarketDataStatic(WebCTPRequest):
    MarketDataStatic: MarketDataStaticField = Field(title="行情静态属性")


class MarketDataLastMatchField(BaseModel):
    """行情最新成交属性"""

    LastPrice: float = Field(0.0, title="最新价")
    Volume: int = Field(0, title="数量")
    Turnover: float = Field(0.0, title="成交金额")
    OpenInterest: float = Field(0.0, title="持仓量")


class WebCTPReqMarketDataLastMatch(WebCTPRequest):
    MarketDataLastMatch: MarketDataLastMatchField = Field(
        title="行情最新成交属性")


class MarketDataBestPriceField(BaseModel):
    """行情最优价属性"""

    BidPrice1: float = Field(0.0, title="申买价一")
    BidVolume1: int = Field(0, title="申买量一")
    AskPrice1: float = Field(0.0, title="申卖价一")
    AskVolume1: int = Field(0, title="申卖量一")


class WebCTPReqMarketDataBestPrice(WebCTPRequest):
    MarketDataBestPrice: MarketDataBestPriceField = Field(
        title="行情最优价属性")


class MarketDataBid23Field(BaseModel):
    """行情申买二、三属性"""

    BidPrice2: float = Field(0.0, title="申买价二")
    BidVolume2: int = Field(0, title="申买量二")
    BidPrice3: float = Field(0.0, title="申买价三")
    BidVolume3: int = Field(0, title="申买量三")


class WebCTPReqMarketDataBid23(WebCTPRequest):
    MarketDataBid23: MarketDataBid23Field = Field(title="行情申买二、三属性")


class MarketDataAsk23Field(BaseModel):
    """行情申卖二、三属性"""

    AskPrice2: float = Field(0.0, title="申卖价二")
    AskVolume2: int = Field(0, title="申卖量二")
    AskPrice3: float = Field(0.0, title="申卖价三")
    AskVolume3: int = Field(0, title="申卖量三")


class WebCTPReqMarketDataAsk23(WebCTPRequest):
    MarketDataAsk23: MarketDataAsk23Field = Field(title="行情申卖二、三属性")


class MarketDataBid45Field(BaseModel):
    """行情申买四、五属性"""

    BidPrice4: float = Field(0.0, title="申买价四")
    BidVolume4: int = Field(0, title="申买量四")
    BidPrice5: float = Field(0.0, title="申买价五")
    BidVolume5: int = Field(0, title="申买量五")


class WebCTPReqMarketDataBid45(WebCTPRequest):
    MarketDataBid45: MarketDataBid45Field = Field(title="行情申买四、五属性")


class MarketDataAsk45Field(BaseModel):
    """行情申卖四、五属性"""

    AskPrice4: float = Field(0.0, title="申卖价四")
    AskVolume4: int = Field(0, title="申卖量四")
    AskPrice5: float = Field(0.0, title="申卖价五")
    AskVolume5: int = Field(0, title="申卖量五")


class WebCTPReqMarketDataAsk45(WebCTPRequest):
    MarketDataAsk45: MarketDataAsk45Field = Field(title="行情申卖四、五属性")


class MarketDataUpdateTimeField(BaseModel):
    """行情更新时间属性"""

    reserve1: str = Field("", title="保留的无效字段")
    UpdateTime: str = Field("", title="最后修改时间")
    UpdateMillisec: int = Field(0, title="最后修改毫秒")
    ActionDay: str = Field("", title="业务日期")
    InstrumentID: str = Field("", title="合约代码")


class WebCTPReqMarketDataUpdateTime(WebCTPRequest):
    MarketDataUpdateTime: MarketDataUpdateTimeField = Field(
        title="行情更新时间属性")


class MarketDataExchangeField(BaseModel):
    """行情交易所代码属性"""

    ExchangeID: str = Field("", title="交易所代码")


class WebCTPReqMarketDataExchange(WebCTPRequest):
    MarketDataExchange: MarketDataExchangeField = Field(
        title="行情交易所代码属性")


class SpecificInstrumentField(BaseModel):
    """指定的合约"""

    reserve1: str = Field("", title="保留的无效字段")
    InstrumentID: str = Field("", title="合约代码")


class WebCTPReqSpecificInstrument(WebCTPRequest):
    SpecificInstrument: SpecificInstrumentField = Field(title="指定的合约")


class InstrumentStatusField(BaseModel):
    """合约状态"""

    ExchangeID: str = Field("", title="交易所代码")
    reserve1: str = Field("", title="保留的无效字段")
    SettlementGroupID: str = Field("", title="结算组代码")
    reserve2: str = Field("", title="保留的无效字段")
    InstrumentStatus: str = Field("", title="合约交易状态")
    TradingSegmentSN: int = Field(0, title="交易阶段编号")
    EnterTime: str = Field("", title="进入本状态时间")
    EnterReason: str = Field("", title="进入本状态原因")
    ExchangeInstID: str = Field("", title="合约在交易所的代码")
    InstrumentID: str = Field("", title="合约代码")


class WebCTPReqInstrumentStatus(WebCTPRequest):
    InstrumentStatus: InstrumentStatusField = Field(title="合约状态")


class QryInstrumentStatusField(BaseModel):
    """查询合约状态"""

    ExchangeID: str = Field("", title="交易所代码")
    reserve1: str = Field("", title="保留的无效字段")
    ExchangeInstID: str = Field("", title="合约在交易所的代码")


class WebCTPReqQryInstrumentStatus(WebCTPRequest):
    QryInstrumentStatus: QryInstrumentStatusField = Field(title="查询合约状态")


class InvestorAccountField(BaseModel):
    """投资者账户"""

    BrokerID: str = Field("", title="经纪公司代码")
    InvestorID: str = Field("", title="投资者代码")
    AccountID: str = Field("", title="投资者帐号")
    CurrencyID: str = Field("", title="币种代码")


class WebCTPReqInvestorAccount(WebCTPRequest):
    InvestorAccount: InvestorAccountField = Field(title="投资者账户")


class PositionProfitAlgorithmField(BaseModel):
    """浮动盈亏算法"""

    BrokerID: str = Field("", title="经纪公司代码")
    AccountID: str = Field("", title="投资者帐号")
    Algorithm: str = Field("", title="盈亏算法")
    Memo: str = Field("", title="备注")
    CurrencyID: str = Field("", title="币种代码")


class WebCTPReqPositionProfitAlgorithm(WebCTPRequest):
    PositionProfitAlgorithm: PositionProfitAlgorithmField = Field(
        title="浮动盈亏算法")


class DiscountField(BaseModel):
    """会员资金折扣"""

    BrokerID: str = Field("", title="经纪公司代码")
    InvestorRange: str = Field("", title="投资者范围")
    InvestorID: str = Field("", title="投资者代码")
    Discount: float = Field(0.0, title="资金折扣比例")


class WebCTPReqDiscount(WebCTPRequest):
    Discount: DiscountField = Field(title="会员资金折扣")


class QryTransferBankField(BaseModel):
    """查询转帐银行"""

    BankID: str = Field("", title="银行代码")
    BankBrchID: str = Field("", title="银行分中心代码")


class WebCTPReqQryTransferBank(WebCTPRequest):
    QryTransferBank: QryTransferBankField = Field(title="查询转帐银行")


class TransferBankField(BaseModel):
    """转帐银行"""

    BankID: str = Field("", title="银行代码")
    BankBrchID: str = Field("", title="银行分中心代码")
    BankName: str = Field("", title="银行名称")
    IsActive: int = Field(0, title="是否活跃")


class WebCTPReqTransferBank(WebCTPRequest):
    TransferBank: TransferBankField = Field(title="转帐银行")


class QryInvestorPositionDetailField(BaseModel):
    """查询投资者持仓明细"""

    BrokerID: str = Field("", title="经纪公司代码")
    InvestorID: str = Field("", title="投资者代码")
    reserve1: str = Field("", title="保留的无效字段")
    ExchangeID: str = Field("", title="交易所代码")
    InvestUnitID: str = Field("", title="投资单元代码")
    InstrumentID: str = Field("", title="合约代码")


class WebCTPReqQryInvestorPositionDetail(WebCTPRequest):
    QryInvestorPositionDetail: QryInvestorPositionDetailField = Field(
        title="查询投资者持仓明细")


class InvestorPositionDetailField(BaseModel):
    """投资者持仓明细"""

    reserve1: str = Field("", title="保留的无效字段")
    BrokerID: str = Field("", title="经纪公司代码")
    InvestorID: str = Field("", title="投资者代码")
    HedgeFlag: str = Field("", title="投机套保标志")
    Direction: str = Field("", title="买卖")
    OpenDate: str = Field("", title="开仓日期")
    TradeID: str = Field("", title="成交编号")
    Volume: int = Field(0, title="数量")
    OpenPrice: float = Field(0.0, title="开仓价")
    TradingDay: str = Field("", title="交易日")
    SettlementID: int = Field(0, title="结算编号")
    TradeType: str = Field("", title="成交类型")
    reserve2: str = Field("", title="保留的无效字段")
    ExchangeID: str = Field("", title="交易所代码")
    CloseProfitByDate: float = Field(0.0, title="逐日盯市平仓盈亏")
    CloseProfitByTrade: float = Field(0.0, title="逐笔对冲平仓盈亏")
    PositionProfitByDate: float = Field(0.0, title="逐日盯市持仓盈亏")
    PositionProfitByTrade: float = Field(0.0, title="逐笔对冲持仓盈亏")
    Margin: float = Field(0.0, title="投资者保证金")
    ExchMargin: float = Field(0.0, title="交易所保证金")
    MarginRateByMoney: float = Field(0.0, title="保证金率")
    MarginRateByVolume: float = Field(0.0, title="保证金率(按手数)")
    LastSettlementPrice: float = Field(0.0, title="昨结算价")
    SettlementPrice: float = Field(0.0, title="结算价")
    CloseVolume: int = Field(0, title="平仓量")
    CloseAmount: float = Field(0.0, title="平仓金额")
    TimeFirstVolume: int = Field(0, title="先开先平剩余数量")
    InvestUnitID: str = Field("", title="投资单元代码")
    SpecPosiType: str = Field("", title="特殊持仓标志")
    InstrumentID: str = Field("", title="合约代码")
    CombInstrumentID: str = Field("", title="组合合约代码")


class WebCTPReqInvestorPositionDetail(WebCTPRequest):
    InvestorPositionDetail: InvestorPositionDetailField = Field(
        title="投资者持仓明细")


class TradingAccountPasswordField(BaseModel):
    """资金账户口令域"""

    BrokerID: str = Field("", title="经纪公司代码")
    AccountID: str = Field("", title="投资者帐号")
    Password: str = Field("", title="密码")
    CurrencyID: str = Field("", title="币种代码")


class WebCTPReqTradingAccountPassword(WebCTPRequest):
    TradingAccountPassword: TradingAccountPasswordField = Field(
        title="资金账户口令域")


class MDTraderOfferField(BaseModel):
    """交易所行情报盘机"""

    ExchangeID: str = Field("", title="交易所代码")
    TraderID: str = Field("", title="交易所交易员代码")
    ParticipantID: str = Field("", title="会员代码")
    Password: str = Field("", title="密码")
    InstallID: int = Field(0, title="安装编号")
    OrderLocalID: str = Field("", title="本地报单编号")
    TraderConnectStatus: str = Field("", title="交易所交易员连接状态")
    ConnectRequestDate: str = Field("", title="发出连接请求的日期")
    ConnectRequestTime: str = Field("", title="发出连接请求的时间")
    LastReportDate: str = Field("", title="上次报告日期")
    LastReportTime: str = Field("", title="上次报告时间")
    ConnectDate: str = Field("", title="完成连接日期")
    ConnectTime: str = Field("", title="完成连接时间")
    StartDate: str = Field("", title="启动日期")
    StartTime: str = Field("", title="启动时间")
    TradingDay: str = Field("", title="交易日")
    BrokerID: str = Field("", title="经纪公司代码")
    MaxTradeID: str = Field("", title="本席位最大成交编号")
    MaxOrderMessageReference: str = Field("", title="本席位最大报单备拷")
    OrderCancelAlg: str = Field("", title="撤单时选择席位算法")


class WebCTPReqMDTraderOffer(WebCTPRequest):
    MDTraderOffer: MDTraderOfferField = Field(title="交易所行情报盘机")


class QryMDTraderOfferField(BaseModel):
    """查询行情报盘机"""

    ExchangeID: str = Field("", title="交易所代码")
    ParticipantID: str = Field("", title="会员代码")
    TraderID: str = Field("", title="交易所交易员代码")


class WebCTPReqQryMDTraderOffer(WebCTPRequest):
    QryMDTraderOffer: QryMDTraderOfferField = Field(title="查询行情报盘机")


class QryNoticeField(BaseModel):
    """查询客户通知"""

    BrokerID: str = Field("", title="经纪公司代码")


class WebCTPReqQryNotice(WebCTPRequest):
    QryNotice: QryNoticeField = Field(title="查询客户通知")


class NoticeField(BaseModel):
    """客户通知"""

    BrokerID: str = Field("", title="经纪公司代码")
    Content: str = Field("", title="消息正文")
    SequenceLabel: str = Field("", title="经纪公司通知内容序列号")


class WebCTPReqNotice(WebCTPRequest):
    Notice: NoticeField = Field(title="客户通知")


class UserRightField(BaseModel):
    """用户权限"""

    BrokerID: str = Field("", title="经纪公司代码")
    UserID: str = Field("", title="用户代码")
    UserRightType: str = Field("", title="客户权限类型")
    IsForbidden: int = Field(0, title="是否禁止")


class WebCTPReqUserRight(WebCTPRequest):
    UserRight: UserRightField = Field(title="用户权限")


class QrySettlementInfoConfirmField(BaseModel):
    """查询结算信息确认域"""

    BrokerID: str = Field("", title="经纪公司代码")
    InvestorID: str = Field("", title="投资者代码")
    AccountID: str = Field("", title="投资者帐号")
    CurrencyID: str = Field("", title="币种代码")


class WebCTPReqQrySettlementInfoConfirm(WebCTPRequest):
    QrySettlementInfoConfirm: QrySettlementInfoConfirmField = Field(
        title="查询结算信息确认域")


class LoadSettlementInfoField(BaseModel):
    """装载结算信息"""

    BrokerID: str = Field("", title="经纪公司代码")


class WebCTPReqLoadSettlementInfo(WebCTPRequest):
    LoadSettlementInfo: LoadSettlementInfoField = Field(title="装载结算信息")


class BrokerWithdrawAlgorithmField(BaseModel):
    """经纪公司可提资金算法表"""

    BrokerID: str = Field("", title="经纪公司代码")
    WithdrawAlgorithm: str = Field("", title="可提资金算法")
    UsingRatio: float = Field(0.0, title="资金使用率")
    IncludeCloseProfit: str = Field("", title="可提是否包含平仓盈利")
    AllWithoutTrade: str = Field("",
                                 title="本日无仓且无成交客户是否受可提比例限制")
    AvailIncludeCloseProfit: str = Field("", title="可用是否包含平仓盈利")
    IsBrokerUserEvent: int = Field(0, title="是否启用用户事件")
    CurrencyID: str = Field("", title="币种代码")
    FundMortgageRatio: float = Field(0.0, title="货币质押比率")
    BalanceAlgorithm: str = Field("", title="权益算法")


class WebCTPReqBrokerWithdrawAlgorithm(WebCTPRequest):
    BrokerWithdrawAlgorithm: BrokerWithdrawAlgorithmField = Field(
        title="经纪公司可提资金算法表")


class TradingAccountPasswordUpdateV1Field(BaseModel):
    """资金账户口令变更域"""

    BrokerID: str = Field("", title="经纪公司代码")
    InvestorID: str = Field("", title="投资者代码")
    OldPassword: str = Field("", title="原来的口令")
    NewPassword: str = Field("", title="新的口令")


class WebCTPReqTradingAccountPasswordUpdateV1(WebCTPRequest):
    TradingAccountPasswordUpdateV1: TradingAccountPasswordUpdateV1Field = Field(
        title="资金账户口令变更域")


class TradingAccountPasswordUpdateField(BaseModel):
    """资金账户口令变更域"""

    BrokerID: str = Field("", title="经纪公司代码")
    AccountID: str = Field("", title="投资者帐号")
    OldPassword: str = Field("", title="原来的口令")
    NewPassword: str = Field("", title="新的口令")
    CurrencyID: str = Field("", title="币种代码")


class WebCTPReqTradingAccountPasswordUpdate(WebCTPRequest):
    TradingAccountPasswordUpdate: TradingAccountPasswordUpdateField = Field(
        title="资金账户口令变更域")


class QryCombinationLegField(BaseModel):
    """查询组合合约分腿"""

    reserve1: str = Field("", title="保留的无效字段")
    LegID: int = Field(0, title="单腿编号")
    reserve2: str = Field("", title="保留的无效字段")
    CombInstrumentID: str = Field("", title="组合合约代码")
    LegInstrumentID: str = Field("", title="单腿合约代码")


class WebCTPReqQryCombinationLeg(WebCTPRequest):
    QryCombinationLeg: QryCombinationLegField = Field(title="查询组合合约分腿")


class QrySyncStatusField(BaseModel):
    """查询组合合约分腿"""

    TradingDay: str = Field("", title="交易日")


class WebCTPReqQrySyncStatus(WebCTPRequest):
    QrySyncStatus: QrySyncStatusField = Field(title="查询组合合约分腿")


class CombinationLegField(BaseModel):
    """组合交易合约的单腿"""

    reserve1: str = Field("", title="保留的无效字段")
    LegID: int = Field(0, title="单腿编号")
    reserve2: str = Field("", title="保留的无效字段")
    Direction: str = Field("", title="买卖方向")
    LegMultiple: int = Field(0, title="单腿乘数")
    ImplyLevel: int = Field(0, title="派生层数")
    CombInstrumentID: str = Field("", title="组合合约代码")
    LegInstrumentID: str = Field("", title="单腿合约代码")


class WebCTPReqCombinationLeg(WebCTPRequest):
    CombinationLeg: CombinationLegField = Field(title="组合交易合约的单腿")


class SyncStatusField(BaseModel):
    """数据同步状态"""

    TradingDay: str = Field("", title="交易日")
    DataSyncStatus: str = Field("", title="数据同步状态")


class WebCTPReqSyncStatus(WebCTPRequest):
    SyncStatus: SyncStatusField = Field(title="数据同步状态")


class QryLinkManField(BaseModel):
    """查询联系人"""

    BrokerID: str = Field("", title="经纪公司代码")
    InvestorID: str = Field("", title="投资者代码")


class WebCTPReqQryLinkMan(WebCTPRequest):
    QryLinkMan: QryLinkManField = Field(title="查询联系人")


class LinkManField(BaseModel):
    """联系人"""

    BrokerID: str = Field("", title="经纪公司代码")
    InvestorID: str = Field("", title="投资者代码")
    PersonType: str = Field("", title="联系人类型")
    IdentifiedCardType: str = Field("", title="证件类型")
    IdentifiedCardNo: str = Field("", title="证件号码")
    PersonName: str = Field("", title="名称")
    Telephone: str = Field("", title="联系电话")
    Address: str = Field("", title="通讯地址")
    ZipCode: str = Field("", title="邮政编码")
    Priority: int = Field(0, title="优先级")
    UOAZipCode: str = Field("", title="开户邮政编码")
    PersonFullName: str = Field("", title="全称")


class WebCTPReqLinkMan(WebCTPRequest):
    LinkMan: LinkManField = Field(title="联系人")


class QryBrokerUserEventField(BaseModel):
    """查询经纪公司用户事件"""

    BrokerID: str = Field("", title="经纪公司代码")
    UserID: str = Field("", title="用户代码")
    UserEventType: str = Field("", title="用户事件类型")


class WebCTPReqQryBrokerUserEvent(WebCTPRequest):
    QryBrokerUserEvent: QryBrokerUserEventField = Field(
        title="查询经纪公司用户事件")


class BrokerUserEventField(BaseModel):
    """查询经纪公司用户事件"""

    BrokerID: str = Field("", title="经纪公司代码")
    UserID: str = Field("", title="用户代码")
    UserEventType: str = Field("", title="用户事件类型")
    EventSequenceNo: int = Field(0, title="用户事件序号")
    EventDate: str = Field("", title="事件发生日期")
    EventTime: str = Field("", title="事件发生时间")
    UserEventInfo: str = Field("", title="用户事件信息")
    InvestorID: str = Field("", title="投资者代码")
    reserve1: str = Field("", title="保留的无效字段")
    InstrumentID: str = Field("", title="合约代码")
    DRIdentityID: int = Field(0, title="交易中心代码")
    TradingDay: str = Field("", title="交易日")


class WebCTPReqBrokerUserEvent(WebCTPRequest):
    BrokerUserEvent: BrokerUserEventField = Field(title="查询经纪公司用户事件")


class QryContractBankField(BaseModel):
    """查询签约银行请求"""

    BrokerID: str = Field("", title="经纪公司代码")
    BankID: str = Field("", title="银行代码")
    BankBrchID: str = Field("", title="银行分中心代码")


class WebCTPReqQryContractBank(WebCTPRequest):
    QryContractBank: QryContractBankField = Field(title="查询签约银行请求")


class ContractBankField(BaseModel):
    """查询签约银行响应"""

    BrokerID: str = Field("", title="经纪公司代码")
    BankID: str = Field("", title="银行代码")
    BankBrchID: str = Field("", title="银行分中心代码")
    BankName: str = Field("", title="银行名称")


class WebCTPReqContractBank(WebCTPRequest):
    ContractBank: ContractBankField = Field(title="查询签约银行响应")


class InvestorPositionCombineDetailField(BaseModel):
    """投资者组合持仓明细"""

    TradingDay: str = Field("", title="交易日")
    OpenDate: str = Field("", title="开仓日期")
    ExchangeID: str = Field("", title="交易所代码")
    SettlementID: int = Field(0, title="结算编号")
    BrokerID: str = Field("", title="经纪公司代码")
    InvestorID: str = Field("", title="投资者代码")
    ComTradeID: str = Field("", title="组合编号")
    TradeID: str = Field("", title="撮合编号")
    reserve1: str = Field("", title="保留的无效字段")
    HedgeFlag: str = Field("", title="投机套保标志")
    Direction: str = Field("", title="买卖")
    TotalAmt: int = Field(0, title="持仓量")
    Margin: float = Field(0.0, title="投资者保证金")
    ExchMargin: float = Field(0.0, title="交易所保证金")
    MarginRateByMoney: float = Field(0.0, title="保证金率")
    MarginRateByVolume: float = Field(0.0, title="保证金率(按手数)")
    LegID: int = Field(0, title="单腿编号")
    LegMultiple: int = Field(0, title="单腿乘数")
    reserve2: str = Field("", title="保留的无效字段")
    TradeGroupID: int = Field(0, title="成交组号")
    InvestUnitID: str = Field("", title="投资单元代码")
    InstrumentID: str = Field("", title="合约代码")
    CombInstrumentID: str = Field("", title="组合持仓合约编码")


class WebCTPReqInvestorPositionCombineDetail(WebCTPRequest):
    InvestorPositionCombineDetail: InvestorPositionCombineDetailField = Field(
        title="投资者组合持仓明细")


class ParkedOrderField(BaseModel):
    """预埋单"""

    BrokerID: str = Field("", title="经纪公司代码")
    InvestorID: str = Field("", title="投资者代码")
    reserve1: str = Field("", title="保留的无效字段")
    OrderRef: str = Field("", title="报单引用")
    UserID: str = Field("", title="用户代码")
    OrderPriceType: str = Field("", title="报单价格条件")
    Direction: str = Field("", title="买卖方向")
    CombOffsetFlag: str = Field("", title="组合开平标志")
    CombHedgeFlag: str = Field("", title="组合投机套保标志")
    LimitPrice: float = Field(0.0, title="价格")
    VolumeTotalOriginal: int = Field(0, title="数量")
    TimeCondition: str = Field("", title="有效期类型")
    GTDDate: str = Field("", title="GTD日期")
    VolumeCondition: str = Field("", title="成交量类型")
    MinVolume: int = Field(0, title="最小成交量")
    ContingentCondition: str = Field("", title="触发条件")
    StopPrice: float = Field(0.0, title="止损价")
    ForceCloseReason: str = Field("", title="强平原因")
    IsAutoSuspend: int = Field(0, title="自动挂起标志")
    BusinessUnit: str = Field("", title="业务单元")
    RequestID: int = Field(0, title="请求编号")
    UserForceClose: int = Field(0, title="用户强评标志")
    ExchangeID: str = Field("", title="交易所代码")
    ParkedOrderID: str = Field("", title="预埋报单编号")
    UserType: str = Field("", title="用户类型")
    Status: str = Field("", title="预埋单状态")
    ErrorID: int = Field(0, title="错误代码")
    ErrorMsg: str = Field("", title="错误信息")
    IsSwapOrder: int = Field(0, title="互换单标志")
    AccountID: str = Field("", title="资金账号")
    CurrencyID: str = Field("", title="币种代码")
    ClientID: str = Field("", title="交易编码")
    InvestUnitID: str = Field("", title="投资单元代码")
    reserve2: str = Field("", title="保留的无效字段")
    MacAddress: str = Field("", title="Mac地址")
    InstrumentID: str = Field("", title="合约代码")
    IPAddress: str = Field("", title="IP地址")


class WebCTPReqParkedOrder(WebCTPRequest):
    ParkedOrder: ParkedOrderField = Field(title="预埋单")


class ParkedOrderActionField(BaseModel):
    """输入预埋单操作"""

    BrokerID: str = Field("", title="经纪公司代码")
    InvestorID: str = Field("", title="投资者代码")
    OrderActionRef: int = Field(0, title="报单操作引用")
    OrderRef: str = Field("", title="报单引用")
    RequestID: int = Field(0, title="请求编号")
    FrontID: int = Field(0, title="前置编号")
    SessionID: int = Field(0, title="会话编号")
    ExchangeID: str = Field("", title="交易所代码")
    OrderSysID: str = Field("", title="报单编号")
    ActionFlag: str = Field("", title="操作标志")
    LimitPrice: float = Field(0.0, title="价格")
    VolumeChange: int = Field(0, title="数量变化")
    UserID: str = Field("", title="用户代码")
    reserve1: str = Field("", title="保留的无效字段")
    ParkedOrderActionID: str = Field("", title="预埋撤单单编号")
    UserType: str = Field("", title="用户类型")
    Status: str = Field("", title="预埋撤单状态")
    ErrorID: int = Field(0, title="错误代码")
    ErrorMsg: str = Field("", title="错误信息")
    InvestUnitID: str = Field("", title="投资单元代码")
    reserve2: str = Field("", title="保留的无效字段")
    MacAddress: str = Field("", title="Mac地址")
    InstrumentID: str = Field("", title="合约代码")
    IPAddress: str = Field("", title="IP地址")


class WebCTPReqParkedOrderAction(WebCTPRequest):
    ParkedOrderAction: ParkedOrderActionField = Field(title="输入预埋单操作")


class QryParkedOrderField(BaseModel):
    """查询预埋单"""

    BrokerID: str = Field("", title="经纪公司代码")
    InvestorID: str = Field("", title="投资者代码")
    reserve1: str = Field("", title="保留的无效字段")
    ExchangeID: str = Field("", title="交易所代码")
    InvestUnitID: str = Field("", title="投资单元代码")
    InstrumentID: str = Field("", title="合约代码")


class WebCTPReqQryParkedOrder(WebCTPRequest):
    QryParkedOrder: QryParkedOrderField = Field(title="查询预埋单")


class QryParkedOrderActionField(BaseModel):
    """查询预埋撤单"""

    BrokerID: str = Field("", title="经纪公司代码")
    InvestorID: str = Field("", title="投资者代码")
    reserve1: str = Field("", title="保留的无效字段")
    ExchangeID: str = Field("", title="交易所代码")
    InvestUnitID: str = Field("", title="投资单元代码")
    InstrumentID: str = Field("", title="合约代码")


class WebCTPReqQryParkedOrderAction(WebCTPRequest):
    QryParkedOrderAction: QryParkedOrderActionField = Field(
        title="查询预埋撤单")


class RemoveParkedOrderField(BaseModel):
    """删除预埋单"""

    BrokerID: str = Field("", title="经纪公司代码")
    InvestorID: str = Field("", title="投资者代码")
    ParkedOrderID: str = Field("", title="预埋报单编号")
    InvestUnitID: str = Field("", title="投资单元代码")


class WebCTPReqRemoveParkedOrder(WebCTPRequest):
    RemoveParkedOrder: RemoveParkedOrderField = Field(title="删除预埋单")


class RemoveParkedOrderActionField(BaseModel):
    """删除预埋撤单"""

    BrokerID: str = Field("", title="经纪公司代码")
    InvestorID: str = Field("", title="投资者代码")
    ParkedOrderActionID: str = Field("", title="预埋撤单编号")
    InvestUnitID: str = Field("", title="投资单元代码")


class WebCTPReqRemoveParkedOrderAction(WebCTPRequest):
    RemoveParkedOrderAction: RemoveParkedOrderActionField = Field(
        title="删除预埋撤单")


class InvestorWithdrawAlgorithmField(BaseModel):
    """经纪公司可提资金算法表"""

    BrokerID: str = Field("", title="经纪公司代码")
    InvestorRange: str = Field("", title="投资者范围")
    InvestorID: str = Field("", title="投资者代码")
    UsingRatio: float = Field(0.0, title="可提资金比例")
    CurrencyID: str = Field("", title="币种代码")
    FundMortgageRatio: float = Field(0.0, title="货币质押比率")


class WebCTPReqInvestorWithdrawAlgorithm(WebCTPRequest):
    InvestorWithdrawAlgorithm: InvestorWithdrawAlgorithmField = Field(
        title="经纪公司可提资金算法表")


class QryInvestorPositionCombineDetailField(BaseModel):
    """查询组合持仓明细"""

    BrokerID: str = Field("", title="经纪公司代码")
    InvestorID: str = Field("", title="投资者代码")
    reserve1: str = Field("", title="保留的无效字段")
    ExchangeID: str = Field("", title="交易所代码")
    InvestUnitID: str = Field("", title="投资单元代码")
    CombInstrumentID: str = Field("", title="组合持仓合约编码")


class WebCTPReqQryInvestorPositionCombineDetail(WebCTPRequest):
    QryInvestorPositionCombineDetail: QryInvestorPositionCombineDetailField = Field(
        title="查询组合持仓明细")


class MarketDataAveragePriceField(BaseModel):
    """成交均价"""

    AveragePrice: float = Field(0.0, title="当日均价")


class WebCTPReqMarketDataAveragePrice(WebCTPRequest):
    MarketDataAveragePrice: MarketDataAveragePriceField = Field(
        title="成交均价")


class VerifyInvestorPasswordField(BaseModel):
    """校验投资者密码"""

    BrokerID: str = Field("", title="经纪公司代码")
    InvestorID: str = Field("", title="投资者代码")
    Password: str = Field("", title="密码")


class WebCTPReqVerifyInvestorPassword(WebCTPRequest):
    VerifyInvestorPassword: VerifyInvestorPasswordField = Field(
        title="校验投资者密码")


class UserIPField(BaseModel):
    """用户IP"""

    BrokerID: str = Field("", title="经纪公司代码")
    UserID: str = Field("", title="用户代码")
    reserve1: str = Field("", title="保留的无效字段")
    reserve2: str = Field("", title="保留的无效字段")
    MacAddress: str = Field("", title="Mac地址")
    IPAddress: str = Field("", title="IP地址")
    IPMask: str = Field("", title="IP地址掩码")


class WebCTPReqUserIP(WebCTPRequest):
    UserIP: UserIPField = Field(title="用户IP")


class TradingNoticeInfoField(BaseModel):
    """用户事件通知信息"""

    BrokerID: str = Field("", title="经纪公司代码")
    InvestorID: str = Field("", title="投资者代码")
    SendTime: str = Field("", title="发送时间")
    FieldContent: str = Field("", title="消息正文")
    SequenceSeries: int = Field(0, title="序列系列号")
    SequenceNo: int = Field(0, title="序列号")
    InvestUnitID: str = Field("", title="投资单元代码")


class WebCTPReqTradingNoticeInfo(WebCTPRequest):
    TradingNoticeInfo: TradingNoticeInfoField = Field(title="用户事件通知信息")


class TradingNoticeField(BaseModel):
    """用户事件通知"""

    BrokerID: str = Field("", title="经纪公司代码")
    InvestorRange: str = Field("", title="投资者范围")
    InvestorID: str = Field("", title="投资者代码")
    SequenceSeries: int = Field(0, title="序列系列号")
    UserID: str = Field("", title="用户代码")
    SendTime: str = Field("", title="发送时间")
    SequenceNo: int = Field(0, title="序列号")
    FieldContent: str = Field("", title="消息正文")
    InvestUnitID: str = Field("", title="投资单元代码")


class WebCTPReqTradingNotice(WebCTPRequest):
    TradingNotice: TradingNoticeField = Field(title="用户事件通知")


class QryTradingNoticeField(BaseModel):
    """查询交易事件通知"""

    BrokerID: str = Field("", title="经纪公司代码")
    InvestorID: str = Field("", title="投资者代码")
    InvestUnitID: str = Field("", title="投资单元代码")


class WebCTPReqQryTradingNotice(WebCTPRequest):
    QryTradingNotice: QryTradingNoticeField = Field(title="查询交易事件通知")


class QryErrOrderField(BaseModel):
    """查询错误报单"""

    BrokerID: str = Field("", title="经纪公司代码")
    InvestorID: str = Field("", title="投资者代码")


class WebCTPReqQryErrOrder(WebCTPRequest):
    QryErrOrder: QryErrOrderField = Field(title="查询错误报单")


class ErrOrderField(BaseModel):
    """错误报单"""

    BrokerID: str = Field("", title="经纪公司代码")
    InvestorID: str = Field("", title="投资者代码")
    reserve1: str = Field("", title="保留的无效字段")
    OrderRef: str = Field("", title="报单引用")
    UserID: str = Field("", title="用户代码")
    OrderPriceType: str = Field("", title="报单价格条件")
    Direction: str = Field("", title="买卖方向")
    CombOffsetFlag: str = Field("", title="组合开平标志")
    CombHedgeFlag: str = Field("", title="组合投机套保标志")
    LimitPrice: float = Field(0.0, title="价格")
    VolumeTotalOriginal: int = Field(0, title="数量")
    TimeCondition: str = Field("", title="有效期类型")
    GTDDate: str = Field("", title="GTD日期")
    VolumeCondition: str = Field("", title="成交量类型")
    MinVolume: int = Field(0, title="最小成交量")
    ContingentCondition: str = Field("", title="触发条件")
    StopPrice: float = Field(0.0, title="止损价")
    ForceCloseReason: str = Field("", title="强平原因")
    IsAutoSuspend: int = Field(0, title="自动挂起标志")
    BusinessUnit: str = Field("", title="业务单元")
    RequestID: int = Field(0, title="请求编号")
    UserForceClose: int = Field(0, title="用户强评标志")
    ErrorID: int = Field(0, title="错误代码")
    ErrorMsg: str = Field("", title="错误信息")
    IsSwapOrder: int = Field(0, title="互换单标志")
    ExchangeID: str = Field("", title="交易所代码")
    InvestUnitID: str = Field("", title="投资单元代码")
    AccountID: str = Field("", title="资金账号")
    CurrencyID: str = Field("", title="币种代码")
    ClientID: str = Field("", title="交易编码")
    reserve2: str = Field("", title="保留的无效字段")
    MacAddress: str = Field("", title="Mac地址")
    InstrumentID: str = Field("", title="合约代码")
    IPAddress: str = Field("", title="IP地址")


class WebCTPReqErrOrder(WebCTPRequest):
    ErrOrder: ErrOrderField = Field(title="错误报单")


class ErrorConditionalOrderField(BaseModel):
    """查询错误报单操作"""

    BrokerID: str = Field("", title="经纪公司代码")
    InvestorID: str = Field("", title="投资者代码")
    reserve1: str = Field("", title="保留的无效字段")
    OrderRef: str = Field("", title="报单引用")
    UserID: str = Field("", title="用户代码")
    OrderPriceType: str = Field("", title="报单价格条件")
    Direction: str = Field("", title="买卖方向")
    CombOffsetFlag: str = Field("", title="组合开平标志")
    CombHedgeFlag: str = Field("", title="组合投机套保标志")
    LimitPrice: float = Field(0.0, title="价格")
    VolumeTotalOriginal: int = Field(0, title="数量")
    TimeCondition: str = Field("", title="有效期类型")
    GTDDate: str = Field("", title="GTD日期")
    VolumeCondition: str = Field("", title="成交量类型")
    MinVolume: int = Field(0, title="最小成交量")
    ContingentCondition: str = Field("", title="触发条件")
    StopPrice: float = Field(0.0, title="止损价")
    ForceCloseReason: str = Field("", title="强平原因")
    IsAutoSuspend: int = Field(0, title="自动挂起标志")
    BusinessUnit: str = Field("", title="业务单元")
    RequestID: int = Field(0, title="请求编号")
    OrderLocalID: str = Field("", title="本地报单编号")
    ExchangeID: str = Field("", title="交易所代码")
    ParticipantID: str = Field("", title="会员代码")
    ClientID: str = Field("", title="客户代码")
    reserve2: str = Field("", title="保留的无效字段")
    TraderID: str = Field("", title="交易所交易员代码")
    InstallID: int = Field(0, title="安装编号")
    OrderSubmitStatus: str = Field("", title="报单提交状态")
    NotifySequence: int = Field(0, title="报单提示序号")
    TradingDay: str = Field("", title="交易日")
    SettlementID: int = Field(0, title="结算编号")
    OrderSysID: str = Field("", title="报单编号")
    OrderSource: str = Field("", title="报单来源")
    OrderStatus: str = Field("", title="报单状态")
    OrderType: str = Field("", title="报单类型")
    VolumeTraded: int = Field(0, title="今成交数量")
    VolumeTotal: int = Field(0, title="剩余数量")
    InsertDate: str = Field("", title="报单日期")
    InsertTime: str = Field("", title="委托时间")
    ActiveTime: str = Field("", title="激活时间")
    SuspendTime: str = Field("", title="挂起时间")
    UpdateTime: str = Field("", title="最后修改时间")
    CancelTime: str = Field("", title="撤销时间")
    ActiveTraderID: str = Field("", title="最后修改交易所交易员代码")
    ClearingPartID: str = Field("", title="结算会员编号")
    SequenceNo: int = Field(0, title="序号")
    FrontID: int = Field(0, title="前置编号")
    SessionID: int = Field(0, title="会话编号")
    UserProductInfo: str = Field("", title="用户端产品信息")
    StatusMsg: str = Field("", title="状态信息")
    UserForceClose: int = Field(0, title="用户强评标志")
    ActiveUserID: str = Field("", title="操作用户代码")
    BrokerOrderSeq: int = Field(0, title="经纪公司报单编号")
    RelativeOrderSysID: str = Field("", title="相关报单")
    ZCETotalTradedVolume: int = Field(0, title="郑商所成交数量")
    ErrorID: int = Field(0, title="错误代码")
    ErrorMsg: str = Field("", title="错误信息")
    IsSwapOrder: int = Field(0, title="互换单标志")
    BranchID: str = Field("", title="营业部编号")
    InvestUnitID: str = Field("", title="投资单元代码")
    AccountID: str = Field("", title="资金账号")
    CurrencyID: str = Field("", title="币种代码")
    reserve3: str = Field("", title="保留的无效字段")
    MacAddress: str = Field("", title="Mac地址")
    InstrumentID: str = Field("", title="合约代码")
    ExchangeInstID: str = Field("", title="合约在交易所的代码")
    IPAddress: str = Field("", title="IP地址")


class WebCTPReqErrorConditionalOrder(WebCTPRequest):
    ErrorConditionalOrder: ErrorConditionalOrderField = Field(
        title="查询错误报单操作")


class QryErrOrderActionField(BaseModel):
    """查询错误报单操作"""

    BrokerID: str = Field("", title="经纪公司代码")
    InvestorID: str = Field("", title="投资者代码")


class WebCTPReqQryErrOrderAction(WebCTPRequest):
    QryErrOrderAction: QryErrOrderActionField = Field(title="查询错误报单操作")


class ErrOrderActionField(BaseModel):
    """错误报单操作"""

    BrokerID: str = Field("", title="经纪公司代码")
    InvestorID: str = Field("", title="投资者代码")
    OrderActionRef: int = Field(0, title="报单操作引用")
    OrderRef: str = Field("", title="报单引用")
    RequestID: int = Field(0, title="请求编号")
    FrontID: int = Field(0, title="前置编号")
    SessionID: int = Field(0, title="会话编号")
    ExchangeID: str = Field("", title="交易所代码")
    OrderSysID: str = Field("", title="报单编号")
    ActionFlag: str = Field("", title="操作标志")
    LimitPrice: float = Field(0.0, title="价格")
    VolumeChange: int = Field(0, title="数量变化")
    ActionDate: str = Field("", title="操作日期")
    ActionTime: str = Field("", title="操作时间")
    TraderID: str = Field("", title="交易所交易员代码")
    InstallID: int = Field(0, title="安装编号")
    OrderLocalID: str = Field("", title="本地报单编号")
    ActionLocalID: str = Field("", title="操作本地编号")
    ParticipantID: str = Field("", title="会员代码")
    ClientID: str = Field("", title="客户代码")
    BusinessUnit: str = Field("", title="业务单元")
    OrderActionStatus: str = Field("", title="报单操作状态")
    UserID: str = Field("", title="用户代码")
    StatusMsg: str = Field("", title="状态信息")
    reserve1: str = Field("", title="保留的无效字段")
    BranchID: str = Field("", title="营业部编号")
    InvestUnitID: str = Field("", title="投资单元代码")
    reserve2: str = Field("", title="保留的无效字段")
    MacAddress: str = Field("", title="Mac地址")
    ErrorID: int = Field(0, title="错误代码")
    ErrorMsg: str = Field("", title="错误信息")
    InstrumentID: str = Field("", title="合约代码")
    IPAddress: str = Field("", title="IP地址")


class WebCTPReqErrOrderAction(WebCTPRequest):
    ErrOrderAction: ErrOrderActionField = Field(title="错误报单操作")


class QryExchangeSequenceField(BaseModel):
    """查询交易所状态"""

    ExchangeID: str = Field("", title="交易所代码")


class WebCTPReqQryExchangeSequence(WebCTPRequest):
    QryExchangeSequence: QryExchangeSequenceField = Field(
        title="查询交易所状态")


class ExchangeSequenceField(BaseModel):
    """交易所状态"""

    ExchangeID: str = Field("", title="交易所代码")
    SequenceNo: int = Field(0, title="序号")
    MarketStatus: str = Field("", title="合约交易状态")


class WebCTPReqExchangeSequence(WebCTPRequest):
    ExchangeSequence: ExchangeSequenceField = Field(title="交易所状态")


class QueryMaxOrderVolumeWithPriceField(BaseModel):
    """根据价格查询最大报单数量"""

    BrokerID: str = Field("", title="经纪公司代码")
    InvestorID: str = Field("", title="投资者代码")
    InstrumentID: str = Field("", title="合约代码")
    Direction: str = Field("", title="买卖方向")
    OffsetFlag: str = Field("", title="开平标志")
    HedgeFlag: str = Field("", title="投机套保标志")
    MaxVolume: int = Field(0, title="最大允许报单数量")
    Price: float = Field(0.0, title="报单价格")
    ExchangeID: str = Field("", title="交易所代码")
    InvestUnitID: str = Field("", title="投资单元代码")


class WebCTPReqQueryMaxOrderVolumeWithPrice(WebCTPRequest):
    QueryMaxOrderVolumeWithPrice: QueryMaxOrderVolumeWithPriceField = Field(
        title="根据价格查询最大报单数量")


class QryBrokerTradingParamsField(BaseModel):
    """查询经纪公司交易参数"""

    BrokerID: str = Field("", title="经纪公司代码")
    InvestorID: str = Field("", title="投资者代码")
    CurrencyID: str = Field("", title="币种代码")
    AccountID: str = Field("", title="投资者帐号")


class WebCTPReqQryBrokerTradingParams(WebCTPRequest):
    QryBrokerTradingParams: QryBrokerTradingParamsField = Field(
        title="查询经纪公司交易参数")


class BrokerTradingParamsField(BaseModel):
    """经纪公司交易参数"""

    BrokerID: str = Field("", title="经纪公司代码")
    InvestorID: str = Field("", title="投资者代码")
    MarginPriceType: str = Field("", title="保证金价格类型")
    Algorithm: str = Field("", title="盈亏算法")
    AvailIncludeCloseProfit: str = Field("", title="可用是否包含平仓盈利")
    CurrencyID: str = Field("", title="币种代码")
    OptionRoyaltyPriceType: str = Field("", title="期权权利金价格类型")
    AccountID: str = Field("", title="投资者帐号")


class WebCTPReqBrokerTradingParams(WebCTPRequest):
    BrokerTradingParams: BrokerTradingParamsField = Field(
        title="经纪公司交易参数")


class QryBrokerTradingAlgosField(BaseModel):
    """查询经纪公司交易算法"""

    BrokerID: str = Field("", title="经纪公司代码")
    ExchangeID: str = Field("", title="交易所代码")
    reserve1: str = Field("", title="保留的无效字段")
    InstrumentID: str = Field("", title="合约代码")


class WebCTPReqQryBrokerTradingAlgos(WebCTPRequest):
    QryBrokerTradingAlgos: QryBrokerTradingAlgosField = Field(
        title="查询经纪公司交易算法")


class BrokerTradingAlgosField(BaseModel):
    """经纪公司交易算法"""

    BrokerID: str = Field("", title="经纪公司代码")
    ExchangeID: str = Field("", title="交易所代码")
    reserve1: str = Field("", title="保留的无效字段")
    HandlePositionAlgoID: str = Field("", title="持仓处理算法编号")
    FindMarginRateAlgoID: str = Field("", title="寻找保证金率算法编号")
    HandleTradingAccountAlgoID: str = Field("", title="资金处理算法编号")
    InstrumentID: str = Field("", title="合约代码")


class WebCTPReqBrokerTradingAlgos(WebCTPRequest):
    BrokerTradingAlgos: BrokerTradingAlgosField = Field(
        title="经纪公司交易算法")


class QueryBrokerDepositField(BaseModel):
    """查询经纪公司资金"""

    BrokerID: str = Field("", title="经纪公司代码")
    ExchangeID: str = Field("", title="交易所代码")


class WebCTPReqQueryBrokerDeposit(WebCTPRequest):
    QueryBrokerDeposit: QueryBrokerDepositField = Field(
        title="查询经纪公司资金")


class BrokerDepositField(BaseModel):
    """经纪公司资金"""

    TradingDay: str = Field("", title="交易日期")
    BrokerID: str = Field("", title="经纪公司代码")
    ParticipantID: str = Field("", title="会员代码")
    ExchangeID: str = Field("", title="交易所代码")
    PreBalance: float = Field(0.0, title="上次结算准备金")
    CurrMargin: float = Field(0.0, title="当前保证金总额")
    CloseProfit: float = Field(0.0, title="平仓盈亏")
    Balance: float = Field(0.0, title="期货结算准备金")
    Deposit: float = Field(0.0, title="入金金额")
    Withdraw: float = Field(0.0, title="出金金额")
    Available: float = Field(0.0, title="可提资金")
    Reserve: float = Field(0.0, title="基本准备金")
    FrozenMargin: float = Field(0.0, title="冻结的保证金")


class WebCTPReqBrokerDeposit(WebCTPRequest):
    BrokerDeposit: BrokerDepositField = Field(title="经纪公司资金")


class QryCFMMCBrokerKeyField(BaseModel):
    """查询保证金监管系统经纪公司密钥"""

    BrokerID: str = Field("", title="经纪公司代码")


class WebCTPReqQryCFMMCBrokerKey(WebCTPRequest):
    QryCFMMCBrokerKey: QryCFMMCBrokerKeyField = Field(
        title="查询保证金监管系统经纪公司密钥")


class CFMMCBrokerKeyField(BaseModel):
    """保证金监管系统经纪公司密钥"""

    BrokerID: str = Field("", title="经纪公司代码")
    ParticipantID: str = Field("", title="经纪公司统一编码")
    CreateDate: str = Field("", title="密钥生成日期")
    CreateTime: str = Field("", title="密钥生成时间")
    KeyID: int = Field(0, title="密钥编号")
    CurrentKey: str = Field("", title="动态密钥")
    KeyKind: str = Field("", title="动态密钥类型")


class WebCTPReqCFMMCBrokerKey(WebCTPRequest):
    CFMMCBrokerKey: CFMMCBrokerKeyField = Field(
        title="保证金监管系统经纪公司密钥")


class CFMMCTradingAccountKeyField(BaseModel):
    """保证金监管系统经纪公司资金账户密钥"""

    BrokerID: str = Field("", title="经纪公司代码")
    ParticipantID: str = Field("", title="经纪公司统一编码")
    AccountID: str = Field("", title="投资者帐号")
    KeyID: int = Field(0, title="密钥编号")
    CurrentKey: str = Field("", title="动态密钥")


class WebCTPReqCFMMCTradingAccountKey(WebCTPRequest):
    CFMMCTradingAccountKey: CFMMCTradingAccountKeyField = Field(
        title="保证金监管系统经纪公司资金账户密钥")


class QryCFMMCTradingAccountKeyField(BaseModel):
    """请求查询保证金监管系统经纪公司资金账户密钥"""

    BrokerID: str = Field("", title="经纪公司代码")
    InvestorID: str = Field("", title="投资者代码")


class WebCTPReqQryCFMMCTradingAccountKey(WebCTPRequest):
    QryCFMMCTradingAccountKey: QryCFMMCTradingAccountKeyField = Field(
        title="请求查询保证金监管系统经纪公司资金账户密钥")


class BrokerUserOTPParamField(BaseModel):
    """用户动态令牌参数"""

    BrokerID: str = Field("", title="经纪公司代码")
    UserID: str = Field("", title="用户代码")
    OTPVendorsID: str = Field("", title="动态令牌提供商")
    SerialNumber: str = Field("", title="动态令牌序列号")
    AuthKey: str = Field("", title="令牌密钥")
    LastDrift: int = Field(0, title="漂移值")
    LastSuccess: int = Field(0, title="成功值")
    OTPType: str = Field("", title="动态令牌类型")


class WebCTPReqBrokerUserOTPParam(WebCTPRequest):
    BrokerUserOTPParam: BrokerUserOTPParamField = Field(
        title="用户动态令牌参数")


class ManualSyncBrokerUserOTPField(BaseModel):
    """手工同步用户动态令牌"""

    BrokerID: str = Field("", title="经纪公司代码")
    UserID: str = Field("", title="用户代码")
    OTPType: str = Field("", title="动态令牌类型")
    FirstOTP: str = Field("", title="第一个动态密码")
    SecondOTP: str = Field("", title="第二个动态密码")


class WebCTPReqManualSyncBrokerUserOTP(WebCTPRequest):
    ManualSyncBrokerUserOTP: ManualSyncBrokerUserOTPField = Field(
        title="手工同步用户动态令牌")


class CommRateModelField(BaseModel):
    """投资者手续费率模板"""

    BrokerID: str = Field("", title="经纪公司代码")
    CommModelID: str = Field("", title="手续费率模板代码")
    CommModelName: str = Field("", title="模板名称")


class WebCTPReqCommRateModel(WebCTPRequest):
    CommRateModel: CommRateModelField = Field(title="投资者手续费率模板")


class QryCommRateModelField(BaseModel):
    """请求查询投资者手续费率模板"""

    BrokerID: str = Field("", title="经纪公司代码")
    CommModelID: str = Field("", title="手续费率模板代码")


class WebCTPReqQryCommRateModel(WebCTPRequest):
    QryCommRateModel: QryCommRateModelField = Field(
        title="请求查询投资者手续费率模板")


class MarginModelField(BaseModel):
    """投资者保证金率模板"""

    BrokerID: str = Field("", title="经纪公司代码")
    MarginModelID: str = Field("", title="保证金率模板代码")
    MarginModelName: str = Field("", title="模板名称")


class WebCTPReqMarginModel(WebCTPRequest):
    MarginModel: MarginModelField = Field(title="投资者保证金率模板")


class QryMarginModelField(BaseModel):
    """请求查询投资者保证金率模板"""

    BrokerID: str = Field("", title="经纪公司代码")
    MarginModelID: str = Field("", title="保证金率模板代码")


class WebCTPReqQryMarginModel(WebCTPRequest):
    QryMarginModel: QryMarginModelField = Field(
        title="请求查询投资者保证金率模板")


class EWarrantOffsetField(BaseModel):
    """仓单折抵信息"""

    TradingDay: str = Field("", title="交易日期")
    BrokerID: str = Field("", title="经纪公司代码")
    InvestorID: str = Field("", title="投资者代码")
    ExchangeID: str = Field("", title="交易所代码")
    reserve1: str = Field("", title="保留的无效字段")
    Direction: str = Field("", title="买卖方向")
    HedgeFlag: str = Field("", title="投机套保标志")
    Volume: int = Field(0, title="数量")
    InvestUnitID: str = Field("", title="投资单元代码")
    InstrumentID: str = Field("", title="合约代码")


class WebCTPReqEWarrantOffset(WebCTPRequest):
    EWarrantOffset: EWarrantOffsetField = Field(title="仓单折抵信息")


class QryEWarrantOffsetField(BaseModel):
    """查询仓单折抵信息"""

    BrokerID: str = Field("", title="经纪公司代码")
    InvestorID: str = Field("", title="投资者代码")
    ExchangeID: str = Field("", title="交易所代码")
    reserve1: str = Field("", title="保留的无效字段")
    InvestUnitID: str = Field("", title="投资单元代码")
    InstrumentID: str = Field("", title="合约代码")


class WebCTPReqQryEWarrantOffset(WebCTPRequest):
    QryEWarrantOffset: QryEWarrantOffsetField = Field(title="查询仓单折抵信息")


class QryInvestorProductGroupMarginField(BaseModel):
    """查询投资者品种/跨品种保证金"""

    BrokerID: str = Field("", title="经纪公司代码")
    InvestorID: str = Field("", title="投资者代码")
    reserve1: str = Field("", title="保留的无效字段")
    HedgeFlag: str = Field("", title="投机套保标志")
    ExchangeID: str = Field("", title="交易所代码")
    InvestUnitID: str = Field("", title="投资单元代码")
    ProductGroupID: str = Field("", title="品种/跨品种标示")


class WebCTPReqQryInvestorProductGroupMargin(WebCTPRequest):
    QryInvestorProductGroupMargin: QryInvestorProductGroupMarginField = Field(
        title="查询投资者品种/跨品种保证金")


class InvestorProductGroupMarginField(BaseModel):
    """投资者品种/跨品种保证金"""

    reserve1: str = Field("", title="保留的无效字段")
    BrokerID: str = Field("", title="经纪公司代码")
    InvestorID: str = Field("", title="投资者代码")
    TradingDay: str = Field("", title="交易日")
    SettlementID: int = Field(0, title="结算编号")
    FrozenMargin: float = Field(0.0, title="冻结的保证金")
    LongFrozenMargin: float = Field(0.0, title="多头冻结的保证金")
    ShortFrozenMargin: float = Field(0.0, title="空头冻结的保证金")
    UseMargin: float = Field(0.0, title="占用的保证金")
    LongUseMargin: float = Field(0.0, title="多头保证金")
    ShortUseMargin: float = Field(0.0, title="空头保证金")
    ExchMargin: float = Field(0.0, title="交易所保证金")
    LongExchMargin: float = Field(0.0, title="交易所多头保证金")
    ShortExchMargin: float = Field(0.0, title="交易所空头保证金")
    CloseProfit: float = Field(0.0, title="平仓盈亏")
    FrozenCommission: float = Field(0.0, title="冻结的手续费")
    Commission: float = Field(0.0, title="手续费")
    FrozenCash: float = Field(0.0, title="冻结的资金")
    CashIn: float = Field(0.0, title="资金差额")
    PositionProfit: float = Field(0.0, title="持仓盈亏")
    OffsetAmount: float = Field(0.0, title="折抵总金额")
    LongOffsetAmount: float = Field(0.0, title="多头折抵总金额")
    ShortOffsetAmount: float = Field(0.0, title="空头折抵总金额")
    ExchOffsetAmount: float = Field(0.0, title="交易所折抵总金额")
    LongExchOffsetAmount: float = Field(0.0, title="交易所多头折抵总金额")
    ShortExchOffsetAmount: float = Field(0.0, title="交易所空头折抵总金额")
    HedgeFlag: str = Field("", title="投机套保标志")
    ExchangeID: str = Field("", title="交易所代码")
    InvestUnitID: str = Field("", title="投资单元代码")
    ProductGroupID: str = Field("", title="品种/跨品种标示")


class WebCTPReqInvestorProductGroupMargin(WebCTPRequest):
    InvestorProductGroupMargin: InvestorProductGroupMarginField = Field(
        title="投资者品种/跨品种保证金")


class QueryCFMMCTradingAccountTokenField(BaseModel):
    """查询监控中心用户令牌"""

    BrokerID: str = Field("", title="经纪公司代码")
    InvestorID: str = Field("", title="投资者代码")
    InvestUnitID: str = Field("", title="投资单元代码")


class WebCTPReqQueryCFMMCTradingAccountToken(WebCTPRequest):
    QueryCFMMCTradingAccountToken: QueryCFMMCTradingAccountTokenField = Field(
        title="查询监控中心用户令牌")


class CFMMCTradingAccountTokenField(BaseModel):
    """监控中心用户令牌"""

    BrokerID: str = Field("", title="经纪公司代码")
    ParticipantID: str = Field("", title="经纪公司统一编码")
    AccountID: str = Field("", title="投资者帐号")
    KeyID: int = Field(0, title="密钥编号")
    Token: str = Field("", title="动态令牌")


class WebCTPReqCFMMCTradingAccountToken(WebCTPRequest):
    CFMMCTradingAccountToken: CFMMCTradingAccountTokenField = Field(
        title="监控中心用户令牌")


class QryProductGroupField(BaseModel):
    """查询产品组"""

    reserve1: str = Field("", title="保留的无效字段")
    ExchangeID: str = Field("", title="交易所代码")
    ProductID: str = Field("", title="产品代码")


class WebCTPReqQryProductGroup(WebCTPRequest):
    QryProductGroup: QryProductGroupField = Field(title="查询产品组")


class ProductGroupField(BaseModel):
    """投资者品种/跨品种保证金产品组"""

    reserve1: str = Field("", title="保留的无效字段")
    ExchangeID: str = Field("", title="交易所代码")
    reserve2: str = Field("", title="保留的无效字段")
    ProductID: str = Field("", title="产品代码")
    ProductGroupID: str = Field("", title="产品组代码")


class WebCTPReqProductGroup(WebCTPRequest):
    ProductGroup: ProductGroupField = Field(
        title="投资者品种/跨品种保证金产品组")


class BulletinField(BaseModel):
    """交易所公告"""

    ExchangeID: str = Field("", title="交易所代码")
    TradingDay: str = Field("", title="交易日")
    BulletinID: int = Field(0, title="公告编号")
    SequenceNo: int = Field(0, title="序列号")
    NewsType: str = Field("", title="公告类型")
    NewsUrgency: str = Field("", title="紧急程度")
    SendTime: str = Field("", title="发送时间")
    Abstract: str = Field("", title="消息摘要")
    ComeFrom: str = Field("", title="消息来源")
    Content: str = Field("", title="消息正文")
    URLLink: str = Field("", title="WEB地址")
    MarketID: str = Field("", title="市场代码")


class WebCTPReqBulletin(WebCTPRequest):
    Bulletin: BulletinField = Field(title="交易所公告")


class QryBulletinField(BaseModel):
    """查询交易所公告"""

    ExchangeID: str = Field("", title="交易所代码")
    BulletinID: int = Field(0, title="公告编号")
    SequenceNo: int = Field(0, title="序列号")
    NewsType: str = Field("", title="公告类型")
    NewsUrgency: str = Field("", title="紧急程度")


class WebCTPReqQryBulletin(WebCTPRequest):
    QryBulletin: QryBulletinField = Field(title="查询交易所公告")


class ReqOpenAccountField(BaseModel):
    """转帐开户请求"""

    TradeCode: str = Field("", title="业务功能码")
    BankID: str = Field("", title="银行代码")
    BankBranchID: str = Field("", title="银行分支机构代码")
    BrokerID: str = Field("", title="期商代码")
    BrokerBranchID: str = Field("", title="期商分支机构代码")
    TradeDate: str = Field("", title="交易日期")
    TradeTime: str = Field("", title="交易时间")
    BankSerial: str = Field("", title="银行流水号")
    TradingDay: str = Field("", title="交易系统日期 ")
    PlateSerial: int = Field(0, title="银期平台消息流水号")
    LastFragment: str = Field("", title="最后分片标志")
    SessionID: int = Field(0, title="会话号")
    CustomerName: str = Field("", title="客户姓名")
    IdCardType: str = Field("", title="证件类型")
    IdentifiedCardNo: str = Field("", title="证件号码")
    Gender: str = Field("", title="性别")
    CountryCode: str = Field("", title="国家代码")
    CustType: str = Field("", title="客户类型")
    Address: str = Field("", title="地址")
    ZipCode: str = Field("", title="邮编")
    Telephone: str = Field("", title="电话号码")
    MobilePhone: str = Field("", title="手机")
    Fax: str = Field("", title="传真")
    EMail: str = Field("", title="电子邮件")
    MoneyAccountStatus: str = Field("", title="资金账户状态")
    BankAccount: str = Field("", title="银行帐号")
    BankPassWord: str = Field("", title="银行密码")
    AccountID: str = Field("", title="投资者帐号")
    Password: str = Field("", title="期货密码")
    InstallID: int = Field(0, title="安装编号")
    VerifyCertNoFlag: str = Field("", title="验证客户证件号码标志")
    CurrencyID: str = Field("", title="币种代码")
    CashExchangeCode: str = Field("", title="汇钞标志")
    Digest: str = Field("", title="摘要")
    BankAccType: str = Field("", title="银行帐号类型")
    DeviceID: str = Field("", title="渠道标志")
    BankSecuAccType: str = Field("", title="期货单位帐号类型")
    BrokerIDByBank: str = Field("", title="期货公司银行编码")
    BankSecuAcc: str = Field("", title="期货单位帐号")
    BankPwdFlag: str = Field("", title="银行密码标志")
    SecuPwdFlag: str = Field("", title="期货资金密码核对标志")
    OperNo: str = Field("", title="交易柜员")
    TID: int = Field(0, title="交易ID")
    UserID: str = Field("", title="用户标识")
    LongCustomerName: str = Field("", title="长客户姓名")


class WebCTPReqOpenAccount(WebCTPRequest):
    ReqOpenAccount: ReqOpenAccountField = Field(title="转帐开户请求")


class ReqCancelAccountField(BaseModel):
    """转帐销户请求"""

    TradeCode: str = Field("", title="业务功能码")
    BankID: str = Field("", title="银行代码")
    BankBranchID: str = Field("", title="银行分支机构代码")
    BrokerID: str = Field("", title="期商代码")
    BrokerBranchID: str = Field("", title="期商分支机构代码")
    TradeDate: str = Field("", title="交易日期")
    TradeTime: str = Field("", title="交易时间")
    BankSerial: str = Field("", title="银行流水号")
    TradingDay: str = Field("", title="交易系统日期 ")
    PlateSerial: int = Field(0, title="银期平台消息流水号")
    LastFragment: str = Field("", title="最后分片标志")
    SessionID: int = Field(0, title="会话号")
    CustomerName: str = Field("", title="客户姓名")
    IdCardType: str = Field("", title="证件类型")
    IdentifiedCardNo: str = Field("", title="证件号码")
    Gender: str = Field("", title="性别")
    CountryCode: str = Field("", title="国家代码")
    CustType: str = Field("", title="客户类型")
    Address: str = Field("", title="地址")
    ZipCode: str = Field("", title="邮编")
    Telephone: str = Field("", title="电话号码")
    MobilePhone: str = Field("", title="手机")
    Fax: str = Field("", title="传真")
    EMail: str = Field("", title="电子邮件")
    MoneyAccountStatus: str = Field("", title="资金账户状态")
    BankAccount: str = Field("", title="银行帐号")
    BankPassWord: str = Field("", title="银行密码")
    AccountID: str = Field("", title="投资者帐号")
    Password: str = Field("", title="期货密码")
    InstallID: int = Field(0, title="安装编号")
    VerifyCertNoFlag: str = Field("", title="验证客户证件号码标志")
    CurrencyID: str = Field("", title="币种代码")
    CashExchangeCode: str = Field("", title="汇钞标志")
    Digest: str = Field("", title="摘要")
    BankAccType: str = Field("", title="银行帐号类型")
    DeviceID: str = Field("", title="渠道标志")
    BankSecuAccType: str = Field("", title="期货单位帐号类型")
    BrokerIDByBank: str = Field("", title="期货公司银行编码")
    BankSecuAcc: str = Field("", title="期货单位帐号")
    BankPwdFlag: str = Field("", title="银行密码标志")
    SecuPwdFlag: str = Field("", title="期货资金密码核对标志")
    OperNo: str = Field("", title="交易柜员")
    TID: int = Field(0, title="交易ID")
    UserID: str = Field("", title="用户标识")
    LongCustomerName: str = Field("", title="长客户姓名")


class WebCTPReqCancelAccount(WebCTPRequest):
    ReqCancelAccount: ReqCancelAccountField = Field(title="转帐销户请求")


class ReqChangeAccountField(BaseModel):
    """变更银行账户请求"""

    TradeCode: str = Field("", title="业务功能码")
    BankID: str = Field("", title="银行代码")
    BankBranchID: str = Field("", title="银行分支机构代码")
    BrokerID: str = Field("", title="期商代码")
    BrokerBranchID: str = Field("", title="期商分支机构代码")
    TradeDate: str = Field("", title="交易日期")
    TradeTime: str = Field("", title="交易时间")
    BankSerial: str = Field("", title="银行流水号")
    TradingDay: str = Field("", title="交易系统日期 ")
    PlateSerial: int = Field(0, title="银期平台消息流水号")
    LastFragment: str = Field("", title="最后分片标志")
    SessionID: int = Field(0, title="会话号")
    CustomerName: str = Field("", title="客户姓名")
    IdCardType: str = Field("", title="证件类型")
    IdentifiedCardNo: str = Field("", title="证件号码")
    Gender: str = Field("", title="性别")
    CountryCode: str = Field("", title="国家代码")
    CustType: str = Field("", title="客户类型")
    Address: str = Field("", title="地址")
    ZipCode: str = Field("", title="邮编")
    Telephone: str = Field("", title="电话号码")
    MobilePhone: str = Field("", title="手机")
    Fax: str = Field("", title="传真")
    EMail: str = Field("", title="电子邮件")
    MoneyAccountStatus: str = Field("", title="资金账户状态")
    BankAccount: str = Field("", title="银行帐号")
    BankPassWord: str = Field("", title="银行密码")
    NewBankAccount: str = Field("", title="新银行帐号")
    NewBankPassWord: str = Field("", title="新银行密码")
    AccountID: str = Field("", title="投资者帐号")
    Password: str = Field("", title="期货密码")
    BankAccType: str = Field("", title="银行帐号类型")
    InstallID: int = Field(0, title="安装编号")
    VerifyCertNoFlag: str = Field("", title="验证客户证件号码标志")
    CurrencyID: str = Field("", title="币种代码")
    BrokerIDByBank: str = Field("", title="期货公司银行编码")
    BankPwdFlag: str = Field("", title="银行密码标志")
    SecuPwdFlag: str = Field("", title="期货资金密码核对标志")
    TID: int = Field(0, title="交易ID")
    Digest: str = Field("", title="摘要")
    LongCustomerName: str = Field("", title="长客户姓名")


class WebCTPReqChangeAccount(WebCTPRequest):
    ReqChangeAccount: ReqChangeAccountField = Field(title="变更银行账户请求")


class ReqTransferField(BaseModel):
    """转账请求"""

    TradeCode: str = Field("", title="业务功能码")
    BankID: str = Field("", title="银行代码")
    BankBranchID: str = Field("", title="银行分支机构代码")
    BrokerID: str = Field("", title="期商代码")
    BrokerBranchID: str = Field("", title="期商分支机构代码")
    TradeDate: str = Field("", title="交易日期")
    TradeTime: str = Field("", title="交易时间")
    BankSerial: str = Field("", title="银行流水号")
    TradingDay: str = Field("", title="交易系统日期 ")
    PlateSerial: int = Field(0, title="银期平台消息流水号")
    LastFragment: str = Field("", title="最后分片标志")
    SessionID: int = Field(0, title="会话号")
    CustomerName: str = Field("", title="客户姓名")
    IdCardType: str = Field("", title="证件类型")
    IdentifiedCardNo: str = Field("", title="证件号码")
    CustType: str = Field("", title="客户类型")
    BankAccount: str = Field("", title="银行帐号")
    BankPassWord: str = Field("", title="银行密码")
    AccountID: str = Field("", title="投资者帐号")
    Password: str = Field("", title="期货密码")
    InstallID: int = Field(0, title="安装编号")
    FutureSerial: int = Field(0, title="期货公司流水号")
    UserID: str = Field("", title="用户标识")
    VerifyCertNoFlag: str = Field("", title="验证客户证件号码标志")
    CurrencyID: str = Field("", title="币种代码")
    TradeAmount: float = Field(0.0, title="转帐金额")
    FutureFetchAmount: float = Field(0.0, title="期货可取金额")
    FeePayFlag: str = Field("", title="费用支付标志")
    CustFee: float = Field(0.0, title="应收客户费用")
    BrokerFee: float = Field(0.0, title="应收期货公司费用")
    Message: str = Field("", title="发送方给接收方的消息")
    Digest: str = Field("", title="摘要")
    BankAccType: str = Field("", title="银行帐号类型")
    DeviceID: str = Field("", title="渠道标志")
    BankSecuAccType: str = Field("", title="期货单位帐号类型")
    BrokerIDByBank: str = Field("", title="期货公司银行编码")
    BankSecuAcc: str = Field("", title="期货单位帐号")
    BankPwdFlag: str = Field("", title="银行密码标志")
    SecuPwdFlag: str = Field("", title="期货资金密码核对标志")
    OperNo: str = Field("", title="交易柜员")
    RequestID: int = Field(0, title="请求编号")
    TID: int = Field(0, title="交易ID")
    TransferStatus: str = Field("", title="转账交易状态")
    LongCustomerName: str = Field("", title="长客户姓名")


class WebCTPReqTransfer(WebCTPRequest):
    ReqTransfer: ReqTransferField = Field(title="转账请求")


class ReqRepealField(BaseModel):
    """冲正请求"""

    RepealTimeInterval: int = Field(0, title="冲正时间间隔")
    RepealedTimes: int = Field(0, title="已经冲正次数")
    BankRepealFlag: str = Field("", title="银行冲正标志")
    BrokerRepealFlag: str = Field("", title="期商冲正标志")
    PlateRepealSerial: int = Field(0, title="被冲正平台流水号")
    BankRepealSerial: str = Field("", title="被冲正银行流水号")
    FutureRepealSerial: int = Field(0, title="被冲正期货流水号")
    TradeCode: str = Field("", title="业务功能码")
    BankID: str = Field("", title="银行代码")
    BankBranchID: str = Field("", title="银行分支机构代码")
    BrokerID: str = Field("", title="期商代码")
    BrokerBranchID: str = Field("", title="期商分支机构代码")
    TradeDate: str = Field("", title="交易日期")
    TradeTime: str = Field("", title="交易时间")
    BankSerial: str = Field("", title="银行流水号")
    TradingDay: str = Field("", title="交易系统日期 ")
    PlateSerial: int = Field(0, title="银期平台消息流水号")
    LastFragment: str = Field("", title="最后分片标志")
    SessionID: int = Field(0, title="会话号")
    CustomerName: str = Field("", title="客户姓名")
    IdCardType: str = Field("", title="证件类型")
    IdentifiedCardNo: str = Field("", title="证件号码")
    CustType: str = Field("", title="客户类型")
    BankAccount: str = Field("", title="银行帐号")
    BankPassWord: str = Field("", title="银行密码")
    AccountID: str = Field("", title="投资者帐号")
    Password: str = Field("", title="期货密码")
    InstallID: int = Field(0, title="安装编号")
    FutureSerial: int = Field(0, title="期货公司流水号")
    UserID: str = Field("", title="用户标识")
    VerifyCertNoFlag: str = Field("", title="验证客户证件号码标志")
    CurrencyID: str = Field("", title="币种代码")
    TradeAmount: float = Field(0.0, title="转帐金额")
    FutureFetchAmount: float = Field(0.0, title="期货可取金额")
    FeePayFlag: str = Field("", title="费用支付标志")
    CustFee: float = Field(0.0, title="应收客户费用")
    BrokerFee: float = Field(0.0, title="应收期货公司费用")
    Message: str = Field("", title="发送方给接收方的消息")
    Digest: str = Field("", title="摘要")
    BankAccType: str = Field("", title="银行帐号类型")
    DeviceID: str = Field("", title="渠道标志")
    BankSecuAccType: str = Field("", title="期货单位帐号类型")
    BrokerIDByBank: str = Field("", title="期货公司银行编码")
    BankSecuAcc: str = Field("", title="期货单位帐号")
    BankPwdFlag: str = Field("", title="银行密码标志")
    SecuPwdFlag: str = Field("", title="期货资金密码核对标志")
    OperNo: str = Field("", title="交易柜员")
    RequestID: int = Field(0, title="请求编号")
    TID: int = Field(0, title="交易ID")
    TransferStatus: str = Field("", title="转账交易状态")
    LongCustomerName: str = Field("", title="长客户姓名")


class WebCTPReqRepeal(WebCTPRequest):
    ReqRepeal: ReqRepealField = Field(title="冲正请求")


class ReqQueryAccountField(BaseModel):
    """查询账户信息请求"""

    TradeCode: str = Field("", title="业务功能码")
    BankID: str = Field("", title="银行代码")
    BankBranchID: str = Field("", title="银行分支机构代码")
    BrokerID: str = Field("", title="期商代码")
    BrokerBranchID: str = Field("", title="期商分支机构代码")
    TradeDate: str = Field("", title="交易日期")
    TradeTime: str = Field("", title="交易时间")
    BankSerial: str = Field("", title="银行流水号")
    TradingDay: str = Field("", title="交易系统日期 ")
    PlateSerial: int = Field(0, title="银期平台消息流水号")
    LastFragment: str = Field("", title="最后分片标志")
    SessionID: int = Field(0, title="会话号")
    CustomerName: str = Field("", title="客户姓名")
    IdCardType: str = Field("", title="证件类型")
    IdentifiedCardNo: str = Field("", title="证件号码")
    CustType: str = Field("", title="客户类型")
    BankAccount: str = Field("", title="银行帐号")
    BankPassWord: str = Field("", title="银行密码")
    AccountID: str = Field("", title="投资者帐号")
    Password: str = Field("", title="期货密码")
    FutureSerial: int = Field(0, title="期货公司流水号")
    InstallID: int = Field(0, title="安装编号")
    UserID: str = Field("", title="用户标识")
    VerifyCertNoFlag: str = Field("", title="验证客户证件号码标志")
    CurrencyID: str = Field("", title="币种代码")
    Digest: str = Field("", title="摘要")
    BankAccType: str = Field("", title="银行帐号类型")
    DeviceID: str = Field("", title="渠道标志")
    BankSecuAccType: str = Field("", title="期货单位帐号类型")
    BrokerIDByBank: str = Field("", title="期货公司银行编码")
    BankSecuAcc: str = Field("", title="期货单位帐号")
    BankPwdFlag: str = Field("", title="银行密码标志")
    SecuPwdFlag: str = Field("", title="期货资金密码核对标志")
    OperNo: str = Field("", title="交易柜员")
    RequestID: int = Field(0, title="请求编号")
    TID: int = Field(0, title="交易ID")
    LongCustomerName: str = Field("", title="长客户姓名")


class WebCTPReqQueryAccount(WebCTPRequest):
    ReqQueryAccount: ReqQueryAccountField = Field(title="查询账户信息请求")


class FutureSignIOField(BaseModel):
    """期商签到签退"""

    TradeCode: str = Field("", title="业务功能码")
    BankID: str = Field("", title="银行代码")
    BankBranchID: str = Field("", title="银行分支机构代码")
    BrokerID: str = Field("", title="期商代码")
    BrokerBranchID: str = Field("", title="期商分支机构代码")
    TradeDate: str = Field("", title="交易日期")
    TradeTime: str = Field("", title="交易时间")
    BankSerial: str = Field("", title="银行流水号")
    TradingDay: str = Field("", title="交易系统日期 ")
    PlateSerial: int = Field(0, title="银期平台消息流水号")
    LastFragment: str = Field("", title="最后分片标志")
    SessionID: int = Field(0, title="会话号")
    InstallID: int = Field(0, title="安装编号")
    UserID: str = Field("", title="用户标识")
    Digest: str = Field("", title="摘要")
    CurrencyID: str = Field("", title="币种代码")
    DeviceID: str = Field("", title="渠道标志")
    BrokerIDByBank: str = Field("", title="期货公司银行编码")
    OperNo: str = Field("", title="交易柜员")
    RequestID: int = Field(0, title="请求编号")
    TID: int = Field(0, title="交易ID")


class WebCTPReqFutureSignIO(WebCTPRequest):
    FutureSignIO: FutureSignIOField = Field(title="期商签到签退")


class ReqFutureSignOutField(BaseModel):
    """期商签退请求"""

    TradeCode: str = Field("", title="业务功能码")
    BankID: str = Field("", title="银行代码")
    BankBranchID: str = Field("", title="银行分支机构代码")
    BrokerID: str = Field("", title="期商代码")
    BrokerBranchID: str = Field("", title="期商分支机构代码")
    TradeDate: str = Field("", title="交易日期")
    TradeTime: str = Field("", title="交易时间")
    BankSerial: str = Field("", title="银行流水号")
    TradingDay: str = Field("", title="交易系统日期 ")
    PlateSerial: int = Field(0, title="银期平台消息流水号")
    LastFragment: str = Field("", title="最后分片标志")
    SessionID: int = Field(0, title="会话号")
    InstallID: int = Field(0, title="安装编号")
    UserID: str = Field("", title="用户标识")
    Digest: str = Field("", title="摘要")
    CurrencyID: str = Field("", title="币种代码")
    DeviceID: str = Field("", title="渠道标志")
    BrokerIDByBank: str = Field("", title="期货公司银行编码")
    OperNo: str = Field("", title="交易柜员")
    RequestID: int = Field(0, title="请求编号")
    TID: int = Field(0, title="交易ID")


class WebCTPReqFutureSignOut(WebCTPRequest):
    ReqFutureSignOut: ReqFutureSignOutField = Field(title="期商签退请求")


class ReqQueryTradeResultBySerialField(BaseModel):
    """查询指定流水号的交易结果请求"""

    TradeCode: str = Field("", title="业务功能码")
    BankID: str = Field("", title="银行代码")
    BankBranchID: str = Field("", title="银行分支机构代码")
    BrokerID: str = Field("", title="期商代码")
    BrokerBranchID: str = Field("", title="期商分支机构代码")
    TradeDate: str = Field("", title="交易日期")
    TradeTime: str = Field("", title="交易时间")
    BankSerial: str = Field("", title="银行流水号")
    TradingDay: str = Field("", title="交易系统日期 ")
    PlateSerial: int = Field(0, title="银期平台消息流水号")
    LastFragment: str = Field("", title="最后分片标志")
    SessionID: int = Field(0, title="会话号")
    Reference: int = Field(0, title="流水号")
    RefrenceIssureType: str = Field("", title="本流水号发布者的机构类型")
    RefrenceIssure: str = Field("", title="本流水号发布者机构编码")
    CustomerName: str = Field("", title="客户姓名")
    IdCardType: str = Field("", title="证件类型")
    IdentifiedCardNo: str = Field("", title="证件号码")
    CustType: str = Field("", title="客户类型")
    BankAccount: str = Field("", title="银行帐号")
    BankPassWord: str = Field("", title="银行密码")
    AccountID: str = Field("", title="投资者帐号")
    Password: str = Field("", title="期货密码")
    CurrencyID: str = Field("", title="币种代码")
    TradeAmount: float = Field(0.0, title="转帐金额")
    Digest: str = Field("", title="摘要")
    LongCustomerName: str = Field("", title="长客户姓名")


class WebCTPReqQueryTradeResultBySerial(WebCTPRequest):
    ReqQueryTradeResultBySerial: ReqQueryTradeResultBySerialField = Field(
        title="查询指定流水号的交易结果请求")


class ReqDayEndFileReadyField(BaseModel):
    """日终文件就绪请求"""

    TradeCode: str = Field("", title="业务功能码")
    BankID: str = Field("", title="银行代码")
    BankBranchID: str = Field("", title="银行分支机构代码")
    BrokerID: str = Field("", title="期商代码")
    BrokerBranchID: str = Field("", title="期商分支机构代码")
    TradeDate: str = Field("", title="交易日期")
    TradeTime: str = Field("", title="交易时间")
    BankSerial: str = Field("", title="银行流水号")
    TradingDay: str = Field("", title="交易系统日期 ")
    PlateSerial: int = Field(0, title="银期平台消息流水号")
    LastFragment: str = Field("", title="最后分片标志")
    SessionID: int = Field(0, title="会话号")
    FileBusinessCode: str = Field("", title="文件业务功能")
    Digest: str = Field("", title="摘要")


class WebCTPReqDayEndFileReady(WebCTPRequest):
    ReqDayEndFileReady: ReqDayEndFileReadyField = Field(
        title="日终文件就绪请求")


class ReturnResultField(BaseModel):
    """返回结果"""

    ReturnCode: str = Field("", title="返回代码")
    DescrInfoForReturnCode: str = Field("", title="返回码描述")


class WebCTPReqReturnResult(WebCTPRequest):
    ReturnResult: ReturnResultField = Field(title="返回结果")


class VerifyFuturePasswordField(BaseModel):
    """验证期货资金密码"""

    TradeCode: str = Field("", title="业务功能码")
    BankID: str = Field("", title="银行代码")
    BankBranchID: str = Field("", title="银行分支机构代码")
    BrokerID: str = Field("", title="期商代码")
    BrokerBranchID: str = Field("", title="期商分支机构代码")
    TradeDate: str = Field("", title="交易日期")
    TradeTime: str = Field("", title="交易时间")
    BankSerial: str = Field("", title="银行流水号")
    TradingDay: str = Field("", title="交易系统日期 ")
    PlateSerial: int = Field(0, title="银期平台消息流水号")
    LastFragment: str = Field("", title="最后分片标志")
    SessionID: int = Field(0, title="会话号")
    AccountID: str = Field("", title="投资者帐号")
    Password: str = Field("", title="期货密码")
    BankAccount: str = Field("", title="银行帐号")
    BankPassWord: str = Field("", title="银行密码")
    InstallID: int = Field(0, title="安装编号")
    TID: int = Field(0, title="交易ID")
    CurrencyID: str = Field("", title="币种代码")


class WebCTPReqVerifyFuturePassword(WebCTPRequest):
    VerifyFuturePassword: VerifyFuturePasswordField = Field(
        title="验证期货资金密码")


class VerifyCustInfoField(BaseModel):
    """验证客户信息"""

    CustomerName: str = Field("", title="客户姓名")
    IdCardType: str = Field("", title="证件类型")
    IdentifiedCardNo: str = Field("", title="证件号码")
    CustType: str = Field("", title="客户类型")
    LongCustomerName: str = Field("", title="长客户姓名")


class WebCTPReqVerifyCustInfo(WebCTPRequest):
    VerifyCustInfo: VerifyCustInfoField = Field(title="验证客户信息")


class VerifyFuturePasswordAndCustInfoField(BaseModel):
    """验证期货资金密码和客户信息"""

    CustomerName: str = Field("", title="客户姓名")
    IdCardType: str = Field("", title="证件类型")
    IdentifiedCardNo: str = Field("", title="证件号码")
    CustType: str = Field("", title="客户类型")
    AccountID: str = Field("", title="投资者帐号")
    Password: str = Field("", title="期货密码")
    CurrencyID: str = Field("", title="币种代码")
    LongCustomerName: str = Field("", title="长客户姓名")


class WebCTPReqVerifyFuturePasswordAndCustInfo(WebCTPRequest):
    VerifyFuturePasswordAndCustInfo: VerifyFuturePasswordAndCustInfoField = Field(
        title="验证期货资金密码和客户信息")


class DepositResultInformField(BaseModel):
    """验证期货资金密码和客户信息"""

    DepositSeqNo: str = Field("",
                              title="出入金流水号，该流水号为银期报盘返回的流水号")
    BrokerID: str = Field("", title="经纪公司代码")
    InvestorID: str = Field("", title="投资者代码")
    Deposit: float = Field(0.0, title="入金金额")
    RequestID: int = Field(0, title="请求编号")
    ReturnCode: str = Field("", title="返回代码")
    DescrInfoForReturnCode: str = Field("", title="返回码描述")


class WebCTPReqDepositResultInform(WebCTPRequest):
    DepositResultInform: DepositResultInformField = Field(
        title="验证期货资金密码和客户信息")


class ReqSyncKeyField(BaseModel):
    """交易核心向银期报盘发出密钥同步请求"""

    TradeCode: str = Field("", title="业务功能码")
    BankID: str = Field("", title="银行代码")
    BankBranchID: str = Field("", title="银行分支机构代码")
    BrokerID: str = Field("", title="期商代码")
    BrokerBranchID: str = Field("", title="期商分支机构代码")
    TradeDate: str = Field("", title="交易日期")
    TradeTime: str = Field("", title="交易时间")
    BankSerial: str = Field("", title="银行流水号")
    TradingDay: str = Field("", title="交易系统日期 ")
    PlateSerial: int = Field(0, title="银期平台消息流水号")
    LastFragment: str = Field("", title="最后分片标志")
    SessionID: int = Field(0, title="会话号")
    InstallID: int = Field(0, title="安装编号")
    UserID: str = Field("", title="用户标识")
    Message: str = Field("", title="交易核心给银期报盘的消息")
    DeviceID: str = Field("", title="渠道标志")
    BrokerIDByBank: str = Field("", title="期货公司银行编码")
    OperNo: str = Field("", title="交易柜员")
    RequestID: int = Field(0, title="请求编号")
    TID: int = Field(0, title="交易ID")


class WebCTPReqSyncKey(WebCTPRequest):
    ReqSyncKey: ReqSyncKeyField = Field(
        title="交易核心向银期报盘发出密钥同步请求")


class NotifyQueryAccountField(BaseModel):
    """查询账户信息通知"""

    TradeCode: str = Field("", title="业务功能码")
    BankID: str = Field("", title="银行代码")
    BankBranchID: str = Field("", title="银行分支机构代码")
    BrokerID: str = Field("", title="期商代码")
    BrokerBranchID: str = Field("", title="期商分支机构代码")
    TradeDate: str = Field("", title="交易日期")
    TradeTime: str = Field("", title="交易时间")
    BankSerial: str = Field("", title="银行流水号")
    TradingDay: str = Field("", title="交易系统日期 ")
    PlateSerial: int = Field(0, title="银期平台消息流水号")
    LastFragment: str = Field("", title="最后分片标志")
    SessionID: int = Field(0, title="会话号")
    CustomerName: str = Field("", title="客户姓名")
    IdCardType: str = Field("", title="证件类型")
    IdentifiedCardNo: str = Field("", title="证件号码")
    CustType: str = Field("", title="客户类型")
    BankAccount: str = Field("", title="银行帐号")
    BankPassWord: str = Field("", title="银行密码")
    AccountID: str = Field("", title="投资者帐号")
    Password: str = Field("", title="期货密码")
    FutureSerial: int = Field(0, title="期货公司流水号")
    InstallID: int = Field(0, title="安装编号")
    UserID: str = Field("", title="用户标识")
    VerifyCertNoFlag: str = Field("", title="验证客户证件号码标志")
    CurrencyID: str = Field("", title="币种代码")
    Digest: str = Field("", title="摘要")
    BankAccType: str = Field("", title="银行帐号类型")
    DeviceID: str = Field("", title="渠道标志")
    BankSecuAccType: str = Field("", title="期货单位帐号类型")
    BrokerIDByBank: str = Field("", title="期货公司银行编码")
    BankSecuAcc: str = Field("", title="期货单位帐号")
    BankPwdFlag: str = Field("", title="银行密码标志")
    SecuPwdFlag: str = Field("", title="期货资金密码核对标志")
    OperNo: str = Field("", title="交易柜员")
    RequestID: int = Field(0, title="请求编号")
    TID: int = Field(0, title="交易ID")
    BankUseAmount: float = Field(0.0, title="银行可用金额")
    BankFetchAmount: float = Field(0.0, title="银行可取金额")
    ErrorID: int = Field(0, title="错误代码")
    ErrorMsg: str = Field("", title="错误信息")
    LongCustomerName: str = Field("", title="长客户姓名")


class WebCTPReqNotifyQueryAccount(WebCTPRequest):
    NotifyQueryAccount: NotifyQueryAccountField = Field(
        title="查询账户信息通知")


class TransferSerialField(BaseModel):
    """银期转账交易流水表"""

    PlateSerial: int = Field(0, title="平台流水号")
    TradeDate: str = Field("", title="交易发起方日期")
    TradingDay: str = Field("", title="交易日期")
    TradeTime: str = Field("", title="交易时间")
    TradeCode: str = Field("", title="交易代码")
    SessionID: int = Field(0, title="会话编号")
    BankID: str = Field("", title="银行编码")
    BankBranchID: str = Field("", title="银行分支机构编码")
    BankAccType: str = Field("", title="银行帐号类型")
    BankAccount: str = Field("", title="银行帐号")
    BankSerial: str = Field("", title="银行流水号")
    BrokerID: str = Field("", title="期货公司编码")
    BrokerBranchID: str = Field("", title="期商分支机构代码")
    FutureAccType: str = Field("", title="期货公司帐号类型")
    AccountID: str = Field("", title="投资者帐号")
    InvestorID: str = Field("", title="投资者代码")
    FutureSerial: int = Field(0, title="期货公司流水号")
    IdCardType: str = Field("", title="证件类型")
    IdentifiedCardNo: str = Field("", title="证件号码")
    CurrencyID: str = Field("", title="币种代码")
    TradeAmount: float = Field(0.0, title="交易金额")
    CustFee: float = Field(0.0, title="应收客户费用")
    BrokerFee: float = Field(0.0, title="应收期货公司费用")
    AvailabilityFlag: str = Field("", title="有效标志")
    OperatorCode: str = Field("", title="操作员")
    BankNewAccount: str = Field("", title="新银行帐号")
    ErrorID: int = Field(0, title="错误代码")
    ErrorMsg: str = Field("", title="错误信息")


class WebCTPReqTransferSerial(WebCTPRequest):
    TransferSerial: TransferSerialField = Field(title="银期转账交易流水表")


class QryTransferSerialField(BaseModel):
    """请求查询转帐流水"""

    BrokerID: str = Field("", title="经纪公司代码")
    AccountID: str = Field("", title="投资者帐号")
    BankID: str = Field("", title="银行编码")
    CurrencyID: str = Field("", title="币种代码")


class WebCTPReqQryTransferSerial(WebCTPRequest):
    QryTransferSerial: QryTransferSerialField = Field(title="请求查询转帐流水")


class NotifyFutureSignInField(BaseModel):
    """期商签到通知"""

    TradeCode: str = Field("", title="业务功能码")
    BankID: str = Field("", title="银行代码")
    BankBranchID: str = Field("", title="银行分支机构代码")
    BrokerID: str = Field("", title="期商代码")
    BrokerBranchID: str = Field("", title="期商分支机构代码")
    TradeDate: str = Field("", title="交易日期")
    TradeTime: str = Field("", title="交易时间")
    BankSerial: str = Field("", title="银行流水号")
    TradingDay: str = Field("", title="交易系统日期 ")
    PlateSerial: int = Field(0, title="银期平台消息流水号")
    LastFragment: str = Field("", title="最后分片标志")
    SessionID: int = Field(0, title="会话号")
    InstallID: int = Field(0, title="安装编号")
    UserID: str = Field("", title="用户标识")
    Digest: str = Field("", title="摘要")
    CurrencyID: str = Field("", title="币种代码")
    DeviceID: str = Field("", title="渠道标志")
    BrokerIDByBank: str = Field("", title="期货公司银行编码")
    OperNo: str = Field("", title="交易柜员")
    RequestID: int = Field(0, title="请求编号")
    TID: int = Field(0, title="交易ID")
    ErrorID: int = Field(0, title="错误代码")
    ErrorMsg: str = Field("", title="错误信息")
    PinKey: str = Field("", title="PIN密钥")
    MacKey: str = Field("", title="MAC密钥")


class WebCTPReqNotifyFutureSignIn(WebCTPRequest):
    NotifyFutureSignIn: NotifyFutureSignInField = Field(title="期商签到通知")


class NotifyFutureSignOutField(BaseModel):
    """期商签退通知"""

    TradeCode: str = Field("", title="业务功能码")
    BankID: str = Field("", title="银行代码")
    BankBranchID: str = Field("", title="银行分支机构代码")
    BrokerID: str = Field("", title="期商代码")
    BrokerBranchID: str = Field("", title="期商分支机构代码")
    TradeDate: str = Field("", title="交易日期")
    TradeTime: str = Field("", title="交易时间")
    BankSerial: str = Field("", title="银行流水号")
    TradingDay: str = Field("", title="交易系统日期 ")
    PlateSerial: int = Field(0, title="银期平台消息流水号")
    LastFragment: str = Field("", title="最后分片标志")
    SessionID: int = Field(0, title="会话号")
    InstallID: int = Field(0, title="安装编号")
    UserID: str = Field("", title="用户标识")
    Digest: str = Field("", title="摘要")
    CurrencyID: str = Field("", title="币种代码")
    DeviceID: str = Field("", title="渠道标志")
    BrokerIDByBank: str = Field("", title="期货公司银行编码")
    OperNo: str = Field("", title="交易柜员")
    RequestID: int = Field(0, title="请求编号")
    TID: int = Field(0, title="交易ID")
    ErrorID: int = Field(0, title="错误代码")
    ErrorMsg: str = Field("", title="错误信息")


class WebCTPReqNotifyFutureSignOut(WebCTPRequest):
    NotifyFutureSignOut: NotifyFutureSignOutField = Field(title="期商签退通知")


class NotifySyncKeyField(BaseModel):
    """交易核心向银期报盘发出密钥同步处理结果的通知"""

    TradeCode: str = Field("", title="业务功能码")
    BankID: str = Field("", title="银行代码")
    BankBranchID: str = Field("", title="银行分支机构代码")
    BrokerID: str = Field("", title="期商代码")
    BrokerBranchID: str = Field("", title="期商分支机构代码")
    TradeDate: str = Field("", title="交易日期")
    TradeTime: str = Field("", title="交易时间")
    BankSerial: str = Field("", title="银行流水号")
    TradingDay: str = Field("", title="交易系统日期 ")
    PlateSerial: int = Field(0, title="银期平台消息流水号")
    LastFragment: str = Field("", title="最后分片标志")
    SessionID: int = Field(0, title="会话号")
    InstallID: int = Field(0, title="安装编号")
    UserID: str = Field("", title="用户标识")
    Message: str = Field("", title="交易核心给银期报盘的消息")
    DeviceID: str = Field("", title="渠道标志")
    BrokerIDByBank: str = Field("", title="期货公司银行编码")
    OperNo: str = Field("", title="交易柜员")
    RequestID: int = Field(0, title="请求编号")
    TID: int = Field(0, title="交易ID")
    ErrorID: int = Field(0, title="错误代码")
    ErrorMsg: str = Field("", title="错误信息")


class WebCTPReqNotifySyncKey(WebCTPRequest):
    NotifySyncKey: NotifySyncKeyField = Field(
        title="交易核心向银期报盘发出密钥同步处理结果的通知")


class QryAccountregisterField(BaseModel):
    """请求查询银期签约关系"""

    BrokerID: str = Field("", title="经纪公司代码")
    AccountID: str = Field("", title="投资者帐号")
    BankID: str = Field("", title="银行编码")
    BankBranchID: str = Field("", title="银行分支机构编码")
    CurrencyID: str = Field("", title="币种代码")


class WebCTPReqQryAccountregister(WebCTPRequest):
    QryAccountregister: QryAccountregisterField = Field(
        title="请求查询银期签约关系")


class AccountregisterField(BaseModel):
    """客户开销户信息表"""

    TradeDay: str = Field("", title="交易日期")
    BankID: str = Field("", title="银行编码")
    BankBranchID: str = Field("", title="银行分支机构编码")
    BankAccount: str = Field("", title="银行帐号")
    BrokerID: str = Field("", title="期货公司编码")
    BrokerBranchID: str = Field("", title="期货公司分支机构编码")
    AccountID: str = Field("", title="投资者帐号")
    IdCardType: str = Field("", title="证件类型")
    IdentifiedCardNo: str = Field("", title="证件号码")
    CustomerName: str = Field("", title="客户姓名")
    CurrencyID: str = Field("", title="币种代码")
    OpenOrDestroy: str = Field("", title="开销户类别")
    RegDate: str = Field("", title="签约日期")
    OutDate: str = Field("", title="解约日期")
    TID: int = Field(0, title="交易ID")
    CustType: str = Field("", title="客户类型")
    BankAccType: str = Field("", title="银行帐号类型")
    LongCustomerName: str = Field("", title="长客户姓名")


class WebCTPReqAccountregister(WebCTPRequest):
    Accountregister: AccountregisterField = Field(title="客户开销户信息表")


class OpenAccountField(BaseModel):
    """银期开户信息"""

    TradeCode: str = Field("", title="业务功能码")
    BankID: str = Field("", title="银行代码")
    BankBranchID: str = Field("", title="银行分支机构代码")
    BrokerID: str = Field("", title="期商代码")
    BrokerBranchID: str = Field("", title="期商分支机构代码")
    TradeDate: str = Field("", title="交易日期")
    TradeTime: str = Field("", title="交易时间")
    BankSerial: str = Field("", title="银行流水号")
    TradingDay: str = Field("", title="交易系统日期 ")
    PlateSerial: int = Field(0, title="银期平台消息流水号")
    LastFragment: str = Field("", title="最后分片标志")
    SessionID: int = Field(0, title="会话号")
    CustomerName: str = Field("", title="客户姓名")
    IdCardType: str = Field("", title="证件类型")
    IdentifiedCardNo: str = Field("", title="证件号码")
    Gender: str = Field("", title="性别")
    CountryCode: str = Field("", title="国家代码")
    CustType: str = Field("", title="客户类型")
    Address: str = Field("", title="地址")
    ZipCode: str = Field("", title="邮编")
    Telephone: str = Field("", title="电话号码")
    MobilePhone: str = Field("", title="手机")
    Fax: str = Field("", title="传真")
    EMail: str = Field("", title="电子邮件")
    MoneyAccountStatus: str = Field("", title="资金账户状态")
    BankAccount: str = Field("", title="银行帐号")
    BankPassWord: str = Field("", title="银行密码")
    AccountID: str = Field("", title="投资者帐号")
    Password: str = Field("", title="期货密码")
    InstallID: int = Field(0, title="安装编号")
    VerifyCertNoFlag: str = Field("", title="验证客户证件号码标志")
    CurrencyID: str = Field("", title="币种代码")
    CashExchangeCode: str = Field("", title="汇钞标志")
    Digest: str = Field("", title="摘要")
    BankAccType: str = Field("", title="银行帐号类型")
    DeviceID: str = Field("", title="渠道标志")
    BankSecuAccType: str = Field("", title="期货单位帐号类型")
    BrokerIDByBank: str = Field("", title="期货公司银行编码")
    BankSecuAcc: str = Field("", title="期货单位帐号")
    BankPwdFlag: str = Field("", title="银行密码标志")
    SecuPwdFlag: str = Field("", title="期货资金密码核对标志")
    OperNo: str = Field("", title="交易柜员")
    TID: int = Field(0, title="交易ID")
    UserID: str = Field("", title="用户标识")
    ErrorID: int = Field(0, title="错误代码")
    ErrorMsg: str = Field("", title="错误信息")
    LongCustomerName: str = Field("", title="长客户姓名")


class WebCTPReqOpenAccount(WebCTPRequest):
    OpenAccount: OpenAccountField = Field(title="银期开户信息")


class CancelAccountField(BaseModel):
    """银期销户信息"""

    TradeCode: str = Field("", title="业务功能码")
    BankID: str = Field("", title="银行代码")
    BankBranchID: str = Field("", title="银行分支机构代码")
    BrokerID: str = Field("", title="期商代码")
    BrokerBranchID: str = Field("", title="期商分支机构代码")
    TradeDate: str = Field("", title="交易日期")
    TradeTime: str = Field("", title="交易时间")
    BankSerial: str = Field("", title="银行流水号")
    TradingDay: str = Field("", title="交易系统日期 ")
    PlateSerial: int = Field(0, title="银期平台消息流水号")
    LastFragment: str = Field("", title="最后分片标志")
    SessionID: int = Field(0, title="会话号")
    CustomerName: str = Field("", title="客户姓名")
    IdCardType: str = Field("", title="证件类型")
    IdentifiedCardNo: str = Field("", title="证件号码")
    Gender: str = Field("", title="性别")
    CountryCode: str = Field("", title="国家代码")
    CustType: str = Field("", title="客户类型")
    Address: str = Field("", title="地址")
    ZipCode: str = Field("", title="邮编")
    Telephone: str = Field("", title="电话号码")
    MobilePhone: str = Field("", title="手机")
    Fax: str = Field("", title="传真")
    EMail: str = Field("", title="电子邮件")
    MoneyAccountStatus: str = Field("", title="资金账户状态")
    BankAccount: str = Field("", title="银行帐号")
    BankPassWord: str = Field("", title="银行密码")
    AccountID: str = Field("", title="投资者帐号")
    Password: str = Field("", title="期货密码")
    InstallID: int = Field(0, title="安装编号")
    VerifyCertNoFlag: str = Field("", title="验证客户证件号码标志")
    CurrencyID: str = Field("", title="币种代码")
    CashExchangeCode: str = Field("", title="汇钞标志")
    Digest: str = Field("", title="摘要")
    BankAccType: str = Field("", title="银行帐号类型")
    DeviceID: str = Field("", title="渠道标志")
    BankSecuAccType: str = Field("", title="期货单位帐号类型")
    BrokerIDByBank: str = Field("", title="期货公司银行编码")
    BankSecuAcc: str = Field("", title="期货单位帐号")
    BankPwdFlag: str = Field("", title="银行密码标志")
    SecuPwdFlag: str = Field("", title="期货资金密码核对标志")
    OperNo: str = Field("", title="交易柜员")
    TID: int = Field(0, title="交易ID")
    UserID: str = Field("", title="用户标识")
    ErrorID: int = Field(0, title="错误代码")
    ErrorMsg: str = Field("", title="错误信息")
    LongCustomerName: str = Field("", title="长客户姓名")


class WebCTPReqCancelAccount(WebCTPRequest):
    CancelAccount: CancelAccountField = Field(title="银期销户信息")


class ChangeAccountField(BaseModel):
    """银期变更银行账号信息"""

    TradeCode: str = Field("", title="业务功能码")
    BankID: str = Field("", title="银行代码")
    BankBranchID: str = Field("", title="银行分支机构代码")
    BrokerID: str = Field("", title="期商代码")
    BrokerBranchID: str = Field("", title="期商分支机构代码")
    TradeDate: str = Field("", title="交易日期")
    TradeTime: str = Field("", title="交易时间")
    BankSerial: str = Field("", title="银行流水号")
    TradingDay: str = Field("", title="交易系统日期 ")
    PlateSerial: int = Field(0, title="银期平台消息流水号")
    LastFragment: str = Field("", title="最后分片标志")
    SessionID: int = Field(0, title="会话号")
    CustomerName: str = Field("", title="客户姓名")
    IdCardType: str = Field("", title="证件类型")
    IdentifiedCardNo: str = Field("", title="证件号码")
    Gender: str = Field("", title="性别")
    CountryCode: str = Field("", title="国家代码")
    CustType: str = Field("", title="客户类型")
    Address: str = Field("", title="地址")
    ZipCode: str = Field("", title="邮编")
    Telephone: str = Field("", title="电话号码")
    MobilePhone: str = Field("", title="手机")
    Fax: str = Field("", title="传真")
    EMail: str = Field("", title="电子邮件")
    MoneyAccountStatus: str = Field("", title="资金账户状态")
    BankAccount: str = Field("", title="银行帐号")
    BankPassWord: str = Field("", title="银行密码")
    NewBankAccount: str = Field("", title="新银行帐号")
    NewBankPassWord: str = Field("", title="新银行密码")
    AccountID: str = Field("", title="投资者帐号")
    Password: str = Field("", title="期货密码")
    BankAccType: str = Field("", title="银行帐号类型")
    InstallID: int = Field(0, title="安装编号")
    VerifyCertNoFlag: str = Field("", title="验证客户证件号码标志")
    CurrencyID: str = Field("", title="币种代码")
    BrokerIDByBank: str = Field("", title="期货公司银行编码")
    BankPwdFlag: str = Field("", title="银行密码标志")
    SecuPwdFlag: str = Field("", title="期货资金密码核对标志")
    TID: int = Field(0, title="交易ID")
    Digest: str = Field("", title="摘要")
    ErrorID: int = Field(0, title="错误代码")
    ErrorMsg: str = Field("", title="错误信息")
    LongCustomerName: str = Field("", title="长客户姓名")


class WebCTPReqChangeAccount(WebCTPRequest):
    ChangeAccount: ChangeAccountField = Field(title="银期变更银行账号信息")


class SecAgentACIDMapField(BaseModel):
    """二级代理操作员银期权限"""

    BrokerID: str = Field("", title="经纪公司代码")
    UserID: str = Field("", title="用户代码")
    AccountID: str = Field("", title="资金账户")
    CurrencyID: str = Field("", title="币种")
    BrokerSecAgentID: str = Field("", title="境外中介机构资金帐号")


class WebCTPReqSecAgentACIDMap(WebCTPRequest):
    SecAgentACIDMap: SecAgentACIDMapField = Field(
        title="二级代理操作员银期权限")


class QrySecAgentACIDMapField(BaseModel):
    """二级代理操作员银期权限查询"""

    BrokerID: str = Field("", title="经纪公司代码")
    UserID: str = Field("", title="用户代码")
    AccountID: str = Field("", title="资金账户")
    CurrencyID: str = Field("", title="币种")


class WebCTPReqQrySecAgentACIDMap(WebCTPRequest):
    QrySecAgentACIDMap: QrySecAgentACIDMapField = Field(
        title="二级代理操作员银期权限查询")


class UserRightsAssignField(BaseModel):
    """灾备中心交易权限"""

    BrokerID: str = Field("", title="应用单元代码")
    UserID: str = Field("", title="用户代码")
    DRIdentityID: int = Field(0, title="交易中心代码")


class WebCTPReqUserRightsAssign(WebCTPRequest):
    UserRightsAssign: UserRightsAssignField = Field(title="灾备中心交易权限")


class BrokerUserRightAssignField(BaseModel):
    """经济公司是否有在本标示的交易权限"""

    BrokerID: str = Field("", title="应用单元代码")
    DRIdentityID: int = Field(0, title="交易中心代码")
    Tradeable: int = Field(0, title="能否交易")


class WebCTPReqBrokerUserRightAssign(WebCTPRequest):
    BrokerUserRightAssign: BrokerUserRightAssignField = Field(
        title="经济公司是否有在本标示的交易权限")


class DRTransferField(BaseModel):
    """灾备交易转换报文"""

    OrigDRIdentityID: int = Field(0, title="原交易中心代码")
    DestDRIdentityID: int = Field(0, title="目标交易中心代码")
    OrigBrokerID: str = Field("", title="原应用单元代码")
    DestBrokerID: str = Field("", title="目标易用单元代码")


class WebCTPReqDRTransfer(WebCTPRequest):
    DRTransfer: DRTransferField = Field(title="灾备交易转换报文")


class FensUserInfoField(BaseModel):
    """Fens用户信息"""

    BrokerID: str = Field("", title="经纪公司代码")
    UserID: str = Field("", title="用户代码")
    LoginMode: str = Field("", title="登录模式")


class WebCTPReqFensUserInfo(WebCTPRequest):
    FensUserInfo: FensUserInfoField = Field(title="Fens用户信息")


class CurrTransferIdentityField(BaseModel):
    """当前银期所属交易中心"""

    IdentityID: int = Field(0, title="交易中心代码")


class WebCTPReqCurrTransferIdentity(WebCTPRequest):
    CurrTransferIdentity: CurrTransferIdentityField = Field(
        title="当前银期所属交易中心")


class LoginForbiddenUserField(BaseModel):
    """禁止登录用户"""

    BrokerID: str = Field("", title="经纪公司代码")
    UserID: str = Field("", title="用户代码")
    reserve1: str = Field("", title="保留的无效字段")
    IPAddress: str = Field("", title="IP地址")


class WebCTPReqLoginForbiddenUser(WebCTPRequest):
    LoginForbiddenUser: LoginForbiddenUserField = Field(title="禁止登录用户")


class QryLoginForbiddenUserField(BaseModel):
    """查询禁止登录用户"""

    BrokerID: str = Field("", title="经纪公司代码")
    UserID: str = Field("", title="用户代码")


class WebCTPReqQryLoginForbiddenUser(WebCTPRequest):
    QryLoginForbiddenUser: QryLoginForbiddenUserField = Field(
        title="查询禁止登录用户")


class MulticastGroupInfoField(BaseModel):
    """UDP组播组信息"""

    GroupIP: str = Field("", title="组播组IP地址")
    GroupPort: int = Field(0, title="组播组IP端口")
    SourceIP: str = Field("", title="源地址")


class WebCTPReqMulticastGroupInfo(WebCTPRequest):
    MulticastGroupInfo: MulticastGroupInfoField = Field(title="UDP组播组信息")


class TradingAccountReserveField(BaseModel):
    """资金账户基本准备金"""

    BrokerID: str = Field("", title="经纪公司代码")
    AccountID: str = Field("", title="投资者帐号")
    Reserve: float = Field(0.0, title="基本准备金")
    CurrencyID: str = Field("", title="币种代码")


class WebCTPReqTradingAccountReserve(WebCTPRequest):
    TradingAccountReserve: TradingAccountReserveField = Field(
        title="资金账户基本准备金")


class QryLoginForbiddenIPField(BaseModel):
    """查询禁止登录IP"""

    reserve1: str = Field("", title="保留的无效字段")
    IPAddress: str = Field("", title="IP地址")


class WebCTPReqQryLoginForbiddenIP(WebCTPRequest):
    QryLoginForbiddenIP: QryLoginForbiddenIPField = Field(
        title="查询禁止登录IP")


class QryIPListField(BaseModel):
    """查询IP列表"""

    reserve1: str = Field("", title="保留的无效字段")
    IPAddress: str = Field("", title="IP地址")


class WebCTPReqQryIPList(WebCTPRequest):
    QryIPList: QryIPListField = Field(title="查询IP列表")


class QryUserRightsAssignField(BaseModel):
    """查询用户下单权限分配表"""

    BrokerID: str = Field("", title="应用单元代码")
    UserID: str = Field("", title="用户代码")


class WebCTPReqQryUserRightsAssign(WebCTPRequest):
    QryUserRightsAssign: QryUserRightsAssignField = Field(
        title="查询用户下单权限分配表")


class ReserveOpenAccountConfirmField(BaseModel):
    """银期预约开户确认请求"""

    TradeCode: str = Field("", title="业务功能码")
    BankID: str = Field("", title="银行代码")
    BankBranchID: str = Field("", title="银行分支机构代码")
    BrokerID: str = Field("", title="期商代码")
    BrokerBranchID: str = Field("", title="期商分支机构代码")
    TradeDate: str = Field("", title="交易日期")
    TradeTime: str = Field("", title="交易时间")
    BankSerial: str = Field("", title="银行流水号")
    TradingDay: str = Field("", title="交易系统日期 ")
    PlateSerial: int = Field(0, title="银期平台消息流水号")
    LastFragment: str = Field("", title="最后分片标志")
    SessionID: int = Field(0, title="会话号")
    CustomerName: str = Field("", title="客户姓名")
    IdCardType: str = Field("", title="证件类型")
    IdentifiedCardNo: str = Field("", title="证件号码")
    Gender: str = Field("", title="性别")
    CountryCode: str = Field("", title="国家代码")
    CustType: str = Field("", title="客户类型")
    Address: str = Field("", title="地址")
    ZipCode: str = Field("", title="邮编")
    Telephone: str = Field("", title="电话号码")
    MobilePhone: str = Field("", title="手机")
    Fax: str = Field("", title="传真")
    EMail: str = Field("", title="电子邮件")
    MoneyAccountStatus: str = Field("", title="资金账户状态")
    BankAccount: str = Field("", title="银行帐号")
    BankPassWord: str = Field("", title="银行密码")
    InstallID: int = Field(0, title="安装编号")
    VerifyCertNoFlag: str = Field("", title="验证客户证件号码标志")
    CurrencyID: str = Field("", title="币种代码")
    Digest: str = Field("", title="摘要")
    BankAccType: str = Field("", title="银行帐号类型")
    BrokerIDByBank: str = Field("", title="期货公司银行编码")
    TID: int = Field(0, title="交易ID")
    AccountID: str = Field("", title="投资者帐号")
    Password: str = Field("", title="期货密码")
    BankReserveOpenSeq: str = Field("", title="预约开户银行流水号")
    BookDate: str = Field("", title="预约开户日期")
    BookPsw: str = Field("", title="预约开户验证密码")
    ErrorID: int = Field(0, title="错误代码")
    ErrorMsg: str = Field("", title="错误信息")


class WebCTPReqReserveOpenAccountConfirm(WebCTPRequest):
    ReserveOpenAccountConfirm: ReserveOpenAccountConfirmField = Field(
        title="银期预约开户确认请求")


class ReserveOpenAccountField(BaseModel):
    """银期预约开户"""

    TradeCode: str = Field("", title="业务功能码")
    BankID: str = Field("", title="银行代码")
    BankBranchID: str = Field("", title="银行分支机构代码")
    BrokerID: str = Field("", title="期商代码")
    BrokerBranchID: str = Field("", title="期商分支机构代码")
    TradeDate: str = Field("", title="交易日期")
    TradeTime: str = Field("", title="交易时间")
    BankSerial: str = Field("", title="银行流水号")
    TradingDay: str = Field("", title="交易系统日期 ")
    PlateSerial: int = Field(0, title="银期平台消息流水号")
    LastFragment: str = Field("", title="最后分片标志")
    SessionID: int = Field(0, title="会话号")
    CustomerName: str = Field("", title="客户姓名")
    IdCardType: str = Field("", title="证件类型")
    IdentifiedCardNo: str = Field("", title="证件号码")
    Gender: str = Field("", title="性别")
    CountryCode: str = Field("", title="国家代码")
    CustType: str = Field("", title="客户类型")
    Address: str = Field("", title="地址")
    ZipCode: str = Field("", title="邮编")
    Telephone: str = Field("", title="电话号码")
    MobilePhone: str = Field("", title="手机")
    Fax: str = Field("", title="传真")
    EMail: str = Field("", title="电子邮件")
    MoneyAccountStatus: str = Field("", title="资金账户状态")
    BankAccount: str = Field("", title="银行帐号")
    BankPassWord: str = Field("", title="银行密码")
    InstallID: int = Field(0, title="安装编号")
    VerifyCertNoFlag: str = Field("", title="验证客户证件号码标志")
    CurrencyID: str = Field("", title="币种代码")
    Digest: str = Field("", title="摘要")
    BankAccType: str = Field("", title="银行帐号类型")
    BrokerIDByBank: str = Field("", title="期货公司银行编码")
    TID: int = Field(0, title="交易ID")
    ReserveOpenAccStas: str = Field("", title="预约开户状态")
    ErrorID: int = Field(0, title="错误代码")
    ErrorMsg: str = Field("", title="错误信息")


class WebCTPReqReserveOpenAccount(WebCTPRequest):
    ReserveOpenAccount: ReserveOpenAccountField = Field(title="银期预约开户")


class AccountPropertyField(BaseModel):
    """银行账户属性"""

    BrokerID: str = Field("", title="经纪公司代码")
    AccountID: str = Field("", title="投资者帐号")
    BankID: str = Field("", title="银行统一标识类型")
    BankAccount: str = Field("", title="银行账户")
    OpenName: str = Field("", title="银行账户的开户人名称")
    OpenBank: str = Field("", title="银行账户的开户行")
    IsActive: int = Field(0, title="是否活跃")
    AccountSourceType: str = Field("", title="账户来源")
    OpenDate: str = Field("", title="开户日期")
    CancelDate: str = Field("", title="注销日期")
    OperatorID: str = Field("", title="录入员代码")
    OperateDate: str = Field("", title="录入日期")
    OperateTime: str = Field("", title="录入时间")
    CurrencyID: str = Field("", title="币种代码")


class WebCTPReqAccountProperty(WebCTPRequest):
    AccountProperty: AccountPropertyField = Field(title="银行账户属性")


class QryCurrDRIdentityField(BaseModel):
    """查询当前交易中心"""

    DRIdentityID: int = Field(0, title="交易中心代码")


class WebCTPReqQryCurrDRIdentity(WebCTPRequest):
    QryCurrDRIdentity: QryCurrDRIdentityField = Field(title="查询当前交易中心")


class CurrDRIdentityField(BaseModel):
    """当前交易中心"""

    DRIdentityID: int = Field(0, title="交易中心代码")


class WebCTPReqCurrDRIdentity(WebCTPRequest):
    CurrDRIdentity: CurrDRIdentityField = Field(title="当前交易中心")


class QrySecAgentCheckModeField(BaseModel):
    """查询二级代理商资金校验模式"""

    BrokerID: str = Field("", title="经纪公司代码")
    InvestorID: str = Field("", title="投资者代码")


class WebCTPReqQrySecAgentCheckMode(WebCTPRequest):
    QrySecAgentCheckMode: QrySecAgentCheckModeField = Field(
        title="查询二级代理商资金校验模式")


class QrySecAgentTradeInfoField(BaseModel):
    """查询二级代理商信息"""

    BrokerID: str = Field("", title="经纪公司代码")
    BrokerSecAgentID: str = Field("", title="境外中介机构资金帐号")


class WebCTPReqQrySecAgentTradeInfo(WebCTPRequest):
    QrySecAgentTradeInfo: QrySecAgentTradeInfoField = Field(
        title="查询二级代理商信息")


class UserSystemInfoField(BaseModel):
    """用户系统信息"""

    BrokerID: str = Field("", title="经纪公司代码")
    UserID: str = Field("", title="用户代码")
    ClientSystemInfoLen: int = Field(0, title="用户端系统内部信息长度")
    ClientSystemInfo: str = Field("", title="用户端系统内部信息")
    reserve1: str = Field("", title="保留的无效字段")
    ClientIPPort: int = Field(0, title="终端IP端口")
    ClientLoginTime: str = Field("", title="登录成功时间")
    ClientAppID: str = Field("", title="App代码")
    ClientPublicIP: str = Field("", title="用户公网IP")
    ClientLoginRemark: str = Field("", title="客户登录备注2")


class WebCTPReqUserSystemInfo(WebCTPRequest):
    UserSystemInfo: UserSystemInfoField = Field(title="用户系统信息")


class ReqUserAuthMethodField(BaseModel):
    """用户发出获取安全安全登陆方法请求"""

    TradingDay: str = Field("", title="交易日")
    BrokerID: str = Field("", title="经纪公司代码")
    UserID: str = Field("", title="用户代码")


class WebCTPReqUserAuthMethod(WebCTPRequest):
    ReqUserAuthMethod: ReqUserAuthMethodField = Field(
        title="用户发出获取安全安全登陆方法请求")


class ReqGenUserCaptchaField(BaseModel):
    """用户发出获取安全安全登陆方法请求"""

    TradingDay: str = Field("", title="交易日")
    BrokerID: str = Field("", title="经纪公司代码")
    UserID: str = Field("", title="用户代码")


class WebCTPReqGenUserCaptcha(WebCTPRequest):
    ReqGenUserCaptcha: ReqGenUserCaptchaField = Field(
        title="用户发出获取安全安全登陆方法请求")


class ReqGenUserTextField(BaseModel):
    """用户发出获取安全安全登陆方法请求"""

    TradingDay: str = Field("", title="交易日")
    BrokerID: str = Field("", title="经纪公司代码")
    UserID: str = Field("", title="用户代码")


class WebCTPReqGenUserText(WebCTPRequest):
    ReqGenUserText: ReqGenUserTextField = Field(
        title="用户发出获取安全安全登陆方法请求")


class ReqUserLoginWithCaptchaField(BaseModel):
    """用户发出带图形验证码的登录请求请求"""

    TradingDay: str = Field("", title="交易日")
    BrokerID: str = Field("", title="经纪公司代码")
    UserID: str = Field("", title="用户代码")
    Password: str = Field("", title="密码")
    UserProductInfo: str = Field("", title="用户端产品信息")
    InterfaceProductInfo: str = Field("", title="接口端产品信息")
    ProtocolInfo: str = Field("", title="协议信息")
    MacAddress: str = Field("", title="Mac地址")
    reserve1: str = Field("", title="保留的无效字段")
    LoginRemark: str = Field("", title="登录备注")
    Captcha: str = Field("", title="图形验证码的文字内容")
    ClientIPPort: int = Field(0, title="终端IP端口")
    ClientIPAddress: str = Field("", title="终端IP地址")


class WebCTPReqUserLoginWithCaptcha(WebCTPRequest):
    ReqUserLoginWithCaptcha: ReqUserLoginWithCaptchaField = Field(
        title="用户发出带图形验证码的登录请求请求")


class ReqUserLoginWithTextField(BaseModel):
    """用户发出带短信验证码的登录请求请求"""

    TradingDay: str = Field("", title="交易日")
    BrokerID: str = Field("", title="经纪公司代码")
    UserID: str = Field("", title="用户代码")
    Password: str = Field("", title="密码")
    UserProductInfo: str = Field("", title="用户端产品信息")
    InterfaceProductInfo: str = Field("", title="接口端产品信息")
    ProtocolInfo: str = Field("", title="协议信息")
    MacAddress: str = Field("", title="Mac地址")
    reserve1: str = Field("", title="保留的无效字段")
    LoginRemark: str = Field("", title="登录备注")
    Text: str = Field("", title="短信验证码文字内容")
    ClientIPPort: int = Field(0, title="终端IP端口")
    ClientIPAddress: str = Field("", title="终端IP地址")


class WebCTPReqUserLoginWithText(WebCTPRequest):
    ReqUserLoginWithText: ReqUserLoginWithTextField = Field(
        title="用户发出带短信验证码的登录请求请求")


class ReqUserLoginWithOTPField(BaseModel):
    """用户发出带动态验证码的登录请求请求"""

    TradingDay: str = Field("", title="交易日")
    BrokerID: str = Field("", title="经纪公司代码")
    UserID: str = Field("", title="用户代码")
    Password: str = Field("", title="密码")
    UserProductInfo: str = Field("", title="用户端产品信息")
    InterfaceProductInfo: str = Field("", title="接口端产品信息")
    ProtocolInfo: str = Field("", title="协议信息")
    MacAddress: str = Field("", title="Mac地址")
    reserve1: str = Field("", title="保留的无效字段")
    LoginRemark: str = Field("", title="登录备注")
    OTPPassword: str = Field("", title="OTP密码")
    ClientIPPort: int = Field(0, title="终端IP端口")
    ClientIPAddress: str = Field("", title="终端IP地址")


class WebCTPReqUserLoginWithOTP(WebCTPRequest):
    ReqUserLoginWithOTP: ReqUserLoginWithOTPField = Field(
        title="用户发出带动态验证码的登录请求请求")


class ReqApiHandshakeField(BaseModel):
    """api握手请求"""

    CryptoKeyVersion: str = Field("", title="api与front通信密钥版本号")


class WebCTPReqApiHandshake(WebCTPRequest):
    ReqApiHandshake: ReqApiHandshakeField = Field(title="api握手请求")


class ReqVerifyApiKeyField(BaseModel):
    """api给front的验证key的请求"""

    ApiHandshakeDataLen: int = Field(0, title="握手回复数据长度")
    ApiHandshakeData: str = Field("", title="握手回复数据")


class WebCTPReqVerifyApiKey(WebCTPRequest):
    ReqVerifyApiKey: ReqVerifyApiKeyField = Field(
        title="api给front的验证key的请求")


class DepartmentUserField(BaseModel):
    """操作员组织架构关系"""

    BrokerID: str = Field("", title="经纪公司代码")
    UserID: str = Field("", title="用户代码")
    InvestorRange: str = Field("", title="投资者范围")
    InvestorID: str = Field("", title="投资者代码")


class WebCTPReqDepartmentUser(WebCTPRequest):
    DepartmentUser: DepartmentUserField = Field(title="操作员组织架构关系")


class QueryFreqField(BaseModel):
    """查询频率，每秒查询比数"""

    QueryFreq: int = Field(0, title="查询频率")


class WebCTPReqQueryFreq(WebCTPRequest):
    QueryFreq: QueryFreqField = Field(title="查询频率，每秒查询比数")


class MulticastInstrumentField(BaseModel):
    """MulticastInstrument"""

    TopicID: int = Field(0, title="主题号")
    reserve1: str = Field("", title="保留的无效字段")
    InstrumentNo: int = Field(0, title="合约编号")
    CodePrice: float = Field(0.0, title="基准价")
    VolumeMultiple: int = Field(0, title="合约数量乘数")
    PriceTick: float = Field(0.0, title="最小变动价位")
    InstrumentID: str = Field("", title="合约代码")


class WebCTPReqMulticastInstrument(WebCTPRequest):
    MulticastInstrument: MulticastInstrumentField = Field(
        title="MulticastInstrument")


class QryMulticastInstrumentField(BaseModel):
    """QryMulticastInstrument"""

    TopicID: int = Field(0, title="主题号")
    reserve1: str = Field("", title="保留的无效字段")
    InstrumentID: str = Field("", title="合约代码")


class WebCTPReqQryMulticastInstrument(WebCTPRequest):
    QryMulticastInstrument: QryMulticastInstrumentField = Field(
        title="QryMulticastInstrument")


class AppIDAuthAssignField(BaseModel):
    """App客户端权限分配"""

    BrokerID: str = Field("", title="经纪公司代码")
    AppID: str = Field("", title="App代码")
    DRIdentityID: int = Field(0, title="交易中心代码")


class WebCTPReqAppIDAuthAssign(WebCTPRequest):
    AppIDAuthAssign: AppIDAuthAssignField = Field(title="App客户端权限分配")


class AuthForbiddenIPField(BaseModel):
    """禁止认证IP"""

    IPAddress: str = Field("", title="IP地址")


class WebCTPReqAuthForbiddenIP(WebCTPRequest):
    AuthForbiddenIP: AuthForbiddenIPField = Field(title="禁止认证IP")


class QryAuthForbiddenIPField(BaseModel):
    """查询禁止认证IP"""

    IPAddress: str = Field("", title="IP地址")


class WebCTPReqQryAuthForbiddenIP(WebCTPRequest):
    QryAuthForbiddenIP: QryAuthForbiddenIPField = Field(title="查询禁止认证IP")


class SyncDelaySwapFrozenField(BaseModel):
    """换汇可提冻结"""

    DelaySwapSeqNo: str = Field("", title="换汇流水号")
    BrokerID: str = Field("", title="经纪公司代码")
    InvestorID: str = Field("", title="投资者代码")
    FromCurrencyID: str = Field("", title="源币种")
    FromRemainSwap: float = Field(0.0, title="源剩余换汇额度(可提冻结)")
    IsManualSwap: int = Field(0, title="是否手工换汇")


class WebCTPReqSyncDelaySwapFrozen(WebCTPRequest):
    SyncDelaySwapFrozen: SyncDelaySwapFrozenField = Field(title="换汇可提冻结")


class QryMaxOrderVolumeField(BaseModel):
    """查询最大报单数量"""

    BrokerID: str = Field("", title="经纪公司代码")
    InvestorID: str = Field("", title="投资者代码")
    reserve1: str = Field("", title="保留的无效字段")
    Direction: str = Field("", title="买卖方向")
    OffsetFlag: str = Field("", title="开平标志")
    HedgeFlag: str = Field("", title="投机套保标志")
    MaxVolume: int = Field(0, title="最大允许报单数量")
    ExchangeID: str = Field("", title="交易所代码")
    InvestUnitID: str = Field("", title="投资单元代码")
    InstrumentID: str = Field("", title="合约代码")


class WebCTPReqQryMaxOrderVolume(WebCTPRequest):
    QryMaxOrderVolume: QryMaxOrderVolumeField = Field(title="查询最大报单数量")


class QryMaxOrderVolumeWithPriceField(BaseModel):
    """根据价格查询最大报单数量"""

    BrokerID: str = Field("", title="经纪公司代码")
    InvestorID: str = Field("", title="投资者代码")
    reserve1: str = Field("", title="保留的无效字段")
    Direction: str = Field("", title="买卖方向")
    OffsetFlag: str = Field("", title="开平标志")
    HedgeFlag: str = Field("", title="投机套保标志")
    MaxVolume: int = Field(0, title="最大允许报单数量")
    Price: float = Field(0.0, title="报单价格")
    ExchangeID: str = Field("", title="交易所代码")
    InvestUnitID: str = Field("", title="投资单元代码")
    InstrumentID: str = Field("", title="合约代码")


class WebCTPReqQryMaxOrderVolumeWithPrice(WebCTPRequest):
    QryMaxOrderVolumeWithPrice: QryMaxOrderVolumeWithPriceField = Field(
        title="根据价格查询最大报单数量")


class AuthUserIDField(BaseModel):
    """终端用户绑定信息"""

    BrokerID: str = Field("", title="经纪公司代码")
    AppID: str = Field("", title="App代码")
    UserID: str = Field("", title="用户代码")
    AuthType: str = Field("", title="校验类型")


class WebCTPReqAuthUserID(WebCTPRequest):
    AuthUserID: AuthUserIDField = Field(title="终端用户绑定信息")


class AuthIPField(BaseModel):
    """用户IP绑定信息"""

    BrokerID: str = Field("", title="经纪公司代码")
    AppID: str = Field("", title="App代码")
    IPAddress: str = Field("", title="用户代码")


class WebCTPReqAuthIP(WebCTPRequest):
    AuthIP: AuthIPField = Field(title="用户IP绑定信息")


class QryClassifiedInstrumentField(BaseModel):
    """查询分类合约"""

    InstrumentID: str = Field("", title="合约代码")
    ExchangeID: str = Field("", title="交易所代码")
    ExchangeInstID: str = Field("", title="合约在交易所的代码")
    ProductID: str = Field("", title="产品代码")
    TradingType: str = Field("", title="合约交易状态")
    ClassType: str = Field("", title="合约分类类型")


class WebCTPReqQryClassifiedInstrument(WebCTPRequest):
    QryClassifiedInstrument: QryClassifiedInstrumentField = Field(
        title="查询分类合约")


class QryCombPromotionParamField(BaseModel):
    """查询组合优惠比例"""

    ExchangeID: str = Field("", title="交易所代码")
    InstrumentID: str = Field("", title="合约代码")


class WebCTPReqQryCombPromotionParam(WebCTPRequest):
    QryCombPromotionParam: QryCombPromotionParamField = Field(
        title="查询组合优惠比例")


class CombPromotionParamField(BaseModel):
    """组合优惠比例"""

    ExchangeID: str = Field("", title="交易所代码")
    InstrumentID: str = Field("", title="合约代码")
    CombHedgeFlag: str = Field("", title="投机套保标志")
    Xparameter: float = Field(0.0, title="期权组合保证金比例")


class WebCTPReqCombPromotionParam(WebCTPRequest):
    CombPromotionParam: CombPromotionParamField = Field(title="组合优惠比例")


class MarketDataBandingPriceField(BaseModel):
    """行情上下带价"""

    BandingUpperPrice: float = Field(0.0, title="上带价")
    BandingLowerPrice: float = Field(0.0, title="下带价")


class WebCTPReqMarketDataBandingPrice(WebCTPRequest):
    MarketDataBandingPrice: MarketDataBandingPriceField = Field(
        title="行情上下带价")


class QryRiskSettleInvstPositionField(BaseModel):
    """投资者风险结算持仓查询"""

    BrokerID: str = Field("", title="经纪公司代码")
    InvestorID: str = Field("", title="投资者代码")
    InstrumentID: str = Field("", title="合约代码")


class WebCTPReqQryRiskSettleInvstPosition(WebCTPRequest):
    QryRiskSettleInvstPosition: QryRiskSettleInvstPositionField = Field(
        title="投资者风险结算持仓查询")


class QryRiskSettleProductStatusField(BaseModel):
    """风险结算产品查询"""

    ProductID: str = Field("", title="产品代码")


class WebCTPReqQryRiskSettleProductStatus(WebCTPRequest):
    QryRiskSettleProductStatus: QryRiskSettleProductStatusField = Field(
        title="风险结算产品查询")


class RiskSettleInvstPositionField(BaseModel):
    """投资者风险结算持仓"""

    InstrumentID: str = Field("", title="合约代码")
    BrokerID: str = Field("", title="经纪公司代码")
    InvestorID: str = Field("", title="投资者代码")
    PosiDirection: str = Field("", title="持仓多空方向")
    HedgeFlag: str = Field("", title="投机套保标志")
    PositionDate: str = Field("", title="持仓日期")
    YdPosition: int = Field(0, title="上日持仓")
    Position: int = Field(0, title="今日持仓")
    LongFrozen: int = Field(0, title="多头冻结")
    ShortFrozen: int = Field(0, title="空头冻结")
    LongFrozenAmount: float = Field(0.0, title="开仓冻结金额")
    ShortFrozenAmount: float = Field(0.0, title="开仓冻结金额")
    OpenVolume: int = Field(0, title="开仓量")
    CloseVolume: int = Field(0, title="平仓量")
    OpenAmount: float = Field(0.0, title="开仓金额")
    CloseAmount: float = Field(0.0, title="平仓金额")
    PositionCost: float = Field(0.0, title="持仓成本")
    PreMargin: float = Field(0.0, title="上次占用的保证金")
    UseMargin: float = Field(0.0, title="占用的保证金")
    FrozenMargin: float = Field(0.0, title="冻结的保证金")
    FrozenCash: float = Field(0.0, title="冻结的资金")
    FrozenCommission: float = Field(0.0, title="冻结的手续费")
    CashIn: float = Field(0.0, title="资金差额")
    Commission: float = Field(0.0, title="手续费")
    CloseProfit: float = Field(0.0, title="平仓盈亏")
    PositionProfit: float = Field(0.0, title="持仓盈亏")
    PreSettlementPrice: float = Field(0.0, title="上次结算价")
    SettlementPrice: float = Field(0.0, title="本次结算价")
    TradingDay: str = Field("", title="交易日")
    SettlementID: int = Field(0, title="结算编号")
    OpenCost: float = Field(0.0, title="开仓成本")
    ExchangeMargin: float = Field(0.0, title="交易所保证金")
    CombPosition: int = Field(0, title="组合成交形成的持仓")
    CombLongFrozen: int = Field(0, title="组合多头冻结")
    CombShortFrozen: int = Field(0, title="组合空头冻结")
    CloseProfitByDate: float = Field(0.0, title="逐日盯市平仓盈亏")
    CloseProfitByTrade: float = Field(0.0, title="逐笔对冲平仓盈亏")
    TodayPosition: int = Field(0, title="今日持仓")
    MarginRateByMoney: float = Field(0.0, title="保证金率")
    MarginRateByVolume: float = Field(0.0, title="保证金率(按手数)")
    StrikeFrozen: int = Field(0, title="执行冻结")
    StrikeFrozenAmount: float = Field(0.0, title="执行冻结金额")
    AbandonFrozen: int = Field(0, title="放弃执行冻结")
    ExchangeID: str = Field("", title="交易所代码")
    YdStrikeFrozen: int = Field(0, title="执行冻结的昨仓")
    InvestUnitID: str = Field("", title="投资单元代码")
    PositionCostOffset: float = Field(0.0, title="持仓成本差值")
    TasPosition: int = Field(0, title="tas持仓手数")
    TasPositionCost: float = Field(0.0, title="tas持仓成本")


class WebCTPReqRiskSettleInvstPosition(WebCTPRequest):
    RiskSettleInvstPosition: RiskSettleInvstPositionField = Field(
        title="投资者风险结算持仓")


class RiskSettleProductStatusField(BaseModel):
    """风险品种"""

    ExchangeID: str = Field("", title="交易所代码")
    ProductID: str = Field("", title="产品编号")
    ProductStatus: str = Field("", title="产品结算状态")


class WebCTPReqRiskSettleProductStatus(WebCTPRequest):
    RiskSettleProductStatus: RiskSettleProductStatusField = Field(
        title="风险品种")


class SyncDeltaInfoField(BaseModel):
    """风险结算追平信息"""

    SyncDeltaSequenceNo: int = Field(0, title="追平序号")
    SyncDeltaStatus: str = Field("", title="追平状态")
    SyncDescription: str = Field("", title="追平描述")
    IsOnlyTrdDelta: int = Field(0, title="是否只有资金追平")


class WebCTPReqSyncDeltaInfo(WebCTPRequest):
    SyncDeltaInfo: SyncDeltaInfoField = Field(title="风险结算追平信息")


class SyncDeltaProductStatusField(BaseModel):
    """风险结算追平产品信息"""

    SyncDeltaSequenceNo: int = Field(0, title="追平序号")
    ExchangeID: str = Field("", title="交易所代码")
    ProductID: str = Field("", title="产品代码")
    ProductStatus: str = Field("", title="是否允许交易")


class WebCTPReqSyncDeltaProductStatus(WebCTPRequest):
    SyncDeltaProductStatus: SyncDeltaProductStatusField = Field(
        title="风险结算追平产品信息")


class SyncDeltaInvstPosDtlField(BaseModel):
    """风险结算追平持仓明细"""

    InstrumentID: str = Field("", title="合约代码")
    BrokerID: str = Field("", title="经纪公司代码")
    InvestorID: str = Field("", title="投资者代码")
    HedgeFlag: str = Field("", title="投机套保标志")
    Direction: str = Field("", title="买卖")
    OpenDate: str = Field("", title="开仓日期")
    TradeID: str = Field("", title="成交编号")
    Volume: int = Field(0, title="数量")
    OpenPrice: float = Field(0.0, title="开仓价")
    TradingDay: str = Field("", title="交易日")
    SettlementID: int = Field(0, title="结算编号")
    TradeType: str = Field("", title="成交类型")
    CombInstrumentID: str = Field("", title="组合合约代码")
    ExchangeID: str = Field("", title="交易所代码")
    CloseProfitByDate: float = Field(0.0, title="逐日盯市平仓盈亏")
    CloseProfitByTrade: float = Field(0.0, title="逐笔对冲平仓盈亏")
    PositionProfitByDate: float = Field(0.0, title="逐日盯市持仓盈亏")
    PositionProfitByTrade: float = Field(0.0, title="逐笔对冲持仓盈亏")
    Margin: float = Field(0.0, title="投资者保证金")
    ExchMargin: float = Field(0.0, title="交易所保证金")
    MarginRateByMoney: float = Field(0.0, title="保证金率")
    MarginRateByVolume: float = Field(0.0, title="保证金率(按手数)")
    LastSettlementPrice: float = Field(0.0, title="昨结算价")
    SettlementPrice: float = Field(0.0, title="结算价")
    CloseVolume: int = Field(0, title="平仓量")
    CloseAmount: float = Field(0.0, title="平仓金额")
    TimeFirstVolume: int = Field(0, title="先开先平剩余数量")
    SpecPosiType: str = Field("", title="特殊持仓标志")
    ActionDirection: str = Field("", title="操作标志")
    SyncDeltaSequenceNo: int = Field(0, title="追平序号")


class WebCTPReqSyncDeltaInvstPosDtl(WebCTPRequest):
    SyncDeltaInvstPosDtl: SyncDeltaInvstPosDtlField = Field(
        title="风险结算追平持仓明细")


class SyncDeltaInvstPosCombDtlField(BaseModel):
    """风险结算追平组合持仓明细"""

    TradingDay: str = Field("", title="交易日")
    OpenDate: str = Field("", title="开仓日期")
    ExchangeID: str = Field("", title="交易所代码")
    SettlementID: int = Field(0, title="结算编号")
    BrokerID: str = Field("", title="经纪公司代码")
    InvestorID: str = Field("", title="投资者代码")
    ComTradeID: str = Field("", title="组合编号")
    TradeID: str = Field("", title="撮合编号")
    InstrumentID: str = Field("", title="合约代码")
    HedgeFlag: str = Field("", title="投机套保标志")
    Direction: str = Field("", title="买卖")
    TotalAmt: int = Field(0, title="持仓量")
    Margin: float = Field(0.0, title="投资者保证金")
    ExchMargin: float = Field(0.0, title="交易所保证金")
    MarginRateByMoney: float = Field(0.0, title="保证金率")
    MarginRateByVolume: float = Field(0.0, title="保证金率(按手数)")
    LegID: int = Field(0, title="单腿编号")
    LegMultiple: int = Field(0, title="单腿乘数")
    TradeGroupID: int = Field(0, title="成交组号")
    ActionDirection: str = Field("", title="操作标志")
    SyncDeltaSequenceNo: int = Field(0, title="追平序号")


class WebCTPReqSyncDeltaInvstPosCombDtl(WebCTPRequest):
    SyncDeltaInvstPosCombDtl: SyncDeltaInvstPosCombDtlField = Field(
        title="风险结算追平组合持仓明细")


class SyncDeltaTradingAccountField(BaseModel):
    """风险结算追平资金"""

    BrokerID: str = Field("", title="经纪公司代码")
    AccountID: str = Field("", title="投资者帐号")
    PreMortgage: float = Field(0.0, title="上次质押金额")
    PreCredit: float = Field(0.0, title="上次信用额度")
    PreDeposit: float = Field(0.0, title="上次存款额")
    PreBalance: float = Field(0.0, title="上次结算准备金")
    PreMargin: float = Field(0.0, title="上次占用的保证金")
    InterestBase: float = Field(0.0, title="利息基数")
    Interest: float = Field(0.0, title="利息收入")
    Deposit: float = Field(0.0, title="入金金额")
    Withdraw: float = Field(0.0, title="出金金额")
    FrozenMargin: float = Field(0.0, title="冻结的保证金")
    FrozenCash: float = Field(0.0, title="冻结的资金")
    FrozenCommission: float = Field(0.0, title="冻结的手续费")
    CurrMargin: float = Field(0.0, title="当前保证金总额")
    CashIn: float = Field(0.0, title="资金差额")
    Commission: float = Field(0.0, title="手续费")
    CloseProfit: float = Field(0.0, title="平仓盈亏")
    PositionProfit: float = Field(0.0, title="持仓盈亏")
    Balance: float = Field(0.0, title="期货结算准备金")
    Available: float = Field(0.0, title="可用资金")
    WithdrawQuota: float = Field(0.0, title="可取资金")
    Reserve: float = Field(0.0, title="基本准备金")
    TradingDay: str = Field("", title="交易日")
    SettlementID: int = Field(0, title="结算编号")
    Credit: float = Field(0.0, title="信用额度")
    Mortgage: float = Field(0.0, title="质押金额")
    ExchangeMargin: float = Field(0.0, title="交易所保证金")
    DeliveryMargin: float = Field(0.0, title="投资者交割保证金")
    ExchangeDeliveryMargin: float = Field(0.0, title="交易所交割保证金")
    ReserveBalance: float = Field(0.0, title="保底期货结算准备金")
    CurrencyID: str = Field("", title="币种代码")
    PreFundMortgageIn: float = Field(0.0, title="上次货币质入金额")
    PreFundMortgageOut: float = Field(0.0, title="上次货币质出金额")
    FundMortgageIn: float = Field(0.0, title="货币质入金额")
    FundMortgageOut: float = Field(0.0, title="货币质出金额")
    FundMortgageAvailable: float = Field(0.0, title="货币质押余额")
    MortgageableFund: float = Field(0.0, title="可质押货币金额")
    SpecProductMargin: float = Field(0.0, title="特殊产品占用保证金")
    SpecProductFrozenMargin: float = Field(0.0, title="特殊产品冻结保证金")
    SpecProductCommission: float = Field(0.0, title="特殊产品手续费")
    SpecProductFrozenCommission: float = Field(0.0, title="特殊产品冻结手续费")
    SpecProductPositionProfit: float = Field(0.0, title="特殊产品持仓盈亏")
    SpecProductCloseProfit: float = Field(0.0, title="特殊产品平仓盈亏")
    SpecProductPositionProfitByAlg: float = Field(0.0,
                                                  title="根据持仓盈亏算法计算的特殊产品持仓盈亏")
    SpecProductExchangeMargin: float = Field(0.0, title="特殊产品交易所保证金")
    FrozenSwap: float = Field(0.0, title="延时换汇冻结金额")
    RemainSwap: float = Field(0.0, title="剩余换汇额度")
    SyncDeltaSequenceNo: int = Field(0, title="追平序号")


class WebCTPReqSyncDeltaTradingAccount(WebCTPRequest):
    SyncDeltaTradingAccount: SyncDeltaTradingAccountField = Field(
        title="风险结算追平资金")


class SyncDeltaInitInvstMarginField(BaseModel):
    """投资者风险结算总保证金"""

    BrokerID: str = Field("", title="经纪公司代码")
    InvestorID: str = Field("", title="投资者代码")
    LastRiskTotalInvstMargin: float = Field(0.0, title="追平前总风险保证金")
    LastRiskTotalExchMargin: float = Field(0.0,
                                           title="追平前交易所总风险保证金")
    ThisSyncInvstMargin: float = Field(0.0, title="本次追平品种总保证金")
    ThisSyncExchMargin: float = Field(0.0, title="本次追平品种交易所总保证金")
    RemainRiskInvstMargin: float = Field(0.0, title="本次未追平品种总保证金")
    RemainRiskExchMargin: float = Field(0.0,
                                        title="本次未追平品种交易所总保证金")
    LastRiskSpecTotalInvstMargin: float = Field(0.0,
                                                title="追平前总特殊产品风险保证金")
    LastRiskSpecTotalExchMargin: float = Field(0.0,
                                               title="追平前总特殊产品交易所风险保证金")
    ThisSyncSpecInvstMargin: float = Field(0.0,
                                           title="本次追平品种特殊产品总保证金")
    ThisSyncSpecExchMargin: float = Field(0.0,
                                          title="本次追平品种特殊产品交易所总保证金")
    RemainRiskSpecInvstMargin: float = Field(0.0,
                                             title="本次未追平品种特殊产品总保证金")
    RemainRiskSpecExchMargin: float = Field(0.0,
                                            title="本次未追平品种特殊产品交易所总保证金")
    SyncDeltaSequenceNo: int = Field(0, title="追平序号")


class WebCTPReqSyncDeltaInitInvstMargin(WebCTPRequest):
    SyncDeltaInitInvstMargin: SyncDeltaInitInvstMarginField = Field(
        title="投资者风险结算总保证金")


class SyncDeltaDceCombInstrumentField(BaseModel):
    """风险结算追平组合优先级"""

    CombInstrumentID: str = Field("", title="合约代码")
    ExchangeID: str = Field("", title="交易所代码")
    ExchangeInstID: str = Field("", title="合约在交易所的代码")
    TradeGroupID: int = Field(0, title="成交组号")
    CombHedgeFlag: str = Field("", title="投机套保标志")
    CombinationType: str = Field("", title="组合类型")
    Direction: str = Field("", title="买卖")
    ProductID: str = Field("", title="产品代码")
    Xparameter: float = Field(0.0, title="期权组合保证金比例")
    ActionDirection: str = Field("", title="操作标志")
    SyncDeltaSequenceNo: int = Field(0, title="追平序号")


class WebCTPReqSyncDeltaDceCombInstrument(WebCTPRequest):
    SyncDeltaDceCombInstrument: SyncDeltaDceCombInstrumentField = Field(
        title="风险结算追平组合优先级")


class SyncDeltaInvstMarginRateField(BaseModel):
    """风险结算追平投资者期货保证金率"""

    InstrumentID: str = Field("", title="合约代码")
    InvestorRange: str = Field("", title="投资者范围")
    BrokerID: str = Field("", title="经纪公司代码")
    InvestorID: str = Field("", title="投资者代码")
    HedgeFlag: str = Field("", title="投机套保标志")
    LongMarginRatioByMoney: float = Field(0.0, title="多头保证金率")
    LongMarginRatioByVolume: float = Field(0.0, title="多头保证金费")
    ShortMarginRatioByMoney: float = Field(0.0, title="空头保证金率")
    ShortMarginRatioByVolume: float = Field(0.0, title="空头保证金费")
    IsRelative: int = Field(0, title="是否相对交易所收取")
    ActionDirection: str = Field("", title="操作标志")
    SyncDeltaSequenceNo: int = Field(0, title="追平序号")


class WebCTPReqSyncDeltaInvstMarginRate(WebCTPRequest):
    SyncDeltaInvstMarginRate: SyncDeltaInvstMarginRateField = Field(
        title="风险结算追平投资者期货保证金率")


class SyncDeltaExchMarginRateField(BaseModel):
    """风险结算追平交易所期货保证金率"""

    BrokerID: str = Field("", title="经纪公司代码")
    InstrumentID: str = Field("", title="合约代码")
    HedgeFlag: str = Field("", title="投机套保标志")
    LongMarginRatioByMoney: float = Field(0.0, title="多头保证金率")
    LongMarginRatioByVolume: float = Field(0.0, title="多头保证金费")
    ShortMarginRatioByMoney: float = Field(0.0, title="空头保证金率")
    ShortMarginRatioByVolume: float = Field(0.0, title="空头保证金费")
    ActionDirection: str = Field("", title="操作标志")
    SyncDeltaSequenceNo: int = Field(0, title="追平序号")


class WebCTPReqSyncDeltaExchMarginRate(WebCTPRequest):
    SyncDeltaExchMarginRate: SyncDeltaExchMarginRateField = Field(
        title="风险结算追平交易所期货保证金率")


class SyncDeltaOptExchMarginField(BaseModel):
    """风险结算追平中金现货期权交易所保证金率"""

    BrokerID: str = Field("", title="经纪公司代码")
    InstrumentID: str = Field("", title="合约代码")
    SShortMarginRatioByMoney: float = Field(0.0,
                                            title="投机空头保证金调整系数")
    SShortMarginRatioByVolume: float = Field(0.0,
                                             title="投机空头保证金调整系数")
    HShortMarginRatioByMoney: float = Field(0.0,
                                            title="保值空头保证金调整系数")
    HShortMarginRatioByVolume: float = Field(0.0,
                                             title="保值空头保证金调整系数")
    AShortMarginRatioByMoney: float = Field(0.0,
                                            title="套利空头保证金调整系数")
    AShortMarginRatioByVolume: float = Field(0.0,
                                             title="套利空头保证金调整系数")
    MShortMarginRatioByMoney: float = Field(0.0,
                                            title="做市商空头保证金调整系数")
    MShortMarginRatioByVolume: float = Field(0.0,
                                             title="做市商空头保证金调整系数")
    ActionDirection: str = Field("", title="操作标志")
    SyncDeltaSequenceNo: int = Field(0, title="追平序号")


class WebCTPReqSyncDeltaOptExchMargin(WebCTPRequest):
    SyncDeltaOptExchMargin: SyncDeltaOptExchMarginField = Field(
        title="风险结算追平中金现货期权交易所保证金率")


class SyncDeltaOptInvstMarginField(BaseModel):
    """风险结算追平中金现货期权投资者保证金率"""

    InstrumentID: str = Field("", title="合约代码")
    InvestorRange: str = Field("", title="投资者范围")
    BrokerID: str = Field("", title="经纪公司代码")
    InvestorID: str = Field("", title="投资者代码")
    SShortMarginRatioByMoney: float = Field(0.0,
                                            title="投机空头保证金调整系数")
    SShortMarginRatioByVolume: float = Field(0.0,
                                             title="投机空头保证金调整系数")
    HShortMarginRatioByMoney: float = Field(0.0,
                                            title="保值空头保证金调整系数")
    HShortMarginRatioByVolume: float = Field(0.0,
                                             title="保值空头保证金调整系数")
    AShortMarginRatioByMoney: float = Field(0.0,
                                            title="套利空头保证金调整系数")
    AShortMarginRatioByVolume: float = Field(0.0,
                                             title="套利空头保证金调整系数")
    IsRelative: int = Field(0, title="是否跟随交易所收取")
    MShortMarginRatioByMoney: float = Field(0.0,
                                            title="做市商空头保证金调整系数")
    MShortMarginRatioByVolume: float = Field(0.0,
                                             title="做市商空头保证金调整系数")
    ActionDirection: str = Field("", title="操作标志")
    SyncDeltaSequenceNo: int = Field(0, title="追平序号")


class WebCTPReqSyncDeltaOptInvstMargin(WebCTPRequest):
    SyncDeltaOptInvstMargin: SyncDeltaOptInvstMarginField = Field(
        title="风险结算追平中金现货期权投资者保证金率")


class SyncDeltaInvstMarginRateULField(BaseModel):
    """风险结算追平期权标的调整保证金率"""

    InstrumentID: str = Field("", title="合约代码")
    InvestorRange: str = Field("", title="投资者范围")
    BrokerID: str = Field("", title="经纪公司代码")
    InvestorID: str = Field("", title="投资者代码")
    HedgeFlag: str = Field("", title="投机套保标志")
    LongMarginRatioByMoney: float = Field(0.0, title="多头保证金率")
    LongMarginRatioByVolume: float = Field(0.0, title="多头保证金费")
    ShortMarginRatioByMoney: float = Field(0.0, title="空头保证金率")
    ShortMarginRatioByVolume: float = Field(0.0, title="空头保证金费")
    ActionDirection: str = Field("", title="操作标志")
    SyncDeltaSequenceNo: int = Field(0, title="追平序号")


class WebCTPReqSyncDeltaInvstMarginRateUL(WebCTPRequest):
    SyncDeltaInvstMarginRateUL: SyncDeltaInvstMarginRateULField = Field(
        title="风险结算追平期权标的调整保证金率")


class SyncDeltaOptInvstCommRateField(BaseModel):
    """风险结算追平期权手续费率"""

    InstrumentID: str = Field("", title="合约代码")
    InvestorRange: str = Field("", title="投资者范围")
    BrokerID: str = Field("", title="经纪公司代码")
    InvestorID: str = Field("", title="投资者代码")
    OpenRatioByMoney: float = Field(0.0, title="开仓手续费率")
    OpenRatioByVolume: float = Field(0.0, title="开仓手续费")
    CloseRatioByMoney: float = Field(0.0, title="平仓手续费率")
    CloseRatioByVolume: float = Field(0.0, title="平仓手续费")
    CloseTodayRatioByMoney: float = Field(0.0, title="平今手续费率")
    CloseTodayRatioByVolume: float = Field(0.0, title="平今手续费")
    StrikeRatioByMoney: float = Field(0.0, title="执行手续费率")
    StrikeRatioByVolume: float = Field(0.0, title="执行手续费")
    ActionDirection: str = Field("", title="操作标志")
    SyncDeltaSequenceNo: int = Field(0, title="追平序号")


class WebCTPReqSyncDeltaOptInvstCommRate(WebCTPRequest):
    SyncDeltaOptInvstCommRate: SyncDeltaOptInvstCommRateField = Field(
        title="风险结算追平期权手续费率")


class SyncDeltaInvstCommRateField(BaseModel):
    """风险结算追平期货手续费率"""

    InstrumentID: str = Field("", title="合约代码")
    InvestorRange: str = Field("", title="投资者范围")
    BrokerID: str = Field("", title="经纪公司代码")
    InvestorID: str = Field("", title="投资者代码")
    OpenRatioByMoney: float = Field(0.0, title="开仓手续费率")
    OpenRatioByVolume: float = Field(0.0, title="开仓手续费")
    CloseRatioByMoney: float = Field(0.0, title="平仓手续费率")
    CloseRatioByVolume: float = Field(0.0, title="平仓手续费")
    CloseTodayRatioByMoney: float = Field(0.0, title="平今手续费率")
    CloseTodayRatioByVolume: float = Field(0.0, title="平今手续费")
    ActionDirection: str = Field("", title="操作标志")
    SyncDeltaSequenceNo: int = Field(0, title="追平序号")


class WebCTPReqSyncDeltaInvstCommRate(WebCTPRequest):
    SyncDeltaInvstCommRate: SyncDeltaInvstCommRateField = Field(
        title="风险结算追平期货手续费率")


class SyncDeltaProductExchRateField(BaseModel):
    """风险结算追平交叉汇率"""

    ProductID: str = Field("", title="产品代码")
    QuoteCurrencyID: str = Field("", title="报价币种类型")
    ExchangeRate: float = Field(0.0, title="汇率")
    ActionDirection: str = Field("", title="操作标志")
    SyncDeltaSequenceNo: int = Field(0, title="追平序号")


class WebCTPReqSyncDeltaProductExchRate(WebCTPRequest):
    SyncDeltaProductExchRate: SyncDeltaProductExchRateField = Field(
        title="风险结算追平交叉汇率")


class SyncDeltaDepthMarketDataField(BaseModel):
    """风险结算追平行情"""

    TradingDay: str = Field("", title="交易日")
    InstrumentID: str = Field("", title="合约代码")
    ExchangeID: str = Field("", title="交易所代码")
    ExchangeInstID: str = Field("", title="合约在交易所的代码")
    LastPrice: float = Field(0.0, title="最新价")
    PreSettlementPrice: float = Field(0.0, title="上次结算价")
    PreClosePrice: float = Field(0.0, title="昨收盘")
    PreOpenInterest: float = Field(0.0, title="昨持仓量")
    OpenPrice: float = Field(0.0, title="今开盘")
    HighestPrice: float = Field(0.0, title="最高价")
    LowestPrice: float = Field(0.0, title="最低价")
    Volume: int = Field(0, title="数量")
    Turnover: float = Field(0.0, title="成交金额")
    OpenInterest: float = Field(0.0, title="持仓量")
    ClosePrice: float = Field(0.0, title="今收盘")
    SettlementPrice: float = Field(0.0, title="本次结算价")
    UpperLimitPrice: float = Field(0.0, title="涨停板价")
    LowerLimitPrice: float = Field(0.0, title="跌停板价")
    PreDelta: float = Field(0.0, title="昨虚实度")
    CurrDelta: float = Field(0.0, title="今虚实度")
    UpdateTime: str = Field("", title="最后修改时间")
    UpdateMillisec: int = Field(0, title="最后修改毫秒")
    BidPrice1: float = Field(0.0, title="申买价一")
    BidVolume1: int = Field(0, title="申买量一")
    AskPrice1: float = Field(0.0, title="申卖价一")
    AskVolume1: int = Field(0, title="申卖量一")
    BidPrice2: float = Field(0.0, title="申买价二")
    BidVolume2: int = Field(0, title="申买量二")
    AskPrice2: float = Field(0.0, title="申卖价二")
    AskVolume2: int = Field(0, title="申卖量二")
    BidPrice3: float = Field(0.0, title="申买价三")
    BidVolume3: int = Field(0, title="申买量三")
    AskPrice3: float = Field(0.0, title="申卖价三")
    AskVolume3: int = Field(0, title="申卖量三")
    BidPrice4: float = Field(0.0, title="申买价四")
    BidVolume4: int = Field(0, title="申买量四")
    AskPrice4: float = Field(0.0, title="申卖价四")
    AskVolume4: int = Field(0, title="申卖量四")
    BidPrice5: float = Field(0.0, title="申买价五")
    BidVolume5: int = Field(0, title="申买量五")
    AskPrice5: float = Field(0.0, title="申卖价五")
    AskVolume5: int = Field(0, title="申卖量五")
    AveragePrice: float = Field(0.0, title="当日均价")
    ActionDay: str = Field("", title="业务日期")
    BandingUpperPrice: float = Field(0.0, title="上带价")
    BandingLowerPrice: float = Field(0.0, title="下带价")
    ActionDirection: str = Field("", title="操作标志")
    SyncDeltaSequenceNo: int = Field(0, title="追平序号")


class WebCTPReqSyncDeltaDepthMarketData(WebCTPRequest):
    SyncDeltaDepthMarketData: SyncDeltaDepthMarketDataField = Field(
        title="风险结算追平行情")


class SyncDeltaIndexPriceField(BaseModel):
    """风险结算追平现货指数"""

    BrokerID: str = Field("", title="经纪公司代码")
    InstrumentID: str = Field("", title="合约代码")
    ClosePrice: float = Field(0.0, title="指数现货收盘价")
    ActionDirection: str = Field("", title="操作标志")
    SyncDeltaSequenceNo: int = Field(0, title="追平序号")


class WebCTPReqSyncDeltaIndexPrice(WebCTPRequest):
    SyncDeltaIndexPrice: SyncDeltaIndexPriceField = Field(
        title="风险结算追平现货指数")


class SyncDeltaEWarrantOffsetField(BaseModel):
    """风险结算追平仓单折抵"""

    TradingDay: str = Field("", title="交易日期")
    BrokerID: str = Field("", title="经纪公司代码")
    InvestorID: str = Field("", title="投资者代码")
    ExchangeID: str = Field("", title="交易所代码")
    InstrumentID: str = Field("", title="合约代码")
    Direction: str = Field("", title="买卖方向")
    HedgeFlag: str = Field("", title="投机套保标志")
    Volume: int = Field(0, title="数量")
    ActionDirection: str = Field("", title="操作标志")
    SyncDeltaSequenceNo: int = Field(0, title="追平序号")


class WebCTPReqSyncDeltaEWarrantOffset(WebCTPRequest):
    SyncDeltaEWarrantOffset: SyncDeltaEWarrantOffsetField = Field(
        title="风险结算追平仓单折抵")


class ReqUserLoginSCField(BaseModel):
    """国密用户登录请求"""

    TradingDay: str = Field("", title="交易日")
    BrokerID: str = Field("", title="经纪公司代码")
    UserID: str = Field("", title="用户代码")
    Password: str = Field("", title="密码")
    UserProductInfo: str = Field("", title="用户端产品信息")
    InterfaceProductInfo: str = Field("", title="接口端产品信息")
    ProtocolInfo: str = Field("", title="协议信息")
    MacAddress: str = Field("", title="Mac地址")
    OneTimePassword: str = Field("", title="动态密码")
    ClientIPAddress: str = Field("", title="终端IP地址")
    LoginRemark: str = Field("", title="登录备注")
    ClientIPPort: int = Field(0, title="终端IP端口")
    AuthCode: str = Field("", title="认证码")
    AppID: str = Field("", title="App代码")


class WebCTPReqUserLoginSC(WebCTPRequest):
    ReqUserLoginSC: ReqUserLoginSCField = Field(title="国密用户登录请求")


class SPBMFutureParameterField(BaseModel):
    """SPBM期货合约保证金参数"""

    TradingDay: str = Field("", title="交易日")
    ExchangeID: str = Field("", title="交易所代码")
    InstrumentID: str = Field("", title="合约代码")
    ProdFamilyCode: str = Field("", title="品种代码")
    Cvf: int = Field(0, title="期货合约因子")
    TimeRange: str = Field("", title="阶段标识")
    MarginRate: float = Field(0.0, title="品种保证金标准")
    LockRateX: float = Field(0.0, title="期货合约内部对锁仓费率折扣比例")
    AddOnRate: float = Field(0.0, title="提高保证金标准")
    PreSettlementPrice: float = Field(0.0, title="昨结算价")
    AddOnLockRateX2: float = Field(0.0,
                                   title="期货合约内部对锁仓附加费率折扣比例")


class WebCTPReqSPBMFutureParameter(WebCTPRequest):
    SPBMFutureParameter: SPBMFutureParameterField = Field(
        title="SPBM期货合约保证金参数")


class SPBMOptionParameterField(BaseModel):
    """SPBM期权合约保证金参数"""

    TradingDay: str = Field("", title="交易日")
    ExchangeID: str = Field("", title="交易所代码")
    InstrumentID: str = Field("", title="合约代码")
    ProdFamilyCode: str = Field("", title="品种代码")
    Cvf: int = Field(0, title="期权合约因子")
    DownPrice: float = Field(0.0, title="期权冲抵价格")
    Delta: float = Field(0.0, title="Delta值")
    SlimiDelta: float = Field(0.0, title="卖方期权风险转换最低值")
    PreSettlementPrice: float = Field(0.0, title="昨结算价")


class WebCTPReqSPBMOptionParameter(WebCTPRequest):
    SPBMOptionParameter: SPBMOptionParameterField = Field(
        title="SPBM期权合约保证金参数")


class SPBMIntraParameterField(BaseModel):
    """SPBM品种内对锁仓折扣参数"""

    TradingDay: str = Field("", title="交易日")
    ExchangeID: str = Field("", title="交易所代码")
    ProdFamilyCode: str = Field("", title="品种代码")
    IntraRateY: float = Field(0.0, title="品种内合约间对锁仓费率折扣比例")
    AddOnIntraRateY2: float = Field(0.0,
                                    title="品种内合约间对锁仓附加费率折扣比例")


class WebCTPReqSPBMIntraParameter(WebCTPRequest):
    SPBMIntraParameter: SPBMIntraParameterField = Field(
        title="SPBM品种内对锁仓折扣参数")


class SPBMInterParameterField(BaseModel):
    """SPBM跨品种抵扣参数"""

    TradingDay: str = Field("", title="交易日")
    ExchangeID: str = Field("", title="交易所代码")
    SpreadId: int = Field(0, title="优先级")
    InterRateZ: float = Field(0.0, title="品种间对锁仓费率折扣比例")
    Leg1ProdFamilyCode: str = Field("", title="第一腿构成品种")
    Leg2ProdFamilyCode: str = Field("", title="第二腿构成品种")


class WebCTPReqSPBMInterParameter(WebCTPRequest):
    SPBMInterParameter: SPBMInterParameterField = Field(
        title="SPBM跨品种抵扣参数")


class SyncSPBMParameterEndField(BaseModel):
    """同步SPBM参数结束"""

    TradingDay: str = Field("", title="交易日")


class WebCTPReqSyncSPBMParameterEnd(WebCTPRequest):
    SyncSPBMParameterEnd: SyncSPBMParameterEndField = Field(
        title="同步SPBM参数结束")


class QrySPBMFutureParameterField(BaseModel):
    """SPBM期货合约保证金参数查询"""

    ExchangeID: str = Field("", title="交易所代码")
    InstrumentID: str = Field("", title="合约代码")
    ProdFamilyCode: str = Field("", title="品种代码")


class WebCTPReqQrySPBMFutureParameter(WebCTPRequest):
    QrySPBMFutureParameter: QrySPBMFutureParameterField = Field(
        title="SPBM期货合约保证金参数查询")


class QrySPBMOptionParameterField(BaseModel):
    """SPBM期权合约保证金参数查询"""

    ExchangeID: str = Field("", title="交易所代码")
    InstrumentID: str = Field("", title="合约代码")
    ProdFamilyCode: str = Field("", title="品种代码")


class WebCTPReqQrySPBMOptionParameter(WebCTPRequest):
    QrySPBMOptionParameter: QrySPBMOptionParameterField = Field(
        title="SPBM期权合约保证金参数查询")


class QrySPBMIntraParameterField(BaseModel):
    """SPBM品种内对锁仓折扣参数查询"""

    ExchangeID: str = Field("", title="交易所代码")
    ProdFamilyCode: str = Field("", title="品种代码")


class WebCTPReqQrySPBMIntraParameter(WebCTPRequest):
    QrySPBMIntraParameter: QrySPBMIntraParameterField = Field(
        title="SPBM品种内对锁仓折扣参数查询")


class QrySPBMInterParameterField(BaseModel):
    """SPBM跨品种抵扣参数查询"""

    ExchangeID: str = Field("", title="交易所代码")
    Leg1ProdFamilyCode: str = Field("", title="第一腿构成品种")
    Leg2ProdFamilyCode: str = Field("", title="第二腿构成品种")


class WebCTPReqQrySPBMInterParameter(WebCTPRequest):
    QrySPBMInterParameter: QrySPBMInterParameterField = Field(
        title="SPBM跨品种抵扣参数查询")


class SPBMPortfDefinitionField(BaseModel):
    """组合保证金套餐"""

    ExchangeID: str = Field("", title="交易所代码")
    PortfolioDefID: int = Field(0, title="组合保证金套餐代码")
    ProdFamilyCode: str = Field("", title="品种代码")
    IsSPBM: int = Field(0, title="是否启用SPBM")


class WebCTPReqSPBMPortfDefinition(WebCTPRequest):
    SPBMPortfDefinition: SPBMPortfDefinitionField = Field(
        title="组合保证金套餐")


class SPBMInvestorPortfDefField(BaseModel):
    """投资者套餐选择"""

    ExchangeID: str = Field("", title="交易所代码")
    BrokerID: str = Field("", title="经纪公司代码")
    InvestorID: str = Field("", title="投资者代码")
    PortfolioDefID: int = Field(0, title="组合保证金套餐代码")


class WebCTPReqSPBMInvestorPortfDef(WebCTPRequest):
    SPBMInvestorPortfDef: SPBMInvestorPortfDefField = Field(
        title="投资者套餐选择")


class InvestorPortfMarginRatioField(BaseModel):
    """投资者新型组合保证金系数"""

    InvestorRange: str = Field("", title="投资者范围")
    BrokerID: str = Field("", title="经纪公司代码")
    InvestorID: str = Field("", title="投资者代码")
    ExchangeID: str = Field("", title="交易所代码")
    MarginRatio: float = Field(0.0,
                               title="会员对投资者收取的保证金和交易所对投资者收取的保证金的比例")


class WebCTPReqInvestorPortfMarginRatio(WebCTPRequest):
    InvestorPortfMarginRatio: InvestorPortfMarginRatioField = Field(
        title="投资者新型组合保证金系数")


class QrySPBMPortfDefinitionField(BaseModel):
    """组合保证金套餐查询"""

    ExchangeID: str = Field("", title="交易所代码")
    PortfolioDefID: int = Field(0, title="组合保证金套餐代码")
    ProdFamilyCode: str = Field("", title="品种代码")


class WebCTPReqQrySPBMPortfDefinition(WebCTPRequest):
    QrySPBMPortfDefinition: QrySPBMPortfDefinitionField = Field(
        title="组合保证金套餐查询")


class QrySPBMInvestorPortfDefField(BaseModel):
    """投资者套餐选择查询"""

    ExchangeID: str = Field("", title="交易所代码")
    BrokerID: str = Field("", title="经纪公司代码")
    InvestorID: str = Field("", title="投资者代码")


class WebCTPReqQrySPBMInvestorPortfDef(WebCTPRequest):
    QrySPBMInvestorPortfDef: QrySPBMInvestorPortfDefField = Field(
        title="投资者套餐选择查询")


class QryInvestorPortfMarginRatioField(BaseModel):
    """投资者新型组合保证金系数查询"""

    BrokerID: str = Field("", title="经纪公司代码")
    InvestorID: str = Field("", title="投资者代码")
    ExchangeID: str = Field("", title="交易所代码")


class WebCTPReqQryInvestorPortfMarginRatio(WebCTPRequest):
    QryInvestorPortfMarginRatio: QryInvestorPortfMarginRatioField = Field(
        title="投资者新型组合保证金系数查询")


class InvestorProdSPBMDetailField(BaseModel):
    """投资者产品SPBM明细"""

    ExchangeID: str = Field("", title="交易所代码")
    BrokerID: str = Field("", title="经纪公司代码")
    InvestorID: str = Field("", title="投资者代码")
    ProdFamilyCode: str = Field("", title="品种代码")
    IntraInstrMargin: float = Field(0.0, title="合约内对锁保证金")
    BCollectingMargin: float = Field(0.0, title="买归集保证金")
    SCollectingMargin: float = Field(0.0, title="卖归集保证金")
    IntraProdMargin: float = Field(0.0, title="品种内合约间对锁保证金")
    NetMargin: float = Field(0.0, title="净保证金")
    InterProdMargin: float = Field(0.0, title="产品间对锁保证金")
    SingleMargin: float = Field(0.0, title="裸保证金")
    AddOnMargin: float = Field(0.0, title="附加保证金")
    DeliveryMargin: float = Field(0.0, title="交割月保证金")
    CallOptionMinRisk: float = Field(0.0, title="看涨期权最低风险")
    PutOptionMinRisk: float = Field(0.0, title="看跌期权最低风险")
    OptionMinRisk: float = Field(0.0, title="卖方期权最低风险")
    OptionValueOffset: float = Field(0.0, title="买方期权冲抵价值")
    OptionRoyalty: float = Field(0.0, title="卖方期权权利金")
    RealOptionValueOffset: float = Field(0.0, title="价值冲抵")
    Margin: float = Field(0.0, title="保证金")
    ExchMargin: float = Field(0.0, title="交易所保证金")


class WebCTPReqInvestorProdSPBMDetail(WebCTPRequest):
    InvestorProdSPBMDetail: InvestorProdSPBMDetailField = Field(
        title="投资者产品SPBM明细")


class QryInvestorProdSPBMDetailField(BaseModel):
    """投资者产品SPBM明细查询"""

    ExchangeID: str = Field("", title="交易所代码")
    BrokerID: str = Field("", title="经纪公司代码")
    InvestorID: str = Field("", title="投资者代码")
    ProdFamilyCode: str = Field("", title="品种代码")


class WebCTPReqQryInvestorProdSPBMDetail(WebCTPRequest):
    QryInvestorProdSPBMDetail: QryInvestorProdSPBMDetailField = Field(
        title="投资者产品SPBM明细查询")


class PortfTradeParamSettingField(BaseModel):
    """组保交易参数设置"""

    ExchangeID: str = Field("", title="交易所代码")
    BrokerID: str = Field("", title="经纪公司代码")
    InvestorID: str = Field("", title="投资者代码")
    Portfolio: str = Field("", title="新型组保算法")
    IsActionVerify: int = Field(0, title="撤单是否验资")
    IsCloseVerify: int = Field(0, title="平仓是否验资")


class WebCTPReqPortfTradeParamSetting(WebCTPRequest):
    PortfTradeParamSetting: PortfTradeParamSettingField = Field(
        title="组保交易参数设置")


class InvestorTradingRightField(BaseModel):
    """投资者交易权限设置"""

    BrokerID: str = Field("", title="经纪公司代码")
    InvestorID: str = Field("", title="投资者代码")
    InvstTradingRight: str = Field("", title="交易权限")


class WebCTPReqInvestorTradingRight(WebCTPRequest):
    InvestorTradingRight: InvestorTradingRightField = Field(
        title="投资者交易权限设置")


class MortgageParamField(BaseModel):
    """质押配比参数"""

    BrokerID: str = Field("", title="经纪公司代码")
    AccountID: str = Field("", title="投资者帐号")
    MortgageBalance: float = Field(0.0, title="质押配比系数")
    CheckMortgageRatio: int = Field(0, title="开仓是否验证质押配比")


class WebCTPReqMortgageParam(WebCTPRequest):
    MortgageParam: MortgageParamField = Field(title="质押配比参数")


class WithDrawParamField(BaseModel):
    """可提控制参数"""

    BrokerID: str = Field("", title="经纪公司代码")
    AccountID: str = Field("", title="投资者帐号")
    WithDrawParamID: str = Field("", title="参数代码")
    WithDrawParamValue: str = Field("", title="参数代码值")


class WebCTPReqWithDrawParam(WebCTPRequest):
    WithDrawParam: WithDrawParamField = Field(title="可提控制参数")


class ThostUserFunctionField(BaseModel):
    """Thost终端用户功能权限"""

    BrokerID: str = Field("", title="经纪公司代码")
    UserID: str = Field("", title="用户代码")
    ThostFunctionCode: int = Field(0, title="Thost终端功能代码")


class WebCTPReqThostUserFunction(WebCTPRequest):
    ThostUserFunction: ThostUserFunctionField = Field(
        title="Thost终端用户功能权限")


class QryThostUserFunctionField(BaseModel):
    """Thost终端用户功能权限查询"""

    BrokerID: str = Field("", title="经纪公司代码")
    UserID: str = Field("", title="用户代码")


class WebCTPReqQryThostUserFunction(WebCTPRequest):
    QryThostUserFunction: QryThostUserFunctionField = Field(
        title="Thost终端用户功能权限查询")


class QryInvestorCommoditySPMMMarginField(BaseModel):
    """投资者商品组SPMM记录查询"""

    BrokerID: str = Field("", title="经纪公司代码")
    InvestorID: str = Field("", title="投资者代码")
    CommodityID: str = Field("", title="商品组代码")


class WebCTPReqQryInvestorCommoditySPMMMargin(WebCTPRequest):
    QryInvestorCommoditySPMMMargin: QryInvestorCommoditySPMMMarginField = Field(
        title="投资者商品组SPMM记录查询")


class QryInvestorCommodityGroupSPMMMarginField(BaseModel):
    """投资者商品群SPMM记录查询"""

    BrokerID: str = Field("", title="经纪公司代码")
    InvestorID: str = Field("", title="投资者代码")
    CommodityGroupID: str = Field("", title="商品群代码")


class WebCTPReqQryInvestorCommodityGroupSPMMMargin(WebCTPRequest):
    QryInvestorCommodityGroupSPMMMargin: QryInvestorCommodityGroupSPMMMarginField = Field(
        title="投资者商品群SPMM记录查询")


class QrySPMMInstParamField(BaseModel):
    """SPMM合约参数查询"""

    InstrumentID: str = Field("", title="合约代码")


class WebCTPReqQrySPMMInstParam(WebCTPRequest):
    QrySPMMInstParam: QrySPMMInstParamField = Field(title="SPMM合约参数查询")


class QrySPMMProductParamField(BaseModel):
    """SPMM产品参数查询"""

    ProductID: str = Field("", title="产品代码")


class WebCTPReqQrySPMMProductParam(WebCTPRequest):
    QrySPMMProductParam: QrySPMMProductParamField = Field(
        title="SPMM产品参数查询")


class InvestorCommoditySPMMMarginField(BaseModel):
    """投资者商品组SPMM记录"""

    ExchangeID: str = Field("", title="交易所代码")
    BrokerID: str = Field("", title="经纪公司代码")
    InvestorID: str = Field("", title="投资者代码")
    CommodityID: str = Field("", title="商品组代码")
    MarginBeforeDiscount: float = Field(0.0, title="优惠仓位应收保证金")
    MarginNoDiscount: float = Field(0.0, title="不优惠仓位应收保证金")
    LongPosRisk: float = Field(0.0, title="多头实仓风险")
    LongOpenFrozenRisk: float = Field(0.0, title="多头开仓冻结风险")
    LongCloseFrozenRisk: float = Field(0.0, title="多头被平冻结风险")
    ShortPosRisk: float = Field(0.0, title="空头实仓风险")
    ShortOpenFrozenRisk: float = Field(0.0, title="空头开仓冻结风险")
    ShortCloseFrozenRisk: float = Field(0.0, title="空头被平冻结风险")
    IntraCommodityRate: float = Field(0.0, title="SPMM品种内跨期优惠系数")
    OptionDiscountRate: float = Field(0.0, title="SPMM期权优惠系数")
    PosDiscount: float = Field(0.0, title="实仓对冲优惠金额")
    OpenFrozenDiscount: float = Field(0.0, title="开仓报单对冲优惠金额")
    NetRisk: float = Field(0.0, title="品种风险净头")
    CloseFrozenMargin: float = Field(0.0, title="平仓冻结保证金")
    FrozenCommission: float = Field(0.0, title="冻结的手续费")
    Commission: float = Field(0.0, title="手续费")
    FrozenCash: float = Field(0.0, title="冻结的资金")
    CashIn: float = Field(0.0, title="资金差额")
    StrikeFrozenMargin: float = Field(0.0, title="行权冻结资金")


class WebCTPReqInvestorCommoditySPMMMargin(WebCTPRequest):
    InvestorCommoditySPMMMargin: InvestorCommoditySPMMMarginField = Field(
        title="投资者商品组SPMM记录")


class InvestorCommodityGroupSPMMMarginField(BaseModel):
    """投资者商品群SPMM记录"""

    ExchangeID: str = Field("", title="交易所代码")
    BrokerID: str = Field("", title="经纪公司代码")
    InvestorID: str = Field("", title="投资者代码")
    CommodityGroupID: str = Field("", title="商品群代码")
    MarginBeforeDiscount: float = Field(0.0, title="优惠仓位应收保证金")
    MarginNoDiscount: float = Field(0.0, title="不优惠仓位应收保证金")
    LongRisk: float = Field(0.0, title="多头风险")
    ShortRisk: float = Field(0.0, title="空头风险")
    CloseFrozenMargin: float = Field(0.0, title="商品群平仓冻结保证金")
    InterCommodityRate: float = Field(0.0, title="SPMM跨品种优惠系数")
    MiniMarginRatio: float = Field(0.0, title="商品群最小保证金比例")
    AdjustRatio: float = Field(0.0, title="投资者保证金和交易所保证金的比例")
    IntraCommodityDiscount: float = Field(0.0, title="SPMM品种内优惠汇总")
    InterCommodityDiscount: float = Field(0.0, title="SPMM跨品种优惠")
    ExchMargin: float = Field(0.0, title="交易所保证金")
    InvestorMargin: float = Field(0.0, title="投资者保证金")
    FrozenCommission: float = Field(0.0, title="冻结的手续费")
    Commission: float = Field(0.0, title="手续费")
    FrozenCash: float = Field(0.0, title="冻结的资金")
    CashIn: float = Field(0.0, title="资金差额")
    StrikeFrozenMargin: float = Field(0.0, title="行权冻结资金")


class WebCTPReqInvestorCommodityGroupSPMMMargin(WebCTPRequest):
    InvestorCommodityGroupSPMMMargin: InvestorCommodityGroupSPMMMarginField = Field(
        title="投资者商品群SPMM记录")


class SPMMInstParamField(BaseModel):
    """SPMM合约参数"""

    ExchangeID: str = Field("", title="交易所代码")
    InstrumentID: str = Field("", title="合约代码")
    InstMarginCalID: str = Field("", title="SPMM合约保证金算法")
    CommodityID: str = Field("", title="商品组代码")
    CommodityGroupID: str = Field("", title="商品群代码")


class WebCTPReqSPMMInstParam(WebCTPRequest):
    SPMMInstParam: SPMMInstParamField = Field(title="SPMM合约参数")


class SPMMProductParamField(BaseModel):
    """SPMM产品参数"""

    ExchangeID: str = Field("", title="交易所代码")
    ProductID: str = Field("", title="产品代码")
    CommodityID: str = Field("", title="商品组代码")
    CommodityGroupID: str = Field("", title="商品群代码")


class WebCTPReqSPMMProductParam(WebCTPRequest):
    SPMMProductParam: SPMMProductParamField = Field(title="SPMM产品参数")


class QryTraderAssignField(BaseModel):
    """席位与交易中心对应关系维护查询"""

    TraderID: str = Field("", title="交易员代码")


class WebCTPReqQryTraderAssign(WebCTPRequest):
    QryTraderAssign: QryTraderAssignField = Field(
        title="席位与交易中心对应关系维护查询")


class TraderAssignField(BaseModel):
    """席位与交易中心对应关系"""

    BrokerID: str = Field("", title="应用单元代码")
    ExchangeID: str = Field("", title="交易所代码")
    TraderID: str = Field("", title="交易所交易员代码")
    ParticipantID: str = Field("", title="会员代码")
    DRIdentityID: int = Field(0, title="交易中心代码")


class WebCTPReqTraderAssign(WebCTPRequest):
    TraderAssign: TraderAssignField = Field(title="席位与交易中心对应关系")


class InvestorInfoCntSettingField(BaseModel):
    """投资者申报费阶梯收取设置"""

    ExchangeID: str = Field("", title="交易所代码")
    BrokerID: str = Field("", title="经纪公司代码")
    InvestorID: str = Field("", title="投资者代码")
    ProductID: str = Field("", title="商品代码")
    IsCalInfoComm: int = Field(0, title="是否收取申报费")
    IsLimitInfoMax: int = Field(0, title="是否限制信息量")
    InfoMaxLimit: int = Field(0, title="信息量限制笔数")


class WebCTPReqInvestorInfoCntSetting(WebCTPRequest):
    InvestorInfoCntSetting: InvestorInfoCntSettingField = Field(
        title="投资者申报费阶梯收取设置")


class SPBMAddOnInterParameterField(BaseModel):
    """SPBM附加跨品种抵扣参数"""

    TradingDay: str = Field("", title="交易日")
    ExchangeID: str = Field("", title="交易所代码")
    SpreadId: int = Field(0, title="优先级")
    AddOnInterRateZ2: float = Field(0.0, title="品种间对锁仓附加费率折扣比例")
    Leg1ProdFamilyCode: str = Field("", title="第一腿构成品种")
    Leg2ProdFamilyCode: str = Field("", title="第二腿构成品种")


class WebCTPReqSPBMAddOnInterParameter(WebCTPRequest):
    SPBMAddOnInterParameter: SPBMAddOnInterParameterField = Field(
        title="SPBM附加跨品种抵扣参数")


class QrySPBMAddOnInterParameterField(BaseModel):
    """SPBM附加跨品种抵扣参数查询"""

    ExchangeID: str = Field("", title="交易所代码")
    Leg1ProdFamilyCode: str = Field("", title="第一腿构成品种")
    Leg2ProdFamilyCode: str = Field("", title="第二腿构成品种")


class WebCTPReqQrySPBMAddOnInterParameter(WebCTPRequest):
    QrySPBMAddOnInterParameter: QrySPBMAddOnInterParameterField = Field(
        title="SPBM附加跨品种抵扣参数查询")


class RCAMSCombProductInfoField(BaseModel):
    """RCAMS产品组合信息"""

    TradingDay: str = Field("", title="交易日")
    ExchangeID: str = Field("", title="交易所代码")
    ProductID: str = Field("", title="产品代码")
    CombProductID: str = Field("", title="商品组代码")
    ProductGroupID: str = Field("", title="商品群代码")


class WebCTPReqRCAMSCombProductInfo(WebCTPRequest):
    RCAMSCombProductInfo: RCAMSCombProductInfoField = Field(
        title="RCAMS产品组合信息")


class RCAMSInstrParameterField(BaseModel):
    """RCAMS同合约风险对冲参数"""

    TradingDay: str = Field("", title="交易日")
    ExchangeID: str = Field("", title="交易所代码")
    ProductID: str = Field("", title="产品代码")
    HedgeRate: float = Field(0.0, title="同合约风险对冲比率")


class WebCTPReqRCAMSInstrParameter(WebCTPRequest):
    RCAMSInstrParameter: RCAMSInstrParameterField = Field(
        title="RCAMS同合约风险对冲参数")


class RCAMSIntraParameterField(BaseModel):
    """RCAMS品种内风险对冲参数"""

    TradingDay: str = Field("", title="交易日")
    ExchangeID: str = Field("", title="交易所代码")
    CombProductID: str = Field("", title="产品组合代码")
    HedgeRate: float = Field(0.0, title="品种内对冲比率")


class WebCTPReqRCAMSIntraParameter(WebCTPRequest):
    RCAMSIntraParameter: RCAMSIntraParameterField = Field(
        title="RCAMS品种内风险对冲参数")


class RCAMSInterParameterField(BaseModel):
    """RCAMS跨品种风险折抵参数"""

    TradingDay: str = Field("", title="交易日")
    ExchangeID: str = Field("", title="交易所代码")
    ProductGroupID: str = Field("", title="商品群代码")
    Priority: int = Field(0, title="优先级")
    CreditRate: float = Field(0.0, title="折抵率")
    CombProduct1: str = Field("", title="产品组合代码1")
    CombProduct2: str = Field("", title="产品组合代码2")


class WebCTPReqRCAMSInterParameter(WebCTPRequest):
    RCAMSInterParameter: RCAMSInterParameterField = Field(
        title="RCAMS跨品种风险折抵参数")


class RCAMSShortOptAdjustParamField(BaseModel):
    """RCAMS空头期权风险调整参数"""

    TradingDay: str = Field("", title="交易日")
    ExchangeID: str = Field("", title="交易所代码")
    CombProductID: str = Field("", title="产品组合代码")
    HedgeFlag: str = Field("", title="投套标志")
    AdjustValue: float = Field(0.0, title="空头期权风险调整标准")


class WebCTPReqRCAMSShortOptAdjustParam(WebCTPRequest):
    RCAMSShortOptAdjustParam: RCAMSShortOptAdjustParamField = Field(
        title="RCAMS空头期权风险调整参数")


class RCAMSInvestorCombPositionField(BaseModel):
    """RCAMS策略组合持仓"""

    ExchangeID: str = Field("", title="交易所代码")
    BrokerID: str = Field("", title="经纪公司代码")
    InvestorID: str = Field("", title="投资者代码")
    InstrumentID: str = Field("", title="合约代码")
    HedgeFlag: str = Field("", title="投套标志")
    PosiDirection: str = Field("", title="持仓多空方向")
    CombInstrumentID: str = Field("", title="组合合约代码")
    LegID: int = Field(0, title="单腿编号")
    ExchangeInstID: str = Field("", title="交易所组合合约代码")
    TotalAmt: int = Field(0, title="持仓量")
    ExchMargin: float = Field(0.0, title="交易所保证金")
    Margin: float = Field(0.0, title="投资者保证金")


class WebCTPReqRCAMSInvestorCombPosition(WebCTPRequest):
    RCAMSInvestorCombPosition: RCAMSInvestorCombPositionField = Field(
        title="RCAMS策略组合持仓")


class InvestorProdRCAMSMarginField(BaseModel):
    """投资者品种RCAMS保证金"""

    ExchangeID: str = Field("", title="交易所代码")
    BrokerID: str = Field("", title="经纪公司代码")
    InvestorID: str = Field("", title="投资者代码")
    CombProductID: str = Field("", title="产品组合代码")
    HedgeFlag: str = Field("", title="投套标志")
    ProductGroupID: str = Field("", title="商品群代码")
    RiskBeforeDiscount: float = Field(0.0, title="品种组合前风险")
    IntraInstrRisk: float = Field(0.0, title="同合约对冲风险")
    BPosRisk: float = Field(0.0, title="品种买持仓风险")
    SPosRisk: float = Field(0.0, title="品种卖持仓风险")
    IntraProdRisk: float = Field(0.0, title="品种内对冲风险")
    NetRisk: float = Field(0.0, title="品种净持仓风险")
    InterProdRisk: float = Field(0.0, title="品种间对冲风险")
    ShortOptRiskAdj: float = Field(0.0, title="空头期权风险调整")
    OptionRoyalty: float = Field(0.0, title="空头期权权利金")
    MMSACloseFrozenMargin: float = Field(0.0, title="大边组合平仓冻结保证金")
    CloseCombFrozenMargin: float = Field(0.0, title="平策略组合冻结保证金")
    CloseFrozenMargin: float = Field(0.0, title="平仓冻结保证金")
    MMSAOpenFrozenMargin: float = Field(0.0, title="大边组合开仓冻结保证金")
    DeliveryOpenFrozenMargin: float = Field(0.0,
                                            title="交割月期货开仓冻结保证金")
    OpenFrozenMargin: float = Field(0.0, title="开仓冻结保证金")
    UseFrozenMargin: float = Field(0.0, title="投资者冻结保证金")
    MMSAExchMargin: float = Field(0.0, title="大边组合交易所持仓保证金")
    DeliveryExchMargin: float = Field(0.0, title="交割月期货交易所持仓保证金")
    CombExchMargin: float = Field(0.0, title="策略组合交易所保证金")
    ExchMargin: float = Field(0.0, title="交易所持仓保证金")
    UseMargin: float = Field(0.0, title="投资者持仓保证金")


class WebCTPReqInvestorProdRCAMSMargin(WebCTPRequest):
    InvestorProdRCAMSMargin: InvestorProdRCAMSMarginField = Field(
        title="投资者品种RCAMS保证金")


class QryRCAMSCombProductInfoField(BaseModel):
    """RCAMS产品组合信息查询"""

    ProductID: str = Field("", title="产品代码")
    CombProductID: str = Field("", title="商品组代码")
    ProductGroupID: str = Field("", title="商品群代码")


class WebCTPReqQryRCAMSCombProductInfo(WebCTPRequest):
    QryRCAMSCombProductInfo: QryRCAMSCombProductInfoField = Field(
        title="RCAMS产品组合信息查询")


class QryRCAMSInstrParameterField(BaseModel):
    """RCAMS同合约风险对冲参数查询"""

    ProductID: str = Field("", title="产品代码")


class WebCTPReqQryRCAMSInstrParameter(WebCTPRequest):
    QryRCAMSInstrParameter: QryRCAMSInstrParameterField = Field(
        title="RCAMS同合约风险对冲参数查询")


class QryRCAMSIntraParameterField(BaseModel):
    """RCAMS品种内风险对冲参数查询"""

    CombProductID: str = Field("", title="产品组合代码")


class WebCTPReqQryRCAMSIntraParameter(WebCTPRequest):
    QryRCAMSIntraParameter: QryRCAMSIntraParameterField = Field(
        title="RCAMS品种内风险对冲参数查询")


class QryRCAMSInterParameterField(BaseModel):
    """RCAMS跨品种风险折抵参数查询"""

    ProductGroupID: str = Field("", title="商品群代码")
    CombProduct1: str = Field("", title="产品组合代码1")
    CombProduct2: str = Field("", title="产品组合代码2")


class WebCTPReqQryRCAMSInterParameter(WebCTPRequest):
    QryRCAMSInterParameter: QryRCAMSInterParameterField = Field(
        title="RCAMS跨品种风险折抵参数查询")


class QryRCAMSShortOptAdjustParamField(BaseModel):
    """RCAMS空头期权风险调整参数查询"""

    CombProductID: str = Field("", title="产品组合代码")


class WebCTPReqQryRCAMSShortOptAdjustParam(WebCTPRequest):
    QryRCAMSShortOptAdjustParam: QryRCAMSShortOptAdjustParamField = Field(
        title="RCAMS空头期权风险调整参数查询")


class QryRCAMSInvestorCombPositionField(BaseModel):
    """RCAMS策略组合持仓查询"""

    BrokerID: str = Field("", title="经纪公司代码")
    InvestorID: str = Field("", title="投资者代码")
    InstrumentID: str = Field("", title="合约代码")
    CombInstrumentID: str = Field("", title="组合合约代码")


class WebCTPReqQryRCAMSInvestorCombPosition(WebCTPRequest):
    QryRCAMSInvestorCombPosition: QryRCAMSInvestorCombPositionField = Field(
        title="RCAMS策略组合持仓查询")


class QryInvestorProdRCAMSMarginField(BaseModel):
    """投资者品种RCAMS保证金查询"""

    BrokerID: str = Field("", title="经纪公司代码")
    InvestorID: str = Field("", title="投资者代码")
    CombProductID: str = Field("", title="产品组合代码")
    ProductGroupID: str = Field("", title="商品群代码")


class WebCTPReqQryInvestorProdRCAMSMargin(WebCTPRequest):
    QryInvestorProdRCAMSMargin: QryInvestorProdRCAMSMarginField = Field(
        title="投资者品种RCAMS保证金查询")


class RULEInstrParameterField(BaseModel):
    """RULE合约保证金参数"""

    TradingDay: str = Field("", title="交易日")
    ExchangeID: str = Field("", title="交易所代码")
    InstrumentID: str = Field("", title="合约代码")
    InstrumentClass: str = Field("", title="合约类型")
    StdInstrumentID: str = Field("", title="标准合约")
    BSpecRatio: float = Field(0.0, title="投机买折算系数")
    SSpecRatio: float = Field(0.0, title="投机卖折算系数")
    BHedgeRatio: float = Field(0.0, title="套保买折算系数")
    SHedgeRatio: float = Field(0.0, title="套保卖折算系数")
    BAddOnMargin: float = Field(0.0, title="买附加风险保证金")
    SAddOnMargin: float = Field(0.0, title="卖附加风险保证金")
    CommodityGroupID: int = Field(0, title="商品群号")


class WebCTPReqRULEInstrParameter(WebCTPRequest):
    RULEInstrParameter: RULEInstrParameterField = Field(
        title="RULE合约保证金参数")


class RULEIntraParameterField(BaseModel):
    """RULE品种内对锁仓折扣参数"""

    TradingDay: str = Field("", title="交易日")
    ExchangeID: str = Field("", title="交易所代码")
    ProdFamilyCode: str = Field("", title="品种代码")
    StdInstrumentID: str = Field("", title="标准合约")
    StdInstrMargin: float = Field(0.0, title="标准合约保证金")
    UsualIntraRate: float = Field(0.0, title="一般月份合约组合保证金系数")
    DeliveryIntraRate: float = Field(0.0, title="临近交割合约组合保证金系数")


class WebCTPReqRULEIntraParameter(WebCTPRequest):
    RULEIntraParameter: RULEIntraParameterField = Field(
        title="RULE品种内对锁仓折扣参数")


class RULEInterParameterField(BaseModel):
    """RULE跨品种抵扣参数"""

    TradingDay: str = Field("", title="交易日")
    ExchangeID: str = Field("", title="交易所代码")
    SpreadId: int = Field(0, title="优先级")
    InterRate: float = Field(0.0, title="品种间对锁仓费率折扣比例")
    Leg1ProdFamilyCode: str = Field("", title="第一腿构成品种")
    Leg2ProdFamilyCode: str = Field("", title="第二腿构成品种")
    Leg1PropFactor: int = Field(0, title="腿1比例系数")
    Leg2PropFactor: int = Field(0, title="腿2比例系数")
    CommodityGroupID: int = Field(0, title="商品群号")
    CommodityGroupName: str = Field("", title="商品群名称")


class WebCTPReqRULEInterParameter(WebCTPRequest):
    RULEInterParameter: RULEInterParameterField = Field(
        title="RULE跨品种抵扣参数")


class QryRULEInstrParameterField(BaseModel):
    """RULE合约保证金参数查询"""

    ExchangeID: str = Field("", title="交易所代码")
    InstrumentID: str = Field("", title="合约代码")


class WebCTPReqQryRULEInstrParameter(WebCTPRequest):
    QryRULEInstrParameter: QryRULEInstrParameterField = Field(
        title="RULE合约保证金参数查询")


class QryRULEIntraParameterField(BaseModel):
    """RULE品种内对锁仓折扣参数查询"""

    ExchangeID: str = Field("", title="交易所代码")
    ProdFamilyCode: str = Field("", title="品种代码")


class WebCTPReqQryRULEIntraParameter(WebCTPRequest):
    QryRULEIntraParameter: QryRULEIntraParameterField = Field(
        title="RULE品种内对锁仓折扣参数查询")


class QryRULEInterParameterField(BaseModel):
    """RULE跨品种抵扣参数查询"""

    ExchangeID: str = Field("", title="交易所代码")
    Leg1ProdFamilyCode: str = Field("", title="第一腿构成品种")
    Leg2ProdFamilyCode: str = Field("", title="第二腿构成品种")
    CommodityGroupID: int = Field(0, title="商品群号")


class WebCTPReqQryRULEInterParameter(WebCTPRequest):
    QryRULEInterParameter: QryRULEInterParameterField = Field(
        title="RULE跨品种抵扣参数查询")


class InvestorProdRULEMarginField(BaseModel):
    """投资者产品RULE保证金"""

    ExchangeID: str = Field("", title="交易所代码")
    BrokerID: str = Field("", title="经纪公司代码")
    InvestorID: str = Field("", title="投资者代码")
    ProdFamilyCode: str = Field("", title="品种代码")
    InstrumentClass: str = Field("", title="合约类型")
    CommodityGroupID: int = Field(0, title="商品群号")
    BStdPosition: float = Field(0.0, title="买标准持仓")
    SStdPosition: float = Field(0.0, title="卖标准持仓")
    BStdOpenFrozen: float = Field(0.0, title="买标准开仓冻结")
    SStdOpenFrozen: float = Field(0.0, title="卖标准开仓冻结")
    BStdCloseFrozen: float = Field(0.0, title="买标准平仓冻结")
    SStdCloseFrozen: float = Field(0.0, title="卖标准平仓冻结")
    IntraProdStdPosition: float = Field(0.0, title="品种内对冲标准持仓")
    NetStdPosition: float = Field(0.0, title="品种内单腿标准持仓")
    InterProdStdPosition: float = Field(0.0, title="品种间对冲标准持仓")
    SingleStdPosition: float = Field(0.0, title="单腿标准持仓")
    IntraProdMargin: float = Field(0.0, title="品种内对锁保证金")
    InterProdMargin: float = Field(0.0, title="品种间对锁保证金")
    SingleMargin: float = Field(0.0, title="跨品种单腿保证金")
    NonCombMargin: float = Field(0.0, title="非组合合约保证金")
    AddOnMargin: float = Field(0.0, title="附加保证金")
    ExchMargin: float = Field(0.0, title="交易所保证金")
    AddOnFrozenMargin: float = Field(0.0, title="附加冻结保证金")
    OpenFrozenMargin: float = Field(0.0, title="开仓冻结保证金")
    CloseFrozenMargin: float = Field(0.0, title="平仓冻结保证金")
    Margin: float = Field(0.0, title="品种保证金")
    FrozenMargin: float = Field(0.0, title="冻结保证金")


class WebCTPReqInvestorProdRULEMargin(WebCTPRequest):
    InvestorProdRULEMargin: InvestorProdRULEMarginField = Field(
        title="投资者产品RULE保证金")


class QryInvestorProdRULEMarginField(BaseModel):
    """投资者产品RULE保证金查询"""

    ExchangeID: str = Field("", title="交易所代码")
    BrokerID: str = Field("", title="经纪公司代码")
    InvestorID: str = Field("", title="投资者代码")
    ProdFamilyCode: str = Field("", title="品种代码")
    CommodityGroupID: int = Field(0, title="商品群号")


class WebCTPReqQryInvestorProdRULEMargin(WebCTPRequest):
    QryInvestorProdRULEMargin: QryInvestorProdRULEMarginField = Field(
        title="投资者产品RULE保证金查询")


class SyncDeltaSPBMPortfDefinitionField(BaseModel):
    """风险结算追平SPBM组合保证金套餐"""

    ExchangeID: str = Field("", title="交易所代码")
    PortfolioDefID: int = Field(0, title="组合保证金套餐代码")
    ProdFamilyCode: str = Field("", title="品种代码")
    IsSPBM: int = Field(0, title="是否启用SPBM")
    ActionDirection: str = Field("", title="操作标志")
    SyncDeltaSequenceNo: int = Field(0, title="追平序号")


class WebCTPReqSyncDeltaSPBMPortfDefinition(WebCTPRequest):
    SyncDeltaSPBMPortfDefinition: SyncDeltaSPBMPortfDefinitionField = Field(
        title="风险结算追平SPBM组合保证金套餐")


class SyncDeltaSPBMInvstPortfDefField(BaseModel):
    """风险结算追平投资者SPBM套餐选择"""

    ExchangeID: str = Field("", title="交易所代码")
    BrokerID: str = Field("", title="经纪公司代码")
    InvestorID: str = Field("", title="投资者代码")
    PortfolioDefID: int = Field(0, title="组合保证金套餐代码")
    ActionDirection: str = Field("", title="操作标志")
    SyncDeltaSequenceNo: int = Field(0, title="追平序号")


class WebCTPReqSyncDeltaSPBMInvstPortfDef(WebCTPRequest):
    SyncDeltaSPBMInvstPortfDef: SyncDeltaSPBMInvstPortfDefField = Field(
        title="风险结算追平投资者SPBM套餐选择")


class SyncDeltaSPBMFutureParameterField(BaseModel):
    """风险结算追平SPBM期货合约保证金参数"""

    TradingDay: str = Field("", title="交易日")
    ExchangeID: str = Field("", title="交易所代码")
    InstrumentID: str = Field("", title="合约代码")
    ProdFamilyCode: str = Field("", title="品种代码")
    Cvf: int = Field(0, title="期货合约因子")
    TimeRange: str = Field("", title="阶段标识")
    MarginRate: float = Field(0.0, title="品种保证金标准")
    LockRateX: float = Field(0.0, title="期货合约内部对锁仓费率折扣比例")
    AddOnRate: float = Field(0.0, title="提高保证金标准")
    PreSettlementPrice: float = Field(0.0, title="昨结算价")
    AddOnLockRateX2: float = Field(0.0,
                                   title="期货合约内部对锁仓附加费率折扣比例")
    ActionDirection: str = Field("", title="操作标志")
    SyncDeltaSequenceNo: int = Field(0, title="追平序号")


class WebCTPReqSyncDeltaSPBMFutureParameter(WebCTPRequest):
    SyncDeltaSPBMFutureParameter: SyncDeltaSPBMFutureParameterField = Field(
        title="风险结算追平SPBM期货合约保证金参数")


class SyncDeltaSPBMOptionParameterField(BaseModel):
    """风险结算追平SPBM期权合约保证金参数"""

    TradingDay: str = Field("", title="交易日")
    ExchangeID: str = Field("", title="交易所代码")
    InstrumentID: str = Field("", title="合约代码")
    ProdFamilyCode: str = Field("", title="品种代码")
    Cvf: int = Field(0, title="期权合约因子")
    DownPrice: float = Field(0.0, title="期权冲抵价格")
    Delta: float = Field(0.0, title="Delta值")
    SlimiDelta: float = Field(0.0, title="卖方期权风险转换最低值")
    PreSettlementPrice: float = Field(0.0, title="昨结算价")
    ActionDirection: str = Field("", title="操作标志")
    SyncDeltaSequenceNo: int = Field(0, title="追平序号")


class WebCTPReqSyncDeltaSPBMOptionParameter(WebCTPRequest):
    SyncDeltaSPBMOptionParameter: SyncDeltaSPBMOptionParameterField = Field(
        title="风险结算追平SPBM期权合约保证金参数")


class SyncDeltaSPBMIntraParameterField(BaseModel):
    """风险结算追平SPBM品种内对锁仓折扣参数"""

    TradingDay: str = Field("", title="交易日")
    ExchangeID: str = Field("", title="交易所代码")
    ProdFamilyCode: str = Field("", title="品种代码")
    IntraRateY: float = Field(0.0, title="品种内合约间对锁仓费率折扣比例")
    AddOnIntraRateY2: float = Field(0.0,
                                    title="品种内合约间对锁仓附加费率折扣比例")
    ActionDirection: str = Field("", title="操作标志")
    SyncDeltaSequenceNo: int = Field(0, title="追平序号")


class WebCTPReqSyncDeltaSPBMIntraParameter(WebCTPRequest):
    SyncDeltaSPBMIntraParameter: SyncDeltaSPBMIntraParameterField = Field(
        title="风险结算追平SPBM品种内对锁仓折扣参数")


class SyncDeltaSPBMInterParameterField(BaseModel):
    """风险结算追平SPBM跨品种抵扣参数"""

    TradingDay: str = Field("", title="交易日")
    ExchangeID: str = Field("", title="交易所代码")
    SpreadId: int = Field(0, title="优先级")
    InterRateZ: float = Field(0.0, title="品种间对锁仓费率折扣比例")
    Leg1ProdFamilyCode: str = Field("", title="第一腿构成品种")
    Leg2ProdFamilyCode: str = Field("", title="第二腿构成品种")
    ActionDirection: str = Field("", title="操作标志")
    SyncDeltaSequenceNo: int = Field(0, title="追平序号")


class WebCTPReqSyncDeltaSPBMInterParameter(WebCTPRequest):
    SyncDeltaSPBMInterParameter: SyncDeltaSPBMInterParameterField = Field(
        title="风险结算追平SPBM跨品种抵扣参数")


class SyncDeltaSPBMAddOnInterParamField(BaseModel):
    """风险结算追平SPBM附加跨品种抵扣参数"""

    TradingDay: str = Field("", title="交易日")
    ExchangeID: str = Field("", title="交易所代码")
    SpreadId: int = Field(0, title="优先级")
    AddOnInterRateZ2: float = Field(0.0, title="品种间对锁仓附加费率折扣比例")
    Leg1ProdFamilyCode: str = Field("", title="第一腿构成品种")
    Leg2ProdFamilyCode: str = Field("", title="第二腿构成品种")
    ActionDirection: str = Field("", title="操作标志")
    SyncDeltaSequenceNo: int = Field(0, title="追平序号")


class WebCTPReqSyncDeltaSPBMAddOnInterParam(WebCTPRequest):
    SyncDeltaSPBMAddOnInterParam: SyncDeltaSPBMAddOnInterParamField = Field(
        title="风险结算追平SPBM附加跨品种抵扣参数")


class SyncDeltaSPMMInstParamField(BaseModel):
    """风险结算追平SPMM合约参数"""

    ExchangeID: str = Field("", title="交易所代码")
    InstrumentID: str = Field("", title="合约代码")
    InstMarginCalID: str = Field("", title="SPMM合约保证金算法")
    CommodityID: str = Field("", title="商品组代码")
    CommodityGroupID: str = Field("", title="商品群代码")
    ActionDirection: str = Field("", title="操作标志")
    SyncDeltaSequenceNo: int = Field(0, title="追平序号")


class WebCTPReqSyncDeltaSPMMInstParam(WebCTPRequest):
    SyncDeltaSPMMInstParam: SyncDeltaSPMMInstParamField = Field(
        title="风险结算追平SPMM合约参数")


class SyncDeltaSPMMProductParamField(BaseModel):
    """风险结算追平SPMM产品相关参数"""

    ExchangeID: str = Field("", title="交易所代码")
    ProductID: str = Field("", title="产品代码")
    CommodityID: str = Field("", title="商品组代码")
    CommodityGroupID: str = Field("", title="商品群代码")
    ActionDirection: str = Field("", title="操作标志")
    SyncDeltaSequenceNo: int = Field(0, title="追平序号")


class WebCTPReqSyncDeltaSPMMProductParam(WebCTPRequest):
    SyncDeltaSPMMProductParam: SyncDeltaSPMMProductParamField = Field(
        title="风险结算追平SPMM产品相关参数")


class SyncDeltaInvestorSPMMModelField(BaseModel):
    """风险结算追平投资者SPMM模板选择"""

    ExchangeID: str = Field("", title="交易所代码")
    BrokerID: str = Field("", title="经纪公司代码")
    InvestorID: str = Field("", title="投资者代码")
    SPMMModelID: str = Field("", title="SPMM模板ID")
    ActionDirection: str = Field("", title="操作标志")
    SyncDeltaSequenceNo: int = Field(0, title="追平序号")


class WebCTPReqSyncDeltaInvestorSPMMModel(WebCTPRequest):
    SyncDeltaInvestorSPMMModel: SyncDeltaInvestorSPMMModelField = Field(
        title="风险结算追平投资者SPMM模板选择")


class SyncDeltaSPMMModelParamField(BaseModel):
    """风险结算追平SPMM模板参数设置"""

    ExchangeID: str = Field("", title="交易所代码")
    SPMMModelID: str = Field("", title="SPMM模板ID")
    CommodityGroupID: str = Field("", title="商品群代码")
    IntraCommodityRate: float = Field(0.0, title="SPMM品种内跨期优惠系数")
    InterCommodityRate: float = Field(0.0, title="SPMM品种间优惠系数")
    OptionDiscountRate: float = Field(0.0, title="SPMM期权优惠系数")
    MiniMarginRatio: float = Field(0.0, title="商品群最小保证金比例")
    ActionDirection: str = Field("", title="操作标志")
    SyncDeltaSequenceNo: int = Field(0, title="追平序号")


class WebCTPReqSyncDeltaSPMMModelParam(WebCTPRequest):
    SyncDeltaSPMMModelParam: SyncDeltaSPMMModelParamField = Field(
        title="风险结算追平SPMM模板参数设置")


class SyncDeltaRCAMSCombProdInfoField(BaseModel):
    """风险结算追平RCAMS产品组合信息"""

    TradingDay: str = Field("", title="交易日")
    ExchangeID: str = Field("", title="交易所代码")
    ProductID: str = Field("", title="产品代码")
    CombProductID: str = Field("", title="商品组代码")
    ProductGroupID: str = Field("", title="商品群代码")
    ActionDirection: str = Field("", title="操作标志")
    SyncDeltaSequenceNo: int = Field(0, title="追平序号")


class WebCTPReqSyncDeltaRCAMSCombProdInfo(WebCTPRequest):
    SyncDeltaRCAMSCombProdInfo: SyncDeltaRCAMSCombProdInfoField = Field(
        title="风险结算追平RCAMS产品组合信息")


class SyncDeltaRCAMSInstrParameterField(BaseModel):
    """风险结算追平RCAMS同合约风险对冲参数"""

    TradingDay: str = Field("", title="交易日")
    ExchangeID: str = Field("", title="交易所代码")
    ProductID: str = Field("", title="产品代码")
    HedgeRate: float = Field(0.0, title="同合约风险对冲比率")
    ActionDirection: str = Field("", title="操作标志")
    SyncDeltaSequenceNo: int = Field(0, title="追平序号")


class WebCTPReqSyncDeltaRCAMSInstrParameter(WebCTPRequest):
    SyncDeltaRCAMSInstrParameter: SyncDeltaRCAMSInstrParameterField = Field(
        title="风险结算追平RCAMS同合约风险对冲参数")


class SyncDeltaRCAMSIntraParameterField(BaseModel):
    """风险结算追平RCAMS品种内风险对冲参数"""

    TradingDay: str = Field("", title="交易日")
    ExchangeID: str = Field("", title="交易所代码")
    CombProductID: str = Field("", title="产品组合代码")
    HedgeRate: float = Field(0.0, title="品种内对冲比率")
    ActionDirection: str = Field("", title="操作标志")
    SyncDeltaSequenceNo: int = Field(0, title="追平序号")


class WebCTPReqSyncDeltaRCAMSIntraParameter(WebCTPRequest):
    SyncDeltaRCAMSIntraParameter: SyncDeltaRCAMSIntraParameterField = Field(
        title="风险结算追平RCAMS品种内风险对冲参数")


class SyncDeltaRCAMSInterParameterField(BaseModel):
    """风险结算追平RCAMS跨品种风险折抵参数"""

    TradingDay: str = Field("", title="交易日")
    ExchangeID: str = Field("", title="交易所代码")
    ProductGroupID: str = Field("", title="商品群代码")
    Priority: int = Field(0, title="优先级")
    CreditRate: float = Field(0.0, title="折抵率")
    CombProduct1: str = Field("", title="产品组合代码1")
    CombProduct2: str = Field("", title="产品组合代码2")
    ActionDirection: str = Field("", title="操作标志")
    SyncDeltaSequenceNo: int = Field(0, title="追平序号")


class WebCTPReqSyncDeltaRCAMSInterParameter(WebCTPRequest):
    SyncDeltaRCAMSInterParameter: SyncDeltaRCAMSInterParameterField = Field(
        title="风险结算追平RCAMS跨品种风险折抵参数")


class SyncDeltaRCAMSSOptAdjParamField(BaseModel):
    """风险结算追平RCAMS空头期权风险调整参数"""

    TradingDay: str = Field("", title="交易日")
    ExchangeID: str = Field("", title="交易所代码")
    CombProductID: str = Field("", title="产品组合代码")
    HedgeFlag: str = Field("", title="投套标志")
    AdjustValue: float = Field(0.0, title="空头期权风险调整标准")
    ActionDirection: str = Field("", title="操作标志")
    SyncDeltaSequenceNo: int = Field(0, title="追平序号")


class WebCTPReqSyncDeltaRCAMSSOptAdjParam(WebCTPRequest):
    SyncDeltaRCAMSSOptAdjParam: SyncDeltaRCAMSSOptAdjParamField = Field(
        title="风险结算追平RCAMS空头期权风险调整参数")


class SyncDeltaRCAMSCombRuleDtlField(BaseModel):
    """风险结算追平RCAMS策略组合规则明细"""

    TradingDay: str = Field("", title="交易日")
    ExchangeID: str = Field("", title="交易所代码")
    ProdGroup: str = Field("", title="策略产品")
    RuleId: str = Field("", title="策略id")
    Priority: int = Field(0, title="优先级")
    HedgeFlag: str = Field("", title="投套标志")
    CombMargin: float = Field(0.0, title="组合保证金标准")
    ExchangeInstID: str = Field("", title="交易所组合合约代码")
    LegID: int = Field(0, title="单腿编号")
    LegInstrumentID: str = Field("", title="单腿合约代码")
    Direction: str = Field("", title="买卖方向")
    LegMultiple: int = Field(0, title="单腿乘数")
    ActionDirection: str = Field("", title="操作标志")
    SyncDeltaSequenceNo: int = Field(0, title="追平序号")


class WebCTPReqSyncDeltaRCAMSCombRuleDtl(WebCTPRequest):
    SyncDeltaRCAMSCombRuleDtl: SyncDeltaRCAMSCombRuleDtlField = Field(
        title="风险结算追平RCAMS策略组合规则明细")


class SyncDeltaRCAMSInvstCombPosField(BaseModel):
    """风险结算追平RCAMS策略组合持仓"""

    ExchangeID: str = Field("", title="交易所代码")
    BrokerID: str = Field("", title="经纪公司代码")
    InvestorID: str = Field("", title="投资者代码")
    InstrumentID: str = Field("", title="合约代码")
    HedgeFlag: str = Field("", title="投套标志")
    PosiDirection: str = Field("", title="持仓多空方向")
    CombInstrumentID: str = Field("", title="组合合约代码")
    LegID: int = Field(0, title="单腿编号")
    ExchangeInstID: str = Field("", title="交易所组合合约代码")
    TotalAmt: int = Field(0, title="持仓量")
    ExchMargin: float = Field(0.0, title="交易所保证金")
    Margin: float = Field(0.0, title="投资者保证金")
    ActionDirection: str = Field("", title="操作标志")
    SyncDeltaSequenceNo: int = Field(0, title="追平序号")


class WebCTPReqSyncDeltaRCAMSInvstCombPos(WebCTPRequest):
    SyncDeltaRCAMSInvstCombPos: SyncDeltaRCAMSInvstCombPosField = Field(
        title="风险结算追平RCAMS策略组合持仓")


class SyncDeltaRULEInstrParameterField(BaseModel):
    """风险结算追平RULE合约保证金参数"""

    TradingDay: str = Field("", title="交易日")
    ExchangeID: str = Field("", title="交易所代码")
    InstrumentID: str = Field("", title="合约代码")
    InstrumentClass: str = Field("", title="合约类型")
    StdInstrumentID: str = Field("", title="标准合约")
    BSpecRatio: float = Field(0.0, title="投机买折算系数")
    SSpecRatio: float = Field(0.0, title="投机卖折算系数")
    BHedgeRatio: float = Field(0.0, title="套保买折算系数")
    SHedgeRatio: float = Field(0.0, title="套保卖折算系数")
    BAddOnMargin: float = Field(0.0, title="买附加风险保证金")
    SAddOnMargin: float = Field(0.0, title="卖附加风险保证金")
    CommodityGroupID: int = Field(0, title="商品群号")
    ActionDirection: str = Field("", title="操作标志")
    SyncDeltaSequenceNo: int = Field(0, title="追平序号")


class WebCTPReqSyncDeltaRULEInstrParameter(WebCTPRequest):
    SyncDeltaRULEInstrParameter: SyncDeltaRULEInstrParameterField = Field(
        title="风险结算追平RULE合约保证金参数")


class SyncDeltaRULEIntraParameterField(BaseModel):
    """风险结算追平RULE品种内对锁仓折扣参数"""

    TradingDay: str = Field("", title="交易日")
    ExchangeID: str = Field("", title="交易所代码")
    ProdFamilyCode: str = Field("", title="品种代码")
    StdInstrumentID: str = Field("", title="标准合约")
    StdInstrMargin: float = Field(0.0, title="标准合约保证金")
    UsualIntraRate: float = Field(0.0, title="一般月份合约组合保证金系数")
    DeliveryIntraRate: float = Field(0.0, title="临近交割合约组合保证金系数")
    ActionDirection: str = Field("", title="操作标志")
    SyncDeltaSequenceNo: int = Field(0, title="追平序号")


class WebCTPReqSyncDeltaRULEIntraParameter(WebCTPRequest):
    SyncDeltaRULEIntraParameter: SyncDeltaRULEIntraParameterField = Field(
        title="风险结算追平RULE品种内对锁仓折扣参数")


class SyncDeltaRULEInterParameterField(BaseModel):
    """风险结算追平RULE跨品种抵扣参数"""

    TradingDay: str = Field("", title="交易日")
    ExchangeID: str = Field("", title="交易所代码")
    SpreadId: int = Field(0, title="优先级")
    InterRate: float = Field(0.0, title="品种间对锁仓费率折扣比例")
    Leg1ProdFamilyCode: str = Field("", title="第一腿构成品种")
    Leg2ProdFamilyCode: str = Field("", title="第二腿构成品种")
    Leg1PropFactor: int = Field(0, title="腿1比例系数")
    Leg2PropFactor: int = Field(0, title="腿2比例系数")
    CommodityGroupID: int = Field(0, title="商品群号")
    CommodityGroupName: str = Field("", title="商品群名称")
    ActionDirection: str = Field("", title="操作标志")
    SyncDeltaSequenceNo: int = Field(0, title="追平序号")


class WebCTPReqSyncDeltaRULEInterParameter(WebCTPRequest):
    SyncDeltaRULEInterParameter: SyncDeltaRULEInterParameterField = Field(
        title="风险结算追平RULE跨品种抵扣参数")
