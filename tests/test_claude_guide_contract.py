"""Agent guidance must track the repository contract it describes (#666)."""

from __future__ import annotations

import re
import subprocess
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
GUIDE = REPO / "CLAUDE.md"


def _text() -> str:
    return GUIDE.read_text(encoding="utf-8")


def test_every_documented_just_recipe_exists():
    documented = set(re.findall(r"\bjust ([a-z][a-z0-9-]*)", _text()))
    result = subprocess.run(
        ["just", "--summary"], cwd=REPO, check=True, capture_output=True, text=True
    )
    available = set(result.stdout.split())

    assert documented
    assert (
        documented <= available
    ), f"CLAUDE.md names missing recipes: {sorted(documented - available)}"


def test_canonical_paths_named_by_the_guide_exist():
    required = {
        "src/communitymech/schema/communitymech.yaml",
        "src/communitymech/schema/mech_shared.yaml",
        "src/communitymech/schema/history.yaml",
        "src/communitymech/datamodel/communitymech.py",
        "src/communitymech/cli.py",
        "kb/communities",
        "data/isolates",
        "kb/taxa",
        "references_cache",
        "history",
        "src/communitymech/templates",
        "docs",
        "scripts",
    }
    assert all(f"`{path}" in _text() for path in required)
    assert not [path for path in required if not (REPO / path).exists()]


def test_stale_architecture_claims_do_not_return():
    text = _text()
    assert "cli.py                       # Entry point (not yet implemented)" not in text
    assert "lossy Koza transforms planned" not in text
    assert "`schema/communitymech.yaml`" not in text
    assert not re.search(r"kb/communities/` \(\d+ files\)", text)


def test_guide_distinguishes_policy_from_enforcement_and_names_safety_boundaries():
    text = _text()
    for phrase in (
        "a curation policy, not a blanket schema guarantee",
        "full text",
        "supplementary text",
        "append-only history",
        "CLAW_SRC",
        "Python 3.12+",
        "Never read, print, modify, or commit `.env`",
        "preserve unrelated or uncommitted user work",
        "not a Koza transform",
    ):
        assert phrase in text
