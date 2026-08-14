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
import time
import urllib.error
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


_RETRY_STATUS = frozenset({429, 500, 502, 503, 504})
_ATTEMPTS = 4


def _get(url: str, *, attempts: int = _ATTEMPTS, sleep=time.sleep) -> bytes:
    """GET with backoff on the statuses Europe PMC returns while it is busy.

    Retried because a 503 here is not an answer (#586). The same reference
    returned 504, then 503, then a clean ``not open-access`` verdict inside
    ninety seconds; only the third was true. Without the retry the transient
    ones reach the caller as a hard failure and get recorded as "this paper
    cannot be retrieved" — a property of the network mistaken for a property of
    the source, the same confusion as #577/#578.

    Retries only transient statuses. A 404 is a real answer and is raised at
    once; retrying it would just slow the sweep down to reach the same verdict.
    """
    for attempt in range(attempts):
        try:
            # EPMC is a fixed trusted https host; url is not user-controlled.
            req = urllib.request.Request(url, headers=_HEADERS)  # noqa: S310
            with urllib.request.urlopen(req, timeout=60) as r:  # noqa: S310
                return r.read()
        except urllib.error.HTTPError as exc:
            if exc.code not in _RETRY_STATUS or attempt == attempts - 1:
                raise
        except (urllib.error.URLError, TimeoutError):
            if attempt == attempts - 1:
                raise
        sleep(2**attempt)
    raise AssertionError("unreachable")  # pragma: no cover


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


def _text_from_file(path: Path) -> str:
    """Extract text from a curator-supplied PDF/HTML/text file.

    The escape hatch for OA papers no API can retrieve — e.g. a publisher that
    returns HTTP 403 to programmatic download (MDPI). The curator downloads the
    paper by hand and points this at it; nothing is fetched or invented.
    """
    if path.suffix.lower() == ".pdf":
        try:
            from pypdf import PdfReader  # noqa: PLC0415
        except ImportError as exc:  # pragma: no cover - depends on env
            raise SystemExit(
                f"reading {path.name} needs pypdf, which is not a project dependency.\n"
                f"Run it ad hoc instead:\n"
                f"  uv run --with pypdf python scripts/cache_fulltext.py ... --from-file {path}"
            ) from exc
        reader = PdfReader(str(path))
        text = "\n".join((page.extract_text() or "") for page in reader.pages)
    else:
        text = path.read_text(encoding="utf-8", errors="replace")
        if path.suffix.lower() in {".html", ".htm", ".xml"}:
            text = re.sub(_INLINE, "", text)
            text = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", text, flags=re.S | re.I)
            text = html.unescape(re.sub(r"<[^>]+>", " ", text))
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n\s*\n+", "\n\n", text)
    return text.strip()


def cache_from_file(ref: str, path: Path) -> str:
    """Append curator-supplied full text to the cache entry for `ref`."""
    if ref.lower().startswith("doi:") or ref.startswith("10."):
        doi = re.sub(r"^doi:", "", ref.strip(), flags=re.IGNORECASE)
        cache = _doi_cache_path(doi)
        label = doi
    else:
        cache = _cache_path(ref.replace("PMID:", "").strip())
        label = ref
    if not path.exists():
        return f"[skip] {label}: no such file {path}"
    if cache.exists() and MARKER in cache.read_text(encoding="utf-8"):
        return f"[ok] {label}: full text already cached"
    text = _text_from_file(path)
    if len(text) < 500:
        return f"[skip] {label}: only {len(text)} chars extracted from {path.name}; refusing"
    sep = f"\n\n{MARKER} (local file {path.name}) =====\n\n"
    head = cache.read_text(encoding="utf-8").rstrip() if cache.exists() else ""
    cache.write_text(head + sep + text + "\n", encoding="utf-8")
    return f"[cached] {label}: appended {len(text)} chars from {path.name} -> {cache.name}"


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
    args = sys.argv[1:]
    if "--from-file" in args:
        i = args.index("--from-file")
        if i + 1 >= len(args) or i == 0:
            print("usage: cache_fulltext.py <PMID|DOI> --from-file <path>")
            return 2
        refs = args[:i]
        path = Path(args[i + 1])
        for ref in refs:
            print(cache_from_file(ref, path))
        return 0
    # Each reference is independent, so one failure must not cost the rest their
    # attempt (#586). Before this, an unhandled HTTPError on item 3 of 20 left
    # items 4-20 unattempted, and the output gave no way to tell "not attempted"
    # from "attempted and unavailable" -- so a transient outage silently shrank
    # the sweep and its tail was recorded as unretrievable.
    failed = []
    for ref in args:
        try:
            if ref.lower().startswith("doi:") or ref.startswith("10."):
                print(cache_one_doi(ref))
            else:
                print(cache_one(ref))
        except Exception as exc:  # noqa: BLE001 - one bad ref must not end the sweep
            # `[error]`, never `[skip]`: a skip is a verdict about the paper, an
            # error is the absence of one. Anything reading this output to build
            # a "needs access" list must be able to tell them apart.
            print(f"[error] {ref}: {type(exc).__name__}: {exc}")
            failed.append(ref)
    if failed:
        print(
            f"[error] {len(failed)} of {len(args)} reference(s) ended without a verdict: {failed}"
        )
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
