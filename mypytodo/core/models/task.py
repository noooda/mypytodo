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
        self._repeat = False if repeat is None else repeat

    @property
    def title(self) -> str:
        return self._title

    @property
    def status(self) -> str:
        return self._status

    @property
    def priority(self) -> str:
        return self._priority

    @property
    def start(self) -> int:
        return self._start

    @property
    def end(self) -> int:
        return self._end

    @property
    def description(self) -> str:
        return self._description

    @property
    def repeat(self) -> bool | None:
        return self._repeat
