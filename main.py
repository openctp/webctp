import anyio
import fastapi
import uvicorn
from utils import GlobalConfig
from apps.td_app import app as td_app

app = fastapi.FastAPI()
app.mount("/td", td_app)


async def main():
    GlobalConfig.load_config("config.json")
    # TODO: configure the log and log_level
    server_config = uvicorn.Config("main:app", host="0.0.0.0", port=GlobalConfig.Port, log_level="info")
    server = uvicorn.Server(server_config)
    await server.serve()

if __name__ == "__main__":
    anyio.run(main)
