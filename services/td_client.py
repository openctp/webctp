import logging
from queue import Queue
from typing import Callable

import anyio
from anyio.abc import TaskGroup

from clients import CTPTdClient

class TdClient(object):
    """
    TdClient is the boundary of websocket and client,
    and the boundray of async code and sync code.
    It is responsible for controling the status of ctp
    client.
    """

    def __init__(self) -> None:
        self._rsp_callback: Callable[[dict[str, any]], None] = None
        self._task_group: TaskGroup = None
        self._running: bool = False
        self._queue: Queue = Queue()
        self._client: CTPTdClient = None
        self._stop_event: anyio.Event = None
   
    @property
    def rsp_callback(self) -> Callable[[dict[str, any]], None]:
        return self._rsp_callback

    @rsp_callback.setter
    def set_rsp_callback(self, callback: Callable[[dict[str, any]], None]) -> None:
        self._rsp_callback = callback
    
    @property
    def task_group(self) -> TaskGroup:
        return self._task_group
    
    @task_group.setter
    def set_task_group(self, task_group: TaskGroup) -> None:
        self._task_group = task_group
    
    def on_rsp_or_rtn(self, data: dict[str, any]) -> None:
        self._queue.put_nowait(data)

    async def call(self, data: dict[str, any]) -> None:
        if data["MessageType"] == "ReqUserLogin":
            user_id: str = data["ReqUserLogin"]["UserID"]
            password: str = data["ReqUserLogin"]["Password"]
            await self.start(user_id, password)

    async def start(self, user_id: str, password: str) -> None:
        # NOTE: This if clause avoid the following secenario
        # 1. start a background corroutine
        # 2. start login
        # 3. login failed
        # 4. start login again
        if not self._client:
            self._client = await anyio.to_thread.run_sync(CTPTdClient, user_id, password, user_id)
            self._client.rsp_callback = self.on_rsp_or_rtn
            self._task_group.start_soon(self.run, name=f"{user_id}-td-bg-corroutine")
        await anyio.to_thread.run_sync(self._client.connect)

    async def stop(self) -> None:
        self._running = False
        if self._stop_event:
            await self._stop_event.wait()
        self._client.release()

    async def run(self) -> None:
        self._stop_event = anyio.Event()
        self._running = True
        while self._running:
            await self._procees_a_message(1.0)
        self._stop_event.set()

    async def _procees_a_message(self, wait_time: float):
        # TODO: try to use cancellable = True
        rsp = await anyio.to_thread.run_sync(self._queue.get, True, wait_time)
        await self.rsp_callback(rsp)

