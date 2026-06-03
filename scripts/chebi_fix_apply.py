#!/usr/bin/env python3
"""Apply CHEBI id/label corrections across community YAMLs.

Two correction kinds, keyed by the exact (in-file id, in-file label) pair:
  REPOINT[(old_id, old_label)] = new_id   -> rewrite id to new_id, label to canon[new_id]
  RELABEL{(old_id, old_label)}            -> keep id, rewrite label to canon[old_id]

Labels are always taken from OAK's live canonical label (no hand-typed labels),
so the id and label are guaranteed consistent after the fix.

Usage: uv run python scripts/chebi_fix_apply.py [--dry-run]
"""
import re
import subprocess
import sys
from pathlib import Path

DRY = "--dry-run" in sys.argv
COMM = Path("kb/communities")
ID_RE = re.compile(r"^(\s*)id:\s*(CHEBI:\d+)\s*$")
LBL_RE = re.compile(r"^(\s*)label:\s*(.+?)\s*$")

# (old_id, old_label) -> new_id   (label will become canon[new_id])
REPOINT = {
    ("CHEBI:10106", "zinc sulfate"): "CHEBI:35176",
    ("CHEBI:131750", "vanadium dioxide"): "CHEBI:30047",
    ("CHEBI:132177", "manganese dichloride"): "CHEBI:63041",
    ("CHEBI:140503", "2'-fucosyllactose"): "CHEBI:147155",
    ("CHEBI:62122", "2'-fucosyllactose"): "CHEBI:147155",
    ("CHEBI:142816", "chitooligosaccharide"): "CHEBI:23104",
    ("CHEBI:15767", "D-glucosamine"): "CHEBI:17315",
    ("CHEBI:16775", "propane-1,3-diol"): "CHEBI:16109",
    ("CHEBI:16968", "dodecane"): "CHEBI:28817",
    ("CHEBI:27740", "violacein"): "CHEBI:131914",
    ("CHEBI:28580", "dextrin"): "CHEBI:28675",
    ("CHEBI:28930", "1-aminocyclopropane-1-carboxylate"): "CHEBI:18053",
    ("CHEBI:30073", "aluminium oxide"): "CHEBI:30187",
    ("CHEBI:30019", "vanadate(3-)"): "CHEBI:46442",
    ("CHEBI:48154", "chromate(2-)"): "CHEBI:35404",
    ("CHEBI:49595", "chromium(3+)"): "CHEBI:49544",
    ("CHEBI:32359", "lanthanum(3+)"): "CHEBI:49701",
    ("CHEBI:32998", "cerium(3+)"): "CHEBI:48782",
    ("CHEBI:33342", "ytterbium(3+)"): "CHEBI:49980",
    ("CHEBI:33372", "neodymium(3+)"): "CHEBI:229785",
    ("CHEBI:33375", "terbium(3+)"): "CHEBI:49902",
    ("CHEBI:33376", "samarium(3+)"): "CHEBI:49890",
    ("CHEBI:49648", "praseodymium(3+)"): "CHEBI:229784",
    ("CHEBI:49976", "yttrium(3+)"): "CHEBI:49962",
    ("CHEBI:33415", "copper(I) sulfide"): "CHEBI:51114",
    ("CHEBI:75219", "copper(II) sulfide"): "CHEBI:51110",
    ("CHEBI:34717", "5-(hydroxymethyl)furan-2-carbaldehyde"): "CHEBI:412516",
    ("CHEBI:35269", "1,2-dichloroethene"): "CHEBI:18882",
    ("CHEBI:39971", "1,1-dichloroethene"): "CHEBI:34031",
    ("CHEBI:36215", "shikimate"): "CHEBI:16119",
    ("CHEBI:37119", "uranium(VI)"): "CHEBI:32992",
    ("CHEBI:33395", "uranium(IV)"): "CHEBI:32995",
    ("CHEBI:37583", "sodium dihydrogen phosphate"): "CHEBI:37585",
    ("CHEBI:37686", "xylan"): "CHEBI:37166",
    ("CHEBI:3961", "cellulose"): "CHEBI:18246",
    ("CHEBI:46627", "pyrite"): "CHEBI:86471",
    ("CHEBI:51905", "pyrite"): "CHEBI:86471",
    ("CHEBI:50885", "chalcopyrite"): "CHEBI:86202",
    ("CHEBI:50831", "chalcopyrite"): "CHEBI:86202",
    ("CHEBI:48850", "N-acyl-L-homoserine lactone"): "CHEBI:55474",
    ("CHEBI:48953", "resazurin"): "CHEBI:8806",
    ("CHEBI:57307", "coproporphyrin III"): "CHEBI:27609",
    ("CHEBI:74807", "methylamine"): "CHEBI:16830",
    ("CHEBI:75314", "N-dodecanoyl-L-homoserine lactone"): "CHEBI:55555",
    ("CHEBI:71190", "cis-11-methyl-2-dodecenoic acid"): "CHEBI:81585",
    ("CHEBI:82823", "ferrihydrite"): "CHEBI:192761",
    ("CHEBI:82898", "sodium propanoate"): "CHEBI:132106",
    ("CHEBI:88613", "sodium butyrate"): "CHEBI:64103",
    ("CHEBI:32447", "L-cysteine hydrochloride"): "CHEBI:91247",
    ("CHEBI:24400", "glycoprotein"): "CHEBI:17089",
    ("CHEBI:49637", "dihydrogen"): "CHEBI:18276",
    ("CHEBI:25196", "methylmercury(1+)"): "CHEBI:49747",
    ("CHEBI:30785", "methylmercury(1+)"): "CHEBI:49747",
    ("CHEBI:18246", "chitin"): "CHEBI:17029",
    ("CHEBI:85357", "sodium sulfide"): "CHEBI:76209",
    ("CHEBI:87157", "sodium sulfide"): "CHEBI:76209",
    ("CHEBI:35222", "alkaloid"): "CHEBI:22315",
    ("CHEBI:39310", "phenanthrene"): "CHEBI:28851",
    ("CHEBI:4551", "dibenzothiophene"): "CHEBI:23681",
    # second batch
    ("CHEBI:27568", "sulfur atom"): "CHEBI:26833",
    ("CHEBI:35235", "L-cysteine"): "CHEBI:17561",
    ("CHEBI:78870", "sodium nitrate"): "CHEBI:63005",
    ("CHEBI:33083", "fluorene"): "CHEBI:28266",
    ("CHEBI:28115", "cob(I)alamin"): "CHEBI:15982",
    ("CHEBI:78320", "sodium L-lactate"): "CHEBI:232798",
    ("CHEBI:26156", "palladium atom"): "CHEBI:33363",
}

