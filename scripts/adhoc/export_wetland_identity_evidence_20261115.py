"""Publish fixed471 identity metadata; #2898/#2912, 2026-11-15.

Inputs: pinned native saved pair and its exact captured application/source/checks.
Outputs: exclusive reports metadata, redacted logs and a versioned intermediate
manifest. Reuses the unchanged capture/publisher and native gate exporter; no
source bodies, canonical mutation, mapping approval or composite admission.
"""

import argparse
import json
import shlex
from collections import Counter
from pathlib import Path

import build_wetland_identity_diagnostic_20261115 as diagnostic
import export_scoped_gtdb_evidence_20261115 as shared
import yaml

audit = shared.audit
ROOT = audit.ROOT
CONFIG = "reports/gtdb-wetland-identity-20261115/471-identity-review-config-003.json"
CONFIG_SHA = "576784879bd4de5fb83847290930a49c8937b67ccf5ab283d5ad346a42603d8c"
PREFIX = "471-identity"
PUBLIC_SCOPE = "Fixed source-identity intermediate only; unresolved roster/graph findings and later mapping remain separate."


def verify_review(review):
    if (
        review["scientific_review"] is not False
        or review["completion"] != "completed"
        or review["verdict"] != "needs_curation"
        or review["scope"]["coverage"] != "partial"
        or review["scope"]["population_size"] != 1
        or review["source"]["git_revision"] != diagnostic.REVISION
        or [(item["target_id"], item["path"]) for item in review["targets"]]
        != [(diagnostic.identity.TARGET_ID, diagnostic.identity.TARGET)]
        or {item["issue_key"] for item in review["findings"] if item["status"] == "open"}
        != {"communitymech-2898", "communitymech-2899"}
        or len(review["checks"]) != 10
        or {item["check_id"] for item in review["checks"]}
        != {"000471-" + key for key in (*shared.RECIPES, "references", "reference-measurement")}
        or any(
            item["required"] is not True or item["status"] != "passed" or item["exit_code"] != 0
            for item in review["checks"]
        )
    ):
        raise ValueError("exact partial identity review and retained findings required")


