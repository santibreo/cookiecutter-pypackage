#!/usr/bin/env python
"""Creates the ``src/{{ cookiecutter.project_name }}`` folder to induce
`src-layout <https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/>`_
for the project
"""

from pathlib import Path


PROJECT_PATH = Path('.').resolve()
PROJECT_NAME = '{{ cookiecutter.project_name }}'


if __name__ == '__main__':
    (PROJECT_PATH / 'src' / PROJECT_NAME).mkdir(parents=True)
    __init__path = PROJECT_PATH / 'src' / PROJECT_NAME / '__init__.py'
    __init__path.write_text('''\
"""Defines package version dynamically"""

import sys
import subprocess


def _get_version_from_git_tags(default='v0.0.1-alpha'):
    cmd = subprocess.run(['git', 'tag'], capture_output=True)
    cmd.check_returncode()
    return next(map(str.strip, cmd.stdout.decode().splitlines()), default)


# If you do following line, function is called everytime package is imported
# but using class approach, only when accessing `__version__` function is called

#  __version__ = _get_version_from_git_tags()


class This(sys.__class__):

    @property
    def __version__(self) -> str:
        return _get_version_from_git_tags()


sys.modules[__name__].__class__ = This
''')
