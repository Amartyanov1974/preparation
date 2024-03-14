FROM python:3.9-alpine3.12

LABEL maintainer="bot"

WORKDIR /code

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . .

RUN python -m pip install --no-cache-dir -r requirements.txt
