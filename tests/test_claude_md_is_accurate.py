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

# Three line shapes carry a path. A nested child (`├── name`) hangs off the
# most recent bare directory; a bare directory (`src/communitymech/`) is both a
# path and a parent; and a top-level entry (`NEXT_TASKS.md`, `conf/oak_config.yaml`)
# is neither. Missing that third shape is how the first version of this test
# checked 12 of 15 paths and stayed green while CLAUDE.md named two files that
# did not exist — including NEXT_TASKS.md, which the same doc calls the backlog
# source of truth.
_CHILD = re.compile(r"^[│\s]*[├└]──\s+(\S+)")
_ROOT = re.compile(r"^([A-Za-z][A-Za-z0-9_./-]*/)\s*(?:#.*)?$")
_TOP_FILE = re.compile(r"^([A-Za-z][A-Za-z0-9_./-]*\.[A-Za-z0-9]+)\s*(?:#.*)?$")
# A continuation of the previous entry's comment, carrying no path of its own.
_COMMENT_ONLY = re.compile(r"^[│\s]*#")


def _tree_block() -> str:
    text = CLAUDE_MD.read_text()
    start = text.index("## Architecture")
    fence = text.index("```", start)
    return text[fence + 3 : text.index("```", fence + 3)]


def _parse_tree() -> tuple[list[str], list[str]]:
    """(paths declared, lines the parser could not account for).

    Returning the leftovers is the point: a lower bound on the path count
    cannot tell "the tree shrank" from "the parser went blind", but a line it
    failed to classify can.
    """
    paths: list[str] = []
    unconsumed: list[str] = []
    parent = ""
    for line in _tree_block().split("\n"):
        if not line.strip() or _COMMENT_ONLY.match(line):
            continue
        root = _ROOT.match(line.strip())
        if root:
            parent = root.group(1)
            paths.append(parent)
            continue
        top = _TOP_FILE.match(line.strip())
        if top:
            paths.append(top.group(1))
            continue
        child = _CHILD.match(line)
        if child:
            name = child.group(1)
            # A parenthetical aside rather than a filename.
            if name.startswith("("):
                continue
            # A child is relative to its parent — that is what the tree means.
            # An earlier version had a ternary trying to special-case rooted
            # names; it hardcoded two directory prefixes, was unreachable for
            # the current tree, and got these wrong when it did fire.
            paths.append(parent + name)
            continue
        unconsumed.append(line)
    return paths, unconsumed


def _declared_paths() -> list[str]:
    return _parse_tree()[0]


def test_the_parser_reads_every_line_of_the_tree():
    """The guard that matters: no line goes unclassified.

    A floor on the path count cannot distinguish a tree that shrank from a
    parser that went blind — the first version asserted `>= 10` and reported
    healthy at 12 while three entries were never checked at all.
    """
    declared, unconsumed = _parse_tree()
    assert unconsumed == [], (
        "these lines of the architecture tree were not recognised as a path, a "
        "directory, or a comment, so nothing checked them:\n" + "\n".join(unconsumed)
    )
    assert any(p.endswith(".py") for p in declared)
    assert any(p.endswith("/") for p in declared)
    assert any(
        p.endswith(".md") for p in declared
    ), "the top-level file entries are the shape the first parser missed"


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


def test_the_python_target_matches_pyproject():
    """Another checkable number that had drifted.

    CLAUDE.md said "Python 3.9+ target" while pyproject requires >=3.10, and
    black/ruff/mypy are all configured for 3.10. A PR premised on executing this
    file's checkable facts should not leave one wrong.
    """
    claimed = re.search(r"Python (\d+\.\d+)\+ target", CLAUDE_MD.read_text())
    assert claimed, "the 'Python N.N+ target' line has moved; update this test"

    pyproject = (REPO / "pyproject.toml").read_text()
    required = re.search(r'requires-python\s*=\s*">=(\d+\.\d+)"', pyproject)
    assert required, "could not read requires-python from pyproject.toml"

    assert claimed.group(1) == required.group(1), (
        f"CLAUDE.md targets Python {claimed.group(1)}+, pyproject requires "
        f">={required.group(1)}"
    )
