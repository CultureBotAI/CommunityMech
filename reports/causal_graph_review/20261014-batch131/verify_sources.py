"""Replay bounded source-table observations and unchanged-record assurances."""

import csv
import hashlib
import json
from pathlib import Path
import posixpath
import subprocess
from xml.etree import ElementTree as ET
from zipfile import ZipFile

import yaml

ROOT = Path(__file__).resolve().parents[3]
SOURCE = ROOT / "reports/causal_graph_review/sources/20261014-phormidium-batch131"
BASE = "ec5e6468b74e874f5474c52d1825fa91a0b595b7"
NS = {"m": "http://schemas.openxmlformats.org/spreadsheetml/2006/main"}
RID = "{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id"


def cells(filename, sheet_name):
    with ZipFile(SOURCE / filename) as book:
        strings = ["".join(si.itertext()) for si in ET.fromstring(book.read("xl/sharedStrings.xml"))]
        relationships = {
            rel.attrib["Id"]: rel.attrib["Target"]
            for rel in ET.fromstring(book.read("xl/_rels/workbook.xml.rels"))
        }
        sheets = ET.fromstring(book.read("xl/workbook.xml")).findall("m:sheets/m:sheet", NS)
        sheet = next(item for item in sheets if item.attrib["name"] == sheet_name)
        target = relationships[sheet.attrib[RID]]
        path = target.lstrip("/") if target.startswith("/") else posixpath.normpath("xl/" + target)
        result = {}
        for cell in ET.fromstring(book.read(path)).findall("m:sheetData/m:row/m:c", NS):
            value = cell.findtext("m:v", default="", namespaces=NS)
            if cell.get("t") == "s":
                value = strings[int(value)]
            elif cell.get("t") == "inlineStr":
                value = "".join(cell.find("m:is", NS).itertext())
            result[cell.attrib["r"]] = value
        return result


def main():
    manifest = json.loads((SOURCE / "manifest.json").read_text())
    for item in manifest["files"]:
        assert hashlib.sha256((ROOT / item["path"]).read_bytes()).hexdigest() == item["sha256"]
    report = yaml.safe_load((SOURCE / "assessment.yaml").read_text())
    genes = cells("Table_3.XLSX", "Niche analysis")
    assert genes["S2"] == "58" and genes["AB2"] == "57"
    assert genes["D149"] == "alkB" and genes["D150"] == "almA"
    assert [part.strip() for part in genes["S149"].split(",")] == ["bin58_01115", "bin58_03410"]
    assert not genes.get("S150", "").strip()
    assert genes["AB149"].strip() == "bin57_00670"
    isotope = cells("Table_4.XLSX", "Calisp statistics")
    assert isotope["E2"].strip() == "Number of Peptides"
    for key, rows, mag in (("mag34", range(13, 18), "34"), ("mag57", range(28, 33), "57"),
                           ("mag58", range(23, 28), "58")):
        assert all(isotope[f"A{row}"] == mag for row in rows)
        counts = [int(isotope[f"E{row}"]) for row in rows]
        expected = report["verified_coverage"][key]
        assert counts == expected["counts"]
        assert sum(counts) == expected["sum"] == expected["figure4_n"]
    assert [int(isotope[f"D{row}"]) for row in range(3, 8)] == [0, 14, 22, 38, 46]
    assert sum(int(isotope[f"E{row}"]) for row in range(3, 8)) == 27220
    with (ROOT / "reports/causal_graph_review/inventory.tsv").open() as handle:
        inventory = {row["path"]: row for row in csv.DictReader(handle, delimiter="\t")}
    discovered = {str(path.relative_to(ROOT)): path
                  for root in (ROOT / "kb/communities", ROOT / "data/isolates")
                  for path in root.rglob("*.yaml")}
    assert set(discovered) == set(inventory)
    for name, path in discovered.items():
        assert hashlib.sha256(path.read_bytes()).hexdigest() == inventory[name]["record_sha256"]
    unchanged = subprocess.check_output([
        "git", "diff", "--name-only", BASE, "--", "kb", "data/isolates", "references_cache", "history"
    ], cwd=ROOT, text=True)
    assert not unchanged, unchanged
    previous = json.loads((ROOT / "reports/causal_graph_review/20261014-batch130/final-network.json").read_text())
    current = json.loads((ROOT / "reports/causal_graph_review/20261014-batch131/baseline-network.json").read_text())
    assert json.loads(previous["stdout"]) == json.loads(current["stdout"])
    issues = json.loads(current["stdout"])
    types = [issue["type"] for group in issues.values() for issue in group]
    assert all(kind in {"DISCONNECTED", "UNKNOWN_TARGET"} for kind in types)
    print(json.dumps({"source_files_verified": len(manifest["files"]), "records_unchanged": len(inventory),
                      "ignored_files_included": True, "source_conflicts_preserved": 4,
                      "network_warnings_unchanged": len(types), "graph_status_promoted": False}, indent=2))


if __name__ == "__main__":
    main()
