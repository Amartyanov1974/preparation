FROM python:3.11-alpine3.19

ARG BASE_DIR=/code

ENV \
    # python
    PYTHONUNBUFFERED=1 \
    # prevents python creating .pyc files
    PYTHONDONTWRITEBYTECODE=1 \
    \
    # poetry
    POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_CREATE=false \
    \
    # pip
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100

RUN pip install poetry==1.5.1
ENV PATH="/root/.local/bin:${PATH}"

WORKDIR ${BASE_DIR}
COPY . .
RUN poetry install --no-ansi
