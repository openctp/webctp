from anyio.abc import TaskGroup

class GlobalTaskGroup(object):

    _task_group: TaskGroup | None = None

    @classmethod
    def set(cls, task_group: TaskGroup) -> None:
        cls._task_group = task_group
    
    @classmethod
    def get(cls, task_group: TaskGroup) -> TaskGroup:
        return cls._task_group
