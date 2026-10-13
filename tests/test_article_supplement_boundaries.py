"""Supplement caches must not be copied into the article evidence surface (#1994)."""

from __future__ import annotations

import importlib.util
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parents[1]
SCRIPT = REPO / "scripts/separate_legacy_supplements.py"
SPEC = importlib.util.spec_from_file_location("separate_supplements", SCRIPT)
assert SPEC and SPEC.loader
migration = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(migration)


def mixed_articles(cache):
    return sorted(
        str(path.relative_to(cache))
        for path in cache.rglob("*")
        if path.is_file()
        and path.suffix in {".md", ".txt"}
        and not path.name.endswith(".supplement.md")
        and migration.MARKER in path.read_bytes()
    )


def test_article_caches_do_not_contain_appended_supplements():
    assert mixed_articles(REPO / "references_cache") == []


@pytest.mark.parametrize("suffix", [".md", ".txt"])
def test_gate_control_mutation_and_restore(tmp_path, suffix):
    article = tmp_path / f"PMID_1{suffix}"
    original = b"Article body.\n\n"
    supplement = migration.MARKER + b" (PMID:1) =====\n\nSupplement only.\n"
    article.write_bytes(original)
    (tmp_path / "PMID_1.supplement.md").write_bytes(supplement)
    assert mixed_articles(tmp_path) == []
    article.write_bytes(original + supplement)
    assert article.read_bytes().count(migration.MARKER) == 1
    assert mixed_articles(tmp_path) == [article.name]
    article.write_bytes(original)
    assert article.read_bytes() == original
    assert mixed_articles(tmp_path) == []


def fixture_entry(tmp_path, existing=None):
    cache = tmp_path / "references_cache"
    cache.mkdir()
    head = b"Article body.\n\n"
    tail = migration.MARKER + b" (PMID:1) =====\n\nSupplement only.\n"
    article = cache / "PMID_1.txt"
    sidecar = cache / "PMID_1.supplement.md"
    article.write_bytes(head + tail)
    if existing is not None:
        sidecar.write_bytes(existing)
    return (
        {
            "article": "references_cache/PMID_1.txt",
            "supplement": "references_cache/PMID_1.supplement.md",
            "article_before_sha256": migration.digest(head + tail),
            "article_after_sha256": migration.digest(head[:-1]),
            "appended_sha256": migration.digest(tail),
            "supplement_before_sha256": (
                migration.digest(existing) if existing is not None else None
            ),
            "preserved_payload_offset": tail.index(b"Supplement only."),
        },
        article,
        sidecar,
        head,
        tail,
    )


@pytest.mark.parametrize("existing", [None, b"Different header\nSupplement only.\nMore tables.\n"])
def test_separation_preserves_article_and_supplement_bytes(tmp_path, existing):
    entry, article, sidecar, head, tail = fixture_entry(tmp_path, existing)
    before = article.read_bytes()
    plan = migration.prepare(tmp_path, [entry])
    assert article.read_bytes() == before
    migration.apply_plan(plan)
    assert article.read_bytes() == head[:-1]
    assert sidecar.read_bytes() == (tail if existing is None else existing)


@pytest.mark.parametrize("failure", ["article", "sidecar", "payload", "collision", "duplicate"])
def test_changed_or_unpreserved_evidence_fails_before_writing(tmp_path, failure):
    existing = b"Supplement only.\n" if failure != "collision" else None
    entry, article, sidecar, _, _ = fixture_entry(tmp_path, existing)
    entries = [entry]
    if failure == "article":
        article.write_bytes(article.read_bytes() + b"Changed")
    elif failure in {"sidecar", "collision"}:
        sidecar.write_bytes(b"Unreviewed evidence")
    elif failure == "payload":
        entry["preserved_payload_offset"] = 0
    else:
        entries.append(entry.copy())
    before = {p.name: p.read_bytes() for p in article.parent.iterdir()}
    with pytest.raises(ValueError):
        migration.prepare(tmp_path, entries)
    assert {p.name: p.read_bytes() for p in article.parent.iterdir()} == before


@pytest.mark.parametrize(
    "raw",
    [b"article", migration.MARKER, b"body " + migration.MARKER, b"body\n" + migration.MARKER * 2],
)
def test_ambiguous_boundaries_are_rejected(raw):
    with pytest.raises(ValueError):
        migration.split_article(raw)
