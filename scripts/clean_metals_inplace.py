#!/usr/bin/env python3
"""Surgical removal of false-positive entries from metals_present.

The original `metal_extraction.py` used plain substring matching against
2-character element symbols ('ti' for TITANIUM, 'au' for GOLD, 'pd' for
PALLADIUM). Those symbols matched inside unrelated words like
'characteristic', 'australia', 'phosphodiesterase' and salted
`metals_present` with elements the source paper never discusses.

This script removes those false positives **only**. Specifically: for
each metal currently listed in a community's `metals_present`, if its
keyword set contains a known-ambiguous short symbol (`ti`, `au`, `pd`)
and *none* of its unambiguous keywords (full word, ionic forms with
charge characters, +ous/+ic adjectival forms) appears anywhere in the
file as a word-bounded token, the entry is removed. Everything else is
left exactly as found.

Out of scope deliberately:

- `metal_notes` and `metal_relevance` are never touched. Curator-authored
  values in those fields would otherwise be silently clobbered, and
  rewriting a multi-line YAML scalar from a key-line regex is unsafe
  (it leaves orphaned continuation lines that get re-folded into the
  new value).
- Adding new metal entries is also out of scope. The fixed extractor
  may find legitimate metals the old buggy run missed (e.g., via CHEBI
  tier-1 matching), but adding them here would surprise curators and
  conflate "fix bug" with "expand annotations." Run
  `scripts/backfill_metals.py --dry-run` to inspect missing additions.
- `rare_earth_elements_present` is left alone because no REE keyword is
  short enough to false-match the substring pattern that affects metals.

Usage:
    uv run python scripts/clean_metals_inplace.py --dry-run
    uv run python scripts/clean_metals_inplace.py

The script self-bootstraps `src/` onto `sys.path`, so PYTHONPATH does
not need to be set when invoking it directly.
"""

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from communitymech.metal_extraction import keyword_in_text

# Metals whose keyword list contains a short symbol that the old buggy
# substring matcher false-fired on. For each, the "unambiguous" tokens
# are the keywords that are safe to match with word boundaries because
# they cannot appear inside an unrelated English or scientific word.
AMBIGUOUS_METAL_KEYWORDS: dict[str, list[str]] = {
    "TITANIUM": ["titanium", "ti4+"],
    "GOLD": ["gold", "au3+"],
    "PALLADIUM": ["palladium", "pd2+"],
}


def _read_metals_block(lines: list[str]) -> tuple[int, int, list[str]] | None:
    """Locate the metals_present block. Returns (start_idx, end_idx, entries)."""
    for i, line in enumerate(lines):
        if line.rstrip("\n") == "metals_present:" or line.startswith("metals_present: "):
            inline = line.rstrip("\n").removeprefix("metals_present:").strip()
            if inline:
                # Inline scalar form (e.g., `metals_present: []`) — nothing to clean.
                return i, i + 1, []
            entries: list[str] = []
            end = i + 1
            while end < len(lines) and lines[end].startswith("- "):
                entries.append(lines[end][2:].strip())
                end += 1
            return i, end, entries
    return None


def clean_file(path: Path, dry_run: bool) -> tuple[bool, str]:
    text = path.read_text()
    lines = text.splitlines(keepends=True)
    located = _read_metals_block(lines)
    if located is None:
        return False, ""
    start, end, entries = located
    if not entries:
        return False, ""

    # Exclude the metals_present block itself when searching for evidence —
    # otherwise the `- TITANIUM` entry we're trying to validate would match
    # its own keywords and never be flagged as a false positive.
    evidence_text = "".join(lines[:start] + lines[end:])

    kept: list[str] = []
    removed: list[str] = []
    for entry in entries:
        unambig = AMBIGUOUS_METAL_KEYWORDS.get(entry)
        if unambig is None:
            kept.append(entry)
            continue
        if any(keyword_in_text(kw, evidence_text) for kw in unambig):
            kept.append(entry)
        else:
            removed.append(entry)

    if not removed:
        return False, ""

    # Rebuild only the metals_present block; everything else (including
    # metal_relevance, metal_notes, and any comments) is preserved.
    if kept:
        body = "".join(f"- {e}\n" for e in kept)
        new_block = "metals_present:\n" + body
    else:
        new_block = "metals_present: []\n"

    new_lines = lines[:start] + [new_block] + lines[end:]
    new_text = "".join(new_lines)

    summary = f"  removed: {removed}; kept: {kept}"
    if not dry_run:
        path.write_text(new_text)
    return True, summary


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    community_dir = Path("kb/communities")
    files = sorted(community_dir.glob("*.yaml"))
    changed = 0
    for f in files:
        did_change, summary = clean_file(f, dry_run=args.dry_run)
        if did_change:
            changed += 1
            print(f"{f.name}")
            print(summary)
    verb = "would change" if args.dry_run else "changed"
    print(f"\n{verb} {changed}/{len(files)} files")


if __name__ == "__main__":
    main()
