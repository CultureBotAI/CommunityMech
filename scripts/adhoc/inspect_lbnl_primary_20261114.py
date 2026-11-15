#!/usr/bin/env python3
"""Capture targeted primary figures and roster for review #1548, 2026-11-14.

Inputs: anonymous open publisher URLs selected from PMID36472419.
Outputs: immutable source bytes, hashes, and DOCX table text in ignored state.
GIF-to-PNG conversion changes only the inspection container, not image pixels.
"""

import argparse
import datetime
import hashlib
import json
import urllib.request
import zipfile
from pathlib import Path

from defusedxml import ElementTree
from PIL import Image

ROOT = Path(__file__).resolve().parents[2]
DEST = ROOT / ".temp/m5-completion-20261114/lbnl-sources"
ASM = "https://journals.asm.org"
SOURCES = {
    "fig2.gif": ASM
    + "/cms/10.1128/msystems.00951-22/asset/16e7e31b-be57-4df1-b650-c37cbcfb2461/assets/images/medium/msystems.00951-22-f002.gif",
    "fig3.gif": ASM
    + "/cms/10.1128/msystems.00951-22/asset/98449edf-865a-4093-bf1a-c15e09b7eed8/assets/images/medium/msystems.00951-22-f003.gif",
    "fig5.gif": ASM
    + "/cms/10.1128/msystems.00951-22/asset/a20a1e63-4a10-43c2-8482-ed7f2d714035/assets/images/medium/msystems.00951-22-f005.gif",
    "table-s1.docx": ASM
    + "/doi/suppl/10.1128/msystems.00951-22/suppl_file/msystems.00951-22-s0006.docx",
    "table-s1-pmc.docx": "https://pmc.ncbi.nlm.nih.gov/articles/instance/9765266/bin/msystems.00951-22-s0006.docx",
}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", choices=sorted(SOURCES))
    args = parser.parse_args()
    DEST.mkdir(parents=True, exist_ok=True)
    path = DEST / args.source
    request = urllib.request.Request(
        SOURCES[args.source], headers={"User-Agent": "CommunityMech-primary-review/1.0"}
    )
    with urllib.request.urlopen(request, timeout=40) as response:
        data = response.read()
        content_type = response.headers.get("Content-Type")
    if path.exists() and path.read_bytes() != data:
        raise RuntimeError("Refusing to replace a changed source snapshot")
    if path.suffix == ".docx" and not data.startswith(b"PK"):
        raise RuntimeError("Expected DOCX archive")
    if path.suffix == ".gif" and not data.startswith(b"GIF"):
        raise RuntimeError("Expected GIF image")
    path.write_bytes(data)
    if path.suffix == ".gif":
        with Image.open(path) as figure:
            figure.save(path.with_suffix(".png"))
    else:
        ns = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}
        with zipfile.ZipFile(path) as archive:
            doc = ElementTree.fromstring(archive.read("word/document.xml"))
        rows = []
        for idx, row in enumerate(doc.findall(".//w:tr", ns), 1):
            cells = [
                " ".join(t.text or "" for t in cell.findall(".//w:t", ns))
                for cell in row.findall("w:tc", ns)
            ]
            rows.append(f"row{idx}: " + " | ".join(cells))
        path.with_suffix(".txt").write_text("\n".join(rows) + "\n")
    receipt = {
        "url": SOURCES[args.source],
        "retrieved_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "content_type": content_type,
        "bytes": len(data),
        "sha256": hashlib.sha256(data).hexdigest(),
    }
    path.with_suffix(path.suffix + ".source.json").write_text(json.dumps(receipt, indent=2) + "\n")
    print(json.dumps(receipt))


if __name__ == "__main__":
    main()
