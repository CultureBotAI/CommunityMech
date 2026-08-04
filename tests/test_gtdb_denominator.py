"""The two GTDB majority denominators, and why the default stays `aggregate` (#371).

`NCBI2GTDB.tsv.gz` is an upstream crosswalk in which each row is an independent
NCBI->GTDB assignment carrying its own genome support. `aggregate` (the default)
sums every matched row; `deepest` keeps one row per lineage, at the deepest rank
present — the rule `kg-microbe-paper` settled on for the same shape of problem.

The comparison is the point, not a winner. `scripts/gtdb_denominator_compare.py`
writes both answers for all 578 KB taxa; 5 flip, affecting 26 stored blocks.

The tests below pin the mechanics and one diagnostic result. `deepest` is *not*
a neutral correction: dropping a lineage's species rows while keeping its strain
rows shifts weight toward lineages that happen to be annotated at strain rank.
`Acetobacter` is the clearest case — `CAG-267`'s support is two strain rows (336
and 2 genomes), so it survives intact while Acetobacter's own support falls from
458 to 289, and a cultivated genus in a Drosophila gut record grounds to an
uncultivated MAG lineage. That is why the default did not change.
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
    try:
        path = gtdb.resolve_kg_microbe_dir(None) / "data/raw/NCBI2GTDB.tsv.gz"
    except SystemExit as exc:
        pytest.skip(f"kg-microbe mapping unavailable: {str(exc).splitlines()[0]}")
    if not path.exists():
        pytest.skip(f"kg-microbe NCBI2GTDB mapping not available at {path}")
    return path


def _row(species="", strain="", genomes="1"):
    """A mapping row with only the columns `deepest_only` reads."""
    cells = [""] * 20
    cells[2], cells[10], cells[11] = genomes, species, strain
    return cells


def test_a_lineage_with_strain_rows_keeps_only_those(gtdb):
    species_row = _row(species="Escherichia coli")
    strain_a = _row(species="Escherichia coli", strain="K-12")
    strain_b = _row(species="Escherichia coli", strain="B")

    kept = gtdb.deepest_only([species_row, strain_a, strain_b])

    assert kept == [strain_a, strain_b], "the species row must not be summed alongside its strains"


def test_a_lineage_without_strain_rows_keeps_its_species_row(gtdb):
    species_row = _row(species="Methylococcus capsulatus")
    assert gtdb.deepest_only([species_row]) == [species_row]


def test_lineages_are_independent(gtdb):
    """One lineage having strains must not suppress another's species row."""
    a_species = _row(species="Species A")
    a_strain = _row(species="Species A", strain="A1")
    b_species = _row(species="Species B")

    kept = gtdb.deepest_only([a_species, a_strain, b_species])

    assert a_strain in kept and b_species in kept
    assert a_species not in kept


def test_a_strain_row_with_no_species_is_its_own_lineage(gtdb):
    """The leaf case, handled first and deliberately.

    In the prior art this was the one real bug: a taxon already at strain rank
    was looked up as if it were a parent, found nothing, and was silently
    dropped. Here, pooling speciesless strain rows under one `""` key would make
    them compete as a single lineage.
    """
    orphan_a = _row(strain="Strain X", genomes="5")
    orphan_b = _row(strain="Strain Y", genomes="7")

    kept = gtdb.deepest_only([orphan_a, orphan_b])

    assert len(kept) == 2, "distinct speciesless strains must not collapse into one lineage"


def test_default_denominator_is_unchanged(gtdb, mapping):
    """`aggregate` must reproduce what the KB was grounded with."""
    _, _, by_higher = gtdb.collect_rows(mapping, set(), set(), {"methylococcaceae"})

    default = gtdb.resolve_higher(
        "methylococcaceae", "NCBITaxon:403", "Methylococcaceae", by_higher
    )
    explicit = gtdb.resolve_higher(
        "methylococcaceae", "NCBITaxon:403", "Methylococcaceae", by_higher, "aggregate"
    )

    assert default == explicit
    assert default["gtdb_id"] == "GTDB:f__Methylomonadaceae"
    assert default["majority_fraction"] == 0.64


def test_deepest_shifts_weight_toward_strain_annotated_lineages(gtdb, mapping):
    """The diagnostic that kept `aggregate` as the default.

    Acetobacter is a cultivated genus; CAG-267 is an uncultivated MAG lineage
    whose support here is entirely strain rows. Under `deepest` it wins, which is
    the wrong answer for the Drosophila gut record that carries this taxon.
    """
    _, _, by_higher = gtdb.collect_rows(mapping, set(), set(), {"acetobacter"})

    aggregate = gtdb.resolve_higher("acetobacter", "NCBITaxon:434", "Acetobacter", by_higher)
    deepest = gtdb.resolve_higher(
        "acetobacter", "NCBITaxon:434", "Acetobacter", by_higher, "deepest"
    )

    assert aggregate["gtdb_id"] == "GTDB:g__Acetobacter"
    assert deepest["gtdb_id"] == "GTDB:g__CAG-267", (
        "if this no longer holds, re-run scripts/gtdb_denominator_compare.py — the "
        "argument for the current default rests on it"
    )
