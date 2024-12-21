from pathlib import Path

import pytest
from tomlkit import table
from tomlkit.exceptions import ParseError
from tomlkit.toml_document import TOMLDocument

from pipenv_uv_migrate.loader import (
    PipfileNotFoundError,
    PyprojectTomlNotFoundError,
    load_pipfile,
    load_pyproject_toml,
    load_toml,
)


def test_load_toml(original_pyproject_toml: Path) -> None:
    toml = load_toml(original_pyproject_toml)

    assert isinstance(toml, TOMLDocument)
    assert (
        toml.get("project", table(is_super_table=True)).get("name")
        == "pipenv-uv-migrate-test"
    )


def test_load_toml_file_not_found(notfound_toml: Path) -> None:
    with pytest.raises(FileNotFoundError):
        load_toml(notfound_toml)


def test_load_toml_parse_error(broken_pyproject_toml: Path) -> None:
    with pytest.raises(ParseError):
        load_toml(broken_pyproject_toml)


def test_load_pipfile(pipfile: Path) -> None:
    toml = load_pipfile(pipfile)

    assert isinstance(toml, TOMLDocument)


def test_load_pipfile_fails_file_not_found(notfound_toml: Path) -> None:
    with pytest.raises(PipfileNotFoundError):
        load_pipfile(notfound_toml)


def test_load_pyproject_toml(original_pyproject_toml: Path) -> None:
    toml = load_pyproject_toml(original_pyproject_toml)

    assert isinstance(toml, TOMLDocument)


def test_load_pyproject_toml_fails_file_not_found(notfound_toml: Path) -> None:
    with pytest.raises(PyprojectTomlNotFoundError):
        load_pyproject_toml(notfound_toml)
