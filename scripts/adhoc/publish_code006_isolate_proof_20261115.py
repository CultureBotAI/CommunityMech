"""Publish the reviewed isolate proof through the shared snapshot guard, 2026-11-15.

Inputs: exact native saved review and its bound actual receipt/recomputation.
Outputs: exclusive metadata-only reports, bound native logs/exits and strict
successor manifest. No canonical/cache/history/review changes (#2848/#2864).
"""

import argparse
import json
import re
from pathlib import Path

import scoped_gtdb_evidence_20261115 as evidence

ROOT = Path(__file__).resolve().parents[2]
BASE = "68699871415fda3c9eebf20382a315f9f3c7b17a"
M5_CHECKOUT = b"/Users/marcin/agent-work/CommunityMech/gtdb-genus-subset-20261115"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--review", type=Path, required=True)
    parser.add_argument("--review-sha256", required=True)
    parser.add_argument("--record", choices=["000552", "000553"], required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--plan", action="store_true")
    args = parser.parse_args()
    helpers = {
        path: path.read_bytes()
        for path in (Path(__file__).resolve(), Path(evidence.__file__).resolve())
    }
    review_path = (ROOT / args.review).resolve()
    output, manifest_path = (ROOT / args.output).resolve(), (ROOT / args.manifest).resolve()
    if (
        output.exists()
        or manifest_path.exists()
        or not output.is_relative_to(ROOT / "reports")
        or not manifest_path.is_relative_to(ROOT / "reports")
    ):
        raise ValueError("exclusive repository report paths required")
    review, captured = evidence.validate_pair(review_path, args.review_sha256)
    for path, raw in helpers.items():
        if path in captured and captured[path] != raw:
            raise ValueError("publication helper overlaps a different saved input")
        captured.setdefault(path, raw)
    identity = "CommunityMech:" + args.record
    if (
        review["scientific_review"] is not False
        or review["completion"] != "completed"
        or review["verdict"] != "pass_with_limitations"
        or len(review["targets"]) != 1
        or review["targets"][0]["target_id"] != identity
    ):
        raise ValueError("one completed scoped technical assessment required")
    target = review["targets"][0]["path"]
    state = ROOT / ".temp/gtdb-code006-20261115"
    application = state / f"isolate-{args.record}-applied-001/receipt.json"
    route = state / f"isolate-{args.record}-native-recomputation-001.json"
    raw_application = evidence.bound(review, application, captured)
    raw_route = evidence.bound(review, route, captured)
    receipt = json.loads(captured[application])
    if (
        receipt["target"] != target
        or receipt["applied"] is not True
        or receipt["execution_revision"] != review["source"]["git_revision"]
    ):
        raise ValueError("actual application differs from saved assessment")
    scaffold = state / f"isolate-{args.record}-run-new-history-001.log"
    evidence.bound(review, scaffold, captured)
    sidecars = [
        ROOT / row["path"]
        for row in review["source"]["inputs"]
        if row["path"].startswith("history/records/") and row["path"] in captured[scaffold].decode()
    ]
    if len(sidecars) != 1:
        raise ValueError("one bound actual sidecar required")
    sidecar = sidecars[0]
    pending = {
        output / "application.raw.json": captured[application],
        output / "native-recomputation.json": captured[route],
    }

    def published(path):
        return {
            "path": str(path.relative_to(ROOT)),
            "sha256": evidence.digest(pending[path]),
        }

    proof = {
        "source_baseline": BASE,
        "target": target,
        "target_id": identity,
        "scientific_review": False,
        "before_sha256": receipt["before_sha256"],
        "after_sha256": receipt["after_sha256"],
        "diagnostic_review": evidence.artifact(review_path, captured),
        "review_markdown": evidence.artifact(review_path.with_name("review.md"), captured),
        "application_receipt": {
            **published(output / "application.raw.json"),
            "raw_path": raw_application["path"],
            "raw_sha256": raw_application["sha256"],
        },
        "before_copy_path": str(application.with_name("before.yaml").relative_to(ROOT)),
        "history_sidecar": evidence.bound(review, sidecar, captured),
        "native_recomputation": {
            **published(output / "native-recomputation.json"),
            "raw_path": raw_route["path"],
        },
    }
    gate_rows = []
    by_id = {row["evidence_id"]: row for row in review["evidence"]}
    required = [row for row in review["checks"] if row["required"]]
    if {row["check_id"] for row in required} != {
        "schema",
        "strict",
        "gtdb",
        "domain",
        "scalars",
        "history",
        "completion",
        "terms",
    }:
        raise ValueError("all eight declared native checks required")
    for check in required:
        if check["status"] != "passed" or check["exit_code"] != 0:
            raise ValueError("native check did not pass")
        log = ROOT / by_id[check["evidence_ids"][0]]["reference"]
        code = log.with_suffix(".exit")
        log_item, code_item = evidence.bound(review, log, captured), evidence.bound(
            review, code, captured
        )
        if not captured[log] or captured[code].strip() != b"0":
            raise ValueError("actual native gate output differs")
        log_raw = captured[log]
        public_log = log_raw
        replacements = 0
        if check["check_id"] == "strict":
            replacements = log_raw.count(M5_CHECKOUT)
            public_log = log_raw.replace(M5_CHECKOUT, b"<checkout>")
        pending[output / (check["check_id"] + ".log.txt")] = public_log
        pending[output / (check["check_id"] + ".exit.txt")] = captured[code]
        gate_rows.append(
            {
                "check_id": check["check_id"],
                "exit_code": 0,
                "raw_log": log_item,
                "raw_exit": code_item,
                "log_byte_identical": public_log == log_raw,
                "log_transformation": (
                    {
                        "kind": "exact native checkout prefix replaced with <checkout>",
                        "replacement_count": replacements,
                    }
                    if replacements
                    else {"kind": "none", "replacement_count": 0}
                ),
                "public_log": published(output / (check["check_id"] + ".log.txt")),
                "public_exit": published(output / (check["check_id"] + ".exit.txt")),
            }
        )
    summary = {
        "records": [proof],
        "review_inputs_verified": len(review["source"]["inputs"]),
        "gates": gate_rows,
        "helper_sha256": {
            str(path.relative_to(ROOT)): evidence.digest(raw) for path, raw in helpers.items()
        },
        "scope": "One genus database correspondence; preserved historical science; no corpus QC, species/genome identity, or issue closure.",
    }
    pending[manifest_path] = (json.dumps(summary, indent=2) + "\n").encode()
    pending[output / "README.md"] = (
        f"# Isolate {args.record}: scoped genus correspondence\n\n"
        f"The native saved [assessment](../../../{proof['diagnostic_review']['path']}) binds {len(review['source']['inputs'])} inputs. "
        "Seven scoped checks and both unchanged outstanding-grounding tests passed. Public logs/exits are byte-identical to the review-bound raw artifacts except the strict log: its one absolute native checkout prefix is replaced with <checkout>, with raw and derived hashes plus the exact transformation recorded in the manifest. "
        "The term CLI reports `Validation passed` without assertion counters; its local adapter identity check used file stats, not database byte hashes.\n\n"
        "The exact application receipt and native recomputation are reproduced byte-for-byte. Only the genus block, grounding status and native inline history changed; study-stock species/genome identity, all biological content and historical scientific findings remain unchanged. "
        "This is a partial technical assessment with scientific_review:false. Full scientific review and full corpus QC are separate.\n"
    ).encode()
    for raw in pending.values():
        text = raw.decode()
        if "/Users/" in text or re.search(r"[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}", text):
            raise ValueError("private path/contact in public artifact")
    evidence.verify_captured(captured)
    if not args.plan:
        evidence.publish(captured, pending)
    print(
        json.dumps(
            {
                "planned": args.plan,
                "artifact_count": len(pending),
                "manifest": str(manifest_path.relative_to(ROOT)),
                "manifest_sha256": evidence.digest(pending[manifest_path]),
                "review_id": review["review_id"],
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
