"""Extract the primary final16 roster and candidate label context for #1548.

2026-11-15: reads retained Coker XML and current EcoFAB YAML, emits JSON only.
Candidate taxonomy is unverified context, never a species/stock identity verdict.
No network, source mutations, or canonical writes.
"""

import hashlib
import json
import re
from pathlib import Path

import yaml
from defusedxml import ElementTree

ROOT = Path(__file__).resolve().parents[2]
XML = ".temp/phase2-science-20261115/lbnl-retained/ecofab-relations/PMC9765266.xml"
NEIGHBOR = "kb/communities/EcoFAB_Ring_Trial_SynCom17.yaml"


def main():
    raw = (ROOT / XML).read_bytes()
    article = ElementTree.fromstring(raw)
    identifiers = {
        element.attrib["pub-id-type"]: element.text for element in article.findall(".//article-id")
    }
    if (
        identifiers.get("pmid") != "36472419"
        or identifiers.get("doi") != "10.1128/msystems.00951-22"
    ):
        raise ValueError("retained XML has the wrong paper identity")
    section = article.find(".//sec[@id='s4-1']")
    paragraphs = ["".join(paragraph.itertext()) for paragraph in section.findall("p")]
    if len(paragraphs) != 1:
        raise ValueError("isolate-selection source structure changed")
    matches = re.findall(r"DSM\s+(\d+)\s+\((\w+)\s+(OA[EPS]\d+)\)", paragraphs[0])
    if len(matches) != 16 or len({item[2] for item in matches}) != 16:
        raise ValueError("expected sixteen unique final source stocks")
    neighbor_bytes = (ROOT / NEIGHBOR).read_bytes()
    neighbor = yaml.safe_load(neighbor_bytes)
    stocks = {
        item.get("strain_designation", {}).get("strain_name"): item for item in neighbor["taxonomy"]
    }
    rows = []
    for deposit, genus, strain in matches:
        candidate = stocks.get(strain)
        rows.append(
            {
                "source_genus": genus,
                "strain": strain,
                "deposit": f"DSM {deposit}",
                "source_quote": f"DSM {deposit} ({genus} {strain})",
                "candidate_neighbor_term": (
                    candidate.get("taxon_term", {}).get("term") if candidate else None
                ),
                "candidate_status": "Unverified neighbor context; validate current genus/rank and preserve source name.",
            }
        )
    if {row["strain"] for row in rows} & {"OAE603", "OAE905", "WCS417"}:
        raise ValueError("a nonfinal stock entered the final16 roster")
    print(
        json.dumps(
            {
                "source": XML,
                "source_sha256": hashlib.sha256(raw).hexdigest(),
                "primary_identifiers": identifiers,
                "locator": "Methods / Isolate selection / s4-1",
                "neighbor": NEIGHBOR,
                "neighbor_sha256": hashlib.sha256(neighbor_bytes).hexdigest(),
                "roster": rows,
                "source_limits": [
                    "The paper explicitly calls these novel strains from unknown species.",
                    "The final16 roster excludes Sphingomonas OAE905 and Pseudomonas simiae WCS417.",
                    "Earlier18/17 assays do not establish that final16 shares the same membership or outcomes.",
                    "A primary-paper deposit assertion is not independent verification of a current collection page.",
                ],
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
