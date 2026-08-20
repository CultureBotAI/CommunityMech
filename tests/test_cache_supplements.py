"""Supplement caching, tested without the network (#653).

`scripts/cache_supplements.py` exists because open access does not mean the
Methods are accessible: `SynCom_ARC_Peanut_Aflatoxin_Nodulation` cites a fully
open, fully cached 30 KB article whose body says "Co-cultured with A. flavus in
liquid medium" and defers every Method to a supplementary file.

These tests build .docx bytes in memory rather than fetching, so they run in the
blocking gate. The one live check that matters — that the endpoint returns a
usable archive — was a canary, not a test: it wrote 30,878 bytes carrying "LB
medium", "200 rpm" and "CFU" to disk, and a second run skipped.
"""

from __future__ import annotations

import importlib.util
import io
import pathlib
import zipfile

import pytest

REPO = pathlib.Path(__file__).parent.parent
SCRIPT = REPO / "scripts/cache_supplements.py"


@pytest.fixture(scope="module")
def module():
    spec = importlib.util.spec_from_file_location("cache_supplements_under_test", SCRIPT)
    loaded = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(loaded)
    return loaded


def _docx(paragraphs: list[str]) -> bytes:
    """Minimal .docx: a zip whose word/document.xml holds w:p paragraphs."""
    body = "".join(f"<w:p><w:r><w:t>{p}</w:t></w:r></w:p>" for p in paragraphs)
    xml = f'<?xml version="1.0"?><w:document><w:body>{body}</w:body></w:document>'
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, "w") as archive:
        archive.writestr("word/document.xml", xml)
    return buffer.getvalue()


def test_docx_text_reads_paragraphs_and_separates_them(module):
    """Run-together paragraphs would create sentences the source never had.

    That matters more here than usual: snippets are validated by substring
    match, so a fabricated join could make a quote that matches nothing, or --
    worse -- match text spanning two unrelated statements.
    """
    text = module._docx_text(_docx(["Grown in LB medium at 28 C.", "Shaken at 200 rpm."]))

    assert "Grown in LB medium at 28 C." in text
    assert "Shaken at 200 rpm." in text
    assert "28 C.Shaken" not in text, "paragraphs ran together"


def test_a_docx_without_a_document_part_yields_nothing_rather_than_raising(module):
    """A malformed member must not abort a whole archive."""
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, "w") as archive:
        archive.writestr("word/settings.xml", "<x/>")

    text, note = module._member_text("s001.docx", buffer.getvalue())

    assert text == ""
    assert "no word/document.xml" in note


def test_member_types_are_classified_with_a_stated_reason(module):
    """Every skip carries why. A silent skip reads as "the supplement was empty".

    The PDF case is the one that matters: it is deliberately NOT extracted, and
    saying so is the difference between a known gap and a supplement that looks
    like it held no prose.
    """
    assert module._member_text("figure.jpg", b"\xff\xd8")[0] == ""
    assert "binary/image" in module._member_text("figure.jpg", b"\xff\xd8")[1]

    pdf_text, pdf_note = module._member_text("methods.pdf", b"%PDF-1.4")
    assert pdf_text == ""
    assert "PDF not extracted" in pdf_note

    table_text, table_note = module._member_text("tables.xlsx", b"PK\x03\x04")
    assert table_text == ""
    assert "unhandled type .xlsx" in table_note

    plain, _ = module._member_text("readme.txt", b"medium: LB")
    assert "medium: LB" in plain


def test_the_supplement_marker_cannot_be_confused_with_the_full_text_markers(module):
    """The guard that matters most here, given what has gone wrong before.

    Two separate incidents deleted real open-access full text because a
    classifier knew only some markers. Supplement caches sit in the same
    directory, so the marker must not collide with either full-text marker, and
    the filename must not look like an article cache.
    """
    full_text_markers = ("===== OPEN-ACCESS FULL TEXT", "Full text (re-fetched")

    for marker in full_text_markers:
        assert marker not in module.MARKER
        assert module.MARKER not in marker

    path = module.supplement_path("PMID:42099455")
    assert path.name == "PMID_42099455.supplement.md"
    assert path.name != "PMID_42099455.md", "a supplement must not shadow the article cache"


def test_a_404_is_a_verdict_and_a_503_is_not(module, monkeypatch):
    """An outage must not be recorded as "this paper has no supplement" (#586).

    Patched through `monkeypatch` rather than by assignment: the module fixture
    is module-scoped, so a raw assignment would leave every later test in this
    file talking to a stub that raises -- and they would pass, for the wrong
    reason, because they patch `fetch_supplement` and never reach the network.
    """
    import urllib.error

    calls = []

    def raising(code):
        def opener(url, timeout=None):
            calls.append(code)
            raise urllib.error.HTTPError(url, code, "boom", {}, None)

        return opener

    # 404: a real answer, raised as such, without retrying.
    monkeypatch.setattr(module.urllib.request, "urlopen", raising(404))
    with pytest.raises(module._NoSupplementError):
        module._get("http://example.invalid/x", sleep=lambda _: None)
    assert len(calls) == 1, "a 404 should not be retried"

    # 503: transient, so it is retried before giving up.
    calls.clear()
    monkeypatch.setattr(module.urllib.request, "urlopen", raising(503))
    with pytest.raises(urllib.error.HTTPError):
        module._get("http://example.invalid/x", attempts=3, sleep=lambda _: None)
    assert len(calls) == 3, "a 503 should be retried"


def test_nothing_is_written_when_there_is_no_extractable_text(module, tmp_path, monkeypatch):
    """An empty supplement must leave no cache file.

    A zero-byte or header-only cache would later read as "checked, nothing
    there" and stop anyone looking again.
    """
    monkeypatch.setattr(module, "CACHE_DIR", tmp_path)
    monkeypatch.setattr(module, "fetch_supplement", lambda ref: ("", ["fig.jpg: SKIPPED (binary)"]))

    message = module.cache_one("PMID:1")

    assert message.startswith("[none]")
    assert list(tmp_path.iterdir()) == [], "a file was written for an empty supplement"


def test_an_existing_cache_is_not_refetched_unless_forced(module, tmp_path, monkeypatch):
    monkeypatch.setattr(module, "CACHE_DIR", tmp_path)
    (tmp_path / "PMID_1.supplement.md").write_text("already here", encoding="utf-8")

    def refuse(ref):
        raise AssertionError("fetched despite an existing cache")

    monkeypatch.setattr(module, "fetch_supplement", refuse)

    assert module.cache_one("PMID:1").startswith("[skip]")
