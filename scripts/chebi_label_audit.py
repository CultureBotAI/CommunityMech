#!/usr/bin/env python3
"""Audit CHEBI id/label consistency across community YAMLs against OAK canonical labels.

Extracts every `id: CHEBI:NNNNN` line and the immediately-following `label:` line,
then compares the in-file label to the OAK (sqlite:obo:chebi) canonical label.
Prints a report of unique (id, in-file-label) pairs that mismatch.

Usage: uv run python scripts/chebi_label_audit.py
"""

import re
import subprocess
from collections import defaultdict
from pathlib import Path

COMM = Path("kb/communities")
ID_RE = re.compile(r"^\s*id:\s*(CHEBI:\d+)\s*$")
LABEL_RE = re.compile(r"^\s*label:\s*(.+?)\s*$")

# pair -> set of files; also id -> set of in-file labels
pair_files = defaultdict(set)
id_labels = defaultdict(set)

for f in sorted(COMM.glob("*.yaml")):
    lines = f.read_text().splitlines()
    for i, ln in enumerate(lines):
        m = ID_RE.match(ln)
        if not m:
            continue
        cid = m.group(1)
        # label is normally the very next line
        lbl = None
        if i + 1 < len(lines):
            lm = LABEL_RE.match(lines[i + 1])
            if lm:
                lbl = lm.group(1)
        if lbl is None:
            continue
        pair_files[(cid, lbl)].add(f.name)
        id_labels[cid].add(lbl)

unique_ids = sorted(id_labels)
print(f"# {len(unique_ids)} unique CHEBI ids across {len(list(COMM.glob('*.yaml')))} files\n")

# Batch OAK lookup
canon = {}
proc = subprocess.run(
    ["uv", "run", "runoak", "-i", "sqlite:obo:chebi", "info", *unique_ids],
    capture_output=True,
    text=True,
)
for line in proc.stdout.splitlines():
    mm = re.match(r"^(CHEBI:\d+)\s*!\s*(.*)$", line.strip())
    if mm:
        canon[mm.group(1)] = mm.group(2).strip()


def norm(s):
    return s.strip().lower()


mismatches = []
for (cid, lbl), files in sorted(pair_files.items()):
    c = canon.get(cid)
    if c is None or c == "" or c.lower() in ("none", "obsolete"):
        mismatches.append((cid, lbl, c or "(NO LABEL / not found)", sorted(files)))
    elif norm(lbl) != norm(c):
        mismatches.append((cid, lbl, c, sorted(files)))

print(f"# {len(mismatches)} mismatching (id,label) pairs\n")
print(f"{'CHEBI id':<14}{'in-file label':<38}{'OAK canonical label':<40}files")
print("-" * 130)
for cid, lbl, c, files in mismatches:
    fl = ",".join(b.replace(".yaml", "") for b in files)
    if len(fl) > 60:
        fl = fl[:57] + "..."
    print(f"{cid:<14}{lbl[:37]:<38}{c[:39]:<40}{fl}")
