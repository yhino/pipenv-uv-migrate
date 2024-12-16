#!/usr/bin/env bash

set -x

uvx ruff check --fix .
uvx ruff format .
