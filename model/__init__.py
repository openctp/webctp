import inspect

from model import request

REQUEST_PAYLOAD = {}

for name, value in inspect.getmembers(request):
    if name.startswith("WebCTP") and name != "WebCTPRequest":
        REQUEST_PAYLOAD[name.replace("WebCTP", "")] = value
