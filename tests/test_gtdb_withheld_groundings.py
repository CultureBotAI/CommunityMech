"""Keep deliberately-withheld GTDB groundings withheld (#292, #293).

A withheld taxon is one where the block ``gtdb_ground.py`` would derive is wrong,
so restating it in a second, independently-derived-looking field would make the
error harder to spot rather than easier.

``gtdb_ground.py --apply`` has no memory of that decision: it is otherwise
perfectly idempotent, but a re-run over the whole KB re-adds exactly these
blocks. Without this test the withhold lasts only until the next person runs the
tool and commits, and nothing anywhere fails.

Two reasons have put an entry here, and they need different fixes:

* **a wrong id** (#292) — the id named a different organism, so everything
  derived from it was wrong. Fix the id, re-run ``--apply``, and the right block
  appears on its own; then drop the entry. That is what happened to
  *Bacteroides ovatus*, which is why it is no longer listed.
* **a wrong majority** (#416) — the id is right, but GTDB's majority vote for it
  lands on a taxon whose physiology contradicts the record. No id edit fixes
  that; it needs a curator to choose the grounding.

Which one applies is in each entry's reason string, because the remediation
differs and guessing wrong wastes a maintainer's afternoon.
"""

from __future__ import annotations

from pathlib import Path

import pytest
import yaml

COMMUNITIES = Path(__file__).parent.parent / "kb/communities"

