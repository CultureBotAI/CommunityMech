"""`just install` must agree with how pyproject declares its dev dependencies.

uv has two separate mechanisms, and the flags are not interchangeable:

* ``[project.optional-dependencies]`` — installed with ``--extra NAME``
* ``[dependency-groups]``            — installed with ``--group NAME``

The recipe passed ``--group dev`` while the deps were declared as an extra, so
``just install`` — the setup command CLAUDE.md and the README both point new
contributors at — failed outright with *"Group `dev` is not defined in the
project's dependency-groups table"* (#290). Nothing caught it because no CI
workflow runs ``just install``; they all call ``uv sync`` directly.

This pins the *pairing* rather than the flag, so moving the deps to a
``[dependency-groups]`` table later is fine — the test then requires ``--group``.

`tomllib` is 3.11+ and CI runs 3.10, with no `tomli` in the tree, so the little
parser below stands in. Where `tomllib` does exist it is used to check the parser
agrees, so the shortcut cannot drift unnoticed.
"""

import re
from pathlib import Path

import pytest

REPO = Path(__file__).parent.parent
JUSTFILE = REPO / "justfile"
PYPROJECT = REPO / "pyproject.toml"


def _array_keys(text: str, section: str) -> set:
    """Names of the array-valued keys declared directly under ``[section]``."""
    match = re.search(rf"^\[{re.escape(section)}\]\n(.*?)(?=^\[|\Z)", text, re.M | re.S)
    if not match:
        return set()
    return set(re.findall(r"^([A-Za-z0-9_.-]+)\s*=\s*\[", match.group(1), re.M))


def _array_values(text: str, section: str, key: str) -> list:
    """The string entries of ``[section] key = [...]``."""
    match = re.search(rf"^\[{re.escape(section)}\]\n(.*?)(?=^\[|\Z)", text, re.M | re.S)
    if not match:
        return []
    body = re.search(rf"^{re.escape(key)}\s*=\s*\[(.*?)^\]", match.group(1), re.M | re.S)
    if not body:
        return []
    # Match on the outer delimiter only. A naive [\"'] character class split
    # `"deep-research-client[cyberian]>=0.2.4; python_version >= '3.12'"` at its
    # inner quotes — caught by the tomllib cross-check below.
    entries = re.findall(r'"((?:[^"\\]|\\.)*)"', body.group(1))
    return entries or re.findall(r"'((?:[^'\\]|\\.)*)'", body.group(1))


@pytest.fixture(scope="module")
def pyproject_text() -> str:
    return PYPROJECT.read_text()


@pytest.fixture(scope="module")
def install_recipe() -> str:
    """The body of the `install` recipe."""
    match = re.search(r"^install:\n((?:[ \t]+.*\n)+)", JUSTFILE.read_text(), re.M)
    assert match, "no `install:` recipe found in the justfile"
    return match.group(1)


def test_install_uses_the_flag_matching_how_dev_deps_are_declared(pyproject_text, install_recipe):
    extras = _array_keys(pyproject_text, "project.optional-dependencies")
    groups = _array_keys(pyproject_text, "dependency-groups")

    assert "dev" in extras or "dev" in groups, "pyproject declares no dev dependencies at all"
    assert not ("dev" in extras and "dev" in groups), (
        "dev is declared both as an extra and as a dependency group; "
        "the install recipe cannot be right for both"
    )

    if "dev" in extras:
        assert "--extra dev" in install_recipe, (
            "pyproject declares dev under [project.optional-dependencies], so the "
            f"install recipe must use `--extra dev`, not:\n{install_recipe}"
        )
        assert "--group dev" not in install_recipe, "`--group dev` cannot install an extra"
    else:
        assert "--group dev" in install_recipe, (
            "pyproject declares dev under [dependency-groups], so the install "
            f"recipe must use `--group dev`, not:\n{install_recipe}"
        )
        assert "--extra dev" not in install_recipe, "`--extra dev` cannot install a group"


def test_install_actually_installs_the_dev_tools(pyproject_text):
    """The recipe is only useful if `dev` carries what the docs then tell you to run.

    CLAUDE.md points a new contributor at `just install` and then `just qc`,
    which runs black, ruff, mypy and pytest.
    """
    declared = _array_values(
        pyproject_text, "project.optional-dependencies", "dev"
    ) or _array_values(pyproject_text, "dependency-groups", "dev")
    names = {re.split(r"[><=\[;]", spec, maxsplit=1)[0].strip() for spec in declared}

    for tool in ("pytest", "black", "ruff", "mypy"):
        assert tool in names, f"`just qc` runs {tool}, but dev does not declare it"


def test_the_shortcut_parser_agrees_with_a_real_toml_parser(pyproject_text):
    """Guard the stand-in. Runs only where `tomllib` exists (3.11+), skips on CI's 3.10."""
    tomllib = pytest.importorskip("tomllib")
    parsed = tomllib.loads(pyproject_text)

    assert _array_keys(pyproject_text, "project.optional-dependencies") == set(
        parsed.get("project", {}).get("optional-dependencies", {})
    )
    assert _array_keys(pyproject_text, "dependency-groups") == set(
        parsed.get("dependency-groups", {})
    )
    assert (
        _array_values(pyproject_text, "project.optional-dependencies", "dev")
        == parsed["project"]["optional-dependencies"]["dev"]
    )
