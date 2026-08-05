"""A `majority_fraction` must say what it is a fraction *of* (#383).

`0.571` reads identically whether it came from 4 genomes or 4000, and `1.0` can
rest on a single row. Across the KB, **182 groundings rest on fewer than 10
genomes, 177 of them reading `1.0`, and 25 rest on a single genome** — in the
stored block those were indistinguishable from groundings drawn from thousands.
(Two of those three figures moved when #386 aggregated the species path; the
assertions below are ranged rather than exact so the prose is the only thing
that rots, and `test_the_thin_groundings_are_visible` pins the shape.)
The named-species filter (#375) sharpened it, because it shrinks the evidence
without recording that it did.

* ``total_genomes``   — genomes the majority was computed over. On **every**
  grounding, because it is the number #383 actually asked for.
* ``support_genomes`` — genomes behind the chosen taxon. Only on genus-and-higher
  groundings, where this script computes the majority itself.

Rounding is why neither can be inferred: `majority_fraction` is rounded to 3
places, so 4/7 and 4000/7000 both store as 0.571.

**Why species blocks carry no numerator.** Two wrong answers came first. Storing
the crosswalk's `total genomes` column into `support_genomes` labelled the
denominator as the numerator, overstating 74 of 335 species blocks — *P.
aeruginosa* read 17191 against a true ~17019 — and hid behind a worked example
where `majority_fraction: 1.0` makes the two identical. Deriving it as
``round(total * majority)`` is no better: that column carries **two decimal
places**, so at 17191 genomes and 0.99 the true numerator spans ~170 genomes. A
5-digit count from a 2-digit fraction asserts precision the source lacks. So the
species path states the denominator, which it knows exactly, and no numerator.
"""

from __future__ import annotations

import importlib.util
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).parent.parent
FIXTURE_RECORD = REPO / "kb/communities/Lake_Washington_Methane_Oxygen_Methylotroph_Community.yaml"
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
    # The denominator is the only place the `w = 1.0` fallback is observable —
    # without this, changing it to 0.0 passed every test (#385 review).
    assert result["total_genomes"] == 11, "the unparseable row must still count as 1"


def test_the_species_path_reports_the_denominator_but_no_numerator(gtdb, mapping):
    """The crosswalk gives the row total exactly and the share only to 2 places."""
    by_id, by_name, by_higher = gtdb.collect_rows(
        mapping, {"492670"}, {"bacillus velezensis"}, set()
    )
    result = gtdb.resolve_target("492670", "Bacillus velezensis", by_id, by_name, by_higher)

    assert result["gtdb_id"] == "GTDB:s__Bacillus_velezensis"
    # 1163: the rows this grounding was resolved from, which on the id path is
    # the single row carrying taxonID 492670. Widening it to the name group was
    # tried and reverted — the group is keyed on `term.label`, so a synonym
    # changed the answer (#404 review).
    assert result["total_genomes"] == 1163, "the rows the grounding was resolved from"
    assert "support_genomes" not in result, (
        "the species path must publish no numerator — majority_fraction comes "
        "from the crosswalk's 2-decimal column, so any numerator derived from it "
        "would assert precision the source lacks"
    )


def test_every_stored_block_is_coherent(grounded):
    """Delegates to the validator rather than restating its rules (#387).

    These assertions used to be inlined here *and* in
    `test_gtdb_grounding_freshness.py` — and the two copies drifted: this one
    compared `round(support/total, 3) != fraction` exactly, so a block at
    `majority_fraction: 0.6948` passed `just validate-gtdb` and failed `just
    test`. A curator trusting the fast gate would ship a record CI rejects.
    One implementation now, called from three gates (#390 review).
    """
    from communitymech.validators.gtdb_coherence import check_block

    wrong = [
        f"{record}: {name} — [{category}] {message}"
        for record, name, block in grounded
        for category, message in check_block(block)
    ]
    assert not wrong, "incoherent gtdb_classification:\n" + "\n".join(f"  {w}" for w in wrong)


