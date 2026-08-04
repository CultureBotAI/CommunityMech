"""The two GTDB majority denominators, and why the default stays `aggregate` (#371).

`NCBI2GTDB.tsv.gz` is an upstream crosswalk in which each row is an independent
NCBI->GTDB assignment carrying its own genome support. `aggregate` (the default)
sums every matched row; `deepest` keeps one row per lineage, at the deepest rank
present — the rule `kg-microbe-paper` settled on for the same shape of problem.

The comparison is the point, not a winner. `scripts/gtdb_denominator_compare.py`
writes both answers for all 578 KB taxa; 5 flip, affecting 26 stored blocks.

`deepest` is *not* a neutral correction: dropping a lineage's species rows while
keeping its strain rows shifts weight toward lineages that happen to be annotated
at strain rank. Table-wide it discards 801367 of 1837914 genome-supports (43.6%).

Judged against GTDB's own rule — the lineage holding the nomenclatural type keeps
the unsuffixed name — `aggregate` is the better answer for 4 of the 5 taxa where
they differ. The sharpest is Pseudomonas: `deepest` discards *P. aeruginosa*'s
17191-genome species row in favour of 615 genomes across 289 strain rows, and
lands on `g__Pseudomonas_E` at 0.852 — more confidently wrong than the Acetobacter
case, which is only 0.522.

**The default is not uniformly right.** For Enterococcus it grounds to
`g__Enterococcus_B`, the *E. faecium* clade, purely because faecium is more
sequenced than the type species *E. faecalis* — see #373 and #374. `deepest`
returns AMBIGUOUS there, which is the honest answer.

A third option neither denominator covers would fix Acetobacter under both:
exclude `sp.`/`uncultured` MAG rows (#375).
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


def test_a_row_with_neither_species_nor_strain_is_kept_separately(gtdb):
    """The both-blank branch — the one the narrative leans on, previously untested.

    Keying on the species alone pools every such row under `""`. Mixed with a
    speciesless *strain* row that pooling is detectable: the blank row would land
    in the same lineage and be suppressed as its "species" alternative, so the
    count drops. Without this case, deleting the fallback entirely passed.
    """
    blank_a = _row(genomes="3")
    blank_b = _row(genomes="4")
    speciesless_strain = _row(strain="Strain Z", genomes="9")

    kept = gtdb.deepest_only([blank_a, blank_b, speciesless_strain])

    assert len(kept) == 3, "three unrelated rows must remain three lineages"
    assert blank_a in kept and blank_b in kept and speciesless_strain in kept


def test_species_key_is_normalised(gtdb):
    """Case and surrounding whitespace must not split one lineage in two."""
    species_row = _row(species="Escherichia coli")
    strain_row = _row(species="  escherichia COLI  ", strain="K-12")

    kept = gtdb.deepest_only([species_row, strain_row])

    assert kept == [strain_row], "the species row must be recognised as the same lineage"


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
    """One of four cases favouring the default, and the narrowest.

    Acetobacter is a cultivated genus; CAG-267 is an uncultivated MAG lineage
    whose support here is entirely strain rows. Under `deepest` it wins, which is
    the wrong answer for the Drosophila gut record that carries this taxon.

    The margin is thin — 458 against 338, and CAG-267 grew 33 -> 120 genomes
    between R214 and R220 — so this assertion doubles as a tripwire on the
    default itself (#375).
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


# ---------------------------------------------------------------------------
# The named-species filter (#375): a third axis, also opt-in.
# ---------------------------------------------------------------------------


def test_unnamed_species_rows_are_dropped(gtdb):
    kept = gtdb.named_species_only(
        [
            _row(species="Acetobacter aceti"),
            _row(species="Acetobacter sp. 46_36"),
            _row(species="uncultured Acetobacter"),
            _row(species="Firmicutes bacterium CAG:176"),
            _row(species="unclassified Acetobacter"),
            _row(species=""),
        ]
    )
    assert [r[10] for r in kept] == ["Acetobacter aceti"]


def test_candidatus_names_are_kept(gtdb):
    """A Candidatus name is a provisional *species* name, not a placeholder.

    Excluding it would discard legitimate taxonomy for uncultivated organisms,
    which is the opposite of what this filter is for.
    """
    row = _row(species="Candidatus Cibiobacter qucibialis")
    assert gtdb.named_species_only([row]) == [row]


def test_filter_never_empties_a_taxon(gtdb, mapping):
    """A genus known only from bins must keep its grounding, not lose it.

    The filter is a tie-breaker among named species, not a reason to abandon a
    taxon that has none.
    """
    _, _, by_higher = gtdb.collect_rows(mapping, set(), set(), {"acetobacter"})
    rows = [r for r in by_higher["acetobacter"] if r[9].strip().lower() == "acetobacter"]
    unnamed = [r for r in rows if not gtdb.named_species_only([r])]
    assert unnamed, "expected some unnamed rows in this genus"

    only_unnamed = {"acetobacter": unnamed}
    result = gtdb.resolve_higher(
        "acetobacter", "NCBITaxon:434", "Acetobacter", only_unnamed, exclude_unnamed=True
    )
    assert result, "filtering to nothing must fall back rather than drop the taxon"


def test_the_filter_makes_both_denominators_agree_on_acetobacter(gtdb, mapping):
    """#375's claim, and the reason the filter exists.

    Without it the two denominators disagree here — `g__Acetobacter` against the
    uncultivated `g__CAG-267`. With it, both reach `g__Acetobacter`.
    """
    _, _, by_higher = gtdb.collect_rows(mapping, set(), set(), {"acetobacter"})
    answers = {
        den: gtdb.resolve_higher(
            "acetobacter", "NCBITaxon:434", "Acetobacter", by_higher, den, exclude_unnamed=True
        )["gtdb_id"]
        for den in ("aggregate", "deepest")
    }
    assert answers == {"aggregate": "GTDB:g__Acetobacter", "deepest": "GTDB:g__Acetobacter"}


def test_the_filter_does_not_settle_the_denominator_question(gtdb, mapping):
    """It fixes the MAG pathology; it does not make the choice moot.

    Pseudomonas still diverges with the filter applied, so #371 stays open.
    """
    _, _, by_higher = gtdb.collect_rows(mapping, set(), set(), {"pseudomonas"})
    agg = gtdb.resolve_higher(
        "pseudomonas", "NCBITaxon:286", "Pseudomonas", by_higher, "aggregate", exclude_unnamed=True
    )
    deep = gtdb.resolve_higher(
        "pseudomonas", "NCBITaxon:286", "Pseudomonas", by_higher, "deepest", exclude_unnamed=True
    )
    assert agg["gtdb_id"] != deep["gtdb_id"]
