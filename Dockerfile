FROM python:3.12 as base

WORKDIR /app/
COPY ./pyproject.toml ./poetry.lock* /app/
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONPATH=/app

RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=/opt/poetry python && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry && \
    poetry config virtualenvs.create false

FROM base AS alembic
COPY ./alembic.ini /app/
COPY ./alembic /app
RUN bash -c "poetry install --no-root"

FROM base as dev
COPY ./alembic.ini /app/
COPY ./app /app/app
EXPOSE 5678
RUN bash -c "poetry install --no-root"
ENTRYPOINT ["python3", "-m", "debugpy", "--listen", "0.0.0.0:5678", "-m", "uvicorn", "app.main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]

# FROM base as prod
# COPY ./app /app/app
# EXPOSE 8000
# RUN bash -c "poetry install --no-root --only main"
# ENTRYPOINT ["uvicorn", "app.main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]

# FROM base as staging
# EXPOSE 8000
# COPY ./requirements.staging.txt /app/app
# COPY ./.env.staging /app
# ENV ENV_FILE_PATH="/app/.env.staging"
# RUN if [ -f "$ENV_FILE_PATH" ]; then export $(cat $ENV_FILE_PATH | xargs); fi
# RUN bash -c "pip install --upgrade pip && pip install -r requirements.staging.txt"