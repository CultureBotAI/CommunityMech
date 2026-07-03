#!/usr/bin/env python3
"""Remap ontology term ids+labels in community YAMLs via text-only edits.

Given a fix map {old_id: (new_id, new_canonical_label)}, rewrite every
`term:` block whose `id:` is old_id: set the id to new_id and the following
`label:` line to the new canonical label. Add/modify-only (no reflow); other
content is byte-for-byte preserved.

Usage: uv run python scripts/term_remap.py [--dry-run]
Edit FIXMAP below, then run.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

DRY = "--dry-run" in sys.argv
COMMUNITIES = Path("kb/communities")

# old_id -> (new_id, new_canonical_label)
FIXMAP: dict[str, tuple[str, str]] = {
    "GO:0055114": ("GO:0016491", "oxidoreductase activity"),
    "GO:0071704": ("GO:0008152", "metabolic process"),
    "GO:1901575": ("GO:0009056", "catabolic process"),
    "GO:0019439": ("GO:0009056", "catabolic process"),
    "GO:0051238": ("GO:0140487", "metal ion sequestering activity"),
    "GO:0051704": ("GO:0044419", "biological process involved in interspecies interaction between organisms"),
    "GO:0015103": ("GO:0008509", "monoatomic anion transmembrane transporter activity"),
}


def remap_file(path: Path) -> int:
    lines = path.read_text().splitlines()
    out, i, n = [], 0, 0
    while i < len(lines):
        line = lines[i]
        m = re.match(r"^(\s*)id: (\S+)\s*$", line)
        if m and m.group(2) in FIXMAP and i + 1 < len(lines) and re.match(r"^\s*label:", lines[i + 1]):
            new_id, new_label = FIXMAP[m.group(2)]
            indent = m.group(1)
            lab_indent = re.match(r"^(\s*)label:", lines[i + 1]).group(1)
            out.append(f"{indent}id: {new_id}")
            out.append(f"{lab_indent}label: {new_label}")
            i += 2
            n += 1
            continue
        out.append(line)
        i += 1
    if n and not DRY:
        path.write_text("\n".join(out) + "\n")
    return n


def main() -> int:
    total, files = 0, 0
    for f in sorted(COMMUNITIES.glob("*.yaml")):
        c = remap_file(f)
        if c:
            files += 1
            total += c
            print(f"  {c:2d}  {f.name}")
    print(f"\n{'[DRY] ' if DRY else ''}remapped {total} term(s) across {files} file(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
