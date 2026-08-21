"""README commands, links, and sample data must stay executable (#665)."""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import unquote

import yaml

REPO = Path(__file__).resolve().parent.parent
README = REPO / "README.md"
SCHEMA = REPO / "src/communitymech/schema/communitymech.yaml"


def _readme_text() -> str:
    return README.read_text(encoding="utf-8")


def test_every_documented_just_recipe_exists():
    documented = set(re.findall(r"\bjust ([a-z][a-z0-9-]*)", _readme_text()))
    result = subprocess.run(
        ["just", "--summary"], cwd=REPO, check=True, capture_output=True, text=True
    )
    available = set(result.stdout.split())

    assert documented, "README contains no just commands; this test checked nothing"
    assert (
        documented <= available
    ), f"README names missing recipes: {sorted(documented - available)}"


def test_every_repository_relative_link_resolves():
    destinations = re.findall(r"\[[^]]*\]\(([^)]+)\)", _readme_text())
    missing = []
    for destination in destinations:
        if re.match(r"^[a-z][a-z0-9+.-]*://", destination, re.IGNORECASE):
            continue
        path_text = unquote(destination.split("#", 1)[0])
        if path_text and not (REPO / path_text).exists():
            missing.append(destination)

    assert not missing, f"README contains broken relative links: {missing}"


def test_schema_example_is_valid_yaml_and_linkml(tmp_path):
    match = re.search(
        r"^## Schema-valid example\b.*?^```yaml\n(?P<yaml>.*?)^```$",
        _readme_text(),
        re.MULTILINE | re.DOTALL,
    )
    assert match, "README has no YAML block under the schema-valid example heading"

    document = yaml.safe_load(match.group("yaml"))
    assert document["id"].startswith("CommunityMech:")
    assert document.get("taxonomy")
    assert document.get("ecological_interactions")

    example = tmp_path / "readme-example.yaml"
    example.write_text(match.group("yaml"), encoding="utf-8")
    validator = Path(sys.executable).with_name("linkml-validate")
    result = subprocess.run(
        [str(validator), "-s", str(SCHEMA), str(example)],
        cwd=REPO,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, result.stdout + result.stderr


def test_readme_describes_the_implemented_export_consistently():
    text = _readme_text()
    assert "custom Python KGX emitter" in text
    assert "commands above are planned" not in text.casefold()
