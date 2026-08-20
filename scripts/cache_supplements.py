#!/usr/bin/env python3
"""Cache the text of a paper's SUPPLEMENTARY files (#653).

Open access does not mean the Methods are accessible. `SynCom_ARC_Peanut_Aflatoxin_
Nodulation` cites a fully open-access, fully cached, 30 KB article whose body says

    Co-cultured with A. flavus in liquid medium

without naming the medium, and points at "Supplementary materials (methods,
figures, tables...)". Journals using the Letter/Correspondence format routinely
put every Method there. Its supplement holds what the body omits:

    Bacteria strain was grown in LB medium for 24 h at 28 C with shaking at 200 rpm
    All plates were incubated at 28 C for 48-72 h
    ... the bacterial strain was 1x10^7 colony-forming units (CFU)/mL

No existing measure can tell that record apart from one whose Methods are
present: it has cached full text, passes the full-text-marker check, and is 30 KB.
That is why #653 called supplement retrieval the higher-value capability -- more
so than further full-text fetching, since these articles are already open.

**Supplement text is cached to its own file**, `<stem>.supplement.md`, never
appended to the article cache. Two reasons, both learned the hard way here:
`validate-references` matches snippets against the article cache, so mixing
supplement prose into it would let a snippet "validate" against text that is not
the article; and a classifier that knows only some markers has twice deleted real
full text it did not recognise. A separate file cannot be mistaken for either.

Only text actually retrieved is written -- never fabricated, and never inferred
from a filename. Idempotent: an existing supplement cache is left alone unless
--force is given.

Usage:
    uv run python scripts/cache_supplements.py PMID:42099455
    uv run python scripts/cache_supplements.py --list PMID:42099455
    uv run python scripts/cache_supplements.py --candidates
"""

from __future__ import annotations

import io
import json
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import zipfile
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
CACHE_DIR = REPO / "references_cache"
EPMC = "https://www.ebi.ac.uk/europepmc/webservices/rest"

MARKER = "===== SUPPLEMENTARY FILE TEXT"
_RETRY_STATUS = frozenset({429, 500, 502, 503, 504})
_ATTEMPTS = 4
_TIMEOUT = 120

# Members worth extracting. Images and archives carry no Methods prose; listing
# what was SKIPPED matters as much as what was read, so a curator can see that a
# PDF-only supplement was not silently treated as empty.
_TEXT_SUFFIXES = {".docx", ".txt", ".xml", ".html", ".htm"}
_BINARY_SUFFIXES = {".jpg", ".jpeg", ".png", ".gif", ".tif", ".tiff", ".zip", ".mov", ".avi"}


class _NoSupplementError(Exception):
    """Europe PMC has no supplementary files for this record."""


def _get(url: str, *, attempts: int = _ATTEMPTS, sleep=time.sleep) -> bytes:
    """Fetch with retry on the transient statuses, as cache_fulltext does (#586).

    An outage must not be recorded as a verdict: a 503 means "ask again", not
    "this paper has no supplement".
    """
    last: Exception | None = None
    for attempt in range(attempts):
        try:
            with urllib.request.urlopen(url, timeout=_TIMEOUT) as response:
                return response.read()
        except urllib.error.HTTPError as exc:
            if exc.code == 404:
                raise _NoSupplementError(f"no supplementary files at {url}") from exc
            if exc.code not in _RETRY_STATUS or attempt == attempts - 1:
                raise
            last = exc
        except (urllib.error.URLError, TimeoutError) as exc:
            if attempt == attempts - 1:
                raise
            last = exc
        sleep(2**attempt)
    raise last if last else RuntimeError("unreachable")


def pmcid_for(reference: str) -> str | None:
    """Resolve a PMID or DOI to a PMCID, which is what the endpoint keys on."""
    ref = reference.strip()
    if ref.upper().startswith("PMC"):
        return ref
    if ref.lower().startswith("doi:"):
        query = f'DOI:"{ref[4:]}"'
    else:
        query = f"EXT_ID:{ref.split(':')[-1]} AND SRC:MED"
    url = f"{EPMC}/search?query={urllib.parse.quote(query)}&format=json&resultType=core"
    payload = json.loads(_get(url).decode("utf-8", "replace"))
    for result in payload.get("resultList", {}).get("result", []):
        if result.get("pmcid"):
            return result["pmcid"]
    return None


def _docx_text(blob: bytes) -> str:
    """Paragraph text from a .docx, without adding a dependency.

    A .docx is a zip of XML; `word/document.xml` holds the body. Tags are
    stripped rather than parsed because the target is prose for substring
    matching, not structure.
    """
    with zipfile.ZipFile(io.BytesIO(blob)) as inner:
        if "word/document.xml" not in inner.namelist():
            return ""
        xml = inner.read("word/document.xml").decode("utf-8", "replace")
    # Paragraph and row ends become newlines so sentences do not run together.
    xml = re.sub(r"</w:(?:p|tr)>", "\n", xml)
    return re.sub(r"[ \t]+", " ", re.sub(r"<[^>]+>", "", xml)).strip()


