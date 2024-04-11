# Installing Dependencies:
To see how poetry is used to install deps, look at the github workflows, backend dockerfile etc.

# Alembic Migrations:

## Run Locally - uses env vars set by default in alembic.env file.
## Run inside docker container - uses env vars from the container setting.
- Create a new revision when new tables or updates are made:
`alembic revision -m "create new revision"`
- Run the migration:
`alembic upgrade head`
- Go back a version:
`alembic downgrade -1 (or head?)`