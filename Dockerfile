FROM python:3.9-alpine
LABEL authors="Henry Gamba"

COPY ./requirements.txt /tmp/requirements.txt

COPY ./app /app

WORKDIR /app

EXPOSE 8000

RUN python -m venv /venv  \
    && /venv/bin/pip install --upgrade pip \
    && apk add --update --no-cache postgresql-client \
    && apk add --update --no-cache --virtual .tmp-build-deps build-base postgresql-dev musl-dev \
    && /venv/bin/pip install -r /tmp/requirements.txt \
    && adduser --disabled-password --no-create-home fastapi \
    && rm -f .tmp-build-deps

ENV PATH="/venv/bin:$PATH"

USER fastapi
