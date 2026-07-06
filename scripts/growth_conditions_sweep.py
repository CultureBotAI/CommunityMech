#!/usr/bin/env python3
"""Prep a growth-conditions deep-research sweep over CommunityMech records.

Companion to the `add-growth-conditions` skill. This script does the *deterministic*
part of the whole-KB sweep so the (LLM) extraction agents get a ready source bundle
instead of each re-fetching:

  1. Enumerate records that lack a `growth_media` (and `cultivation_setup`) block.
  2. For each, pick the **primary reference** — the PMID/DOI cited most often in the
     record's evidence items.
  3. Fetch the Europe PMC abstract and run the legal full-text **access ladder**
     (Europe PMC OA -> Unpaywall -> CORE; else an author-request draft) via
     `fulltext_access.py`.
  4. Write one staging bundle per record under `reports/growth_conditions_sweep/`
     (abstract + access verdict + full-text URL to fetch Methods from, or the
     author-request draft) and an `INDEX.md` with per-record access status + counts.

It never edits kb/ — extraction and YAML writes are the agent's job, so a curator
can review this prep before any record changes. Access status buckets each record as
OA_FULLTEXT (Methods reachable), ABSTRACT_ONLY (paywalled; abstract-level only), or
NO_REFERENCE (no citable PMID/DOI found).

Usage:
  python scripts/growth_conditions_sweep.py --list
  python scripts/growth_conditions_sweep.py --prep                 # all missing records
  python scripts/growth_conditions_sweep.py --prep --limit 5       # first 5 (test batch)
  python scripts/growth_conditions_sweep.py --prep FILE [FILE ...]  # explicit records
"""

from __future__ import annotations

import argparse
import re
import sys
from collections import Counter
from pathlib import Path

# fulltext_access.py lives beside this script; its dir is on sys.path when run directly.
from fulltext_access import (
    author_request_draft,
    crossref_meta,
    epmc_core,
    try_core,
    try_europepmc,
    try_unpaywall,
)

REPO = Path(__file__).resolve().parent.parent
COMMUNITIES = REPO / "kb" / "communities"
OUT_DIR = REPO / "reports" / "growth_conditions_sweep"

REF_RE = re.compile(r"^\s*-?\s*reference:\s*(\S+)", re.MULTILINE)
HAS_BLOCK_RE = re.compile(r"^(growth_media|cultivation_setup):", re.MULTILINE)


def lacks_conditions(text: str) -> bool:
    """True if the record has neither a growth_media nor cultivation_setup block."""
    return not HAS_BLOCK_RE.search(text)


def candidates(explicit: list[Path] | None) -> list[Path]:
    files = explicit or sorted(COMMUNITIES.glob("*.yaml"))
    return [f for f in files if lacks_conditions(f.read_text())]


def primary_reference(text: str) -> tuple[str | None, list[tuple[str, int]]]:
    """Most-cited reference in the record, plus the frequency-ranked full list."""
    refs = [r.strip().strip("\"'") for r in REF_RE.findall(text)]
    if not refs:
        return None, []
    ranked = Counter(refs).most_common()
    return ranked[0][0], ranked


def split_ref(ref: str) -> tuple[str | None, str | None]:
    """Split a 'PMID:123' / 'doi:10.x' reference into (pmid, doi)."""
    low = ref.lower()
    if low.startswith("pmid:"):
        return ref.split(":", 1)[1].strip(), None
    if low.startswith("doi:"):
        return None, ref.split(":", 1)[1].strip()
    if ref.startswith("10."):  # bare DOI
        return None, ref
    return None, None


def access_ladder(rec: dict, doi: str | None, title: str | None) -> tuple[str, str | None]:
    """Return (method, url) for the first legal full-text hit, or ('none', None)."""
    for method, fn in (
        ("europepmc_oa", lambda: try_europepmc(rec)),
        ("unpaywall", lambda: try_unpaywall(doi)),
        ("core", lambda: try_core(doi, title)),
    ):
        url = fn()
        if url:
            return method, url
    return "none", None


def strip_html(s: str) -> str:
    return re.sub(r"<[^>]+>", "", s or "").strip()


