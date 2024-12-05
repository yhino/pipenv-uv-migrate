#!/usr/bin/env bash

set -ue
set -x

uvx mypy .
uvx ruff check .
uvx ruff format --check --diff .
