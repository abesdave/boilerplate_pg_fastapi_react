# Getting Started:
A mono repo with the backend and frontend in a single repo.
When running the project 3 containers will be spun up:
- database (postgres)
- backend (fastapi)
- frontend (react)

## System Requirements: 
- Docker

## Running the project
- Download the project
- open the root of the project
- run command `docker-compose up --build`
- log into backend container `docker-compose exec -it backend bash` and then run the alembic migration `alembic upgrade head`
- access frontend on localhost:5137/data
- the backend is configured to run on localhost:8000
- to shut down the projec run `docker-compose down`

# Project features:
- backend and frontend try use the repository pattern
- some basic unit tests are available in login-controller
- nice dockerized developer environment

# Project needs:
- could use some more polish and a review of the overall architecture.
- may not properly conform to the zens of python.

# Video Recordings:
https://1drv.ms/v/c/75a7f3715f3a408c/ETQ0F8KwZURLmuQmg1wwpL0BpKpjQSyLPHU8Lc-BRpoocw?e=xOHju6