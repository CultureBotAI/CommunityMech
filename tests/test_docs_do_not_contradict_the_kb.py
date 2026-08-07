"""The published site linked the wrong organism, twice (#442).

`generate-pages.yaml` serves the committed `docs/` tree verbatim, and nothing
regenerated or checked it. A data PR that corrected a record and did not re-run
`just gen-html` published a page contradicting the KB — invisibly, since no
schema validator or id↔label gate reads HTML.

Three ways it had drifted:

* **8 pages linked a taxon id the record no longer holds there.** Two rendered
  `NCBITaxon:169215` — the flowering-plant genus *Bosea* — as a live NCBI link
  on a bacterium. `BioModels_MODEL2405300001_Infant_Gut_HMO_SynCom` linked
  *Bacteroides ovatus* to `NCBITaxon:821`, which is *Phocaeicola vulgatus* —
  the row above it.
* **7 records had no page at all**, added without a regeneration. A diff of
  existing files cannot see that, which is why the gate counts untracked files.
* **Orphan pages** survive a record rename, since `gen-html` only writes.

The oracle here is positional, and that is the point. An earlier version of this
file compared *sets* — every `NCBITaxon:` id anywhere in the page against every
one anywhere in the record — and passed the *Bacteroides ovatus* case, because
821 does appear in that record, one row up. Set membership cannot see a swap
between two ids a record both contains, and swaps are what wrong-organism links
are made of. Each `taxon_term.term.id` is also duplicated as
`gtdb_classification.ncbi_source_id`, so the document-wide set is unusually
forgiving.

The renderer emits `taxonomy[].taxon_term.term.id` first and in record order;
verified across all 312 pages, the record's taxonomy ids are a prefix of the
page's NCBI links. Interaction participants add links after that prefix, so the
check is a prefix comparison rather than equality.

`just check-docs-current` (CI: `docs-current.yaml`) remains the real gate — it
regenerates and demands a byte-identical tree. These tests are the fast local
signal, and they name the contradiction where the gate can only say "re-run the
renderer".
"""

from __future__ import annotations

import pathlib
import re

import pytest
import yaml

REPO = pathlib.Path(__file__).parent.parent
PAGES = REPO / "docs/communities"
RECORDS = REPO / "kb/communities"

# The link is what a reader actually follows, and it carries a bare numeric id.
_LINK = re.compile(r"wwwtax\.cgi\?id=(\d+)")
_CURIE = re.compile(r"NCBITaxon:(\d+)")


def _taxonomy_ids(record: pathlib.Path) -> list[str]:
    """The record's taxonomy ids, in order — the sequence the renderer emits."""
    document = yaml.safe_load(record.read_text()) or {}
    ids = []
    for entry in document.get("taxonomy") or []:
        term = ((entry or {}).get("taxon_term") or {}).get("term") or {}
        value = term.get("id")
        if isinstance(value, str) and value.startswith("NCBITaxon:"):
            ids.append(value.split(":", 1)[1])
    return ids


def _all_record_ids(record: pathlib.Path) -> set[str]:
    document = yaml.safe_load(record.read_text()) or {}
    found: set[str] = set()
    stack = [document]
    while stack:
        node = stack.pop()
        if isinstance(node, dict):
            value = node.get("id")
            if isinstance(value, str) and value.startswith("NCBITaxon:"):
                found.add(value.split(":", 1)[1])
            stack.extend(node.values())
        elif isinstance(node, list):
            stack.extend(node)
    return found


def _paired() -> list[tuple[pathlib.Path, pathlib.Path]]:
    return [
        (record, PAGES / f"{record.stem}.html")
        for record in sorted(RECORDS.glob("*.yaml"))
        if (PAGES / f"{record.stem}.html").exists()
    ]


_PAIRS = _paired()


def test_there_are_pages_to_check():
    """Guard: if the pairing breaks, every test below passes vacuously."""
    assert len(_PAIRS) > 300, (
        f"only {len(_PAIRS)} record/page pairs resolved; the naming convention "
        f"between kb/communities/*.yaml and docs/communities/*.html has "
        f"probably changed, and the checks below are no longer checking it"
    )


def test_every_record_has_a_published_page():
    """A record with no page is invisible on the site and produces no diff.

    Seven were missing when this was written.
    """
    missing = [
        record.name
        for record in sorted(RECORDS.glob("*.yaml"))
        if not (PAGES / f"{record.stem}.html").exists()
    ]
    assert missing == [], (
        "these records have no published page; run `just gen-html` and commit "
        f"docs/ (#442): {missing}"
    )


def test_no_page_survives_its_record():
    """An orphan page stays published after a rename, and the tree still diffs clean.

    `gen-html` only ever writes, so a renamed record leaves the old page
    tracked and served. f8d85b1 is a rename of exactly that shape.
    """
    orphans = [
        page.name
        for page in sorted(PAGES.glob("*.html"))
        if not (RECORDS / f"{page.stem}.yaml").exists()
    ]
    assert orphans == [], f"these published pages have no record and should be deleted: {orphans}"


@pytest.mark.parametrize(("record", "page"), _PAIRS, ids=[r.stem for r, _ in _PAIRS])
def test_the_taxonomy_links_match_the_record_row_for_row(record: pathlib.Path, page: pathlib.Path):
    """The strong check: right id, right row, right order.

    A set comparison passes when two rows swap ids, which is precisely how
    *Bacteroides ovatus* came to link to *Phocaeicola vulgatus*'s taxon.
    """
    expected = _taxonomy_ids(record)
    rendered = _LINK.findall(page.read_text())

    assert rendered[: len(expected)] == expected, (
        f"{page.name} links taxa that do not match {record.name} row for row.\n"
        f"  record: {expected}\n"
        f"  page:   {rendered[: len(expected)]}\n"
        f"The committed docs/ tree is published verbatim, so a mismatch here is "
        f"a live wrong-organism link — run `just gen-html` and commit (#442)."
    )


@pytest.mark.parametrize(("record", "page"), _PAIRS, ids=[r.stem for r, _ in _PAIRS])
def test_no_page_mentions_a_taxon_id_absent_from_its_record(
    record: pathlib.Path, page: pathlib.Path
):
    """Covers what the positional check cannot: ids rendered after the prefix.

    Interaction participants render below the taxonomy block, in no order this
    test can predict, so they get the weaker set treatment.
    """
    text = page.read_text()
    rendered = set(_LINK.findall(text)) | set(_CURIE.findall(text))

    contradictions = sorted(rendered - _all_record_ids(record))
    assert contradictions == [], (
        f"{page.name} renders NCBITaxon ids that {record.name} does not "
        f"contain anywhere: {contradictions} (#442)"
    )
