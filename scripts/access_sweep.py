#!/usr/bin/env python3
"""Deep legal access sweep for the paywalled #183 residual (no gray-area sources).

`fulltext_access.py` runs the per-record ladder (Europe PMC OA -> Unpaywall ->
CORE -> author draft). This script goes one layer wider for the records that
ladder left as NO_LEGAL_OA: it queries **OpenAlex**, which lists *every* OA
location it knows (not just Unpaywall's single `best_oa_location`), so it catches
green/preprint copies (bioRxiv, institutional repositories, PMC mirrors) that the
single-best heuristic misses. CORE is tried too when $CORE_API_KEY is set.

For every residual it records:
  - any OA PDF / landing URLs discovered (OpenAlex locations + CORE), and
  - the publisher landing URL (doi.org / PubMed) as a last-resort pointer for a
    curator with institutional access to fetch the PDF by hand.

Sci-Hub and other gray-area mirrors are deliberately NOT used (the sibling
CultureMech `literature_verifier` gates them off too; we keep them off).

Reads the residual list from the "Need author-request" section of
reports/fulltext_access_183.md. Writes reports/missing_pdfs.md.

Usage:
    uv run python scripts/access_sweep.py
"""

from __future__ import annotations

import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

EMAIL = os.environ.get("UNPAYWALL_EMAIL", "marcinjoachimiak@gmail.com")
UA = {"User-Agent": f"CommunityMech-access/1.0 (mailto:{EMAIL})"}
ROOT = Path(__file__).resolve().parent.parent
RESIDUAL_MD = ROOT / "reports" / "fulltext_access_183.md"
AUTHOR_DIR = ROOT / "reports" / "author_requests"
OUT_MD = ROOT / "reports" / "missing_pdfs.md"


def _get_json(url: str, headers: dict | None = None):
    if not url.startswith("https://"):
        return None
    req = urllib.request.Request(url, headers={**UA, **(headers or {})})  # noqa: S310
    try:
        with urllib.request.urlopen(req, timeout=30) as r:  # noqa: S310
            return json.load(r)
    except Exception:
        return None


def parse_residuals() -> list[dict]:
    """Records under 'Need author-request': `CommunityMech:NNN  <ref>`."""
    text = RESIDUAL_MD.read_text()
    tail = text.split("Need author-request", 1)[-1]
    out = []
    for m in re.finditer(r"CommunityMech:(\d+)\s+((?:PMID|doi):\S+)", tail):
        cid, ref = m.group(1), m.group(2)
        pmid = ref.split(":", 1)[1] if ref.lower().startswith("pmid") else None
        doi = ref.split(":", 1)[1] if ref.lower().startswith("doi") else None
        # human title from the author-request filename (NNN_Title.txt)
        title = ""
        for f in AUTHOR_DIR.glob(f"{cid}_*.txt"):
            title = f.stem.split("_", 1)[-1].replace("_", " ")
            break
        out.append({"cid": cid, "ref": ref, "pmid": pmid, "doi": doi, "title": title})
    return out


def openalex_locations(pmid: str | None, doi: str | None) -> dict:
    """All OA locations OpenAlex knows, plus the canonical doi/landing."""
    if doi:
        key = f"doi:{doi}"
    elif pmid:
        key = f"pmid:{pmid}"
    else:
        return {}
    d = _get_json(
        f"https://api.openalex.org/works/{urllib.parse.quote(key, safe=':')}?mailto={EMAIL}"
    )
    if not d:
        return {}
    oa_urls = []
    for loc in d.get("locations") or []:
        if not loc.get("is_oa"):
            continue
        for u in (loc.get("pdf_url"), loc.get("landing_page_url")):
            if u and u not in oa_urls:
                oa_urls.append(u)
    src = d.get("primary_location") or {}
    return {
        "oa_status": (d.get("open_access") or {}).get("oa_status"),
        "oa_urls": oa_urls,
        "landing": src.get("landing_page_url"),
        "host": ((src.get("source") or {}).get("display_name")),
        "resolved_doi": (d.get("doi") or "").replace("https://doi.org/", "") or None,
    }


