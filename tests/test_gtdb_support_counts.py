"""A `majority_fraction` must say what it is a fraction *of* (#383).

`0.571` reads identically whether it came from 4 genomes or 4000, and `1.0` can
rest on a single row. That is not hypothetical: across the KB, **19 higher-rank
groundings rest on fewer than 10 genomes and every one of them reads 1.0** — a
phylum grounded on 7 genomes is indistinguishable, in the stored block, from one
grounded on 7000. The named-species filter (#375) made this sharper, because it
shrinks the evidence without recording that it did.

So the block now carries the numerator and the denominator:

* ``support_genomes`` — genomes behind the chosen GTDB taxon.
* ``total_genomes``   — genomes across every candidate at that rank.

Rounding is why they cannot be inferred: `majority_fraction` is rounded to 3
places, so 4/7 and 4000/7000 both store as 0.571.

**`total_genomes` is deliberately absent on the species path.** There the
fraction is the crosswalk's own column rather than something this script
computes, so a locally-summed denominator would contradict it — *Bacillus
velezensis* is 1163 genomes on the chosen row against 1196 across all its rows,
while the crosswalk calls it 1.0. Publishing 1163/1196 next to `1.0` would be
worse than publishing no denominator at all, so only `support_genomes` is
emitted there.
"""

from __future__ import annotations

import importlib.util
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).parent.parent
RECORD_DIRS = ("kb/communities", "data/isolates")


