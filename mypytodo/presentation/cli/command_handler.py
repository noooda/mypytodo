import argparse

from termcolor import colored

from mypytodo.application.use_cases import GetTodoList


class CommandHandler:
    def __init__(self, get_todo_list: GetTodoList) -> None:
        self._get_todo_list = get_todo_list
        self.todo_list = self._get_todo_list.execute()

    def list_cmd(self) -> None:
        for task in self.todo_list:
            output = (
                f'{task.id}\n'
                f'{task.title}\n'
                f'{task.start}\n'
                f'{task.end}\n'
            )
            if task.priority == 'high':
                print(colored(output, 'red'))
            elif task.priority == 'middle':
                print(colored(output, 'yellow'))
            else:
                print(output)

    # TODO: list --detailだったり、list --filter title="hoge"に対応できるか考える
    def call_process(self, args: argparse.Namespace) -> None:
        command = args.command

        action = getattr(self, f'{command}_cmd')
        action()
