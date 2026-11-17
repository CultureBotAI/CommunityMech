"""Capture primary soil-study evidence for review/fix #2709, 2026-11-14.

Inputs: existing Ding full-text XML and one named publisher supplement/figure.
Outputs: immutable raw bytes, SHA256 retrieval receipts and readable XLSX text
under ignored .temp/m5-completion-20261114/yolo-sources. Anonymous retrieval.
"""

import argparse
import hashlib
import json
import statistics
import zipfile
from datetime import datetime, timezone
from pathlib import Path
from urllib.request import Request, urlopen

from defusedxml import ElementTree
from verify_ecofab_primary_sources_20261114 import extract_xlsx

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / ".temp/m5-completion-20261114/yolo-sources"
SOURCES = {
    "soil-data5.xlsx": "https://static-content.springer.com/esm/art%3A10.1038%2Fs41467-026-76211-1/MediaObjects/41467_2026_76211_MOESM7_ESM.xlsx",
    "figure4.webp": "https://cdn.ncbi.nlm.nih.gov/pmc/blobs/5106/13522444/7db46ccc68fc/41467_2026_76211_Fig4_HTML.webp",
}


def summarize():
    """Recompute control phylum means; do not infer absolute biomass or function."""
    path = OUT / "soil-data5.xlsx"
    ns = {"m": "http://schemas.openxmlformats.org/spreadsheetml/2006/main"}
    with zipfile.ZipFile(path) as archive:
        strings = [
            "".join(x.itertext())
            for x in ElementTree.fromstring(archive.read("xl/sharedStrings.xml"))
        ]
        rows = ElementTree.fromstring(archive.read("xl/worksheets/sheet1.xml")).findall(
            ".//m:row", ns
        )
        totals = [0.0, 0.0, 0.0]
        groups = {}
        for row in rows:
            cells = {}
            for cell in row.findall("m:c", ns):
                value = cell.find("m:v", ns)
                if value is None:
                    continue
                cells[cell.get("r").rstrip("0123456789")] = (
                    strings[int(value.text)] if cell.get("t") == "s" else value.text
                )
            if int(row.get("r")) < 3 or not cells.get("Q"):
                continue
            values = [float(cells.get(c, 0)) for c in "BCD"]
            group = groups.setdefault(cells["Q"], [0.0, 0.0, 0.0])
            for i, value in enumerate(values):
                totals[i] += value
                group[i] += value
    result = {
        "source_sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
        "method": "Sum source sheet1 counts by columnQ phylum; divide each B-D control replicate by its all-row total, then average three proportions. No statistical retest.",
        "control_read_totals": totals,
        "control_phylum_mean_fractions": {
            name: statistics.mean(v / total for v, total in zip(values, totals, strict=True))
            for name, values in sorted(groups.items())
        },
        "latitude_from_source_dms": 38 + 32 / 60 + 16.9 / 3600,
        "longitude_from_source_dms": -(121 + 46 / 60 + 0.2 / 3600),
    }
    (OUT / "source-comparison.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", choices=[*SOURCES, "summarize"])
    args = parser.parse_args()
    if args.source == "summarize":
        summarize()
        return
    OUT.mkdir(parents=True, exist_ok=True)
    path = OUT / args.source
    if path.exists():
        raise ValueError("refusing to overwrite source snapshot")
    url = SOURCES[args.source]
    with urlopen(
        Request(url, headers={"User-Agent": "CommunityMech source review"}), timeout=60
    ) as response:
        data = response.read()
    expected = b"PK" if path.suffix == ".xlsx" else b"RIFF"
    if not data.startswith(expected):
        raise ValueError("unexpected response format")
    path.write_bytes(data)
    if path.suffix == ".xlsx":
        extract_xlsx(path)
    receipt = {
        "url": url,
        "retrieved_at": datetime.now(timezone.utc).isoformat(),
        "bytes": len(data),
        "sha256": hashlib.sha256(data).hexdigest(),
    }
    path.with_suffix(path.suffix + ".source.json").write_text(json.dumps(receipt, indent=2) + "\n")
    print(json.dumps(receipt))


if __name__ == "__main__":
    main()
