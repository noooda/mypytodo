from mypytodo.application.interfaces import TodoRepository
from mypytodo.core.models import Task


class ShowTodoList:
    def __init__(self, todo_repository: TodoRepository) -> None:
        self.todo_repository = todo_repository
        # TODO: use_cache (default: True) 引数を用意して、
        # use_cacheがFalseならキャッシュデータを使うみたいなやつ

    def default(self) -> dict[str, list[Task]]:
        todo_list = self._get_todo_list()
        if todo_list['repeat']:
            todo_list['repeat'].sort(key=lambda task: task.start)
        if todo_list['normal']:
            todo_list['normal'].sort(key=lambda task: task.start)
        return todo_list

    def _get_todo_list(self) -> dict[str, list[Task]]:
        load_data = self.todo_repository.load()
        todo_list = [Task(**data) for data in load_data]

        repeat_todo_list = []
        normal_todo_list = []
        for task in todo_list:
            if task.is_repeat():
                repeat_todo_list.append(task)
            else:
                normal_todo_list.append(task)

        return {'repeat': repeat_todo_list, 'normal': normal_todo_list}
