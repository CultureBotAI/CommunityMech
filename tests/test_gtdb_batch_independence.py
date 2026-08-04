"""Grounding a taxon must not depend on which other taxa share the run.

`collect_rows()` indexes each mapping row under the NCBI names it carries. It
used to `break` after the first rank that matched something the caller wanted, so
a row naming two wanted taxa — genus *Methanosarcina* inside phylum
*Methanobacteriota*, say — counted only toward whichever rank `HIGHER_RANKS`
reached first. A taxon's row set therefore depended on the *batch*: grounding one
record alone and grounding the whole KB could disagree for the same id.

Measured before the fix: asking for `methanobacteriota` alone collected 1534
rows; asking for it alongside three unrelated taxa collected 1456. Higher ranks
were starved worst — over the whole KB, `pseudomonadota` went from 238 rows to
35874 once the `break` was removed.

That is not academic. It changed three whole-KB outcomes, one of which was live
in the KB: `NCBITaxon:403` (*Methylococcaceae*) had been grounded to
`GTDB:f__Methylococcaceae` on a bare 0.505 majority computed from a starved row
set. With the full set it resolves to `GTDB:f__Methylomonadaceae` at 0.695 (0.64 before the
named-species filter became the default in #372), and
`is_reclassified` flips to true. GTDB did not *rename* Methylococcaceae —
`f__Methylococcaceae` still exists and holds 31% of the NCBI family, including
the type genus *Methylococcus*. It **split** it, and the majority moved. The
record's own notes name *Methylobacter*, *Methylomonas* and *Methylosarcina*,
all of which are `f__Methylomonadaceae` with zero genomes in the retained family,
so the grounding matches this record's organisms and not merely the majority.

These tests are deliberately structural: they compare row sets rather than
grounding outcomes, so they hold regardless of which `NCBI2GTDB` release is
present. Outcome-level drift against a newer release is a different problem
(#369).
"""

import importlib.util
from pathlib import Path

import pytest

REPO = Path(__file__).parent.parent


@pytest.fixture(scope="module")
def gtdb():
    spec = importlib.util.spec_from_file_location("gtdb_ground", REPO / "scripts/gtdb_ground.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def mapping(gtdb):
    """The kg-microbe NCBI2GTDB table, or skip.

    CI has no kg-microbe checkout. `resolve_kg_microbe_dir` calls `sys.exit()`
    when it finds none, which pytest reports as an *error*, not a skip — so
    catching SystemExit is what keeps this from reddening a build that simply
    lacks an optional local dependency.
    """
    try:
        path = gtdb.resolve_kg_microbe_dir(None) / "data/raw/NCBI2GTDB.tsv.gz"
    except SystemExit as exc:
        pytest.skip(f"kg-microbe mapping unavailable: {str(exc).splitlines()[0]}")
    if not path.exists():
        pytest.skip(f"kg-microbe NCBI2GTDB mapping not available at {path}")
    return path


def test_row_set_is_unchanged_by_unrelated_taxa_in_the_batch(gtdb, mapping):
    """The defect, at its smallest: one taxon, with and without company.

    *Methanosarcina* is a genus inside phylum *Methanobacteriota*, so rows naming
    both were stolen by the genus and never counted toward the phylum.
    """
    alone = gtdb.collect_rows(mapping, set(), set(), {"methanobacteriota"})[2]
    assert alone.get("methanobacteriota"), (
        "no rows for this taxon — the mapping no longer carries the name, so this "
        "test would pass by comparing None to None"
    )
    with_company = gtdb.collect_rows(
        mapping, set(), set(), {"methanobacteriota", "methanosarcina", "clostridia", "bacilli"}
    )[2]

    assert alone.get("methanobacteriota") == with_company.get("methanobacteriota"), (
        "asking for extra taxa changed this taxon's row set — a row matching two "
        "wanted ranks is being counted toward only one of them (#366)"
    )


def test_a_nested_pair_lands_in_both_row_sets(gtdb, mapping):
    """A row naming both a wanted genus and its wanted phylum belongs to each."""
    both = gtdb.collect_rows(mapping, set(), set(), {"methanobacteriota", "methanosarcina"})[2]

    assert both.get("methanosarcina"), "expected rows for the genus"
    assert both.get("methanobacteriota"), "expected rows for the phylum"

    genus_rows = {tuple(row) for row in both["methanosarcina"]}
    phylum_rows = {tuple(row) for row in both["methanobacteriota"]}
    shared = genus_rows & phylum_rows
    assert shared, (
        "no row was indexed under both the genus and its parent phylum, so one "
        "rank is still shadowing the other (#366)"
    )


@pytest.mark.parametrize(
    "name",
    ["pseudomonadota", "bacillota", "gammaproteobacteria", "actinomycetota", "bacilli"],
)
def test_higher_ranks_are_not_starved_by_their_own_members(gtdb, mapping, name):
    """Each of these lost most of its rows to a nested genus or family.

    `pseudomonadota` collected 238 rows before the fix and 35874 after, so a
    majority computed from the old set was drawn from under 1% of the evidence.
    """
    alone = gtdb.collect_rows(mapping, set(), set(), {name})[2].get(name, [])
    assert alone, f"no rows for {name} — the comparison below would be 0 == 0"
    crowded = gtdb.collect_rows(
        mapping,
        set(),
        set(),
        {name, "escherichia", "bacillus", "staphylococcus", "streptomyces", "pseudomonas"},
    )[2].get(name, [])

    assert alone == crowded, (
        f"{name} collected {len(alone)} rows alone but {len(crowded)} alongside "
        f"five common genera — its row set depends on the batch (#366)"
    )


def test_the_regrounded_record_matches_the_tool(gtdb, mapping):
    """`NCBITaxon:403` is the live outcome the fix changed, pinned to the tool.

    The stored block claimed `GTDB:f__Methylococcaceae` at a 0.505 majority and
    `is_reclassified: false`; the full row set gives `Methylomonadaceae` at 0.695,
    reclassified. If these drift apart again, one of them is stale.
    """
    import yaml

    record = REPO / "kb/communities/Lake_Washington_Methane_Oxygen_Methylotroph_Community.yaml"
    data = yaml.safe_load(record.read_text())
    stored = next(
        t["taxon_term"]["gtdb_classification"]
        for t in data["taxonomy"]
        if (t["taxon_term"].get("term") or {}).get("id") == "NCBITaxon:403"
    )

    by_id, by_name, by_higher = gtdb.collect_rows(mapping, {"403"}, set(), {"methylococcaceae"})
    fresh = gtdb.resolve_target("403", "Methylococcaceae", by_id, by_name, by_higher)

    assert fresh["gtdb_id"] == stored["gtdb_id"] == "GTDB:f__Methylomonadaceae"
    # Pin the tool's own values too. Asserting only on the stored YAML let two
    # mutants through: destroying the genome weighting, and hard-wiring
    # is_reclassified False in resolve_higher.
    assert fresh["majority_fraction"] == stored["majority_fraction"] == 0.695
    assert (
        fresh["is_reclassified"] is stored["is_reclassified"] is True
    ), "GTDB's name for this family differs from NCBI's, so both must say so"
