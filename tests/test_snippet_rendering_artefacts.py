"""A snippet that fails only because of subscript spacing is a fixable mistake.

Two records have now shipped with this defect, and both were found by hand:

* `Syntrophobacter_Methanobacterium_Syntrophy` wrote strain designations as
  `MPOB T`, `JF1 T`, `MF T`; the cached text renders the superscript type-strain
  marker closed up — `MPOBT`, `JF1T`, `MFT`.
* `hCom2_Complex_Gut_Microbiome` wrote a chamber gas mix as `CO 2`, `H 2`,
  `N 2`; the cache has `CO2`, `H2`, `N2`.

Neither is a misquotation. The curator read a PDF or a rendered page where the
character *was* a subscript, and the cache flattened it. But
`validate-references` compares substrings, so both records failed it — and
because that validator is deliberately outside `just qc` (#417), nothing said so
until somebody ran it on that file.

**What this gate adds over `validate-references`.** That tool answers "does this
snippet appear?". This one answers "and if not, is it *nearly* there?" — which is
the difference between a curation error worth investigating and a typographic
one worth fixing in ten seconds. It only ever fires on snippets that already
fail, so it cannot mask a real mismatch.

**A caution the earlier version of this check earns.** The one-off sweep that
first established the artefact was "isolated" flattened the snippet but compared
it against the cache file's **raw** text. Any occurrence spanning a line break
was invisible to it, so it reported zero for `hCom2` while the record was
demonstrably broken. Its conclusion happened to be right and its method could
not have shown it. Both sides are flattened here, and
`test_the_gate_can_actually_fire` exists so this file cannot repeat that.
"""

from __future__ import annotations

import pathlib
import re
import sys

import pytest
import yaml

from communitymech.paths import record_files

REPO = pathlib.Path(__file__).parent.parent
COMMUNITIES = REPO / "kb/communities"
CACHE = REPO / "references_cache"

# Superscript markers that a PDF renders raised and a text cache closes up.
# `MPOB T` -> `MPOBT` (type strain); `CO 2` -> `CO2` (formula subscript).
_PATTERNS = (
    re.compile(r"\b([A-Z][A-Za-z0-9\-]{1,12}) T\b"),
    re.compile(r"\b([A-Z][a-z]?[A-Za-z]{0,6}) (\d)\b"),
)


def _cached_text(reference: str) -> str | None:
    """The cache entry for a reference, whitespace-flattened.

    Flattened deliberately: the snippet is stored line-wrapped in YAML and the
    cache is wrapped independently, so comparing either against the other's raw
    form misses anything that straddles a newline in the file that was not
    normalised. That is the bug this file's docstring records.
    """
    stem = (reference or "").replace(":", "_").replace("/", "_")
    for suffix in (".md", ".txt"):
        path = CACHE / f"{stem}{suffix}"
        if path.is_file():
            return " ".join(path.read_text(errors="replace").split())
    return None


def _evidence(document: object):
    """Every (reference, snippet) pair anywhere in a record."""
    if isinstance(document, dict):
        if document.get("snippet") and document.get("reference"):
            yield document["reference"], document["snippet"]
        for value in document.values():
            yield from _evidence(value)
    elif isinstance(document, list):
        for value in document:
            yield from _evidence(value)


def _record_files() -> list[pathlib.Path]:
    """Indirection, so the mutation check below can point the walk at one record.

    It used to monkeypatch a `COMMUNITIES` constant. Sweeping both roots means
    the walk is a call rather than a directory, so the seam moves here (#689).
    """
    return record_files()


def _artefacts() -> list[str]:
    """Snippets that fail only because a subscript was written with a space."""
    found = []
    for path in _record_files():
        document = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        for reference, snippet in _evidence(document):
            if not isinstance(snippet, str):
                continue
            text = _cached_text(reference)
            if text is None:
                continue  # uncached; not this gate's business
            flat = " ".join(snippet.split())
            if flat in text:
                continue  # validates already
            for pattern in _PATTERNS:
                for match in pattern.finditer(flat):
                    closed = match.group(0).replace(" ", "")
                    if match.group(0) not in text and closed in text:
                        found.append(f"{path.name}: {match.group(0)!r} -> {closed!r} ({reference})")
    return sorted(set(found))


@pytest.fixture(scope="module")
def artefacts() -> list[str]:
    return _artefacts()


def test_no_snippet_fails_only_on_subscript_spacing(artefacts):
    """The gate. Both known cases were found by hand; this finds the next one."""
    assert artefacts == [], (
        "these snippets do not match their cached source, and would match if a "
        "space were removed — a rendering artefact from reading a PDF, not a "
        "misquotation. Close the gap up:\n" + "\n".join(f"  {line}" for line in artefacts)
    )


def test_the_gate_can_actually_fire(tmp_path, monkeypatch):
    """Mutation check, because the corpus is clean and silence proves nothing.

    Every assertion above passes if `_cached_text` returns `None` for everything,
    if `_evidence` walks nothing, or if the patterns match nothing — the exact
    failure the one-off version of this sweep had. This drives the same code
    over a record built to contain the defect.
    """
    record = tmp_path / "communities"
    record.mkdir()
    (record / "r.yaml").write_text(
        "id: CommunityMech:000999\n"
        "taxonomy:\n"
        "- taxon_term:\n"
        "    preferred_term: Example organism\n"
        "  evidence:\n"
        "  - reference: PMID:29611893\n"
        "    snippet: Syntrophobacter fumaroxidans MPOB T (DSM 10017) was cultivated\n",
        encoding="utf-8",
    )
    # This module, by identity rather than by import path — `tests/` is not a
    # package, so `import tests.test_...` raises ModuleNotFoundError.
    module = sys.modules[__name__]
    monkeypatch.setattr(module, "_record_files", lambda: sorted(record.glob("*.yaml")))
    found = module._artefacts()
    assert found, "the gate found nothing in a record built to contain the defect"
    assert "MPOB T" in found[0] and "MPOBT" in found[0]


def test_the_walk_reaches_the_corpus(artefacts):
    """Guard: the gate must be looking at real snippets, not an empty set.

    Counted rather than assumed, because `_artefacts` returning `[]` is both the
    success state and what a broken walk produces.
    """
    seen = 0
    cached = 0
    for path in _record_files():
        document = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        for reference, snippet in _evidence(document):
            if isinstance(snippet, str):
                seen += 1
                if _cached_text(reference) is not None:
                    cached += 1
    assert seen > 1000, f"only {seen} snippets walked; the evidence walk is broken"
    assert cached > 200, f"only {cached} snippets have a cached source; the lookup is broken"
