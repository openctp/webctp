import argparse
import logging
import sys
import anyio
import uvicorn
from utils import GlobalConfig


def init_log():
    root = logging.getLogger()
    root.setLevel(GlobalConfig.LogLevel)
    
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(GlobalConfig.LogLevel)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    root.addHandler(handler)

async def main(config_file_path: str, app_type: str):
    GlobalConfig.load_config(config_file_path)
    init_log()

    server_config = None
    app: str = ""
    if app_type == "td":
        logging.info("start td app")
        app = "apps:td_app"
    elif app_type == "md":
        logging.info("start md app")
        app = "apps:md_app"
    elif app_type == "dev":
        logging.info("start dev app")
        app = "apps:dev_app"
    else:
        logging.error("error app type: %s", app_type)
        exit(1)

    server_config = uvicorn.Config(app, host=GlobalConfig.Host, port=GlobalConfig.Port, log_level="info")
    server = uvicorn.Server(server_config)
    await server.serve()

if __name__ == "__main__":
    argparser = argparse.ArgumentParser("webctp", description="WebCTP")
    argparser.add_argument("--config", type=str, default="./config.yaml", help="config file path")
    argparser.add_argument("--app_type", type=str, default="td", help="app type, td or md")
    parsed_args = argparser.parse_args(sys.argv[1:])
    anyio.run(main, parsed_args.config, parsed_args.app_type)
