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


class _LookupFailed(str):
    """An Unpaywall lookup that did not complete, carrying why.

    A `str` subclass so it stays printable, but a distinct type so callers can
    tell it from a URL and from `None`. The three states a caller needs are
    genuinely different (#589): an OA location, a confirmed absence, and no
    answer at all — collapsing the last two into `None` is what made the script
    report an outage as a property of the paper.
    """


class _NoEmailConfigured(str):
    """UNPAYWALL_EMAIL is unset, so no lookup was attempted."""


_NO_EMAIL = _NoEmailConfigured("")


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


class _NoFullTextServedError(Exception):
    """Europe PMC says the paper is OA, then 404s on its full text (#590).

    A stable inconsistency in Europe PMC's own metadata, not an outage:
    `isOpenAccess: Y` and `inEPMC: Y` from the search endpoint, and a 404 from
    `fullTextXML` for the very same PMCID. Distinguished because it is a
    *verdict* — there is nothing to retry — and #587 would otherwise report it
    as "no verdict", inflating the count it added to make under-retrieval
    visible. The mirror of the bug that PR fixed.
    """


def _fulltext(pmcid: str) -> str:
    try:
        return _fulltext_xml(pmcid)
    except urllib.error.HTTPError as exc:
        if exc.code == 404:
            raise _NoFullTextServedError(pmcid) from exc
        raise


def _fulltext_xml(pmcid: str) -> str:
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
    """Where an OA copy of this DOI lives, per Unpaywall — in one of four states.

    Only used to tell the curator where the text is when Europe PMC has no full
    text. Requires UNPAYWALL_EMAIL; the API 422s on placeholder addresses.

    Returns:
        * a URL — Unpaywall knows of an OA copy;
        * ``None`` — Unpaywall answered, and knows of none. **A fact about the
          paper.**
        * ``_LookupFailed`` — the lookup did not complete. *Not* a fact about
          the paper, and the distinction is the whole point of #589: these last
          two were both ``None``, so an outage was reported as a paywall;
        * ``_NoEmailConfigured`` — no lookup was attempted at all.

    The type is annotated ``str | None`` because both sentinel classes subclass
    ``str``; callers must branch with ``isinstance``, not truthiness, since a
    ``_LookupFailed`` carrying a message is truthy and would otherwise be
    mistaken for a URL.
    """
    import json
    import os

    email = os.environ.get("UNPAYWALL_EMAIL")
    if not email:
        return _NO_EMAIL
    try:
        url = f"https://api.unpaywall.org/v2/{urllib.parse.quote(doi)}?email={urllib.parse.quote(email)}"
        data = json.loads(_get(url))
    except (urllib.error.URLError, TimeoutError, ValueError) as exc:
        # Not `None` (#589). `None` is this function's way of saying "Unpaywall
        # knows of no OA copy" — a fact about the paper. A timeout or a 500 is
        # the absence of an answer, and reporting it as the former told the
        # curator to go set an env var they had already set. Narrowed from a
        # bare `except Exception` at the same time, so a genuine bug in here
        # surfaces instead of being swallowed as "no OA copy".
        return _LookupFailed(f"{type(exc).__name__}: {exc}")
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
        head = f"{doi}: no Europe PMC full text (pmcid={pmcid}, oa={oa})"
        where = _unpaywall_location(doi)
        # Three outcomes, three messages (#589). Previously the last two were
        # both `None` and both produced the "set UNPAYWALL_EMAIL" advice — wrong
        # for anyone who had set it, and it filed an outage as a paywall.
        if isinstance(where, _LookupFailed):
            return (
                f"[error] {head}; the Unpaywall lookup did not complete "
                f"({where}) — whether an OA copy exists is unknown, retry"
            )
        if isinstance(where, _NoEmailConfigured):
            return f"[skip] {head}; set UNPAYWALL_EMAIL to look up an OA location"
        if where:
            return (
                f"[skip] {head}; Unpaywall OA location is {where} — retrieve by "
                f"hand if the publisher blocks automated download"
            )
        return f"[skip] {head}; Unpaywall knows of no OA copy"
    try:
        text = _fulltext(pmcid)
    except _NoFullTextServedError:  # same verdict as the PMID path (#590)
        return (
            f"[skip] {doi}: Europe PMC reports OA ({pmcid}) but serves no "
            f"full-text XML; try another route"
        )
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
    try:
        text = _fulltext(pmcid)
    except _NoFullTextServedError:
        # Worded distinctly from the `not open-access` skip above, because the
        # two call for different follow-up (#590): this paper has an OA copy
        # that Europe PMC simply is not serving, so an Unpaywall lookup or a
        # `--from-file` retrieval may still get it.
        return (
            f"[skip] {pmid}: Europe PMC reports OA ({pmcid}) but serves no "
            f"full-text XML; try another route"
        )
    sep = f"\n\n{MARKER} (Europe PMC {pmcid}) =====\n\n"
    cache.write_text(
        cache.read_text(encoding="utf-8").rstrip() + sep + text + "\n", encoding="utf-8"
    )
    return f"[cached] {pmid}: appended {len(text)} chars of OA full text from {pmcid}"


def _sweep(refs: list[str], handler) -> int:
    """Run `handler` over every ref, and report how many produced no verdict.

    Shared by both of `main`'s branches on purpose (#588). Each reference is
    independent, so one failure must not cost the rest their attempt: before
    this, an unhandled HTTPError on item 3 of 20 left items 4-20 unattempted,
    and the output gave no way to tell "not attempted" from "attempted and
    unavailable" — so a transient outage silently shrank the sweep and its tail
    was recorded as unretrievable (#586).

    Extracted rather than copied into the second loop. Copying is how the two
    branches drifted in the first place: the `--from-file` path kept the
    original bare loop for the entire life of the network-path fix.
    """
    failed = []
    for ref in refs:
        try:
            message = handler(ref)
            print(message)
            # A handler can also *return* a no-verdict outcome rather than
            # raising — `cache_one_doi` does, when the Unpaywall lookup fails
            # (#589). Both must reach the exit code, or the sweep prints
            # `[error]` and still reports success.
            if message.startswith("[error]"):
                failed.append(ref)
        except Exception as exc:  # noqa: BLE001 - one bad ref must not end the sweep
            # `[error]`, never `[skip]`: a skip is a verdict about the paper, an
            # error is the absence of one. Anything reading this output to build
            # a "needs access" list must be able to tell them apart.
            print(f"[error] {ref}: {type(exc).__name__}: {exc}")
            failed.append(ref)
    if failed:
        print(
            f"[error] {len(failed)} of {len(refs)} reference(s) ended without a verdict: {failed}"
        )
        return 1
    return 0


def _fetch(ref: str) -> str:
    if ref.lower().startswith("doi:") or ref.startswith("10."):
        return cache_one_doi(ref)
    return cache_one(ref)


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
        path = Path(args[i + 1])
        return _sweep(args[:i], lambda ref: cache_from_file(ref, path))
    return _sweep(args, _fetch)


if __name__ == "__main__":
    raise SystemExit(main())
