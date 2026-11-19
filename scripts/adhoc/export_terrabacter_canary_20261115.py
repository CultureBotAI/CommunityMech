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
from batch144_mapping_successor import (  # noqa: E402
    BASELINE,
    TERRABACTER,
    current_record_sha256,
)
from export_m5_technical_evidence_20261114 import digest, immutable, sanitize  # noqa: E402

STATE = ROOT / ".temp/gtdb-source-routes-2849-20261115"
OUT = ROOT / "reports/gtdb-source-routes-2849-20261115"
TARGET = TERRABACTER
IDENTITY = "CommunityMech:000532"
M5_ROOT = Path("/Users/marcin/agent-work/CommunityMech/gtdb-terrabacter-2849-20261115")
REVIEW = "20261115T053046Z-terrabacter-gtdb-diagnostic"
REVISION = "75c079352fbb823d6fefb5ccb5d0e712eea28676"
BEFORE = "81c8fd983bc57050595d7a4d51b64acdf2617ce9fea0f03f7ec9db4fa617c05e"
AFTER = "068a38e5be07ab6756b1fe32683c166d8562e8405fae7bc4429575a33e2578ec"
SIDECAR = "history/records/Terrabacter_2APm3_Sulfadiazine_Isolate_Baseline/2026-11-15T052909Z-codex-068f78.yaml"


def artifact(path, raw):
    return {"path": str(path.relative_to(ROOT)), "sha256": digest(raw)}


def bound_input(review, path, snapshot):
    expected = artifact(path, snapshot[path])
    matches = [item for item in review["source"]["inputs"] if item["path"] == expected["path"]]
    if len(matches) != 1 or matches[0]["sha256"] != expected["sha256"]:
        raise ValueError("saved review does not bind exact input: " + expected["path"])
    return expected


def capture_review(review_path):
    snapshot = {review_path: review_path.read_bytes()}
    review = yaml.safe_load(snapshot[review_path])
    for item in review["source"]["inputs"]:
        path = ROOT / item["path"]
        if not path.resolve().is_relative_to(ROOT.resolve()):
            raise ValueError("saved input escapes repository")
        if path not in snapshot:
            snapshot[path] = path.read_bytes()
        if digest(snapshot[path]) != item["sha256"]:
            raise ValueError("saved diagnostic input changed: " + item["path"])
    markdown = review_path.with_name("review.md")
    if markdown not in snapshot:
        snapshot[markdown] = markdown.read_bytes()
    return review, snapshot


def verify_snapshot(snapshot):
    for path, raw in snapshot.items():
        if path.read_bytes() != raw:
            raise ValueError(
                "captured input changed before publication: " + str(path.relative_to(ROOT))
            )


