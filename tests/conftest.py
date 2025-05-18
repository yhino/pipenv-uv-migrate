from pathlib import Path

import pytest


@pytest.fixture
def pipfile() -> Path:
    return Path("tests/testdata/toml/Pipfile")


@pytest.fixture
def pipfile_single_source() -> Path:
    return Path("tests/testdata/toml/Pipfile_single_source")


@pytest.fixture
def original_pyproject_toml() -> Path:
    return Path("tests/testdata/toml/pyproject.toml")


@pytest.fixture
def expect_pyproject_toml() -> Path:
    return Path("tests/testdata/toml/expect_pyproject.toml")


@pytest.fixture
def expect_single_source_pyproject_toml() -> Path:
    return Path("tests/testdata/toml/expect_single_source_pyproject.toml")


@pytest.fixture
def broken_pyproject_toml() -> Path:
    return Path("tests/testdata/toml/broken_pyproject.toml")


@pytest.fixture
def notfound_toml() -> Path:
    return Path("tests/testdata/toml/notfound.toml")
