import yaml

class GlobalConfig(object):

    TdFrontAddress: str
    MdFrontAddress: str
    BrokerID: str
    AuthCode: str
    AppID: str
    Host: str
    Port: int
    LogLevel: str

    @classmethod
    def load_config(cls, config_file_path: str):
        with open(config_file_path) as f:
            config = yaml.load(f, Loader=yaml.FullLoader)
            cls.TdFrontAddress = config.get("TdFrontAddress", "")
            cls.MdFrontAddress = config.get("MdFrontAddress", "")
            cls.BrokerID = config.get("BrokerID", "")
            cls.AuthCode = config.get("AuthCode", "")
            cls.AppID = config.get("AppID", "")
            cls.Host = config.get("Host", "0.0.0.0")
            cls.Port = config.get("Port", 8080)
            cls.LogLevel = config.get("LogLevel", "info")


if __name__ == "__main__":
    GlobalConfig.load_config("../config.sample.yaml")
    print(GlobalConfig.TdFrontAddress, type(GlobalConfig.TdFrontAddress))
    print(GlobalConfig.MdFrontAddress, type(GlobalConfig.MdFrontAddress))
    print(GlobalConfig.BrokerID, type(GlobalConfig.BrokerID))
    print(GlobalConfig.AuthCode, type(GlobalConfig.AuthCode))
    print(GlobalConfig.AppID, type(GlobalConfig.AppID))
    print(GlobalConfig.Host, type(GlobalConfig.Host))
    print(GlobalConfig.Port, type(GlobalConfig.Port))
    print(GlobalConfig.LogLevel, type(GlobalConfig.LogLevel))
