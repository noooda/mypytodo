import argparse

import yaml


def main() -> None:
    parser = setup_parser()
    args = parser.parse_args()
    print(args)


def setup_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog='mypytodo', description='mypytodo manages your todo list'
    )

    subparsers = parser.add_subparsers(dest='command', required=True)

    list_parser = subparsers.add_parser('list', help='Shot todo list')
    list_parser.add_argument('--all', action='store_true', help='Show all')
    list_parser.add_argument('--sort', type=str, help='Sort by a property')

    return parser


if __name__ == '__main__':
    main()
