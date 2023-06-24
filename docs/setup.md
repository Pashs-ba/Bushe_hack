# Setup

## Prerequisites

Before you start, make sure that [Python](https://python.org/downloads/),
[Poetry](https://python-poetry.org), and
[Yarn](https://yarnpkg.com)/[NPM](https://www.npmjs.com/package/npm) are installed.

## Dependencies

To install backend dependencies with Poetry, run:

``` bash
cd backend
poetry install
```

Frontend dependencies are installed with Yarn.

``` bash
cd frontend
yarn
```

## Django server

Apply Django database migrations on your first run:

``` bash
poetry run python manage.py makemigrations
poetry run python manage.py migrate
```

Additionally, you may need to create a new superuser
in order to access the Django admin interface:

``` bash
poetry run python manage.py createsuperuser
```

You'll be asked to provide some data. For `account_type`,
specify `0`.

To start Django server, run:

``` bash
poetry run python manage.py runserver 0.0.0.0:8000
```

## Vite server

The server can be started with:

```bash
yarn dev
```

## Recommended VSCode config

Recommended VSCode ``.vscode/settings.json``:


