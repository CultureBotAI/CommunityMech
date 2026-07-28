#!/usr/bin/env python3
"""Append open-access full text to a reference cache entry (for snippet validation).

`references_cache/PMID_<id>.txt` normally holds only the PubMed abstract, so
`just validate-references` can't verify evidence snippets taken from a paper's
Methods/Results. For **open-access** papers this fetches the full text from Europe
PMC and appends it to the cache file, so full-text snippets validate as substrings.

Accepts both PMIDs and DOIs. DOIs are resolved against Europe PMC by DOI, which
covers OA papers that have a PMC record even when they carry no PMID. When a DOI
has no Europe PMC full text, Unpaywall is queried so the message can name the OA
location a curator would have to retrieve by hand — some publishers (MDPI, for one)
return HTTP 403 to programmatic download, so those stay manual.

Only text actually retrieved is cached; everything else is reported and skipped
(never fabricated). Idempotent: a file that already carries the appended full-text
marker is left unchanged.

Set UNPAYWALL_EMAIL to your address to enable the Unpaywall lookup; its API
rejects placeholder addresses with HTTP 422.

Usage:
    PYTHONPATH=src uv run python scripts/cache_fulltext.py PMID:36847519
    PYTHONPATH=src uv run python scripts/cache_fulltext.py 36847519 38744211
    PYTHONPATH=src uv run python scripts/cache_fulltext.py doi:10.1128/spectrum.00941-23
"""

import html
import re
import sys
import urllib.parse
import urllib.request
from pathlib import Path

CACHE_DIR = Path(__file__).parent.parent / "references_cache"
EPMC = "https://www.ebi.ac.uk/europepmc/webservices/rest"
MARKER = "===== OPEN-ACCESS FULL TEXT"
# inline/format tags removed WITHOUT a space so "H<sub>2</sub>" -> "H2" (keeps
# chemical formulas intact for substring matching); all other tags -> a space.
_INLINE = r"</?(sub|sup|italic|bold|i|b|underline|sc|monospace|named-content|styled-content)[^>]*>"


_HEADERS = {"User-Agent": "communitymech-cache-fulltext"}


def _get(url: str) -> bytes:
    # EPMC is a fixed trusted https host; url is not user-controlled.
    req = urllib.request.Request(url, headers=_HEADERS)  # noqa: S310
    with urllib.request.urlopen(req, timeout=60) as r:  # noqa: S310
        return r.read()


def _pmcid(pmid: str) -> tuple[str | None, bool]:
    """Return (pmcid, is_open_access) for a PMID via Europe PMC, or (None, False)."""
    import json

    q = urllib.parse.quote(f"EXT_ID:{pmid} AND SRC:MED")
    data = json.loads(_get(f"{EPMC}/search?query={q}&format=json&resultType=core"))
    results = data.get("resultList", {}).get("result", [])
    if not results:
        return None, False
    r = results[0]
    return r.get("pmcid"), r.get("isOpenAccess") == "Y" and r.get("inEPMC") == "Y"


def _fulltext(pmcid: str) -> str:
    xml = _get(f"{EPMC}/{pmcid}/fullTextXML").decode("utf-8", "replace")
    xml = re.sub(_INLINE, "", xml)
    text = re.sub(r"<[^>]+>", " ", xml)
    text = html.unescape(text)
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n\s*\n+", "\n\n", text)
    return text.strip()


def _pmcid_for_doi(doi: str) -> tuple[str | None, bool]:
    """Return (pmcid, is_open_access) for a DOI via Europe PMC, or (None, False)."""
    import json

    q = urllib.parse.quote(f'DOI:"{doi}"')
    data = json.loads(_get(f"{EPMC}/search?query={q}&format=json&resultType=core"))
    results = data.get("resultList", {}).get("result", [])
    if not results:
        return None, False
    r = results[0]
    return r.get("pmcid"), r.get("isOpenAccess") == "Y" and r.get("inEPMC") == "Y"