def test_the_kb_carries_the_counts(grounded):
    """Shipping the schema change without the sweep, or half of it, must fail.

    `total_genomes` is the field every grounding gets, so it is the one that
    detects a partial sweep. Only the four blocks the tool cannot recompute may
    lack it: the curated Pelobacter pin (#384), the curated Chlorobium block, and
    the two taxa that are now AMBIGUOUS (#376).
    """
    without = [
        f"{record}: {name}" for record, name, b in grounded if b.get("total_genomes") is None
    ]
    assert len(without) <= 4, (
        f"{len(without)} of {len(grounded)} blocks carry no total_genomes — the KB "
        f"was not fully re-swept after the schema change (#383):\n"
        + "\n".join(f"  {w}" for w in without[:10])
    )
    with_support = [b for _, _, b in grounded if b.get("support_genomes") is not None]
    assert len(with_support) > 250, (
        f"only {len(with_support)} blocks carry support_genomes — the higher-rank "
        f"path should populate it on roughly 307"
    )


def test_the_thin_groundings_are_visible(grounded):
    """The population this issue exists for, now findable by reading the KB.

    These are *visible*, not wrong — a small genus is legitimately small. What
    was wrong is that nothing distinguished them from a grounding drawn from
    thousands. An earlier revision of this docstring claimed every one reads
    `1.0`; 5 do not, and asserting the claim rather than narrating it is what
    caught that.
    """
    thin = [
        (record, name, b["gtdb_id"], b.get("support_genomes"), b["total_genomes"])
        for record, name, b in grounded
        if b.get("total_genomes") is not None and b["total_genomes"] < 10
    ]
    assert len(thin) > 100, (
        f"only {len(thin)} low-evidence groundings — this population is the "
        f"reason #383 exists; has the mapping changed?"
    )
    assert all(t[4] > 0 for t in thin), "a zero denominator would be a division bug"
    assert any(t[1] != 1.0 for t in thin), (
        "every thin grounding reads 1.0 — the earlier narrative said exactly "
        "this and it was false, so it is asserted rather than assumed"
    )
    assert any(t[4] == 1 for t in thin), "expected groundings resting on a single genome"


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


def test_an_emitted_species_block_omits_the_numerator(gtdb, mapping):
    """`_block` must not invent a `support_genomes` the species path cannot know."""
    by_id, by_name, by_higher = gtdb.collect_rows(
        mapping, {"492670"}, {"bacillus velezensis"}, set()
    )
    grounding = gtdb.resolve_target("492670", "Bacillus velezensis", by_id, by_name, by_higher)

    block = gtdb._block(grounding, "test-source")

    assert block["total_genomes"] == 1163
    assert "support_genomes" not in block, (
        "a species block must omit the numerator entirely — writing "
        "`support_genomes: null` puts noise on 336 records and hides from a "
        "`.get()`-based diff, which is how it survived the first sweep"
    )
    assert "support_genomes" not in gtdb.emit_block(grounding, "test-source")


