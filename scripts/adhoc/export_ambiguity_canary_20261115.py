"""Export captured metadata-only ambiguity canary proof, #2848, 2026-11-15.

Inputs: immutable saved diagnostic and exact mirrored M5 source/check receipts.
Outputs: public metadata proofs, sanitized native triplets and strict successor
manifest. No source bodies, record/history/cache writes or network operations.
"""

import argparse
import json
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tests"))
import check_ambiguity_canary_20261115 as check  # noqa: E402
from ambiguity_status_successor import (  # noqa: E402
    BASELINE,
    IDENTITY,
    MANIFEST,
    TARGET,
    current_record_sha256,
)
from export_m5_technical_evidence_20261114 import sanitize  # noqa: E402
from scoped_gtdb_evidence_20261115 import (  # noqa: E402
    bound,
    digest,
    publish,
    validate_pair,
    verify_captured,
)

STATE = ROOT / ".temp/gtdb-ambiguity-20261115"
OUT = ROOT / "reports/gtdb-ambiguity-20261115"
REVIEW = "20261115T061642Z-faecalibacterium-ambiguity-diagnostic"
REVIEW_SHA = "7bddbfd88734b5657855f743ed55c0f01e31b42aa49603772d714fecfb68b383"
SIDECAR = check.HISTORY + "/2026-11-15T060616Z-codex-7ba0d3.yaml"


