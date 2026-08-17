"""Stem matching must be loose enough to see a rank change and no looser (#605).

`scripts/taxon_absent_from_source.py` asks whether a taxon appears in its cited
source. Whole-word matching answered "no" for cases that are plainly "yes":

* the KB says the phylum `Thermotogota`, the paper names the genus *Thermotoga*
* the KB says `Ignavibacteriota`, the paper writes "Ignavibacteria"
* the KB says `Desulfobacterales`, the paper writes "Desulfobacter"

So the check truncates rank suffixes and matches the stem as a **prefix**. That
is a deliberate loosening, and loosening a defect-finder is how a defect-finder
stops finding defects — the pattern this file exists to pin.

**The property that makes it safe is the leading word boundary.**
`\\bThiobacill` does not match "Acidithiobacillus", which matters concretely:
`PGM_Spent_Catalyst_Bioleaching` claims *Thiobacillus thioparus* on papers that
name *Acidithiobacillus* instead, and the record lists those Acidithiobacillus
species separately. If the stem matched inside a longer genus, that real defect
would be silently rescued.

These are pure string tests — no ontology, no network — so they run in the
blocking gate even though the script they cover cannot.
"""

from __future__ import annotations

import importlib.util
import pathlib

import pytest

REPO = pathlib.Path(__file__).parent.parent
SCRIPT = REPO / "scripts/taxon_absent_from_source.py"


@pytest.fixture(scope="module")
def check():
    spec = importlib.util.spec_from_file_location("taxon_absent_under_test", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _matches(check, name: str, text: str) -> bool:
    """Drives the script's OWN matcher.

    An earlier version of this helper rebuilt the regex itself. That made every
    assertion below pass while the script's leading word boundary was removed —
    the safety property they exist to protect was untested by the tests
    protecting it.
    """
    return check.mentions(name, text)


@pytest.mark.parametrize(
    ("name", "text"),
    [
        # The rank changes this loosening exists for, all from the real corpus.
        ("Thermotogota", "the phylum Thermotoga was abundant"),
        ("Ignavibacteriota", "Ignavibacteria dominated the anode biofilm"),
        ("Desulfobacterales", "Desulfobacter species were enriched"),
        ("Desulfobacteraceae", "members of Desulfobacter"),
        # And the reverse direction: a paper using the newer, longer name.
        ("Thermotoga", "Thermotogota comprised 4% of reads"),
    ],
)
def test_a_rank_change_still_counts_as_present(check, name, text):
    assert _matches(check, name, text)


@pytest.mark.parametrize(
    ("name", "text", "why"),
    [
        (
            "Thiobacillus",
            "we used Acidithiobacillus thiooxidans and A. ferrooxidans",
            "Acidithiobacillus is a DIFFERENT genus that contains the string "
            "'thiobacillus'; PGM_Spent_Catalyst_Bioleaching's real defect depends "
            "on this not matching",
        ),
        (
            "Yarrowia",
            "co-cultured with Saccharomyces cerevisiae W303",
            "Synechococcus_Yarrowia_SPC's real defect depends on this not matching",
        ),
        (
            "Bacillota",
            "Lactobacillus and Streptococcus were present",
            "the boundary must hold inside a compound genus: 'Lactobacillus' "
            "contains 'bacill' but not at a word start",
        ),
    ],
)
def test_these_must_not_match(check, name, text, why):
    assert not _matches(check, name, text), why


def test_a_stem_is_never_shortened_below_the_floor(check):
    """Short names keep their suffix rather than becoming a promiscuous prefix."""
    assert check.stem_of("Vibrio") == "Vibrio"
    for name in ("Thermotogota", "Ignavibacteriota", "Desulfobacterales"):
        assert len(check.stem_of(name)) >= 6


def test_a_phylum_stem_matching_a_member_genus_is_correct(check):
    """`Bacillota` stems to `Bacill`, which matches *Bacillus*. That is right.

    Written down because it looks like over-matching and is not: *Bacillus* is a
    member of the phylum Bacillota, so a paper naming the genus does support a
    claim about the phylum — the same logic as Thermotoga supporting
    Thermotogota. The boundary is what keeps it honest; see the "must not match"
    cases above for `Lactobacillus`.
    """
    assert _matches(check, "Bacillota", "Bacillus subtilis was included")
    assert not _matches(check, "Bacillota", "only Lactobacillus was found")


def test_promiscuous_stems_are_stopped_before_stemming_not_by_it(check):
    """ "Bacteria" WOULD stem to "Bacter" and match half the corpus.

    It never gets the chance: `search_keys` drops it as uninformative first. The
    protection is the vocabulary filter, not the length floor, and conflating
    the two would leave a real gap if either changed.
    """
    assert check.stem_of("Bacteria") == "Bacter"
    assert check.search_keys("Bacteria") == []


def test_uninformative_names_are_dropped_entirely(check):
    """Including the obsolete genus 'Bacterium', which survives as a synonym.

    *Thiobacillus thioparus* carries "Bacterium thioparum" in NCBITaxon, and
    "bacterium" appears in essentially every microbiology paper — it rescued a
    known-bad claim as if it were a renaming.
    """
    for name in ("Bacteria", "bacterium", "Archaea", "Fungi"):
        assert check.search_keys(name, require_capital=False) == []


def test_lowercase_synonyms_survive(check):
    """NCBITaxon lower-cases many synonyms; requiring a capital discarded them.

    `Bacillota` carries "firmicutes" and `Cyanobacteriota` carries
    "cyanobacteria". Requiring an initial capital reported twenty phylum
    renamings as unsupported claims.
    """
    assert check.search_keys("firmicutes", require_capital=False) == ["firmicutes"]
    assert check.search_keys("cyanobacteria", require_capital=False) == ["cyanobacteria"]
    # Still rejected for a PRIMARY label, where a proper name is expected.
    assert check.search_keys("firmicutes") == []


def test_candidatus_prefix_is_skipped(check):
    """ "Candidatus" is a status marker, not a genus; 53 KB taxa carry it."""
    assert check.search_keys("Candidatus Methanogaster") == ["Methanogaster"]
    assert check.search_keys("Candidatus Brocadia") == ["Brocadia"]
