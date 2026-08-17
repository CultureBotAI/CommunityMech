"""The validator's "only abstract available" note is a claim it cannot make (#496).

`validate-references` annotates every failed match with

    (note: only abstract available for PMID:X, full text may contain this excerpt)

That is a statement about the **cache**. What the validator knows is only "I could
not match this snippet". When the full text is cached the note is false, and it
sends the reader to `cache-fulltext` after a gap that does not exist — which cost
a full canary cycle on #259 and happened again on #622.

`scripts/annotate_reference_errors.py` rewrites the note with what the cache
actually supports. These tests pin each branch, because the value of the tool is
entirely in telling the four cases apart:

* no full text cached — the note is true, fetching may help
* a stitched quote (`..`) — legitimate; this validator matches whole substrings
  only, and `evidence_snippet_audit.py` accepts it
* a gap left by the validator stripping `[bracketed]` text (#622) — the quote is
  fine and the tool is not
* genuinely absent — the only case worth a curator's time
"""

from __future__ import annotations

import importlib.util
import pathlib

import pytest

REPO = pathlib.Path(__file__).parent.parent
SCRIPT = REPO / "scripts/annotate_reference_errors.py"


@pytest.fixture()
def annotator(tmp_path, monkeypatch):
    spec = importlib.util.spec_from_file_location("annotate_under_test", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    cache = tmp_path / "references_cache"
    cache.mkdir()
    monkeypatch.setattr(module, "CACHE", cache)
    return module, cache


def _write(cache, name: str, body: str, *, full_text: bool) -> None:
    marker = "\n\n===== OPEN-ACCESS FULL TEXT (Europe PMC PMC1) =====\n\n" if full_text else "\n"
    (cache / name).write_text(f"# header{marker}{body}\n", encoding="utf-8")


def test_abstract_only_keeps_the_original_advice(annotator):
    """The one case where the upstream note is correct."""
    module, cache = annotator
    _write(cache, "PMID_1.txt", "a short abstract", full_text=False)

    note = module.diagnose("PMID:1", "some phrase that is absent")

    assert "only the abstract is cached" in note
    assert "cache-fulltext" in note


def test_a_stitched_quote_is_identified_as_fine(annotator):
    """`..` elision is supported by the audit tool and unmatchable by this one."""
    module, cache = annotator
    _write(
        cache,
        "PMID_2.md",
        "Metatranscriptomics reveals expression of genes for hydrogenases, pyruvate oxidation",
        full_text=True,
    )

    note = module.diagnose("PMID:2", "expression of genes..pyruvate oxidation")

    assert "stitched quote" in note
    assert "nothing to do" in note


def test_a_bracket_gap_is_blamed_on_the_validator(annotator):
    """The #622 case: the validator strips `[NiFe]` and quotes the wreckage back."""
    module, cache = annotator
    _write(
        cache,
        "PMID_3.md",
        "expression of genes for [NiFe]-hydrogenases, pyruvate",
        full_text=True,
    )

    # What the validator reports, with the brackets already removed.
    note = module.diagnose("PMID:3", "expression of genes for  -hydrogenases")

    assert "#622" in note
    assert "the quote is fine and the tool is not" in note


def test_a_genuine_absence_is_still_reported_as_one(annotator):
    """The loosening must not swallow the case the validator exists to find."""
    module, cache = annotator
    _write(cache, "PMID_4.md", "a paper about something else entirely", full_text=True)

    note = module.diagnose("PMID:4", "Yarrowia lipolytica was co-cultured")

    assert "absent from the cached full text" in note
    assert "curator" in note


def test_a_bracket_gap_whose_fragments_are_absent_is_not_excused(annotator):
    """Two spaces alone must not clear a snippet.

    A fabricated quote can contain a double space too. The fragments either side
    of the gap have to be present, and in order, or this stays an absence.
    """
    module, cache = annotator
    _write(cache, "PMID_5.md", "an unrelated body of text", full_text=True)

    note = module.diagnose("PMID:5", "invented phrase  with a gap in it")

    assert "absent from the cached full text" in note


def test_fragments_out_of_order_are_not_excused(annotator):
    """Order matters, or the check degenerates into "these words appear somewhere"."""
    module, cache = annotator
    _write(cache, "PMID_6.md", "beta appears first and then alpha follows later", full_text=True)

    note = module.diagnose("PMID:6", "alpha  beta")

    assert "absent from the cached full text" in note


def test_the_stream_rewrites_only_the_note(annotator, capsys, monkeypatch):
    """Everything else the validator says must pass through untouched."""
    module, cache = annotator
    _write(cache, "PMID_7.md", "a paper about something else entirely", full_text=True)
    line = (
        "  [ERROR] Text part not found as substring: 'absent phrase' "
        "(note: only abstract available for PMID:7, full text may contain this excerpt)\n"
    )
    monkeypatch.setattr(module.sys, "stdin", [line, "  Location: taxonomy[0]\n"])

    module.main()
    out = capsys.readouterr().out

    error_line = next(line for line in out.splitlines() if "[ERROR]" in line)
    assert "only abstract available" not in error_line
    assert "absent from the cached full text" in error_line
    assert "Location: taxonomy[0]" in out, "unrelated lines must survive"
    assert "[ERROR] Text part not found as substring: 'absent phrase'" in out
