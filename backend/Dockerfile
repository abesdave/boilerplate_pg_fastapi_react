FROM python:3.12 as base

WORKDIR /app/

RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=/opt/poetry python && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry && \
    poetry config virtualenvs.create false

COPY ./pyproject.toml ./poetry.lock* /app/

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONPATH=/app

COPY ./alembic.ini /app/
COPY ./app /app/app

FROM base as dev
EXPOSE 5678
RUN bash -c "poetry install --no-root"
ENTRYPOINT ["python3", "-m", "debugpy", "--listen", "0.0.0.0:5678", "-m", "uvicorn", "app.main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]

FROM base as prod
EXPOSE 8000
RUN bash -c "poetry install --no-root --only main"
ENTRYPOINT ["uvicorn", "app.main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]