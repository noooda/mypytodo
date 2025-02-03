import yaml

from mypytodo.application.interfaces import TodoRepository


class YamlTodoRepository(TodoRepository):
    def __init__(self, repository_path: str) -> None:
        self.repository_path = repository_path

    def load(self) -> list[dict]:
        with open(self.repository_path, 'r') as f:
            todo_list = yaml.safe_load(f)
        return todo_list
