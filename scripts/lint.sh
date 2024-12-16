#!/usr/bin/env bash

set -x

uv run mypy .
uv run ruff check .
uv run ruff format --check --diff .
