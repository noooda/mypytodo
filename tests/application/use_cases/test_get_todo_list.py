from unittest.mock import Mock

import pytest

from mypytodo.application.interfaces import TodoRepository
from mypytodo.application.use_cases import GetTodoList
from mypytodo.core.models import Task


@pytest.fixture
def load_data() -> list[dict]:
    return [
        {
            'repeat': True,
            'title': 'test1',
            'priority': 'middle',
            'start': 20250211,
            'end': 20250220,
            'description': 'test test test test',
        },
        {
            'repeat': None,
            'title': 'test2',
            'priority': 'low',
            'start': 20250201,
            'end': 20250320,
            'description': 'test test test test test',
        },
        {
            'repeat': True,
            'title': 'test3',
            'priority': 'high',
            'start': 20250125,
            'end': 20250201,
            'description': 'test test test',
        },
    ]


def test_default(mocker: Mock, load_data: list[dict]) -> None:
    mock_todo_repository = mocker.Mock(spec=TodoRepository)
    mock_todo_repository.load.return_value = load_data
    mock_get_todo_list = GetTodoList(mock_todo_repository)

    todo_list = mock_get_todo_list.execute()
    mock_todo_repository.load.assert_called_once()
    assert len(todo_list) == 3
    assert isinstance(todo_list[0], Task)
    assert (
        todo_list[0].id
        == 'fd61a03af4f77d870fc21e05e7e80678095c92d808cfb3b5c279ee04c74aca13'
    )
    assert todo_list[0].start == 20250125
    assert todo_list[1].start == 20250201
    assert todo_list[2].start == 20250211
    assert todo_list[0].title == 'test3 [re]'
    assert todo_list[1].title == 'test2'
