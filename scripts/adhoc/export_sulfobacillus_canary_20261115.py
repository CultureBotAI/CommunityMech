"""Export verified metadata-only M5 canary provenance for #2849, 2026-11-15.

Inputs: exact native saved diagnostic and locally mirrored M5 raw artifacts.
Outputs: immutable public apply/recompute proof, sanitized check triplets and a
one-target successor manifest. No record/history/cache writes or network calls.
"""

import argparse
import json
import sys
from collections import Counter
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tests"))
sys.path.insert(0, str(ROOT / "scripts/adhoc"))
from export_m5_technical_evidence_20261114 import digest, immutable, sanitize  # noqa: E402
from sulfobacillus_mapping_successor import (  # noqa: E402
    BASELINE,
    IDENTITY,
    TARGET,
    current_record_sha256,
)

STATE = ROOT / ".temp/gtdb-source-routes-2849-20261115"
OUT = ROOT / "reports/gtdb-source-routes-2849-20261115"
REVIEW = "20261115T050549Z-sulfobacillus-gtdb-diagnostic"
REVISION = "cb642708f04b12d3a30ecdb662854dd26816014c"
BEFORE = "71160959bae2c8e3f0caf63d57452a597e29967f70faea6bec59016752b9aad4"
AFTER = "24c55ff3c29b21fa5988c4859fdcccfacc52caf62a1902cb28887b68780f551e"
SIDECAR = "history/records/Industrial_Bioreactor_Consortium/2026-11-15T050250Z-codex-3f8936.yaml"


def artifact(path):
    return {"path": str(path.relative_to(ROOT)), "sha256": digest(path.read_bytes())}


def bound_input(review, path):
    expected = artifact(path)
    matches = [item for item in review["source"]["inputs"] if item["path"] == expected["path"]]
    if len(matches) != 1 or matches[0]["sha256"] != expected["sha256"]:
        raise ValueError("saved review does not bind exact input: " + expected["path"])
    return expected


def public_bytes(path, raw):
    # Raw public proof is deliberately metadata-only. Never silently sanitize a
    # byte-identical receipt: reject private values and keep its reviewed hash.
    counts = Counter()
    if sanitize(raw.decode(), counts).encode() != raw:
        raise ValueError("raw public proof contains private content")
    immutable(path, raw)
    return artifact(path)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--plan", action="store_true")
    args = parser.parse_args()
    review_path = ROOT / "reviews/structured" / REVIEW / "review.yaml"
    review = yaml.safe_load(review_path.read_bytes())
    if review["source"]["git_revision"] != REVISION:
        raise ValueError("wrong saved M5 assessment revision")
    if digest((ROOT / TARGET).read_bytes()) != AFTER:
        raise ValueError("exact authoritative M5 canonical bytes must be mirrored first")
    bound_input(review, ROOT / TARGET)
    for item in review["source"]["inputs"]:
        if digest((ROOT / item["path"]).read_bytes()) != item["sha256"]:
            raise ValueError("saved diagnostic input changed: " + item["path"])
    raw_apply = STATE / "sulfobacillus-applied-m5-001/receipt.json"
    raw_route = STATE / "diagnostic-001/native-route.json"
    proof = bound_input(review, raw_apply)
    route = bound_input(review, raw_route)
    pending = {}
    for gate in ("schema", "strict", "gtdb", "domain", "scalars", "history", "new-history"):
        directory = STATE / f"canary-run-{gate}-001"
        receipt_raw = (directory / "receipt.json").read_bytes()
        receipt = json.loads(receipt_raw)
        log = (directory / "native.log").read_bytes()
        exit_raw = (directory / "native.exit").read_bytes()
        for name in ("receipt.json", "native.log", "native.exit"):
            bound_input(review, directory / name)
        if (
            receipt["revision"] != REVISION
            or receipt["plan"] is not False
            or receipt["inputs"].get(str(ROOT / TARGET)) != AFTER
            or receipt["exit_code"] != 0
            or int(exit_raw) != receipt["exit_code"]
            or not receipt.get("finished_at")
            or not log
            or digest(log) != receipt["log_sha256"]
            or len(log) != receipt["log_bytes"]
        ):
            raise ValueError("actual native command evidence differs")
        counts = Counter()
        public_log = sanitize(log.decode(), counts).encode()
        public_receipt = json.loads(sanitize(receipt_raw.decode(), counts))
        public_receipt["public_evidence"] = {
            "raw_receipt_sha256": digest(receipt_raw),
            "raw_log_sha256": digest(log),
            "raw_exit_sha256": digest(exit_raw),
            "public_log_sha256": digest(public_log),
            "redactions": {k: v for k, v in sorted(counts.items()) if v},
            "raw_location": "Original M5 isolated checkout and verified local mirror; repository .temp.",
            "scope": "One mapping canary; no corpus or scientific completion claim.",
        }
        pending[OUT / f"sulfobacillus-{gate}-001.log.txt"] = public_log
        pending[OUT / f"sulfobacillus-{gate}-001.exit.txt"] = exit_raw
        pending[OUT / f"sulfobacillus-{gate}-001.receipt.json"] = (
            json.dumps(public_receipt, indent=2) + "\n"
        ).encode()
    if args.plan:
        print(
            json.dumps(
                {
                    "public_check_artifacts": len(pending),
                    "raw_metadata_proofs": 2,
                    "manifest": "sulfobacillus-successor-001.json",
                    "writes": 0,
                }
            )
        )
        return
    OUT.mkdir(exist_ok=True, parents=True)
    apply_artifact = public_bytes(OUT / "sulfobacillus-apply-001.raw.json", raw_apply.read_bytes())
    apply_artifact.update(raw_path=proof["path"], raw_sha256=proof["sha256"])
    route_artifact = public_bytes(
        OUT / "sulfobacillus-native-recomputation-001.json", raw_route.read_bytes()
    )
    route_artifact.update(raw_path=route["path"])
    manifest = {
        "source_baseline": BASELINE,
        "target": TARGET,
        "target_id": IDENTITY,
        "before_sha256": BEFORE,
        "after_sha256": AFTER,
        "scientific_review": False,
        "diagnostic_review": artifact(review_path),
        "review_markdown": artifact(review_path.with_name("review.md")),
        "application_receipt": apply_artifact,
        "native_recomputation": route_artifact,
        "history_sidecar": bound_input(review, ROOT / SIDECAR),
        "scope": "Only one GTDB mapping plus append-only inline history differs; batch53 biological/graph assertions and unresolved1509 are preserved.",
    }
    # Reuse the actual regression consumer before persisting the proof manifest.
    current_record_sha256(ROOT, TARGET, BEFORE, manifest=manifest)
    for path, data in pending.items():
        immutable(path, data)
    immutable(
        OUT / "sulfobacillus-successor-001.json", (json.dumps(manifest, indent=2) + "\n").encode()
    )
    print(
        json.dumps(
            {
                "public_check_artifacts": len(pending),
                "actual_applied_sha256": proof["sha256"],
                "after_sha256": AFTER,
            }
        )
    )


if __name__ == "__main__":
    main()
