import logging
from queue import Queue, Empty
from typing import Callable

import anyio
from anyio.abc import TaskGroup
from constants import CallError
from constants import CommonConstant as Constant
from clients import CTPMdClient

class MdClient(object):
    """
    MdClient is the boundary of websocket and client,
    and the boundary of async code and sync code.
    It is responsible for controlling the status of
    ctp client.
    """

    def __init__(self) -> None:
        self._rsp_callback: Callable[[dict[str, any]], None] = None
        self._task_group: TaskGroup = None
        self._running: bool = False
        self._queue: Queue = Queue()
        self._client: CTPMdClient = None
        self._client_lock: anyio.Lock = anyio.Lock()
        self._stop_event: anyio.Event = None
        self._call_map: dict[str, Callable[[dict[str, any]], int]] = {}
   
    @property
    def rsp_callback(self) -> Callable[[dict[str, any]], None]:
        return self._rsp_callback

    @rsp_callback.setter
    def rsp_callback(self, callback: Callable[[dict[str, any]], None]) -> None:
        self._rsp_callback = callback
    
    @property
    def task_group(self) -> TaskGroup:
        return self._task_group
    
    @task_group.setter
    def task_group(self, task_group: TaskGroup) -> None:
        self._task_group = task_group
    
    def on_rsp_or_rtn(self, data: dict[str, any]) -> None:
        self._queue.put_nowait(data)

    async def call(self, request: dict[str, any]) -> None:
        message_type = request[Constant.MessageType]
        if message_type == Constant.ReqUserLogin:
            user_id: str = request[Constant.ReqUserLogin]["UserID"]
            password: str = request[Constant.ReqUserLogin]["Password"]
            await self.start(user_id, password)
        else:
            if message_type in self._call_map:
                await anyio.to_thread.run_sync(self._call_map[message_type], request)
            else:
                resposne = {
                    Constant.MessageType: message_type,
                    Constant.RspInfo: CallError.get_rsp_info(404)
                }
                await self.rsp_callback(resposne)

    async def start(self, user_id: str, password: str) -> None:
        # NOTE: This if clause avoid the following secenario
        # 1. start a background corroutine
        # 2. start login
        # 3. login failed
        # 4. start login again
        async with self._client_lock:
            if not self._client:
                self._client = await anyio.to_thread.run_sync(CTPMdClient, user_id, password)
                self._client.rsp_callback = self.on_rsp_or_rtn
                self._init_call_map()
                # TODO: need to create a random name to replace user_id
                self._task_group.start_soon(self.run, name=f"{user_id}-md-bg-corroutine")
            await anyio.to_thread.run_sync(self._client.connect)

    async def stop(self) -> None:
        logging.debug(f"stopping md client")
        self._running = False
        if self._stop_event:
            await self._stop_event.wait()
            self._stop_event = None
        
        if self._client:
            await anyio.to_thread.run_sync(self._client.release)
        logging.debug(f"md client stopped")

    async def run(self) -> None:
        logging.info("start to run new corroutine")
        self._stop_event = anyio.Event()
        self._running = True
        while self._running:
            await self._procees_a_message(1.0)
        logging.info("stop running corroutine")
        self._stop_event.set()

    async def _procees_a_message(self, wait_time: float):
        try:
            rsp = await anyio.to_thread.run_sync(self._queue.get, True, wait_time, cancellable=True)
            await self.rsp_callback(rsp)
        except Empty:
            pass
        except Exception as e:
            logging.info(f"exception in md client {e} {type(e)}")

    def _init_call_map(self):
        self._call_map["SubscribeMarketData"] = self._client.subscribeMarketData
        self._call_map["UnSubscribeMarketData"] = self._client.unSubscribeMarketData
