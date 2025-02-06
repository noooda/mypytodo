from string import Template

from termcolor import colored

from mypytodo.core.models import Task

TEMPLATE = '''\
$_id
$_title
$_start
$_end
'''

TEMPLATE_DETAIL = '''\
$_id
$_title
$_start
$_end
$_description
'''


class TaskRenderer:
    @classmethod
    def render(cls, todo_list: list[Task], detail: bool) -> None:
        rendering_template = (
            Template(TEMPLATE)
            if detail is False
            else Template(TEMPLATE_DETAIL)
        )

        for task in todo_list:
            output = rendering_template.substitute(**vars(task))
            if task.priority == 'high':
                print(colored(output, 'red'))
            elif task.priority == 'middle':
                print(colored(output, 'yellow'))
            else:
                print(output)
