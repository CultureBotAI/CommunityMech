"""Audit/export the saved BR1 canary evidence for #2849, 2026-11-15.

Inputs: immutable native review, all mirrored inputs and actual M5 check receipts.
Outputs: new metadata-only public proofs, sanitized gate triplets and manifest.
No source/canonical/history mutation; --plan validates everything without writes.
"""

import argparse
import copy
import json
import sys
from collections import Counter
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts"))
sys.path.insert(0, str(ROOT / "scripts/adhoc"))
import record_review as native_review  # noqa: E402
from check_br1_grounding_20261115 import (  # noqa: E402
    AFTER,
    BEFORE,
    HISTORY,
    RECIPES,
    STATE,
    TARGET,
)
from curate_br1_grounding_20261115 import NEW_ID, OLD_ID, REPORT, SUMMARY  # noqa: E402
from export_m5_technical_evidence_20261114 import digest, immutable, sanitize  # noqa: E402

REVIEW = "20261115T053150Z-br1-gtdb-diagnostic"
REVIEW_SHA = "2adc93fb4ea6d0386b873b1310c95c9121f997e3fcf5349961e1ca49ba50d214"
REVISION = "56138e068c7b2d73d366fdcf9d6d95173cd599c6"
OUT = ROOT / "reports/br1-source-review-20261115"
SIDECAR = HISTORY + "/2026-11-15T053038Z-codex-1c781b.yaml"
M5_ROOT = "/Users/marcin/agent-work/CommunityMech/br1-grounding-20261115"


class FrozenSchema:
    """Supply the native validator/renderer the exact captured schema text (#2860)."""

    def __init__(self, raw):
        self.raw = raw

    def read_text(self, encoding="utf-8"):
        return self.raw.decode(encoding)


def capture_inputs(review_path):
    captured = {review_path: review_path.read_bytes()}
    if digest(captured[review_path]) != REVIEW_SHA:
        raise ValueError("immutable accepted review bytes differ")
    review = yaml.safe_load(captured[review_path])
    seen = set()
    for item in review["source"]["inputs"]:
        path = (ROOT / item["path"]).resolve()
        if not path.is_relative_to(ROOT) or path in seen:
            raise ValueError("unsafe or duplicate saved input: " + item["path"])
        seen.add(path)
        if path not in captured:
            captured[path] = path.read_bytes()
        if digest(captured[path]) != item["sha256"]:
            raise ValueError("saved diagnostic input differs: " + item["path"])
    for path in (review_path.with_name("review.md"), ROOT / "schema/record_review.yaml"):
        if path not in captured:
            captured[path] = path.read_bytes()
    return review, captured


def artifact(path, captured):
    return {"path": str(path.relative_to(ROOT)), "sha256": digest(captured[path])}


def bound(review, path, captured):
    item = artifact(path, captured)
    matches = [entry for entry in review["source"]["inputs"] if entry["path"] == item["path"]]
    if len(matches) != 1 or matches[0]["sha256"] != item["sha256"]:
        raise ValueError("saved review does not bind exact input: " + item["path"])
    return item


def raw_metadata(review, source, destination, captured):
    item = bound(review, source, captured)
    raw = captured[source]
    if sanitize(raw.decode(), Counter()).encode() != raw:
        raise ValueError("byte-identical public metadata contains private content")
    return raw, {
        "path": str(destination.relative_to(ROOT)),
        "sha256": digest(raw),
        "raw_path": item["path"],
        "raw_sha256": item["sha256"],
    }


def verify_captured(captured):
    for path, raw in captured.items():
        if path.read_bytes() != raw:
            raise ValueError("captured input changed before publication: " + str(path))


def publish(captured, pending):
    # Recheck the complete snapshot, including the immutable review and every
    # parsed/exported raw input, before creating any new public file (#2860).
    if any(path.exists() for path in pending):
        raise ValueError("public canary artifacts must use new exclusive paths")
    verify_captured(captured)
    for path, raw in pending.items():
        immutable(path, raw)