def _unpaywall_location(doi: str) -> str | None:
    """Best OA URL for a DOI per Unpaywall, or None.

    Only used to tell the curator where the text lives when Europe PMC has no
    full text. Requires UNPAYWALL_EMAIL; the API 422s on placeholder addresses.
    """
    import json
    import os

    email = os.environ.get("UNPAYWALL_EMAIL")
    if not email:
        return None
    try:
        url = f"https://api.unpaywall.org/v2/{urllib.parse.quote(doi)}?email={urllib.parse.quote(email)}"
        data = json.loads(_get(url))
    except Exception:
        return None
    if not data.get("is_oa"):
        return None
    loc = data.get("best_oa_location") or {}
    return loc.get("url_for_pdf") or loc.get("url") or loc.get("url_for_landing_page")


def _doi_cache_path(doi: str) -> Path:
    """The cache file the reference validator reads for this DOI.

    Mirrors _cache_path: prefer the ``.md`` the validator reads, else the legacy
    ``.txt``. Matches the existing on-disk convention, e.g.
    ``DOI_10.1039_C3EE42189A.md``.
    """
    slug = doi.replace("/", "_")
    md = CACHE_DIR / f"DOI_{slug}.md"
    if md.exists():
        return md
    txt = CACHE_DIR / f"DOI_{slug}.txt"
    if txt.exists():
        return txt
    lower_md = CACHE_DIR / f"doi_{slug}.md"
    return lower_md if lower_md.exists() else md


def cache_one_doi(doi: str) -> str:
    doi = re.sub(r"^doi:", "", doi.strip(), flags=re.IGNORECASE)
    cache = _doi_cache_path(doi)
    if not cache.exists():
        return f"[skip] {doi}: no abstract cache ({cache.name}); fetch the abstract first"
    if MARKER in cache.read_text(encoding="utf-8"):
        return f"[ok] {doi}: full text already cached"
    pmcid, oa = _pmcid_for_doi(doi)
    if not pmcid or not oa:
        where = _unpaywall_location(doi)
        if where:
            return (
                f"[skip] {doi}: no Europe PMC full text (pmcid={pmcid}, oa={oa}); "
                f"Unpaywall OA location is {where} — retrieve by hand if the "
                f"publisher blocks automated download"
            )
        return (
            f"[skip] {doi}: no Europe PMC full text (pmcid={pmcid}, oa={oa}); "
            f"set UNPAYWALL_EMAIL to look up an OA location"
        )
    text = _fulltext(pmcid)
    sep = f"\n\n{MARKER} (Europe PMC {pmcid}) =====\n\n"
    cache.write_text(
        cache.read_text(encoding="utf-8").rstrip() + sep + text + "\n", encoding="utf-8"
    )
    return f"[cached] {doi}: appended {len(text)} chars of OA full text from {pmcid}"


def _cache_path(pmid: str) -> Path:
    """The cache file the reference validator actually reads for this PMID.

    linkml-reference-validator reads ``PMID_<id>.md`` and only falls back to a
    legacy ``.txt`` when no ``.md`` exists. Append full text to whichever it
    reads, otherwise the appended text is silently ignored during validation.
    """
    md = CACHE_DIR / f"PMID_{pmid}.md"
    return md if md.exists() else CACHE_DIR / f"PMID_{pmid}.txt"


def cache_one(pmid: str) -> str:
    pmid = pmid.replace("PMID:", "").strip()
    cache = _cache_path(pmid)
    if not cache.exists():
        return f"[skip] {pmid}: no abstract cache ({cache.name}); fetch the abstract first"
    if MARKER in cache.read_text(encoding="utf-8"):
        return f"[ok] {pmid}: full text already cached"
    pmcid, oa = _pmcid(pmid)
    if not pmcid or not oa:
        return f"[skip] {pmid}: not open-access in Europe PMC (pmcid={pmcid}, oa={oa})"
    text = _fulltext(pmcid)
    sep = f"\n\n{MARKER} (Europe PMC {pmcid}) =====\n\n"
    cache.write_text(
        cache.read_text(encoding="utf-8").rstrip() + sep + text + "\n", encoding="utf-8"
    )
    return f"[cached] {pmid}: appended {len(text)} chars of OA full text from {pmcid}"


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    for ref in sys.argv[1:]:
        if ref.lower().startswith("doi:") or ref.startswith("10."):
            print(cache_one_doi(ref))
        else:
            print(cache_one(ref))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
