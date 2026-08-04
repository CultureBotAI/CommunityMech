"""A `gtdb_classification` must still describe the `term.id` it was derived from.

The block is derived data: `gtdb_ground.py` reads `taxon_term.term.id` and writes
the result, recording the input in `ncbi_source_id`. Nothing tied the two
together afterwards, so editing the id left the derived block describing a
different organism, with no gate objecting (#314).

That is exactly what happened to `Mesorhizobium_Synechococcus_B12_Synthetic_Consortium`:
grounding ran against `NCBITaxon:1126` (*Microcystis aeruginosa*), review then
established the paper names only a genus and changed the id to `NCBITaxon:1125`,
and grounding was never re-run.

The resulting blank is worse than wrong, it is *ambiguous*: of 382 ungrounded
taxa, 288 have no GTDB equivalent, 87 are ambiguous, and a handful are withheld
on purpose (#292, pinned by `tests/test_gtdb_withheld_groundings.py`). Telling an
accidental gap from a deliberate one took re-running the grounding tool over the
whole KB. `#294`'s status enum is the real fix; this is the cheap half that works
today and needs no schema change.

`ncbi_source_id` is the only self-check the block carries, so it is worth
asserting even though it holds for all 647 grounded taxa right now — it is a
guard against the next id edit, not a report on this one.
"""

from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).parent.parent
COMMUNITIES = REPO / "kb/communities"


def _grounded_taxa():
    """(record, preferred_term, term_id, gtdb_classification) for every grounded taxon."""
    found = []
    for path in sorted(COMMUNITIES.glob("*.yaml")):
        data = yaml.safe_load(path.read_text()) or {}
        for taxon in data.get("taxonomy") or []:
            if not isinstance(taxon, dict):
                continue
            term_block = taxon.get("taxon_term") or {}
            grounding = term_block.get("gtdb_classification")
            if not grounding:
                continue
            found.append(
                (
                    path.name,
                    term_block.get("preferred_term"),
                    (term_block.get("term") or {}).get("id"),
                    grounding,
                )
            )
    return found


@pytest.fixture(scope="module")
def grounded():
    found = _grounded_taxa()
    # A relative path or an empty glob would pass every assertion below vacuously.
    assert len(found) > 500, f"expected the grounded KB, swept only {len(found)} taxa"
    return found


def test_grounding_records_the_id_it_was_derived_from(grounded):
    """`ncbi_source_id` must be present — it is the block's only provenance."""
    missing = [
        f"{record}: {name}"
        for record, name, _, grounding in grounded
        if not grounding.get("ncbi_source_id")
    ]
    assert not missing, "gtdb_classification without ncbi_source_id:\n" + "\n".join(
        f"  {m}" for m in missing
    )


def test_grounding_is_not_stale_against_its_taxon_id(grounded):
    """The derived block must describe the taxon it is attached to.

    Editing `term.id` after grounding leaves the block describing the *previous*
    organism. Nothing else in the pipeline notices (#314).
    """
    stale = [
        f"{record}: {name}\n"
        f"      term.id        = {term_id}\n"
        f"      ncbi_source_id = {grounding.get('ncbi_source_id')}"
        for record, name, term_id, grounding in grounded
        if term_id and grounding.get("ncbi_source_id") != term_id
    ]
    assert not stale, (
        "gtdb_classification derived from a different id than the taxon now carries — "
        "re-run `gtdb_ground.py --apply` on these records:\n" + "\n".join(f"  {s}" for s in stale)
    )


def test_the_known_stale_entry_is_now_grounded():
    """The instance that prompted #314, pinned so it cannot silently regress."""
    record = COMMUNITIES / "Mesorhizobium_Synechococcus_B12_Synthetic_Consortium.yaml"
    data = yaml.safe_load(record.read_text())

    by_id = {
        (t["taxon_term"].get("term") or {}).get("id"): t["taxon_term"] for t in data["taxonomy"]
    }
    microcystis = by_id.get("NCBITaxon:1125")
    assert microcystis, "NCBITaxon:1125 is no longer in this record"

    grounding = microcystis.get("gtdb_classification")
    assert grounding, "NCBITaxon:1125 is ungrounded again (#314)"
    assert grounding["ncbi_source_id"] == "NCBITaxon:1125"
    assert grounding["gtdb_id"] == "GTDB:g__Microcystis", (
        "the paper names only a genus, so this must stay at g__ rank — an earlier "
        "draft grounded it to Microcystis aeruginosa, which the source never names"
    )
