"""`/goal` prompts must fit the harness's input budget.

`/goal` truncates past roughly 4000, and a truncated prompt fails in the worst
way available: silently, losing whatever sat at the end. In
`prompts/backlog-loop.goal.md` the tail is the Gotchas section, so the material
most likely to be lost is the accumulated list of things that have already gone
wrong once.

Nothing enforced this. The file was maintained by hand against a remembered
number and reached **2 characters** of headroom before this test existed (#358).

``LIMIT`` itself is that remembered number: no measurement of the real ceiling
exists anywhere in the repo, only `CLAUDE.md`'s assertion of it. Worth pinning to
a measured value.

**Characters or bytes is unresolved** (#358), so this enforces the stricter of
the two: bytes. Be clear about what that means — UTF-8 uses at least one byte per
code point, so ``bytes <= LIMIT`` *implies* ``chars <= LIMIT``. The character
assertion below can never fail on its own; it is kept only because it fires first
and says "characters" when a plain-ASCII edit runs long, which is the common case
and the clearer message.

The distinction is not academic. The prose is em-dash heavy at 3 bytes per
character, and the file exceeded 4000 *bytes* in two of its three revisions while
never exceeding 4000 characters —

    2429a7a  3987 chars  4015 bytes
    5a1d60b  3998 chars  4028 bytes
    9f9ba22  3944 chars  3974 bytes

So this is not a free hedge: it costs real budget. The file carried 15 non-ASCII
characters costing 30 bytes, against 10 bytes of headroom — the hedge was
spending three times what was left. They are ASCII now, and the headroom went
from 10 bytes to 39. `test_goal_prompts_are_ascii_only` keeps it that way, so
the byte and character counts stay equal and the unresolved unit stops mattering
for this file (#363).
"""

from pathlib import Path

import pytest

REPO = Path(__file__).parent.parent
PROMPTS = REPO / "prompts"

# The `/goal` input budget. Applied to both units, since which one the harness
# counts is unknown — see the module docstring.
LIMIT = 4000


def _goal_prompts() -> list:
    return sorted(PROMPTS.glob("*.goal.md"))


def test_there_is_something_to_check():
    """A glob that matches nothing passes every parametrised test vacuously."""
    assert PROMPTS.is_dir(), f"{PROMPTS} does not exist"
    assert _goal_prompts(), f"no *.goal.md found in {PROMPTS}"


@pytest.mark.parametrize("path", _goal_prompts(), ids=lambda p: p.name)
def test_goal_prompt_fits_the_budget_in_both_units(path: Path):
    raw = path.read_bytes()
    text = raw.decode("utf-8")
    chars, byte_count = len(text), len(raw)

    # Implied by the byte assertion below, never independently reachable; kept
    # for the clearer message on a plain-ASCII overrun. See the module docstring.
    assert chars <= LIMIT, (
        f"{path.name} is {chars} characters, {chars - LIMIT} over the {LIMIT} limit. "
        f"Cut prose rather than dropping a gotcha or a loop step."
    )
    assert byte_count <= LIMIT, (
        f"{path.name} is {byte_count} bytes ({chars} characters), {byte_count - LIMIT} "
        f"over the {LIMIT} limit. Non-ASCII punctuation costs extra bytes — em dashes "
        f"and arrows are the usual culprits here."
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
    costs this file nothing either way — and an em-dash was costing 2 bytes
    apiece against 10 bytes of headroom.
    """
    text = path.read_text()
    offenders = sorted({c for c in text if ord(c) > 127})
    assert not offenders, (
        f"{path.name} contains non-ASCII characters {offenders}, which cost extra "
        f"bytes against the /goal budget for no gain — use ASCII punctuation (#363)"
    )
