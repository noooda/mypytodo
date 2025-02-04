import argparse

from mypytodo.application.use_cases import GetTodoList
from mypytodo.infrastructure.repositories import YamlTodoRepository
from mypytodo.presentation.cli import CommandHandler


def main() -> None:
    parser = setup_parser()
    command_handler = setup_command_handler()

    args = parser.parse_args()
    command_handler.call_process(args)


def setup_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog='mypytodo', description='mypytodo manages your todo list'
    )

    subparsers = parser.add_subparsers(dest='command', required=True)

    list_parser = subparsers.add_parser('list', help='Shot todo list')
    list_parser.add_argument('--all', action='store_true', help='Show all')
    list_parser.add_argument('--sort', type=str, help='Sort by a property')

    list_parser = subparsers.add_parser('edit', help='Shot todo list')
    list_parser.add_argument('--new', action='store_true', help='Show all')
    list_parser.add_argument('--update', type=str, help='Sort by a property')

    return parser


def setup_command_handler() -> CommandHandler:
    return CommandHandler(
        get_todo_list=GetTodoList(
            todo_repository=YamlTodoRepository('todo_list.yaml')
        )
    )


if __name__ == '__main__':
    main()
