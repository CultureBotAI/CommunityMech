"""`/goal` prompts must fit the harness's input budget, which is now measured.

**4000 characters, on the trimmed string, rejected rather than truncated.**
From Claude Code 2.1.220 — the handler is in the installed binary at
`~/.local/share/claude/versions/2.1.220`:

    let n = r.trim();
    ...
    if (n.length > Ydr) return Ne("goal_set","too_long"),
      e(`Goal condition is limited to ${Ydr} characters (got ${n.length})`, ...)

with `Ydr=4000` as the unique binding of that name. Re-derive it the same way if
the version moves; a grep for `Goal condition is limited to` finds the call
sites and the constant is one identifier away.

Two things this file used to assert are wrong, and both mattered (#363):

* **It said `/goal` truncates, silently, losing whatever sat at the end.** It
  does not. It rejects the whole prompt with `Goal condition is limited to 4000
  characters (got N)` and sets no goal. Loud, not silent — which is a much
  better failure than the one this module was written to prevent.
* **It enforced bytes**, calling that "the stricter reading while the unit is
  unknown". The unit is characters. Bytes is not a conservative hedge on the
  same axis; it is the wrong axis, and it would have rejected a legal prompt
  that used non-ASCII punctuation.

The canonical `prompts/backlog-loop-goal.md` is guarded below and by the
vendored fleet frontmatter test.

`test_goal_prompts_are_ascii_only` stays, for a narrower reason than before: JS
`.length` counts UTF-16 code units, so an astral character (emoji, some
mathematical symbols) costs **2** where Python's `len()` counts 1. ASCII keeps
Python's count an exact proxy for the harness's. The file has no astral
characters today.

The history the old docstring cited is still true and still the reason the
character/byte distinction was ever confusing — the prose was em-dash heavy at
3 bytes per character, and exceeded 4000 *bytes* in two early revisions while
never exceeding 4000 characters:

    2429a7a  3987 chars  4015 bytes
    5a1d60b  3998 chars  4028 bytes
    9f9ba22  3944 chars  3974 bytes

Under the measured rule none of those was ever over budget.
"""

import re
from pathlib import Path

import pytest

REPO = Path(__file__).parent.parent
PROMPTS = REPO / "prompts"

# Measured, not remembered: `Ydr=4000` in Claude Code 2.1.220, compared against
# `r.trim().length`. See the module docstring for how to re-derive it.
LIMIT = 4000
LIMIT_UNIT = "characters"


def _goal_prompts() -> list:
    path = PROMPTS / "backlog-loop-goal.md"
    return [path] if path.is_file() else []


def test_there_is_something_to_check():
    """A glob that matches nothing passes every parametrised test vacuously."""
    assert PROMPTS.is_dir(), f"{PROMPTS} does not exist"
    assert _goal_prompts(), f"no backlog-loop-goal.md found in {PROMPTS}"


@pytest.mark.parametrize("path", _goal_prompts(), ids=lambda p: p.name)
def test_goal_prompt_fits_the_measured_budget(path: Path):
    """Trimmed characters, because that is what the handler compares.

    `/goal` does `r.trim()` first, so a trailing newline is free.
    """
    text = path.read_text(encoding="utf-8")
    trimmed = len(text.strip())

    assert trimmed <= LIMIT, (
        f"{path.name} is {trimmed} {LIMIT_UNIT} once trimmed, {trimmed - LIMIT} "
        f"over the {LIMIT} limit. `/goal` will refuse it outright — 'Goal "
        f"condition is limited to {LIMIT} characters (got {trimmed})' — and set "
        f"no goal. Cut prose rather than dropping a gotcha or a loop step."
    )


@pytest.mark.parametrize("path", _goal_prompts(), ids=lambda p: p.name)
def test_python_len_is_a_valid_proxy_for_the_harness_count(path: Path):
    """JS `.length` counts UTF-16 code units; Python's `len` counts code points.

    They agree for everything in the Basic Multilingual Plane and diverge on
    astral characters — an emoji is 1 to Python and 2 to `/goal`. So a file full
    of emoji could pass this suite and still be refused. ASCII-only (enforced
    below) makes the two counts identical; this asserts the property directly
    rather than relying on that.
    """
    text = path.read_text(encoding="utf-8")
    utf16_units = len(text.strip().encode("utf-16-le")) // 2
    assert utf16_units == len(text.strip()), (
        f"{path.name} contains astral characters, which `/goal` counts as two "
        f"each: Python sees {len(text.strip())}, the harness sees {utf16_units}"
    )


@pytest.mark.parametrize("path", _goal_prompts(), ids=lambda p: p.name)
def test_goal_prompt_is_valid_utf8_and_not_empty(path: Path):
    """A prompt that cannot be decoded, or is blank, would pass the size check."""
    raw = path.read_bytes()
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError as exc:  # pragma: no cover - would be a real defect
        pytest.fail(f"{path.name} is not valid UTF-8: {exc}")
    assert text.strip(), f"{path.name} is empty"


