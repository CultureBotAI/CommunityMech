"""Capture primary PMID29930200 XML for the 000122/#1548 review, 2026-11-15.

Input: anonymous Europe PMC article endpoint. Outputs: exclusive private XML,
wrapped main-body sections, supplement link inventory and SHA-256 receipt.
No canonical writes, source-cache edits, credentials or provider credits.
"""

import argparse
import hashlib
import json
import textwrap
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

from defusedxml import ElementTree

ROOT = Path(__file__).resolve().parents[2]
URL = "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC6011841/fullTextXML"
STATE = ROOT / ".temp/phase2-gut-20261115/primary-001"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--plan", action="store_true")
    args = parser.parse_args()
    if STATE.exists():
        raise ValueError("refusing to overwrite retained source evidence")
    if args.plan:
        print(json.dumps({"url": URL, "destination": str(STATE.relative_to(ROOT))}))
        return
    request = urllib.request.Request(URL, headers={"User-Agent": "CommunityMech scientific review"})
    with urllib.request.urlopen(request, timeout=60) as response:
        data = response.read()
    article = ElementTree.fromstring(data)
    identifiers = [node.text for node in article.findall(".//article-id")]
    if "29930200" not in identifiers or article.find("body") is None:
        raise ValueError("download is not the expected primary article")
    STATE.mkdir(parents=True)
    (STATE / "article.xml").write_bytes(data)
    sections = []
    for index, section in enumerate(article.find("body")):
        text = " ".join(" ".join(section.itertext()).split())
        path = STATE / f"section-{index:02d}.txt"
        path.write_text(textwrap.fill(text, width=110) + "\n")
        sections.append(
            {
                "path": path.name,
                "title": section.findtext("title"),
                "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
            }
        )
    supplements = []
    for node in article.findall(".//supplementary-material"):
        supplements.append(
            {
                "text": " ".join(node.itertext()).strip(),
                "links": [
                    dict(child.attrib)
                    for child in node.iter()
                    if any("href" in key for key in child.attrib)
                ],
            }
        )
    result = {
        "url": URL,
        "accessed_at": datetime.now(timezone.utc).isoformat(),
        "article_sha256": hashlib.sha256(data).hexdigest(),
        "bytes": len(data),
        "sections": sections,
        "supplements": supplements,
    }
    (STATE / "receipt.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
