FROM python:3.8-slim

RUN apt-get update && apt-get install -y gettext

ADD . /test

RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r /test/requirements/dev.txt

WORKDIR test/src