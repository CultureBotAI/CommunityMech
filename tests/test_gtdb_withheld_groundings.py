"""Keep deliberately-withheld GTDB groundings withheld (#292, #293).

Two taxa carry an ``NCBITaxon`` id belonging to a different organism, so the GTDB
classification derived from that id describes the wrong species. Restating a wrong
grounding in a second, independently-derived-looking field makes it harder to
spot, not easier, so those two entries are left ungrounded until the ids are
fixed.

``gtdb_ground.py --apply`` has no memory of that decision: it is otherwise
perfectly idempotent, but a re-run over the whole KB re-adds exactly these two
blocks. Without this test the withhold lasts only until the next person runs the
tool and commits, and nothing anywhere fails.

Removing an entry from ``WITHHELD`` is part of fixing #292 — correct the id, then
re-run ``--apply`` and the right block appears on its own.
"""

from __future__ import annotations

from pathlib import Path

import pytest
import yaml

COMMUNITIES = Path(__file__).parent.parent / "kb/communities"

# (record, preferred_term) -> why the id is wrong. Tracked in #292.
WITHHELD = {
    ("BioModels_MODEL2405300001_Infant_Gut_HMO_SynCom.yaml", "Bacteroides ovatus"): (
        "NCBITaxon:821 is Phocaeicola vulgatus; B. ovatus is NCBITaxon:28116. "
        "The record uses 821 correctly for its Bacteroides vulgatus entry."
    ),
    ("KBase_ORT_Workflow_Community_Model.yaml", "Nitrospiraceae bacterium"): (
        "NCBITaxon:1236 is class Gammaproteobacteria; Nitrospiraceae is Nitrospirota. "
        "The record uses 1236 correctly for its two Steroidobacteraceae entries."
    ),
}


def _taxon_term(record: str, preferred: str) -> dict | None:
    doc = yaml.safe_load((COMMUNITIES / record).read_text())
    for entry in doc.get("taxonomy") or []:
        term = entry.get("taxon_term") or {}
        if term.get("preferred_term") == preferred:
            return term
    return None


@pytest.mark.parametrize(
    ("record", "preferred"), list(WITHHELD), ids=[f"{r}::{p}" for r, p in WITHHELD]
)
def test_withheld_taxon_is_still_present(record: str, preferred: str):
    """The entry must still exist, or the pin is silently protecting nothing."""
    assert _taxon_term(record, preferred) is not None, (
        f"'{preferred}' is no longer in {record}. If the record was restructured, "
        f"update WITHHELD (see #292)."
    )


@pytest.mark.parametrize(
    ("record", "preferred"), list(WITHHELD), ids=[f"{r}::{p}" for r, p in WITHHELD]
)
def test_withheld_taxon_stays_ungrounded(record: str, preferred: str):
    """No GTDB block on a taxon whose NCBITaxon id names a different organism."""
    term = _taxon_term(record, preferred)
    assert term is not None
    assert "gtdb_classification" not in term, (
        f"'{preferred}' in {record} was grounded in GTDB, but its NCBITaxon id is "
        f"wrong: {WITHHELD[(record, preferred)]} A GTDB block derived from that id "
        f"describes the wrong organism. `gtdb_ground.py --apply` re-adds it on every "
        f"run (#293), so this is most likely an unreviewed tool re-run — revert it. "
        f"To ground it properly, fix the NCBITaxon id first (#292), then drop this "
        f"entry from WITHHELD."
    )


# ---------------------------------------------------------------------------
# The mirror case: a grounding the tool *will* produce, and must not (#372, #384).
# ---------------------------------------------------------------------------

# (record, preferred_term) -> (required gtdb_id, why the majority vote is wrong)
CURATED = {
    (
        "Dehalococcoides_Pelobacter_Acetylene_TCE_Coculture.yaml",
        "Pelobacter strain SFB93",
    ): (
        "GTDB:g__Syntrophotalea",
        "The organism is an acetylene fermenter, and the entry's own notes tie SFB93 "
        "to Syntrophotalea acetylenivorans. GTDB moved the acetylene-fermenting "
        "Pelobacters into Syntrophotalea (s__Syntrophotalea acetylenica, 8 genomes; "
        "s__Syntrophotalea_A acetylenivorans, 3). But all three NCBI Pelobacter "
        "rows naming Syntrophotalea are `sp.` rows, so the named-species filter "
        "(#375) discards the plurality lineage and the majority vote lands on "
        "g__Seleniibacterium at 0.571 — derived from P. seleniigenes, a selenate "
        "reducer. The tool has no memory of this, so `--refresh` re-breaks it.",
    ),
}


@pytest.mark.parametrize(
    ("record", "preferred"), list(CURATED), ids=[f"{r}::{p}" for r, p in CURATED]
)
def test_curated_grounding_is_not_overwritten_by_the_majority_vote(record: str, preferred: str):
    """A grounding chosen on evidence must survive a tool re-run.

    `WITHHELD` above protects taxa that must stay *ungrounded*. This protects the
    opposite: a taxon that is grounded correctly, where re-running the tool would
    replace a right answer with a confidently-wrong one.
    """
    term = _taxon_term(record, preferred)
    assert term is not None, f"'{preferred}' is no longer in {record}; update CURATED."

    expected, why = CURATED[(record, preferred)]
    grounding = term.get("gtdb_classification")
    assert grounding, f"'{preferred}' in {record} lost its curated grounding. {why}"
    assert grounding.get("gtdb_id") == expected, (
        f"'{preferred}' in {record} is grounded to {grounding.get('gtdb_id')}, not "
        f"the curated {expected}. {why} This is most likely an unreviewed "
        f"`gtdb_ground.py --refresh` — revert this block."
    )
