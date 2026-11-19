"""Copy hash-verified retained primary inputs for the #1548 canary, 2026-11-15.

Inputs: immutable predecessor review and its retained local source captures.
Outputs: exclusive source copies and a public-safe receipt in new ignored state.
No network, canonical/cache edits, validators, or source interpretation.
"""

import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
PREDECESSOR = "reviews/structured/20261114T213343Z-m5-lbnl-switchgrass-completion/review.yaml"
PREFIXES = (
    ".temp/m5-completion-20261114/ecofab-independent/",
    ".temp/m5-completion-20261114/ecofab-relations/",
    ".temp/m5-completion-20261114/lbnl-sources/",
)
DESTINATION = ROOT / ".temp/phase2-science-20261115/lbnl-retained"


def sha256(raw):
    return hashlib.sha256(raw).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--retained-root", type=Path, required=True)
    parser.add_argument("--plan", action="store_true")
    args = parser.parse_args()
    review_bytes = (ROOT / PREDECESSOR).read_bytes()
    review = yaml.safe_load(review_bytes)
    plans = []
    for item in review["source"]["inputs"]:
        source_path = item["path"]
        if not source_path.startswith(PREFIXES):
            continue
        relative = Path(source_path).relative_to(".temp/m5-completion-20261114")
        source = args.retained_root / source_path
        if source.is_symlink() or not source.is_file():
            raise ValueError(f"missing/nonregular retained source: {source_path}")
        raw = source.read_bytes()
        if sha256(raw) != item["sha256"]:
            raise ValueError(f"retained source disagrees with predecessor hash: {source_path}")
        destination = DESTINATION / relative
        if destination.exists():
            raise ValueError(f"exclusive output already exists: {relative}")
        plans.append(
            (
                raw,
                destination,
                {
                    "source_path": source_path,
                    "destination_path": str(destination.relative_to(ROOT)),
                    "sha256": item["sha256"],
                    "bytes": len(raw),
                },
            )
        )
    receipt_path = DESTINATION / "copy-receipt.json"
    if receipt_path.exists():
        raise ValueError("copy receipt already exists")
    if not plans:
        raise ValueError("no retained primary inputs selected")
    output = {
        "created_at": datetime.now(timezone.utc).isoformat(),
        "mode": "plan" if args.plan else "copy",
        "predecessor": PREDECESSOR,
        "predecessor_sha256": sha256(review_bytes),
        "inputs": [plan[2] for plan in plans],
        "limitations": "Copied retained evidence only; no new retrieval or scientific assessment.",
    }
    if not args.plan:
        for raw, destination, _ in plans:
            destination.parent.mkdir(parents=True, exist_ok=True)
            with destination.open("xb") as stream:
                stream.write(raw)
            if destination.read_bytes() != raw:
                raise ValueError("persisted source differs from retained bytes")
        with receipt_path.open("x") as stream:
            json.dump(output, stream, indent=2)
            stream.write("\n")
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
