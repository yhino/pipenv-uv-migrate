<h1 align="center">pipenv-uv-migrate</h1>
<p align="center">This is simple migration script, migrate pipenv to uv.</p>

<p align="center">
    <a href="https://pypi.org/project/pipenv-uv-migrate/"><img alt="PyPI - Python Version" src="https://img.shields.io/pypi/pyversions/pipenv-uv-migrate"></a>
    <a href="https://pypi.org/project/pipenv-uv-migrate/"><img src="https://img.shields.io/pypi/dm/pipenv-uv-migrate" alt="PyPI - Downloads"></a>
    <a href="https://github.com/yhino/pipenv-uv-migrate/actions/workflows/test.yml"><img src="https://github.com/yhino/pipenv-uv-migrate/actions/workflows/test.yml/badge.svg" alt="Test"></a>      
    <a href="https://codecov.io/gh/yhino/pipenv-uv-migrate" ><img src="https://codecov.io/gh/yhino/pipenv-uv-migrate/graph/badge.svg?token=ZKkbXAb46g"/></a>
    <a href="https://app.fossa.com/projects/git%2Bgithub.com%2Fyhino%2Fpipenv-uv-migrate?ref=badge_shield"><img src="https://app.fossa.com/api/projects/git%2Bgithub.com%2Fyhino%2Fpipenv-uv-migrate.svg?type=shield" alt="FOSSA Status"></a>
</p>

## :rocket: Get Started

### Installation

    $ uv tool install pipenv-uv-migrate
    # -- or --
    $ pipx install pipenv-uv-migrate

### Migration

#### Step 1: Create `pyproject.toml` file

    $ uv init

#### Step 2: Migrate

To migrate `Pipfile` to `pyproject.toml`.

    $ pipenv-uv-migrate -f Pipfile -t pyproject.toml

When want to run dry-run mode:

    $ pipenv-uv-migrate -f Pipfile -t pyproject.toml -n

Dry-run mode is `pyproject.toml` file does not overwrite, results are displayed on standard output.

> [!Note]  
> If the dependency already exists in the project dependency and you want to re-migrate it, please use the `--re-migrate` option.
> However, if the dependency is removed from pipenv, the project dependency will not be removed.
>
>     $ pipenv-uv-migrate -f Pipfile -t pyproject.toml --re-migrate

#### Step 3: Generate lock file

    $ uv lock

If there is already a `uv.lock` file, remove it first.

#### Step 4: Installing dependencies

To install the defined dependencies for your project.

    $ uv sync

### Example output

This is an example of a Pipfile to be migrated.

```toml
[[source]]
url = "https://pypi.python.org/simple"
verify_ssl = true
name = "pypi"

[packages]
requests = "*"

[dev-packages]
pytest = ">=5.2"
```

Migrate the above file to the following pyproject.toml.

```toml
[project]
name = "migrate-sample"
version = "0.1.0"
description = "Add your description here"
readme = "README.md"
authors = [
    { name = "Yoshiyuki HINO", email = "yhinoz@gmail.com" }
]
requires-python = ">=3.9"
dependencies = []

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"
```

By executing this script, pyproject.toml is rewritten as follows.

```toml
[project]
name = "migrate-sample"
version = "0.1.0"
description = "Add your description here"
readme = "README.md"
authors = [
    { name = "Yoshiyuki HINO", email = "yhinoz@gmail.com" }
]
requires-python = ">=3.9"
dependencies = [
    "requests",
]

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[dependency-groups]
dev = [
    "pytest>=5.2",
]
```

> [!Note]  
> If the version of the dependent package is not specified, it will also be migrated. but the following warning will be displayed when lock or sync is performed with uv.
>
>     warning: Missing version constraint (e.g., a lower bound) for `requests`.
>
> Please specify the version after migration.

## :handshake: Contributing

1. Fork and clone the repository, and create the development branch.
2. Run `uv pip install -U -r pyproject.toml` to setup your develop environment.
3. Do your code.
4. Run `bash scripts/test.sh` to check that your test passed.
5. Run `bash scripts/format.sh` and `bash scripts/lint.sh` to check that you haven't warnings.
6. Open a PR on GitHub.

### Test cases

Test cases are in `tests/testdata/toml`, update `Pipfile` with additional entries and `expect_pyproject.toml` with expected output.


## :pencil: License

[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2Fyhino%2Fpipenv-uv-migrate.svg?type=large)](https://app.fossa.com/projects/git%2Bgithub.com%2Fyhino%2Fpipenv-uv-migrate?ref=badge_large)
