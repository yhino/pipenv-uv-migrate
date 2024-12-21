from pathlib import Path
from typing import Any, Callable

import pytest

from pipenv_uv_migrate.loader import load_toml
from pipenv_uv_migrate.migration import MigrationOption, PipenvUvMigration


@pytest.fixture
def load_fixture(request: pytest.FixtureRequest) -> Callable[[str], Any]:
    def _load_fixture(fixture_name: str) -> Any:
        return request.getfixturevalue(fixture_name)

    return _load_fixture


@pytest.mark.parametrize(
    ("pipfile_", "original_pyproject_toml_", "expect_pyproject_toml_"),
    [
        (
            "pipfile",
            "original_pyproject_toml",
            "expect_pyproject_toml",
        ),
    ],
)
def test_migrate(
    pipfile_: str,
    original_pyproject_toml_: str,
    expect_pyproject_toml_: str,
    tmp_path: Path,
    load_fixture: Callable[[str], Any],
) -> None:
    replica_pyproject_toml = tmp_path.joinpath("pyproject")
    replica_pyproject_toml.write_bytes(
        load_fixture(original_pyproject_toml_).read_bytes()
    )

    pipenv_uv_migrate = PipenvUvMigration(
        load_fixture(pipfile_),
        replica_pyproject_toml,
        option=MigrationOption(),
    )
    pipenv_uv_migrate.migrate()

    actual = load_toml(pipenv_uv_migrate.pyproject_toml)
    expect = load_toml(load_fixture(expect_pyproject_toml_))
    assert actual == expect


@pytest.mark.parametrize(
    ("pipfile_", "original_pyproject_toml_", "expect_pyproject_toml_"),
    [
        (
            "pipfile",
            "original_pyproject_toml",
            "expect_pyproject_toml",
        ),
    ],
)
def test_migrate_with_re_migrate(
    pipfile_: str,
    original_pyproject_toml_: str,
    expect_pyproject_toml_: str,
    tmp_path: Path,
    load_fixture: Callable[[str], Any],
) -> None:
    replica_pyproject_toml = tmp_path.joinpath("pyproject")
    replica_pyproject_toml.write_bytes(
        load_fixture(original_pyproject_toml_).read_bytes()
    )

    pipenv_uv_migrate = PipenvUvMigration(
        load_fixture(pipfile_),
        replica_pyproject_toml,
        option=MigrationOption(
            re_migrate=True,
        ),
    )
    pipenv_uv_migrate.migrate()

    actual = load_toml(pipenv_uv_migrate.pyproject_toml)
    expect = load_toml(load_fixture(expect_pyproject_toml_))
    assert actual == expect
