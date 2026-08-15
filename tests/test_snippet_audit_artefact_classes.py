"""Two artefact classes the audit used to call fabrication suspects (#596).

The #596 survey of 296 MISMATCH snippets found that 290 were a *retrieval* gap —
a Methods quote checked against an abstract-only cache — and only 6 were
mismatches against a fully cached paper. Of those 6, only one was a genuine
curation defect. The other five were the two shapes gated here.

**1. A typographic symbol spelled out.** `alnum()` strips punctuation but not
letters, so the cache's `(ATCC® 47054)` reduces to `atcc47054` while a record's
`(ATCC(R) 47054)` keeps the R and reduces to `atccr47054`. A faithful quote of
a registered trademark therefore looked like a fabrication.

**2. A snippet assembled from parts.** OMM12 quotes

    "Lactobacillus reuteri I49, Enterococcus faecalis KB1, Blautia coccoides YL58"

which is three non-adjacent rows of a strain table, each present verbatim,
joined with commas.

**What is deliberately NOT rescued.** PET's

    "R. jostii was added to reduce the inhibition caused by terephthalic acid"

welds the opening of one sentence to the tail of another 35 KB away, and no
single part of it appears in the paper. That is a paraphrase presented as a
quote and it must stay a MISMATCH. A matcher loose enough to bless it would be
loose enough to hide the defect this audit exists to find, so
`test_a_stitched_paraphrase_is_still_a_mismatch` pins it.
"""

from __future__ import annotations

import importlib.util
import pathlib

import pytest

REPO = pathlib.Path(__file__).parent.parent
SCRIPT = REPO / "scripts/evidence_snippet_audit.py"


@pytest.fixture(scope="module")
def audit():
    spec = importlib.util.spec_from_file_location("evidence_snippet_audit_under_test", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


# --- 1. typographic symbols ------------------------------------------------


@pytest.mark.parametrize(
    ("cached", "written"),
    [
        ("P. putida KT2440 (ATCC® 47054)", "P. putida KT2440 (ATCC(R) 47054)"),
        ("BioBrick™ assembly", "BioBrick(TM) assembly"),
        ("Somebody© 2019", "Somebody(C) 2019"),
    ],
)
def test_a_spelled_out_symbol_matches_the_symbol(audit, cached, written):
    """The real PET case and its siblings."""
    assert audit.alnum(written) == audit.alnum(cached)


def test_symbols_do_not_collapse_unrelated_text(audit):
    """Guard: the mapping must not make different strings equal.

    `®`→`r` is a character-level equivalence, but a mapping that over-reached
    would silently turn mismatches into matches — the exact direction of error
    this audit must never make.
    """
    assert audit.alnum("ATCC 47054") != audit.alnum("ATCC(R) 47054")
    assert audit.alnum("strain R6") != audit.alnum("strain 6")


def test_greek_transliteration_still_works(audit):
    """The pre-existing behaviour the symbol change sits next to."""
    assert audit.alnum("β-5") == audit.alnum("beta-5")


# --- 2. assembled snippets -------------------------------------------------

_STRAIN_TABLE = (
    "Clostridium innocuum I46 DSM 26113 1 Bacteroides caecimuris I48 DSM 26085 1 "
    "Lactobacillus reuteri I49 DSM 32035 1 Bifidobacterium longum subsp. animalis "
    "YL2 DSM 26074 1 Muribaculum intestinale YL27 DSM 28989 2 Blautia coccoides "
    "YL58 DSM 26115 1 Acutalibacter muris KB18 DSM 26090 2 Enterococcus faecalis "
    "KB1 DSM 32036 1 Subsequently, 100 ul of each subculture was transferred"
)


def test_a_table_flattened_into_prose_is_assembled(audit):
    """The real OMM12 case: three non-adjacent rows joined with commas."""
    snippet = "Lactobacillus reuteri I49, Enterococcus faecalis KB1, Blautia coccoides YL58"

    parts = audit.assembled_parts(snippet, _STRAIN_TABLE)

    assert parts is not None, "the OMM12 table join was not recognised"
    assert len(parts) == 3
    assert audit.norm(snippet) not in audit.norm(_STRAIN_TABLE), (
        "this fixture no longer exercises the case — the snippet matches "
        "literally, so it would never reach the assembled check"
    )


def test_a_stitched_paraphrase_is_still_a_mismatch(audit):
    """The one genuine defect among the six, which must NOT be rescued.

    Both halves exist in the paper, far apart, but neither comma-part of the
    snippet does — so it stays unclassified here and falls through to MISMATCH.
    """
    source = (
        "Besides, the PET monomer TPA inhibited the degradation process. Therefore, "
        "R. jostii was added to the existing consortium to break down TPA, leading to "
        "a three-species microbial consortium with improved degradation efficiency. "
        + "filler " * 200
        + "a three-species microbial consortium was further obtained by adding R. "
        "jostii to reduce the inhibition caused by terephthalic acid (TPA)."
    )
    snippet = "R. jostii was added to reduce the inhibition caused by terephthalic acid"

    assert audit.assembled_parts(snippet, source) is None, (
        "a paraphrase welded from two sentences was classified as merely "
        "reformatted; that is the failure mode this audit exists to catch"
    )


def test_one_unsupported_part_keeps_the_whole_a_mismatch(audit):
    """A snippet is only 'assembled' if EVERY part is real.

    Otherwise a fabricated clause could ride along beside two genuine ones.
    """
    source = "Lactobacillus reuteri I49 DSM 32035 and Enterococcus faecalis KB1 DSM 32036"
    snippet = "Lactobacillus reuteri I49, Enterococcus faecalis KB1, Nonexistent bacterium Q99"

    assert audit.assembled_parts(snippet, source) is None


def test_a_single_part_snippet_is_never_assembled(audit):
    """No comma structure means nothing was assembled; it is just absent."""
    assert audit.assembled_parts("a phrase that is simply not present", "unrelated text") is None
    assert audit.assembled_parts("present text", "some present text here") is None


def test_short_fragments_do_not_qualify_as_parts(audit):
    """Parts under the floor are too short to be evidence of anything.

    Without a floor, "E. coli, pH 7, 37 C" would be 'assembled' against almost
    any microbiology paper.
    """
    source = "we grew E. coli at pH 7 and 37 C in rich medium"
    assert audit.assembled_parts("E. coli, pH 7, 37 C", source) is None


def test_the_corpus_classification_is_stable(audit):
    """The buckets exist and the tool still runs over the real corpus."""
    import subprocess

    result = subprocess.run(
        ["uv", "run", "python", str(SCRIPT)],
        capture_output=True,
        text=True,
        cwd=REPO,
    )
    assert result.returncode == 0, result.stderr
    for bucket in ("MATCH", "RENDERING", "ASSEMBLED", "MISMATCH", "NOCONTENT"):
        assert bucket in result.stdout, f"{bucket} missing from the summary"