def test_species_counts_match_the_crosswalk(gtdb, mapping):
    """Nothing compared a species-path count to the source, so two bugs hid here.

    `support_genomes` was the crosswalk's *total* column mislabelled as the
    numerator, and the chosen row was whichever the file listed first. Both
    passed a `> 0` assertion. This reads the table directly.
    """
    import gzip

    wanted = {"492670": "Bacillus velezensis", "1423": "Bacillus subtilis"}
    expected = {}
    with gzip.open(mapping, "rt") as handle:
        next(handle)
        for line in handle:
            cells = line.rstrip("\n").split("\t")
            if len(cells) > gtdb.COL_NCBI_SPECIES and cells[0] in wanted:
                best = expected.get(cells[0])
                key = (gtdb._maj(cells), gtdb._genomes(cells))
                if best is None or key > best[0]:
                    expected[cells[0]] = (key, gtdb._genomes(cells))

    for ncbi_id, label in wanted.items():
        by_id, by_name, by_higher = gtdb.collect_rows(mapping, {ncbi_id}, {label.lower()}, set())
        result = gtdb.resolve_target(ncbi_id, label, by_id, by_name, by_higher)
        # Exact, not `>=`. Both fixtures resolve via the NCBI *id*, whose row set
        # is a single row, so #386's aggregation is a no-op here and the count
        # must equal that row. A `>=` passes for any mutant that inflates the
        # total — including dropping the agreeing-rows filter entirely.
        # `>=` since #389: the denominator is sized from every row for this
        # taxon at one depth, so it cannot be smaller than the single best row
        # but is usually larger. Exactness moved to `_species_denominator`'s own
        # tests, which can state the rule rather than a sample of it.
        assert result["total_genomes"] >= expected[ncbi_id][1], (
            f"{label}: stored {result['total_genomes']}, less than the "
            f"{expected[ncbi_id][1]} on the row this id resolves to"
        )


def test_the_chosen_species_row_does_not_depend_on_file_order(gtdb, mapping):
    """The #382 tie-break bug, which reappeared on this path (#385 review).

    `sorted(key=_maj)` is stable, so among rows tied on majority the winner was
    whichever came first: reversing the input moved *Anaerobutyricum hallii* from
    156 genomes to 1, with an unchanged gtdb_id and an unchanged 1.0.
    """
    _, by_name, _ = gtdb.collect_rows(mapping, set(), {"anaerobutyricum hallii"}, set())
    rows = by_name["anaerobutyricum hallii"]
    assert len(rows) > 1, "this taxon no longer has the tied rows the test needs"

    forward = gtdb.resolve_target(
        "", "Anaerobutyricum hallii", {}, {"anaerobutyricum hallii": rows}, {}
    )
    reverse = gtdb.resolve_target(
        "", "Anaerobutyricum hallii", {}, {"anaerobutyricum hallii": list(reversed(rows))}, {}
    )

    assert (
        forward["total_genomes"] == reverse["total_genomes"]
    ), "reversing the crosswalk row order changed the stored evidence count"
    # 157 = 156 + 1, so the aggregation and not a single row produced it.
    #
    # Note what this test can no longer prove. Once the counts became
    # order-invariant sums, `forward == reverse` holds for *any* row ordering,
    # so it no longer guards the #382/#385 tie-break. The sort still decides
    # which GTDB species wins when the rows disagree, and
    # `test_the_sort_picks_the_best_supported_species_from_a_mixed_set` is what
    # actually covers that.
    assert forward["total_genomes"] == 157, (
        f"got {forward['total_genomes']} — expected 156 + 1 aggregated across "
        f"both rows mapping to this GTDB species (#386)"
    )


def test_the_cli_prints_the_counts_and_flags_thin_evidence(gtdb, mapping, capsys):
    """Nothing covered the CLI, so deleting the annotation or the marker passed."""
    assert gtdb.main(["--name", "Pelobacter"]) == 0
    thin = capsys.readouterr().out
    assert "[4/7 genomes]" in thin, "the CLI must say what the fraction is a fraction of"
    assert "THIN" in thin, "a 7-genome grounding must be flagged"

    assert gtdb.main(["--name", "Acetobacter"]) == 0
    thick = capsys.readouterr().out
    assert "[395/395 genomes]" in thick
    assert "THIN" not in thick, "395 genomes is not thin"


