import hashlib


class Task:
    def __init__(
        self,
        repeat: bool | None,
        title: str,
        priority: str,
        start: int,
        end: int,
        description: str,
    ) -> None:
        self._id = self._generate_sha256_hash(title)
        self._repeat = repeat
        self._title = self._mark_is_repeat_task(title)
        self._priority = priority
        self._start = start
        self._end = end
        self._description = description

    @property
    def id(self) -> str:
        return self._id

    @property
    def title(self) -> str:
        return self._title

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

    def _generate_sha256_hash(self, title: str) -> str:
        data = title.encode()
        sha256_hash = hashlib.sha256(data).hexdigest()
        return sha256_hash

    def _mark_is_repeat_task(self, title: str) -> str:
        return title if self._repeat is None else f'{title} [re]'
