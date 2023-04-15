from openctp import thostmduserapi as mdapi
from openctp import thosttraderapi as tdapi

_mdapi = mdapi.CThostFtdcMdApi.CreateFtdcMdApi()
# print all the methods of the object to a specified file

if __name__ == "__main__":
    print("mdapi methods: ")
    with open("./mdapi.txt", "w") as f:
        for method in dir(_mdapi):
            print(f"mdapi methods: {method}")
            f.write(method + "\n")