def test_a_curated_grounding_is_skipped_by_refresh(gtdb, tmp_path, mapping):
    """The tool must refuse to recompute a block a curator pinned (#384).

    Excluding the whole *file* from the sweep instead — the first attempt — left
    its other taxon ungrounded-by-counts and the record maintainable only by hand.
    """
    assert gtdb.CURATED_GROUNDINGS, "the curated map is empty; nothing is protected"
    record, ncbi_id = next(iter(gtdb.CURATED_GROUNDINGS))

    source = REPO / "kb/communities" / record
    assert source.exists(), f"{record} no longer exists; update CURATED_GROUNDINGS"
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
    rows = gtdb.collect_rows(
        mapping,
        {i.split(":")[1] for i, _ in pairs if i},
        {c.lower() for c in cleaned if " " in c},
        {c.lower() for c in cleaned if " " not in c},
    )
    gtdb.apply_to_community(destination, *rows, "test-source", refresh=True)

    after = yaml.safe_load(destination.read_text())
    pinned = next(
        e["taxon_term"]
        for e in after["taxonomy"]
        if (e["taxon_term"].get("term") or {}).get("id") == ncbi_id
    )
    assert (
        pinned["gtdb_classification"]["gtdb_id"] == "GTDB:g__Syntrophotalea"
    ), "refresh overwrote a curated grounding"
    assert "test-source" not in (
        pinned["gtdb_classification"].get("mapping_source") or ""
    ), "the curated block was rewritten even though its value survived"


def test_the_name_path_aggregates_every_row_for_the_species(gtdb, mapping):
    """#386: one species name spans many crosswalk rows, and all of them count.

    `_ground_species` read a single row and discarded the rest, so
    *Bifidobacterium breve* reported 3 genomes where 25 rows totalling 1593 map
    to `s__Bifidobacterium_breve` — an understatement of ~500x. The name path is
    where this bites, because a species name covers several NCBI strain taxonIDs.
    """
    _, by_name, _ = gtdb.collect_rows(mapping, set(), {"bifidobacterium breve"}, set())
    result = gtdb.resolve_target("", "Bifidobacterium breve", {}, by_name, {})

    assert result["gtdb_id"] == "GTDB:s__Bifidobacterium_breve"
    assert (
        result["total_genomes"] == 1593
    ), f"got {result['total_genomes']} — a single row's count, not the aggregate"


def test_the_species_fraction_is_weighted_by_genomes(gtdb, mapping):
    """A summed denominator needs a fraction computed over the same rows.

    *B. breve*'s rows are 1544 genomes at 0.99 and 49 at 1.0. Keeping the chosen
    row's 1.0 beside a 1593 denominator would assert "1.0 of 1593", which no row
    supports; the genome-weighted mean is 0.99.
    """
    _, by_name, _ = gtdb.collect_rows(mapping, set(), {"bifidobacterium breve"}, set())
    result = gtdb.resolve_target("", "Bifidobacterium breve", {}, by_name, {})

    assert result["majority_fraction"] == 0.99, (
        "the fraction must be the genome-weighted mean over the aggregated rows, "
        "not whichever row happened to be chosen"
    )


def test_aggregation_falls_back_when_no_gtdb_species_is_named(gtdb):
    """A row with an empty GTDB species cell must not aggregate to a zero total.

    `total_genomes: 0` would be a majority over nothing, which the schema now
    rejects outright (#387) — so the fallback has to hold.
    """
    cells = [""] * 20
    cells[2], cells[3], cells[10] = "12", "1.0", "Somegenus somespecies"
    result = gtdb._ground_species([cells], "NCBITaxon:1", "Somegenus somespecies", "ncbi_id")

    assert result["gtdb_id"] is None, "no GTDB species cell means no grounding"
    assert result["total_genomes"] == 12, "must fall back to the chosen row, not 0"


# ---------------------------------------------------------------------------
# What the schema itself rejects, as opposed to what a test catches (#387).
# ---------------------------------------------------------------------------

SCHEMA = REPO / "src/communitymech/schema/communitymech.yaml"


