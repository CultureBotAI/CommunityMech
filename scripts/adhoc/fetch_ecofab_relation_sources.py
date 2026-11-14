#!/usr/bin/env python3
"""Fetch one open primary article for the EcoFAB relation dependency check.

Purpose: CommunityMech:000025/PR2102 review, 2026-11-14. Inputs: one PMCID,
anonymous Europe PMC fullTextXML endpoint. Outputs: raw XML, paragraph JSON,
and retrieval metadata under ignored .temp/m5-completion-20261114/ecofab-relations.
No credentials, personal contact information, record changes or publication.
"""

import argparse
import hashlib
import json
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

from defusedxml import ElementTree


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("pmcid")
    args = parser.parse_args()
    if not args.pmcid.startswith("PMC") or not args.pmcid[3:].isdigit():
        parser.error("Expected a PMCID")
    out = Path(__file__).resolve().parents[2] / ".temp/m5-completion-20261114/ecofab-relations"
    out.mkdir(parents=True, exist_ok=True)
    url = f"https://www.ebi.ac.uk/europepmc/webservices/rest/{args.pmcid}/fullTextXML"
    request = urllib.request.Request(
        url, headers={"User-Agent": "CommunityMech source verification"}
    )
    with urllib.request.urlopen(request, timeout=60) as response:
        payload = response.read()
    root = ElementTree.fromstring(payload)
    assert root.tag == "article" and len(payload) > 10000
    xml_path = out / f"{args.pmcid}.xml"
    xml_path.write_bytes(payload)
    paragraphs = []
    for section in root.iter("sec"):
        title = (
            " ".join("".join(section.find("title").itertext()).split())
            if section.find("title") is not None
            else ""
        )
        for index, paragraph in enumerate(section.findall("p")):
            paragraphs.append(
                {
                    "section": title,
                    "section_id": section.get("id"),
                    "paragraph_index": index,
                    "id": paragraph.get("id"),
                    "text": " ".join("".join(paragraph.itertext()).split()),
                }
            )
    (out / f"{args.pmcid}-paragraphs.json").write_text(json.dumps(paragraphs, indent=2) + "\n")
    metadata = {
        "pmcid": args.pmcid,
        "url": url,
        "retrieved_at": datetime.now(timezone.utc).isoformat(),
        "bytes": len(payload),
        "sha256": hashlib.sha256(payload).hexdigest(),
        "paragraphs": len(paragraphs),
        "path": str(xml_path.relative_to(out.parent)),
    }
    (out / f"{args.pmcid}-retrieval.json").write_text(json.dumps(metadata, indent=2) + "\n")
    print(json.dumps(metadata))


if __name__ == "__main__":
    main()
