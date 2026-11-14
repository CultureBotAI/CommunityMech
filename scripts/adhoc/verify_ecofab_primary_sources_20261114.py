#!/usr/bin/env python3
"""Capture anonymous primary sources for EcoFAB review #1427/#2674/#2675 (2026-11-14).

Inputs: explicitly selected public article, supplementary, and taxonomy URLs.
Outputs: ignored source snapshots, hashes, and readable XML/XLSX extracts beneath
.temp/m5-completion-20261114/ecofab-independent. No KB or review-bundle edits.
"""

import argparse
import datetime
import hashlib
import json
import urllib.request
import zipfile
from pathlib import Path

from defusedxml import ElementTree

ROOT = Path(__file__).resolve().parents[2]
DEST = ROOT / ".temp/m5-completion-20261114/ecofab-independent"
PLOS = "https://journals.plos.org/plosbiology/article/file?id=10.1371/journal.pbio.3003358"
SOURCES = {
    "ring-main-plos.xml": PLOS + "&type=manuscript",
    "ring-main.xml": "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC12416739/fullTextXML",
    "nitrogen-main.xml": "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC10776018/fullTextXML",
    "ring-s1.xlsx": PLOS + ".s012&type=supplementary",
    "ring-s2.xlsx": PLOS + ".s013&type=supplementary",
    "ring-s9.xlsx": PLOS + ".s020&type=supplementary",
    "ring-s8.tif": PLOS + ".s008&type=supplementary",
    "ring-s10.tif": PLOS + ".s010&type=supplementary",
    "ring-s11.tif": PLOS + ".s011&type=supplementary",
    "ring-fig2.png": "https://journals.plos.org/plosbiology/article/figure/image?size=large&id=10.1371/journal.pbio.3003358.g002",
    "ring-fig4.png": "https://journals.plos.org/plosbiology/article/figure/image?size=large&id=10.1371/journal.pbio.3003358.g004",
    "dsm113524.html": "https://www.dsmz.de/collection/catalogue/details/culture/DSM-113524",
    "arthrobacter-taxonomy.xml": "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1663,1667",
}


def text(element):
    return " ".join("".join(element.itertext()).split())


def extract_xml(path):
    root = ElementTree.parse(path).getroot()
    rows = []
    for element in root.iter():
        if element.tag in {"article-title", "title", "p", "caption", "Taxon"}:
            rows.append(f"[{element.tag} {element.attrib.get('id', '')}] {text(element)}")
    path.with_suffix(".txt").write_text("\n\n".join(rows) + "\n")


def extract_xlsx(path):
    ns = {"m": "http://schemas.openxmlformats.org/spreadsheetml/2006/main"}
    rows = []
    with zipfile.ZipFile(path) as archive:
        strings = []
        if "xl/sharedStrings.xml" in archive.namelist():
            strings = [
                text(x) for x in ElementTree.fromstring(archive.read("xl/sharedStrings.xml"))
            ]
        for sheet in sorted(archive.namelist()):
            if sheet.startswith("xl/worksheets/sheet") and sheet.endswith(".xml"):
                rows.append(f"SHEET {sheet}")
                for row in ElementTree.fromstring(archive.read(sheet)).findall(".//m:row", ns):
                    cells = []
                    for cell in row.findall("m:c", ns):
                        value = cell.find("m:v", ns)
                        value = value.text if value is not None else ""
                        if cell.get("t") == "s":
                            value = strings[int(value)]
                        elif cell.get("t") == "inlineStr":
                            value = text(cell)
                        if value:
                            cells.append(f"{cell.get('r')}={value}")
                    rows.append(" | ".join(cells))
    path.with_suffix(".txt").write_text("\n".join(rows) + "\n")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", choices=sorted(SOURCES))
    args = parser.parse_args()
    DEST.mkdir(parents=True, exist_ok=True)
    path = DEST / args.source
    url = SOURCES[args.source]
    request = urllib.request.Request(
        url, headers={"User-Agent": "CommunityMech-primary-source-review/1.0"}
    )
    with urllib.request.urlopen(request, timeout=60) as response:
        data = response.read()
        content_type = response.headers.get("Content-Type")
        final_url = response.geturl()
    if not data:
        raise RuntimeError("Empty source response")
    if path.suffix == ".xlsx" and not data.startswith(b"PK"):
        raise RuntimeError("Expected XLSX archive")
    if path.suffix == ".pdf" and not data.startswith(b"%PDF"):
        raise RuntimeError("Expected PDF")
    path.write_bytes(data)
    if path.suffix == ".xml":
        extract_xml(path)
    elif path.suffix == ".xlsx":
        extract_xlsx(path)
    entry = {
        "source": args.source,
        "url": url,
        "final_url": final_url,
        "retrieved_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "content_type": content_type,
        "bytes": path.stat().st_size,
        "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
    }
    path.with_suffix(path.suffix + ".source.json").write_text(json.dumps(entry, indent=2) + "\n")
    print(json.dumps(entry))


if __name__ == "__main__":
    main()
