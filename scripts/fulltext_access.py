#!/usr/bin/env python3
"""Legal full-text access ladder for enrichment (no gray-area sources).

Given a PMID or DOI, tries — in order of legality + cost — to locate an
openly/legally accessible full text, and if none is reachable, drafts an
author-request email. Routes (all legal; Sci-Hub etc. deliberately excluded):

  1. Europe PMC OA full text  — free, no key; JATS `fullTextXML` for the PMCID.
  2. Unpaywall best OA location — free (email only); nonprofit OurResearch, only
     legally-uploaded green/gold/hybrid copies.
  3. CORE full text            — free for public-research orgs; needs $CORE_API_KEY
     (register at https://core.ac.uk/services/api). Largest OA full-text corpus.
  4. Author-request draft       — corresponding author + a templated email asking
     for the Methods/cultivation section (legal, often effective).

Use for records whose primary paper is closed-access (the #183 residual): thin
membership stubs and records lacking growth conditions.

Usage:
    uv run python scripts/fulltext_access.py --pmid 41825563
    uv run python scripts/fulltext_access.py --doi 10.1016/j.biortech.2026.134417
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import urllib.parse
import urllib.request

EMAIL = os.environ.get("UNPAYWALL_EMAIL", "marcinjoachimiak@gmail.com")
UA = {"User-Agent": f"CommunityMech-fulltext/1.0 (mailto:{EMAIL})"}


def _get_json(url: str, headers: dict | None = None):
    if not url.startswith("https://"):  # only fixed https API hosts are queried
        return None
    hdr = {**UA, **(headers or {})}
    req = urllib.request.Request(url, headers=hdr)  # noqa: S310
    try:
        with urllib.request.urlopen(req, timeout=30) as r:  # noqa: S310
            return json.load(r)
    except Exception:
        return None


def epmc_core(pmid: str | None, doi: str | None) -> dict:
    """Europe PMC core record: pmcid, OA status, DOI/PMID, title, corresponding author."""
    if pmid:
        q = f"EXT_ID:{pmid} AND SRC:MED"
    elif doi:
        q = f'DOI:"{doi}"'
    else:
        return {}
    url = "https://www.ebi.ac.uk/europepmc/webservices/rest/search?" + urllib.parse.urlencode(
        {"query": q, "format": "json", "resultType": "core", "pageSize": "1"}
    )
    d = _get_json(url) or {}
    r = (d.get("resultList", {}).get("result") or [{}])[0]
    return r


def crossref_meta(doi: str | None) -> dict:
    """Title + author string from CrossRef, for records not in Europe PMC (e.g. DOI-only)."""
    if not doi:
        return {}
    d = _get_json(f"https://api.crossref.org/works/{urllib.parse.quote(doi)}")
    m = (d or {}).get("message", {})
    if not m:
        return {}
    authors = ", ".join(
        " ".join(x for x in (a.get("given"), a.get("family")) if x) for a in m.get("author", [])[:6]
    )
    return {"title": (m.get("title") or [""])[0], "authorString": authors}


def try_europepmc(rec: dict) -> str | None:
    pmcid = rec.get("pmcid")
    if pmcid and rec.get("isOpenAccess") == "Y":
        return f"https://www.ebi.ac.uk/europepmc/webservices/rest/{pmcid}/fullTextXML"
    return None


def try_unpaywall(doi: str | None) -> str | None:
    if not doi:
        return None
    d = _get_json(f"https://api.unpaywall.org/v2/{doi}?email={EMAIL}")
    if not d or not d.get("is_oa"):
        return None
    loc = d.get("best_oa_location") or {}
    url = loc.get("url_for_pdf") or loc.get("url")
    # Reject the DOI resolver itself — Unpaywall sometimes reports it as the
    # "OA location" for bronze/hybrid records, but it just redirects to the
    # publisher paywall (observed for Elsevier). Not a real full-text copy.
    if url and re.match(r"https?://(dx\.)?doi\.org/", url):
        return loc.get("url_for_pdf") if loc.get("url_for_pdf") not in (None, url) else None
    return url


def try_core(doi: str | None, title: str | None) -> str | None:
    key = os.environ.get("CORE_API_KEY")
    if not key or not (doi or title):
        return None
    q = f'doi:"{doi}"' if doi else f'title:"{title}"'
    url = "https://api.core.ac.uk/v3/search/works?" + urllib.parse.urlencode({"q": q, "limit": "1"})
    d = _get_json(url, headers={"Authorization": f"Bearer {key}"})
    for w in (d or {}).get("results", []) or []:
        for link in w.get("links", []) or []:
            if link.get("type") in ("download", "reader") and link.get("url"):
                return link["url"]
        if w.get("downloadUrl"):
            return w["downloadUrl"]
    return None


def author_request_draft(rec: dict, doi: str | None) -> str:
    title = re.sub(r"<[^>]+>", "", rec.get("title", "") or "").rstrip(".")
    authors = rec.get("authorString", "") or "the corresponding author"
    ref = f"doi:{doi}" if doi else f"PMID:{rec.get('pmid', '?')}"
    return (
        f"To: <corresponding author of: {authors}>\n"
        f"Subject: Request for Methods details — {title[:70]}\n\n"
        f"Dear Author,\n\n"
        f"I am curating an open, public microbial-community knowledge base and would like to "
        f'cite your paper "{title}" ({ref}). The abstract does not include the cultivation / '
        f"Methods details I need (medium composition, temperature, pH, atmosphere, and the "
        f"member strain identities). Could you share the relevant Methods/supplementary text, "
        f"or a PDF? The extracted, source-attributed data would be published openly with full "
        f"citation to your work.\n\nThank you,\nCommunityMech curation team\n"
    )


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    g = p.add_mutually_exclusive_group(required=True)
    g.add_argument("--pmid")
    g.add_argument("--doi")
    p.add_argument("--title", help="fallback for CORE title search")
    args = p.parse_args(argv)

    rec = epmc_core(args.pmid, args.doi)
    doi = args.doi or rec.get("doi")
    if not rec.get("title"):  # DOI-only / not in Europe PMC — fall back to CrossRef
        rec = {**crossref_meta(doi), **rec}
    title = args.title or re.sub(r"<[^>]+>", "", rec.get("title", "") or "")

    ladder = [
        ("europepmc_oa", lambda: try_europepmc(rec)),
        ("unpaywall", lambda: try_unpaywall(doi)),
        ("core", lambda: try_core(doi, title)),
    ]
    for method, fn in ladder:
        url = fn()
        if url:
            print(f"ACCESS\t{method}\t{url}")
            return 0

    print("NO_LEGAL_OA\t(paywalled; no OA copy via Europe PMC / Unpaywall / CORE)", file=sys.stderr)
    if not os.environ.get("CORE_API_KEY"):
        print(
            "  (set CORE_API_KEY to also try CORE — https://core.ac.uk/services/api)",
            file=sys.stderr,
        )
    print("\n--- author-request draft ---")
    print(author_request_draft(rec, doi))
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
