from pathlib import Path

import tomlkit
from tomlkit import table

from pipenv_uv_migrate import __version__


def test_version() -> None:
    with Path("pyproject.toml").open("r") as f:
        pyproject = tomlkit.loads(f.read())
    project = pyproject.get("project", table(is_super_table=True))
    assert __version__ == project.get("version")
