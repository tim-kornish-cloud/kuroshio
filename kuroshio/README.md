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
  - psql -U postgres -c "CREATE USER bloguser WITH PASSWORD 'blogpass';"
  - createdb -U postgres -O bloguser blog
  - createdb -U postgres -O bloguser test_blog
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
