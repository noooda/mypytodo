from unittest.mock import Mock

import pytest

from mypytodo.application.interfaces import TodoRepository
from mypytodo.application.use_cases import ShowTodoList
from mypytodo.core.models import Task


@pytest.fixture
def load_data() -> list[dict]:
    return [
        {
            'title': 'test',
            'status': 'pending',
            'priority': 'high',
            'start': 20250125,
            'end': 20250201,
            'description': 'test test test',
            'repeat': True,
        },
        {
            'title': 'test2',
            'status': 'ongoing',
            'priority': 'middle',
            'start': 20250211,
            'end': 20250220,
            'description': 'test test test test',
            'repeat': None,
        },
        {
            'title': 'test3',
            'status': 'ongoing',
            'priority': 'low',
            'start': 20250201,
            'end': 20250320,
            'description': 'test test test test test',
            'repeat': True,
        },
    ]


# TODO: default()の実装が変わったので、テストを修正する
def test_default(mocker: Mock, load_data: list[dict]) -> None:
    mock_todo_repository = mocker.Mock(spec=TodoRepository)
    mock_todo_repository.load.return_value = load_data
    list = ShowTodoList(mock_todo_repository)

    todo_list = list.default()
    mock_todo_repository.load.assert_called_once()
    assert len(todo_list) == 2
    assert isinstance(todo_list[0], Task)
