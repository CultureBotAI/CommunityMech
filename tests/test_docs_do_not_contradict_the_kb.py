"""The published site rendered a plant's taxon id for a bacterium (#442).

`generate-pages.yaml` serves the committed `docs/` tree verbatim, and nothing
regenerated or checked it. A data PR that corrected a record and did not re-run
`just gen-html` published a page contradicting the KB — invisibly, since no
schema validator or id↔label gate reads HTML.

Both directions had drifted by the time this was written:

* 7 pages carried taxon ids the record no longer held. Two rendered
  `NCBITaxon:169215` — the *plant* genus *Bosea* — as a live NCBI link on a
  bacterium, and `KBase_ORT_Workflow_Community_Model` still showed the
  class/phylum ids its record replaced in 2a3b691.
* 7 records had **no page at all**. That is the failure a diff of existing
  files cannot see, which is why `just check-docs-current` counts untracked
  files and why `test_every_record_has_a_published_page` is separate below.

`just check-docs-current` (CI: `docs-current.yaml`) is the real gate — it
regenerates and demands a byte-identical tree. These tests are the fast local
signal, and they state the *property* rather than the mechanism: a page must
not assert a taxon id its record does not have. That distinction matters
because the gate can only say "re-run the renderer", while a failure here names
the contradiction.
"""

from __future__ import annotations

import pathlib
import re

import pytest
import yaml

REPO = pathlib.Path(__file__).parent.parent
PAGES = REPO / "docs/communities"
RECORDS = REPO / "kb/communities"

# Matches both the visible CURIE and the NCBI browser links the pages emit
# (`wwwtax.cgi?id=169215`), since the link is what a reader actually follows.
_CURIE = re.compile(r"NCBITaxon:(\d+)")
_LINK = re.compile(r"wwwtax\.cgi\?id=(\d+)")


def _record_taxon_ids(record: pathlib.Path) -> set[str]:
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
    pairs = []
    for record in sorted(RECORDS.glob("*.yaml")):
        page = PAGES / f"{record.stem}.html"
        if page.exists():
            pairs.append((record, page))
    return pairs


def test_there_are_pages_to_check():
    """Guard: if the pairing breaks, every test below passes vacuously."""
    pairs = _paired()
    assert len(pairs) > 300, (
        f"only {len(pairs)} record/page pairs resolved; the naming convention "
        f"between kb/communities/*.yaml and docs/communities/*.html has "
        f"probably changed, and the checks below are no longer checking it"
    )


def test_every_record_has_a_published_page():
    """A record with no page is invisible on the site and produces no diff.

    Seven were missing when this was written — added without regenerating, so
    nothing anywhere reported them.
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


@pytest.mark.parametrize(("record", "page"), _paired(), ids=[r.stem for r, _ in _paired()])
def test_no_page_asserts_a_taxon_id_its_record_does_not_have(
    record: pathlib.Path, page: pathlib.Path
):
    """The property, stated directly: the page may not contradict the record.

    Checked one-directionally on purpose. A page carrying an id the record
    dropped is a published falsehood — the Bosea case, where the link resolved
    to a flowering plant. The converse (a record id absent from the page) is
    routine: pages summarise, and not every id is rendered.
    """
    expected = _record_taxon_ids(record)
    text = page.read_text()
    rendered = set(_CURIE.findall(text)) | set(_LINK.findall(text))

    contradictions = sorted(rendered - expected)
    assert contradictions == [], (
        f"{page.name} renders NCBITaxon ids that {record.name} does not "
        f"contain: {contradictions}. The committed docs/ tree is published "
        f"verbatim, so this is live on the site — run `just gen-html` and "
        f"commit (#442)."
    )
