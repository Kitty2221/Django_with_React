FROM python:3.8-slim

RUN apt-get update && apt-get install -y gettext

ADD . /test

ENV PYTHONPATH ''${PYTHONPATH}/test''
ENV PYTHONBUFFERED 1

RUN chmod +x /test/docker/scripts/api.entrypoint.dev.sh && \
    chmod +x /test/docker/scripts/wait-for-it.sh

RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r /test/requirements/dev.txt
