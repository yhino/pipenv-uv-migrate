#!/usr/bin/env bash

set -x

export PYTHONPATH=.
uvx --with pytest-cov pytest -vv --cov=pipenv_uv_migrate --cov-report=term ${@} tests