def _validates(tmp_path, mutate) -> bool:
    """Apply `mutate` to one grounded block of a real record; is it still valid?"""
    import subprocess

    source = REPO / "kb/communities/Lake_Washington_Methane_Oxygen_Methylotroph_Community.yaml"
    doc = yaml.safe_load(source.read_text())
    for entry in doc["taxonomy"]:
        block = (entry.get("taxon_term") or {}).get("gtdb_classification")
        if block and "support_genomes" in block:
            mutate(block)
            break
    else:
        pytest.fail("no block with support_genomes in the fixture record")

    path = tmp_path / "mutated.yaml"
    path.write_text(yaml.dump(doc, sort_keys=False, allow_unicode=True))
    return (
        subprocess.run(
            ["uv", "run", "linkml-validate", "-s", str(SCHEMA), str(path)],
            capture_output=True,
            cwd=REPO,
        ).returncode
        == 0
    )


def test_schema_rejects_a_numerator_without_a_denominator(tmp_path):
    """The one coherence constraint the JSON-Schema backend can express."""
    assert not _validates(tmp_path, lambda b: b.pop("total_genomes")), (
        "a block with support_genomes and no total_genomes validated — the "
        "class rule is not being enforced (#387)"
    )


def test_schema_rejects_a_majority_over_zero_genomes(tmp_path):
    assert not _validates(tmp_path, lambda b: b.update(total_genomes=0))
    assert not _validates(tmp_path, lambda b: b.update(support_genomes=0))


def test_schema_still_accepts_an_untouched_block(tmp_path):
    """Guards the two above: if everything failed, they would pass vacuously."""
    assert _validates(tmp_path, lambda b: None), "the unmutated fixture must validate"


def test_schema_cannot_catch_contradictory_counts(tmp_path):
    """Documents the known gap, so it is a decision rather than an oversight.

    `support_genomes <= total_genomes` and agreement with `majority_fraction` are
    cross-field arithmetic, which the JSON-Schema backend cannot express. The
    coherence test in tests/test_gtdb_grounding_freshness.py carries them for the
    committed KB. If this ever starts failing, LinkML gained the capability and
    the constraint should move into the schema (#387).
    """
    assert _validates(tmp_path, lambda b: b.update(support_genomes=99, total_genomes=3)), (
        "the schema now rejects contradictory counts — move the relational "
        "checks out of the tests and into the schema, and delete this test"
    )


def test_aggregation_counts_only_rows_reaching_the_chosen_species(gtdb):
    """Sum the rows that *agree*, not every row in the set.

    Every species-path taxon in the KB happens to have one GTDB species in play,
    so dropping the filter is invisible against real data — a synthetic split is
    the only thing that pins it. Counting the disagreeing rows would inflate the
    denominator with genomes supporting a different species entirely.
    """

    def row(gtdb_species, genomes, majority="1.0"):
        cells = [""] * 20
        cells[2], cells[3] = genomes, majority
        cells[10], cells[18] = "Somegenus somespecies", gtdb_species
        return cells

    chosen = row("Somegenus somespecies", "100")
    other = row("Somegenus otherspecies", "40", majority="0.5")

    result = gtdb._ground_species(
        [chosen, other], "NCBITaxon:1", "Somegenus somespecies", "ncbi_id"
    )

    assert result["gtdb_taxon"] == "Somegenus somespecies"
    assert (
        result["total_genomes"] == 100
    ), "the 40 genomes mapping to a different GTDB species must not be counted"
    assert result["majority_fraction"] == 1.0, "nor may they drag the fraction down"


def test_the_sort_picks_the_best_supported_species_from_a_mixed_set(gtdb):
    """What the row sort still decides, now that the counts are order-invariant.

    `sp` is read off `top`, so with rows disagreeing on GTDB species the sort
    chooses the winner — and `agreeing` then narrows to it. Aggregation made
    `total_genomes` a sum, which is order-independent by construction, so
    `test_the_chosen_species_row_does_not_depend_on_file_order` stopped guarding
    the #382/#385 tie-break. Reverting to the buggy stable `sorted(key=_maj)`
    must fail here.
    """

    def row(gtdb_species, genomes, majority="1.0"):
        cells = [""] * 20
        cells[2], cells[3] = genomes, majority
        cells[10], cells[18] = "Somegenus somespecies", gtdb_species
        return cells

    # Both species tie on majority, so only the genome count separates them —
    # exactly the case a stable sort decides by file order.
    weak = row("Somegenus weakspecies", "2")
    strong = row("Somegenus strongspecies", "500")

    for ordering in ([weak, strong], [strong, weak]):
        result = gtdb._ground_species(ordering, "NCBITaxon:1", "Somegenus somespecies", "ncbi_id")
        assert result["gtdb_taxon"] == "Somegenus strongspecies", (
            f"picked the 2-genome species over the 500-genome one for ordering "
            f"{[r[18] for r in ordering]} — the tie-break fell through to row order"
        )
        assert result["total_genomes"] == 500


