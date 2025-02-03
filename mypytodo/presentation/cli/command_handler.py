import argparse
from string import Template

from mypytodo.application.use_cases import ShowTodoList
from mypytodo.templates import TASK_DEFAULT


class CommandHandler:
    def __init__(self, show_todo_list: ShowTodoList) -> None:
        self._show_todo_list = show_todo_list

    def list_cmd(self) -> None:
        template = Template(TASK_DEFAULT)
        todo_list = self._show_todo_list.default()

        for i, task in enumerate(todo_list):
            result = template.substitute(
                id=task.id,
                title=task.title,
                status=task.status,
                priority=task.priority,
                start=task.start,
                end=task.end,
                repeat=task.repeat,
            )

            # TODO: 何かしらのRenderを実装した方が良さそう
            # TODO: repeatがTrueかどうかは色の濃さで判断させたい
            print('-' * 20)
            print(result)
            if i + 1 == len(todo_list):
                print('-' * 20)

    # TODO: list --detailだったり、list --filter title="hoge"に対応できるか考える
    def call_process(self, args: argparse.Namespace) -> None:
        command = args.command
        print(args)

        action = getattr(self, f'{command}_cmd')
        action()
