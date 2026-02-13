#!/usr/bin/env bash

set -ue
set -x

uv run ruff check --fix .
uv run ruff format .
