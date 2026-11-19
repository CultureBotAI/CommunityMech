"""Read the four retained XLSX supplements for 000122/#1548, 2026-11-15.

Input: exact downloaded publisher XLSX files; output JSON to stdout with all
nonempty cells, including formulas and stored values. No execution or writes.
"""

import argparse
import hashlib
import json
import zipfile
from pathlib import Path

from defusedxml import ElementTree

ROOT = Path(__file__).resolve().parents[2]
NS = {"s": "http://schemas.openxmlformats.org/spreadsheetml/2006/main"}


def inspect(number):
    folder = ROOT / f".temp/phase2-gut-20261115/publisher-supplement-{number:02d}"
    path = next(folder.glob("*.xlsx"))
    receipt = json.loads((folder / "receipt.json").read_bytes())
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    if digest != receipt["sha256"]:
        raise ValueError("downloaded source changed")
    with zipfile.ZipFile(path) as archive:
        strings = []
        if "xl/sharedStrings.xml" in archive.namelist():
            strings = [
                "".join(node.itertext())
                for node in ElementTree.fromstring(archive.read("xl/sharedStrings.xml"))
            ]
        relations = {
            node.attrib["Id"]: node.attrib["Target"]
            for node in ElementTree.fromstring(archive.read("xl/_rels/workbook.xml.rels"))
        }
        sheets = []
        for sheet in ElementTree.fromstring(archive.read("xl/workbook.xml")).findall(
            "s:sheets/s:sheet", NS
        ):
            relation = sheet.attrib[
                "{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id"
            ]
            target = relations[relation]
            target = target.lstrip("/") if target.startswith("/") else "xl/" + target
            cells = []
            for cell in ElementTree.fromstring(archive.read(target)).findall(".//s:c", NS):
                value = cell.findtext("s:v", namespaces=NS)
                if cell.attrib.get("t") == "s" and value is not None:
                    value = strings[int(value)]
                if cell.attrib.get("t") == "inlineStr":
                    value = "".join(cell.find("s:is", NS).itertext())
                formula = cell.findtext("s:f", namespaces=NS)
                if value is not None or formula is not None:
                    cells.append({"cell": cell.attrib["r"], "value": value, "formula": formula})
            sheets.append({"name": sheet.attrib["name"], "cells": cells})
    return {"path": str(path.relative_to(ROOT)), "sha256": digest, "sheets": sheets}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("number", type=int, choices=(2, 3, 4, 5))
    args = parser.parse_args()
    print(json.dumps(inspect(args.number), indent=2))


if __name__ == "__main__":
    main()
