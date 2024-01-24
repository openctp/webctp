import abc
import anyio
import json
import logging
from fastapi import WebSocket, WebSocketDisconnect
from starlette.websockets import WebSocketState

from constants.call_errors import CallError
from constants.constant import CommonConstant as Constant
from .td_client import TdClient
from .md_client import MdClient


class BaseConnection(abc.ABC):
    def __init__(self, websocket: WebSocket) -> None:
        self._ws: WebSocket = websocket
        self._client: TdClient | MdClient = None
    
    async def connect(self):
        await self._ws.accept()
        self._client = self.create_client()
    
    async def disconnect(self) -> None:
        await self._client.stop()
    
    async def send(self, data: dict[str, any]) -> None:
        if self._ws.client_state == WebSocketState.CONNECTED:
            await self._ws.send_json(data)
    
    async def recv(self) -> dict[str, any]:
        return await self._ws.receive_json()

    async def run(self):
        await self.connect()

        async with anyio.create_task_group() as task_group:
            self._client.task_group = task_group
            try:
                while True:
                    try:
                        data = await self.recv()
                        await self._client.call(data)
                    except json.decoder.JSONDecodeError as err:
                        await self.send({
                            Constant.MessageType: "",
                            Constant.RspInfo: CallError.get_rsp_info(400),
                            "Detail": str(err),
                        })
            except WebSocketDisconnect:
                logging.debug("websocket disconnect")
                await self.disconnect()
    
    @abc.abstractmethod
    def create_client(self):
        pass


class TdConnection(BaseConnection):
    def __init__(self, websocket: WebSocket) -> None:
        super().__init__(websocket)

    def create_client(self):
        client = TdClient()
        client.rsp_callback = self.send
        return client

class MdConnection(BaseConnection):
    def __init__(self, websocket: WebSocket) -> None:
        super().__init__(websocket)
    
    def create_client(self):
        client = MdClient()
        client.rsp_callback = self.send
        return client
