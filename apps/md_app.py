from fastapi import FastAPI, WebSocket
from services.connection import MdConnection


app = FastAPI()

@app.websocket("/")
async def md_websocket(websocket: WebSocket):
    connection = MdConnection(websocket)
    await connection.run()
