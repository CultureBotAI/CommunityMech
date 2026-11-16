"""Capture one official R232 taxonomy for #2948, 2026-11-16.

Inputs: three fixed public GTDB URLs and the retained correspondence workbook.
Outputs: exclusive private captures/receipts and exact Akkermansia lineage rows.
No canonical changes, strain matching, release equivalence or application approval.
"""

import argparse
import gzip
import hashlib
import io
import json
import re
import subprocess
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[2]
BASE = "https://data.gtdb.ecogenomic.org/releases/release232/232.0/"
TABLE = "bac120_taxonomy_r232.tsv.gz"
COMPRESSED_MD5 = "807e3221f5553142eb0544ce3247d079"
EXPANDED_MD5 = "4d42e137959485d57e8589bdf1b4c347"
WORKBOOK_MD5 = "73d6b898524b726978761c9700200626"
WORKBOOK = (
    ".temp/akkermansia-source-20261116/retained-source-001/" "ncbi_vs_gtdb_r232_bacteria.xlsx"
)
WORKBOOK_SHA = "e401d80c914c727268c184d19201aa35dcd23aabfd027a0d6e5a57476e71f3de"
LIMITS = {"MD5SUM.txt": 64 * 1024, "VERSION.txt": 1024, TABLE: 16 * 1024 * 1024}


def now():
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def md5(raw):
    return hashlib.md5(raw).hexdigest()  # noqa: S324 - publisher integrity checksum


def save(path, value):
    with path.open("x") as handle:
        json.dump(value, handle, indent=2)
        handle.write("\n")


def fetch(output, filename):
    url = BASE + filename
    request = Request(url, headers={"User-Agent": "CommunityMech source verification"})
    with urlopen(request, timeout=45) as response:  # noqa: S310 - fixed anonymous URLs
        if response.status != 200 or response.geturl() != url:
            raise ValueError("unexpected source status or redirect")
        raw = response.read(LIMITS[filename] + 1)
        receipt = {
            "url": url,
            "retrieved_at": now(),
            "status": response.status,
            "content_type": response.headers.get("Content-Type"),
            "last_modified": response.headers.get("Last-Modified"),
            "bytes": len(raw),
            "sha256": sha(raw),
        }
    if not raw or len(raw) > LIMITS[filename]:
        raise ValueError("empty or over-limit source")
    with (output / filename).open("xb") as handle:
        handle.write(raw)
    save(output / (filename + ".receipt.json"), receipt)
    return raw, receipt


def inspect_taxonomy(raw):
    if md5(raw) != COMPRESSED_MD5:
        raise ValueError("compressed taxonomy differs from official MD5")
    with gzip.GzipFile(fileobj=io.BytesIO(raw)) as handle:
        expanded = handle.read(160 * 1024 * 1024 + 1)
    if len(expanded) > 160 * 1024 * 1024 or md5(expanded) != EXPANDED_MD5:
        raise ValueError("expanded taxonomy differs from bound official source")
    identities = set()
    matches = []
    rows = 0
    for rows, line in enumerate(expanded.decode().splitlines(), start=1):
        fields = line.split("\t")
        if len(fields) != 2:
            raise ValueError("expected two-column taxonomy")
        accession, lineage = fields
        ranks = lineage.split(";")
        if (
            accession in identities
            or not re.fullmatch(r"(?:RS_GCF|GB_GCA)_\d+\.\d+", accession)
            or len(ranks) != 7
            or [rank[:3] for rank in ranks] != [rank + "__" for rank in "dpcofgs"]
            or ranks[0] != "d__Bacteria"
        ):
            raise ValueError("duplicate accession or unexpected taxonomy row")
        identities.add(accession)
        if ranks[5] == "g__Akkermansia":
            matches.append({"line": rows, "accession": accession, "lineage": lineage})
    if not matches:
        raise ValueError("target genus absent from captured taxonomy")
    return {
        "rows_examined": rows,
        "expanded_bytes": len(expanded),
        "expanded_sha256": sha(expanded),
        "expanded_md5": md5(expanded),
        "selection": "exact rank 6 equals g__Akkermansia",
        "matching_rows": matches,
        "lineage_counts": dict(sorted(Counter(row["lineage"] for row in matches).items())),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--plan", action="store_true")
    args = parser.parse_args()
    output = args.output.absolute()
    if (
        not output.resolve().is_relative_to((ROOT / ".temp").resolve())
        or output.exists()
        or output.is_symlink()
    ):
        parser.error("new private output directory required")
    helper = Path(__file__).resolve()
    inputs = {helper: helper.read_bytes(), ROOT / WORKBOOK: (ROOT / WORKBOOK).read_bytes()}
    workbook = inputs[ROOT / WORKBOOK]
    if sha(workbook) != WORKBOOK_SHA or md5(workbook) != WORKBOOK_MD5:
        parser.error("retained workbook bytes differ")
    plan = {
        "revision": subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip(),
        "inputs": {str(path.relative_to(ROOT)): sha(raw) for path, raw in inputs.items()},
        "output": str(output.relative_to(ROOT)),
        "sources": {BASE + name: limit for name, limit in LIMITS.items()},
        "canonical_writes": False,
        "scientific_review": False,
    }
    if args.plan:
        print(json.dumps({**plan, "plan": True}, indent=2))
        return
    output.mkdir(parents=True)
    save(output / "started.json", {**plan, "started_at": now()})
    try:
        md5_raw, md5_receipt = fetch(output, "MD5SUM.txt")
        checksums = dict(line.split()[::-1] for line in md5_raw.decode().splitlines() if line)
        if (
            checksums.get("./" + TABLE) != COMPRESSED_MD5
            or checksums.get("./" + TABLE.removesuffix(".gz")) != EXPANDED_MD5
            or checksums.get("./auxillary_files/ncbi_vs_gtdb_r232_bacteria.xlsx") != WORKBOOK_MD5
        ):
            raise ValueError("official checksum declaration differs")
        version, version_receipt = fetch(output, "VERSION.txt")
        if version.decode().splitlines()[0] != "v232":
            raise ValueError("unexpected official version")
        table, table_receipt = fetch(output, TABLE)
        result = inspect_taxonomy(table)
        inputs.update(
            {output / "MD5SUM.txt": md5_raw, output / "VERSION.txt": version, output / TABLE: table}
        )
        if any(path.read_bytes() != raw for path, raw in inputs.items()):
            raise ValueError("captured input changed during source inspection")
        result.update(
            **plan,
            sources_verified=[md5_receipt, version_receipt, table_receipt],
            version=version.decode(),
            compressed_md5=md5(table),
            retained_workbook_official_md5_verified=WORKBOOK_MD5,
            inputs_unchanged=True,
            finished_at=now(),
            limits="GTDB genus lineage rows are not an NCBI correspondence population. No stock assembly, type-strain identity, BAA-83 synonymy, original metadata recovery or 761 release relationship is inferred.",
        )
        save(output / "lineage-evidence.json", result)
        print(
            json.dumps(
                {
                    "output": str(output.relative_to(ROOT)),
                    "rows_examined": result["rows_examined"],
                    "lineage_counts": result["lineage_counts"],
                    "evidence_sha256": sha((output / "lineage-evidence.json").read_bytes()),
                },
                indent=2,
            )
        )
    except Exception as error:
        save(output / "failure.json", {"finished_at": now(), "error": str(error)})
        raise


if __name__ == "__main__":
    main()
