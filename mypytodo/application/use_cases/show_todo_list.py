from mypytodo.application.interfaces import TodoRepository
from mypytodo.core.models import Task


class ShowTodoList:
    def __init__(self, todo_repository: TodoRepository) -> None:
        self.todo_repository = todo_repository
        # TODO: use_cache (default: True) 引数を用意して、
        # use_cacheがFalseならキャッシュデータを使うみたいなやつ

    def default(self) -> list[Task]:
        todo_list = self._get_todo_list()
        todo_list.sort(key=lambda task: task.start)

        return todo_list

    def _get_todo_list(self) -> list[Task]:
        load_data = self.todo_repository.load()
        todo_list = [Task(**data) for data in load_data]

        return todo_list
