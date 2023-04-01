import abc
import anyio
from fastapi import WebSocket, WebSocketDisconnect

from .td_client import TdClient
from .md_client import MdClient


@abc.ABC
class BaseConnection(object):
    def __init__(self, websocket: WebSocket) -> None:
        self._ws: WebSocket = websocket
        self._client: TdClient | MdClient = None
    
    async def connect(self):
        await self._ws.accept()
        self._client = self.create_client()
    
    def disconnect(self) -> None:
        self._client.stop()
    
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
    
    @abc.abstractmethod
    def create_client(self):
        pass


class TdConnection(BaseConnection):
    def __init__(self, websocket: WebSocket) -> None:
        super().__init__()

    def create_client(self):
        client = TdClient()
        client.rsp_callback = self.send
        return client

class MdConnection(BaseConnection):
    def __init__(self, websocket: WebSocket) -> None:
        super().__init__()
    
    def create_client(self):
        client = MdClient()
        client.rsp_callback = self.send
        return client
