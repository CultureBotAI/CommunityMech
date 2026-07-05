#!/usr/bin/env python3
"""Consolidate the 22 author-request drafts into one review-ready package.

Corresponding-author emails for these papers live only in the (paywalled) full
text, so they cannot be resolved programmatically (CrossRef/Europe PMC do not
expose them). This script enriches each draft with everything that *is* public —
title, journal, author list, likely corresponding author (last author), and the
publisher landing URL — so a human can open the paper, grab the email, and send
in one pass. It does NOT send anything.

Reads the "Need author-request" list from reports/fulltext_access_183.md and the
per-record draft bodies from reports/author_requests/. Writes
reports/author_requests_index.md.

Usage:
    uv run python scripts/author_request_index.py
"""

from __future__ import annotations

import html
import json
import re
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

EMAIL = "marcinjoachimiak@gmail.com"
UA = {"User-Agent": f"CommunityMech/1.0 (mailto:{EMAIL})"}
ROOT = Path(__file__).resolve().parent.parent
RESIDUAL_MD = ROOT / "reports" / "fulltext_access_183.md"
AUTHOR_DIR = ROOT / "reports" / "author_requests"
OUT_MD = ROOT / "reports" / "author_requests_index.md"


def _get_json(url: str):
    try:
        req = urllib.request.Request(url, headers=UA)  # noqa: S310
        with urllib.request.urlopen(req, timeout=25) as r:  # noqa: S310
            return json.load(r)
    except Exception:
        return None


def parse_residuals() -> list[dict]:
    tail = RESIDUAL_MD.read_text().split("Need author-request", 1)[-1]
    out = []
    for m in re.finditer(r"CommunityMech:(\d+)\s+((?:PMID|doi):\S+)", tail):
        cid, ref = m.group(1), m.group(2)
        pmid = ref.split(":", 1)[1] if ref.lower().startswith("pmid") else None
        doi = ref.split(":", 1)[1] if ref.lower().startswith("doi") else None
        draft = next(iter(AUTHOR_DIR.glob(f"{cid}_*.txt")), None)
        out.append({"cid": cid, "ref": ref, "pmid": pmid, "doi": doi, "draft": draft})
    return out


def meta(rec: dict) -> dict:
    """Title, journal, authors, resolved DOI — from CrossRef (DOI) or Europe PMC (PMID)."""
    doi = rec["doi"]
    if not doi and rec["pmid"]:
        q = urllib.parse.urlencode(
            {"query": f"EXT_ID:{rec['pmid']} AND SRC:MED", "format": "json", "resultType": "core"}
        )
        r = (
            (_get_json(f"https://www.ebi.ac.uk/europepmc/webservices/rest/search?{q}") or {})
            .get("resultList", {})
            .get("result")
            or [{}]
        )[0]
        doi = r.get("doi")
    m = {}
    if doi:
        d = _get_json(f"https://api.crossref.org/works/{urllib.parse.quote(doi)}")
        m = (d or {}).get("message", {})
    authors = [
        " ".join(x for x in (a.get("given"), a.get("family")) if x) for a in m.get("author", [])
    ]
    return {
        "doi": doi,
        "title": re.sub(r"\s+", " ", (m.get("title") or [""])[0]).strip(),
        "journal": (m.get("container-title") or [""])[0],
        "authors": authors,
        "last_author": authors[-1] if authors else "",
        "landing": (
            f"https://doi.org/{doi}" if doi else f"https://pubmed.ncbi.nlm.nih.gov/{rec['pmid']}/"
        ),
    }


def main() -> int:
    residuals = parse_residuals()
    print(f"Enriching {len(residuals)} author-request drafts...", file=sys.stderr)
    rows = []
    for r in residuals:
        m = meta(r)
        rows.append({**r, **m})
        print(f"  {r['cid']} {m['journal'][:40]:<40} corr?~{m['last_author']}", file=sys.stderr)
        time.sleep(0.2)

    lines = [
        "# Author-request package — 22 paywalled #183 residuals",
        "",
        "Emails are **not** machine-resolvable (they appear only in the paywalled full "
        "text). For each record below: open the landing URL, copy the corresponding "
        "author's email from the PDF/HTML, and send the draft body (in "
        "`reports/author_requests/<file>`). The likely corresponding author (last in the "
        "byline) is noted as a starting point — verify against the paper's "
        "✉ marking. Nothing here has been sent.",
        "",
        "| # | community | journal | likely corresponding author "
        "| landing (grab email here) | draft |",
        "|---|---|---|---|---|---|",
    ]
    for r in rows:
        draft = r["draft"].name if r["draft"] else ""
        title = html.unescape(r["title"] or "").replace("|", "\\|")[:60]
        jour = html.unescape(r["journal"] or "?").replace("|", "\\|")[:32]
        lines.append(
            f"| {r['cid']} | {title} | {jour} | {r['last_author'] or '?'} "
            f"| <{r['landing']}> | `{draft}` |"
        )
    lines.append("")
    OUT_MD.write_text("\n".join(lines))
    print(f"\nWrote {OUT_MD.relative_to(ROOT)}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
