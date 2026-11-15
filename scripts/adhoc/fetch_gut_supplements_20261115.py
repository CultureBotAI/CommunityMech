"""Retain primary-paper supplements for 000122/#1548, 2026-11-15.

Input: anonymous Europe PMC supplement package for PMC6011841. Outputs: exclusive
private ZIP, its declared PDF/XLSX/code files, and exact hashes. No execution of
downloaded code, canonical writes, credentials or provider requests.
"""

import argparse
import hashlib
import io
import json
import urllib.request
import zipfile
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
URL = "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC6011841/supplementaryFiles"
NAMES = {
    f"MSB-14-e8157-s00{i}.{ext}"
    for i, ext in enumerate(("pdf", "xlsx", "xlsx", "xlsx", "xlsx", "zip", "pdf"), start=1)
}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--plan", action="store_true")
    parser.add_argument("--attempt", required=True, choices=("002", "003"))
    args = parser.parse_args()
    state = ROOT / f".temp/phase2-gut-20261115/supplements-{args.attempt}"
    if state.exists():
        raise ValueError("refusing to replace retained supplement attempt")
    if args.plan:
        print(json.dumps({"url": URL, "expected_files": sorted(NAMES)}))
        return
    request = urllib.request.Request(URL, headers={"User-Agent": "CommunityMech scientific review"})
    state.mkdir(parents=True)
    try:
        with urllib.request.urlopen(request, timeout=300) as response:
            data = response.read(32 * 1024 * 1024 + 1)
    except Exception as error:
        (state / "failure.json").write_text(
            json.dumps(
                {
                    "url": URL,
                    "at": datetime.now(timezone.utc).isoformat(),
                    "error": type(error).__name__,
                    "message": str(error),
                },
                indent=2,
            )
            + "\n"
        )
        raise
    if len(data) > 32 * 1024 * 1024 or not data.startswith(b"PK"):
        raise ValueError("response is not a bounded ZIP supplement archive")
    selected = {}
    with zipfile.ZipFile(io.BytesIO(data)) as archive:
        for name in archive.namelist():
            basename = Path(name).name
            if basename in NAMES:
                if basename in selected:
                    raise ValueError("ambiguous supplement basename")
                selected[basename] = archive.read(name)
    if set(selected) != NAMES or any(not value for value in selected.values()):
        raise ValueError("supplement archive does not match article-declared complete inventory")
    (state / "supplements.zip").write_bytes(data)
    for name, contents in selected.items():
        (state / name).write_bytes(contents)
    report = {
        "url": URL,
        "accessed_at": datetime.now(timezone.utc).isoformat(),
        "archive_sha256": hashlib.sha256(data).hexdigest(),
        "bytes": len(data),
        "files": {
            name: {"sha256": hashlib.sha256(value).hexdigest(), "bytes": len(value)}
            for name, value in sorted(selected.items())
        },
    }
    (state / "receipt.json").write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
