"""A cited reference must find its cache by exact filename, not by luck (#690).

`references_cache/` carried two conventions for one prefix -- 133 files named
`DOI_*` and 79 named `doi_*` -- while every reference in the corpus writes
`doi:` in lowercase. The stem convention shared by this repo's scripts and by
the upstream validator is::

    reference.replace(":", "_").replace("/", "_")

which yields `doi_...`. The `DOI_*` half was therefore findable only on a
filesystem that ignores case. macOS ignores case; Linux does not.

That is not a tidiness problem. `linkml_reference_validator`'s fetcher builds
the same stem and calls `.exists()`
(``etl/reference_fetcher.py:204-225``), so on Linux those references were cache
**misses** -- and per the rationale in ``src/communitymech/paths.py`` a miss is
not a skip, it sends the fetcher to the network. 117 of 514 distinct references
(23%) were in that state when this was measured.

It surfaced as a local/CI divergence: #688 scored six records on macOS and
reported them blind on the runner. The first diagnosis blamed uncommitted files
in the working tree and was wrong -- hiding them inverted the result rather
than reproducing it.

**Why `os.listdir` and not `Path.is_file()`.** On a case-insensitive filesystem
`is_file()` answers the question this module exists to ask with a "yes" that
Linux would not give. `os.listdir` returns the names as they are actually
stored, so exact string membership is a genuinely case-sensitive test on both
platforms -- the check has to be one that can fail on the machine running it.
"""

from __future__ import annotations

import os
import pathlib
import re

import pytest

from communitymech.paths import KB_TAXA, REFERENCES_CACHE, default_record_roots

# `reference:` is the slot every EvidenceItem carries. Matching the YAML text
# rather than loading each document keeps this independent of the schema's
# nesting, which differs between MicrobialCommunity and CommonTaxon.
_REFERENCE = re.compile(r'reference:\s*["\']?([A-Za-z][A-Za-z0-9]*:[^"\'\s]+)')

_SUFFIXES = (".md", ".txt")


def _record_paths() -> list[pathlib.Path]:
    roots = [*default_record_roots(), KB_TAXA]
    return [path for root in roots for path in sorted(root.glob("*.yaml"))]


def _references() -> dict[str, list[str]]:
    """Every cited reference, mapped to the records citing it."""
    found: dict[str, list[str]] = {}
    for path in _record_paths():
        for reference in _REFERENCE.findall(path.read_text(encoding="utf-8")):
            found.setdefault(reference, []).append(f"{path.parent.name}/{path.name}")
    return found


def _stem(reference: str) -> str:
    """The cache stem, built exactly as the scripts and the validator build it."""
    return reference.replace(":", "_").replace("/", "_")


@pytest.fixture(scope="module")
def cache_names() -> set[str]:
    return set(os.listdir(REFERENCES_CACHE))


@pytest.fixture(scope="module")
def references() -> dict[str, list[str]]:
    return _references()


def test_there_are_references_and_caches_to_check(references, cache_names):
    """Guard: an empty corpus or an empty cache makes the check below vacuous."""
    assert len(references) >= 400, f"only {len(references)} references found; the scan broke"
    assert len(cache_names) >= 400, f"only {len(cache_names)} cache files found"


def test_no_reference_resolves_only_by_filename_case(references, cache_names):
    """The check itself: a cache found on macOS must be found on Linux too."""
    lower = {name.lower(): name for name in cache_names}
    offenders = []
    for reference, records in sorted(references.items()):
        stem = _stem(reference)
        if any(f"{stem}{suffix}" in cache_names for suffix in _SUFFIXES):
            continue  # exact match: correct on every filesystem
        for suffix in _SUFFIXES:
            actual = lower.get(f"{stem}{suffix}".lower())
            if actual is not None:
                offenders.append(
                    f"  {reference}\n"
                    f"      looks for {stem}{suffix}\n"
                    f"      on disk   {actual}\n"
                    f"      cited by  {records[0]}"
                )
                break
        # No match either way is an uncached reference -- a real gap, but a
        # different one (the source was never fetched), and not this test's.

    assert offenders == [], (
        "these references find their cache only because the local filesystem "
        "ignores case; on Linux they are cache misses, which sends the "
        "validator to the network (#690):\n" + "\n".join(offenders) + "\n\n"
        "Rename the file to the name the stem convention produces. On macOS a "
        "direct `git mv DOI_x.md doi_x.md` is a no-op -- go via a temporary "
        "name:\n"
        "    git mv references_cache/DOI_x.md references_cache/DOI_x.md.tmp\n"
        "    git mv references_cache/DOI_x.md.tmp references_cache/doi_x.md"
    )


def test_the_case_check_can_actually_fail(tmp_path):
    """Mutation check on synthetic input, since the corpus is clean.

    Without this, a `cache_names` that came back empty -- or a `_stem` that
    stopped matching anything -- would look exactly like success.
    """
    names = {"DOI_10.1000_example.md"}
    lower = {name.lower(): name for name in names}
    stem = _stem("doi:10.1000/example")
    assert f"{stem}.md" not in names, "the exact-match arm must miss here"
    assert lower.get(f"{stem}.md".lower()) == "DOI_10.1000_example.md"

    # ...and the reverse: a correctly-named file must NOT be flagged.
    ok = {"doi_10.1000_example.md"}
    assert f"{stem}.md" in ok