# (record, preferred_term) -> why the derived block would be wrong, and so which
# remediation applies. Tracked in #292 (wrong id) and #416 (wrong majority).
# `Bacteroides ovatus` was here until #292 was fixed: its id is now
# NCBITaxon:28116 and `--apply` produced GTDB:s__Bacteroides_ovatus on its own,
# exactly as the module docstring says it should. The entry is gone rather than
# kept-and-skipped, because a withhold list that outlives its reason is how a
# correct grounding gets suppressed later.
WITHHELD = {
    ("KBase_ORT_Workflow_Community_Model.yaml", "Nitrospiraceae bacterium"): (
        "GTDB's majority for NCBI Nitrospiraceae is f__Leptospirillaceae at 0.534, "
        "and Leptospirillum is an iron oxidizer while this genome is the record's "
        "nitrite oxidizer (#416). The id itself was corrected to NCBITaxon:189779."
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
    """No GTDB block on a taxon the tool would ground wrongly."""
    term = _taxon_term(record, preferred)
    assert term is not None
    assert "gtdb_classification" not in term, (
        f"'{preferred}' in {record} was grounded in GTDB, but that grounding is "
        f"wrong: {WITHHELD[(record, preferred)]} `gtdb_ground.py --apply` re-adds "
        f"it on every run (#293), so this is most likely an unreviewed tool re-run "
        f"— revert it. Read the reason above before trying to fix it properly: if "
        f"the NCBITaxon id is wrong, correct the id and the right block follows on "
        f"its own (#292); if the id is right and GTDB's majority is the problem, no "
        f"id edit helps and a curator has to choose the grounding (#416, #396). "
        f"Either way, drop this entry from WITHHELD only once it is actually right."
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


# ---------------------------------------------------------------------------
# The classifier that turns a withhold into a stored status (#294).
# ---------------------------------------------------------------------------


@pytest.fixture(scope="module")
def gtdb():
    import importlib.util

    spec = importlib.util.spec_from_file_location(
        "gtdb_ground", Path(__file__).parent.parent / "scripts/gtdb_ground.py"
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.mark.parametrize(("record", "preferred"), list(WITHHELD))
def test_a_withheld_taxon_classifies_as_withheld(gtdb, record, preferred):
    """Not NOT_ATTEMPTED, and not whatever the tool would have computed.

    WITHHELD is checked before anything is resolved, because the point of a
    withhold is that the tool *can* produce a grounding and must not. Classifying
    by outcome would mark these groundable and invite the re-run #293 exists to
    prevent.
    """
    term = _taxon_term(record, preferred)
    assert term is not None
    status, candidates = gtdb.classify_status(
        record,
        (term.get("term") or {}).get("id", ""),
        (term.get("term") or {}).get("label", ""),
        "gtdb_classification" in term,
        {},
        {},
        {},
        preferred=preferred,
    )
    assert status == "WITHHELD", f"{preferred} classified as {status}"
    assert candidates == []


def test_the_withhold_does_not_catch_a_sibling_sharing_the_id(gtdb):
    """The collision that keying by NCBITaxon id introduced (#294).

    Both withheld records use the offending id *correctly* for another entry —
    BioModels for its real Bacteroides vulgatus, KBase for two
    Steroidobacteraceae — so an id-keyed withhold list marked three sound
    groundings WITHHELD. The list is keyed by preferred_term for that reason.
    """
    record = "BioModels_MODEL2405300001_Infant_Gut_HMO_SynCom.yaml"
    doc = yaml.safe_load((COMMUNITIES / record).read_text())
    siblings = [
        entry["taxon_term"]
        for entry in doc["taxonomy"]
        if (entry["taxon_term"].get("term") or {}).get("id") == "NCBITaxon:821"
        and entry["taxon_term"].get("preferred_term") != "Bacteroides ovatus"
    ]
    assert siblings, "expected another entry on NCBITaxon:821 in this record"

    for term in siblings:
        status, _ = gtdb.classify_status(
            record,
            "NCBITaxon:821",
            (term.get("term") or {}).get("label", ""),
            "gtdb_classification" in term,
            {},
            {},
            {},
            preferred=term.get("preferred_term"),
        )
        assert status == "GROUNDED", (
            f"'{term.get('preferred_term')}' shares the withheld id and was "
            f"classified {status} — the withhold list is keyed by id again"
        )


def test_apply_does_not_reinstate_a_withheld_grounding(gtdb, tmp_path):
    """The guard #293 closed with a CI pin rather than a tool-level refusal.

    `WITHHELD_GROUNDINGS` was consulted only by `classify_status`, so the
    documented `gtdb_ground.py --community <file> --apply` still wrote the block:
    running it over the KB reinstated `NCBITaxon:1236` as
    `GTDB:c__Gammaproteobacteria`, derived from an id that names a different
    organism. CI caught it — after the write, in a diff that looked like every
    other block in the sweep (#402 review).

    The record keeps its real filename because the withhold is keyed on it.
    """
    record, preferred = next(iter(gtdb.WITHHELD_GROUNDINGS))
    source = COMMUNITIES / record
    destination = tmp_path / record
    destination.write_text(source.read_text())

    pairs = [
        (
            (e["taxon_term"].get("term") or {}).get("id", ""),
            (e["taxon_term"].get("term") or {}).get("label", ""),
        )
        for e in yaml.safe_load(destination.read_text())["taxonomy"]
    ]
    cleaned = [gtdb._clean_label(label) for _, label in pairs]
    try:
        mapping = gtdb.resolve_kg_microbe_dir(None) / "data/raw/NCBI2GTDB.tsv.gz"
    except SystemExit:
        pytest.skip("kg-microbe mapping unavailable")
    if not mapping.exists():
        pytest.skip("kg-microbe mapping unavailable")
    rows = gtdb.collect_rows(
        mapping,
        {i.split(":")[1] for i, _ in pairs if i},
        {c.lower() for c in cleaned if " " in c},
        {c.lower() for c in cleaned if " " not in c},
    )

    gtdb.apply_to_community(destination, *rows, "test-source")

    after = yaml.safe_load(destination.read_text())
    withheld = next(
        e["taxon_term"]
        for e in after["taxonomy"]
        if e["taxon_term"].get("preferred_term") == preferred
    )
    assert (
        "gtdb_classification" not in withheld
    ), f"--apply reinstated the withheld grounding for {preferred!r}"


def test_the_withhold_does_not_block_a_sibling_sharing_the_id(gtdb, tmp_path):
    """Both withheld records use the offending id correctly elsewhere.

    Keying the guard on the NCBITaxon id would leave those siblings permanently
    ungroundable — the same collision that mislabelled three groundings in #294.
    """
    record = "BioModels_MODEL2405300001_Infant_Gut_HMO_SynCom.yaml"
    doc = yaml.safe_load((COMMUNITIES / record).read_text())
    siblings = [
        e["taxon_term"]
        for e in doc["taxonomy"]
        if (e["taxon_term"].get("term") or {}).get("id") == "NCBITaxon:821"
        and e["taxon_term"].get("preferred_term") != "Bacteroides ovatus"
    ]
    assert siblings, "expected another entry on NCBITaxon:821"
    for term in siblings:
        assert term.get(
            "gtdb_classification"
        ), "a correct grounding sharing the withheld id lost its block"
