class CallError(object):

    _errors: dict[int, any] = {}

    def __init__(self, ret: int, error_id: int, error_message: str):
        self._ret = ret
        self._error_id = error_id
        self._error_message = error_message
    
    def to_rsp_info(self) -> dict[str, any]:
        return {
            "ErrorID": self._error_id,
            "ErrorMsg": self._error_message
        }

    @classmethod
    def register_error(cls, ret: int, error_id: int, error_message: str):
        cls._errors[ret] = CallError(ret, error_id, error_message)

    @classmethod
    def get_error(cls, ret: int) -> any:
        return cls._errors[ret]

    @classmethod
    def get_rsp_info(cls, ret: int) -> dict[str, any]:
        return cls._errors[ret].to_rsp_info()


CallError.register_error(1, -1, "CTP:请求失败")
CallError.register_error(2, -2, "CTP:未处理请求超过许可数")
CallError.register_error(3, -3, "CTP:每秒发送请求数超过许可数")
CallError.register_error(404, -404, "Not implemented")
CallError.register_error(401, -401, "未登录")
