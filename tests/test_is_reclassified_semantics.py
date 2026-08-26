"""`is_reclassified` does not mean what it is named, and nothing said so (#441).

The schema described it as "True when the GTDB **species** name differs from
the NCBITaxon **species** name (a GTDB reclassification/rename)". Both halves
were wrong, measurably:

* **Rank.** 33 of the 154 true blocks are grounded above species — genus,
  family, order, class, phylum.
* **Meaning.** It is a string comparison, at two call sites that do not even
  agree: `bool(sp and ref and sp != ref)` on the species path (121 of the 154)
  and `top != _clean_label(label)` on the genus-and-higher path. Neither can
  know *why* two labels differ.

Partitioning the 154 by why they differ gives 83 — **54%** — that are not
reclassifications under any reading: 40 dropped strain designations, 24
polyphyly suffixes, 11 that are both, 5 GTDB placeholder epithets within the
same genus, 3 nomenclatural endings. The remaining 71 are genuinely different
names, and *those* still mix GTDB reclassifications with NCBI renames and
orthographic variants, so 54% is a floor.

The `Allobosea` -> `Bosea` case that raised #441 is an NCBI rename: NCBI moved
the bacterial genus's label because it was a later homonym of the plant *Bosea*,
and GTDB reclassified nothing. Note the direction — the KB stores
`term.label: Allobosea` with `gtdb_taxon: Bosea`, so NCBI is the *longer* name
here. An earlier draft of this file had it backwards and tested a pair that
does not exist in the corpus.

These tests pin the breakdown so the description cannot go stale again. They
deliberately do **not** assert the flag is correct — narrowing it is #480, a
data migration and a modelling decision. They assert it still means what the
schema now says.
"""

from __future__ import annotations

import glob
import importlib.util
import pathlib
import re

import pytest
import yaml

REPO = pathlib.Path(__file__).parent.parent
GROUND = REPO / "scripts/gtdb_ground.py"
SCHEMA = REPO / "src/communitymech/schema/communitymech.yaml"
RECORD_GLOBS = ("kb/communities/*.yaml", "data/isolates/*.yaml", "kb/taxa/*.yaml")

# GTDB's polyphyly marker. `_[A-Z]+` rather than `_[A-Z]{1,2}`: the corpus
# maxes out at `_AM`, but nothing upstream promises two characters, and a
# looser bound costs no precision here.
_POLYPHYLY = re.compile(r"_[A-Z]+\b")
# GTDB's placeholder epithet for an unnamed species — `sp017744695`.
_PLACEHOLDER = re.compile(r"\bsp\d{6,}$")

# Exact counts, not bands. An earlier draft used ±30 on 154, which let a
# simulated #480 migration flip 15 of the 40 strain-drop blocks with every test
# still green — a tolerance wide enough to hide the change the file exists to
# notice. Exact numbers mean curation updates them deliberately, and the
# failure message says where else the same number is written.
EXPECTED = {
    "different_name": 73,
    # 0 since #480: a dropped strain designation is no longer a difference.
    # The key stays, with its reason, so the bucket cannot silently repopulate.
    "strain_dropped": 0,
    "polyphyly_only": 24,
    "strain_dropped_and_polyphyly": 13,
    "gtdb_placeholder_same_genus": 5,
    "nomenclatural_ending": 3,
}
NOT_A_RECLASSIFICATION = 45
TOTAL_TRUE = 118
ABOVE_SPECIES = 34


def _normalise(name: str) -> str:
    """Strip what is not part of the name: Candidatus, NCBI's <disambiguator>,
    and any GTDB polyphyly suffix.

    Mirrors `gtdb_ground.py`'s `_clean_label`, which anchors the Candidatus
    strip and removes `<...>`. An unanchored `.replace("Candidatus ", "")`
    silently diverges from the tool it is describing.
    """
    name = re.sub(r"^Candidatus\s+", "", name.strip())
    name = re.sub(r"\s*<[^>]*>", "", name)
    return _POLYPHYLY.sub("", name).strip()


