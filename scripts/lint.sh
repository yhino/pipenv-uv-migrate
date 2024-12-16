#!/usr/bin/env bash

set -x

uvx mypy .
uvx ruff check .
uvx ruff format --check --diff .
