"""Resolving a reference to a cache file must not depend on directory order.

`references_cache/` holds `.md`, `.txt` and `.json` for the same reference, and
**63 references have more than one**. Per #265 the `.md` typically holds
open-access full text while the `.txt` is often just the abstract, so they are
not interchangeable: scanning snippets while preferring one or the other located
4471 vs 4400 of them — **71 snippets differ**.

Any consumer resolving with `glob(key + ".*")` and taking the first match
therefore reads a filesystem-order-dependent file, so whether those 71 get
checked depends on the machine (#306).

`evidence_snippet_audit.py` already does the right thing — it collects every
candidate, orders them by extension, and concatenates the ones carrying real
prose. This pins that, because the property is invisible in normal runs: it only
shows up as a different answer on a different filesystem.

`.json` is CrossRef metadata rather than prose, so treating it as text is wrong
outright, and that is asserted separately.
"""

import importlib.util
import random
import re
from collections import defaultdict
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
def audit():
    return _load_audit()


@pytest.fixture(scope="module")
def multi_cache_refs() -> list:
    """References that have more than one cache file — the population at issue."""
    by_stem = defaultdict(list)
    for path in CACHE.iterdir():
        if path.is_file():
            by_stem[re.sub(r"\.(md|txt|json)$", "", path.name)].append(path)

    refs = [
        "PMID:" + stem.split("_", 1)[1]
        for stem, files in by_stem.items()
        if len(files) > 1 and stem.startswith("PMID_")
    ]
    assert len(refs) > 20, f"expected the multi-cache population, found {len(refs)}"
    return sorted(refs)


def test_resolution_is_independent_of_directory_order(audit, multi_cache_refs, monkeypatch):
    """The answer must not change when the filesystem hands back a different order.

    Shuffling `Path.iterdir` stands in for a different filesystem. Taking the
    first `glob` match would fail this immediately.
    """
    sample = multi_cache_refs[:25]
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
