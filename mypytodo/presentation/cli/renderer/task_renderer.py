from termcolor import colored

from mypytodo.core.models import Task


class TaskRenderer:
    @classmethod
    def render(cls, task: Task) -> None:
        template = (
            f'{task.id}\n' f'{task.title}\n' f'{task.start}\n' f'{task.end}\n'
        )
        if task.priority == 'high':
            print(colored(template, 'red'))
        elif task.priority == 'middle':
            print(colored(template, 'yellow'))
        else:
            print(template)

    @classmethod
    def render_detailed(cls, task: Task) -> None:
        pass
