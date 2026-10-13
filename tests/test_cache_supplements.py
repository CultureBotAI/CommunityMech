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
import shutil
import subprocess
import sys
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


def _xlsx(rows: list[list[str]]) -> bytes:
    """Minimal workbook for testing spreadsheet supplements."""
    import openpyxl

    workbook = openpyxl.Workbook()
    worksheet = workbook.active
    worksheet.title = "Table_S1"
    for row in rows:
        worksheet.append(row)

    buffer = io.BytesIO()
    workbook.save(buffer)
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

    table_text, table_note = module._member_text(
        "tables.xlsx", _xlsx([["strain", "species"], ["09-022", "Cyclobacterium sp."]])
    )
    assert "### Table_S1" in table_text
    assert "09-022\nCyclobacterium sp." in table_text
    assert table_note == ""

    plain, _ = module._member_text("readme.txt", b"medium: LB")
    assert "medium: LB" in plain


def test_nested_zip_members_are_extracted(module):
    """Publishers often serve the useful supplement inside a top-level archive."""
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, "w") as archive:
        archive.writestr("methods.docx", _docx(["Grown in L1 medium."]))
        archive.writestr(
            "tables.xlsx",
            _xlsx([["strain", "species"], ["19-037", "Marinovum algicola"]]),
        )
        archive.writestr("figure.jpg", b"\xff\xd8")

    text, note = module._member_text("supplementary.zip", buffer.getvalue())

    assert "Grown in L1 medium." in text
    assert "19-037\nMarinovum algicola" in text
    assert "figure.jpg: SKIPPED (binary/image, no prose)" in note


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


def test_cache_one_strips_trailing_whitespace(module, tmp_path, monkeypatch):
    """Generated caches must pass git's whitespace check."""
    monkeypatch.setattr(module, "CACHE_DIR", tmp_path)
    monkeypatch.setattr(
        module,
        "fetch_supplement",
        lambda ref: ("Method one. \n\nMethod two.\t\n", ["methods.docx: 28 chars"]),
    )

    message = module.cache_one("PMID:1")
    text = (tmp_path / "PMID_1.supplement.md").read_text(encoding="utf-8")

    assert message.startswith("[ok]")
    assert not any(line.endswith((" ", "\t")) for line in text.splitlines())
    assert "Method one.\n\nMethod two." in text


def test_an_existing_cache_is_not_refetched_unless_forced(module, tmp_path, monkeypatch):
    monkeypatch.setattr(module, "CACHE_DIR", tmp_path)
    (tmp_path / "PMID_1.supplement.md").write_text("already here", encoding="utf-8")

    def refuse(ref):
        raise AssertionError("fetched despite an existing cache")

    monkeypatch.setattr(module, "fetch_supplement", refuse)

    assert module.cache_one("PMID:1").startswith("[skip]")


@pytest.mark.parametrize("article_suffixes", [(), (".txt",), (".md",), (".txt", ".md")])
@pytest.mark.parametrize(
    "args",
    [
        ["--append"],
        ["--append", "PMID:1"],
        ["PMID:1", "--append"],
        ["--list", "--append", "PMID:1"],
        ["--candidates", "--append"],
        ["--force", "PMID:1", "--append"],
        ["PMID:1", "PMID:2", "--append"],
    ],
)
def test_append_cli_refuses_before_io(
    module, tmp_path, monkeypatch, capsys, article_suffixes, args
):
    for suffix in article_suffixes:
        (tmp_path / f"PMID_1{suffix}").write_text(f"article {suffix}\n", encoding="utf-8")
    (tmp_path / "PMID_1.supplement.md").write_text("supplement\n", encoding="utf-8")
    before = {path.name: path.read_bytes() for path in tmp_path.iterdir()}
    monkeypatch.setattr(module, "CACHE_DIR", tmp_path)
    monkeypatch.setattr(sys, "argv", [str(SCRIPT), *args])

    def refuse(*args, **kwargs):
        raise AssertionError("--append reached retrieval, writing, or candidate discovery")

    for name in ("cache_one", "fetch_supplement", "candidates", "_get"):
        monkeypatch.setattr(module, name, refuse)

    assert module.main() == 2
    output = capsys.readouterr()
    assert "--append" in output.err and ".supplement.md" in output.err
    assert not output.out
    assert {path.name: path.read_bytes() for path in tmp_path.iterdir()} == before


def test_append_entrypoint_rejects_without_changing_evidence(tmp_path):
    scripts = tmp_path / "scripts"
    scripts.mkdir()
    script = scripts / SCRIPT.name
    shutil.copyfile(SCRIPT, script)
    cache = tmp_path / "references_cache"
    cache.mkdir()
    for filename in ("PMID_1.txt", "PMID_1.md", "PMID_1.supplement.md"):
        (cache / filename).write_text(f"original {filename}\n", encoding="utf-8")
    before = {path.name: path.read_bytes() for path in cache.iterdir()}

    result = subprocess.run(
        [sys.executable, str(script), "PMID:1", "--append"],
        capture_output=True,
        text=True,
        timeout=10,
        check=False,
    )

    assert result.returncode == 2, result.stdout + result.stderr
    assert "--append" in result.stderr and ".supplement.md" in result.stderr
    assert {path.name: path.read_bytes() for path in cache.iterdir()} == before


@pytest.mark.parametrize("list_only", [False, True])
def test_supported_cli_modes_preserve_article_caches(module, tmp_path, monkeypatch, list_only):
    for suffix in (".md", ".txt"):
        (tmp_path / f"PMID_1{suffix}").write_text(f"article {suffix}\n", encoding="utf-8")
    before = {path.name: path.read_bytes() for path in tmp_path.iterdir()}
    monkeypatch.setattr(module, "CACHE_DIR", tmp_path)
    monkeypatch.setattr(module, "fetch_supplement", lambda ref: ("supplement\n", ["methods.txt"]))
    args = [str(SCRIPT), "PMID:1"]
    if list_only:
        args.append("--list")
    monkeypatch.setattr(sys, "argv", args)

    assert module.main() == 0
    for filename, content in before.items():
        assert (tmp_path / filename).read_bytes() == content
    assert (tmp_path / "PMID_1.supplement.md").is_file() is not list_only