def prepare():
    review_path = ROOT / "reviews/structured" / REVIEW / "review.yaml"
    review, captured = capture_inputs(review_path)
    schema = FrozenSchema(captured[ROOT / "schema/record_review.yaml"])
    native_review.validate_review(review, schema_path=schema)
    if (
        native_review.render_markdown(review, schema_path=schema).encode()
        != captured[review_path.with_name("review.md")]
    ):
        raise ValueError("saved Markdown differs from native derivation")
    if (
        review["source"]["git_revision"] != REVISION
        or review["scientific_review"] is not False
        or review["completion"] != "completed"
        or review["scope"]["coverage"] != "partial"
        or review["verdict"] != "pass_with_limitations"
        or digest(captured[ROOT / TARGET]) != AFTER
    ):
        raise ValueError("actual scoped M5 assessment differs")
    raw_apply = STATE / "applied-m5-001/receipt.json"
    applied = json.loads(captured[raw_apply])
    if (
        applied["applied"] is not True
        or applied["execution_revision"] != REVISION
        or applied["before_sha256"] != BEFORE
        or applied["after_sha256"] != AFTER
    ):
        raise ValueError("actual application proof differs")
    before = yaml.safe_load(captured[raw_apply.with_name("before.yaml")])
    after = yaml.safe_load(captured[ROOT / TARGET])
    if (
        digest(captured[raw_apply.with_name("before.yaml")]) != BEFORE
        or before["description"].count(OLD_ID) != 1
        or after["description"] != before["description"].replace(OLD_ID, NEW_ID, 1)
        or after["curation_history"][:-1] != before["curation_history"]
        or after["curation_history"][-1]["changes"] != SUMMARY
    ):
        raise ValueError("exact accepted description/history delta differs")
    old, new = copy.deepcopy(before), copy.deepcopy(after)
    for document in (old, new):
        document.pop("description")
        document.pop("curation_history")
        document["taxonomy"][0]["taxon_term"].pop("gtdb_classification")
    if old != new:
        raise ValueError("unrelated canonical semantics changed")
    raw_route = STATE / "diagnostic-001/native-route.json"
    route = json.loads(captured[raw_route])
    if (
        route["native_result"] is not None
        or route["curated"] is not True
        or route["majority_fraction_asserted"] is not False
        or route["total_genomes_asserted"] is not False
    ):
        raise ValueError("native absence/population limits differ")
    pending = {}
    apply_raw, apply_artifact = raw_metadata(
        review, raw_apply, OUT / "br1-apply-001.raw.json", captured
    )
    route_raw, route_artifact = raw_metadata(
        review, raw_route, OUT / "br1-native-route-001.json", captured
    )
    pending[OUT / "br1-apply-001.raw.json"] = apply_raw
    pending[OUT / "br1-native-route-001.json"] = route_raw
    checks = {check["check_id"]: check for check in review["checks"]}
    if set(checks) != set(RECIPES):
        raise ValueError("exact eight required checks differ")
    for gate in RECIPES:
        directory = STATE / f"canary-run-{gate}-001"
        receipt_raw = captured[directory / "receipt.json"]
        receipt = json.loads(receipt_raw)
        log, exit_raw = captured[directory / "native.log"], captured[directory / "native.exit"]
        for name in ("receipt.json", "native.log", "native.exit"):
            bound(review, directory / name, captured)
        if (
            receipt["revision"] != REVISION
            or receipt["plan"] is not False
            or receipt["inputs"].get(M5_ROOT + "/" + TARGET) != AFTER
            or receipt["exit_code"] != 0
            or int(exit_raw) != 0
            or not receipt.get("finished_at")
            or not log
            or digest(log) != receipt["log_sha256"]
            or len(log) != receipt["log_bytes"]
            or checks[gate]["required"] is not True
            or checks[gate]["status"] != "passed"
            or checks[gate]["exit_code"] != 0
        ):
            raise ValueError("actual native gate proof differs: " + gate)
        counts = Counter()
        public_log = sanitize(log.decode(), counts).encode()
        public_receipt = json.loads(sanitize(receipt_raw.decode(), counts))
        public_receipt["public_evidence"] = {
            "raw_receipt_sha256": digest(receipt_raw),
            "raw_log_sha256": digest(log),
            "raw_exit_sha256": digest(exit_raw),
            "public_log_sha256": digest(public_log),
            "redactions": {key: value for key, value in sorted(counts.items()) if value},
            "raw_location": "Original M5 isolated checkout and hash-verified local mirror, under repository .temp.",
            "scope": "One grounding canary; no corpus or full scientific completion claim.",
        }
        pending[OUT / f"br1-{gate}-001.log.txt"] = public_log
        pending[OUT / f"br1-{gate}-001.exit.txt"] = exit_raw
        pending[OUT / f"br1-{gate}-001.receipt.json"] = (
            json.dumps(public_receipt, indent=2) + "\n"
        ).encode()
    manifest = {
        "source_baseline": "68699871415fda3c9eebf20382a315f9f3c7b17a",
        "execution_revision": REVISION,
        "target": TARGET,
        "target_id": "CommunityMech:000531",
        "before_sha256": BEFORE,
        "after_sha256": AFTER,
        "scientific_review": False,
        "diagnostic_review": artifact(review_path, captured),
        "review_markdown": artifact(review_path.with_name("review.md"), captured),
        "application_receipt": apply_artifact,
        "native_recomputation": route_artifact,
        "grounding_evidence": bound(review, ROOT / REPORT, captured),
        "history_sidecar": bound(review, ROOT / SIDECAR, captured),
        "description_replacement": {"old": OLD_ID, "new": NEW_ID, "occurrences": 1},
        "required_checks": list(RECIPES),
        "review_inputs_verified": len(review["source"]["inputs"]),
        "native_markdown_verified": True,
        "scope": "Only the exact-genome GTDB block, one description identifier and appended native history differ. Prior batch144 experimental/graph/discussion assertions remain historical and unmodified.",
    }
    pending[OUT / "br1-successor-001.json"] = (json.dumps(manifest, indent=2) + "\n").encode()
    if any(path.exists() for path in pending):
        raise ValueError("public canary artifacts must use new exclusive paths")
    result = {
        "review": REVIEW,
        "review_inputs_verified": len(review["source"]["inputs"]),
        "native_markdown_verified": True,
        "public_artifacts": len(pending),
        "artifacts": [
            {"path": str(path.relative_to(ROOT)), "sha256": digest(raw)}
            for path, raw in sorted(pending.items())
        ],
    }
    return captured, pending, result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--plan", action="store_true")
    args = parser.parse_args()
    captured, pending, result = prepare()
    if args.plan:
        verify_captured(captured)
    else:
        publish(captured, pending)
    result["writes"] = 0 if args.plan else len(pending)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
