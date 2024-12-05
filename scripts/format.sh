#!/usr/bin/env bash

set -ue
set -x

uvx ruff check --fix .
uvx ruff format .
