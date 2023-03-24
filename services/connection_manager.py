from fastapi import WebSocket

class ConnectionManager(object):
    def __init__(self) -> None:
        self._active_connections: dict[WebSocket, bool] = dict()
    
    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        # TODO: change to client
        self._active_connections[websocket] = True
    
    def disconnect(self, websocket: WebSocket):
        if websocket in self._active_connections:
            # TODO: release client
            del self._active_connections[websocket]
    
    async def send(self, websocket: WebSocket, data: dict[str, any]) -> None:
        await websocket.send_json(data)
    
    async def recv(self, websocket: WebSocket, data: dict[str, any]) -> None:
        result = await self._active_connections[websocket].call(data)
        await self.send(websocket, result)
