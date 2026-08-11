#!/usr/bin/env python3
"""Drop the low-value generic obsolete-GO biological_process annotations (#182).

The id-label cleanup remapped obsolete generic GO terms to the nearest valid
current term. Per the #182 decision, the *generic* ones (redox process -> the MF
oxidoreductase activity; organic-substance metabolic/catabolic -> broad parents)
add little and are dropped here. Meaningful remaps are KEPT (multi-organism ->
interspecies interaction GO:0044419, metal-ion sequestering GO:0140487, anion
transporter GO:0008509).

Matches a biological_process entry only when BOTH the remapped id AND the
obsolete-origin preferred_term match, so legitimate uses of the target terms are
untouched. Removes the 4-line entry; if that empties a biological_processes list,
removes the header line too. Text-only (no reflow).

Usage: uv run python scripts/drop_obsolete_go_bp.py [--dry-run]
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

# `python scripts/foo.py` does not put `src/` on the path.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from communitymech.curate.curation_event import (  # noqa: E402
    append_curation_event_text,
)

DRY = "--dry-run" in sys.argv
COMMUNITIES = Path("kb/communities")

# (preferred_term, remapped_id) pairs to drop.
DROP = {
    ("oxidation-reduction process", "GO:0016491"),
    ("organic substance metabolic process", "GO:0008152"),
    ("organic substance catabolic process", "GO:0009056"),
    ("aromatic compound catabolic process", "GO:0009056"),
}


def drop_file(path: Path) -> int:
    lines = path.read_text().splitlines()
    out: list[str] = []
    i, removed = 0, 0
    while i < len(lines):
        m = re.match(r"^(\s*)- preferred_term: (.+?)\s*$", lines[i])
        if m and i + 3 < len(lines):
            indent, pt = m.group(1), m.group(2)
            term_ok = re.match(rf"^{indent}  term:\s*$", lines[i + 1])
            idm = re.match(rf"^{indent}    id: (\S+)\s*$", lines[i + 2])
            label_ok = re.match(rf"^{indent}    label:", lines[i + 3])
            if term_ok and idm and label_ok and (pt, idm.group(1)) in DROP:
                i += 4  # skip the whole entry
                removed += 1
                continue
        out.append(lines[i])
        i += 1

    if not removed:
        return 0

    # Remove any biological_processes: header that no longer has list items.
    cleaned: list[str] = []
    j = 0
    while j < len(out):
        hm = re.match(r"^(\s*)biological_processes:\s*$", out[j])
        if hm:
            nxt = out[j + 1] if j + 1 < len(out) else ""
            if not re.match(rf"^{hm.group(1)}- ", nxt):  # no remaining list items
                j += 1
                continue
        cleaned.append(out[j])
        j += 1

    if not DRY:
        # Leave a trace. These edits delete curated annotations, and a deletion
        # is the case where "what did this and why" is least recoverable from
        # the record itself — the removed lines are simply not there any more
        # (#325). Text append rather than a YAML round-trip because this whole
        # module is a line editor; the shared helper owns the insertion rules
        # (#526).
        text = append_curation_event_text(
            "\n".join(cleaned) + "\n",
            curator="drop_obsolete_go_bp.py",
            action="DROP_OBSOLETE_GO_BP",
            changes=(
                f"Dropped {removed} generic obsolete-GO biological_process "
                f"annotation(s) that the id-label cleanup had remapped to "
                f"high-level parents carrying no mechanistic information (#182)."
            ),
        )
        path.write_text(text)
    return removed


def main() -> int:
    total, files = 0, 0
    for f in sorted(COMMUNITIES.glob("*.yaml")):
        n = drop_file(f)
        if n:
            files += 1
            total += n
            print(f"  -{n:2d}  {f.name}")
    tag = "[DRY] " if DRY else ""
    print(f"\n{tag}dropped {total} generic obsolete-GO entries across {files} files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