def test_the_schema_rule_does_not_catch_an_explicit_null(tmp_path):
    """A known hole, asserted so it cannot be mistaken for coverage (#388 review).

    `value_presence: PRESENT` compiles to JSON-Schema `required`, which a null
    satisfies, and `minimum_value` does not apply to null. So the rule catches a
    *missing* `total_genomes`, not `total_genomes: null`. `_block()` never emits
    nulls and the coherence test uses `.get()`, so the KB is covered — but the
    schema alone is weaker than its description suggests. If this ever starts
    failing, LinkML tightened and the note in the schema should go.
    """
    assert _validates(tmp_path, lambda b: b.update(total_genomes=None)), (
        "the schema now rejects an explicit null — update the rule's comment and "
        "delete this test"
    )


def test_the_coherence_gate_does_catch_that_null(gtdb):
    """What actually protects the KB from the hole above."""
    import importlib.util

    spec = importlib.util.spec_from_file_location(
        "freshness", REPO / "tests/test_gtdb_grounding_freshness.py"
    )
    freshness = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(freshness)

    bad = [("rec.yaml", "Some taxon", None, {"support_genomes": 5, "total_genomes": None})]
    # `total_genomes` is present-but-null, so this is `null_count`, not
    # `numerator_without_denominator` — the key exists. Matching on the wrong
    # category is how a cross-file coupling passes for the wrong reason.
    with pytest.raises(AssertionError, match="null_count"):
        freshness.test_grounding_is_internally_coherent(bad)


def test_the_weighted_fraction_keeps_three_decimal_places(gtdb):
    """The precision the rest of the block is stored at.

    Every real weighted mean in the KB happens to round identically at 2 and 3
    places (B. breve is 0.99031), so nothing distinguished them. 3 genomes at 1.0
    and 1 at 0.85 gives 0.9625 — 0.963 at three places, 0.96 at two — and
    `test_every_stored_fraction_agrees_with_its_counts` compares against
    `round(support/total, 3)`, so the two must not drift apart.
    """

    def row(genomes, majority):
        cells = [""] * 20
        cells[2], cells[3] = genomes, majority
        cells[10], cells[18] = "Somegenus somespecies", "Somegenus somespecies"
        return cells

    result = gtdb._ground_species(
        [row("3", "1.0"), row("1", "0.85")], "NCBITaxon:1", "Somegenus somespecies", "ncbi_id"
    )

    assert result["total_genomes"] == 4
    assert result["majority_fraction"] == 0.963, "the mean must keep three decimal places"


# ---------------------------------------------------------------------------
# The species denominator: one depth, widest evidence, path-independent (#389).
# ---------------------------------------------------------------------------


def _depth_row(genomes, majority="1.0", strain=""):
    """A crosswalk row for one GTDB species, at species or strain depth."""
    cells = [""] * 20
    cells[2], cells[3] = genomes, majority
    cells[10], cells[11], cells[18] = "Somegenus somespecies", strain, "Somegenus somespecies"
    return cells


