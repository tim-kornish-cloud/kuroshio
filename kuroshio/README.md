# KuroShio

Similar project to Salesforce Jetstream for querying data and metadata from salesforce with added functionality for generating mapping documents and other features.

## console commands

- add package:
  - uv add pandas
  - uv add fastapi
  - uv add simple_salesforce
### run app
  - uv run fastapi dev main.py

### create secret_key in terminal
  - python -c "import secrets; print(secrets.token_hex(32))"
### Postgres commands
  - psql -U postgres
    - access command line
  - psql -U postgres -c "CREATE USER kuroshio WITH PASSWORD '<put password here>';"
  - createdb -U postgres -O kuroshio kuroshio_db
  - createdb -U postgres -O kuroshio test_kuroshio_db
### postgres command line:
  - \l - list all database
  - \c <dbname> connect to specific db
  - \dt list all table in current database
  - \d <tablename> describe table, columns, datatypes, indexes...
  - \dn list all schemas on db
  - \dv list all views on db
  - \du list all users and privileges
  - \dx	List installed extensions.
  - \q quit out of postgres terminal
  - \i filename.sql	Execute an SQL file directly from inside the session.

### Run alembic for database setup/migration

  - Modify alembic.ini in /kuroshio folder
  - Modify env.py in /kuroshio/alembic folder

  - uv run alembic init -t async alembic
  - uv run alembic revision --autogenerate -m "initial schema"
    - --autogenerate creates migration file, but does not execute it
  - uv run alembic upgrade head
    - update migrations based on latest version in version folder
    - (this is the execution of migration file)
  - uv run alembic current
    - check state on latest alembic migration
  - uv run alembic downgrade -1
    - go back one migration
### pytest commands
  - uv run pytest tests/test_posts.py -v
  - uv run pytest tests/test_users.py -v
  - uv run pytest tests/ -v
  - uv run pytest tests/
  - uv run pytest tests/test_posts.py::test_get_posts_empty -v
