"""Inspect R226 NCBI correspondence for the 000393 source dispute, #2848, 2026-11-15.

Inputs: retained official MD5 metadata, one official correspondence workbook,
and unchanged canonical record. Outputs: private exact capture and matching
sheet rows. No record edits, classification policy or scientific clearance.
"""

import argparse
import hashlib
import json
import re
import subprocess
from pathlib import Path

import openpyxl
from inspect_r226_name_population_20261115 import RECORD, RECORD_SHA, ROOT, fetch, now, save, sha

WORKBOOK = "ncbi_vs_gtdb_r226_bacteria.xlsx"
PUBLISHER_MD5 = "2d3db581c432d2b75f37b5ced415360f"
CHECKSUM_SHA = "00715faa537d601027d611377f7d7dedb4da2decf6fda4c950faab41da64bf3f"
PATTERN = re.compile(r"Paenibacillus(?:_[A-Z]+)?[ _]polymyxa(?:_[A-Z]+)?(?=$|[^A-Za-z_])")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--checksum-file", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--plan", action="store_true")
    args = parser.parse_args()
    output, checksum = args.output.absolute(), args.checksum_file.resolve()
    private = (ROOT / ".temp").resolve()
    if (
        not output.resolve().is_relative_to(private)
        or output.exists()
        or output.is_symlink()
        or not checksum.is_relative_to(private)
    ):
        parser.error("retained private metadata and new private output directory required")
    checksum_raw, record_raw = checksum.read_bytes(), (ROOT / RECORD).read_bytes()
    if sha(checksum_raw) != CHECKSUM_SHA or sha(record_raw) != RECORD_SHA:
        parser.error("reviewed checksum metadata or canonical record changed")
    wanted = "./auxillary_files/" + WORKBOOK
    matches = [line.split() for line in checksum_raw.decode().splitlines() if line.endswith(wanted)]
    if matches != [[PUBLISHER_MD5, wanted]]:
        parser.error("exact official correspondence checksum required")
    inputs = {
        str(checksum.relative_to(ROOT)): CHECKSUM_SHA,
        RECORD: RECORD_SHA,
        str(Path(__file__).relative_to(ROOT)): sha(Path(__file__).read_bytes()),
        "scripts/adhoc/inspect_r226_name_population_20261115.py": sha(
            (ROOT / "scripts/adhoc/inspect_r226_name_population_20261115.py").read_bytes()
        ),
        "uv.lock": sha((ROOT / "uv.lock").read_bytes()),
    }
    plan = {
        "inputs": inputs,
        "revision": subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=ROOT, text=True
        ).strip(),
        "source": "auxillary_files/" + WORKBOOK,
        "max_bytes": 3 * 1024 * 1024,
        "scientific_review": False,
    }
    if args.plan:
        print(json.dumps({**plan, "plan": True}, indent=2))
        return 0
    output.mkdir(parents=True)
    save(output / "started.json", {**plan, "started_at": now()})
    try:
        (output / "auxillary_files").mkdir()
        raw, receipt = fetch(output, plan["source"], plan["max_bytes"])
        if hashlib.md5(raw).hexdigest() != PUBLISHER_MD5:  # noqa: S324 - official file checksum
            raise ValueError("workbook differs from the official checksum")
        workbook = openpyxl.load_workbook(output / plan["source"], read_only=True, data_only=True)
        sheets = []
        for sheet in workbook.worksheets:
            selected, header, examined = [], [], 0
            for examined, row in enumerate(sheet.iter_rows(values_only=True), start=1):
                values = list(row)
                if examined == 1:
                    header = values
                if any(isinstance(value, str) and PATTERN.search(value) for value in values):
                    selected.append({"row": examined, "values": values})
            sheets.append(
                {
                    "sheet": sheet.title,
                    "header": header,
                    "rows_examined": examined,
                    "matches": selected,
                }
            )
        workbook.close()
        if not any(sheet["matches"] for sheet in sheets if sheet["sheet"] == "Species"):
            raise ValueError("target species correspondence was not found")
        if any(sha((ROOT / path).read_bytes()) != digest for path, digest in inputs.items()):
            raise ValueError("an inspected input changed during the run")
        result = {
            **plan,
            "finished_at": now(),
            "source_receipt": receipt,
            "publisher_md5": PUBLISHER_MD5,
            "query_pattern": PATTERN.pattern,
            "sheets": sheets,
            "limits": (
                "Fresh official R226 correspondence rows only. These are distinct from the "
                "R226 GTDB name-query population and the kg-microbe crosswalk. No original "
                "historical input identity, study-stock assignment or complete scientific review."
            ),
        }
        save(output / "correspondence-evidence.json", result)
        print(json.dumps(result, indent=2))
        return 0
    except Exception as error:
        save(output / "failure.json", {"finished_at": now(), "error": str(error)})
        raise


if __name__ == "__main__":
    raise SystemExit(main())
