"""Bind the actual fixed471 identity intermediate; #2898/#2899, 2026-11-15.

Inputs: reviewed authored assessment, actual source/application/native checks.
Outputs: exclusive private native inspection and review candidate. No canonical,
cache, history or saved-review mutation; mapping remains a separate transition.
"""

import argparse
import copy
import json
import shlex
from datetime import datetime, timezone
from pathlib import Path

import build_gtdb_batch_diagnostic_20261115 as shared
import check_wetland_identity_unit_20261115 as gate_tool
import curate_wetland_identity_20261115 as identity
import measure_wetland_identity_references_20261115 as measured
import yaml

ROOT = Path(__file__).resolve().parents[2]
REVISION = "af80bc0970b2b495b16c2c5c237cdfbbaa771ce8"
AFTER = "b3234d5f041636195f4c9867aaccd0df802d22ff5f2fbc28b904868ee02b901a"


def verify_runtime_inventory(receipt):
    """Recheck the complete measured namespace, including unused cache files."""
    if measured.native.input_manifest(ROOT, [identity.TARGET]) != receipt["input_sha256"]:
        raise ValueError("complete measurement runtime inventory changed")


def capture_measurement_inputs(captured, receipt, result):
    """Archive loaded source bytes; retain unrelated cache context as raw hashes."""
    for assertion in result["records"][0]["assertions"]:
        cache = assertion["cache"]
        if (
            cache["loaded"] is not True
            or cache["requested_path"] != identity.SOURCE
            or cache["sha256"] != identity.SOURCE_SHA
            or receipt["input_sha256"].get(identity.SOURCE) != identity.SOURCE_SHA
        ):
            raise ValueError("exact loaded primary cache required for every assertion")
    verify_runtime_inventory(receipt)
    for name, expected in receipt["input_sha256"].items():
        if Path(name).parts[0] != "references_cache" or name == identity.SOURCE:
            identity.capture_core.capture(captured, name, expected)


def verify_references(current, directory, started, receipt, result, commands):
    """Accept only the actual complete successful fixed-record reference chain."""
    expected_commands = {
        "references": [
            "env",
            "JUST_NO_DOTENV=true",
            "just",
            "--verbose",
            "--no-dotenv",
            "--color",
            "never",
            "validate-references-explained",
            identity.TARGET,
        ],
        "reference-measurement": [
            ".venv/bin/python",
            "scripts/adhoc/measure_wetland_identity_references_20261115.py",
            "--output",
            directory,
        ],
    }
    if set(commands) != set(expected_commands):
        raise ValueError("exact required reference command identities required")
    for name, expected in expected_commands.items():
        command, log = commands[name]
        if (
            command["head"] != REVISION
            or command["command"] != expected
            or command["exit_code"] != 0
            or not command.get("finished_at")
            or not log
            or identity.sha(log) != command["log_sha256"]
            or len(log) != command["log_bytes"]
        ):
            raise ValueError("actual successful reference command differs")
    final_fields = {
        "finished_at",
        "inputs_unchanged",
        "measurement_sha256",
        "log_sha256",
        "exit_code",
        "counts",
    }
    if (
        set(receipt) != set(started) | final_fields
        or {key: value for key, value in receipt.items() if key not in final_fields} != started
        or receipt["revision"] != REVISION
        or receipt["target"] != identity.TARGET
        or receipt["after_sha256"] != AFTER
        or receipt["input_sha256"].get(identity.TARGET) != AFTER
        or receipt["plan"] is not False
        or receipt["inputs_unchanged"] is not True
        or receipt["exit_code"] != 0
        or receipt["source_state"]
        != "Frozen working tree with applied AFTER; target differs from HEAD."
        or receipt["measurement_sha256"]
        != identity.sha((json.dumps(result, indent=2) + "\n").encode())
        or (json.dumps(receipt, indent=2) + "\n").encode() != commands["reference-measurement"][1]
    ):
        raise ValueError("measurement start/final/outer receipt chain differs")
    shell = commands["reference-measurement"][0]
    times = [
        shell["started_at"],
        started["started_at"],
        receipt["finished_at"],
        shell["finished_at"],
    ]
    parsed = [datetime.fromisoformat(value.replace("Z", "+00:00")) for value in times]
    if parsed != sorted(parsed):
        raise ValueError("measurement time bounds differ")
    expected = {
        path: (identity.sha(value.encode()), measured.native.raw_reference(instance))
        for path, value, _, _, instance in measured.native.snippet_surfaces(yaml.safe_load(current))
    }
    if (
        identity.sha(current) != AFTER
        or len(expected) != 16
        or any(
            result.get(key) is not True
            for key in (
                "measurement_valid",
                "record_processing_complete",
                "assertion_coverage_complete",
                "native_validation_passed",
                "validation_passed",
            )
        )
        or result["native_exit_code"] != 0
        or result["errors"]
        or result["assertion_status_counts"] != {"matched": 16}
        or result["counts"] != receipt["counts"]
        or result["counts"]["records_selected"] != 1
        or result["counts"]["records_completed"] != 1
        or result["counts"]["snippet_surfaces"] != 16
        or result["counts"]["snippet_occurrences_compared"] != 16
        or result["counts"]["native_issues"] != 0
        or len(result["records"]) != 1
    ):
        raise ValueError("complete successful16-surface measurement required")
    row = result["records"][0]
    assertions = row["assertions"]
    if (
        row["record"] != identity.TARGET
        or row["completed"] is not True
        or row["native_issue_count"] != 0
        or len(assertions) != 16
        or {item["path"] for item in assertions} != set(expected)
    ):
        raise ValueError("exact one measured record and assertion population required")
    for item in assertions:
        digest, reference = expected[item["path"]]
        if (
            item["text_sha256"] != digest
            or item["validated_text_sha256"] != digest
            or item["expected_reference"] != reference
            or item["status"] != "matched"
            or item["reference_binding_consistent"] is not True
            or item["actually_compared"] is not True
        ):
            raise ValueError("measured assertion differs from captured target")


