#!/usr/bin/env bash

set -x

export PYTHONPATH=.
uv run pytest -vv --cov=pipenv_uv_migrate --cov-report=term ${@} tests
