"""Extract exact DOCX table cells for the #1548 source canary (2026-11-15).

Inputs: named private Coker Tables S1/S3 files from the saved Europe PMC archive.
Output: JSON on stdout with source hashes, table/row/cell locators and text.
No input mutation or scientific inference; source discrepancies stay explicit.
"""

import hashlib
import json
import zipfile
from pathlib import Path

from defusedxml import ElementTree

ROOT = Path(__file__).resolve().parents[2]
SOURCES = ROOT / ".temp/phase2-science-20261115/lbnl-supplements"
NS = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}


def main():
    outputs = []
    for name in ("msystems.00951-22-s0006.docx", "msystems.00951-22-s0008.docx"):
        path = SOURCES / name
        raw = path.read_bytes()
        with zipfile.ZipFile(path) as archive:
            document = ElementTree.fromstring(archive.read("word/document.xml"))
        tables = []
        for table_index, table in enumerate(document.findall(".//w:tbl", NS), 1):
            rows = []
            for row_index, row in enumerate(table.findall("w:tr", NS), 1):
                cells = [
                    "".join(node.text or "" for node in cell.findall(".//w:t", NS))
                    for cell in row.findall("w:tc", NS)
                ]
                rows.append({"row": row_index, "cells": cells})
            tables.append({"table": table_index, "rows": rows})
        paragraphs = [
            "".join(node.text or "" for node in p.findall(".//w:t", NS))
            for p in document.findall("./w:body/w:p", NS)
        ]
        outputs.append(
            {
                "path": str(path.relative_to(ROOT)),
                "sha256": hashlib.sha256(raw).hexdigest(),
                "bytes": len(raw),
                "paragraphs": paragraphs,
                "tables": tables,
            }
        )
    print(json.dumps({"documents": outputs}, indent=2))


if __name__ == "__main__":
    main()
