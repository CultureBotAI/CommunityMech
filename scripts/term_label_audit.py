#!/usr/bin/env python3
"""Audit ontology id/label consistency across community YAMLs vs OAK canonical labels.

Generalises scripts/chebi_label_audit.py to all ontology prefixes used in
kb/communities (NCBITaxon, GO, ENVO, UBERON, CL, CHEBI). Extracts every
`id: <PREFIX>:NNN` line + the immediately-following `label:` line and compares
the in-file label to the OAK canonical label for that id.

Usage:
  uv run python scripts/term_label_audit.py [PREFIX ...]
  (default: GO ENVO UBERON CL ; NCBITaxon/CHEBI must be named explicitly
   because their sqlite adapters are large/slow to load)
"""
import re
import subprocess
import sys
from collections import defaultdict
from pathlib import Path

COMM = Path("kb/communities")
ADAPTER = {
    "NCBITaxon": "sqlite:obo:ncbitaxon",
    "GO": "sqlite:obo:go",
    "ENVO": "sqlite:obo:envo",
    "UBERON": "sqlite:obo:uberon",
    "CL": "sqlite:obo:cl",
    "CHEBI": "sqlite:obo:chebi",
}
LBL_RE = re.compile(r"^\s*label:\s*(.+?)\s*$")

prefixes = [a for a in sys.argv[1:] if a in ADAPTER] or ["GO", "ENVO", "UBERON", "CL"]


def norm(s):
    return " ".join(s.split()).strip().lower()


for prefix in prefixes:
    id_re = re.compile(rf"^\s*id:\s*({prefix}:\d+)\s*$")
    pair_files = defaultdict(set)
    id_labels = defaultdict(set)
    for f in sorted(COMM.glob("*.yaml")):
        lines = f.read_text().splitlines()
        for i, ln in enumerate(lines):
            m = id_re.match(ln)
            if not m or i + 1 >= len(lines):
                continue
            lm = LBL_RE.match(lines[i + 1])
            if lm:
                pair_files[(m.group(1), lm.group(1))].add(f.name)
                id_labels[m.group(1)].add(lm.group(1))

    ids = sorted(id_labels)
    if not ids:
        print(f"\n## {prefix}: no terms in corpus")
        continue
    canon = {}
    proc = subprocess.run(["uv", "run", "runoak", "-i", ADAPTER[prefix], "info", *ids],
                          capture_output=True, text=True)
    for line in proc.stdout.splitlines():
        mm = re.match(rf"^({prefix}:\d+)\s*!\s*(.*)$", line.strip())
        if mm:
            canon[mm.group(1)] = mm.group(2).strip()

    mism = []
    for (cid, lbl), files in sorted(pair_files.items()):
        c = canon.get(cid)
        if c is None or c == "" or c.lower() in ("none", "obsolete"):
            mism.append((cid, lbl, c or "(NOT FOUND)", sorted(files)))
        elif norm(lbl) != norm(c):
            mism.append((cid, lbl, c, sorted(files)))

    print(f"\n## {prefix}: {len(ids)} unique ids, {len(mism)} mismatching (id,label) pairs")
    print(f"{'id':<16}{'in-file label':<40}{'OAK canonical':<40}files")
    print("-" * 130)
    for cid, lbl, c, files in mism:
        fl = ",".join(b.replace(".yaml", "") for b in files)
        if len(fl) > 48:
            fl = fl[:45] + "..."
        print(f"{cid:<16}{lbl[:39]:<40}{c[:39]:<40}{fl}")