def verify_chain(original, current, applied, staged, plan):
    if (
        applied["applied"] is not True
        or applied["scope"] != identity.SCOPE
        or applied["scientific_review"] is not False
        or applied["execution_revision"] != REVISION
        or applied["target"] != identity.TARGET
        or applied["target_id"] != identity.TARGET_ID
        or applied["before_sha256"] != identity.BEFORE
        or applied["after_sha256"] != AFTER
        or staged["canonical_apply"] is not False
        or staged["source_inputs_unchanged"] is not True
        or staged["candidate_sha256"] != AFTER
        or any(
            staged[key] != applied[key]
            for key in (
                "target",
                "target_id",
                "execution_revision",
                "before_sha256",
                "source_plan",
                "inputs",
                "appended_native_inline_history",
                "scope",
                "scientific_review",
            )
        )
    ):
        raise ValueError("exact actual identity stage/application chain required")
    expected, _, event = identity.render_candidate(
        original, plan, applied["appended_native_inline_history"]["timestamp"]
    )
    if current != expected or event != applied["appended_native_inline_history"]:
        raise ValueError("current record differs from exact identity-only transition")


def verify_gate(receipt, log, exit_raw, gate, directory, check_config, check_sha):
    recipe = gate_tool.checks.RECIPES[gate]
    command = ["just", "--verbose", "--no-dotenv", "--color", "never", recipe]
    if (
        receipt["revision"] != REVISION
        or receipt["plan"] is not False
        or receipt["exit_code"] != 0
        or exit_raw.strip() != b"0"
        or not receipt.get("finished_at")
        or not log
        or identity.sha(log) != receipt["log_sha256"]
        or len(log) != receipt["log_bytes"]
        or receipt["execution_inputs_unchanged"] is not True
        or any(
            receipt["inputs"].get(str(ROOT / name)) != value
            for name, value in {
                identity.TARGET: AFTER,
                check_config["application_receipt"]: check_config["application_receipt_sha256"],
            }.items()
        )
        or check_sha not in receipt["inputs"].values()
    ):
        raise ValueError("actual completed bound identity gate required")
    if gate == "new-history":
        if receipt["command"][:6] != command or len(receipt["new_history_sidecars"]) != 1:
            raise ValueError("one exact native sidecar required")
        args = receipt["command"]
        if args[args.index("--sections") + 1] != gate_tool.SECTIONS:
            raise ValueError("identity history sections differ")
    else:
        command.append(
            "history/records/" + Path(identity.TARGET).stem
            if gate == "history"
            else identity.TARGET
        )
        if gate == "strict":
            command.extend(["--out", directory + "/strict.tsv"])
        if receipt["command"] != command or receipt["new_history_sidecars"]:
            raise ValueError("native command scope differs")


