"""Inspect one official R226 name population for record 000393, #2848, 2026-11-15.

Inputs: fixed official metadata and bacterial taxonomy URLs, current record.
Outputs: exclusive private source captures, checksums and complete matching rows.
This is a fresh release-specific name query, not recovered historical bytes,
an NCBI correspondence, a strain assignment, or permission to change a record.
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
BASE = "https://data.gtdb.ecogenomic.org/releases/release226/226.0/"
TABLE = "bac120_taxonomy_r226.tsv.gz"
COMPRESSED_MD5 = "b3aa58d378388e1cb233f3bd20a9f6c0"
EXPANDED_MD5 = "7d183b39c41f2370056fa5c5962fd999"
RECORD = "kb/communities/Calcium_Tomato_Bacterial_Wilt_SynCom.yaml"
RECORD_SHA = "2003158329c3f2113f6239f65b1e6a1b85bd3c19204f7aaf9d90be7f1f5c68f0"
PATTERN = r"s__Paenibacillus(?:_[A-Z]+)? polymyxa(?:_[A-Z]+)?"
LIMITS = {"MD5SUM.txt": 64 * 1024, "VERSION.txt": 1024, TABLE: 12 * 1024 * 1024}


def now():
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def save(path, value):
    with path.open("x") as stream:
        json.dump(value, stream, indent=2)
        stream.write("\n")


def fetch(output, filename, limit):
    url = BASE + filename
    request = Request(url, headers={"User-Agent": "CommunityMech source verification"})
    with urlopen(request, timeout=45) as response:  # noqa: S310 - fixed public HTTPS URLs
        if response.status != 200 or response.geturl() != url:
            raise ValueError("unexpected source status or redirect")
        raw = response.read(limit + 1)
        metadata = {
            "url": url,
            "retrieved_at": now(),
            "status": response.status,
            "content_type": response.headers.get("Content-Type"),
            "last_modified": response.headers.get("Last-Modified"),
            "bytes": len(raw),
            "sha256": sha(raw),
        }
    if not raw or len(raw) > limit:
        raise ValueError("empty or over-limit source response")
    path = output / filename
    with path.open("xb") as stream:
        stream.write(raw)
    if path.read_bytes() != raw:
        raise ValueError("source capture did not persist")
    save(output / (filename + ".receipt.json"), metadata)
    return raw, metadata


def inspect_table(raw):
    if hashlib.md5(raw).hexdigest() != COMPRESSED_MD5:  # noqa: S324 - publisher checksum
        raise ValueError("compressed source differs from the official checksum")
    with gzip.GzipFile(fileobj=io.BytesIO(raw)) as stream:
        expanded = stream.read(160 * 1024 * 1024 + 1)
    if len(expanded) > 160 * 1024 * 1024:
        raise ValueError("expanded source exceeds its bound")
    if hashlib.md5(expanded).hexdigest() != EXPANDED_MD5:  # noqa: S324 - publisher checksum
        raise ValueError("expanded source differs from the official checksum")
    identities, matches = set(), []
    rows = 0
    for rows, line in enumerate(expanded.decode("utf-8").splitlines(), start=1):
        fields = line.split("\t")
        if len(fields) != 2:
            raise ValueError("taxonomy source must have exactly two columns")
        accession, lineage = fields
        ranks = lineage.split(";")
        if (
            accession in identities
            or not re.fullmatch(r"(?:RS_GCF|GB_GCA)_\d+\.\d+", accession)
            or len(ranks) != 7
            or [value[:3] for value in ranks] != [rank + "__" for rank in "dpcofgs"]
            or ranks[0] != "d__Bacteria"
        ):
            raise ValueError("duplicate accession or unexpected taxonomy row")
        identities.add(accession)
        if re.fullmatch(PATTERN, ranks[-1]):
            matches.append(
                {"line": rows, "accession": accession, "lineage": lineage, "species": ranks[-1]}
            )
    if not rows or not matches:
        raise ValueError("taxonomy source or target name population is empty")
    return {
        "expanded_bytes": len(expanded),
        "expanded_sha256": sha(expanded),
        "expanded_md5": EXPANDED_MD5,
        "rows_examined": rows,
        "query_fullmatch": PATTERN,
        "matching_rows": matches,
        "species_row_counts": dict(sorted(Counter(row["species"] for row in matches).items())),
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
        parser.error("a new private output directory is required")
    record = (ROOT / RECORD).read_bytes()
    if sha(record) != RECORD_SHA:
        parser.error("canonical source changed; reassess before a fresh query")
    plan = {
        "record": RECORD,
        "record_sha256": RECORD_SHA,
        "revision": subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=ROOT, text=True
        ).strip(),
        "helper_sha256": sha(Path(__file__).read_bytes()),
        "output": str(output.relative_to(ROOT)),
        "sources": {BASE + name: limit for name, limit in LIMITS.items()},
        "scientific_review": False,
    }
    if args.plan:
        print(json.dumps({**plan, "plan": True}, indent=2))
        return 0
    output.mkdir(parents=True)
    save(output / "started.json", {**plan, "started_at": now()})
    try:
        md5_raw, md5_meta = fetch(output, "MD5SUM.txt", LIMITS["MD5SUM.txt"])
        checksums = dict(
            line.split()[::-1] for line in md5_raw.decode().splitlines() if line.strip()
        )
        if (
            checksums.get("./" + TABLE) != COMPRESSED_MD5
            or checksums.get("./" + TABLE.removesuffix(".gz")) != EXPANDED_MD5
        ):
            raise ValueError("official checksum metadata changed")
        version, version_meta = fetch(output, "VERSION.txt", LIMITS["VERSION.txt"])
        if version.decode().splitlines()[0] != "v226":
            raise ValueError("unexpected release version")
        raw, table_meta = fetch(output, TABLE, LIMITS[TABLE])
        result = inspect_table(raw)
        if (ROOT / RECORD).read_bytes() != record:
            raise ValueError("canonical source changed during inspection")
        result.update(
            **plan,
            finished_at=now(),
            sources_verified=[md5_meta, version_meta, table_meta],
            version=version.decode(),
            compressed_md5=COMPRESSED_MD5,
            limits=(
                "Fresh R226 GTDB name-query population only. Does not establish which original "
                "table was used, an NCBI-to-GTDB correspondence, a crosswalk denominator, "
                "a study-stock species or an assembly match. No canonical changes."
            ),
        )
        save(output / "name-population.json", result)
        print(json.dumps(result, indent=2))
        return 0
    except Exception as error:
        save(output / "failure.json", {"finished_at": now(), "error": str(error)})
        raise


if __name__ == "__main__":
    raise SystemExit(main())
