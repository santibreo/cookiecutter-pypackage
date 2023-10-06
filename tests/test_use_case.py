from pathlib import Path
from unittest import mock
from urllib import request

import pytest
from cookiecutter import main, exceptions


COOKIECUTTER_TEMPLATE_PATH = Path(__file__).parent.parent
COOKIECUTTER_TEMPLATE_LS = (
    '.github',
    '.github/workflows',
    '.github/workflows/publish-to-pypi.yaml',
    '.gitignore',
    '.pre-commit-config.yaml',
    'LICENSE',
    'Makefile',
    'README.rst',
    'pyproject.toml',
    'requirements-dev.txt',
    'sphinx',
    'sphinx/Makefile',
    'sphinx/source',
    'sphinx/source/_static',
    'sphinx/source/_static/css',
    'sphinx/source/_static/css/custom.css',
    'sphinx/source/_templates',
    'sphinx/source/conf.py',
    'sphinx/source/index.rst',
    'src',
    'tests',
    'tests/conftest.py',
    'tox.ini',
)


def test_project_creation(tmp_path: Path) -> None:
    with mock.patch('urllib.request.urlopen', spec=request.urlopen) as urlopen_mock:
        urlopen_mock.return_value = ''
        _ = main.cookiecutter(
            str(COOKIECUTTER_TEMPLATE_PATH),
            no_input=True,
            output_dir=str(tmp_path)
        )
    assert len(list(tmp_path.iterdir())) == 1, 'More than just 1 folder created'
    new_project_path = next(tmp_path.iterdir())
    assert new_project_path.name == 'awesome-python-project', 'Project name differs from expected'
    new_project_ls = [
        str(p.relative_to(new_project_path)) for p in new_project_path.rglob('*')
    ]
    additional_files = set(new_project_ls).difference(COOKIECUTTER_TEMPLATE_LS)
    assert not additional_files, f'Files {additional_files} created and not expected'
    missing_files = set(COOKIECUTTER_TEMPLATE_LS).difference(new_project_ls)
    assert not missing_files, f'Files {missing_files} not created and expected'


def test_project_name_is_checked(tmp_path: Path) -> None:
    with (
        mock.patch('urllib.request.urlopen', spec=request.urlopen) as urlopen_mock,
        pytest.raises(exceptions.FailedHookException)
    ):
        urlopen_mock.return_value = '<a class="package-snippet" href="/project/hola/"></a>'
        _ = main.cookiecutter(
            str(COOKIECUTTER_TEMPLATE_PATH),
            no_input=True,
            output_dir=str(tmp_path),
            extra_context={'project_name': 'hola'}
        )
    _ = main.cookiecutter(
        str(COOKIECUTTER_TEMPLATE_PATH),
        no_input=True,
        output_dir=str(tmp_path),
        extra_context={'project_name': 'hola', 'check_package_name': False}
    )
