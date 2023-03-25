import anyio
from fastapi import WebSocket, WebSocketDisconnect

from td_client import TdClient

class TdConnection(object):
    def __init__(self, websocket: WebSocket) -> None:
        self._ws: WebSocket = websocket
        self._client = None
    
    async def connect(self):
        await self._ws.accept()
        # TODO: create a client
        self._client = TdClient()
        self._client.rsp_callback = self.send
    
    def disconnect(self) -> None:
        # TODO: release client
        self._client.release()
    
    async def send(self, data: dict[str, any]) -> None:
        await self._ws.send_json(data)
    
    async def recv(self) -> dict[str, any]:
        return await self._ws.receive_json()

    async def run(self):
        await self.connect()

        async with anyio.create_task_group() as task_group:
            self._client.task_group = task_group
            try:
                while True:
                    data = await self.recv()
                    result = await self._client.call(data)
                    await self.send(result)
            except WebSocketDisconnect:
                self.disconnect()
