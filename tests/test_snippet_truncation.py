"""Catch evidence snippets truncated at a genus abbreviation (#299).

Snippet validation checks only that the text is a substring of the cached
reference. A fragment therefore validates exactly as well as a full clause, and
two mechanical truncations slip through unnoticed:

    snippet: The main products from C.          # + " ljungdahlii fermentation…"
    snippet: benzoate-fermenting bacterium S.   # + " gentianae is approximately…"

Both come from splitting sentences naively: an abbreviated genus reads as a full
stop, so the snippet stops at exactly the word it existed to identify.

**Why there is no minimum-length rule here.** The obvious guard is a length
floor, and the data says it would be wrong. Of 5106 snippets, 627 are under 40
characters and the shortest are legitimate — ``pH 6.8``, ``150 g/L``,
``glucose 10 g/L``, ``Firmicutes``. Those are precisely the right evidence for a
pH, a concentration, or a taxon, and a floor would bury a real signal under
hundreds of false positives.

The signature used instead is specific and self-verifying: the snippet ends in a
single capital letter followed by a period, **and the cache continues with a
lowercase word**. That second half is what makes it precise — it distinguishes a
truncated genus from a sentence that legitimately ends in an abbreviation or a
unit. Measured over the whole KB it flagged 4 snippets, all genuine, and zero
false positives; ``27 °C.`` and ``1.0 ppm F.`` are correctly ignored because no
lowercase continuation follows.

A second signature — a snippet stopping immediately before a non-ASCII character
present in the cache, which is how the U+2010 HYPHEN in isolate codes truncates
things — is **not** gated here. It fired once across the KB, on a snippet that
ends a complete clause before an em-dash, so it is currently all false positive.
It is documented in #299 in case isolate-code records make it worth revisiting.
"""

from __future__ import annotations

import re
from pathlib import Path

import pytest
import yaml

COMMUNITIES = Path(__file__).parent.parent / "kb/communities"
CACHE = Path(__file__).parent.parent / "references_cache"

# Snippet ends with a single capital + period, e.g. "… from C." — the shape an
# abbreviated genus leaves behind when a sentence splitter treats it as a stop.
_ABBREV_TAIL = re.compile(r"(?:^|\s)[A-Z]\.$")
# The cache continues with a lowercase word, i.e. the species epithet.
_LOWER_CONT = re.compile(r"^\s+[a-z]")


def _cache_texts(reference: str) -> list[str]:
    """Return every cached text for a reference, normalised to single spaces.

    A reference often has more than one cache file — 63 of them carry both a
    `.md` and a `.txt`, and per #265 those differ in substance: the `.md` usually
    holds open-access full text while the `.txt` may be only the abstract.
    Taking the first glob match would make this check filesystem-order dependent;
    measured, 71 snippets are findable in one variant and not the other (#306).

    All of them are searched instead. They are deliberately *not* concatenated:
    this check inspects what follows the snippet, and joining two files would
    manufacture a continuation across the boundary. `.json` files are CrossRef
    metadata rather than prose and are excluded.
    """
    key = reference.replace("PMID:", "PMID_").replace("doi:", "DOI_").replace("/", "_")
    return [
        " ".join(candidate.read_text(errors="replace").split())
        for candidate in sorted(CACHE.glob(key + ".*"))
        if candidate.suffix != ".json"
    ]


def _evidence_items(node):
    """Yield every evidence-shaped mapping anywhere in a record."""
    if isinstance(node, dict):
        if "snippet" in node and "reference" in node:
            yield node
        for value in node.values():
            yield from _evidence_items(value)
    elif isinstance(node, list):
        for value in node:
            yield from _evidence_items(value)


def _community_files() -> list[Path]:
    return sorted(COMMUNITIES.glob("*.yaml"))


def test_there_are_community_files_to_check():
    """Guard against the glob matching nothing and the suite passing vacuously."""
    assert len(_community_files()) > 100


@pytest.mark.parametrize("path", _community_files(), ids=lambda p: p.name)
def test_no_snippet_truncated_at_a_genus_abbreviation(path: Path):
    """No snippet may stop at an abbreviated genus that the cache continues.

    Snippets absent from their cache are skipped: that is a different defect
    (a stale or mis-rendered cache) with its own audit, and this test should not
    report it as truncation.
    """
    record = yaml.safe_load(path.read_text())
    offenders: list[str] = []

    for item in _evidence_items(record):
        snippet = " ".join(str(item.get("snippet") or "").split())
        if not snippet or not _ABBREV_TAIL.search(snippet):
            continue
        for cached in _cache_texts(str(item.get("reference"))):
            start = cached.find(snippet)
            if start < 0:
                continue
            continuation = cached[start + len(snippet) :]
            if _LOWER_CONT.match(continuation):
                offenders.append(f"{snippet[-52:]!r} + {continuation[:26]!r}")
                break  # one report per snippet, not one per cache variant

    assert not offenders, (
        f"{path.name} has {len(offenders)} snippet(s) truncated at a genus "
        f"abbreviation — the sentence splitter treated e.g. 'C.' as a full stop, "
        f"so the snippet stops at the word it was meant to identify:\n  "
        + "\n  ".join(offenders)
        + "\nExtend each to the end of the clause; the continuation shown is what "
        "the cached reference actually says next."
    )
