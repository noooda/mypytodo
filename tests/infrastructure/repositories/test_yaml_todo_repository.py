import tempfile
import textwrap

import pytest

from mypytodo.infrastructure.repositories import YamlTodoRepository


@pytest.fixture
def yaml_content() -> str:
    return textwrap.dedent(
        '''
        - title: test
          status: pending
          priority: high
          deadline: 20250201
          description: test test test
          repeat: True
        - title: test2
          status: ongoing
          priority: middle
          deadline: 20250211
          description: test test test test
          repeat:
        '''
    )


@pytest.fixture
def expected_load_data() -> list[dict]:
    return [
        {
            'title': 'test',
            'status': 'pending',
            'priority': 'high',
            'deadline': 20250201,
            'description': 'test test test',
            'repeat': True,
        },
        {
            'title': 'test2',
            'status': 'ongoing',
            'priority': 'middle',
            'deadline': 20250211,
            'description': 'test test test test',
            'repeat': None,
        },
    ]


def test_load_todo_list(
    yaml_content: str, expected_load_data: list[dict]
) -> None:
    with tempfile.NamedTemporaryFile() as fp:
        with open(fp.name, 'w') as f:
            f.write(yaml_content)

        yaml_todo_repository = YamlTodoRepository(repository_path=fp.name)
        load_data = yaml_todo_repository.load()
        assert len(load_data) == 2
        assert load_data == expected_load_data


def test_fail_to_load_todo_list() -> None:
    yaml_todo_repository = YamlTodoRepository(repository_path='not/exist.yaml')
    with pytest.raises(FileNotFoundError):
        yaml_todo_repository.load()
