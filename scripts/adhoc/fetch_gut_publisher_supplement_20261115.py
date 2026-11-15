"""Preserve an article-linked supplement for 000122/#1548, 2026-11-15.

Input: explicit supplement number from the publisher's article page. Output:
exclusive private source bytes and receipt. Anonymous; no code execution.
"""

import argparse
import hashlib
import json
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BASE = "https://static-content.springer.com/esm/art%3A10.15252%2Fmsb.20178157/MediaObjects/"
EXTENSIONS = {1: "pdf", 2: "xlsx", 3: "xlsx", 4: "xlsx", 5: "xlsx", 6: "zip", 7: "pdf"}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("number", type=int, choices=EXTENSIONS)
    parser.add_argument("--plan", action="store_true")
    args = parser.parse_args()
    name = f"44320_2018_BFMSB178157_MOESM{args.number}_ESM.{EXTENSIONS[args.number]}"
    state = ROOT / f".temp/phase2-gut-20261115/publisher-supplement-{args.number:02d}"
    if state.exists():
        raise ValueError("retained attempt exists")
    if args.plan:
        print(json.dumps({"url": BASE + name, "destination": str(state.relative_to(ROOT))}))
        return
    state.mkdir(parents=True)
    request = urllib.request.Request(
        BASE + name, headers={"User-Agent": "CommunityMech source inspection"}
    )
    try:
        with urllib.request.urlopen(request, timeout=120) as response:
            data = response.read(32 * 1024 * 1024 + 1)
        expected = b"%PDF" if EXTENSIONS[args.number] == "pdf" else b"PK"
        if len(data) > 32 * 1024 * 1024 or not data.startswith(expected):
            raise ValueError("unexpected source format/size")
    except Exception as error:
        (state / "failure.json").write_text(
            json.dumps({"url": BASE + name, "error": str(error)}) + "\n"
        )
        raise
    path = state / name
    path.write_bytes(data)
    result = {
        "url": BASE + name,
        "accessed_at": datetime.now(timezone.utc).isoformat(),
        "path": str(path.relative_to(ROOT)),
        "sha256": hashlib.sha256(data).hexdigest(),
        "bytes": len(data),
        "source": "Publisher article Supplementary Information link",
    }
    (state / "receipt.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
