"""Verify one public GTDB R232 species population for #2833, 2026-11-15.

Input: exactly the official NCBI-to-GTDB bacterial correspondence workbook.
Outputs: one exclusive private source capture, hash receipt and sheet/row/cell
metadata for Blautia hydrogenotrophica. No record edits, provider calls or email.
"""

import argparse
import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path
from urllib.request import Request, urlopen

import openpyxl
import yaml

ROOT = Path(__file__).resolve().parents[2]
URL = (
    "https://data.gtdb.ecogenomic.org/releases/release232/232.0/"
    "auxillary_files/ncbi_vs_gtdb_r232_bacteria.xlsx"
)
MAX_BYTES = 3 * 1024 * 1024
NAME = re.compile(r"(?<![A-Za-z0-9])Blautia(?:_A)?[ _]hydrogenotrophica\b", re.IGNORECASE)
RECORD = "kb/communities/Mucin_Glycan_MDSC_Synthetic_Gut_Community.yaml"


def now():
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def save(path, value):
    with path.open("x") as stream:
        json.dump(value, stream, indent=2, default=str)
        stream.write("\n")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument(
        "--capture-dir",
        type=Path,
        help="Reuse a hash-verified retained capture without network access",
    )
    args = parser.parse_args()
    output = args.output.absolute()
    if (
        not output.resolve().is_relative_to(ROOT / ".temp")
        or output.exists()
        or output.is_symlink()
    ):
        parser.error("new private output directory required before any network access")
    output.mkdir(parents=True)
    save(output / "started.json", {"source_url": URL, "started_at": now(), "issue": 2833})
    try:
        if args.capture_dir:
            capture = args.capture_dir.resolve()
            if not capture.is_relative_to(ROOT / ".temp"):
                raise ValueError("retained capture must be under this checkout's private .temp")
            metadata = json.loads((capture / "source-receipt.json").read_text())
            workbook_path = capture / "ncbi_vs_gtdb_r232_bacteria.xlsx"
            raw = workbook_path.read_bytes()
            if (
                metadata["source_url"] != URL
                or metadata["sha256"] != hashlib.sha256(raw).hexdigest()
                or metadata["bytes"] != len(raw)
            ):
                raise ValueError("retained workbook differs from its source receipt")
        else:
            request = Request(URL, headers={"User-Agent": "CommunityMech source verification"})
            with urlopen(request, timeout=45) as response:  # noqa: S310 - fixed public HTTPS URL
                raw = response.read(MAX_BYTES + 1)
                metadata = {
                    "source_url": URL,
                    "retrieved_at": now(),
                    "http_status": response.status,
                    "content_type": response.headers.get("Content-Type"),
                    "last_modified": response.headers.get("Last-Modified"),
                    "bytes": len(raw),
                    "sha256": hashlib.sha256(raw).hexdigest(),
                }
        if not raw.startswith(b"PK") or len(raw) > MAX_BYTES:
            raise ValueError("response is not a bounded XLSX ZIP artifact")
        if not args.capture_dir:
            workbook_path = output / "ncbi_vs_gtdb_r232_bacteria.xlsx"
            with workbook_path.open("xb") as stream:
                stream.write(raw)
        if workbook_path.read_bytes() != raw:
            raise ValueError("source capture did not persist exact bytes")
        save(output / "source-receipt.json", metadata)
        workbook = openpyxl.load_workbook(workbook_path, read_only=True, data_only=True)
        sheets = []
        for sheet in workbook.worksheets:
            first_rows, matches = [], []
            for number, row in enumerate(sheet.iter_rows(values_only=True), start=1):
                values = list(row)
                if number == 1:
                    first_rows.append({"row": number, "values": values})
                if any(isinstance(value, str) and NAME.search(value) for value in values):
                    matches.append({"row": number, "values": values})
            sheets.append({"sheet": sheet.title, "first_rows": first_rows, "matches": matches})
        workbook.close()
        species_rows = next(sheet["matches"] for sheet in sheets if sheet["sheet"] == "Species")
        if len(species_rows) != 1:
            raise ValueError("expected exactly one matching primary species row")
        values = species_rows[0]["values"]
        if values != [
            "s__Blautia hydrogenotrophica",
            25,
            1,
            "s__Blautia_A hydrogenotrophica 100.0%",
        ]:
            raise ValueError("primary source differs from the reviewed R232 population")
        record = yaml.safe_load((ROOT / RECORD).read_text())
        blocks = [
            entry["taxon_term"]["gtdb_classification"]
            for entry in record["taxonomy"]
            if entry["taxon_term"]["term"]["id"] == "NCBITaxon:53443"
        ]
        if len(blocks) != 1:
            raise ValueError("expected exactly one stored Mucin species block")
        block = blocks[0]
        if (
            block["ncbi_source_id"] != "NCBITaxon:53443"
            or block["total_genomes"] != values[1]
            or block["gtdb_id"] != "GTDB:s__Blautia_A_hydrogenotrophica"
            or block["majority_fraction"] != 1.0
        ):
            raise ValueError("stored species/population assertion differs from source cells")
        result = {
            "issue": 2833,
            "source": metadata,
            "helper_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            "sheets": sheets,
            "record_assertion": {
                "path": RECORD,
                "ncbi_source_id": block["ncbi_source_id"],
                "semantic_block_sha256": hashlib.sha256(
                    json.dumps(block, sort_keys=True, separators=(",", ":")).encode()
                ).hexdigest(),
                "verified_fields": ["total_genomes", "gtdb_id", "majority_fraction"],
            },
            "limits": "The source species row verifies population size, species correspondence and fraction only. The complete higher-rank lineage and NCBI identifier are not independently reverified by this workbook row.",
        }
        save(output / "species-row-evidence.json", result)
        print(json.dumps(result, indent=2, default=str))
        return 0
    except Exception as error:
        save(
            output / "failed.json",
            {"finished_at": now(), "exception_type": type(error).__name__, "message": str(error)},
        )
        raise


if __name__ == "__main__":
    raise SystemExit(main())