def test_a_species_row_is_never_summed_with_its_strain_rows(gtdb):
    """The double-count #389 had to avoid.

    A crosswalk row is one NCBI taxonID's assignment, so a species-rank row and
    its strain rows describe overlapping genome sets. *E. coli* has a
    166397-genome species row plus 2609 strain rows; adding them gives 184367
    for a population no larger than the species.
    """
    rows = [_depth_row("100"), _depth_row("7", strain="K-12"), _depth_row("3", strain="B")]

    total, _ = gtdb._species_denominator(rows)

    assert total == 100, "the species row was summed with its own strains"


def test_the_larger_depth_wins(gtdb):
    """Not `deepest_only`'s rule, which would discard the largest measurement.

    Keeping strains over the species row would report 17969 for *E. coli*
    against its 166397-genome species row. Containment does not hold in this
    table, so the larger depth is the best supported lower bound (#371).
    """
    strain_heavy = [_depth_row("10"), _depth_row("60", strain="A"), _depth_row("50", strain="B")]
    assert gtdb._species_denominator(strain_heavy)[0] == 110

    species_heavy = [_depth_row("500"), _depth_row("6", strain="A")]
    assert gtdb._species_denominator(species_heavy)[0] == 500


def test_the_fraction_is_weighted_within_the_winning_depth(gtdb):
    """Mixing depths in the mean would describe a population that was not counted."""
    # The strain row must be the *smaller* depth, or it legitimately wins and
    # the test measures the wrong branch — which is how this was first written.
    rows = [
        _depth_row("300", majority="1.0"),
        _depth_row("100", majority="0.9"),
        _depth_row("50", majority="0.1", strain="ignored"),
    ]

    total, fraction = gtdb._species_denominator(rows)

    assert total == 400
    assert fraction == 0.975, "the strain row's 0.1 must not drag the species-depth mean"


def test_a_denominator_is_not_a_function_of_the_label(gtdb, mapping):
    """`term.label` is curator prose; the denominator must not follow it.

    #389 widened the id path to include every row sharing the label, which made
    `NCBITaxon:33038` report 2945 genomes as "Mediterraneibacter gnavus" and 311
    under its NCBI synonym "Ruminococcus gnavus" — a 9.5x swing from a rename.
    The KB already carries one id under two labels (`NCBITaxon:408`). Reverted;
    an id is stable, a label is not (#404 review).
    """
    answers = set()
    for label in ("Mediterraneibacter gnavus", "Ruminococcus gnavus"):
        by_id, by_name, by_higher = gtdb.collect_rows(mapping, {"33038"}, {label.lower()}, set())
        result = gtdb.resolve_target("33038", label, by_id, by_name, by_higher)
        answers.add((result["total_genomes"], result["majority_fraction"]))

    assert len(answers) == 1, f"the label changed the denominator: {sorted(answers)}"


def test_every_kb_taxon_reports_one_denominator(grounded):
    """KB-level: the same NCBI taxon must never carry two different totals.

    Different NCBI taxa mapping to one GTDB species legitimately differ —
    `NCBITaxon:562` (*E. coli*) sits at 166398 while its K-12 substrains report
    37, 50 and 4 — because the denominator is scoped to the taxon grounded, not
    to the GTDB species. What must not vary is one taxon against itself.
    """
    from collections import defaultdict

    by_taxon = defaultdict(set)
    for _record, _name, block in grounded:
        if block.get("support_genomes") is None and block.get("total_genomes"):
            by_taxon[block.get("ncbi_source_id")].add(block["total_genomes"])

    inconsistent = {tid: sorted(v) for tid, v in by_taxon.items() if len(v) > 1}
    assert not inconsistent, f"one taxon, several denominators: {inconsistent}"


