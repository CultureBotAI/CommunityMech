"""Verify retained R226 sources from captured bytes, #2869, 2026-11-15.

Inputs: fixed private source captures, prior extraction results and native receipt.
Outputs: exclusive offline verification and labeled public receipt derivative.
Preserves the original retrieval helpers/runs; never rereads a path for parsing.
"""

import argparse
import hashlib
import io
import json
import re
import subprocess
from pathlib import Path

import openpyxl
from inspect_r226_name_population_20261115 import (
    BASE,
    RECORD,
    RECORD_SHA,
    ROOT,
    TABLE,
    inspect_table,
    now,
    save,
    sha,
)

STATE = ".temp/gtdb-r226-source-20261115/"
NAMES = STATE + "paenibacillus-001/"
CORRESPONDENCE = STATE + "ncbi-correspondence-001/"
WORKBOOK = "auxillary_files/ncbi_vs_gtdb_r226_bacteria.xlsx"
WORKBOOK_SHA = "75c06fc44a01afe7463d5998a4bd5260d9938937fd995fa5b9ca3b6e4a057a53"
PATTERN = re.compile(r"Paenibacillus(?:_[A-Z]+)?[ _]polymyxa(?:_[A-Z]+)?(?=$|[^A-Za-z_])")
NATIVE = ".temp/phase2-schema-20261115/paenibacillus-native-route-001"


def capture(captured, name, expected=None):
    raw = (ROOT / name).read_bytes()
    if expected is not None and sha(raw) != expected:
        raise ValueError("retained input hash differs: " + name)
    captured[name] = raw
    return raw


def unchanged(captured):
    if any((ROOT / name).read_bytes() != raw for name, raw in captured.items()):
        raise ValueError("retained input changed during verification")


def workbook_rows(raw):
    """Parse the exact bytes whose digest was checked, independent of source paths."""
    workbook = openpyxl.load_workbook(io.BytesIO(raw), read_only=True, data_only=True)
    sheets = []
    try:
        for sheet in workbook.worksheets:
            matches, header, examined = [], [], 0
            for examined, row in enumerate(sheet.iter_rows(values_only=True), start=1):
                values = list(row)
                if examined == 1:
                    header = values
                if any(isinstance(value, str) and PATTERN.search(value) for value in values):
                    matches.append({"row": examined, "values": values})
            sheets.append(
                {
                    "sheet": sheet.title,
                    "header": header,
                    "rows_examined": examined,
                    "matches": matches,
                }
            )
    finally:
        workbook.close()
    return sheets


def verified_download(captured, prefix, filename, expected):
    raw = capture(captured, prefix + filename, expected)
    receipt = json.loads(capture(captured, prefix + filename + ".receipt.json"))
    if (
        receipt["url"] != BASE + filename
        or receipt["status"] != 200
        or receipt["bytes"] != len(raw)
        or receipt["sha256"] != sha(raw)
    ):
        raise ValueError("retained download receipt does not bind its bytes")
    return raw, receipt


def sanitized_receipt(receipt, raw_sha):
    result = json.loads(json.dumps(receipt))
    index = result["command"].index("--ncbi-db") + 1
    result["command"][index] = "<local NCBI taxonomy database>"
    result["public_derivative"] = {
        "raw_receipt_sha256": raw_sha,
        "sanitized_fields": [f"command[{index}]"],
        "scope": "Only the local absolute database path is replaced; original receipt retained privately.",
    }
    return result


def verify():
    captured = {}
    capture(captured, RECORD, RECORD_SHA)
    capture(
        captured,
        "scripts/adhoc/inspect_r226_name_population_20261115.py",
        "2788d81f43dafd886e18c9b7c2728bcbdffcab81a44728dc25e755cfd4fb4c42",
    )
    capture(
        captured,
        "scripts/adhoc/inspect_r226_ncbi_correspondence_20261115.py",
        "036d52ec552b06c9838bb8738e6b686344d3d973b2eaa163e7707cb6963020cb",
    )
    capture(captured, "scripts/adhoc/verify_r226_retained_sources_20261115.py")
    capture(captured, "uv.lock")
    name_result = json.loads(
        capture(
            captured,
            NAMES + "name-population.json",
            "6871416b623d93a3b453b841ef99fb4f225206f71fe89bac2ca2730e4a83dd2a",
        )
    )
    correspondence = json.loads(
        capture(
            captured,
            CORRESPONDENCE + "correspondence-evidence.json",
            "87a1aee395657c7d71ccc620c46c8761afaf909be827442b9d0eb84bb6496b40",
        )
    )
    receipts = []
    sources = {}
    for filename, expected in (
        ("MD5SUM.txt", "00715faa537d601027d611377f7d7dedb4da2decf6fda4c950faab41da64bf3f"),
        ("VERSION.txt", "f1a34e5c882e437196f2823c2c34281100596f273660c8682da63b529f7d62de"),
        (TABLE, "a54d30b1deb505e813cb754f4298a225687df3cd882675cad7b53796d1429ebc"),
    ):
        sources[filename], receipt = verified_download(captured, NAMES, filename, expected)
        receipts.append(receipt)
    checksums = dict(line.split()[::-1] for line in sources["MD5SUM.txt"].decode().splitlines())
    raw, receipt = verified_download(captured, CORRESPONDENCE, WORKBOOK, WORKBOOK_SHA)
    if hashlib.md5(raw).hexdigest() != checksums["./" + WORKBOOK]:  # noqa: S324 - publisher
        raise ValueError("official workbook checksum differs")
    fresh = inspect_table(sources[TABLE])
    if (
        any(name_result[key] != value for key, value in fresh.items())
        or name_result["sources_verified"] != receipts
        or name_result["version"] != sources["VERSION.txt"].decode()
        or correspondence["source_receipt"] != receipt
        or correspondence["sheets"] != workbook_rows(raw)
    ):
        raise ValueError("retained extraction differs from the checked source bytes")
    native_raw = capture(
        captured,
        NATIVE + ".json",
        "e1954f29418833d0e9f8cf18188d23312c56670f91d04d2ce9041c22dbecdf13",
    )
    native = json.loads(native_raw)
    native_log = capture(
        captured,
        NATIVE + ".log",
        "f8d6b56b29fae6e15258fe440fe69c8b6e77df672077f564ef99fe6aa0316220",
    )
    native_exit = capture(captured, NATIVE + ".exit")
    if (
        native_exit != b"0\n"
        or native["exit_code"] != 0
        or native["log_sha256"] != sha(native_log)
        or native["log_bytes"] != len(native_log)
    ):
        raise ValueError("native receipt/log/exit disagree")
    unchanged(captured)
    return {
        "checked_at": now(),
        "revision": subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=ROOT, text=True
        ).strip(),
        "inputs": {name: {"sha256": sha(raw), "bytes": len(raw)} for name, raw in captured.items()},
        "captured_inputs_unchanged": True,
        "table_rows_recomputed": fresh["rows_examined"],
        "matching_name_rows": len(fresh["matching_rows"]),
        "all_saved_extractions_equal": True,
        "canonical_writes": False,
        "scientific_review": False,
        "limitation": "Offline verification of the actual retained captures; does not retroactively repair the original helper's mutable-path race or certify exact study-stock placement.",
    }, sanitized_receipt(native, sha(native_raw))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    output = args.output.resolve()
    if not output.is_relative_to(ROOT / ".temp") or output.exists():
        parser.error("new private output directory required")
    result, receipt = verify()
    output.mkdir(parents=True)
    save(output / "verification.json", result)
    save(output / "native-public-receipt.json", receipt)
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