def classify(ncbi_label: str, gtdb_taxon: str) -> str:
    """Why these two names differ, as far as the strings can say.

    A partition — every block lands in exactly one bucket, so the counts sum to
    the total. The earlier three-way version was not a partition: 11 blocks are
    a strain drop *and* a polyphyly suffix, and it dropped them into
    "genuinely different", understating the conflation.
    """
    ncbi, gtdb = _normalise(ncbi_label), _normalise(gtdb_taxon)
    has_suffix = _POLYPHYLY.search(gtdb_taxon) is not None

    if ncbi == gtdb:
        return "polyphyly_only" if has_suffix else "identical_after_normalisation"
    if ncbi.startswith(gtdb + " "):
        return "strain_dropped_and_polyphyly" if has_suffix else "strain_dropped"
    if _PLACEHOLDER.search(gtdb):
        # Only a placeholder if the genus is unchanged; `Paenarthrobacter sp.
        # GOM3` -> `Arthrobacter sp018215265` moved genus, which is a real
        # reclassification wearing a placeholder epithet.
        ncbi_words, gtdb_words = ncbi.split(), gtdb.split()
        if ncbi_words and gtdb_words and ncbi_words[0] == gtdb_words[0]:
            return "gtdb_placeholder_same_genus"
        return "different_name"
    if len(ncbi.split()) == 1 and len(gtdb.split()) == 1:

        def stem(value: str) -> str:
            return re.sub(r"(ota|ia|ales|aceae|eae|i)$", "", value)

        if stem(ncbi) == stem(gtdb):
            return "nomenclatural_ending"
    return "different_name"


def _blocks():
    """(ncbi_label, gtdb_taxon, gtdb_id) for every block flagged reclassified.

    Walks the document rather than only `taxonomy[].taxon_term`: the skill
    documents `gtdb_classification` as also attachable to interaction
    participants, and a block landing there would silently stop being counted.
    """
    for pattern in RECORD_GLOBS:
        for path in sorted(glob.glob(str(REPO / pattern))):
            stack = [yaml.safe_load(pathlib.Path(path).read_text()) or {}]
            while stack:
                node = stack.pop()
                if isinstance(node, dict):
                    grounding = node.get("gtdb_classification")
                    if isinstance(grounding, dict) and grounding.get("is_reclassified") is True:
                        label = (node.get("term") or {}).get("label") or ""
                        yield (
                            label,
                            grounding.get("gtdb_taxon") or "",
                            grounding.get("gtdb_id") or "",
                        )
                    stack.extend(node.values())
                elif isinstance(node, list):
                    stack.extend(node)


def _counts() -> dict[str, int]:
    tally: dict[str, int] = {}
    for label, gtdb, _ in _blocks():
        tally[classify(label, gtdb)] = tally.get(classify(label, gtdb), 0) + 1
    return tally


_DRIFT = (
    "If curation moved this legitimately, update this file AND the "
    "is_reclassified description in the schema, which quotes the same numbers, "
    "AND the percentage in .claude/skills/ground-taxa-gtdb/SKILL.md (#441)."
)


def test_the_flag_is_set_on_the_expected_number_of_blocks():
    """Guard: at zero, every breakdown below is vacuous."""
    total = len(list(_blocks()))
    assert total == TOTAL_TRUE, f"blocks with is_reclassified true: {total}. {_DRIFT}"


def test_the_buckets_partition_the_whole_set():
    """The counts must sum, or the percentage below is arithmetic on nothing.

    The bug this catches is real: the first version's buckets overlapped, so
    11 blocks were counted as "genuinely different" while being both a strain
    drop and a polyphyly split.
    """
    tally = _counts()
    assert sum(tally.values()) == TOTAL_TRUE
    assert set(tally) <= set(EXPECTED) | {
        "identical_after_normalisation"
    }, f"classify() produced an unexpected bucket: {sorted(set(tally) - set(EXPECTED))}"


@pytest.mark.parametrize("bucket", sorted(EXPECTED))
def test_each_bucket_holds_what_it_held(bucket: str):
    actual = _counts().get(bucket, 0)
    assert actual == EXPECTED[bucket], f"{bucket}: {actual}, expected {EXPECTED[bucket]}. {_DRIFT}"


def test_the_majority_of_true_values_are_not_reclassifications():
    """The headline claim, computed rather than asserted."""
    tally = _counts()
    not_reclassified = sum(v for k, v in tally.items() if k != "different_name")
    assert not_reclassified == NOT_A_RECLASSIFICATION, (
        f"{not_reclassified} of {TOTAL_TRUE} are not reclassifications, "
        f"expected {NOT_A_RECLASSIFICATION}. {_DRIFT}"
    )
    # No longer a majority, and that is the #480 improvement rather than a
    # regression: removing the 40 strain-drop blocks took the
    # non-reclassification share from 54% to 38%, and the genuinely-different
    # share from 46% to 62%. Pinned as a band so the direction cannot quietly
    # reverse.
    assert 0.3 < not_reclassified / TOTAL_TRUE < 0.45, (
        f"{not_reclassified / TOTAL_TRUE:.0%} of true values are not "
        "reclassifications; #480 left this at 38% and the schema says so"
    )