# (old_id, old_label) where id is the correct compound; relabel to canon[old_id]
RELABEL = {
    ("CHEBI:15138", "sulfide"),
    ("CHEBI:15366", "acetate"),
    ("CHEBI:28837", "octanoate"),
    ("CHEBI:30031", "succinate"),
    ("CHEBI:30746", "benzoate"),
    ("CHEBI:30772", "butyrate"),
    ("CHEBI:30769", "citrate(3-)"),
    ("CHEBI:30776", "hexanoate"),
    ("CHEBI:422", "lactate"),
    ("CHEBI:7916", "pantothenate(1-)"),
    ("CHEBI:18012", "fumarate(2-)"),
    ("CHEBI:18367", "phosphate"),
    ("CHEBI:23252", "cinnamate"),
    ("CHEBI:32374", "coumarate"),
    ("CHEBI:16094", "thiosulfate"),
    ("CHEBI:57586", "biotin"),
    ("CHEBI:49631", "gallium(3+)"),
    ("CHEBI:49713", "lithium atom"),
    ("CHEBI:28358", "lactic acid"),
    ("CHEBI:15603", "leucine"),
    ("CHEBI:16411", "indol-3-yl-acetic acid"),
    ("CHEBI:16457", "dimethylsulfoniopropionate"),
    ("CHEBI:16828", "tryptophan"),
    ("CHEBI:16899", "mannitol"),
    ("CHEBI:17045", "nitrous oxide"),
    ("CHEBI:17750", "betaine"),
    ("CHEBI:17997", "nitrogen"),
    ("CHEBI:18246", "cellulose"),
    ("CHEBI:18276", "hydrogen"),
    ("CHEBI:18385", "thiamine"),
    ("CHEBI:2181", "L-fucose"),
    ("CHEBI:23334", "cobalamin"),
    ("CHEBI:24875", "iron atom"),
    ("CHEBI:25555", "nitrogen molecular entity"),
    ("CHEBI:26401", "purine"),
    ("CHEBI:28009", "N-acetyl-D-glucosamine"),
    ("CHEBI:3312", "calcium chloride"),
    ("CHEBI:32599", "magnesium sulfate heptahydrate"),
    ("CHEBI:33229", "vitamin"),
    ("CHEBI:33364", "platinum atom"),
    ("CHEBI:34683", "disodium hydrogen phosphate"),
    ("CHEBI:36219", "lactose"),
    ("CHEBI:37585", "sodium dihydrogen phosphate"),
    ("CHEBI:4167", "D-glucose"),
    ("CHEBI:50821", "iron(II,III) oxide"),
    ("CHEBI:63036", "potassium dihydrogenphosphate"),
    ("CHEBI:82420", "3-Chloronitrobenzene"),
    ("CHEBI:9754", "tris(hydroxymethyl)aminomethane"),
    ("CHEBI:35352", "organic nitrogen compound"),
    ("CHEBI:75213", "sodium molybdate (anhydrous)"),
    ("CHEBI:31357", "carboxymethylcellulose"),
    ("CHEBI:28984", "aluminium(3+)"),
}

