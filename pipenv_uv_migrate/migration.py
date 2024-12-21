from __future__ import annotations

import re
import sys
import warnings
from dataclasses import dataclass
from pathlib import Path

from packaging.markers import Marker
from packaging.requirements import Requirement
from packaging.specifiers import SpecifierSet
from tomlkit import aot, array, dumps, inline_table, key, table
from typing_extensions import Any

from pipenv_uv_migrate.loader import load_pipfile, load_pyproject_toml


@dataclass
class MigrationOption:
    re_migrate: bool = False
    dry_run: bool = False


class PipenvUvMigration:
    def __init__(
        self,
        pipfile: Path,
        pyproject_toml: Path,
        *,
        option: MigrationOption,
    ) -> None:
        self._pyproject_toml = pyproject_toml
        self._pipenv = load_pipfile(pipfile)
        self._pyproject = load_pyproject_toml(pyproject_toml)

        self._project = self._pyproject.get("project", table(is_super_table=True))
        self._pyproject["project"] = self._project
        self._project_dependencies = self._project.get("dependencies", array())
        self._project_dependencies = self._project_dependencies.multiline(True)  # noqa: FBT003
        self._project["dependencies"] = self._project_dependencies

        self._dependency_groups = self._pyproject.get("dependency-groups", table())
        self._pyproject["dependency-groups"] = self._dependency_groups
        self._dependency_groups_dev = self._dependency_groups.get("dev", array())
        self._dependency_groups_dev = self._dependency_groups_dev.multiline(True)  # noqa: FBT003
        self._dependency_groups["dev"] = self._dependency_groups_dev

        self._tool = self._pyproject.get("tool", table(is_super_table=True))
        self._pyproject["tool"] = self._tool
        self._tool_uv = self._tool.get("uv", table())
        self._tool["uv"] = self._tool_uv
        self._tool_uv_sources = self._tool_uv.get("sources", table())
        self._tool_uv["sources"] = self._tool_uv_sources
        self._tool_uv_index = self._tool_uv.get("index", aot())
        self._tool_uv["index"] = self._tool_uv_index

        self._option = option

    @property
    def pyproject_toml(self) -> Path:
        return self._pyproject_toml

    def migrate(self) -> None:
        self._migrate_dependencies()
        self._migrate_dev_dependencies()
        self._migrate_scripts()
        self._migrate_source()
        self._save()

    def _migrate_dependencies(self) -> None:
        for raw_name, properties in self._pipenv.get("packages", {}).items():
            name, extras = split_extras(raw_name)
            formatted_properties = reformat_dependency_properties(extras, properties)
            r = Requirement(name)
            if "version" in formatted_properties:
                if formatted_properties["version"] == "*":
                    pass
                else:
                    r.specifier = SpecifierSet(formatted_properties["version"])
            if "extras" in formatted_properties:
                r.extras = set(formatted_properties["extras"])
            if "markers" in formatted_properties:
                r.marker = Marker(formatted_properties["markers"])
            self._project_dependencies.append(r.__str__())

            if "index" in formatted_properties:
                if formatted_properties["index"] == "pypi":
                    continue
                t = inline_table()
                t.add("index", formatted_properties["index"])
                self._tool_uv_sources.append(key(name), t)
            if "git" in formatted_properties:
                t = inline_table()
                t.add("git", formatted_properties["git"])
                if "ref" in formatted_properties:
                    k = "tag"
                    if formatted_properties["ref"] in ["master", "main"]:
                        k = "branch"
                    t.add(k, formatted_properties["ref"])
                if "editable" in formatted_properties:
                    warnings.warn(
                        f"cannot specify both `git` and `editable`; dependency={name}",
                        stacklevel=1,
                    )
                self._tool_uv_sources.append(key(name), t)
            if "path" in formatted_properties:
                t = inline_table()
                t.add("path", formatted_properties["path"])
                if "editable" in formatted_properties:
                    t.add("editable", True)  # noqa: FBT003
                self._tool_uv_sources.append(key(name), t)

    def _migrate_dev_dependencies(self) -> None:
        for raw_name, properties in self._pipenv.get("dev-packages", {}).items():
            name, extras = split_extras(raw_name)
            formatted_properties = reformat_dependency_properties(extras, properties)
            r = Requirement(name)
            if "version" in formatted_properties:
                if formatted_properties["version"] == "*":
                    pass
                else:
                    r.specifier = SpecifierSet(formatted_properties["version"])
            if "extras" in formatted_properties:
                r.extras = set(formatted_properties["extras"])
            if "markers" in formatted_properties:
                r.marker = Marker(formatted_properties["markers"])
            self._dependency_groups_dev.append(r.__str__())

            if "index" in formatted_properties:
                t = inline_table()
                t.add("index", formatted_properties["index"])
                self._tool_uv_sources.append(key(name), t)
            if "git" in formatted_properties:
                t = inline_table()
                t.add("git", formatted_properties["git"])
                if "ref" in formatted_properties:
                    k = "tag"
                    if formatted_properties["ref"] in ["master", "main"]:
                        k = "branch"
                    t.add(k, formatted_properties["ref"])
                if "editable" in formatted_properties:
                    warnings.warn(
                        f"cannot specify both `git` and `editable`; dependency={name}",
                        stacklevel=1,
                    )
                self._tool_uv_sources.append(key(name), t)
            if "path" in formatted_properties:
                t = inline_table()
                t.add("path", formatted_properties["path"])
                if "editable" in formatted_properties:
                    t.add("editable", True)  # noqa: FBT003
                self._tool_uv_sources.append(key(name), t)

    def _migrate_scripts(self) -> None:
        if "scripts" not in self._pipenv:
            return
        warnings.warn(
            "uv does not have the feature of task runner."
            " migration of the scripts section will be skipped.",
            stacklevel=2,
        )

    def _migrate_source(self) -> None:
        for s in self._pipenv.get("source", aot()):
            if s["name"] == "pypi":
                continue

            source = table()
            source.add("name", s["name"])
            source.add("url", s["url"])
            self._tool_uv_index.append(source)

    def _save(self) -> None:
        if self._option.dry_run:
            sys.stdout.write(dumps(self._pyproject))
        else:
            with Path(self._pyproject_toml).open("w") as f:
                f.write(dumps(self._pyproject))


def split_extras(name: str) -> tuple[str, str | None]:
    m = re.match(r"^(.+)\[([^\]]+)\]$", name)
    extras = None
    if m:
        name_no_extras = m.group(1)
        extras = m.group(2)
    else:
        name_no_extras = name
    return name_no_extras, extras


def reformat_dependency_properties(
    extras: str | None,
    properties: str | dict[str, Any],
) -> dict[str, Any]:
    formatted: dict[str, Any] = {}
    if extras is not None:
        formatted["extras"] = extras.split(",")
    if isinstance(properties, dict):
        formatted.update(properties)
    else:
        formatted["version"] = properties
    return formatted
