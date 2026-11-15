"""Retain anonymous primary metadata for CommunityMech:000275, #2848, 2026-11-15.

Input: the fixed PMID42343824 Europe PMC core endpoint and a new output directory.
Output: exact private JSON response and a hash/identity receipt. No canonical
writes, email addresses in requests, author contact or scientific approval.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PMID = "42343824"
DOI = "10.1021/acssynbio.6c00072"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    output = args.output
    if not output.is_absolute():
        output = ROOT / output
    if output.resolve() != output.absolute():
        parser.error("symlinked output paths are not permitted")
    if not output.is_relative_to(ROOT / ".temp"):
        parser.error("source metadata must remain in repository .temp")
    output.mkdir(parents=True, exist_ok=False)
    url = "https://www.ebi.ac.uk/europepmc/webservices/rest/search?" + urllib.parse.urlencode(
        {"query": f"EXT_ID:{PMID} AND SRC:MED", "format": "json", "resultType": "core"}
    )
    request = urllib.request.Request(url, headers={"User-Agent": "CommunityMech-source-review/1.0"})
    with urllib.request.urlopen(request, timeout=30) as response:  # noqa: S310
        raw = response.read()
    (output / "response.json").write_bytes(raw)
    payload = json.loads(raw)
    entries = payload.get("resultList", {}).get("result", [])
    if len(entries) != 1:
        raise ValueError("exactly one primary record required; raw response retained")
    entry = entries[0]
    if entry.get("id") != PMID or entry.get("doi", "").lower() != DOI:
        raise ValueError("primary identifier mismatch; raw response retained")
    if not entry.get("abstractText"):
        raise ValueError("primary abstract unavailable; raw response retained")
    receipt = {
        "record_id": "CommunityMech:000275",
        "retrieved_at": datetime.now(timezone.utc).isoformat(),
        "url": url,
        "pmid": PMID,
        "doi": DOI,
        "title": entry.get("title"),
        "pmcid": entry.get("pmcid"),
        "is_open_access": entry.get("isOpenAccess"),
        "response_sha256": hashlib.sha256(raw).hexdigest(),
        "response_bytes": len(raw),
        "source_path": str((output / "response.json").relative_to(ROOT)),
        "full_text_retrieved": False,
        "scientific_review": False,
    }
    with (output / "receipt.json").open("x") as handle:
        json.dump(receipt, handle, indent=2)
        handle.write("\n")
    if (output / "response.json").read_bytes() != raw:
        raise ValueError("persisted response differs")
    print(json.dumps(receipt, indent=2))


if __name__ == "__main__":
    main()
