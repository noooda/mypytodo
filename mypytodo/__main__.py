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

    list_parser = subparsers.add_parser('list', help='Show todo list')
    list_parser.add_argument(
        '--detail', action='store_true', help='Show in detail'
    )
    list_parser.add_argument('--query', type=str, help='Sort by the query')

    list_parser = subparsers.add_parser('edit', help='Edit a task')
    list_parser.add_argument(
        '--id', required=True, type=str, help='Specify task id'
    )
    list_parser.add_argument('--title', type=str, help='New title')
    list_parser.add_argument('--priority', type=str, help='New priority')
    list_parser.add_argument('--start', type=str, help='New start')
    list_parser.add_argument('--end', type=str, help='New end')
    list_parser.add_argument('--description', type=str, help='New description')
    list_parser.add_argument('--repeat', type=str, help='True or Blank')

    list_parser = subparsers.add_parser('remove', help='Remove a task')
    list_parser.add_argument(
        '--id', required=True, type=str, help='Specify task id'
    )

    return parser


def setup_command_handler() -> CommandHandler:
    return CommandHandler(
        get_todo_list=GetTodoList(
            todo_repository=YamlTodoRepository('todo_list.yaml')
        )
    )


if __name__ == '__main__':
    main()
