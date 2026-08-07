"""`is_reclassified` does not mean what it is named, and nothing said so (#441).

The schema described it as "True when the GTDB **species** name differs from
the NCBITaxon **species** name (a GTDB reclassification/rename)". Both halves
were wrong, and measurably so:

* **Rank.** 33 of the 154 true blocks are grounded above species — genus,
  family, order, class, phylum. A fifth of the data the description did not
  cover.
* **Meaning.** `gtdb_ground.py` computes `top != _clean_label(label)`. That is
  a string comparison. It cannot know *why* two labels differ, so it lumps
  together GTDB reclassifications, NCBI renames, dropped strain designations,
  GTDB polyphyly suffixes, and orthographic variants.

The `Bosea` case that raised #441 is the second kind: NCBI renamed the
bacterial genus because it was a later homonym of the plant *Bosea*. GTDB
reclassified nothing, and the flag still says `true`.

These tests pin the breakdown so the description cannot quietly go stale again,
and so that the scale of the conflation is a number somebody has to update
rather than a claim in prose. They deliberately do **not** assert that the flag
is correct — narrowing it is #480, a data migration and a modelling decision.
What they assert is that it still means what the schema now says it means.
"""

from __future__ import annotations

import glob
import re

import pytest
import yaml

RECORD_GLOBS = ("kb/communities/*.yaml", "data/isolates/*.yaml")

# Tolerances, not exact equality: curation adds records continually, and a test
# that fails on every new grounding is a test people delete. The point is that a
# large shift has to be looked at.
_TOTAL_TRUE = (154, 30)
_ABOVE_SPECIES = (33, 15)
_STRAIN_DROPPED = (40, 15)
_POLYPHYLY = (24, 12)


def _blocks():
    """(ncbi_label, gtdb_taxon, gtdb_id) for every block flagged reclassified."""
    import pathlib

    repo = pathlib.Path(__file__).parent.parent
    for pattern in RECORD_GLOBS:
        for path in sorted(glob.glob(str(repo / pattern))):
            document = yaml.safe_load(pathlib.Path(path).read_text()) or {}
            for entry in document.get("taxonomy") or []:
                term_block = (entry or {}).get("taxon_term") or {}
                grounding = term_block.get("gtdb_classification") or {}
                if grounding.get("is_reclassified") is not True:
                    continue
                label = (term_block.get("term") or {}).get("label") or ""
                yield label, grounding.get("gtdb_taxon") or "", grounding.get("gtdb_id") or ""


def classify(ncbi_label: str, gtdb_taxon: str) -> str:
    """Why these two names differ, as far as the strings can say.

    Mechanical and deliberately conservative — it reports `different_name`
    whenever it cannot prove otherwise, so the two "not a reclassification"
    buckets are lower bounds.
    """
    bare = ncbi_label.strip().replace("Candidatus ", "")
    gtdb = gtdb_taxon.strip()

    # GTDB's polyphyly marker: the same name carrying an _A/_B/_AM suffix,
    # either on the whole name (Bacillota -> Bacillota_A) or on the genus word
    # (Clostridium drakei -> Clostridium_AM drakei).
    if re.fullmatch(re.escape(bare) + r"_[A-Z]{1,2}", gtdb):
        return "polyphyly_suffix"
    ncbi_words, gtdb_words = bare.split(), gtdb.split()
    if (
        len(ncbi_words) >= 2
        and len(gtdb_words) >= 2
        and ncbi_words[1:] == gtdb_words[1:]
        and re.fullmatch(re.escape(ncbi_words[0]) + r"_[A-Z]{1,2}", gtdb_words[0])
    ):
        return "polyphyly_suffix"

    # NCBI names a strain, GTDB names the species it belongs to.
    if bare == gtdb or bare.startswith(gtdb + " "):
        return "strain_suffix_dropped"

    return "different_name"


