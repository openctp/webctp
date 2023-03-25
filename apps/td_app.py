from fastapi import FastAPI, WebSocket, WebSocketDisconnect

from services.connection import TdConnection


app = FastAPI()

@app.websocket("/")
async def td_websocket(websocket: WebSocket):
    connection = TdConnection(websocket)
    await connection.run()
