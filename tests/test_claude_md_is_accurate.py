"""CLAUDE.md is loaded as authoritative context, and nothing checked it (#460).

Every session starts with this file in context, described as instructions that
override default behaviour. It had drifted in two ways at once, both found by
accident while working #410:

* its architecture tree named `validators/reference_validator.py` as the sole
  occupant of that directory. That file was deleted in **4dd299a**, "Replace
  custom validators with official LinkML validators" — only an untracked
  `.pyc` survives, so a naive `find` appears to succeed. Meanwhile the seven
  validators that *are* there, and that the CI gate runs, went undocumented.
* it said `kb/communities/` holds **60** files. It holds 312.

Neither is exotic: a doc nobody executes drifts from a tree that changes weekly.
The fix is to execute it. This parses the tree — tracking parents, since it is
nested and a bare `cli.py` means `src/communitymech/cli.py` — and asserts every
path is real, then checks the counts the prose quotes.

Kept deliberately narrow. It checks facts that are mechanically checkable and
says nothing about whether the prose is *good*, which no test can.
"""

from __future__ import annotations

import re
from pathlib import Path

import pytest

REPO = Path(__file__).parent.parent
CLAUDE_MD = REPO / "CLAUDE.md"

# `├── name` / `└── name`, and the bare `parent/` lines they hang from.
_CHILD = re.compile(r"^[│\s]*[├└]──\s+(\S+)")
_ROOT = re.compile(r"^([A-Za-z][A-Za-z0-9_./-]*/)\s*(?:#.*)?$")


def _tree_block() -> str:
    text = CLAUDE_MD.read_text()
    start = text.index("## Architecture")
    fence = text.index("```", start)
    return text[fence + 3 : text.index("```", fence + 3)]


def _declared_paths() -> list[str]:
    """Reconstruct full paths from the nested tree."""
    paths, parent = [], ""
    for line in _tree_block().split("\n"):
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        root = _ROOT.match(line.strip())
        if root:
            parent = root.group(1)
            paths.append(parent)
            continue
        child = _CHILD.match(line)
        if not child:
            continue
        name = child.group(1)
        # A parenthetical or prose aside, not a path.
        if name.startswith("(") or name.endswith(","):
            continue
        paths.append(parent + name if not name.startswith(("kb/", "src/")) else name)
    return paths


def test_the_tree_is_parseable():
    """Guard the parser, so a reformat cannot silently empty the next test."""
    declared = _declared_paths()
    assert len(declared) >= 10, f"parsed only {len(declared)} paths; has the tree been reformatted?"
    assert any(p.endswith(".py") for p in declared)
    assert any(p.endswith("/") for p in declared)


@pytest.mark.parametrize("declared", _declared_paths())
def test_every_path_named_in_the_architecture_tree_exists(declared: str):
    assert (REPO / declared).exists(), (
        f"CLAUDE.md's architecture tree names {declared!r}, which is not in the "
        f"repo. This file is loaded as authoritative context every session, so a "
        f"stale entry misdirects every reader — `validators/reference_validator.py` "
        f"outlived its deletion in 4dd299a by many months this way (#460)."
    )


def test_the_community_record_count_is_current():
    """The prose quotes a count, and counts rot faster than paths."""
    text = CLAUDE_MD.read_text()
    match = re.search(r"kb/communities/[^.]*?\((\d+) files\)", text)
    assert match, "the 'kb/communities/ (N files)' claim has moved; update this test"

    claimed = int(match.group(1))
    actual = len(list((REPO / "kb/communities").glob("*.yaml")))
    assert claimed == actual, (
        f"CLAUDE.md says kb/communities/ holds {claimed} files; it holds {actual}. "
        f"It said 60 for long enough to be off by a factor of five (#460)."
    )