def prep_record(path: Path) -> dict:
    """Fetch sources for one record and write its staging bundle. Returns a summary row."""
    text = path.read_text()
    ref, ranked = primary_reference(text)
    row = {"record": path.stem, "ref": ref or "—", "status": "", "method": "", "url": ""}

    if not ref:
        row["status"] = "NO_REFERENCE"
        _write_bundle(path.stem, ref, {}, ranked, "none", None, None)
        return row

    pmid, doi = split_ref(ref)
    rec = epmc_core(pmid, doi)
    doi = doi or rec.get("doi")
    if not rec.get("title") and doi:  # DOI-only / not in EPMC -> CrossRef metadata
        rec = {**crossref_meta(doi), **rec}
    title = strip_html(rec.get("title", ""))
    method, url = access_ladder(rec, doi, title)

    row["method"] = method
    row["url"] = url or ""
    row["status"] = "OA_FULLTEXT" if url else "ABSTRACT_ONLY"
    _write_bundle(path.stem, ref, rec, ranked, method, url, doi)
    return row


def _write_bundle(
    stem: str,
    ref: str | None,
    rec: dict,
    ranked: list[tuple[str, int]],
    method: str,
    url: str | None,
    doi: str | None,
) -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    title = strip_html(rec.get("title", ""))
    abstract = strip_html(rec.get("abstractText", ""))
    lines = [
        f"# Growth-conditions prep — {stem}",
        "",
        f"- **Primary reference:** `{ref or 'none found'}`",
        f"- **Title:** {title or '(unresolved)'}",
        f"- **All cited refs (freq):** {', '.join(f'{r}×{n}' for r, n in ranked) or '—'}",
    ]
    if url:
        lines += [
            f"- **Full-text access:** `{method}` — OA full text available",
            f"- **Methods URL (fetch this):** {url}",
            "  - Europe PMC XML: fetch with `curl --compressed <url>` and read the Methods.",
        ]
    else:
        lines += [
            "- **Full-text access:** `NO_LEGAL_OA` — abstract-level conditions only.",
            "  - Use only conditions stated in the abstract below; do **not** invent any.",
        ]
    lines += ["", "## Abstract", "", abstract or "_(no abstract retrieved)_", ""]
    if not url and (rec.get("title") or ref):
        lines += [
            "## Author-request draft (for closed-access follow-up)",
            "",
            "```",
            author_request_draft(rec, doi),
            "```",
            "",
        ]
    (OUT_DIR / f"{stem}.md").write_text("\n".join(lines))


def write_index(rows: list[dict]) -> Path:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    counts = Counter(r["status"] for r in rows)
    lines = [
        "# Growth-conditions sweep — prep index",
        "",
        f"- Records prepped: **{len(rows)}**",
        f"- OA full text (Methods reachable): **{counts.get('OA_FULLTEXT', 0)}**",
        f"- Abstract-only (paywalled): **{counts.get('ABSTRACT_ONLY', 0)}**",
        f"- No citable reference: **{counts.get('NO_REFERENCE', 0)}**",
        "",
        "| Record | Primary ref | Access | Method | Methods URL |",
        "|---|---|---|---|---|",
    ]
    for r in sorted(rows, key=lambda x: (x["status"], x["record"])):
        url = f"[link]({r['url']})" if r["url"] else "—"
        lines.append(
            f"| {r['record']} | `{r['ref']}` | {r['status']} | {r['method'] or '—'} | {url} |"
        )
    lines += ["", "Per-record source bundles are in this directory (`<Record>.md`)."]
    path = OUT_DIR / "INDEX.md"
    path.write_text("\n".join(lines))
    return path


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    mode = p.add_mutually_exclusive_group(required=True)
    mode.add_argument("--list", action="store_true", help="List candidate records and exit.")
    mode.add_argument("--prep", action="store_true", help="Fetch sources + write staging bundles.")
    p.add_argument(
        "files", nargs="*", type=Path, help="Explicit record paths (default: all missing)."
    )
    p.add_argument("--limit", type=int, default=0, help="Cap the number of records processed.")
    args = p.parse_args(argv)

    cand = candidates(args.files or None)
    if args.limit:
        cand = cand[: args.limit]

    if args.list:
        for f in cand:
            print(f.name)
        print(f"\n{len(cand)} record(s) lack growth_media/cultivation_setup", file=sys.stderr)
        return 0

    rows = []
    for i, f in enumerate(cand, 1):
        print(f"[sweep] ({i}/{len(cand)}) {f.stem}", file=sys.stderr)
        rows.append(prep_record(f))
    idx = write_index(rows)
    print(f"[sweep] wrote {len(rows)} bundles + {idx.relative_to(REPO)}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
