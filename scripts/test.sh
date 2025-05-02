#!/usr/bin/env bash

set -x

export PYTHONPATH=.
uv run --active pytest -vv --cov=pipenv_uv_migrate --cov-report=term ${@} tests
