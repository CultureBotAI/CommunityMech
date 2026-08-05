"""A grounding just over 0.5 is a coin flip that landed right (#396).

#394 moved the threshold from `>=0.5` to `>0.5`, so a tie-break can no longer
*decide* a grounding. That is narrower than it sounds, and #396 was filed so the
stronger reading does not take hold: it removed the exact ties, not the near
ones. Four blocks sit at **0.50098** — 226306 against 225423, a margin of 883
genomes in 451729.

The marker is advisory. It stores nothing and withholds nothing, because there is
no natural cut point in the distribution and raising the threshold is a curation
policy call (#396 option 3, rejected there). What it does is tell a curator at
the moment of decision.

#416 is why that matters. NCBI *Nitrospiraceae* grounds to
`f__Leptospirillaceae` at 0.534 — and *Leptospirillum* is an **iron** oxidizer
while the record's genome is its **nitrite** oxidizer. The majority vote would
have assigned the wrong physiology, wearing a confidence number that looked like
a decision rather than a coin flip.
"""

from __future__ import annotations

import importlib.util
import subprocess
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).parent.parent


def _module():
    spec = importlib.util.spec_from_file_location("_gtdb", REPO / "scripts/gtdb_ground.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.mark.parametrize(
    ("fraction", "expected"),
    [
        (0.50098, True),  # the four Bacillota blocks
        (0.501, True),
        (0.534, True),  # the #416 Nitrospiraceae case
        (0.5449, True),
        (0.55, False),  # the bound is exclusive
        (0.57, False),  # g__Bacillus, the next real population up
        (1.0, False),
        # "unknown" is not "marginal". (A curated block may still carry a
        # fraction — the KB's does, at 0.5 — so this is about absence, not
        # about curation.)
        (None, False),
        ("0.5", False),
        # Booleans are ints in Python. They are excluded by the range rather
        # than by a type guard: `True` is 1 (above the bound) and `False` is 0
        # (fails `0 < fraction`). An explicit guard was dead code.
        (True, False),
        (False, False),
        (0, False),
    ],
)
def test_the_predicate_fires_only_on_a_near_tie(fraction, expected):
    assert _module()._is_near_tie(fraction) is expected


def test_the_bound_is_where_the_population_gap_is():
    """The threshold is a judgement call, so pin what justified it.

    5 blocks below 0.55, then a gap to 0.57. If the KB drifts so the marker
    covers a crowd, it stops pointing at anything and should be revisited.
    """
    fractions = sorted(
        block["majority_fraction"]
        for _, block in _grounded()
        if isinstance(block.get("majority_fraction"), (int, float))
    )
    marked = [f for f in fractions if f < _module().NEAR_TIE_BELOW]

    assert len(marked) <= 12, (
        f"{len(marked)} of {len(fractions)} groundings are now near-ties; the "
        f"marker is supposed to single out the marginal few (#396)"
    )
    assert marked, "no near-ties at all — either the KB changed or the bound is wrong"


def _grounded():
    for path in sorted((REPO / "kb/communities").glob("*.yaml")):
        for entry in (yaml.safe_load(path.read_text()) or {}).get("taxonomy") or []:
            block = (entry.get("taxon_term") or {}).get("gtdb_classification")
            if block:
                yield path.name, block


def test_the_known_near_ties_are_still_there():
    """The population #396 documents, so it cannot shrink unnoticed.

    Five blocks, and they are two different things:

    * four `p__Bacillota_A` at 0.50098 — the tool's own output, retained because
      0.50098 > 0.5. These are what #396 is about.
    * one `g__Syntrophotalea` at exactly 0.5, which the threshold would reject.
      It is in the KB because a curator pinned it against the vote (#384), and
      it carries `curated: true` saying so.

    That second one is why the *flag* stays a pure function of the fraction while
    the *judgement* does not: 0.5 really is a coin flip, and the record already
    answers "should someone look at this" with a curation note.
    """
    near = [
        (name, block["gtdb_id"], bool(block.get("curated")))
        for name, block in _grounded()
        if _module()._is_near_tie(block.get("majority_fraction"))
    ]
    uncurated = [(n, g) for n, g, curated in near if not curated]

    assert len(uncurated) >= 4, f"expected the 0.50098 Bacillota blocks, found {near}"
    assert all(gtdb_id == "GTDB:p__Bacillota_A" for _, gtdb_id in uncurated), uncurated
    # Every block at or below the strict threshold must be a deliberate override,
    # or the threshold is not being enforced.
    for name, block in _grounded():
        fraction = block.get("majority_fraction")
        if isinstance(fraction, (int, float)) and fraction <= 0.5:
            assert block.get("curated") is True, (
                f"{name}: {block['gtdb_id']} sits at {fraction} with no `curated` "
                f"flag — a non-majority grounding that nobody chose (#394)"
            )


@pytest.mark.parametrize(
    ("name", "marked"),
    [
        ("Bacillota", True),  # 0.501 -- 226306/451729
        ("Nitrospiraceae", True),  # 0.534 -- the #416 case
        ("Bacillus", False),  # 0.57 -- just above
        ("Steroidobacteraceae", False),  # 1.0
    ],
)
def test_the_cli_marks_the_right_groundings(name, marked):
    """End to end through the CLI, which is where a curator actually sees it."""
    result = subprocess.run(
        ["uv", "run", "python", "scripts/gtdb_ground.py", "--name", name],
        capture_output=True,
        text=True,
        cwd=REPO,
        timeout=900,
    )
    lines = [ln for ln in result.stdout.splitlines() if "majority" in ln]
    if not lines:
        pytest.skip(f"{name} no longer grounds; this test is stale")

    assert ("NEAR-TIE" in lines[0]) is marked, lines[0]


def test_the_marker_does_not_replace_thin():
    """Two different weaknesses; a block can have either, both, or neither.

    THIN is "too few genomes to say anything"; NEAR-TIE is "plenty of genomes,
    split down the middle". Collapsing them would hide the 0.50098 blocks, which
    have 451729 genomes and are anything but thin.
    """
    source = (REPO / "scripts/gtdb_ground.py").read_text()

    assert "⚠ THIN" in source and "⚠ NEAR-TIE" in source
    assert "{thin}{near}" in source, "both markers should be able to appear together"
