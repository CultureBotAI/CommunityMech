"""Publish completed M5 product evidence, 2026-11-15, #2844/#2852.

Inputs: explicit retained canary/batch, original product snapshots and a native
M5 checksum listing. Outputs: immutable sanitized reports; no execution/network.
Log hashes are independently captured after completion, not native receipt fields.
"""

import argparse
import json
import re
from collections import Counter
from datetime import datetime
from pathlib import Path

from export_m5_technical_evidence_20261114 import ROOT, digest, immutable, sanitize

PIN = "f471548888761bd217084c4405a9a5d4e222251a"
STATE = ROOT / ".temp/product-labels-20261115"
OUT = ROOT / "reports/product-labels-20261115"
NAMES = ("render", "export", "validate-export", "validate-labels")
CANARY = "Yolo_Silt_Loam_Soil_Dopamine_Amendment_Microcosm.yaml"
PRODUCTS = (
    "docs/communities/" + CANARY.replace(".yaml", ".html"),
    "output/kgx/nodes.tsv",
    "output/kgx/edges.tsv",
    "output/kgx/manifest.json",
)


def prepare(run):
    """Validate all inputs before returning any proposed public bytes."""
    if run not in {"canary-001", "batch-001"}:
        raise ValueError("explicit completed product run required")
    checksum_path = STATE / "m5-raw-checksums-001.txt"
    checksum_bytes = checksum_path.read_bytes()
    remote = {}
    for line in checksum_bytes.decode().splitlines():
        match = re.fullmatch(r"([0-9a-f]{64})  (\.temp/product-labels-20261115/.+)", line)
        if not match or match[2] in remote or ".." in Path(match[2]).parts:
            raise ValueError("invalid or duplicate native checksum entry")
        remote[match[2]] = match[1]
    retained = {checksum_path: checksum_bytes}

    def read(path):
        value = path.read_bytes()
        if not value or digest(value) != remote.get(str(path.relative_to(ROOT))):
            raise ValueError("missing or changed execution-host evidence: " + path.name)
        retained[path] = value
        return value

    raw_receipt = read(STATE / run / "receipt.json")
    receipt = json.loads(raw_receipt)
    mode = run.split("-")[0]
    started = datetime.fromisoformat(receipt["started_at"])
    finished = datetime.fromisoformat(receipt["finished_at"])
    if (
        receipt["revision"] != PIN
        or receipt["mode"] != mode
        or receipt["validate_labels"] is not True
        or receipt["exit_code"] != 0
        or not started.tzinfo
        or not finished.tzinfo
        or finished <= started
        or set(receipt["products"]) != set(PRODUCTS)
        or [c["name"] for c in receipt["commands"]] != list(NAMES)
        or any(c["exit_code"] != 0 for c in receipt["commands"])
    ):
        raise ValueError("incomplete or inconsistent product receipt")
    for name, expected_sha in receipt["implementation"].items():
        path = ROOT / name
        if not path.resolve().is_relative_to(ROOT) or digest(path.read_bytes()) != expected_sha:
            raise ValueError("reviewed implementation changed: " + name)
    python = receipt["commands"][0]["argv"][0]
    if not Path(python).is_absolute() or not python.endswith("/.venv/bin/python"):
        raise ValueError("expected execution-checkout Python")
    expected_commands = [
        [
            python,
            "-m",
            "communitymech.render",
            "--all" if mode == "batch" else "kb/communities/" + CANARY,
        ],
        [python, "-m", "communitymech.export", "--kb", "kb/communities", "--output", "output/kgx"]
        + ([] if mode == "batch" else ["--record", CANARY]),
        [python, "-m", "communitymech.export.validate_kgx", "--strict"],
        [
            "/opt/homebrew/bin/just",
            "--verbose",
            "--no-dotenv",
            "--color",
            "never",
            "validate-products",
        ],
    ]
    if [c["argv"] for c in receipt["commands"]] != expected_commands:
        raise ValueError("native command scope changed")
    if mode == "batch":
        canary = json.loads(read(STATE / "canary-001/receipt.json"))
        if (
            canary["exit_code"] != 0
            or canary["mode"] != "canary"
            or canary["validate_labels"] is not True
            or canary["revision"] != PIN
            or canary["implementation"] != receipt["implementation"]
            or datetime.fromisoformat(canary["finished_at"]) >= started
        ):
            raise ValueError("batch lacks preceding compatible successful canary")
    product_checks = {}
    for name in PRODUCTS:
        raw = read(STATE / (run + "-products") / Path(name).name)
        observed = {"sha256": digest(raw), "bytes": len(raw)}
        if observed != receipt["products"][name]:
            raise ValueError("product does not match completed native receipt")
        product_checks[name] = observed
    counts = Counter()
    proposed = {}
    log_checks = {}
    for name in NAMES:
        raw = read(STATE / run / (name + ".log.txt"))
        public = sanitize(raw.decode(), counts).encode()
        if name == "validate-labels" and (
            "SKIPPED, NOT PASSED" in raw.decode()
            or "All id↔label pairs correspond." not in raw.decode()
        ):
            raise ValueError("native label gate was not completed successfully")
        proposed[f"{run}-{name}.log.txt"] = public
        log_checks[name] = {
            "raw_sha256": digest(raw),
            "raw_bytes": len(raw),
            "public_sha256": digest(public),
            "public_bytes": len(public),
        }
    public_receipt = json.loads(sanitize(raw_receipt.decode(), counts))
    public_receipt["public_evidence"] = {
        "raw_receipt_sha256": digest(raw_receipt),
        "m5_native_checksum_listing_sha256": digest(checksum_bytes),
        "logs": log_checks,
        "verified_preserved_products": product_checks,
        "redactions": dict(sorted(counts.items())),
        "limits": "Product technical evidence only. Logs independently hash-compared with M5 after completion; the native receipt does not bind logs. Non-adapter skips and configured exceptions remain explicit. No scientific approval or aggregate-QC success inferred.",
    }
    proposed[run + ".receipt.json"] = (json.dumps(public_receipt, indent=2) + "\n").encode()
    if any(path.read_bytes() != value for path, value in retained.items()):
        raise ValueError("retained evidence changed during export")
    return proposed


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run", required=True, choices=["canary-001", "batch-001"])
    args = parser.parse_args()
    proposed = prepare(args.run)
    # Check every destination before writing any, preserving partial exports too.
    for name, value in proposed.items():
        target = OUT / name
        if target.is_symlink() or (target.exists() and target.read_bytes() != value):
            raise ValueError("existing public evidence differs: " + name)
    OUT.mkdir(parents=True, exist_ok=True)
    for name, value in proposed.items():
        immutable(OUT / name, value)
    print(json.dumps({"run": args.run, "files": len(proposed), "native_exit": 0}))


if __name__ == "__main__":
    main()
