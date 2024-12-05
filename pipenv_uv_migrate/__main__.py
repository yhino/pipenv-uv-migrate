from pathlib import Path

import typer
from typing_extensions import Annotated

from pipenv_uv_migrate import __version__
from pipenv_uv_migrate.loader import (
    PipfileNotFoundError,
    PyprojectTomlNotFoundError,
)
from pipenv_uv_migrate.migration import MigrationOption, PipenvUvMigration

app = typer.Typer()


def show_version(is_show: bool) -> None:
    if is_show:
        typer.echo(f"{__version__}")
        raise typer.Exit


@app.command(
    context_settings={
        "help_option_names": ["-h", "--help"],
    },
)
def main(
    pipfile: Annotated[
        Path,
        typer.Option(
            "--pipfile",
            "-f",
            help="path to Pipfile",
        ),
    ],
    pyproject_toml: Annotated[
        Path,
        typer.Option(
            "--pyproject-toml",
            "-t",
            help="path to pyproject.toml",
        ),
    ],
    re_migrate: Annotated[
        bool,
        typer.Option(
            "--re-migrate",
            help="""
            re-migrate a dependency if it already exists in the poetry dependency.
            however, if a dependency is removed from pipenv,
            it does not remove the poetry dependency
        """,
        ),
    ] = False,
    dry_run: Annotated[
        bool,
        typer.Option(
            "--dry-run",
            "-n",
            help="dry-run",
        ),
    ] = False,
    _: Annotated[
        bool,
        typer.Option(
            "--version",
            "-v",
            help="show version",
            callback=show_version,
            is_eager=True,
        ),
    ] = False,
) -> None:
    """Migrate pipenv to uv"""
    try:
        PipenvUvMigration(
            pipfile,
            pyproject_toml,
            option=MigrationOption(
                re_migrate=re_migrate,
                dry_run=dry_run,
            ),
        ).migrate()
    except PipfileNotFoundError as exc:
        typer.secho(f"Pipfile '{pipfile}' not found", err=True, fg=typer.colors.RED)
        raise typer.Exit(code=1) from exc
    except PyprojectTomlNotFoundError as exc:
        typer.secho("Please run `uv init` first", err=True, fg=typer.colors.RED)
        raise typer.Exit(code=1) from exc


if __name__ == "__main__":
    app()
