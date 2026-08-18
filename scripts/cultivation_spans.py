#!/usr/bin/env python3
"""Show the Methods spans that would support growth_media / cultivation_setup (#183).

#183 is gated on "once full text is accessible", and much of it now is: 52 of the
75 records lacking cultivation conditions have at least one reference with cached
full text. Deciding which of those are genuinely enrichable means reading the
Methods, not counting keywords — a paper's Discussion says "incubated" about
someone else's work, and `growth_media: []` has been written for records whose
medium is spelled out in a table.

This prints, per reference, the spans around cultivation cues so a curator can
see whether the source actually describes growing this community. It extracts
nothing into YAML on purpose: the judgement of whether a span describes *this*
study is the part that cannot be automated, and a tool that guessed would
produce exactly the wrong-assertion problem it is meant to fix.

Snippets copied from this output are byte-exact, which matters: the extracted
text uses U+2009 THIN SPACE between value and unit ("200 rpm", "48 h"), so a
retyped quote fails to match the cache while looking identical (#622-adjacent).

Usage:
    uv run python scripts/cultivation_spans.py kb/communities/Foo.yaml [--width 320]
    uv run python scripts/cultivation_spans.py --list-candidates
"""

from __future__ import annotations

import pathlib
import re
import sys

import yaml

REPO = pathlib.Path(__file__).resolve().parent.parent
COMMUNITIES = REPO / "kb/communities"
CACHE = REPO / "references_cache"
FULL_TEXT_MARKERS = ("===== OPEN-ACCESS FULL TEXT", "Full text (re-fetched")

# Ordered roughly by how strongly each implies "this study grew it".
CUES = (
    r"was operated",
    r"were operated",
    r"incubated (?:at|in|for|under)",
    r"grown (?:at|in|on|under)",
    r"cultivated",
    r"culture medium",
    r"growth medium",
    r"synthetic medi(?:um|a)",
    r"medium contain",
    r"media contain",
    r"amended with",
    r"inoculated with",
    r"microcosm",
    r"mesocosm",
    r"serum bottle",
    r"headspace",
    r"growth chamber",
    r"greenhouse",
    r"EcoFAB",
    r"light(?:/|:| )dark",
    r"photoperiod",
    r"rpm\b",
    r"°\s?C",
    r"pH (?:was|of|\d)",
)


def cached_full_text(reference: str) -> str:
    """The cached body for a reference, but only if it holds real full text.

    Both markers, because knowing only one of them has twice led to real full
    text being classified as a stub and deleted.
    """
    stem = reference.strip().replace(":", "_").replace("/", "_")
    for suffix in (".md", ".txt"):
        path = CACHE / f"{stem}{suffix}"
        if path.is_file():
            body = path.read_text(errors="replace")
            if any(marker in body for marker in FULL_TEXT_MARKERS):
                return body
    return ""


def references_of(node, found: set[str]) -> None:
    if isinstance(node, dict):
        if isinstance(node.get("reference"), str):
            found.add(node["reference"])
        for value in node.values():
            references_of(value, found)
    elif isinstance(node, list):
        for value in node:
            references_of(value, found)


def spans(text: str, width: int) -> list[tuple[str, str]]:
    """(cue, span) pairs, de-duplicated by overlapping window."""
    out: list[tuple[str, str]] = []
    taken: list[tuple[int, int]] = []
    for cue in CUES:
        for match in re.finditer(cue, text, re.IGNORECASE):
            start = max(0, match.start() - width // 3)
            end = min(len(text), match.end() + width)
            if any(start < b and a < end for a, b in taken):
                continue
            taken.append((start, end))
            out.append((match.group(0), text[start:end]))
    return out


def lacks_conditions(document: dict) -> bool:
    return not (document.get("growth_media") or document.get("cultivation_setup"))


def list_candidates() -> int:
    print("# records lacking growth_media AND cultivation_setup, with cached full text")
    for path in sorted(COMMUNITIES.glob("*.yaml")):
        document = yaml.safe_load(path.read_text()) or {}
        if not lacks_conditions(document):
            continue
        found: set[str] = set()
        references_of(document, found)
        with_text = sorted(r for r in found if cached_full_text(r))
        if not with_text:
            continue
        empty = "growth_media: []" if "growth_media" in document else "no growth_media key"
        print(f"  {path.name:58} {document.get('id', ''):22} {empty:22} {','.join(with_text)}")
    return 0


def main() -> int:
    argv = sys.argv[1:]
    if "--list-candidates" in argv:
        return list_candidates()
    if not argv:
        print(__doc__)
        return 2
    width = int(argv[argv.index("--width") + 1]) if "--width" in argv else 320
    path = pathlib.Path(argv[0])
    if not path.is_file():
        path = COMMUNITIES / argv[0]
    document = yaml.safe_load(path.read_text()) or {}

    found: set[str] = set()
    references_of(document, found)
    print(f"# {path.name}  ({document.get('id', '')})")
    print(
        f"# origin={document.get('community_origin')} category={document.get('community_category')}"
    )
    print(f"# lacks conditions: {lacks_conditions(document)}")

    for reference in sorted(found):
        text = cached_full_text(reference)
        if not text:
            print(f"\n## {reference} — NO cached full text (absence is not reportable from here)")
            continue
        hits = spans(text, width)
        print(f"\n## {reference} — {len(text)} chars cached, {len(hits)} cultivation spans")
        for cue, span in hits:
            print(f"\n  [{cue}] {span!r}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