# Resolve canonical labels for every id we will write
need_ids = sorted({nid for nid in REPOINT.values()} | {oid for (oid, _l) in RELABEL})
proc = subprocess.run(["uv", "run", "runoak", "-i", "sqlite:obo:chebi", "info", *need_ids],
                      capture_output=True, text=True)
canon = {}
for line in proc.stdout.splitlines():
    m = re.match(r"^(CHEBI:\d+)\s*!\s*(.*)$", line.strip())
    if m:
        canon[m.group(1)] = m.group(2).strip()

# Guard: every target must have a non-empty canonical label
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
    i = 0
    while i < len(L) - 1:
        m = ID_RE.match(L[i].rstrip("\n"))
        if m:
            indent, oid = m.group(1), m.group(2)
            lm = LBL_RE.match(L[i + 1].rstrip("\n"))
            if lm:
                olbl = lm.group(2)
                key = (oid, olbl)
                if key in REPOINT:
                    nid = REPOINT[key]
                    nlbl = canon[nid]
                    out[i] = f"{indent}id: {nid}\n"
                    out[i + 1] = f"{lm.group(1)}label: {nlbl}\n"
                    changes += 1; files_touched.add(f.name)
                    per_pair[key] = per_pair.get(key, 0) + 1
                elif key in RELABEL:
                    nlbl = canon[oid]
                    out[i + 1] = f"{lm.group(1)}label: {nlbl}\n"
                    changes += 1; files_touched.add(f.name)
                    per_pair[key] = per_pair.get(key, 0) + 1
        i += 1
    if not DRY:
        f.write_text("".join(out))

print(f"{'DRY-RUN: ' if DRY else ''}{changes} line-pairs changed across {len(files_touched)} files")
print(f"{len(per_pair)} of {len(REPOINT)+len(RELABEL)} correction rules matched at least once")
unmatched = (set(REPOINT) | RELABEL) - set(per_pair)
if unmatched:
    print("\nRules that matched NOTHING (verify):")
    for k in sorted(unmatched):
        print("  ", k)
