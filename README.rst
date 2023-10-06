##########################
Python package boilerplate
##########################

There must be a thousand of these around, including the one that is used in the `cookiecutter turorial <https://cookiecutter.readthedocs.io/en/latest/tutorials/tutorial1.html#case-study-cookiecutter-pypackage>`_, so this is just one more.

****
Why?
****

- You are prompted just for 5 things.
- This contains boilerplate for:

  - Testing your package using `pytest <https://docs.pytest.org/en/7.3.x/contents.html>`_
  - Analysing test coverage of your package using `coverage <https://coverage.readthedocs.io/en/7.3.2/>`_
  - Documenting your package with `Sphinx <https://www.sphinx-doc.org/en/master/>`_.
  - Publishing documentation as a static website with `Github Pages <https://pages.github.com/>`_
  - Publishing your package in `PyPI <https://pypi.org/>`_ when you push a tag to the ``main`` branch.
  - Using `pre-commit <https://pre-commit.com/>`_ hooks to ensure style alignment and code quality.
  - Using `tox <https://tox.wiki/en/4.11.3/>`_ to be sure that everything works fine in multiple Python versions (and compile documentation)
  - Using make to make your life much simpler
  - Checking that your package name is not currently in use in PyPI.


**********
How to use
**********

This can be used normally with `cookiecutter <https://cookiecutter.readthedocs.io/en/latest>`_ just run:\ ::

  $ cookiecutter gh:santibreo/cookiecutter-pypackage

To make the Github Workflow work you need to:

1. Create an environment in your remote repo called 'release'.
2. Configure a trusted publishing for your PyPI project.

If this is your first time best follow `this tutorial <https://packaging.python.org/en/latest/guides/publishing-package-distribution-releases-using-github-actions-ci-cd-workflows/>`_ (this workflow does not contain the signing part).

To publish the documentation to Github Pages you have to go to remote repo Settings > Pages and there select a branch and `docs` folder.
