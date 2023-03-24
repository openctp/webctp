from fastapi import FastAPI, WebSocket, WebSocketDisconnect

from services.connection_manager import ConnectionManager


connection_manager = ConnectionManager()

app = FastAPI()

@app.websocket("/")
async def td_websocket(websocket: WebSocket):
    await connection_manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_json()
            await connection_manager.recv(websocket, data)
    except WebSocketDisconnect:
        connection_manager.disconnect(websocket)
