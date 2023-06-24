# Diary56x backend

## Table of contents

- [Diary56x backend](#diary56x-backend)
  - [Table of contents](#table-of-contents)
  - [Development setup](#development-setup)
    - [Tools to install](#tools-to-install)
    - [Recommended VSCode plugins](#recommended-vscode-plugins)
    - [Dependencies](#dependencies)
    - [Server setup](#server-setup)
    - [VSCode configuration](#vscode-configuration)

## Development setup

### Tools to install

- [Python](https://python.org/downloads/)
- [Poetry](https://python-poetry.org) (can be installed with _pip_)

### Recommended VSCode plugins

- [Django](https://marketplace.visualstudio.com/items?itemName=batisteo.vscode-django)
- [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)

### Dependencies

```bash
poetry install
```

### Server setup

On your first run, you will need to migrate changes to a development database and create a new root admin user with Django:

```bash
# Django migrations
poetry run python manage.py makemigrations
poetry run python manage.py migrate

# You'll be asked to provide some data
# like your email, name, etc.
# Use 0 for account_type.
poetry run python manage.py createsuperuser
```

To start the server, run:

```bash
# Django development server
poetry run python manage.py runserver 0.0.0.0:8000
```

### VSCode configuration

Recommended VSCode ``.vscode/settings.json``:

```json
{
  "files.exclude": {
    "**/.git": true,
    ".venv": true,
    "**/__pycache__": true,
  },
  "python.pythonPath": ".venv/bin/python",
  "python.linting.enabled": true,
  "python.linting.lintOnSave": true,
  "python.linting.flake8Enabled": true,
  "python.formatting.provider": "black",
  "python.sortImports.args": ["-rc", "--atomic"],
  "[python]": {
    "editor.codeActionsOnSave": {
      "source.organizeImports": true
    }
  },
  "files.associations": {
    "**/templates/*.html": "django-html"
  },
  "emmet.includeLanguages": {
    "django-html": "html"
  },
}
```
