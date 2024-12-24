FROM python:3.10-slim
WORKDIR /client

COPY pyproject.toml poetry.lock ./

RUN pip install poetry
RUN poetry install
RUN poetry lock
COPY . .
CMD ["poetry","run","python", "app.py"]
EXPOSE 5000