def describe(path, raw):
    return {"path": str(path.relative_to(ROOT)), "sha256": digest(raw)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--plan", action="store_true")
    args = parser.parse_args()
    review_path = ROOT / "reviews/structured" / REVIEW / "review.yaml"
    review, snapshot = validate_pair(review_path, REVIEW_SHA)
    if (
        review["source"]["git_revision"] != check.REVISION
        or digest(snapshot[ROOT / TARGET]) != check.AFTER
    ):
        raise ValueError("exact actual saved M5 diagnostic required")
    apply_path = check.APPLIED
    route_path = STATE / "ambiguity-diagnostic-002/native-route.json"
    for path in (apply_path, route_path, ROOT / SIDECAR):
        bound(review, path, snapshot)
    public_apply = OUT / "ambiguity-apply-001.raw.json"
    public_route = OUT / "ambiguity-native-route-001.json"
    pending = {}
    for gate, recipe in check.RECIPES.items():
        directory = STATE / f"ambiguity-canary-run-{gate}-001"
        for filename in ("receipt.json", "native.log", "native.exit"):
            bound(review, directory / filename, snapshot)
        raw_receipt = snapshot[directory / "receipt.json"]
        receipt = json.loads(raw_receipt)
        log, exit_raw = snapshot[directory / "native.log"], snapshot[directory / "native.exit"]
        expected = ["just", "--verbose", "--no-dotenv", "--color", "never", recipe]
        if gate == "new-history":
            if receipt["command"][:6] != expected or set(receipt["history_created"]) != {SIDECAR}:
                raise ValueError("native sidecar command differs")
        else:
            expected.append(check.HISTORY if gate == "history" else TARGET)
            if gate == "strict":
                expected.extend(["--out", str((directory / "strict.tsv").relative_to(ROOT))])
            if receipt["command"] != expected:
                raise ValueError("native check scope differs")
        if (
            receipt["revision"] != check.REVISION
            or receipt["plan"] is not False
            or receipt["inputs"].get(str(ROOT / TARGET)) != check.AFTER
            or receipt["exit_code"] != 0
            or exit_raw != b"0\n"
            or not receipt.get("finished_at")
            or not log
            or digest(log) != receipt["log_sha256"]
            or len(log) != receipt["log_bytes"]
        ):
            raise ValueError("native check identity/completion/hash differs")
        redactions = Counter()
        public_log = sanitize(log.decode(), redactions).encode()
        public_receipt = json.loads(sanitize(raw_receipt.decode(), redactions))
        public_receipt["public_evidence"] = {
            "raw_receipt_sha256": digest(raw_receipt),
            "raw_log_sha256": digest(log),
            "raw_exit_sha256": digest(exit_raw),
            "public_log_sha256": digest(public_log),
            "redactions": {name: count for name, count in sorted(redactions.items()) if count},
            "raw_location": "Original isolated M5 checkout and verified local mirror; repository .temp.",
            "scope": "One status/candidate canary; no full scientific or corpus completion claim.",
        }
        pending[OUT / f"ambiguity-{gate}-001.log.txt"] = public_log
        pending[OUT / f"ambiguity-{gate}-001.exit.txt"] = exit_raw
        pending[OUT / f"ambiguity-{gate}-001.receipt.json"] = (
            json.dumps(public_receipt, indent=2) + "\n"
        ).encode()
    helpers = [
        Path(__file__),
        ROOT / "tests/ambiguity_status_successor.py",
        ROOT / "scripts/adhoc/scoped_gtdb_evidence_20261115.py",
        ROOT / "scripts/adhoc/export_m5_technical_evidence_20261114.py",
    ]
    for path in helpers:
        if path not in snapshot:
            snapshot[path] = path.read_bytes()
    entry = {
        "target": TARGET,
        "target_id": IDENTITY,
        "scientific_review": False,
        "before_sha256": check.BEFORE,
        "after_sha256": check.AFTER,
        "diagnostic_review": describe(review_path, snapshot[review_path]),
        "review_markdown": describe(
            review_path.with_name("review.md"), snapshot[review_path.with_name("review.md")]
        ),
        "application_receipt": {
            **describe(public_apply, snapshot[apply_path]),
            "raw_path": str(apply_path.relative_to(ROOT)),
            "raw_sha256": digest(snapshot[apply_path]),
        },
        "native_recomputation": {
            **describe(public_route, snapshot[route_path]),
            "raw_path": str(route_path.relative_to(ROOT)),
            "raw_sha256": digest(snapshot[route_path]),
        },
        "history_sidecar": describe(ROOT / SIDECAR, snapshot[ROOT / SIDECAR]),
    }
    manifest = {
        "source_baseline": BASELINE,
        "records": [entry],
        "helper_sources": [describe(path, snapshot[path]) for path in helpers],
        "scope": "Exact one-record status/candidate successor only; original biological content and batch146 ledger remain unchanged. A2-165 stock-species/genome identity is not resolved.",
    }
    verify_captured(snapshot)
    if args.plan:
        print(
            json.dumps(
                {
                    "public_check_artifacts": len(pending),
                    "raw_metadata_proofs": 2,
                    "manifest": MANIFEST,
                    "writes": 0,
                },
                indent=2,
            )
        )
        return
    # Reject any private-content transformation of byte-identical raw proof.
    # These two inputs contain metadata/hashes only, never captured paper bodies.
    for path in (apply_path, route_path):
        if sanitize(snapshot[path].decode(), Counter()).encode() != snapshot[path]:
            raise ValueError("raw metadata proof contains private content")
    all_paths = [*pending, public_apply, public_route, ROOT / MANIFEST]
    if any(path.exists() or path.is_symlink() for path in all_paths):
        raise ValueError("preserve all existing publication artifacts")
    publish(snapshot, {public_apply: snapshot[apply_path], public_route: snapshot[route_path]})
    current_record_sha256(ROOT, TARGET, check.BEFORE, manifest=manifest)
    pending[ROOT / MANIFEST] = (json.dumps(manifest, indent=2) + "\n").encode()
    publish(snapshot, pending)
    current_record_sha256(ROOT, TARGET, check.BEFORE)
    print(
        json.dumps(
            {
                "manifest": MANIFEST,
                "sha256": digest((ROOT / MANIFEST).read_bytes()),
                "public_check_artifacts": len(check.RECIPES) * 3,
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