def biorxiv_pdf(doi: str | None) -> str | None:
    """bioRxiv/medRxiv preprints are OA; OpenAlex lags on the newest ones (esp. the
    2025+ `10.64898` prefix), so probe the preprint API directly for a PDF URL."""
    if not doi:
        return None
    prefix = doi.split("/", 1)[0]
    if prefix not in ("10.1101", "10.64898"):
        return None
    for server in ("biorxiv", "medrxiv"):
        d = _get_json(f"https://api.biorxiv.org/details/{server}/{doi}")
        coll = (d or {}).get("collection") or []
        if coll:
            ver = coll[-1].get("version", "1")
            return f"https://www.{server}.org/content/{doi}v{ver}.full.pdf"
    return None


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


def landing_url(rec: dict, resolved_doi: str | None) -> str:
    doi = rec["doi"] or resolved_doi
    if doi:
        return f"https://doi.org/{doi}"
    if rec["pmid"]:
        return f"https://pubmed.ncbi.nlm.nih.gov/{rec['pmid']}/"
    return "(no identifier)"


def main() -> int:
    residuals = parse_residuals()
    core_on = bool(os.environ.get("CORE_API_KEY"))
    print(
        f"Sweeping {len(residuals)} residuals (CORE {'ON' if core_on else 'off'})...",
        file=sys.stderr,
    )

    recovered, still_missing = [], []
    for r in residuals:
        oa = openalex_locations(r["pmid"], r["doi"])
        doi = r["doi"] or oa.get("resolved_doi")
        urls = list(oa.get("oa_urls") or [])
        for extra in (biorxiv_pdf(doi), try_core(doi, r["title"])):
            if extra and extra not in urls:
                urls.append(extra)
        r["oa_status"] = oa.get("oa_status")
        r["oa_urls"] = urls
        r["host"] = oa.get("host")
        r["landing"] = landing_url(r, oa.get("resolved_doi"))
        (recovered if urls else still_missing).append(r)
        status = f"OA:{len(urls)}" if urls else "paywalled"
        print(f"  {r['cid']} {r['ref']:<28} {status:<10} {r['host'] or ''}", file=sys.stderr)
        time.sleep(0.2)  # be polite to OpenAlex

    lines = [
        "# Missing-PDF pointers for the paywalled #183 residual",
        "",
        "Legal access sweep (OpenAlex all-OA-locations + Unpaywall + "
        f"CORE{'  [key set]' if core_on else '  [no key — rerun with $CORE_API_KEY]'}). "
        "No gray-area sources (Sci-Hub etc. excluded by policy).",
        "",
        f"- **Newly-recovered OA copy: {len(recovered)} / {len(residuals)}** "
        "(green/preprint/repository copy found via OpenAlex all-locations or the "
        "bioRxiv/medRxiv API that the single-best Unpaywall pick missed; bioRxiv PDFs "
        "are OA but Cloudflare-gated to bots — open in a browser)",
        f"- **Still no legal OA: {len(still_missing)} / {len(residuals)}** — publisher "
        "landing URL listed for a curator with institutional access to fetch by hand.",
        "",
    ]
    if recovered:
        lines += ["## Newly-recovered OA copies (enrich these)", ""]
        for r in recovered:
            lines.append(f"### {r['cid']} — {r['title']}")
            lines.append(f"- ref: `{r['ref']}`  ·  host: {r['host'] or '?'}")
            for u in r["oa_urls"]:
                lines.append(f"- OA: <{u}>")
            lines.append("")
    lines += ["## Still paywalled — institutional-access fetch list", ""]
    for r in still_missing:
        lines.append(
            f"- **{r['cid']}** {r['title']}  ·  `{r['ref']}`  ·  landing: <{r['landing']}>"
        )
    lines.append("")

    OUT_MD.write_text("\n".join(lines))
    rel = OUT_MD.relative_to(ROOT)
    print(
        f"\nWrote {rel}: {len(recovered)} recovered, {len(still_missing)} paywalled",
        file=sys.stderr,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
