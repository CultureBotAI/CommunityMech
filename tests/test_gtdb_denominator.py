"""The two GTDB majority denominators, and why the default stays `aggregate` (#371).

`NCBI2GTDB.tsv.gz` is an upstream crosswalk in which each row is an independent
NCBI->GTDB assignment carrying its own genome support. `aggregate` (the default)
sums every matched row; `deepest` keeps one row per lineage, at the deepest rank
present — the rule `kg-microbe-paper` settled on for the same shape of problem.

Orthogonal to that choice, the named-species filter (#375) drops `sp.` /
`uncultured` / `bacterium` MAG rows from the count. It is **on by default** as of
#372; `exclude_unnamed=False` restores the older, unfiltered behaviour, which
several tests below still pin because the argument for the default rests on it.

The comparison is the point, not a winner. `scripts/gtdb_denominator_compare.py`
writes all four answers for the 578 distinct KB taxa; 16 vary across the four
scenarios. Counts here are deliberately few and cheap to re-derive — the report
is the source, and quoted numbers rot (this docstring has been wrong twice).

`deepest` is *not* a neutral correction: dropping a lineage's species rows while
keeping its strain rows shifts weight toward lineages that happen to be annotated
at strain rank. Table-wide it discards 801367 of 1837914 genome-supports (43.6%).

Judged against GTDB's own rule — the lineage holding the nomenclatural type keeps
the unsuffixed name — `aggregate` is the better answer on most of the taxa where
they differ. The sharpest is Pseudomonas: `deepest` discards *P. aeruginosa*'s
17191-genome species row in favour of 615 genomes across 289 strain rows, and
lands on `g__Pseudomonas_E` at 0.852 — more confidently wrong than the Acetobacter
case, which is only 0.522.

**The default is not uniformly right.** For Enterococcus it grounds to
`g__Enterococcus_B`, the *E. faecium* clade, purely because faecium is more
sequenced than the type species *E. faecalis* — see #373 and #374. `deepest`
returns AMBIGUOUS there, which is the honest answer.

That third axis — excluding `sp.`/`uncultured` MAG rows (#375) — is what fixes
Acetobacter under *both* denominators, which is why it is now the default. It
does not settle #371: Pseudomonas still diverges with the filter applied.
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
    assert default["majority_fraction"] == 0.695  # filter on by default (#375)


def test_deepest_shifts_weight_toward_strain_annotated_lineages(gtdb, mapping):
    """The case that motivated turning the named-species filter on by default.

    Acetobacter is a cultivated genus; CAG-267 is an uncultivated MAG lineage
    whose support here is entirely strain rows. `deepest` keeps a lineage's strain
    rows and drops its species rows, which hands CAG-267 the majority — the wrong
    answer for the Drosophila gut record that carries this taxon.

    With the filter on (now the default) the MAG rows never enter the count, so
    both denominators reach the cultivated genus and this divergence is gone. The
    second half pins the *unfiltered* behaviour, because that is the observation
    the filter's default rests on: if it stops holding, the argument for the
    default has changed and `scripts/gtdb_denominator_compare.py` wants re-running.
    """
    _, _, by_higher = gtdb.collect_rows(mapping, set(), set(), {"acetobacter"})

    def ground(denominator, **kwargs):
        return gtdb.resolve_higher(
            "acetobacter", "NCBITaxon:434", "Acetobacter", by_higher, denominator, **kwargs
        )

    assert ground("aggregate")["gtdb_id"] == "GTDB:g__Acetobacter"
    assert ground("deepest")["gtdb_id"] == "GTDB:g__Acetobacter", (
        "the filter is on by default, so the MAG lineage must no longer win under "
        "`deepest` — see #375"
    )

    # The pathology the filter suppresses, still present when it is switched off.
    assert ground("deepest", exclude_unnamed=False)["gtdb_id"] == "GTDB:g__CAG-267", (
        "if this no longer holds, re-run scripts/gtdb_denominator_compare.py — the "
        "argument for the current default rests on it"
    )


# ---------------------------------------------------------------------------
# The named-species filter (#375): a third axis, on by default since #372.
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


def test_an_exact_tie_is_ambiguous_not_a_grounding(gtdb, mapping):
    """A 50/50 split is not a majority, so it must not ground (#382).

    `NCBITaxon:106591` (*Ensifer*) sat at 19/38 in two live records, grounded to
    whichever of `g__Ensifer` / `g__Sinorhizobium` the tie-break favoured. The
    tie-break was there to make the answer *reproducible*; it should never have
    been what decided it. Both blocks are withdrawn and the taxon now reports
    AMBIGUOUS with both contenders recorded, which is the honest answer.
    """
    _, _, by_higher = gtdb.collect_rows(mapping, set(), set(), {"ensifer"})
    result = gtdb.resolve_higher("ensifer", "NCBITaxon:106591", "Ensifer", by_higher)

    assert result["ambiguous"] is True, "an exact tie must not produce a grounding"
    assert set(result["gtdb_options"]) >= {"Ensifer", "Sinorhizobium"}


def test_a_bare_majority_above_the_tie_still_grounds(gtdb):
    """The bound is strict, not a wholesale raise of the threshold.

    One genome either side of 50% is the whole difference between a grounding
    and AMBIGUOUS, so both sides are pinned — moving `>` back to `>=` fails the
    test above, and raising the threshold fails this one.
    """

    def row(gtdb_genus, genomes):
        cells = [""] * 20
        cells[2], cells[9], cells[17] = genomes, "Testgenus", gtdb_genus
        cells[10] = "Testgenus namedspecies"
        return cells

    tied = {"testgenus": [row("g__Alpha", "50"), row("g__Beta", "50")]}
    assert gtdb.resolve_higher("testgenus", "NCBITaxon:1", "Testgenus", tied)["ambiguous"]

    won = {"testgenus": [row("g__Alpha", "51"), row("g__Beta", "50")]}
    result = gtdb.resolve_higher("testgenus", "NCBITaxon:1", "Testgenus", won)
    assert result.get("gtdb_taxon") == "g__Alpha"
    assert result["majority_fraction"] == 0.505


def test_ambiguous_options_do_not_depend_on_row_order(gtdb, mapping):
    """The tie-break still has a job: making the option list reproducible.

    Before it, `max()` returned whichever maximum the crosswalk listed first, so
    the contenders a curator reads varied with the file.
    """
    _, _, by_higher = gtdb.collect_rows(mapping, set(), set(), {"ensifer"})
    rows = by_higher["ensifer"]

    forward = gtdb.resolve_higher("ensifer", "NCBITaxon:106591", "Ensifer", {"ensifer": rows})
    reverse = gtdb.resolve_higher(
        "ensifer", "NCBITaxon:106591", "Ensifer", {"ensifer": list(reversed(rows))}
    )

    assert forward["gtdb_options"] == reverse["gtdb_options"]


@pytest.mark.parametrize(
    "species",
    [
        "Wolbachia endosymbiont of Culex quinquefasciatus",  # \b missed the compound
        "Pseudomonas syringae group genomosp. 3",
        "gamma proteobacterium HTCC2080",
        "Firmicutes bacterium CAG:176",
        "Methanococci archaeon",
    ],
)
def test_compound_placeholder_words_are_dropped(gtdb, species):
    """`\\b` anchors the start of a word, so compounds slipped through (#372 review).

    `\\bsymbiont\\b` cannot match `endosymbiont`, and 331 crosswalk rows named that
    way were being counted as though they were binomials.
    """
    assert gtdb.named_species_only([_row(species=species)]) == []


@pytest.mark.parametrize(
    "species",
    [
        "Acetobacterium woodii",  # genus ends in -bacterium; a real binomial
        "Acidipropionibacterium jensenii",
        "Bacillus subtilis subsp. spizizenii",  # `subsp.` is not `sp.`
        "Syntrophotalea acetylenivorans",
        "Candidatus Cibiobacter qucibialis",
    ],
)
def test_real_binomials_survive_the_compound_match(gtdb, species):
    """The fix must not become an over-match.

    Relaxing to `\\w*bacterium` swallowed 1805 binomial-shaped names — every genus
    ending in *-bacterium*. The compound alternations are case-sensitive and
    lowercase-only precisely so a capitalised genus cannot match.
    """
    row = _row(species=species)
    assert gtdb.named_species_only([row]) == [row]


def test_ambiguous_options_are_ordered_deterministically(gtdb):
    """The tie-break fix reached `top` but not the option list a curator reads."""

    def row(gtdb_genus, genomes):
        cells = [""] * 20
        cells[2], cells[9], cells[17] = genomes, "Testgenus", gtdb_genus
        cells[10] = "Testgenus namedspecies"
        return cells

    rows = [row("g__Zeta", "5"), row("g__Alpha", "5"), row("g__Mu", "5")]
    forward = gtdb.resolve_higher("testgenus", "NCBITaxon:1", "Testgenus", {"testgenus": rows})
    reverse = gtdb.resolve_higher(
        "testgenus", "NCBITaxon:1", "Testgenus", {"testgenus": list(reversed(rows))}
    )

    assert forward["ambiguous"] and reverse["ambiguous"], "expected a three-way split"
    assert forward["gtdb_options"] == reverse["gtdb_options"] == ["g__Alpha", "g__Mu", "g__Zeta"]


@pytest.mark.parametrize("bad", ["TYPO", "", None, "Aggregate"])
def test_an_unknown_denominator_always_raises(gtdb, bad):
    """Validation sat inside the rank loop, so it was skipped on every early return."""
    with pytest.raises(ValueError, match="unknown denominator"):
        gtdb.resolve_higher("nothing-matches-this", "NCBITaxon:1", "X", {}, bad)


def test_the_cli_can_reach_both_denominators(gtdb, mapping, capsys):
    """Without flags, `deepest_only` is dead code in production (#372 review).

    `main()` had no `--denominator` / `--include-unnamed`, and both `resolve_target`
    call sites used bare defaults — so the only thing that could reach the
    alternative denominator was the comparison script, which just writes a report.
    """
    assert gtdb.main(["--name", "Acetobacter"]) == 0
    default = capsys.readouterr().out

    assert (
        gtdb.main(["--name", "Acetobacter", "--include-unnamed", "--denominator", "deepest"]) == 0
    )
    alternative = capsys.readouterr().out

    assert "g__Acetobacter" in default
    assert "g__CAG-267" in alternative, "the flags did not reach the grounding"


def test_domain_rank_resolves(gtdb, mapping):
    """`Bacteria` and `Archaea` are the roots of GTDB and must ground (#393).

    `HIGHER_RANKS` stopped at phylum, so neither resolved and 72 KB entries
    recorded "the tool produced no grounding" — which an earlier revision of the
    status enum reported as "GTDB has no counterpart and never will".
    """
    _, _, by_higher = gtdb.collect_rows(mapping, set(), set(), {"bacteria", "archaea"})

    bacteria = gtdb.resolve_higher("bacteria", "NCBITaxon:2", "Bacteria", by_higher)
    archaea = gtdb.resolve_higher("archaea", "NCBITaxon:2157", "Archaea", by_higher)

    assert bacteria["gtdb_id"] == "GTDB:d__Bacteria"
    assert archaea["gtdb_id"] == "GTDB:d__Archaea"
    assert bacteria["majority_fraction"] == 1.0
    assert bacteria["total_genomes"] > 1_000_000, "expected the whole table behind a domain"
    assert not bacteria["is_reclassified"], "GTDB and NCBI agree on the name here"


def test_a_shallower_rank_cannot_pre_empt_a_deeper_one(gtdb):
    """Order matters — demonstrated, not restated.

    The first version of this test resolved *Acetobacter* and asserted it landed
    at `g__`. That passed under every mutant, including deleting domain rank
    entirely, because no real name occupies two rank columns — so the assertion
    could not distinguish the ordering working from the hazard being absent
    (#402 review).

    A synthetic row that carries one name at *both* domain and genus rank does
    distinguish them: with domain last the genus answers, and only then.
    """
    cells = [""] * 20
    cells[2] = "10"
    # Bare names: the crosswalk stores them without a rank prefix and `_curie`
    # adds one. Writing `g__FromGenus` here yields `GTDB:g__g__FromGenus`.
    cells[4], cells[12] = "Ambiguous", "FromDomain"  # NCBI domain, GTDB domain
    cells[9], cells[17] = "Ambiguous", "FromGenus"  # NCBI genus, GTDB genus
    cells[10] = "Ambiguous namedspecies"

    result = gtdb.resolve_higher("ambiguous", "NCBITaxon:1", "Ambiguous", {"ambiguous": [cells]})

    assert (
        result["gtdb_id"] == "GTDB:g__FromGenus"
    ), "a shallower rank answered ahead of a deeper one — HIGHER_RANKS is misordered"
    assert gtdb.HIGHER_RANKS[-1][2] == "d", "domain must remain last"
