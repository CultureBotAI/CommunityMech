"""A `gtdb_classification` must still describe the `term.id` it was derived from.

The block is derived data: `gtdb_ground.py` reads `taxon_term.term.id` and writes
the result, recording the input in `ncbi_source_id`. Nothing tied the two
together afterwards, so editing the id left the derived block describing a
different organism, with no gate objecting (#314).

**Be precise about what this does and does not catch.** In the #314 instance the
id was corrected *before* the record was ever committed, so `main` held an
**absent** block, never a stale one — `git log --follow` shows the entry reading
`NCBITaxon:1125` with no grounding from its first commit. The two general
assertions below inspect only taxa that *have* a block, so neither would have
caught #314. Test 3 pins that instance directly; the general pair guards the
sibling failure mode, where the block survives an id edit and quietly describes
the previous organism.

The resulting blank is also *ambiguous*, which is the deeper problem: of the 381
ungrounded taxa here, 292 have no GTDB equivalent, 87 are ambiguous, and 2 are
withheld on purpose (#292, pinned by `tests/test_gtdb_withheld_groundings.py`) —
292 + 87 + 2 = 381. Telling an accidental gap from a deliberate one took
re-running the grounding tool over the whole KB. #294's status enum is the real
fix; this is the cheap half that works today and needs no schema change.

`ncbi_source_id` holds for all 647 grounded taxa right now, so this is a guard
against the next id edit, not a report on this one.
"""

from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).parent.parent
# `data/isolates/` uses the same `taxonomy[].taxon_term` shape and carries no
# grounding today, but a grounded isolate would otherwise slip past unseen — the
# directory has been outside a gate's scope once already (#310).
RECORD_DIRS = ("kb/communities", "data/isolates")


def _grounded_taxa():
    """(record, preferred_term, term_id, gtdb_classification) for every grounded taxon."""
    found = []
    paths = [p for d in RECORD_DIRS for p in sorted((REPO / d).glob("*.yaml"))]
    for path in paths:
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
        if grounding.get("ncbi_source_id") != term_id
    ]
    assert not stale, (
        "gtdb_classification derived from a different id than the taxon now carries — "
        "re-run `gtdb_ground.py --apply` on these records:\n" + "\n".join(f"  {s}" for s in stale)
    )


def test_the_known_stale_entry_is_now_grounded():
    """The instance that prompted #314, pinned so it cannot silently regress."""
    record = REPO / "kb/communities/Mesorhizobium_Synechococcus_B12_Synthetic_Consortium.yaml"
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


def test_grounding_is_internally_coherent(grounded):
    """A block whose fields contradict each other passed every check above.

    `gtdb_id`, `gtdb_taxon` and the tail of `gtdb_lineage` are three spellings of
    one answer, and `majority_fraction` is a share of genomes, so it cannot
    exceed 1 — nor fall at or below 0.5, since the tool grounds on a majority.
    `linkml-validate` accepts `majority_fraction: 7.5` today.
    """
    problems = []
    for record, name, _, g in grounded:
        gtdb_id, taxon, lineage = (
            g.get("gtdb_id", ""),
            g.get("gtdb_taxon"),
            g.get("gtdb_lineage", ""),
        )
        where = f"{record}: {name}"

        # GTDB:g__Foo -> the lineage must end in that same g__Foo
        rank_token = gtdb_id.split(":", 1)[-1]
        if lineage and rank_token and lineage.split(";")[-1].replace(" ", "_") != rank_token:
            problems.append(
                f"{where}\n      gtdb_id={gtdb_id} but lineage ends {lineage.split(';')[-1]!r}"
            )

        if taxon and rank_token and taxon.replace(" ", "_") != rank_token.split("__", 1)[-1]:
            problems.append(f"{where}\n      gtdb_id={gtdb_id} but gtdb_taxon={taxon!r}")

        fraction = g.get("majority_fraction")
        if fraction is not None and not (0.5 <= fraction <= 1.0):
            problems.append(f"{where}\n      majority_fraction={fraction} outside (0.5, 1]")

    assert not problems, "internally inconsistent gtdb_classification:\n" + "\n".join(
        f"  {p}" for p in problems
    )
