# Contributing to shor

First off, thanks for your interest in contributing to the project!

We are excited to work with you.

We have setup a few tools and guidelines to help streamline the dev process and ensure consistency across the library.

## Developer Setup
Fork the repo, creating a copy of shor that you own and can make changes to.
Open a terminal session and change the directory to your forked repo.

### Install pipx
pipx is a utility for easily installing other Python command line tools.

https://pipxproject.github.io/pipx/
```
python3 -m pip install --user pipx
python3 -m pipx ensurepath
```

### Install poetry
poetry is a command line tool for dependency management, and package publishing. We use it to freeze our library and development dependencies to specific and compatible versions.

https://python-poetry.org/docs/basic-usage/
```
pipx install poetry
```

### Install the depenencies with poetry
```
poetry install
```

### Setup the pre-commit hooks
We currently use black and isort for auto-formatting, flake8 for linting (pep8) and pytest for unit tests. All of these run during the pre-commit hooks.
Much of this setup came from - https://sourcery.ai/blog/python-best-practices/#pipx
```
poetry run pre-commit install
```

## Opening a pull request
After you make your changes, make sure you write new unit tests to cover your changes.

It is important to maintain a high test coverage for this library.

You can run these tests with:
```
poetry run pytest --cov
```
