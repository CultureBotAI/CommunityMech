#!/usr/bin/env python3
"""Append open-access full text to a PMID's reference cache (for snippet validation).

`references_cache/PMID_<id>.txt` normally holds only the PubMed abstract, so
`just validate-references` can't verify evidence snippets taken from a paper's
Methods/Results. For **open-access** papers this fetches the full text from Europe
PMC and appends it to the cache file, so full-text snippets validate as substrings.

Only OA papers with full text in Europe PMC are cached; others are reported and
skipped (never fabricated). Idempotent: a file that already carries the appended
full-text marker is left unchanged.

Usage:
    PYTHONPATH=src uv run python scripts/cache_fulltext.py PMID:36847519
    PYTHONPATH=src uv run python scripts/cache_fulltext.py 36847519 38744211
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
    for pmid in sys.argv[1:]:
        print(cache_one(pmid))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
