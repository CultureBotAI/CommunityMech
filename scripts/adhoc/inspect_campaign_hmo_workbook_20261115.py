"""Read retained HMO source-data cells for #1428/#2845, 2026-11-15.

Input: one completed private asset receipt and its exact XLSX bytes; optional
bounded worksheet/row selection. Output: JSON to stdout only, with coordinates
and hashes. No files, network, workbook recalculation or scientific verdict.
"""

import argparse
import hashlib
import json
from pathlib import Path

from openpyxl import load_workbook

ROOT = Path(__file__).resolve().parents[2]
STATE = ROOT / ".temp/campaign-resume-20261115"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("receipt", type=Path)
    parser.add_argument("--sheet")
    parser.add_argument("--first-row", type=int, default=1)
    parser.add_argument("--last-row", type=int, default=30)
    parser.add_argument("--columns", type=int, default=30)
    args = parser.parse_args()
    receipt = args.receipt.resolve()
    if not receipt.is_relative_to(STATE.resolve()):
        raise ValueError("private campaign receipt required")
    if (
        not 1 <= args.first_row <= args.last_row <= args.first_row + 499
        or not 1 <= args.columns <= 60
    ):
        raise ValueError("bounded worksheet selection required")
    receipt_bytes = receipt.read_bytes()
    receipt_sha = hashlib.sha256(receipt_bytes).hexdigest()
    entry = json.loads(receipt_bytes)
    path = (receipt.parent / entry["filename"]).resolve()
    if path.parent != receipt.parent or path.suffix != ".xlsx":
        raise ValueError("receipt must name an adjacent XLSX")
    before = sha(path)
    if before != entry["sha256"] or path.stat().st_size != entry["bytes"]:
        raise ValueError("source differs from completed acquisition")
    workbook = load_workbook(path, read_only=True, data_only=True, keep_links=False)
    result = {
        "source": str(path.relative_to(ROOT)),
        "source_sha256": before,
        "receipt_sha256": receipt_sha,
        "method": "openpyxl read_only data_only: retained cached values, no formula recomputation",
        "worksheets": [
            {"name": sheet.title, "rows": sheet.max_row, "columns": sheet.max_column}
            for sheet in workbook
        ],
    }
    if args.sheet:
        sheet = workbook[args.sheet]
        result["selection"] = {
            "worksheet": args.sheet,
            "first_row": args.first_row,
            "last_row": args.last_row,
            "columns": args.columns,
            "rows": [
                [
                    {"cell": cell.coordinate, "value": cell.value}
                    for cell in row
                    if cell.value is not None
                ]
                for row in sheet.iter_rows(
                    min_row=args.first_row, max_row=args.last_row, max_col=args.columns
                )
            ],
        }
    workbook.close()
    if sha(path) != before:
        raise ValueError("source changed while reading")
    if sha(receipt) != receipt_sha:
        raise ValueError("receipt changed while reading")
    print(json.dumps(result, indent=2, ensure_ascii=False, default=str))


if __name__ == "__main__":
    main()
