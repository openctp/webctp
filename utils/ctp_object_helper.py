import logging

class CTPObjectHelper(object):

    exclude_attrs = ["thisown"]

    @staticmethod
    def object_to_dict(obj: object, typ: any) -> dict[str, any]:
        data = {}
        if obj:
            # filter python built-in attributes
            attrs = list(filter(lambda x: not (x.startswith("__") or x in CTPObjectHelper.exclude_attrs), dir(typ)))
            for attr in attrs:
                data[attr] = obj.__getattribute__(attr)
        return data
    
    @staticmethod
    def dict_to_object(data: dict[str, any], obj: object) -> None:
        for attr, value in data.items():
            obj.__setattr__(attr, value)
    
    @staticmethod
    def build_response_dict(message_type: str, rsp_info: object = None, request_id: int = None, is_last: bool = None) -> dict[str, any]:
        response = {
            "MsgType": message_type,
            "RspInfo": None,
        }
        if request_id:
            response["RequestID"] = request_id
        if is_last:
            response["IsLast"] = is_last
        if rsp_info:
            response["RspInfo"] = {
                "ErrorID": rsp_info.ErrorID,
                "ErrorMsg": rsp_info.ErrorMsg
            }
        return response
    
    @staticmethod
    def extract_request(request_dict: dict[str, any], request_field_name: str, request_type):
        req = request_type()
        CTPObjectHelper.dict_to_object(request_dict[request_field_name], req)
        return (req, request_dict["RequestID"])