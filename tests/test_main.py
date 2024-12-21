from pathlib import Path

from typer.testing import CliRunner

from pipenv_uv_migrate import __version__
from pipenv_uv_migrate.__main__ import app

runner = CliRunner(mix_stderr=False)


def test_main(
    pipfile: Path,
    original_pyproject_toml: Path,
) -> None:
    argv = ["-f", str(pipfile), "-t", str(original_pyproject_toml), "-n"]
    result = runner.invoke(app, argv)

    assert result.exit_code == 0
    assert result.stdout != ""


def test_main_show_version() -> None:
    argv = ["-v"]
    result = runner.invoke(app, argv)

    assert result.exit_code == 0
    assert __version__ in result.stdout
    assert result.stderr == ""


def test_main_raise_pipfile_not_found_error(
    original_pyproject_toml: Path,
    notfound_toml: Path,
) -> None:
    argv = ["-f", str(notfound_toml), "-t", str(original_pyproject_toml), "-n"]
    result = runner.invoke(app, argv)

    assert result.exit_code == 1
    assert result.stdout == ""
    assert f"Pipfile '{notfound_toml}' not found" in result.stderr


def test_main_raise_pyproject_toml_not_found_error(
    pipfile: Path,
    notfound_toml: Path,
) -> None:
    argv = ["-f", str(pipfile), "-t", str(notfound_toml), "-n"]
    result = runner.invoke(app, argv)

    assert result.exit_code == 1
    assert result.stdout == ""
    assert "Please run `uv init` first" in result.stderr