def _member_text(name: str, blob: bytes) -> tuple[str, str]:
    """(text, note). An empty text with a note is a skip, not a failure."""
    suffix = Path(name).suffix.lower()
    if suffix == ".docx":
        text = _docx_text(blob)
        return text, "" if text else "docx with no word/document.xml"
    if suffix in {".txt", ".xml", ".html", ".htm"}:
        raw = blob.decode("utf-8", "replace")
        return re.sub(r"<[^>]+>", " ", raw) if suffix != ".txt" else raw, ""
    if suffix == ".pdf":
        # Deliberately not parsed: extracting PDF text needs a dependency this
        # repo does not carry, and a half-extracted Methods section is worse
        # than a stated gap -- a snippet would fail and look like bad curation.
        return "", "PDF not extracted (no PDF text extractor in this repo)"
    if suffix in _BINARY_SUFFIXES:
        return "", "binary/image, no prose"
    return "", f"unhandled type {suffix or '(none)'}"


def supplement_path(reference: str) -> Path:
    stem = reference.strip().replace(":", "_").replace("/", "_")
    return CACHE_DIR / f"{stem}.supplement.md"


def fetch_supplement(reference: str) -> tuple[str, list[str]]:
    """(combined text, per-member notes) for a reference's supplementary files."""
    pmcid = pmcid_for(reference)
    if not pmcid:
        raise _NoSupplementError(f"{reference}: no PMCID, so no Europe PMC supplement")
    blob = _get(f"{EPMC}/{pmcid}/supplementaryFiles")
    if not blob:
        raise _NoSupplementError(f"{reference}: empty supplement archive")

    chunks: list[str] = []
    notes: list[str] = []
    with zipfile.ZipFile(io.BytesIO(blob)) as archive:
        for name in sorted(archive.namelist()):
            text, note = _member_text(name, archive.read(name))
            if text.strip():
                chunks.append(f"----- {name} -----\n{text.strip()}")
                notes.append(f"{name}: {len(text.strip())} chars")
            else:
                notes.append(f"{name}: SKIPPED ({note})")
    return "\n\n".join(chunks), notes


def cache_one(reference: str, *, force: bool = False) -> str:
    path = supplement_path(reference)
    if path.is_file() and not force:
        return f"[skip] {reference}: {path.name} already cached ({path.stat().st_size} bytes)"
    text, notes = fetch_supplement(reference)
    if not text.strip():
        return f"[none] {reference}: supplement holds no extractable text -- " + "; ".join(notes)
    header = [
        f"{MARKER} ({reference}) =====",
        "",
        "Cached by scripts/cache_supplements.py (#653). This is SUPPLEMENTARY text,",
        "not the article body: validate-references matches snippets against the",
        "article cache, so nothing here is a substitute for it.",
        "",
        "Members:",
        *(f"  - {note}" for note in notes),
        "",
    ]
    path.write_text("\n".join(header) + "\n" + text + "\n", encoding="utf-8")
    return (
        f"[ok] {reference}: wrote {path.name} ({path.stat().st_size} bytes; {len(notes)} members)"
    )


def _references_of(node: object, found: set[str]) -> None:
    """Collect every `reference` value in a parsed record.

    Module level rather than a closure inside `candidates()`: closing over the
    loop's accumulator is the B023 pattern, and a walker that captured the wrong
    record's set would under-report candidates silently.
    """
    if isinstance(node, dict):
        if isinstance(node.get("reference"), str):
            found.add(node["reference"])
        for value in node.values():
            _references_of(value, found)
    elif isinstance(node, list):
        for value in node:
            _references_of(value, found)


def candidates() -> int:
    """Records lacking growth conditions whose article cache may hide its Methods."""
    import yaml

    print("# records lacking cultivation conditions, with a cached article and no supplement yet")
    for path in sorted((REPO / "kb/communities").glob("*.yaml")):
        document = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        if document.get("growth_media") or document.get("cultivation_setup"):
            continue
        refs: set[str] = set()
        _references_of(document, refs)
        pending = [r for r in sorted(refs) if not supplement_path(r).is_file()]
        if pending:
            print(f"  {path.name[:56]:56} {','.join(pending[:3])}")
    return 0


def main() -> int:
    argv = [a for a in sys.argv[1:] if a not in {"--force", "--list", "--candidates"}]
    force = "--force" in sys.argv
    if "--candidates" in sys.argv:
        return candidates()
    if not argv:
        print(__doc__)
        return 2

    failed = []
    for reference in argv:
        try:
            if "--list" in sys.argv:
                _, notes = fetch_supplement(reference)
                print(f"[list] {reference}:")
                for note in notes:
                    print(f"    {note}")
            else:
                print(cache_one(reference, force=force))
        except _NoSupplementError as exc:
            print(f"[none] {exc}")
        except Exception as exc:  # noqa: BLE001
            print(f"[error] {reference}: {type(exc).__name__}: {exc}")
            failed.append(reference)
    if failed:
        print(f"\n{len(failed)} reference(s) failed: {', '.join(failed)}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