def test_the_flag_is_not_confined_to_species_rank():
    """The description said "species"; a fifth of the data is not species."""
    above = [
        gtdb_id for _, _, gtdb_id in _blocks() if gtdb_id and not gtdb_id.startswith("GTDB:s__")
    ]
    assert (
        len(above) == ABOVE_SPECIES
    ), f"reclassified blocks above species rank: {len(above)}. {_DRIFT}"


def _description() -> str:
    schema = SCHEMA.read_text()
    start = schema.index("      is_reclassified:")
    end = schema.index("\n        range: boolean", start)
    return schema[start:end]


def test_the_schema_description_still_disclaims_what_the_flag_is_not():
    """Guards the claim, not one literal substring.

    The first version asserted a single sentence was absent, which a one-word
    rewrite defeated — changing `NCBITaxon` to `NCBI` restored the identical
    wrong assertion with all tests green. Requiring the *disclaimers* to be
    present cannot be sidestepped that way: any rewrite that drops them fails,
    however it is worded.
    """
    description = _description()
    for required in ("string comparison", "#480", "#441", "not reclassifications"):
        assert required in description, (
            f"the is_reclassified description no longer contains {required!r}, so "
            f"it has stopped saying what the flag is not (#441)"
        )
    assert not re.search(r"GTDB\s+\*?\*?species\*?\*?\s+name differs", description), (
        "the description has reverted to claiming a species-level GTDB "
        "reclassification, which it is not (#441)"
    )


def test_the_schema_and_this_file_quote_the_same_numbers():
    """Two places hold these counts; nothing else makes them agree."""
    description = _description()
    for number in (TOTAL_TRUE, NOT_A_RECLASSIFICATION, ABOVE_SPECIES):
        assert str(number) in description, (
            f"the schema description no longer quotes {number}; it and this "
            f"file must be updated together (#441)"
        )


@pytest.mark.parametrize(
    ("ncbi", "gtdb", "expected"),
    [
        ("Escherichia coli K-12", "Escherichia coli", "strain_dropped"),
        (
            "Bacteroides thetaiotaomicron VPI-5482",
            "Bacteroides thetaiotaomicron",
            "strain_dropped",
        ),
        ("Bacillota", "Bacillota_A", "polyphyly_only"),
        ("Veillonella parvula", "Veillonella parvula_A", "polyphyly_only"),
        ("Clostridium drakei", "Clostridium_AM drakei", "polyphyly_only"),
        # Both at once — the bucket the first version had no room for.
        ("Buchnera aphidicola BCc", "Buchnera aphidicola_F", "strain_dropped_and_polyphyly"),
        (
            "Clostridium cellulovorans 743B",
            "Clostridium_K cellulovorans",
            "strain_dropped_and_polyphyly",
        ),
        # The direction the KB actually stores: NCBI Allobosea, GTDB Bosea.
        ("Allobosea", "Bosea", "different_name"),
        ("Agrobacterium deltae", "Agrobacterium leguminum", "different_name"),
        ("Dyadobacter sp.", "Dyadobacter sp017744695", "gtdb_placeholder_same_genus"),
        # A placeholder that also moved genus is a real reclassification.
        ("Paenarthrobacter sp. GOM3", "Arthrobacter sp018215265", "different_name"),
        ("Chlorobiota", "Chlorobiia", "nomenclatural_ending"),
        # NCBI's <disambiguator> is not a strain designation; _clean_label
        # strips it, so this must not read as a strain drop.
        ("Bacillus <firmicutes>", "Bacillus", "identical_after_normalisation"),
        # A longer GTDB name is a real difference, not a suffix being removed.
        ("Escherichia coli", "Escherichia coli K-12", "different_name"),
    ],
)
def test_the_classifier_itself(ncbi: str, gtdb: str, expected: str):
    """Every count above is only as good as this function."""
    assert classify(ncbi, gtdb) == expected


def _blocks_with_stored_flag():
    """(ncbi_label, gtdb_taxon, gtdb_id, stored_flag) for EVERY grounded block.

    `_blocks` yields only the ones already flagged true, which is right for
    counting buckets and wrong for checking that the tool would reproduce what
    is stored — a block wrongly left `false` would be invisible to it.
    """
    for pattern in RECORD_GLOBS:
        for path in sorted(glob.glob(str(REPO / pattern))):
            stack = [yaml.safe_load(pathlib.Path(path).read_text()) or {}]
            while stack:
                node = stack.pop()
                if isinstance(node, dict):
                    grounding = node.get("gtdb_classification")
                    if isinstance(grounding, dict) and "is_reclassified" in grounding:
                        yield (
                            (node.get("term") or {}).get("label") or "",
                            grounding.get("gtdb_taxon") or "",
                            grounding.get("gtdb_id") or "",
                            grounding["is_reclassified"],
                        )
                    stack.extend(node.values())
                elif isinstance(node, list):
                    stack.extend(node)


