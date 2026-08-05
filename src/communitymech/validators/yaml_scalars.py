"""Catch hand-written YAML scalars that silently lose their tail (#398).

In YAML a ``#`` **preceded by whitespace** opens a comment, even mid-value. So an
unquoted scalar like::

    curation_note: rather than by decision (#376, #384).

parses as ``rather than by decision (#376,`` — the rest is a comment. The file is
valid YAML, the value is non-empty, and every schema check passes. It bit once
already: that exact line shipped, losing the pointer to the issue the field
existed for and leaving an unbalanced paren, and nothing noticed because every
check tested only that the note was non-empty (#397 review).

The hazard is general rather than specific to one field. `notes`, `curation_note`
and evidence `snippet` are all prose a curator types by hand, and all routinely
reference issues and PRs by ``#number``.

Two things make this hard to catch after the fact:

* Re-serializing does not reveal it. PyYAML emits the *truncated* value as
  perfectly good YAML, so a load/dump round-trip compares equal to itself. The
  check has to read the raw line.
* ``#`` is legitimate in three places — a whole-line comment, anywhere inside a
  quoted scalar, and anywhere inside a block scalar (``>`` or ``|``), where it is
  literal. Flagging those would make the rule unusable.

So this reports only an **unquoted plain scalar containing a space-hash**, which
is exactly the case that loses data.

A whole-line comment needs no explicit guard: it cannot match the ``key: value``
patterns, which require a letter or underscore first.

Usage::

    from communitymech.validators.yaml_scalars import find_truncated_scalars

    for issue in find_truncated_scalars(Path("kb/communities/Foo.yaml")):
        print(issue.line, issue.message)
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

# `key: value` or `- key: value`, capturing the indent, the key and the value.
_MAPPING = re.compile(r"^(?P<indent>\s*)(?:-\s+)?(?P<key>[A-Za-z_][\w.\-]*):\s(?P<value>\S.*)$")
# A bare sequence item: `- some text`.
_SEQUENCE = re.compile(r"^(?P<indent>\s*)-\s(?P<value>\S.*)$")
# A block scalar header: `key: >`, `key: |-`, `key: >2`, etc.
_BLOCK_HEADER = re.compile(r"^(?P<indent>\s*)(?:-\s+)?[A-Za-z_][\w.\-]*:\s*[|>][+\-0-9]*\s*$")
# The defect: whitespace then `#`. A `#` with no space before it — `(#376` — is
# part of the scalar and safe.
_SPACE_HASH = re.compile(r"\s#")


@dataclass(frozen=True)
class ScalarIssue:
    """One line whose value will lose its tail."""

    file: str
    line: int
    key: str
    truncated_to: str
    lost: str

    @property
    def message(self) -> str:
        return (
            f"unquoted `{self.key}` is cut short by a mid-scalar comment: keeps "
            f"{self.truncated_to!r}, loses {self.lost!r}. Quote the value."
        )

    def __str__(self) -> str:  # pragma: no cover - display only
        return f"{self.file}:{self.line}: {self.message}"


def _is_quoted(value: str) -> bool:
    """Is the value a quoted scalar, so a `#` inside it is literal?"""
    stripped = value.strip()
    return len(stripped) >= 2 and stripped[0] in "\"'" and stripped[-1] == stripped[0]


def find_truncated_scalars(path: Path) -> list[ScalarIssue]:
    """Report unquoted scalars in `path` that a mid-line comment will truncate."""
    issues: list[ScalarIssue] = []
    block_indent: int | None = None

    for number, line in enumerate(path.read_text().splitlines(), start=1):
        indent = len(line) - len(line.lstrip())

        # Inside a block scalar every line is literal, including `#`. The block
        # ends at the first non-blank line indented no deeper than its header.
        if block_indent is not None:
            if not line.strip() or indent > block_indent:
                continue
            block_indent = None

        if _BLOCK_HEADER.match(line):
            block_indent = indent
            continue
        match = _MAPPING.match(line) or _SEQUENCE.match(line)
        if not match:
            continue
        value = match.group("value")
        if _is_quoted(value):
            continue
        hit = _SPACE_HASH.search(value)
        if not hit:
            continue
        issues.append(
            ScalarIssue(
                file=str(path),
                line=number,
                key=match.groupdict().get("key") or "-",
                truncated_to=value[: hit.start()].rstrip(),
                lost=value[hit.start() :].strip(),
            )
        )
    return issues
