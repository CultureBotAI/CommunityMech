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
import io
import pathlib
import sys

import pytest

REPO = pathlib.Path(__file__).parent.parent
SCRIPT = REPO / "scripts/evidence_snippet_audit.py"


@pytest.fixture(scope="module")
def audit():
    spec = importlib.util.spec_from_file_location("evidence_snippet_audit_under_test", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _write_cache(cache: pathlib.Path) -> None:
    cache.mkdir()
    (cache / "PMID_1.md").write_text(
        "---\n"
        "content_type: abstract_only\n"
        "---\n"
        "## Content\n"
        "This source text contains the community quote and the isolate quote. "
        + "Additional real source prose. " * 12,
        encoding="utf-8",
    )


def _write_record(path: pathlib.Path, snippet: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        "id: CommunityMech:000999\n"
        "evidence:\n"
        "- reference: PMID:1\n"
        f"  snippet: {snippet}\n",
        encoding="utf-8",
    )


# --- executable scope ------------------------------------------------------


def test_main_defaults_to_shared_record_files(audit, tmp_path, monkeypatch):
    """The audit's executable path must use both MicrobialCommunity roots."""
    cache = tmp_path / "references_cache"
    _write_cache(cache)
    community = tmp_path / "kb/communities/community.yaml"
    isolate = tmp_path / "data/isolates/isolate.yaml"
    _write_record(community, "community quote")
    _write_record(isolate, "isolate quote")

    monkeypatch.setattr(audit, "CACHE", cache)
    monkeypatch.setattr(audit, "REPO_ROOT", tmp_path)
    monkeypatch.setattr(audit, "record_files", lambda: [community, isolate])

    out = io.StringIO()

    assert audit.main([], out) == 0
    assert "# 2 evidence snippets scanned across 2 files" in out.getvalue()
    assert "MATCH      2" in out.getvalue()


def test_main_accepts_explicit_record_paths(audit, tmp_path, monkeypatch):
    """A targeted audit should not fall back to the whole corpus."""
    cache = tmp_path / "references_cache"
    _write_cache(cache)
    first = tmp_path / "first.yaml"
    second = tmp_path / "second.yaml"
    _write_record(first, "community quote")
    _write_record(second, "isolate quote")

    monkeypatch.setattr(audit, "CACHE", cache)
    monkeypatch.setattr(audit, "REPO_ROOT", tmp_path)
    monkeypatch.setattr(audit, "record_files", lambda: pytest.fail("record_files was called"))

    out = io.StringIO()

    assert audit.main([str(second)], out) == 0
    assert "# 1 evidence snippets scanned across 1 files" in out.getvalue()
    assert str(first) not in out.getvalue()


@pytest.mark.parametrize("heading", ["## Cached Evidence Snippets", "## Content", "## Abstract"])
@pytest.mark.parametrize(
    "content_type", ["selected_excerpts", '"selected_excerpts"', "'SELECTED_EXCERPTS'"]
)
def test_selected_excerpts_are_not_independent_source_text(
    audit, tmp_path, monkeypatch, heading, content_type
):
    cache = tmp_path / "references_cache"
    cache.mkdir()
    (cache / "PMID_1.md").write_text(
        f"---\ncontent_type: {content_type}\n---\n"
        + heading
        + "\n"
        + "A selected phrase without independent retrieved context. " * 12,
        encoding="utf-8",
    )
    record = tmp_path / "record.yaml"
    _write_record(record, "A selected phrase without independent retrieved context.")
    monkeypatch.setattr(audit, "CACHE", cache)

    assert audit.cache_text("PMID:1") == ("", False)
    report = audit.audit_records([record])
    assert report.stats["NOCONTENT"] == 1
    assert report.stats["MATCH"] == 0


def test_selected_excerpts_do_not_hide_independently_retrieved_text(audit, tmp_path, monkeypatch):
    cache = tmp_path / "references_cache"
    cache.mkdir()
    (cache / "PMID_1.md").write_text(
        "---\ncontent_type: selected_excerpts\n---\n## Content\n" + "Excerpt-only phrase. " * 20,
        encoding="utf-8",
    )
    (cache / "PMID_1.txt").write_text("Independent retrieved abstract.", encoding="utf-8")
    monkeypatch.setattr(audit, "CACHE", cache)

    assert audit.cache_text("PMID:1") == ("Independent retrieved abstract.", True)


SELECTED_MARKERS = [
    "===== SELECTED PUBLIC PMC ARTICLE EXCERPTS (PMC13485441) =====",
    "===== SELECTED FULL-TEXT EXCERPTS FROM PMC12816627 =====",
]


@pytest.mark.parametrize("marker", SELECTED_MARKERS)
@pytest.mark.parametrize("suffix", [".txt", ".md"])
def test_appended_selected_excerpts_cannot_certify_a_quote(
    audit, tmp_path, monkeypatch, marker, suffix
):
    cache = tmp_path / "references_cache"
    cache.mkdir()
    abstract = "Independent abstract measuring community productivity. " * 8
    selected = "Curator-only staging phrase without any separately retrieved context."
    prefix = "---\ncontent_type: abstract_only\n---\n## Content\n" if suffix == ".md" else ""
    (cache / ("PMID_1" + suffix)).write_text(
        prefix + abstract + "\n\n" + marker + "\n\n" + selected, encoding="utf-8"
    )
    source_record = tmp_path / "kb/communities/source.yaml"
    selected_record = tmp_path / "data/isolates/selected.yaml"
    _write_record(source_record, "Independent abstract measuring community productivity.")
    _write_record(selected_record, selected)
    monkeypatch.setattr(audit, "CACHE", cache)

    text, trusted = audit.cache_text("PMID:1")
    assert trusted
    assert abstract in text
    assert selected not in text
    assert marker not in text
    report = audit.audit_records([source_record, selected_record])
    assert report.stats["MATCH"] == 1
    assert report.stats["MISMATCH"] == 1


@pytest.mark.parametrize("marker", SELECTED_MARKERS)
@pytest.mark.parametrize("suffix", [".txt", ".md"])
def test_selected_only_cache_is_not_real_content(audit, tmp_path, monkeypatch, marker, suffix):
    cache = tmp_path / "references_cache"
    cache.mkdir()
    (cache / ("PMID_1" + suffix)).write_text(
        marker + "\n" + "Curator-selected phrase without retrieved source context. " * 20,
        encoding="utf-8",
    )
    monkeypatch.setattr(audit, "CACHE", cache)

    assert audit.cache_text("PMID:1") == ("", False)


@pytest.mark.parametrize(
    "real_marker",
    [
        "===== OPEN-ACCESS FULL TEXT (Europe PMC PMC123) =====",
        "Full text (re-fetched from NCBI BioC):",
    ],
)
@pytest.mark.parametrize("suffix", [".txt", ".md"])
def test_selected_section_does_not_hide_later_retrieved_full_text(
    audit, tmp_path, monkeypatch, real_marker, suffix
):
    cache = tmp_path / "references_cache"
    cache.mkdir()
    selected = "Curator-selected staging phrase."
    full_text = "Independent full text describing an experimentally measured result. " * 10
    (cache / ("PMID_1" + suffix)).write_text(
        SELECTED_MARKERS[0] + "\n" + selected + "\n" + real_marker + "\n" + full_text,
        encoding="utf-8",
    )
    record = tmp_path / "kb/communities/source.yaml"
    _write_record(record, "Independent full text describing an experimentally measured result.")
    monkeypatch.setattr(audit, "CACHE", cache)

    text, trusted = audit.cache_text("PMID:1")
    assert trusted
    assert full_text in text
    assert selected not in text
    assert audit.audit_records([record]).stats["MATCH"] == 1


def test_selected_marker_case_crlf_and_multiple_sections(audit, tmp_path, monkeypatch):
    cache = tmp_path / "references_cache"
    cache.mkdir()
    body = (
        "Independent abstract.\r\n"
        "  " + SELECTED_MARKERS[0].lower() + "\r\n"
        "Curated first phrase.\r\n"
        "===== OPEN-ACCESS FULL TEXT (Europe PMC PMC123) =====\r\n"
        "Independent article body.\r\n" + SELECTED_MARKERS[1] + "\r\nCurated second phrase.\r\n"
    )
    (cache / "PMID_1.txt").write_bytes(body.encode())
    monkeypatch.setattr(audit, "CACHE", cache)

    text, trusted = audit.cache_text("PMID:1")
    assert trusted
    assert "Independent abstract." in text
    assert "Independent article body." in text
    assert "Curated" not in text


@pytest.mark.parametrize("text", ["", " \n\t", SELECTED_MARKERS[0]])
def test_empty_or_marker_only_txt_is_not_source_text(audit, tmp_path, monkeypatch, text):
    cache = tmp_path / "references_cache"
    cache.mkdir()
    (cache / "PMID_1.txt").write_text(text, encoding="utf-8")
    monkeypatch.setattr(audit, "CACHE", cache)

    assert audit.cache_text("PMID:1") == ("", False)


@pytest.mark.parametrize(
    "text",
    [
        "Independent abstract about selected excerpts and microbial communities.",
        "Independent abstract.\n===== OPEN-ACCESS FULL TEXT (Europe PMC PMC123) =====\n"
        "Independent article body.",
        "A source sentence mentioning " + SELECTED_MARKERS[0] + " within its prose.",
    ],
)
def test_retrieved_txt_without_curated_sections_is_unchanged(audit, tmp_path, monkeypatch, text):
    cache = tmp_path / "references_cache"
    cache.mkdir()
    (cache / "PMID_1.txt").write_text(text, encoding="utf-8")
    monkeypatch.setattr(audit, "CACHE", cache)

    assert audit.cache_text("PMID:1") == (text, True)


@pytest.mark.parametrize(
    "fake_marker",
    [
        "==== OPEN-ACCESS FULL TEXT (only four delimiter characters)",
        "  ===== OPEN-ACCESS FULL TEXT (indented, not a retrieval marker)",
        "===== open-access full text (not the retrieval marker's case)",
    ],
)
def test_only_established_fulltext_markers_end_selected_sections(
    audit, tmp_path, monkeypatch, fake_marker
):
    cache = tmp_path / "references_cache"
    cache.mkdir()
    (cache / "PMID_1.txt").write_text(
        SELECTED_MARKERS[0] + "\nCurated paragraph.\n" + fake_marker + "\n"
        "Still part of the selected appendix, not independently retrieved text.",
        encoding="utf-8",
    )
    monkeypatch.setattr(audit, "CACHE", cache)
    assert not audit.FULLTEXT_MARKER.search(fake_marker)

    assert audit.cache_text("PMID:1") == ("", False)


def test_write_report_honors_injected_output_for_assembled(audit, capsys):
    report = audit.AuditReport(
        record_count=1,
        stats=audit.Counter({"ASSEMBLED": 1}),
        file_mismatch={},
        file_nocontent={},
        file_rendering={},
        file_assembled={"data/isolates/example.yaml": [("path", "PMID:1", "part, part")]},
        yaml_errors=[],
    )
    out = io.StringIO()

    audit.write_report(report, out, list_assembled=True)

    assert "# ASSEMBLED" in out.getvalue()
    assert "data/isolates/example.yaml" in out.getvalue()
    assert capsys.readouterr().out == ""


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
        [sys.executable, str(SCRIPT)],
        capture_output=True,
        text=True,
        cwd=REPO,
    )
    assert result.returncode == 0, result.stderr
    for bucket in ("MATCH", "RENDERING", "ASSEMBLED", "MISMATCH", "NOCONTENT"):
        assert bucket in result.stdout, f"{bucket} missing from the summary"