# --------------------------------------------------------------------------
# One definition, and a dropped strain is not one (#480, #482)
# --------------------------------------------------------------------------


@pytest.fixture(scope="module")
def ground():
    spec = importlib.util.spec_from_file_location("gtdb_ground_semantics", GROUND)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.mark.parametrize(
    ("label", "gtdb"),
    [
        ("Escherichia coli K-12", "Escherichia coli"),
        ("Mucispirillum schaedleri ASF457", "Mucispirillum schaedleri"),
        ("Bacteroides thetaiotaomicron VPI-5482", "Bacteroides thetaiotaomicron"),
    ],
)
def test_a_dropped_strain_designation_is_not_a_difference(ground, label, gtdb):
    """#480. GTDB carries no strain designations, so the organism has not moved."""
    assert ground.name_differs(label, gtdb) is False


@pytest.mark.parametrize(
    ("label", "gtdb"),
    [
        ("Agrobacterium deltae", "Agrobacterium leguminum"),
        ("Bacillota", "Bacillota_A"),
        ("Veillonella parvula", "Veillonella parvula_A"),
    ],
)
def test_a_real_name_difference_is_still_reported(ground, label, gtdb):
    assert ground.name_differs(label, gtdb) is True


def test_the_polyphyly_suffix_is_not_swallowed_by_the_strain_rule(ground):
    """Polyphyly survives the strain rule, though NOT for the reason I first wrote.

    I claimed the trailing space in `gtdb + " "` was what protected it. It is
    not, and a mutation removing the space passed every test. The real reason is
    direction: for a dropped strain the NCBI label is the LONGER string
    (`Escherichia coli K-12` starts with `Escherichia coli`), while for polyphyly
    the GTDB name is longer (`Bacillota_A` against `Bacillota`), so no prefix
    test on the label can match it either way.

    The space still earns its place — it stops a GTDB name that is a bare prefix
    of the label, such as `Bacillus` against a label `Bacillusfoo`, from reading
    as a strain drop — but that is a different guarantee, and no data exercises
    it. Recorded so the next person does not trust the wrong mechanism.
    """
    assert ground.name_differs("Bacillota", "Bacillota_A") is True
    assert ground.name_differs("Veillonella parvula", "Veillonella parvula_A") is True
    assert ground.name_differs("Escherichia coli K-12", "Escherichia coli") is False
    # The guarantee the space actually provides, on synthetic input.
    assert ground.name_differs("Bacillusfoo", "Bacillus") is True


@pytest.mark.parametrize(
    ("label", "gtdb"),
    [(None, "Escherichia coli"), ("Escherichia coli", None), ("", "Escherichia coli")],
)
def test_missing_information_is_not_a_difference(ground, label, gtdb):
    """#482's disagreement: the higher-rank path returned True here.

    `top != ""` is true for any non-empty name, so an unparseable label read as
    a name change at genus rank and not at species rank — for the same absence
    of information.
    """
    assert ground.name_differs(label, gtdb) is False


def test_both_call_sites_use_the_shared_function():
    """#482. Two expressions was the defect; one function is the fix.

    Asserted on the source, because a second copy drifts silently — the two
    disagreed for as long as they both existed and nothing noticed.
    """
    source = GROUND.read_text(encoding="utf-8")
    assignments = [line.strip() for line in source.splitlines() if '"is_reclassified":' in line]
    assert len(assignments) >= 2, f"expected both call sites, found {assignments}"
    for line in assignments:
        assert (
            "name_differs(" in line or 'g["is_reclassified"]' in line
        ), f"an is_reclassified assignment computes its own answer: {line!r}"


def test_the_corpus_agrees_with_the_tool():
    """Stored data and tool must agree, or the next --apply reverts the migration.

    #480 names this as the constraint on the migration. Recomputing every stored
    block from its own label and gtdb_taxon must reproduce what is on disk.
    """
    spec = importlib.util.spec_from_file_location("gtdb_ground_corpus", GROUND)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    disagreements = []
    for label, gtdb, _gtdb_id, stored in _blocks_with_stored_flag():
        expected = module.name_differs(label, gtdb)
        if bool(stored) != expected:
            disagreements.append(f"{label!r} -> {gtdb!r}: stored={stored} computed={expected}")

    assert disagreements == [], (
        "stored is_reclassified values disagree with the current rule, so the "
        "next `gtdb_ground.py --apply` would rewrite them (#480):\n"
        + "\n".join(f"  {line}" for line in disagreements[:20])
    )
