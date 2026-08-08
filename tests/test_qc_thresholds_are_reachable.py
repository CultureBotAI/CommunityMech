"""A QC threshold nobody can reach is a warning nobody reads (#325).

`conf/qc_config.yaml` asked for **90%** `curation_history` coverage. The corpus
has **0.6%** — 2 records of 312. That slot had been warning since it was
written and could only ever clear if somebody backfilled 310 records, which
#325 is the open question about. A gate in that state trains its readers to
skip past it, and the next slot to go genuinely wrong inherits the habit.

The distinction this file draws is between a target that is *ambitious* and one
that is *unreachable*:

* `associated_datasets` asks 0.30 and has 0.282 — six records short. That is a
  target, and leaving it short is the point of having one.
* `curation_history` asked 0.90 and had 0.006 — a factor of 150. That is not a
  target, it is a mislabelled aspiration.

So the rule is deliberately loose: a threshold may sit above current coverage,
but not so far above that no plausible amount of curation closes it. Anything
tighter would forbid aspirational targets, which are useful.

Not a claim that provenance coverage is fine. It is 2 of 312, the dashboard says
so on its face ("from 2 of 312 records"), and #325 remains open for what to do
about it — backfill, grow forward, or move provenance to the `history/` tree.
"""

from __future__ import annotations

import pathlib

import pytest
import yaml

REPO = pathlib.Path(__file__).parent.parent
CONFIG = REPO / "conf/qc_config.yaml"
RECORDS = REPO / "kb/communities"

# A threshold may exceed reality by this factor and still count as a target.
# Above it, the slot can only be cleared by a bulk backfill, which is a decision
# rather than a curation step.
REACHABLE_FACTOR = 3.0

# ...or by this absolute margin, whichever is larger. A purely multiplicative
# rule collapses on a near-empty slot: at 0.6% coverage it permits at most 1.9%,
# so the only legal non-zero target is a rounding error, and a curator who wants
# "grow curation_history to 10%" is forbidden from saying so. That would make
# this rule permit exactly the answer this PR chose and nothing else, which is
# not a rule, it is a rationalisation. The margin keeps a real growth target
# legal on a near-empty slot while still rejecting 0.90 against 0.006.
REACHABLE_MARGIN = 0.10


def _config() -> dict:
    return yaml.safe_load(CONFIG.read_text(encoding="utf-8"))


def _coverage(dotted: str) -> float:
    records = [
        document
        for document in (
            yaml.safe_load(path.read_text(encoding="utf-8"))
            for path in sorted(RECORDS.rglob("*.yaml"))
        )
        if isinstance(document, dict)
    ]
    assert records, "no community records found; this test would pass vacuously"
    hits = 0
    for record in records:
        node = record
        for part in dotted.split("."):
            node = node.get(part) if isinstance(node, dict) else None
            if node is None:
                break
        if node:
            hits += 1
    return hits / len(records)


def test_the_config_has_slots_to_check():
    assert len(_config().get("slots") or []) >= 10


@pytest.mark.parametrize("slot", _config().get("slots") or [], ids=lambda s: s.get("path", "?"))
def test_every_threshold_is_reachable(slot: dict):
    """Ambitious is fine; unreachable is not."""
    actual = _coverage(slot["path"])
    threshold = float(slot["threshold"])
    if threshold == 0.0 or actual >= threshold:
        return
    ceiling = max(actual * REACHABLE_FACTOR, actual + REACHABLE_MARGIN)
    assert threshold <= ceiling, (
        f"{slot['path']} asks for {threshold:.0%} and the corpus has "
        f"{actual:.1%} — a factor of {threshold / actual:.0f}, and above the "
        f"{ceiling:.1%} a slot at this coverage can plausibly reach. That is "
        f"not a target, it is a permanent warning. Either lower it to something "
        f"curation can close, or set it to 0.0 and say why in a comment, as "
        f"`curation_history` and `discussions` do (#325)."
    )


def test_curation_history_is_not_asserted_at_a_level_it_cannot_reach():
    """The specific slot #325 is about, pinned by name.

    Kept separate from the sweep so that raising it back to 0.90 fails with a
    message naming this issue, rather than with the generic reachability one.
    """
    slot = next(s for s in _config()["slots"] if s["path"] == "curation_history")
    actual = _coverage("curation_history")
    assert slot["threshold"] <= max(actual, 0.05), (
        f"curation_history is at {actual:.1%}; the config asks "
        f"{slot['threshold']:.0%}. Raise it when coverage is actually growing "
        f"— since #395 every gtdb_ground.py write appends an event, so a "
        f"grounding sweep moves it (#325)."
    )
