#!/usr/bin/env bash

cd test && celery -A src.common.celery worker -l info --concurrency=2