def prepare(review_name, expected_review_sha, output_name):
    review_path = shared.safe_path(review_name)
    output = shared.safe_path(output_name)
    if not output.is_relative_to(ROOT / "reports") or output.exists():
        raise ValueError("new exclusive public report directory required")
    review, captured = audit.validate_pair(review_path, expected_review_sha)
    verify_review(review)
    implementations = [
        Path(__file__).resolve(),
        Path(shared.__file__).resolve(),
        Path(audit.__file__).resolve(),
        Path(shared.redactor.__file__).resolve(),
    ]
    shared.capture_additional(captured, implementations)

    def read(name, expected=None):
        path = shared.safe_path(name)
        item = audit.bound(review, path, captured)
        if expected is not None and item["sha256"] != expected:
            raise ValueError("fixed saved input digest differs")
        return captured[path]

    # The chain verifier and exact writer must be the bytes inspected by the review.
    for module in (diagnostic, diagnostic.identity):
        path = Path(module.__file__).resolve()
        read(str(path.relative_to(ROOT)), audit.digest(path.read_bytes()))
    config = json.loads(read(CONFIG, CONFIG_SHA))
    check = config["check_config"]
    check_config = json.loads(read(check["path"], check["sha256"]))
    applied_name = check_config["application_receipt"]
    applied = json.loads(read(applied_name, check_config["application_receipt_sha256"]))
    before = read(str(Path(applied_name).with_name("before.yaml")), diagnostic.identity.BEFORE)
    after = read(diagnostic.identity.TARGET, diagnostic.AFTER)
    stage_item, plan_item = applied["reviewed_receipt"], applied["source_plan"]
    stage = json.loads(read(stage_item["path"], stage_item["sha256"]))
    plan = json.loads(read(plan_item["path"], plan_item["sha256"]))
    diagnostic.verify_chain(before, after, applied, stage, plan)
    new_history = json.loads(read(config["gates"]["new-history"] + "/receipt.json"))
    if len(new_history["new_history_sidecars"]) != 1:
        raise ValueError("one exact native identity sidecar required")
    sidecar_name, sidecar_sha = next(iter(new_history["new_history_sidecars"].items()))
    history = yaml.safe_load(read(sidecar_name, sidecar_sha))
    if (
        history["target"]["path"] != diagnostic.identity.TARGET
        or len(history["events"]) != 1
        or history["events"][0]["sections"] != diagnostic.gate_tool.SECTIONS.split(",")
        or history["events"][0]["type"] != "EDIT"
        or applied_name not in history["events"][0]["details"]
        or check_config["application_receipt_sha256"] not in history["events"][0]["details"]
    ):
        raise ValueError("exact identity history link required")
    row = {
        "target": diagnostic.identity.TARGET,
        "target_id": diagnostic.identity.TARGET_ID,
        "after_sha256": diagnostic.AFTER,
        "history_sidecar": sidecar_name,
        "history_directory": str(Path(sidecar_name).parent),
    }
    pending, check_evidence = {}, {}
    for gate, directory_name in config["gates"].items():
        directory = shared.safe_path(directory_name)
        check_id = "000471-" + gate
        values = shared.gate_payload(
            review, captured, row, gate, directory, check_id, diagnostic.REVISION
        )
        receipt = json.loads(values[2])
        receipt["public_evidence"]["scope"] = PUBLIC_SCOPE
        values = (*values[:2], (json.dumps(receipt, indent=2) + "\n").encode())
        payloads, proof = shared.gate_artifacts(
            captured, directory, output, PREFIX, gate, check_id, values
        )
        pending.update(payloads)
        check_evidence[gate] = proof

    def public(name, suffix, *, identical=False):
        path, destination = shared.safe_path(name), output / (PREFIX + "-" + suffix)
        read(name)
        if identical:
            raw, artifact = shared.raw_metadata(review, path, destination, captured)
        else:
            counts = Counter()
            raw = shared.sanitize(captured[path].decode(), counts).encode()
            artifact = {
                "path": str(destination.relative_to(ROOT)),
                "sha256": audit.digest(raw),
                "raw_path": name,
                "raw_sha256": audit.digest(captured[path]),
                "redactions": dict(sorted(counts.items())),
            }
        if destination in pending:
            raise ValueError("duplicate public artifact destination")
        pending[destination] = raw
        return artifact

    application = public(applied_name, "apply.raw.json", identical=True)
    staged = public(stage_item["path"], "stage.raw.json", identical=True)
    reference_commands, references = {}, {}
    for item in config["recorded_commands"]:
        if not item["required"]:
            continue
        prefix, name = item["prefix"], item["name"]
        receipt = json.loads(read(prefix + ".json"))
        log = read(prefix + ".log", receipt["log_sha256"])
        saved_check = next(x for x in review["checks"] if x["check_id"] == "000471-" + name)
        if (
            int(read(prefix + ".exit").strip()) != receipt["exit_code"]
            or shlex.split(saved_check["command"]) != receipt["command"]
            or saved_check["target_ids"] != [diagnostic.identity.TARGET_ID]
        ):
            raise ValueError("actual reference command exit differs")
        reference_commands[name] = (receipt, log)
        references[name] = {
            suffix: public(prefix + "." + suffix, name + "." + suffix + ".txt")
            for suffix in ("json", "log", "exit")
        }
    directory = config["measurement_directory"]
    started = json.loads(read(directory + "/started.json"))
    receipt = json.loads(read(directory + "/receipt.json"))
    result = json.loads(read(directory + "/measurement.json", receipt["measurement_sha256"]))
    read(directory + "/measurement.log", receipt["log_sha256"])
    diagnostic.verify_references(after, directory, started, receipt, result, reference_commands)
    measurement = {
        name: public(directory + "/" + name, name)
        for name in ("started.json", "receipt.json", "measurement.json", "measurement.log")
    }
    manifest = {
        "schema_version": "wetland471-identity-intermediate-v1",
        "execution_revision": diagnostic.REVISION,
        **row,
        "before_sha256": diagnostic.identity.BEFORE,
        "scientific_review": False,
        "verdict": review["verdict"],
        "scope": PUBLIC_SCOPE,
        "diagnostic_review": audit.artifact(review_path, captured),
        "review_markdown": audit.artifact(review_path.with_name("review.md"), captured),
        "application_receipt": application,
        "staged_receipt": staged,
        "source_plan": audit.bound(review, shared.safe_path(plan_item["path"]), captured),
        "history_sidecar": audit.bound(review, shared.safe_path(sidecar_name), captured),
        "check_evidence": check_evidence,
        "reference_commands": references,
        "reference_measurement": measurement,
        "required_checks": [x["check_id"] for x in review["checks"]],
        "review_inputs_verified": len(review["source"]["inputs"]),
        "native_markdown_verified": True,
        "runtime_cache_limit": "Complete cache inventory hashes remain in the raw measurement receipt; only the actually loaded article cache is an individually archived source input.",
    }
    manifest_path = output / (PREFIX + "-intermediate.json")
    pending[manifest_path] = (json.dumps(manifest, indent=2) + "\n").encode()
    audit.verify_captured(captured)
    return (
        captured,
        pending,
        {
            "review": review_name,
            "manifest": str(manifest_path.relative_to(ROOT)),
            "implementation": {
                str(p.relative_to(ROOT)): audit.digest(captured[p]) for p in implementations
            },
            "artifacts": [
                {"path": str(p.relative_to(ROOT)), "sha256": audit.digest(raw)}
                for p, raw in sorted(pending.items())
            ],
        },
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--review", required=True)
    parser.add_argument("--review-sha256", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--plan", action="store_true")
    args = parser.parse_args()
    capture, payloads, report = prepare(args.review, args.review_sha256, args.output)
    if not args.plan:
        audit.publish(capture, payloads)
    print(json.dumps(report, indent=2))
