"""No publication PDFs, and no paywalled article bodies, in the repository (#754).

`references_cache/` exists so `linkml-reference-validator` can show that a
snippet really came from the source a record cites. That purpose is served by
abstracts and by open-access full text. It is not served by keeping text we have
no right to redistribute, and the repository is **public**.

What #754 found: 754 cache files and 24 MB committed, with no licence recorded
anywhere and no statement of provenance; a **14 MB Elsevier publication PDF** in
`references_pdfs/`; and three cache files holding non-open-access article bodies,
two of them carrying the publisher's own copyright line.

`scripts/cache_fulltext.py` filters on Europe PMC's OA flag. That does not
verify permission for a particular curator-supplied publication version. These
tests detect PDFs and a rights-marker/body-size pattern; they are regression
heuristics, not an exhaustive license audit.
"""

from __future__ import annotations

import pathlib
import re

from communitymech.paths import REPO_ROOT

CACHE = REPO_ROOT / "references_cache"

# A publisher asserting rights over the text in the same file as the text.
RIGHTS = re.compile(
    r"All rights are reserved|All rights reserved|"
    r"Copyright\s+©\s+\d{4},\s+American Association|"
    r"©\s*\d{4}\s+Elsevier",
    re.I,
)

# A Creative Commons marker bypasses this heuristic to avoid known false
# positives; it does not prove permission for the version or use. Check the
# actual terms separately. `PMID_39111313.txt` carries a CC BY-NC marker and
# "All rights reserved" in publisher furniture, motivating this exemption.
CC = re.compile(r"creativecommons\.org|CC[- ]BY", re.I)

# Size is the crude proxy for "this is a body, not an abstract". A PubMed
# abstract dump with author affiliations reaches ~7 kB (`PMID_42167379.md` is
# 5.5 kB of content and is an abstract). The bodies #754 removed were 10, 24,
# 48, 80, 110 and 139 kB. 9000 separates them with room on both sides.
BODY_BYTES = 9000


def _tracked(pattern: str) -> list[pathlib.Path]:
    return sorted(REPO_ROOT.glob(pattern))


def test_no_publication_pdfs_are_committed():
    """A PDF of a paper is the least ambiguous form of the problem."""
    pdfs = [
        p for p in REPO_ROOT.glob("**/*.pdf") if ".venv" not in p.parts and ".git" not in p.parts
    ]
    assert pdfs == [], (
        "publication PDFs must not live in this repository (#754). Cite the DOI "
        "and cache the abstract or the OA full text instead:\n"
        + "\n".join(f"  {p.relative_to(REPO_ROOT)} ({p.stat().st_size // 1024} kB)" for p in pdfs)
    )


def test_no_cache_file_carries_a_publisher_rights_assertion_over_a_body():
    """A rights line beside a large body is the signature of the real problem.

    A rights line in a *short* file is usually the copyright footer Europe PMC
    ships with an abstract, which is fine to hold — so size and the assertion
    together are what this looks for, not either alone.
    """
    offenders = []
    for path in sorted(CACHE.glob("*.md")) + sorted(CACHE.glob("*.txt")):
        text = path.read_text(encoding="utf-8", errors="replace")
        if CC.search(text):
            continue
        if path.stat().st_size > BODY_BYTES and RIGHTS.search(text):
            match = RIGHTS.search(text)
            offenders.append(
                f"  {path.name} ({path.stat().st_size // 1024} kB): {match.group(0)!r}"
            )
    assert offenders == [], (
        "these cache files hold a large body alongside a publisher's rights "
        "assertion (#754). Replace the body with the abstract; snippets taken "
        "from the removed text will stop verifying, and that is the correct "
        "outcome:\n" + "\n".join(offenders)
    )


def test_the_check_can_actually_fail():
    """Pin both predicates against known inputs rather than trusting a green run."""
    assert RIGHTS.search("© 2026 Elsevier Ltd. All rights are reserved, including those for text")
    assert RIGHTS.search("Copyright © 2014, American Association for the Advancement of Science.")
    assert not RIGHTS.search(
        "This is an open-access article distributed under the terms of the CC BY 4.0 licence"
    )
    assert CC.search("http://creativecommons.org/licenses/by-nc/4.0/")
    assert not CC.search("Copyright © 2014, American Association for the Advancement of Science.")
