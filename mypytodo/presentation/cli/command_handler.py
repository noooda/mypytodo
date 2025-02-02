import argparse

from mypytodo.application.use_cases import ShowTodoList


class CommandHandler:
    def __init__(self, show_todo_list: ShowTodoList) -> None:
        self.list_command = show_todo_list

    def call_process(self, args: argparse.Namespace) -> None:
        command = args.command
        action = getattr(self, f'{command}_command')
        action()
