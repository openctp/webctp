from openctp import thostmduserapi as mdapi
from openctp import thosttraderapi as tdapi

with open("./mdapi.txt", "w+") as f:
    for method in dir(mdapi.CThostFtdcMdApi):
        f.write("- " + method + "\n")

with open("./mdspi.txt", "w+") as f:
    for method in dir(mdapi.CThostFtdcMdSpi):
        f.write("- " + method + "\n")

with open("./tdapi.txt", "w+") as f:
    for method in dir(tdapi.CThostFtdcTraderApi):
        f.write("- " + method + "\n")

with open("./tdspi.txt", "w+") as f:
    for method in dir(tdapi.CThostFtdcTraderSpi):
        f.write("- " + method + "\n")
