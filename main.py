import anyio
import uvicorn
from utils import GlobalConfig


async def main():
    GlobalConfig.load_config("config.json")
    server_config = uvicorn.Config("main:app", host="0.0.0.0", port=GlobalConfig.Port, log_level="info")
    server = uvicorn.Server(server_config)
    await server.serve()

if __name__ == "__main__":
    anyio.run(main)
