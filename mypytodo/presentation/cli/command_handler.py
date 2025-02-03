import argparse

from mypytodo.application.use_cases import ShowTodoList


class CommandHandler:
    def __init__(self, show_todo_list: ShowTodoList) -> None:
        self.show_todo_list = show_todo_list

    def list_cmd(self) -> None:
        todo_list = self.show_todo_list.default()

        for id, task in enumerate(todo_list):
            print('#' * 20)
            print(f'id: {id+1}')
            print(f'title: {task.title}')
            print(f'status: {task.status}')
            print(f'priority: {task.priority}')
            print(f'start: {task.start}')
            print(f'end: {task.end}')
            print(f'repeat: {task.repeat}')
            print('#' * 20)

    def call_process(self, args: argparse.Namespace) -> None:
        command = args.command

        action = getattr(self, f'{command}_cmd')
        action()
