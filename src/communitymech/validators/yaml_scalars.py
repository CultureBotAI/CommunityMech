"""Catch YAML scalars that a mid-line ``#`` silently truncates (#398).

In YAML a ``#`` preceded by whitespace opens a comment, even mid-value. So::

    curation_note: rather than by decision (#376, #384).

parses as ``rather than by decision (#376,``. The file stays valid, the value
stays non-empty, and every schema check passes. That exact line shipped in #397.

Re-serializing cannot reveal it — PyYAML emits the *truncated* value as good
YAML, so a load/dump round-trip compares equal to itself.

**This asks PyYAML where each scalar actually ends** rather than pattern-matching
lines. The first version hand-rolled the lexing and was wrong in both directions
(#399 review):

* it missed a value that *begins* with ``#`` (``notes: #398 why``), which parses
  as ``null`` — total loss, and the same ``#issue`` idiom this check exists for;
* it inspected only the first line of a plain scalar, and 5333 of the KB's
  scalars span several lines, so most prose was checked only where it started;
* it reported every deliberate trailing comment as data loss — 13 in this repo's
  ``conf/`` and ``.github/`` — because it judged quoting by whether the raw value
  happened to start and end with a quote, rather than by where the ``#`` sat.

Scalar *style* answers all of that for free. A quoted or block scalar carries its
own delimiters, so a ``#`` inside it is literal and a ``#`` after it cannot have
eaten anything the author wrote. Only a **plain** scalar can be cut short, and
PyYAML reports precisely where it stopped.

A trailing comment on a plain scalar stays reportable, because nothing can
distinguish "I meant a comment" from "I lost my tail" — the message says to quote
the value, which resolves it either way. The record trees contain none today.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

import yaml

# Only to name the field in the message; detection never relies on it.
_KEY = re.compile(r"^\s*(?:-\s+)?(?P<key>[^\s:#][^:#]*):\s")


def _name_for(lines: list[str], number: int) -> str:
    """The field name to quote in the message.

    A scalar's own line usually carries its key. A sequence item does not, so
    walk out to the enclosing key — the one at a *smaller* indent. Scanning
    backwards for any `key:` instead attributed eleven list items in
    `conf/id_label_targets.yaml` to whichever key happened to precede them.
    """
    own = _KEY.match(lines[number])
    if own:
        return own.group("key").strip()

    indent = len(lines[number]) - len(lines[number].lstrip())
    # A block sequence may sit at the same indent as its key (`items:` then
    # `- one`), so an entry accepts an equal indent while a wrapped scalar
    # requires a strictly smaller one.
    limit = indent if lines[number].lstrip().startswith("- ") else indent - 1
    for candidate in range(number - 1, -1, -1):
        line = lines[candidate]
        if not line.strip():
            continue
        if len(line) - len(line.lstrip()) <= limit:
            found = _KEY.match(line) or re.match(r"^\s*(?P<key>[^\s:#][^:#]*):\s*$", line)
            if found:
                return found.group("key").strip()
    return "-"


@dataclass(frozen=True)
class ScalarIssue:
    """One scalar whose value stops short because a comment opened mid-line."""

    file: str
    line: int
    key: str
    truncated_to: str
    lost: str

    @property
    def message(self) -> str:
        kept = f"keeps {self.truncated_to!r}, " if self.truncated_to else "keeps nothing — "
        return (
            f"plain scalar `{self.key}` is cut short by a mid-line comment: "
            f"{kept}loses {self.lost!r}. Quote the value (or move the comment to "
            f"its own line if it was meant as one)."
        )

    def __str__(self) -> str:  # pragma: no cover - display only
        return f"{self.file}:{self.line}: {self.message}"


def find_truncated_scalars(path: Path) -> list[ScalarIssue]:
    """Report plain scalars in `path` that a mid-line comment cut short."""
    text = path.read_text()
    lines = text.splitlines()

    try:
        events = list(yaml.parse(text))
    except yaml.YAMLError:
        # An unparseable document is a different failure, already reported as
        # `yaml_parse_error` by validate-strict. Saying it twice helps nobody.
        return []

    issues: list[ScalarIssue] = []
    for event in events:
        # A quoted scalar ('"', "'") or a block scalar ('|', '>') delimits itself,
        # so a `#` inside it is literal and a `#` after it ends a value that was
        # already complete. Only `style is None` — a plain scalar — can be cut.
        if not isinstance(event, yaml.ScalarEvent) or event.style is not None:
            continue

        end = event.end_mark
        if end.line >= len(lines):
            continue
        remainder = lines[end.line][end.column :]
        if not remainder.lstrip().startswith("#"):
            continue

        key = _name_for(lines, end.line)

        issues.append(
            ScalarIssue(
                file=str(path),
                line=end.line + 1,
                key=key,
                truncated_to=event.value.strip(),
                lost=remainder.strip(),
            )
        )
    return issues
