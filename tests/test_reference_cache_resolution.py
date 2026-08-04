"""Resolving a reference to a cache file must not depend on directory order.

`references_cache/` holds `.md`, `.txt` and `.json` for the same reference, and
63 references have more than one. Per #265 the `.md` typically holds open-access
full text while the `.txt` is often just the abstract, so they are not
interchangeable — scanning snippets under one preference or the other disagrees
on roughly 70. (The absolute totals depend on the normalisation used, so they are
deliberately not quoted here; #306 recorded 4471 vs 4400 under its own
convention. Note the *net* difference of the two totals is not the count of
snippets that differ: measured here, a net 72 against 74 actually divergent, in
both directions.)

Any consumer resolving with `glob(key + ".*")` and taking the first match reads a
filesystem-order-dependent file, so whether those get checked depends on the
machine (#306).

`evidence_snippet_audit.py` collects every candidate and concatenates the ones
carrying real prose, but ordering them by extension alone was not enough: 14
PMIDs have both `PMID_<id>.txt` and `pmc_full_pmid_<id>.txt`, which tie on
suffix, and Python's sort is stable — so their concatenation order fell through
to `iterdir`. Sorting by name as well fixes it, and the report is unchanged.

The tests below cover both populations, built the way `cache_text` itself selects
(substring over the whole filename). A fixture that groups by stem instead misses
exactly those 14, because the two names are different stems but one hit-set.

`.json` is CrossRef metadata rather than prose, so treating it as text is wrong
outright, and that is asserted separately.
"""

import importlib.util
import random
from pathlib import Path

import pytest

REPO = Path(__file__).parent.parent
CACHE = REPO / "references_cache"


def _load_audit():
    """Import the audit script for its resolver.

    It has a `main()` guard so importing prints nothing; before #306 the module
    ran a full KB audit as an import side effect.
    """
    spec = importlib.util.spec_from_file_location(
        "evidence_snippet_audit", REPO / "scripts/evidence_snippet_audit.py"
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def audit(monkeypatch_session=None):
    """The audit module, with its relative CACHE path resolved against the repo.

    `evidence_snippet_audit.py` uses `Path("references_cache")`, so importing it
    from anywhere but the repo root would otherwise resolve to nothing.
    """
    module = _load_audit()
    module.CACHE = CACHE
    module.COMM = REPO / "kb/communities"
    return module


@pytest.fixture(scope="module")
def multi_cache_refs(audit) -> list:
    """References whose *hit-set* has more than one file — the population at issue.

    Built the way `cache_text` selects (case-insensitive substring over the whole
    filename), not by stripping extensions off a stem. The two disagree, and the
    difference is exactly where the bug lived: `PMID_24743269.txt` and
    `pmc_full_pmid_24743269.txt` are different stems but the same hit-set, both
    `.txt`, so the extension sort tied and order fell through to the filesystem.
    A stem-based fixture excludes precisely the 14 references that could fail.
    """
    files = [path for path in CACHE.iterdir() if path.is_file()]
    cores = sorted(
        {
            path.name.split(".")[0].replace("PMID_", "")
            for path in files
            if path.name.startswith("PMID_")
        }
    )

    refs = []
    for core in cores:
        hits = [path for path in files if core.lower() in path.name.lower()]
        if len(hits) > 1:
            refs.append("PMID:" + core)

    assert len(refs) > 20, f"expected the multi-cache population, found {len(refs)}"
    return refs


@pytest.fixture(scope="module")
def same_suffix_refs(audit) -> list:
    """The subset whose hit-set holds two files of the *same* extension.

    These are the only references the extension sort cannot order on its own, so
    they are the ones that actually exercise the tiebreak.
    """
    files = [path for path in CACHE.iterdir() if path.is_file()]
    cores = sorted(
        {
            path.name.split(".")[0].replace("PMID_", "")
            for path in files
            if path.name.startswith("PMID_")
        }
    )

    refs = []
    for core in cores:
        hits = [path for path in files if core.lower() in path.name.lower()]
        suffixes = [path.suffix for path in hits]
        if len(suffixes) != len(set(suffixes)):
            refs.append("PMID:" + core)

    assert refs, "no same-suffix references found; the tiebreak would be untested"
    return refs


def test_resolution_is_independent_of_directory_order(audit, multi_cache_refs, monkeypatch):
    """The answer must not change when the filesystem hands back a different order.

    Shuffling `Path.iterdir` stands in for a different filesystem. Taking the
    first `glob` match would fail this immediately.
    """
    sample = multi_cache_refs
    baseline = {ref: audit.cache_text(ref) for ref in sample}

    real_iterdir = Path.iterdir
    rng = random.Random(0)  # noqa: S311 — shuffling a directory listing, not crypto

    def shuffled(self):
        items = list(real_iterdir(self))
        rng.shuffle(items)
        return iter(items)

    monkeypatch.setattr(Path, "iterdir", shuffled)

    for attempt in range(5):
        for ref in sample:
            assert audit.cache_text(ref) == baseline[ref], (
                f"{ref} resolved differently on shuffle {attempt} — cache resolution "
                f"depends on directory order (#306)"
            )


def test_json_metadata_is_not_treated_as_prose(audit, tmp_path, monkeypatch):
    """`.json` is CrossRef metadata; matching snippets against it is wrong."""
    monkeypatch.setattr(audit, "CACHE", tmp_path)
    (tmp_path / "PMID_999999.json").write_text(
        '{"title": "a distinctive phrase that only exists in metadata"}'
    )

    text, has_content = audit.cache_text("PMID:999999")

    assert not has_content, "a .json-only reference must not count as having prose"
    assert "distinctive phrase" not in text


def test_a_reference_with_no_cache_reports_no_content(audit, tmp_path, monkeypatch):
    monkeypatch.setattr(audit, "CACHE", tmp_path)
    text, has_content = audit.cache_text("PMID:404404")
    assert (text, has_content) == ("", False)


def test_importing_the_audit_does_not_run_it(capsys):
    """Before #306 the module printed a full KB audit on import."""
    _load_audit()
    captured = capsys.readouterr()
    assert captured.out == "", f"import printed {len(captured.out)} chars"


def test_same_suffix_candidates_are_ordered_deterministically(audit, same_suffix_refs, monkeypatch):
    """The case the extension sort alone cannot decide.

    14 PMIDs carry both `PMID_<id>.txt` and `pmc_full_pmid_<id>.txt`. Both are
    appended unconditionally, so with a stable sort and no name tiebreak their
    concatenation order was whatever `iterdir` returned — different answers on
    different filesystems. A stem-based population misses all 14 (#306).
    """
    baseline = {ref: audit.cache_text(ref) for ref in same_suffix_refs}

    real_iterdir = Path.iterdir
    rng = random.Random(1)  # noqa: S311 — shuffling a directory listing, not crypto

    def shuffled(self):
        items = list(real_iterdir(self))
        rng.shuffle(items)
        return iter(items)

    monkeypatch.setattr(Path, "iterdir", shuffled)

    for attempt in range(8):
        for ref in same_suffix_refs:
            assert audit.cache_text(ref) == baseline[ref], (
                f"{ref} resolved differently on shuffle {attempt}: two cache files "
                f"share an extension and the sort has no deterministic tiebreak (#306)"
            )
