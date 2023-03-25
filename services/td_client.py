from typing import Callable

from anyio.abc import TaskGroup

class TdClient(object):
    """
    TdClient is the boundary of websocket and client,
    the boundary of object data and CTP structure data,
    and also the boundray of async code and sync code.
    It is responsible for controling the status of ctp
    client.
    """

    def __init__(self) -> None:
        self._rsp_callback: Callable[[dict[str, any]], None] = None
        self._task_group: TaskGroup = None
        self._running: bool = False

    async def call(self, data: dict[str, any]) -> None:
        pass

    async def release(self) -> None:
        pass

    async def run(self) -> None:
        pass
    
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
