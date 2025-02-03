from abc import ABC, abstractmethod


class TodoRepository(ABC):
    @abstractmethod
    def load(self) -> list[dict]:
        pass
