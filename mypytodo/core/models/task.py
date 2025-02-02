class Task:
    def __init__(
        self,
        title: str,
        status: str,
        priority: str,
        start: int,
        end: int,
        description: str,
        repeat: bool | None,
    ) -> None:
        self._title = title
        self._status = status
        self._priority = priority
        self._start = start
        self._end = end
        self._description = description
        self._repeat = repeat if repeat is True else False

    @property
    def start(self) -> int:
        return self._start

    def is_repeat(self) -> bool | None:
        return self._repeat
