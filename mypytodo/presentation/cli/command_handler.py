import argparse

from mypytodo.application.use_cases import GetTodoList
from mypytodo.presentation.cli.renderer import TaskRenderer


class CommandHandler:
    def __init__(self, get_todo_list: GetTodoList) -> None:
        self._get_todo_list = get_todo_list
        self.todo_list = self._get_todo_list.execute()

    def list_action(self, detail: bool, query: str | None = None) -> None:
        TaskRenderer.render(self.todo_list, detail)

    def call_process(self, args: argparse.Namespace) -> None:
        command = args.command
        del args.command

        action = getattr(self, f'{command}_action')
        action(**vars(args))
