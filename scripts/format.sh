#!/usr/bin/env bash

set -x

uv run ruff check --fix .
uv run ruff format .
