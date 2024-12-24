FROM python:3.10

WORKDIR /server
COPY pyproject.toml poetry.lock ./
RUN pip install poetry
RUN poetry install
RUN poetry lock
COPY . .
CMD ["poetry", "run", "alembic", "upgrade", "head"]

CMD ["poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "7000"]