def public_bytes(path, raw, *, verify_only=False):
    # Raw public proof is deliberately metadata-only. Never silently sanitize a
    # byte-identical receipt: reject private values and keep its reviewed hash.
    counts = Counter()
    if sanitize(raw.decode(), counts).encode() != raw:
        raise ValueError("raw public proof contains private content")
    if verify_only:
        if path.read_bytes() != raw:
            raise ValueError("existing public proof differs from captured input")
    else:
        immutable(path, raw)
    return artifact(path, raw)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--plan", action="store_true")
    parser.add_argument("--verify-existing", action="store_true")
    args = parser.parse_args()
    review_path = ROOT / "reviews/structured" / REVIEW / "review.yaml"
    review, snapshot = capture_review(review_path)
    if review["source"]["git_revision"] != REVISION:
        raise ValueError("wrong saved M5 assessment revision")
    if digest(snapshot[ROOT / TARGET]) != AFTER:
        raise ValueError("exact authoritative M5 canonical bytes must be mirrored first")
    bound_input(review, ROOT / TARGET, snapshot)
    raw_apply = STATE / "terrabacter-applied-m5-001/receipt.json"
    raw_route = STATE / "terrabacter-diagnostic-001/native-route.json"
    proof = bound_input(review, raw_apply, snapshot)
    route = bound_input(review, raw_route, snapshot)
    pending = {}
    for gate in ("schema", "strict", "gtdb", "domain", "scalars", "history", "new-history"):
        directory = STATE / f"terrabacter-canary-run-{gate}-001"
        receipt_raw = snapshot[directory / "receipt.json"]
        receipt = json.loads(receipt_raw)
        log = snapshot[directory / "native.log"]
        exit_raw = snapshot[directory / "native.exit"]
        for name in ("receipt.json", "native.log", "native.exit"):
            bound_input(review, directory / name, snapshot)
        if (
            receipt["revision"] != REVISION
            or receipt["plan"] is not False
            or receipt["inputs"].get(str(M5_ROOT / TARGET)) != AFTER
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
        pending[OUT / f"terrabacter-{gate}-001.log.txt"] = public_log
        pending[OUT / f"terrabacter-{gate}-001.exit.txt"] = exit_raw
        pending[OUT / f"terrabacter-{gate}-001.receipt.json"] = (
            json.dumps(public_receipt, indent=2) + "\n"
        ).encode()
    verify_snapshot(snapshot)
    if args.plan:
        print(
            json.dumps(
                {
                    "public_check_artifacts": len(pending),
                    "raw_metadata_proofs": 2,
                    "manifest": "terrabacter-successor-001.json",
                    "writes": 0,
                }
            )
        )
        return
    OUT.mkdir(exist_ok=True, parents=True)
    apply_artifact = public_bytes(
        OUT / "terrabacter-apply-001.raw.json",
        snapshot[raw_apply],
        verify_only=args.verify_existing,
    )
    apply_artifact.update(raw_path=proof["path"], raw_sha256=proof["sha256"])
    route_artifact = public_bytes(
        OUT / "terrabacter-native-recomputation-001.json",
        snapshot[raw_route],
        verify_only=args.verify_existing,
    )
    route_artifact.update(raw_path=route["path"])
    entry = {
        "target": TARGET,
        "target_id": IDENTITY,
        "before_sha256": BEFORE,
        "after_sha256": AFTER,
        "scientific_review": False,
        "diagnostic_review": artifact(review_path, snapshot[review_path]),
        "review_markdown": artifact(
            review_path.with_name("review.md"), snapshot[review_path.with_name("review.md")]
        ),
        "application_receipt": apply_artifact,
        "grounding_proof": route_artifact,
        "history_sidecar": bound_input(review, ROOT / SIDECAR, snapshot),
        "scope": "Only one documented manual GTDB genus mapping plus append-only inline history differs; exact stock identity and all batch144 biological/graph assertions remain unchanged.",
    }
    manifest = {"source_baseline": BASELINE, "records": [entry]}
    # Reuse the actual regression consumer before persisting the proof manifest.
    current_record_sha256(ROOT, TARGET, BEFORE, manifest=manifest)
    verify_snapshot(snapshot)
    manifest_bytes = (json.dumps(manifest, indent=2) + "\n").encode()
    if args.verify_existing:
        expected_public = {
            **pending,
            OUT / "terrabacter-apply-001.raw.json": snapshot[raw_apply],
            OUT / "terrabacter-native-recomputation-001.json": snapshot[raw_route],
            OUT / "terrabacter-successor-001.json": manifest_bytes,
        }
        public_mtimes = {path: path.stat().st_mtime_ns for path in expected_public}
        for path, raw in expected_public.items():
            if path.read_bytes() != raw:
                raise ValueError(
                    "existing public derivative differs: " + str(path.relative_to(ROOT))
                )
        previous_helper = STATE / "export-terrabacter-before-snapshot-001.py"
        control_paths = [
            STATE / f"terrabacter-export-snapshot-{phase}-{attempt}.{suffix}"
            for phase, attempt in (("before", "001"), ("after", "002"))
            for suffix in ("log", "exit")
        ]
        control_snapshot = {path: path.read_bytes() for path in control_paths}
        snapshot.update(control_snapshot)
        for path in (previous_helper, Path(__file__)):
            if path not in snapshot:
                snapshot[path] = path.read_bytes()
        if (
            int(control_snapshot[control_paths[1]]) != 1
            or int(control_snapshot[control_paths[3]]) != 0
        ):
            raise ValueError("actual failing-before/passing-after controls required")
        attestation = {
            "scope": "Additive current-byte verification of the unchanged earlier public001 artifacts; no retrospective claim that the earlier exporter used the snapshot fix.",
            "earlier_publication_used_snapshot_guard": False,
            "previous_exporter_sha256": digest(snapshot[previous_helper]),
            "fixed_exporter_sha256": digest(snapshot[Path(__file__)]),
            "review_sha256": digest(snapshot[review_path]),
            "verified_public_artifacts": [
                artifact(path, raw) for path, raw in expected_public.items()
            ],
            "regression_artifacts": [artifact(path, raw) for path, raw in control_snapshot.items()],
            "existing_public_bytes_preserved": True,
            "existing_public_mtimes_preserved": True,
        }
        verify_snapshot(snapshot)
        for path, raw in expected_public.items():
            if path.read_bytes() != raw or path.stat().st_mtime_ns != public_mtimes[path]:
                raise ValueError("existing public artifact changed during verification")
        immutable(
            OUT / "terrabacter-export-verification-002.json",
            (json.dumps(attestation, indent=2) + "\n").encode(),
        )
        print(
            json.dumps({"verified_existing_artifacts": len(expected_public), "existing_writes": 0})
        )
        return
    for path, data in pending.items():
        immutable(path, data)
    immutable(OUT / "terrabacter-successor-001.json", manifest_bytes)
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