@pytest.fixture(scope="module")
def gtdb():
    spec = importlib.util.spec_from_file_location("gtdb_ground", REPO / "scripts/gtdb_ground.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def mapping(gtdb):
    try:
        path = gtdb.resolve_kg_microbe_dir(None) / "data/raw/NCBI2GTDB.tsv.gz"
    except SystemExit as exc:
        pytest.skip(f"kg-microbe mapping unavailable: {str(exc).splitlines()[0]}")
    if not path.exists():
        pytest.skip(f"kg-microbe NCBI2GTDB mapping not available at {path}")
    return path


@pytest.fixture(scope="module")
def grounded():
    """Every stored gtdb_classification block in the KB."""
    found = []
    for directory in RECORD_DIRS:
        for path in sorted((REPO / directory).glob("*.yaml")):
            data = yaml.safe_load(path.read_text()) or {}
            for entry in data.get("taxonomy") or []:
                if not isinstance(entry, dict):
                    continue
                term = entry.get("taxon_term") or {}
                block = term.get("gtdb_classification")
                if block:
                    found.append((path.name, term.get("preferred_term"), block))
    assert len(found) > 500, f"expected the grounded KB, swept only {len(found)}"
    return found


def _higher_rank_row(gtdb_genus, genomes, species="Testgenus namedspecies"):
    """A crosswalk row matching NCBI genus `Testgenus`."""
    cells = [""] * 20
    cells[2], cells[9], cells[17], cells[10] = genomes, "Testgenus", gtdb_genus, species
    return cells


def test_the_denominator_is_recorded_for_a_computed_majority(gtdb):
    by_higher = {
        "testgenus": [
            _higher_rank_row("g__Alpha", "40"),
            _higher_rank_row("g__Beta", "60"),
        ]
    }
    result = gtdb.resolve_higher("testgenus", "NCBITaxon:1", "Testgenus", by_higher)

    assert result["gtdb_taxon"] == "g__Beta"
    assert result["support_genomes"] == 60
    assert result["total_genomes"] == 100
    assert result["majority_fraction"] == 0.6


def test_the_counts_distinguish_two_groundings_that_share_a_fraction(gtdb):
    """The whole point: 4/7 and 4000/7000 both round to 0.571."""
    thin = gtdb.resolve_higher(
        "testgenus",
        "NCBITaxon:1",
        "Testgenus",
        {"testgenus": [_higher_rank_row("g__Alpha", "4"), _higher_rank_row("g__Beta", "3")]},
    )
    thick = gtdb.resolve_higher(
        "testgenus",
        "NCBITaxon:1",
        "Testgenus",
        {"testgenus": [_higher_rank_row("g__Alpha", "4000"), _higher_rank_row("g__Beta", "3000")]},
    )

    assert thin["majority_fraction"] == thick["majority_fraction"] == 0.571
    assert (thin["support_genomes"], thin["total_genomes"]) == (4, 7)
    assert (thick["support_genomes"], thick["total_genomes"]) == (4000, 7000)


def test_the_filter_shrinks_the_denominator_it_reports(gtdb):
    """The counts must describe what was *counted*, not what was available.

    A denominator that included the dropped MAG rows would overstate the evidence
    by exactly the amount the filter removed, which is the opposite of the point.
    """
    rows = [
        _higher_rank_row("g__Alpha", "4"),
        _higher_rank_row("g__Beta", "3"),
        _higher_rank_row("g__Beta", "500", species="Testgenus sp. MAG-1"),
    ]
    filtered = gtdb.resolve_higher("testgenus", "NCBITaxon:1", "Testgenus", {"testgenus": rows})
    unfiltered = gtdb.resolve_higher(
        "testgenus", "NCBITaxon:1", "Testgenus", {"testgenus": rows}, exclude_unnamed=False
    )

    assert filtered["total_genomes"] == 7, "the dropped MAG row must not be counted"
    assert unfiltered["total_genomes"] == 507
    assert filtered["gtdb_taxon"] != unfiltered["gtdb_taxon"], "expected the filter to decide this"


@pytest.mark.parametrize("cell", ["", "not-a-number", None])
def test_an_unparseable_genome_count_does_not_crash_the_grounding(gtdb, cell):
    row = _higher_rank_row("g__Alpha", "10")
    bad = _higher_rank_row("g__Beta", "1")
    bad[2] = cell
    result = gtdb.resolve_higher("testgenus", "NCBITaxon:1", "Testgenus", {"testgenus": [row, bad]})
    assert result["support_genomes"] == 10


def test_the_species_path_reports_support_but_no_denominator(gtdb, mapping):
    """A locally-summed denominator would contradict the crosswalk's own fraction."""
    by_id, by_name, by_higher = gtdb.collect_rows(
        mapping, {"492670"}, {"bacillus velezensis"}, set()
    )
    result = gtdb.resolve_target("492670", "Bacillus velezensis", by_id, by_name, by_higher)

    assert result["gtdb_id"] == "GTDB:s__Bacillus_velezensis"
    assert result["support_genomes"] > 0, "the species path must still say how much evidence"
    assert "total_genomes" not in result, (
        "the species path must not publish a denominator — its majority_fraction "
        "comes from the crosswalk, not from this script"
    )


def test_every_stored_fraction_agrees_with_its_counts(grounded):
    """The stored block must be internally consistent, or the counts mislead."""
    wrong = []
    for record, name, block in grounded:
        support, total = block.get("support_genomes"), block.get("total_genomes")
        fraction = block.get("majority_fraction")
        if total is None or support is None or fraction is None:
            continue
        if total <= 0 or round(support / total, 3) != fraction:
            wrong.append(f"{record}: {name} — {support}/{total} != {fraction}")
    assert not wrong, "majority_fraction disagrees with its own counts:\n" + "\n".join(
        f"  {w}" for w in wrong
    )


def test_support_never_exceeds_the_total(grounded):
    bad = [
        f"{record}: {name} — support {block['support_genomes']} > total {block['total_genomes']}"
        for record, name, block in grounded
        if block.get("total_genomes") is not None
        and block.get("support_genomes") is not None
        and block["support_genomes"] > block["total_genomes"]
    ]
    assert not bad, "\n".join(bad)


def test_the_kb_carries_the_counts(grounded):
    """Without this, shipping the schema change but not the sweep would pass."""
    with_support = [b for _, _, b in grounded if b.get("support_genomes") is not None]
    assert len(with_support) > 600, (
        f"only {len(with_support)} of {len(grounded)} blocks carry support_genomes — "
        f"the KB was not re-swept after the schema change (#383)"
    )


def test_the_thin_groundings_are_visible(grounded):
    """The population this issue exists for, now findable by reading the KB.

    Every one of these reads `majority_fraction: 1.0`. Before the counts landed,
    nothing in the record distinguished them from a grounding drawn from
    thousands of genomes. This asserts they are *visible*, not that they are
    wrong — a small genus is legitimately small.
    """
    thin = [
        (record, name, b["gtdb_id"], b["support_genomes"], b["total_genomes"])
        for record, name, b in grounded
        if b.get("total_genomes") is not None and b["total_genomes"] < 10
    ]
    assert thin, "expected to find low-evidence groundings; has the mapping changed?"
    assert all(t[4] > 0 for t in thin), "a zero denominator would be a division bug"


def test_the_emitted_block_carries_the_counts(gtdb):
    """`_block` is what actually reaches the YAML, and nothing covered it.

    The KB-level assertions above read files that were already swept, so deleting
    the counts from `_block` left every one of them green — a regression would
    ship and only surface on the next re-grounding.
    """
    grounding = gtdb.resolve_higher(
        "testgenus",
        "NCBITaxon:1",
        "Testgenus",
        {"testgenus": [_higher_rank_row("g__Alpha", "4"), _higher_rank_row("g__Beta", "3")]},
    )

    block = gtdb._block(grounding, "test-source")

    assert block["support_genomes"] == 4
    assert block["total_genomes"] == 7
    assert "support_genomes" in gtdb.emit_block(grounding, "test-source")


def test_an_emitted_species_block_omits_the_denominator(gtdb, mapping):
    """`_block` must not invent a `total_genomes` the species path did not compute."""
    by_id, by_name, by_higher = gtdb.collect_rows(
        mapping, {"492670"}, {"bacillus velezensis"}, set()
    )
    grounding = gtdb.resolve_target("492670", "Bacillus velezensis", by_id, by_name, by_higher)

    block = gtdb._block(grounding, "test-source")

    assert block["support_genomes"] > 0
    assert "total_genomes" not in block, (
        "a species block must omit the denominator entirely — writing "
        "`total_genomes: null` puts noise on 335 records and hides from a "
        "`.get()`-based diff, which is how it survived the first sweep"
    )
    assert "total_genomes" not in gtdb.emit_block(grounding, "test-source")
