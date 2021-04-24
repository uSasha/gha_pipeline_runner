FROM python:3.8-buster

ARG sentry_dsn

ENV SENTRY_DSN=$sentry_dsn
ENV PYTHONPATH="${PYTHONPATH}:/app/src"
ENV PYTHONPATH="${PYTHONPATH}:/app"

RUN groupadd -r app && useradd -r -m -g app app

COPY tox.ini /app/
COPY requirements.txt /app/
RUN pip install -r /app/requirements.txt

USER app
WORKDIR /app/src

COPY ./src /app/src
COPY ./tests /app/tests

CMD ["python", "app.py"]