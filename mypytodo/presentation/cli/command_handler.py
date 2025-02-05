import argparse

from mypytodo.application.use_cases import GetTodoList
from mypytodo.presentation.cli.renderer import TaskRenderer


class CommandHandler:
    def __init__(self, get_todo_list: GetTodoList) -> None:
        self._get_todo_list = get_todo_list
        self.todo_list = self._get_todo_list.execute()

    def list_cmd(self) -> None:
        for task in self.todo_list:
            TaskRenderer.render(task)

    # TODO: list --detailだったり、list --filter title="hoge"に対応できるか考える
    def call_process(self, args: argparse.Namespace) -> None:
        command = args.command

        action = getattr(self, f'{command}_cmd')
        action()
