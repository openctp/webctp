from openctp import thosttraderapi as tdapi
from openctp import thostmduserapi as mdapi

# 小工具，给对象名和类型，生成转字典代码
object_name = "pQryOptionInstrCommRate"
typ = tdapi.CThostFtdcQryOptionInstrCommRateField   

exclude_attrs = ["thisown","reserve","reserve1","reserve2","reserve3"]
attrs = list(filter(lambda x: not (x.startswith("__") or x in exclude_attrs), dir(typ)))
result = '{\n'
for attr in attrs:
    result += f'\t"{attr}": {object_name}.{attr},\n'
result = result[:-2]
result += '\n\t}'
print(result)