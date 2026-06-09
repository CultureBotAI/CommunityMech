#!/usr/bin/env python3
"""Apply ontology id/label corrections across community YAMLs (generalised).

Like scripts/chebi_fix_apply.py but for any ontology prefix. Edit ADAPTER,
REPOINT and RELABEL below per run. Labels are always taken from OAK's live
canonical label, so id+label stay consistent.

  REPOINT[(old_id, old_label)] = new_id  -> rewrite id to new_id, label to canon[new_id]
  RELABEL{(old_id, old_label)}           -> keep id, rewrite label to canon[old_id]

Usage: uv run python scripts/term_fix_apply.py [--dry-run]
"""
import re
import subprocess
import sys
from pathlib import Path

DRY = "--dry-run" in sys.argv
COMM = Path("kb/communities")
ADAPTER = "sqlite:obo:envo"
PREFIX = "ENVO"

# (old_id, old_label) -> new_id   (label becomes canon[new_id])
REPOINT = {
    ("ENVO:00000035", "lake"): "ENVO:00000020",
    ("ENVO:00000044", "wetland"): "ENVO:00000043",
    ("ENVO:00000072", "mine tailing"): "ENVO:00000003",
    ("ENVO:00002001", "wastewater treatment plant"): "ENVO:00002043",
    ("ENVO:00002019", "hypersaline water"): "ENVO:00002012",
    ("ENVO:00002047", "waste water"): "ENVO:00002001",
    ("ENVO:00002149", "marine environment"): "ENVO:01000320",
    ("ENVO:00002179", "permafrost"): "ENVO:00000134",
    ("ENVO:00002186", "acid mine drainage"): "ENVO:00001997",
    ("ENVO:00002230", "regolith"): "ENVO:01000747",
    ("ENVO:00002233", "rhizosphere"): "ENVO:00005801",
    ("ENVO:00002874", "contaminated soil"): "ENVO:00002116",
    ("ENVO:01000605", "bioreactor"): "ENVO:00002123",
    ("ENVO:01000650", "mine tailings"): "ENVO:00000003",
    ("ENVO:01001063", "sulfide-rich spring"): "ENVO:00000126",
    ("ENVO:01001242", "freshwater environment"): "ENVO:01000306",
    ("ENVO:01000017", "subsurface environment"): "ENVO:01000942",
    ("ENVO:0001998", "human gut environment"): "ENVO:2100002",
    ("ENVO:00002009", "feces environment"): "ENVO:00002003",
    ("ENVO:00002359", "river sediment"): "ENVO:00002127",
}

# (old_id, old_label) where id is the correct/acceptable term; relabel to canon[old_id]
RELABEL = {
    ("ENVO:00000044", "bog"),               # canon: peatland (peat bog)
    ("ENVO:00002046", "sludge"),            # canon: activated sludge
    ("ENVO:01001405", "laboratory bioreactor"),  # canon: laboratory environment
    ("ENVO:01001405", "laboratory culture"),     # canon: laboratory environment
}

# Intentionally left for manual curation (no clean ENVO term):
#   ENVO:00000274 "soda lake" (=continental rise), ENVO:00002009 "feces environment"
#   (=obsolete), ENVO:00002229 "anaerobic environment" (=arenosol), ENVO:00002359
#   "river sediment" (=None), ENVO:0001998 "human gut environment" (=None),
#   ENVO:01001442 "phyllosphere" (=agriculture)

ID_RE = re.compile(rf"^(\s*)id:\s*({PREFIX}:\d+)\s*$")
LBL_RE = re.compile(r"^(\s*)label:\s*(.+?)\s*$")

need_ids = sorted({n for n in REPOINT.values()} | {o for (o, _l) in RELABEL})
proc = subprocess.run(["uv", "run", "runoak", "-i", ADAPTER, "info", *need_ids],
                      capture_output=True, text=True)
canon = {}
for line in proc.stdout.splitlines():
    m = re.match(rf"^({PREFIX}:\d+)\s*!\s*(.*)$", line.strip())
    if m:
        canon[m.group(1)] = m.group(2).strip()
bad = [i for i in need_ids if not canon.get(i) or canon[i].lower() in ("none", "")]
if bad:
    print("ABORT: missing canonical labels for:", bad)
    sys.exit(1)

changes = 0
files_touched = set()
per_pair = {}
for f in sorted(COMM.glob("*.yaml")):
    L = f.read_text().splitlines(keepends=True)
    out = list(L)
    for i in range(len(L) - 1):
        m = ID_RE.match(L[i].rstrip("\n"))
        if not m:
            continue
        indent, oid = m.group(1), m.group(2)
        lm = LBL_RE.match(L[i + 1].rstrip("\n"))
        if not lm:
            continue
        key = (oid, lm.group(2))
        if key in REPOINT:
            nid = REPOINT[key]
            out[i] = f"{indent}id: {nid}\n"
            out[i + 1] = f"{lm.group(1)}label: {canon[nid]}\n"
            changes += 1; files_touched.add(f.name); per_pair[key] = per_pair.get(key, 0) + 1
        elif key in RELABEL:
            out[i + 1] = f"{lm.group(1)}label: {canon[oid]}\n"
            changes += 1; files_touched.add(f.name); per_pair[key] = per_pair.get(key, 0) + 1
    if not DRY:
        f.write_text("".join(out))

print(f"{'DRY-RUN: ' if DRY else ''}{changes} line-pairs changed across {len(files_touched)} files")
print(f"{len(per_pair)} of {len(REPOINT)+len(RELABEL)} rules matched")
for k in (set(REPOINT) | RELABEL) - set(per_pair):
    print("  UNMATCHED:", k)
