"""Mechanically check the repository facts declared in CLAUDE.md (#460, #666).

The guide is authoritative agent context, so paths and version claims should be
executable facts. Volatile corpus counts are deliberately forbidden rather than
continuously updated.
"""

from __future__ import annotations

import re
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
CLAUDE_MD = REPO / "CLAUDE.md"


def _text() -> str:
    return CLAUDE_MD.read_text(encoding="utf-8")


def _canonical_table_paths() -> list[str]:
    text = _text()
    start = text.index("## Canonical and generated files")
    end = text.index("\n## ", start + 3)
    section = text[start:end]
    paths = re.findall(r"^\| `([^`]+)` \|", section, re.MULTILINE)
    assert paths, "the canonical-files table moved or became unparsable"
    return paths


@pytest.mark.parametrize("declared", _canonical_table_paths())
def test_every_path_in_the_canonical_files_table_exists(declared: str):
    assert (
        REPO / declared
    ).exists(), f"CLAUDE.md names {declared!r}, which does not exist in the repository"


def test_the_core_python_target_matches_pyproject():
    claimed = re.search(r"Core package and validation: Python (\d+\.\d+)\+", _text())
    assert claimed, "the core Python support statement moved or disappeared"

    pyproject = (REPO / "pyproject.toml").read_text(encoding="utf-8")
    required = re.search(r'requires-python\s*=\s*">=(\d+\.\d+)"', pyproject)
    assert required, "could not read requires-python from pyproject.toml"
    assert claimed.group(1) == required.group(1)


def test_the_guide_does_not_publish_a_volatile_community_count():
    assert not re.search(r"kb/communities/[^.]*?\(\d+ files\)", _text())


def test_generated_datamodel_is_named_and_protected():
    text = _text()
    assert "`src/communitymech/datamodel/communitymech.py`" in text
    assert "Never hand-edit" in text
    assert "`just gen-python`" in text