def test_every_grounding_carries_a_queryable_rank(grounded):
    """The rank must be readable from `gtdb_id` (#403).

    #403 proposed a rank field so filtering would be a query rather than a
    substring match on `mapping_source`. It already is one — but only because
    `gtdb_id` is *required*; a LinkML pattern says nothing when the key is
    absent, so before #414 a block could omit it and pass every gate while the
    documented filter raised KeyError.

    Note what this does not check. `mapping_source`'s rank prose is formatted
    from the same variable as the CURIE in the same dict literal, so "they
    agree" is a property of one f-string, not a cross-check — and 336 of 715
    blocks have no such prose at all. Comparing them was theatre; the useful
    assertion is that the prefix is there and well-formed.
    """
    import re

    missing = [
        f"{record}: {name} — {block.get('gtdb_id')!r}"
        for record, name, block in grounded
        if not re.match(r"GTDB:[cdfgops]__", block.get("gtdb_id") or "")
    ]
    assert not missing, "gtdb_id without a rank prefix:\n" + "\n".join(missing[:10])


def test_the_schema_requires_a_rank_prefix_and_the_field_itself():
    """Both halves, because the pattern alone guards nothing.

    An earlier version asserted only that the pattern contained `__`, which let
    `^GTDB:[cdfgops]?__.+` — the most natural loosening, making the rank
    optional — pass green (#414 review). This drives the real validator over
    concrete CURIEs instead of inspecting the regex.
    """
    import subprocess
    import tempfile

    schema = REPO / "src/communitymech/schema/communitymech.yaml"

    def accepts(block: dict) -> bool:
        document = yaml.safe_load(FIXTURE_RECORD.read_text())
        for entry in document["taxonomy"]:
            term = entry.get("taxon_term") or {}
            if term.get("gtdb_classification"):
                term["gtdb_classification"] = block
                break
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "probe.yaml"
            path.write_text(yaml.dump(document, sort_keys=False, allow_unicode=True))
            return (
                subprocess.run(
                    ["uv", "run", "linkml-validate", "-s", str(schema), str(path)],
                    capture_output=True,
                    cwd=REPO,
                ).returncode
                == 0
            )

    good = {"gtdb_id": "GTDB:d__Bacteria", "gtdb_taxon": "Bacteria"}
    assert accepts(good), "a well-formed block must validate"

    assert not accepts({"gtdb_taxon": "Bacteria"}), "a block with no gtdb_id validated"
    assert not accepts({**good, "gtdb_id": "GTDB:Bacteria"}), "an un-ranked CURIE validated"
    assert not accepts({**good, "gtdb_id": "GTDB:k__Bacteria"}), "an unknown rank validated"
    # The one string `^GTDB:[cdfgops]?__.+` accepts and the real pattern does
    # not. Without it that mutant — the most natural loosening, making the rank
    # character optional — passes every probe above and survives green.
    assert not accepts({**good, "gtdb_id": "GTDB:__Bacteria"}), "an empty rank validated"


def test_the_domain_groundings_are_filterable(grounded):
    """The population #403 is about, and the query that removes it."""
    domain = [b for _, _, b in grounded if b["gtdb_id"].startswith("GTDB:d__")]

    assert {b["gtdb_id"] for b in domain} == {"GTDB:d__Bacteria", "GTDB:d__Archaea"}
    # Tight both ways: `> 50` let a regression lose 21 of the 72 and still pass.
    assert 65 <= len(domain) <= 80, (
        f"{len(domain)} domain groundings; SKILL.md's rank table says 72 and is "
        f"the thing that goes stale"
    )


def test_domain_is_not_the_whole_tautological_population(grounded):
    """The filter SKILL.md documents is under-inclusive, and says so.

    64 higher-rank groundings carry a GTDB name identical to the NCBI name at
    the same rank — `Actinomycetota` -> `p__Actinomycetota` — and say exactly as
    little as `d__Bacteria`. Pinned so the docs' caveat cannot quietly become
    wrong (#414 review).
    """
    uninformative = [
        b
        for _, _, b in grounded
        if not b["gtdb_id"].startswith(("GTDB:s__", "GTDB:g__", "GTDB:d__"))
        and not b.get("is_reclassified")
    ]

    assert len(uninformative) > 40, (
        "the same-name higher-rank population vanished; SKILL.md's caveat about "
        "d__ not being the whole story may now be wrong"
    )