def _within(actual: int, expected: tuple[int, int], what: str) -> None:
    target, tolerance = expected
    assert abs(actual - target) <= tolerance, (
        f"{what}: {actual}, expected about {target} (±{tolerance}). If curation "
        f"moved this legitimately, update the constant in this file AND the "
        f"is_reclassified description in the schema, which quotes the same "
        f"numbers (#441)."
    )


def test_the_flag_is_set_on_a_meaningful_number_of_blocks():
    """Guard: at zero, every breakdown below is vacuous."""
    total = len(list(_blocks()))
    assert total > 50, f"only {total} blocks are is_reclassified; the breakdown means little"
    _within(total, _TOTAL_TRUE, "blocks with is_reclassified true")


def test_the_flag_is_not_confined_to_species_rank():
    """The description said "species"; a fifth of the data is not species."""
    above = [
        (label, gtdb_id)
        for label, _, gtdb_id in _blocks()
        if gtdb_id and not gtdb_id.startswith("GTDB:s__")
    ]
    assert above, (
        "every reclassified block is now species-rank, so the schema could "
        "legitimately say 'species' again — check before simplifying (#441)"
    )
    _within(len(above), _ABOVE_SPECIES, "reclassified blocks above species rank")


def test_a_dropped_strain_designation_is_not_a_reclassification():
    """`Escherichia coli K-12` -> `Escherichia coli` changes no placement.

    The largest clearly-wrong bucket, and the easiest to narrow mechanically
    (#480).
    """
    dropped = [
        (label, gtdb)
        for label, gtdb, _ in _blocks()
        if classify(label, gtdb) == "strain_suffix_dropped"
    ]
    _within(len(dropped), _STRAIN_DROPPED, "reclassified blocks that only dropped a strain")


def test_a_polyphyly_suffix_is_not_a_rename():
    """`Bacillota` -> `Bacillota_A` is a split marker on the same name."""
    suffixed = [
        (label, gtdb) for label, gtdb, _ in _blocks() if classify(label, gtdb) == "polyphyly_suffix"
    ]
    _within(len(suffixed), _POLYPHYLY, "reclassified blocks differing only by a polyphyly suffix")


def test_the_schema_no_longer_calls_this_a_species_level_reclassification():
    """The description is the artifact this issue was actually about.

    pythongen drops attribute descriptions, so nothing generated carries this
    text and no other test would notice it reverting.
    """
    import pathlib

    schema = (
        pathlib.Path(__file__).parent.parent / "src/communitymech/schema/communitymech.yaml"
    ).read_text()
    start = schema.index("      is_reclassified:")
    description = schema[start : schema.index("range: boolean", start)]

    assert "GTDB species name differs from the NCBITaxon species" not in description, (
        "the is_reclassified description has reverted to claiming a "
        "species-level GTDB reclassification, which it is not (#441)"
    )
    assert "#441" in description


@pytest.mark.parametrize(
    ("ncbi", "gtdb", "expected"),
    [
        ("Escherichia coli K-12", "Escherichia coli", "strain_suffix_dropped"),
        (
            "Bacteroides thetaiotaomicron VPI-5482",
            "Bacteroides thetaiotaomicron",
            "strain_suffix_dropped",
        ),
        ("Bacillota", "Bacillota_A", "polyphyly_suffix"),
        ("Veillonella parvula", "Veillonella parvula_A", "polyphyly_suffix"),
        ("Clostridium drakei", "Clostridium_AM drakei", "polyphyly_suffix"),
        ("Bosea", "Allobosea", "different_name"),
        ("Agrobacterium deltae", "Agrobacterium leguminum", "different_name"),
        # Not a strain drop in the other direction: GTDB naming something longer
        # than NCBI is a real difference, not a suffix being removed.
        ("Escherichia coli", "Escherichia coli K-12", "different_name"),
    ],
)
def test_the_classifier_itself(ncbi: str, gtdb: str, expected: str):
    """The counts above are only as good as this function."""
    assert classify(ncbi, gtdb) == expected
