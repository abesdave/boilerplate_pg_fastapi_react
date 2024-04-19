# Postgres FastAPI React Boilerplate

##  Project structure:
The project is a monorepo with the following structure:
- Root
  - Frontend (React Application)
  - Backend (Fast API)
  - Database
    - Temporary database volumens

## Running the project:
To run the project follow the following steps.
The dev environment setup will be explained later.

### Using docker-compose:
The project can be started using docker compose from the root dir by issuing the following commands:
- `docker-compose up --build` or `docker-compose up`
- `docker-exec -it backend bash` to get bash shell on the backend container
  - `alembic upgrade head` to migrate the database to the latest revision
- Visit `localhost:8000/docs` to view the FastAPI documentation or visit `localhost:3000` to load the react frontend.

## The development environment and workflow
