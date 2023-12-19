# FastApi

## Requirements:

- Docker CE/Desktop 20 or above

- Python 3.11

- [pipx](https://pipx.pypa.io/stable/installation/) and [poetry](https://python-poetry.org/docs/#installing-with-pipx)

## Development:

1. Prepare

- Install dependencies: `poetry install`
- Activate venv: `poetry shell`

2. Install lib

- production: `poetry install <lib-name>`
- dev: `poetry install -Gdev <lib-name>`

3. Run

- Run in local: `poetry run start`

4. Migration
- Generate new migration: `alembic revision --autogenerate -m "<message here>"`
- Run migration: `alembic upgrade head`
