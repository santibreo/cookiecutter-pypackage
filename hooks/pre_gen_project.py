#!/usr/bin/env python
"""Checks that selected project name is not currently in use in PyPI"""

from urllib import request
from html.parser import HTMLParser


PROJECT_NAME = '{{ cookiecutter.project_name }}'
CHECK_NAME = '{{ cookiecutter.check_package_name }}'.lower() == 'true'


class ProjectNameChecker(HTMLParser):
    R"""Retrieves all projects when querying `PyPI <https://pypi.org>`_ for the
    given ``project_name``.

    Projects are extracted from response HTML as they come in hyperlinks like: \::

        <a class="package-snippet" href="/project/<project_name>/">

    Once all projects are retrieved, the :attr:`~.is_in_use` is defined indicating
    if given ``project_name`` is already in use or not.
    """

    def __init__(self, project_name: str, *, convert_charrefs: bool = True) -> None:
        super().__init__(convert_charrefs=convert_charrefs)
        response = request.urlopen(f'https://pypi.org/search/?q={project_name}')
        resp_text = response.read().decode()
        self.projects: dict[str, str] = {}
        self.feed(resp_text)
        self.is_in_use = project_name in self.projects

    def handle_starttag(self, tag, attrs):
        """Scans all opening tags (like <a>)

        Args:
            tag: The tag identifier, e.g. `html`, `div`, `p`, `a`, ....
            attrs: The attributes of the tag as a list of 2-tuples:  attribute
                name and attribute value (if any)

        Return:
            Nothing. Just fills the ``projects`` attribute of the instance.
        """
        attrs = dict(attrs)
        if tag != 'a':
            return
        if 'class' not in attrs:
            return
        if 'package-snippet' not in (attrs['class'] or '').split():
            return
        project_href = attrs['href']
        assert project_href is not None, f'Project {attrs} has no link'
        project_name = list(filter(bool, project_href.split('/')))[-1]
        if project_name in self.projects:
            raise ValueError(f'Multiple projects with name: {project_name}')
        self.projects[project_name] = project_href


if __name__ == '__main__':
    if CHECK_NAME:
        project_name_checker = ProjectNameChecker(project_name=PROJECT_NAME)
        if project_name_checker.is_in_use:
            raise ValueError("There is already a project named '{}' in PyPI: {}".format(
                PROJECT_NAME, f'https://pypi.org{project_name_checker.projects[PROJECT_NAME]}'
            ))
