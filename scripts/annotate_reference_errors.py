#!/usr/bin/env python3
"""Correct `validate-references`' misleading "only abstract available" note (#496).

The upstream validator annotates every failed match with

    (note: only abstract available for PMID:X, full text may contain this excerpt)

which is a claim about the **cache**. What it actually knows is "I could not
match this snippet". When the full text *is* cached the note is simply false, and
it sends the reader to `cache-fulltext` after a gap that does not exist — that
cost a full canary cycle on #259.

The wording lives upstream in `linkml-reference-validator`, so this does not fix
it there. It reads the validator's output and replaces the note with what the
cache actually supports, which is the part a curator needs in order to act:

  no full-text marker   -> the note is TRUE; fetching may help
  full text cached, and
    the snippet elides with ".." or "…"  -> a legitimate stitched quote that this
        validator cannot match by construction; `evidence_snippet_audit.py`
        accepts it, so nothing needs doing
    a near-miss on spacing              -> a PDF/XML extraction artefact
        (RENDERING); do NOT edit the snippet to match the cache
    otherwise                           -> genuinely absent from the full text;
        this is the case worth a curator's time

Usage:
    just validate-references FILE 2>&1 | uv run python scripts/annotate_reference_errors.py
"""

from __future__ import annotations

import pathlib
import re
import sys

REPO = pathlib.Path(__file__).resolve().parent.parent
CACHE = REPO / "references_cache"
FULL_TEXT_MARKERS = ("===== OPEN-ACCESS FULL TEXT", "Full text (re-fetched")

_NOTE = re.compile(r"\(note: only abstract available for (?P<ref>[^,]+), full text may[^)]*\)")
_SNIPPET = re.compile(r"not found as substring: '(?P<snippet>.*?)'(?:\s|$)")


def cached(reference: str) -> tuple[str, bool]:
    """(text, has_full_text) for a reference as the validator names it."""
    stem = reference.strip().replace(":", "_").replace("/", "_")
    parts, full = [], False
    for suffix in (".md", ".txt"):
        path = CACHE / f"{stem}{suffix}"
        if path.is_file():
            body = path.read_text(errors="replace")
            parts.append(body)
            full = full or any(m in body for m in FULL_TEXT_MARKERS)
    return " ".join(" ".join(parts).split()), full


def diagnose(reference: str, snippet: str) -> str:
    text, full = cached(reference)
    if not full:
        return f"only the abstract is cached for {reference}; try `just cache-fulltext {reference}`"

    flat = " ".join(snippet.split())
    if re.search(r"\.\.+|…", snippet):
        fragments = [f.strip() for f in re.split(r"\.\.+|…", flat) if f.strip()]
        if fragments and all(f in text for f in fragments):
            return (
                f"stitched quote — every fragment is in the cached full text of {reference}, "
                f"but this validator matches whole substrings only. "
                f"evidence_snippet_audit.py accepts it; nothing to do"
            )

    # A near-miss on spacing is the documented RENDERING class: the curator read
    # a rendered page and the extractor closed a subscript up, or vice versa.
    if re.sub(r"\s+", "", flat) in re.sub(r"\s+", "", text):
        return (
            f"whitespace-only difference from the cached full text of {reference} — a PDF/XML "
            f"extraction artefact (RENDERING). Do NOT edit the snippet to match the cache"
        )

    # The validator strips [bracketed] text from a snippet before matching and
    # then quotes the mangled version back (#622), so a verbatim quote of
    # "[NiFe]-hydrogenases" or "(80:20 [v/v])" arrives here looking absent. The
    # give-away is a run of two spaces where the brackets were, so split on that
    # and ask whether the surviving fragments are all present and in order —
    # the same test the elision branch uses, rather than trying to rebuild the
    # original string.
    if "  " in " ".join(snippet.split(" ")):
        fragments = [f.strip() for f in re.split(r" {2,}", snippet.strip()) if f.strip()]
        if len(fragments) > 1:
            position, ordered = 0, True
            for fragment in fragments:
                found = text.find(fragment, position)
                if found < 0:
                    ordered = False
                    break
                position = found + len(fragment)
            if ordered:
                return (
                    f"matches the cached full text of {reference} either side of the gap — this "
                    f"validator strips [bracketed] text before matching, so the quote is fine "
                    f"and the tool is not (#622)"
                )

    return f"absent from the cached full text of {reference} — worth a curator's attention"


def main() -> int:
    replaced = 0
    for line in sys.stdin:
        match = _NOTE.search(line)
        if match:
            snippet_match = _SNIPPET.search(line)
            snippet = snippet_match.group("snippet") if snippet_match else ""
            line = line.replace(match.group(0), f"(note: {diagnose(match.group('ref'), snippet)})")
            replaced += 1
        sys.stdout.write(line)
    if replaced:
        print(
            f"\n[annotate] rewrote {replaced} misleading 'only abstract available' note(s) (#496)"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
