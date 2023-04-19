FROM mcr.microsoft.com/devcontainers/python:0-3.10

WORKDIR /code

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT python app/main.py