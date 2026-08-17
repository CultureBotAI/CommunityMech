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


def find_truncated_scalars(path: Path, *, require_gap: bool = False) -> list[ScalarIssue]:
    """Report plain scalars in `path` that a mid-line comment cut short.

    `require_gap` reports only comments written *tight* against the value —
    fewer than two spaces before the `#`. YAML cannot distinguish

        notes: some text #398 here        <- prose the author lost
        fetch-depth: 0  # need the merge base   <- a comment on purpose

    because both end the value at the `#`. Nothing in the document separates
    them, which is why the check was scoped to the record trees, where trailing
    comments are not an idiom and every report is therefore real (#398, #399).

    Elsewhere they are an idiom, and the one thing that does separate them is
    how they are written. Measured across `conf/`, `.github/workflows/`,
    `vocab/` and the schema: all 13 deliberate trailing comments use **three or
    more** spaces before the `#`, and none uses fewer. A `#` swallowed
    mid-sentence has one or none, because it was typed as part of the prose.

    So this is a convention check, not a proof: an author who writes
    `notes: text   #398 here` with three spaces defeats it, and one who writes
    `key: value # comment` with a single space gets a false report. It is
    offered for trees where the alternative is no checking at all (#400).
    """
    text = path.read_text()
    lines = text.splitlines()

    try:
        events = list(yaml.parse(text))
    except yaml.YAMLError:
        # An unparseable document is a different failure, already reported as
        # `yaml_parse_error` by validate-strict. Saying it twice helps nobody.
        return []

    issues: list[ScalarIssue] = []
    # PyYAML puts `flow_style` on the START events only — Sequence/MappingEnd
    # carry no such attribute, so `getattr(event, "flow_style", None) is not
    # False` (my first attempt) was always true and excluded nothing. Track it
    # from the starts instead.
    #
    # This restriction is DEFENSIVE, not load-bearing, and no test can make it
    # fail: a block collection's end_mark lands on the next *token*, so it skips
    # over comment lines entirely and can never produce a remainder starting
    # with `#`. Removing the restriction changes nothing observable today. It is
    # here so the intent is stated rather than accidental — the same reason
    # `_species_denominator` documents a rule that is currently a no-op on the
    # KB. Verified by inspection: for `k:\n  - a\nnext: 1`, the SequenceEnd
    # remainder is "next: 1"; with a trailing comment it is past EOF.
    flow_stack: list[bool] = []
    for event in events:
        if isinstance(event, (yaml.SequenceStartEvent, yaml.MappingStartEvent)):
            flow_stack.append(bool(event.flow_style))
        # Two kinds of event can have a comment eat their tail.
        #
        # A plain scalar. A quoted ('"', "'") or block ('|', '>') scalar
        # delimits itself, so a `#` inside it is literal and a `#` after it ends
        # a value that was already complete. Only `style is None` can be cut.
        #
        # And the END of a FLOW collection (#489). `key: [a, b] # comment`
        # anchors nothing useful on the last scalar: `b`'s end_mark sits before
        # the `]`, so the remainder is `] # comment`, which does not start with
        # `#`, and the line was skipped under both rules. The collection's own
        # end event carries an end_mark after the bracket, where the same
        # remainder logic works. Flow style only — a block collection ends on a
        # later line and its end_mark says nothing about this one.
        if isinstance(event, yaml.ScalarEvent) and event.style is None:
            value, is_collection = event.value, False
        elif isinstance(event, (yaml.SequenceEndEvent, yaml.MappingEndEvent)) and (
            flow_stack.pop() if flow_stack else False
        ):
            # A flag, not an empty `value`. Overloading `value = ""` here made
            # the gap rule treat every flow collection as total loss — for a
            # SCALAR an empty value means the whole thing became a comment — and
            # `deliberate_flow: [a, b]   # note` was reported. A collection that
            # ends before the `#` has its value intact; only the comment after
            # it is in question.
            value, is_collection = "", True
        else:
            continue

        end = event.end_mark
        if end.line >= len(lines):
            continue
        remainder = lines[end.line][end.column :]
        if not remainder.lstrip().startswith("#"):
            continue
        if (
            require_gap
            and (value != "" or is_collection)
            and len(remainder) - len(remainder.lstrip()) >= 2
        ):
            # Two or more spaces: written as a deliberate end-of-line comment.
            #
            # Except when the value is EMPTY. `description:  #400 all of it` is
            # total loss — the whole value became a comment — and no deliberate
            # end-of-line comment leaves its key valueless, so the ambiguity the
            # gap rule exists to resolve does not arise. This module's own
            # header calls that the worst case; relaxing it would have been the
            # one place the relaxation cost something real (review of #488).
            continue

        key = _name_for(lines, end.line)

        issues.append(
            ScalarIssue(
                file=str(path),
                line=end.line + 1,
                key=key,
                truncated_to=value.strip(),
                lost=remainder.strip(),
            )
        )
    return issues
