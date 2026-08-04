"""A `majority_fraction` must say what it is a fraction *of* (#383).

`0.571` reads identically whether it came from 4 genomes or 4000, and `1.0` can
rest on a single row. Across the KB, **197 groundings rest on fewer than 10
genomes, 192 of them reading `1.0`, and 25 rest on a single genome** — in the
stored block those were indistinguishable from groundings drawn from thousands.
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
    assert result["total_genomes"] == 1163, "the chosen row's own genome count"
    assert "support_genomes" not in result, (
        "the species path must publish no numerator — majority_fraction comes "
        "from the crosswalk's 2-decimal column, so any numerator derived from it "
        "would assert precision the source lacks"
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
        assert result["total_genomes"] == expected[ncbi_id][1], (
            f"{label}: stored {result['total_genomes']} but the best crosswalk row "
            f"carries {expected[ncbi_id][1]} genomes"
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
    # Deterministic is not enough — it must be the *best-supported* row. Both
    # rows here sit at majority 1.0, carrying 156 genomes and 1, so consistently
    # picking either end would satisfy the assertion above.
    assert forward["total_genomes"] == 156, (
        f"chose a {forward['total_genomes']}-genome row over the 156-genome one; "
        f"a tie must break toward the better-supported row"
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
