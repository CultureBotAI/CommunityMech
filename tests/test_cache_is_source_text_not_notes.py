"""A reference cache must hold the source, not a restatement of the curation (#592).

`linkml-reference-validator` matches an evidence snippet as a **substring of the
cache file**. So anything written into a cache file becomes something snippets
can validate against. 34 files in `references_cache/` had grown a curator-authored
section:

    Key snippets used in curated records:
    - "The altered Schaedler flora (ASF) is a model community of eight microorganisms"
    - "ASF356 Clostridium sp."

Every snippet listed there validated against a file whose content was copied from
the snippet. The check confirmed the curation against itself. 198 snippets across
16 records had no other source on disk at all.

Measured end-to-end on one record, against a scratch cache directory: with the
block present the validator reported 4 failures; with only that block removed, 9.
Corpus-wide, removing them took `validate-references` from 331 failing snippets
to 460. Those 129 were never passing on merit.

**The second failure mode, which is the same mistake inverted.** `literature.py`
writes a fetched abstract to `PMID_<id>.txt`, but the validator reads
`PMID_<id>.md` and only falls back to `.txt` when no `.md` exists. So a
hand-written `.md` silently *shadowed* the real abstract. `PMID_26323627.md` was
1095 bytes with no abstract in it, while `PMID_26323627.txt` held the genuine
PubMed abstract — and this verbatim quote was reported unverifiable:

    "stably passed through multiple generations (at least 15 years or more by
     the authors) in gnotobiotic mice continually bred in isolator facilities"

Faithful quotes failed while paraphrases passed. Deleting the shadowing stub
fixed it with no other change.

This file gates the first failure mode directly, and the second by asserting that
no `.md` cache is a stub sitting on top of a real `.txt`.
"""

from __future__ import annotations

import pathlib
import re

import pytest

REPO = pathlib.Path(__file__).parent.parent
CACHE = REPO / "references_cache"

# Matched loosely on purpose. The first sweep of this pattern searched for the
# exact phrase "Key snippets used in curated records" and reported the corpus
# clean — while eleven files carried "Quoted snippets used in curated records"
# and went on validating against themselves. The habit is what matters, not the
# wording someone reached for.
_SNIPPET_LISTING = re.compile(r"snippets used in curated records", re.IGNORECASE)

# Set by cache_fulltext.py when it appends genuinely retrieved text.
_FULL_TEXT_MARKER = "===== OPEN-ACCESS FULL TEXT"

# A real abstract is a paragraph of prose. A stub is a title, a couple of links,
# and some bullets. Prose length separates them where file size cannot: 308
# caches use a structured format (YAML front matter, then the abstract under
# `## Content`) whose *byte count* can sit below its own `.txt` sibling purely
# because the `.txt` carries MEDLINE boilerplate. Measured on the real corpus,
# the gap is unambiguous — the one true stub had a longest paragraph of 142
# characters, the structured format 1300.
_PROSE_FLOOR = 300


def _cache_files() -> list[pathlib.Path]:
    return sorted(p for p in CACHE.iterdir() if p.is_file() and p.suffix in {".md", ".txt"})


def _longest_paragraph(text: str) -> int:
    """Length of the longest prose paragraph, ignoring structural furniture.

    Front matter, headings, bold author lines, bullets and bare URL/DOI lines
    are not abstract text; counting them would let a stub look like a paper.
    """
    text = re.sub(r"^---.*?^---", "", text, flags=re.S | re.M)
    paragraphs = (" ".join(p.split()) for p in re.split(r"\n\s*\n", text))
    return max(
        (len(p) for p in paragraphs if not p.startswith(("#", "**", "- ", "* ", "URL:", "DOI:"))),
        default=0,
    )


def test_no_cache_file_lists_the_snippets_it_will_be_checked_against():
    """The gate. A snippet must validate against the paper, not against itself."""
    offenders = [
        p.name for p in _cache_files() if _SNIPPET_LISTING.search(p.read_text(errors="replace"))
    ]
    assert offenders == [], (
        "these cache files contain a curator-written list of the snippets that "
        "are validated against them, so those snippets confirm the curation "
        "against itself (#592). A cache file must hold retrieved source text "
        "only — put notes somewhere that is not searched for evidence:\n"
        + "\n".join(f"  {name}" for name in offenders)
    )


def test_no_md_stub_shadows_a_real_txt_abstract():
    """`.md` wins over `.txt`, so a hand-written `.md` hides a fetched abstract.

    `literature.py` caches to `.txt`; the validator reads `.md` first. Any small
    `.md` with no retrieved-text marker sitting next to a `.txt` is that bug.
    """
    shadowing = []
    for md in sorted(CACHE.glob("*.md")):
        txt = md.with_suffix(".txt")
        if not txt.is_file():
            continue
        body = md.read_text(errors="replace")
        if _FULL_TEXT_MARKER in body:
            continue  # carries genuinely retrieved full text; not a stub
        prose = _longest_paragraph(body)
        if prose < _PROSE_FLOOR and txt.stat().st_size > len(body):
            shadowing.append(
                f"{md.name} (longest paragraph {prose} chars) shadows "
                f"{txt.name} ({txt.stat().st_size}B)"
            )
    assert shadowing == [], (
        "a small `.md` with no retrieved-text marker is sitting on top of a "
        "larger `.txt`. The validator reads the `.md` and never sees the "
        "fetched abstract, so faithful quotes are reported as unverifiable "
        "(#592). Delete the stub, or append real retrieved text to it:\n"
        + "\n".join(f"  {line}" for line in shadowing)
    )