@pytest.mark.parametrize("path", _goal_prompts(), ids=lambda p: p.name)
def test_goal_prompts_are_ascii_only(path):
    """Non-ASCII punctuation costs budget for nothing.

    While the unit is unresolved the test enforces bytes, the stricter reading.
    Keeping these files ASCII makes bytes and characters equal, so the ambiguity
    costs this file nothing either way - and each em-dash was 3 bytes where a
    hyphen is 1, so 15 of them spent 30 bytes against 10 bytes of headroom.
    """
    text = path.read_bytes().decode("utf-8")
    offenders = sorted({c for c in text if ord(c) > 127})
    assert not offenders, (
        f"{path.name} contains non-ASCII characters {offenders}, which cost extra "
        f"bytes against the /goal budget for no gain — use ASCII punctuation (#363)"
    )


# ---------------------------------------------------------------------------
# The number and its unit live in two places: `LIMIT` here and the prose in
# CLAUDE.md. Nothing checked that they agreed, and #363 was filed because they
# did not — CLAUDE.md documented a *character* limit while this file enforced
# *bytes*. They agree now; these keep them agreeing.
#
# This is the repo's recurring defect: documentation asserting one thing while
# code enforces another, with no gate between them. CLAUDE.md is loaded as
# authoritative context every session, so a stale claim there misdirects every
# reader (#460).
# ---------------------------------------------------------------------------

CLAUDE_MD = REPO / "CLAUDE.md"

# Anchored to the /goal sentence, not to the first "Kept under N" anywhere in
# the file: an unrelated budget line ("Commit summaries: Kept under 72 chars")
# hijacked both assertions and reported a 72-character /goal limit. Tolerant of
# `*chars*`, `**chars**`, backticks and a thousands comma, because a reworded
# doc should fail the *number* test loudly, not this regex quietly (#363 review).
_DOCUMENTED = re.compile(
    r"Kept under[^\n]*?([\d,]+)\s*[*`]{0,2}(bytes|chars|characters)[*`]{0,2}[^\n]*for /goal",
    re.IGNORECASE,
)


def _documented_limit() -> tuple[int, str]:
    """(number, unit) as CLAUDE.md states them for /goal."""
    match = _DOCUMENTED.search(CLAUDE_MD.read_text(encoding="utf-8"))
    assert match, (
        "CLAUDE.md no longer states the /goal budget in a form this test can "
        "read ('Kept under N <unit> ... for /goal'). Update the prose and this "
        "regex together (#363)."
    )
    return int(match.group(1).replace(",", "")), (
        "characters" if match.group(2).lower().startswith("char") else "bytes"
    )


def test_claude_md_and_this_test_agree_on_the_number():
    documented, _ = _documented_limit()
    assert documented == LIMIT, (
        f"CLAUDE.md documents a {documented} /goal budget; this test enforces "
        f"{LIMIT}, which is measured (Ydr=4000). Reconcile them (#363)."
    )


def test_claude_md_and_this_test_agree_on_the_unit():
    """The disagreement #363 was filed for, now settled by measurement.

    It was filed as "CLAUDE.md says chars, the test says bytes". The answer is
    that CLAUDE.md was right: `/goal` compares `r.trim().length`. The guard
    enforced bytes on the theory that it was the stricter reading — but bytes is
    a different axis, not a safer one, and it would have rejected a legal prompt
    for using an em dash.
    """
    _, unit = _documented_limit()
    assert unit == LIMIT_UNIT, (
        f"CLAUDE.md documents the /goal budget in {unit}; the harness counts "
        f"{LIMIT_UNIT} (`r.trim().length`). Reconcile them (#363)."
    )


def test_claude_md_says_the_limit_rejects_rather_than_truncates():
    """It rejects; it does not truncate.

    Both this module and CLAUDE.md described silent truncation, which is the
    scarier failure and the one that justified the guard. The real behaviour is
    a refusal naming the overage. Keeping the wrong story would have the next
    reader budget for a partial prompt that never happens.

    Asserted positively — the docs must *say* "rejects". The first version
    checked that the word "truncat" was absent near the budget line, and failed
    on the corrected prose itself, which reads "rejects ... rather than
    truncating it". A substring scan cannot tell a claim from its negation; this
    is the third time that has bitten in this repo (#471's curation note, #487's
    module docstring).
    """
    text = CLAUDE_MD.read_text(encoding="utf-8")
    anchor = text.find("for /goal")
    assert anchor != -1, "the /goal budget line has moved; update this test (#363)"
    window = text[max(0, anchor - 400) : anchor + 400]
    assert "reject" in window.lower(), (
        "CLAUDE.md no longer says the /goal limit *rejects* an over-long "
        "condition. It does not truncate, and describing it as truncation is "
        "what #363 inherited (#363)."
    )
