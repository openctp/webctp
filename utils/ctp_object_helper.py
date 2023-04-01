class CTPObjectHelper(object):

    exclude_attrs = ["thisown"]

    @staticmethod
    def object_to_dict(obj: object) -> dict[str, any]:
        data = {}
        for attr, value in obj.__dict__.items():
            if attr not in CTPObjectHelper.exclude_attrs:
                data[attr] = value
    
    @staticmethod
    def dict_to_object(data: dict[str, any], obj: object) -> None:
        for attr, value in data.items():
            obj.__setattr__(attr, value)
