FROM python:3.10

WORKDIR /App
COPY pyproject.toml poetry.lock ./
RUN pip install poetry
RUN poetry install
RUN poetry lock
COPY . .

CMD ["poetry", "run", "uvicorn", "App.main:app", "--host", "0.0.0.0", "--port", "7000"]