def build(config_name, config_sha, output_name):
    output = identity.path(output_name, private=True)
    if output.exists() or identity.capture_core.head() != REVISION:
        raise ValueError("exclusive private output at frozen execution revision required")
    captured = {}

    def read(name, expected=None):
        return identity.capture_core.capture(captured, name, expected)

    def external(name, expected):
        path = Path(name)
        if not path.is_absolute():
            raise ValueError("native absolute input required")
        if path not in captured:
            captured[path] = path.read_bytes()
        if identity.sha(captured[path]) != expected:
            raise ValueError("native captured input differs")

    config = json.loads(read(config_name, config_sha))
    check_item = config["check_config"]
    check_config = json.loads(read(check_item["path"], check_item["sha256"]))
    if check_config["target"] != identity.TARGET or check_config["scope"] != identity.SCOPE:
        raise ValueError("fixed identity check configuration required")
    current = read(identity.TARGET, AFTER)
    applied_name = check_config["application_receipt"]
    applied = json.loads(read(applied_name, check_config["application_receipt_sha256"]))
    original = read(str(Path(applied_name).with_name("before.yaml")), identity.BEFORE)
    stage_item, plan_item = applied["reviewed_receipt"], applied["source_plan"]
    stage = json.loads(read(stage_item["path"], stage_item["sha256"]))
    read(str(Path(stage_item["path"]).with_name(Path(identity.TARGET).name)), AFTER)
    plan = json.loads(read(plan_item["path"], plan_item["sha256"]))
    verify_chain(original, current, applied, stage, plan)
    read(str(Path(identity.__file__).relative_to(ROOT)), applied["helper_sha256"])
    for name, expected in applied["inputs"].items():
        read(name, AFTER if name == identity.TARGET else expected)
    source = read(identity.SOURCE, identity.SOURCE_SHA).decode()
    if any(anchor not in source for anchor in plan["source_anchors"]):
        raise ValueError("captured primary source anchor differs")
    for name in (
        str(Path(__file__).relative_to(ROOT)),
        str(Path(shared.__file__).relative_to(ROOT)),
        str(Path(gate_tool.__file__).relative_to(ROOT)),
        "scripts/record_review.py",
        "schema/record_review.yaml",
    ):
        read(name)
    checks, evidence = [], []
    accessed = shared.now()

    def add_check(name, command, code, log_name, summary):
        key = "000471-" + name
        evidence.append(
            {
                "evidence_id": key,
                "kind": "validation",
                "reference": log_name,
                "accessed_at": accessed,
                "support": "supports" if code == 0 else "refutes",
                "summary": summary,
            }
        )
        checks.append(
            {
                "check_id": key,
                "name": name,
                "status": "passed" if code == 0 else "failed",
                "required": True,
                "summary": summary,
                "target_ids": [identity.TARGET_ID],
                "command": shlex.join(command),
                "exit_code": code,
                "expected_exit_code": 0,
                "evidence_ids": [key],
                "scope_note": "Bounded identity intermediate; not full scientific approval or corpus QC.",
            }
        )

    if set(config["gates"]) != set(gate_tool.checks.RECIPES):
        raise ValueError("eight exact native identity gates required")
    for gate, directory in config["gates"].items():
        receipt = json.loads(read(directory + "/receipt.json"))
        log_name = directory + "/native.log"
        log, exit_raw = read(log_name), read(directory + "/native.exit")
        verify_gate(receipt, log, exit_raw, gate, directory, check_config, check_item["sha256"])
        if receipt["inputs"].get(str(ROOT / check_item["path"])) != check_item["sha256"]:
            raise ValueError("exact check config path/digest missing")
        for name, expected in receipt["inputs"].items():
            external(name, expected)
        for path in identity.path(directory, private=True).iterdir():
            if path.is_file():
                read(str(path.relative_to(ROOT)))
        for name, expected in receipt["new_history_sidecars"].items():
            sidecar = yaml.safe_load(read(name, expected))
            event = sidecar["events"]
            if (
                sidecar["target"]["path"] != identity.TARGET
                or len(event) != 1
                or event[0]["sections"] != gate_tool.SECTIONS.split(",")
                or event[0]["type"] != "EDIT"
                or event[0]["outcome"] != "changed"
                or applied_name not in event[0]["details"]
                or check_config["application_receipt_sha256"] not in event[0]["details"]
            ):
                raise ValueError("identity sidecar actual link differs")
        add_check(
            gate,
            receipt["command"],
            0,
            log_name,
            "Actual scoped native command passed on the exact identity-corrected intermediate with unchanged captured inputs.",
        )

    reference_commands = {}
    for item in config["recorded_commands"]:
        prefix = item["prefix"]
        receipt = json.loads(read(prefix + ".json"))
        log = read(prefix + ".log", receipt["log_sha256"])
        code = int(read(prefix + ".exit").strip())
        if (
            receipt["head"] != REVISION
            or not receipt.get("finished_at")
            or receipt["command"] != item["command"]
            or code != receipt["exit_code"]
            or not log
            or len(log) != receipt["log_bytes"]
        ):
            raise ValueError("actual standalone reference command differs")
        if item["required"]:
            if item["name"] in reference_commands:
                raise ValueError("duplicate required reference command")
            reference_commands[item["name"]] = (receipt, log)
            add_check(item["name"], receipt["command"], code, prefix + ".log", item["summary"])
    measurement_dir = config["measurement_directory"]
    receipt = json.loads(read(measurement_dir + "/receipt.json"))
    result = json.loads(read(measurement_dir + "/measurement.json", receipt["measurement_sha256"]))
    read(measurement_dir + "/measurement.log", receipt["log_sha256"])
    started = json.loads(read(measurement_dir + "/started.json"))
    verify_references(current, measurement_dir, started, receipt, result, reference_commands)
    if (
        receipt["revision"] != REVISION
        or receipt["after_sha256"] != AFTER
        or receipt["target"] != identity.TARGET
        or receipt["plan"] is not False
        or receipt["inputs_unchanged"] is not True
        or not receipt.get("finished_at")
        or not result["measurement_valid"]
        or not result["record_processing_complete"]
        or receipt["counts"] != result["counts"]
    ):
        raise ValueError("valid actual working-record measurement required")
    capture_measurement_inputs(captured, receipt, result)
    for name, expected in receipt["implementation_sha256"].items():
        external(name, expected)
    for name, expected in config.get("additional_inputs", {}).items():
        read(name, expected)
    identity.capture_core.unchanged(captured, REVISION)
    verify_runtime_inventory(receipt)
    native = shared.native_review()
    review = copy.deepcopy(config["review"])
    if (
        review["scientific_review"] is not False
        or review["scope"]["coverage"] != "partial"
        or review["scope"]["population_size"] != 1
    ):
        raise ValueError("one partial nonscientific identity assessment required")
    inspection = native.inspect_source(
        ROOT,
        review["targets"],
        [str(p.relative_to(ROOT)) for p in captured if p.is_relative_to(ROOT)],
    )
    shared.verify_inspection(inspection, captured, REVISION)
    review.update(
        review_id=datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
        + "-wetland471-identity-intermediate",
        started_at=accessed,
        finished_at=shared.now(),
        source=inspection["source"],
        checks=checks,
    )
    review["evidence"] = [
        {**item, "accessed_at": accessed} for item in review["evidence"]
    ] + evidence
    if any(item["status"] == "failed" for item in checks):
        review["verdict"] = "needs_curation"
    native.validate_review(review)
    identity.capture_core.unchanged(captured, REVISION)
    verify_runtime_inventory(receipt)
    output.mkdir(parents=True)
    (output / "inspection.json").write_text(json.dumps(inspection, indent=2) + "\n")
    (output / "review.json").write_text(json.dumps(review, indent=2) + "\n")
    return {
        "review": str((output / "review.json").relative_to(ROOT)),
        "sha256": identity.sha((output / "review.json").read_bytes()),
        "inputs": len(inspection["source"]["inputs"]),
        "checks": len(checks),
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", required=True)
    parser.add_argument("--config-sha256", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    print(json.dumps(build(args.config, args.config_sha256, args.output), indent=2))
