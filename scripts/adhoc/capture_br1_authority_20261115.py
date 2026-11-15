"""Capture one anonymous BR1 authority response for #2849, 2026-11-15.

Inputs: one fixed public source key. Outputs: exclusive private bytes and receipt
under .temp/br1-source-review-20261115; no retries, secrets or canonical writes.
"""

import argparse
import hashlib
import json
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

from defusedxml import ElementTree

ROOT = Path(__file__).resolve().parents[2]
SOURCES = {
    "assembly": (
        "https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCF_002812725.1/dataset_report",
        "json",
    ),
    "bioproject": (
        "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=bioproject&id=394223",
        "xml",
    ),
    "biosample": (
        "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=biosample&id=7351343",
        "xml",
    ),
    "gtdb-card": ("https://gtdb-api.ecogenomic.org/genome/GCF_002812725.1/card", "json"),
    "gtdb-api-schema": ("https://gtdb-api.ecogenomic.org/openapi.json", "json"),
    "gtdb-version": ("https://gtdb-api.ecogenomic.org/meta/version", "json"),
    "gtdb-history": (
        "https://gtdb-api.ecogenomic.org/genome/GCF_002812725.1/taxon-history",
        "json",
    ),
}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", choices=SOURCES)
    parser.add_argument("--attempt", type=int, default=1)
    args = parser.parse_args()
    if args.attempt < 1:
        parser.error("positive unique attempt required")
    url, kind = SOURCES[args.source]
    output = ROOT / ".temp/br1-source-review-20261115" / f"{args.source}-{args.attempt:03d}"
    output.mkdir(parents=True, exist_ok=False)
    started = datetime.now(timezone.utc).isoformat()
    request = urllib.request.Request(url, headers={"User-Agent": "CommunityMech-source-review/1.0"})
    try:
        with urllib.request.urlopen(request, timeout=40) as response:
            data = response.read(4 * 1024 * 1024 + 1)
            status, final_url = response.status, response.geturl()
        if status != 200 or not data or len(data) > 4 * 1024 * 1024:
            raise ValueError("bounded nonempty successful response required")
        with (output / f"source.{kind}").open("xb") as handle:
            handle.write(data)
        if kind == "json":
            parsed = json.loads(data)
            if not isinstance(parsed, (dict, list)) or not parsed:
                raise ValueError("substantive structured response required")
        else:
            ElementTree.fromstring(data)
        receipt = {
            "source": args.source,
            "url": url,
            "final_url": final_url,
            "started_at": started,
            "finished_at": datetime.now(timezone.utc).isoformat(),
            "http_status": status,
            "bytes": len(data),
            "sha256": hashlib.sha256(data).hexdigest(),
            "parsed": True,
            "limit": "Anonymous captured authority metadata; identity and scientific interpretation require inspection.",
        }
        with (output / "receipt.json").open("x") as handle:
            json.dump(receipt, handle, indent=2)
            handle.write("\n")
        if (output / f"source.{kind}").read_bytes() != data:
            raise ValueError("persisted source differs")
        print(json.dumps(receipt))
    except Exception as error:
        with (output / "failure.json").open("x") as handle:
            json.dump(
                {
                    "source": args.source,
                    "url": url,
                    "started_at": started,
                    "exception_type": type(error).__name__,
                    "http_status": getattr(error, "code", None),
                    "completed": False,
                },
                handle,
                indent=2,
            )
        raise


if __name__ == "__main__":
    main()
