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
ADAPTER = "sqlite:obo:ncbitaxon"
PREFIX = "NCBITaxon"

# (old_id, old_label) -> new_id   (label becomes canon[new_id])
# Replacement ids cross-checked against the kg-microbe ncbitaxon snapshot
# (/Users/marcin/.../kg-microbe/data/transformed/ontologies/ncbitaxon_nodes.tsv),
# then verified to exist in OAK's current sqlite:obo:ncbitaxon adapter.
REPOINT = {
    ("NCBITaxon:1379270", "Candidatus Nitrosotalea devanaterra"): "NCBITaxon:1078905",  # → Nitrosotalea devaniterrae (spelling correction)
    ("NCBITaxon:1380867", "Kazachstania exigua"): "NCBITaxon:34358",                    # → Maudiozyma exigua (genus rename)
    ("NCBITaxon:1655434", "Asgard group"): "NCBITaxon:1935183",                          # → Promethearchaeati (phylum rename)
    ("NCBITaxon:1798711", "Dormibacterota"): "NCBITaxon:2052312",                        # → Candidatus Dormiibacterota
    ("NCBITaxon:1930587", "Eisenbacteria"): "NCBITaxon:1817801",                         # → Candidatus Eiseniibacteriota
    ("NCBITaxon:1934217", "DPANN group"): "NCBITaxon:1783276",                           # → Nanobdellati
    ("NCBITaxon:194708",  "Ochrobactrum intermedium"): "NCBITaxon:94625",                # → Brucella intermedia (genus rename)
    ("NCBITaxon:221109",  "Ochrobactrum pituitosum"): "NCBITaxon:571256",                # → Brucella pituitosa (genus rename)
    ("NCBITaxon:2426",    "Syntrophus"): "NCBITaxon:43773",                              # → Syntrophus <bacteria> (id 2426 now points to Teredinibacter)
    ("NCBITaxon:283683",  "Clostridium straminisolvens"): "NCBITaxon:253314",            # → Acetivibrio straminisolvens (genus rename)
    ("NCBITaxon:445709",  "candidate division OP3"): "NCBITaxon:67812",                  # → Candidatus Omnitrophota
    ("NCBITaxon:655028",  "Rhizobium pusense"): "NCBITaxon:648995",                      # → Agrobacterium pusense (genus rename)
}

# (old_id, old_label) where the id is correct/current; relabel to OAK canonical.
RELABEL = {
    ("NCBITaxon:1801631", "Candidatus Micrarchaeota"),  # canon is now "Microcaldota" (same id)
}

# Intentionally left for the conf/id_label_targets.yaml exceptions list
# (not in current OAK ncbitaxon snapshot, even after kg-microbe cross-check):
#   NCBITaxon:1807132 "Candidatus Phormidium alkaliphilum"
#   NCBITaxon:3050471 "Stenotrophomonas goyi"

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