@pytest.mark.parametrize(
    "heading",
    [
        "Key snippets used in curated records:",
        # The wording an exact-phrase search missed on the first pass, leaving
        # eleven files validating against themselves.
        "Quoted snippets used in curated records:",
        "SNIPPETS USED IN CURATED RECORDS",
    ],
)
def test_the_snippet_listing_gate_can_fire(tmp_path, heading):
    """Mutation check: the corpus is clean, so silence proves nothing.

    Parametrised over the wordings actually found on disk, because the first
    version of this gate matched one literal string and reported clean while the
    defect was still present under a different heading.
    """
    cache = tmp_path / "references_cache"
    cache.mkdir()
    (cache / "PMID_1.md").write_text(
        f"# PMID:1\n\nTitle: Something\n\n{heading}\n" '- "a phrase somebody wanted to validate"\n',
        encoding="utf-8",
    )
    (cache / "PMID_2.md").write_text("# PMID:2\n\nA real abstract.\n", encoding="utf-8")

    offenders = [p.name for p in _cache_files_in(cache) if _SNIPPET_LISTING.search(p.read_text())]
    assert offenders == ["PMID_1.md"], f"gate did not identify the planted file: {offenders}"


def _cache_files_in(directory: pathlib.Path) -> list[pathlib.Path]:
    return sorted(p for p in directory.iterdir() if p.is_file() and p.suffix in {".md", ".txt"})


def test_the_shadowing_gate_can_fire(tmp_path):
    """Mutation check for the second gate, using the real PMID_26323627 shape."""
    cache = tmp_path / "references_cache"
    cache.mkdir()
    (cache / "PMID_26323627.md").write_text("# PMID:26323627\n\nTitle: x\n", encoding="utf-8")
    (cache / "PMID_26323627.txt").write_text(
        "1. ILAR J. " + "real abstract " * 200, encoding="utf-8"
    )

    found = [
        md.name
        for md in sorted(cache.glob("*.md"))
        if md.with_suffix(".txt").is_file()
        and _FULL_TEXT_MARKER not in md.read_text()
        and _longest_paragraph(md.read_text()) < _PROSE_FLOOR
        and md.with_suffix(".txt").stat().st_size > md.stat().st_size
    ]
    assert found == ["PMID_26323627.md"], f"gate missed the planted stub: {found}"


def test_the_shadowing_gate_spares_the_structured_format(tmp_path):
    """The false positive this gate had on its first run, pinned.

    308 caches use YAML front matter plus the abstract under `## Content`. Sized
    against a MEDLINE `.txt` they can look smaller, and the first version of
    this gate duly flagged `PMID_34726691.md` — which contains the real
    abstract. Prose length is what separates them, so prove it does.
    """
    cache = tmp_path / "references_cache"
    cache.mkdir()
    # Taken from the real PMID_34726691.md, which measures 1300 characters of
    # prose. A synthetic two-sentence stand-in measured 276 and failed this
    # test — worth keeping in mind that the floor sits nearer a stub than an
    # abstract, so the fixture has to be a realistic length to prove anything.
    abstract = (
        "Genome-scale metabolic models (GSMs) have been widely used to study "
        "microbial ecosystems. Yet the dynamic nature of microbial systems "
        "remains a challenge for GSMs to predict. Reactive transport codes "
        "(RTCs) simulate biogeochemical systems by modeling the mass transfer "
        "and biochemical reactions occurring in an environmental system through "
        "time and space. Both approaches seek to predict metabolic processes and "
        "biogeochemical reactions; however, they operate at different scales and "
        "employ distinct model parameterizations. To leverage the distinct "
        "advantages of each modeling approach, we developed an automated workflow "
        "that iteratively cycles between metabolic modeling software in KBase and "
        "the reactive transport code PFLOTRAN. Here, we demonstrate this "
        "workflow's ability to predict nitrogen cycling patterns with site-"
        "specific insight into the chemical and biological drivers of "
        "nitrification and denitrification processes."
    )
    (cache / "PMID_34726691.md").write_text(
        f"---\nreference_id: PMID:34726691\ncontent_type: abstract_only\n---\n\n"
        f"# ORT: a workflow\n**Authors:** A B\n\n## Content\n\n{abstract}\n",
        encoding="utf-8",
    )
    (cache / "PMID_34726691.txt").write_text("1. Bioinformatics. " + "x" * 4000, encoding="utf-8")

    md = cache / "PMID_34726691.md"
    assert _longest_paragraph(md.read_text()) >= _PROSE_FLOOR, (
        "the structured abstract format was measured as prose-free, so the "
        "shadowing gate would flag 308 legitimate caches"
    )


def test_the_walk_reaches_the_real_corpus():
    """Guard: an empty walk passes both gates as surely as a clean corpus does."""
    files = _cache_files()
    assert len(files) > 400, f"only {len(files)} cache files walked; the glob is broken"
    assert any(
        _FULL_TEXT_MARKER in p.read_text(errors="replace") for p in files[:200] + files[-200:]
    ), "no cache file carries retrieved full text; the read is broken"
