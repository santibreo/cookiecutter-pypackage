#!/usr/bin/env python
"""Creates the ``src`` folder to induce
`src-layout <https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/>`_
for the project
"""

from pathlib import Path


PROJECT_PATH = Path('.').resolve()


if __name__ == '__main__':
    (PROJECT_PATH / 'src').mkdir()
