"""Copy hash-verified retained linked-record evidence, 2026-11-15.

Inputs: immutable predecessor review and its retained local source captures.
Outputs: exclusive source copies and a public-safe receipt in new ignored state.
Serves #2674/#2774/#2806. No network, canonical/cache edits or interpretation.
"""

import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
PREDECESSORS = {
    "ecofab": "reviews/structured/20261114T212137Z-m5-ecofab-completion-canary/review.yaml",
    "dopamine": "reviews/structured/20261114T213444Z-m5-dopamine-syncom-primary-review/review.yaml",
}
PREFIXES = (
    ".temp/m5-completion-20261114/ecofab-independent/",
    ".temp/m5-completion-20261114/ecofab-relations/",
    ".temp/m5-completion-20261114/dopamine-syncom-sources/",
)
DESTINATION = ROOT / ".temp/phase2-science-20261115/linked-retained"


def sha256(raw):
    return hashlib.sha256(raw).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--retained-root", type=Path, required=True)
    parser.add_argument("--record", choices=PREDECESSORS, required=True)
    parser.add_argument("--only-source", help="same-path one-file persistence canary")
    parser.add_argument("--receipt", required=True, help="new receipt basename")
    parser.add_argument("--plan", action="store_true")
    args = parser.parse_args()
    if not args.receipt.replace("-", "").isalnum():
        raise ValueError("unsafe receipt basename")
    predecessor = PREDECESSORS[args.record]
    review_bytes = (ROOT / predecessor).read_bytes()
    review = yaml.safe_load(review_bytes)
    plans = []
    for item in review["source"]["inputs"]:
        source_path = item["path"]
        if not source_path.startswith(PREFIXES):
            continue
        if args.only_source and source_path != args.only_source:
            continue
        relative = Path(source_path).relative_to(".temp/m5-completion-20261114")
        source = args.retained_root / source_path
        if source.is_symlink() or not source.is_file():
            raise ValueError(f"missing/nonregular retained source: {source_path}")
        raw = source.read_bytes()
        if sha256(raw) != item["sha256"]:
            raise ValueError(f"retained source disagrees with predecessor hash: {source_path}")
        destination = DESTINATION / relative
        exists = destination.exists()
        if exists and (destination.is_symlink() or destination.read_bytes() != raw):
            raise ValueError(f"existing destination differs: {relative}")
        plans.append(
            (
                raw,
                destination,
                {
                    "source_path": source_path,
                    "destination_path": str(destination.relative_to(ROOT)),
                    "sha256": item["sha256"],
                    "bytes": len(raw),
                    "already_present_verified": exists,
                },
            )
        )
    receipt_path = DESTINATION / (args.receipt + ".json")
    if receipt_path.exists():
        raise ValueError("copy receipt already exists")
    if not plans:
        raise ValueError("no retained primary inputs selected")
    output = {
        "created_at": datetime.now(timezone.utc).isoformat(),
        "mode": "plan" if args.plan else "copy",
        "predecessor": predecessor,
        "predecessor_sha256": sha256(review_bytes),
        "inputs": [plan[2] for plan in plans],
        "limitations": "Copied retained evidence only; no new retrieval or scientific assessment.",
    }
    if not args.plan:
        for raw, destination, item in plans:
            destination.parent.mkdir(parents=True, exist_ok=True)
            if not item["already_present_verified"]:
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
