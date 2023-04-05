import logging
import sys
import anyio
import fastapi
import uvicorn
from utils import GlobalConfig
from apps.td_app import app as td_app
from apps.md_app import app as md_app

app = fastapi.FastAPI()
app.mount("/td", td_app)
app.mount("/md", md_app)

root = logging.getLogger()
root.setLevel(logging.DEBUG)

handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
root.addHandler(handler)

async def main():
    GlobalConfig.load_config("config.json")
    # TODO: configure the log and log_level
    server_config = uvicorn.Config("main:app", host="0.0.0.0", port=GlobalConfig.Port, log_level="info")
    server = uvicorn.Server(server_config)
    await server.serve()

if __name__ == "__main__":
    anyio.run(main)
