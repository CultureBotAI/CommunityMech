#!/usr/bin/env python3
"""Compare named stock sets for the bounded EcoFAB/PR2102 dependency review.

2026-11-14. Inputs: retrieved Coker/Ding primary paragraphs, ring-trial S2 table,
and three maintained YAML records. Output: ignored roster-comparison.json;
supports ecofab-relations.md. No record writes, remote calls or publication.
"""

import hashlib
import json
import re
from pathlib import Path


def main() -> None:
    repo = Path(__file__).resolve().parents[2]
    work = repo / ".temp/m5-completion-20261114"
    sources = work / "ecofab-relations"
    coker_rows = json.loads((sources / "PMC9765266-paragraphs.json").read_text())
    ding_rows = json.loads((sources / "PMC13522444-paragraphs.json").read_text())
    coker = next(row for row in coker_rows if row["section"] == "Isolate selection.")
    ding = next(row for row in ding_rows if "Bacillus OAE603" in row["text"])

    def stocks(text: str) -> set[str]:
        return set(re.findall(r"\bO[A-Z]{2}\d+\b", text))

    coker_set = stocks(coker["text"].split("Sphingomonas")[0])
    ding_set = stocks(ding["text"])
    ring_path = work / "ecofab-independent/ring-s2.txt"
    ring_set = set()
    for line in ring_path.read_text().splitlines():
        if re.match(r"A\d+=", line):
            ring_set.update(stocks(line.split(" | ")[0]))
    assert (len(coker_set), len(ding_set), len(ring_set)) == (16, 16, 17)
    assert coker_set < ring_set and ding_set < ring_set
    results = {
        "coker_final16": sorted(coker_set),
        "dopamine16": sorted(ding_set),
        "ring17": sorted(ring_set),
        "ring_minus_coker": sorted(ring_set - coker_set),
        "ring_minus_dopamine": sorted(ring_set - ding_set),
        "coker_dopamine_intersection": sorted(coker_set & ding_set),
        "source_locators": {
            "coker": {k: v for k, v in coker.items() if k != "text"},
            "dopamine": {k: v for k, v in ding.items() if k != "text"},
            "ring": "S2 Table, rows2–18, columnsA/K; OAE829 row9",
        },
        "record_inputs": [],
    }
    for stem in [
        "EcoFAB_Ring_Trial_SynCom17",
        "Brachypodium_Natural_Variation_Dopamine_SynCom16",
        "LBNL_Switchgrass_Soil_SynCom16",
    ]:
        path = repo / "kb/communities" / (stem + ".yaml")
        content = path.read_bytes()
        names = re.findall(r"^\s+strain_name: (O[A-Z]{2}\d+)\s*$", content.decode(), re.MULTILINE)
        if stem.startswith("EcoFAB"):
            assert set(names) == ring_set
        if stem.startswith("Brachypodium"):
            assert set(names) == ding_set
        results["record_inputs"].append(
            {
                "path": str(path.relative_to(repo)),
                "sha256": hashlib.sha256(content).hexdigest(),
                "named_stocks": names,
            }
        )
    (sources / "roster-comparison.json").write_text(json.dumps(results, indent=2) + "\n")
    print(
        json.dumps(
            {
                "ring_minus_coker": results["ring_minus_coker"],
                "ring_minus_dopamine": results["ring_minus_dopamine"],
                "shared_coker_dopamine": len(coker_set & ding_set),
            }
        )
    )


if __name__ == "__main__":
    main()
