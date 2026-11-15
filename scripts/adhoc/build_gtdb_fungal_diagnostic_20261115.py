"""Additive mixed fungal-domain diagnostic builder, #2904, 2026-11-15.

The original executed builder is unchanged. This version additionally binds
the affirmative native domain artifact before constructing any assessment.

Inputs: externally pinned max-ten-record authored config, raw source/application
chains, native gates and sidecars. Outputs: exclusive metadata-only source
reports and private native inspection/review candidate. Does not save a review,
edit canonical sources, or infer scientific approval from validators.
"""

import argparse
import importlib.util
import json
import shlex
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

import check_gtdb_batch_unit_20261115 as gates
import export_m5_technical_evidence_20261114 as redactor
import gtdb_fungal_batch_curation_20261115 as core
import gtdb_fungal_domain_contract_20261115 as domain_contract
import yaml

ROOT = Path(__file__).resolve().parents[2]


def now():
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def native_review():
    spec = importlib.util.spec_from_file_location(
        "gtdb_native_review", ROOT / "scripts/record_review.py"
    )
    native = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(native)
    return native


def verify_inspection(inspection, captured, revision):
    rows = inspection["source"]["inputs"]
    names = [row["path"] for row in rows]
    expected = {
        str(location.relative_to(ROOT)): core.sha(raw)
        for location, raw in captured.items()
        if location.is_relative_to(ROOT)
    }
    if (
        inspection["source"]["git_revision"] != revision
        or len(names) != len(set(names))
        or {row["path"]: row["sha256"] for row in rows} != expected
    ):
        raise ValueError("native inspection must match the complete assessed capture exactly")


def verify_domain_chain(row, stage_receipt, applied, read):
    """Bind one actual application to the same captured affirmative observation."""
    item = applied["domain_proof"]
    if (
        applied.get("contract") != domain_contract.CONTRACT
        or stage_receipt.get("contract") != domain_contract.CONTRACT
        or stage_receipt.get("domain_proof") != item
        or applied["native_operations"] != ["--apply", "--apply-status"]
        or stage_receipt["native_operations"] != applied["native_operations"]
        or applied["inputs"] != stage_receipt["inputs"]
    ):
        raise ValueError("mixed fungal stage/application contract differs")
    document = json.loads(read(item["path"], item["sha256"]))
    domain_contract.verify_document(row, document, applied["source_proof"], applied["inputs"])
    return item, document


def build(config_name, config_sha, output_name, revision):
    output = core.path(output_name, private=True)
    if output.exists() or core.head() != revision:
        raise ValueError("exclusive private output and exact execution revision required")
    captured = {}

    def read(name, expected=None):
        return core.capture(captured, name, expected)

    config = json.loads(read(config_name, config_sha))
    units = config["records"]
    if not 1 <= len(units) <= 10 or len({unit["target"] for unit in units}) != len(units):
        raise ValueError("one to ten unique whole-record units required")
    if len({unit["target_id"] for unit in units}) != len(units):
        raise ValueError("unique target identities required")
    for name in (
        str(Path(__file__).relative_to(ROOT)),
        str(Path(core.__file__).relative_to(ROOT)),
        domain_contract.HELPER,
        str(Path(gates.__file__).relative_to(ROOT)),
        str(Path(redactor.__file__).relative_to(ROOT)),
        "scripts/record_review.py",
        "schema/record_review.yaml",
    ):
        read(name)
    checks, evidence, assessments, targets, public = [], [], [], [], {}
    started = now()
    for unit in units:
        identity, target = unit["target_id"], unit["target"]
        prefix = identity.split(":")[-1] + "-"
        current = read(target, unit["after_sha256"])
        applied_path = core.path(unit["application_receipt"], private=True)
        applied_raw = read(unit["application_receipt"], unit["application_receipt_sha256"])
        applied = json.loads(applied_raw)
        read(str(Path(core.__file__).relative_to(ROOT)), applied["helper_sha256"])
        before = read(
            str(applied_path.with_name("before.yaml").relative_to(ROOT)), unit["before_sha256"]
        )
        stage_dir = core.path(unit["stage_directory"], private=True)
        stage_receipt = json.loads(
            read(
                str((stage_dir / "receipt.json").relative_to(ROOT)),
                applied["reviewed_receipt_sha256"],
            )
        )
        read(str((stage_dir / Path(target).name).relative_to(ROOT)), unit["after_sha256"])
        if (
            applied["applied"] is not True
            or applied["execution_revision"] != revision
            or applied["target"] != target
            or applied["before_sha256"] != unit["before_sha256"]
            or applied["after_sha256"] != unit["after_sha256"]
            or applied["inputs"] != stage_receipt["inputs"]
            or stage_receipt["target"] != target
            or stage_receipt["target_id"] != identity
            or stage_receipt["candidate_sha256"] != unit["after_sha256"]
            or stage_receipt["exit_codes"] != [0] * len(stage_receipt["native_operations"])
            or stage_receipt["source_inputs_unchanged"] is not True
        ):
            raise ValueError("actual reviewed before-to-after chain differs")
        for name, expected in applied["inputs"].items():
            read(name, unit["after_sha256"] if name == target else expected)
        proof_item = stage_receipt["source_proof"]
        if applied["source_proof"] != proof_item:
            raise ValueError("actual application source-proof linkage differs")
        source = json.loads(read(proof_item["path"], proof_item["sha256"]))
        row, _ = core.source_unit(source, identity)
        domain_item, domain_document = verify_domain_chain(row, stage_receipt, applied, read)
        _, events = core.verify_candidate(
            before, current, row, core.native_module(), stage_receipt["mapping_source"]
        )
        if events != stage_receipt["appended_native_inline_history"]:
            raise ValueError("actual appended native history differs")
        if set(unit["gates"]) != set(gates.RECIPES):
            raise ValueError("all eight declared native gates required")
        sidecars = None
        for gate, recipe in gates.RECIPES.items():
            directory = core.path(unit["gates"][gate], private=True)
            receipt = json.loads(read(str((directory / "receipt.json").relative_to(ROOT))))
            log_name = str((directory / "native.log").relative_to(ROOT))
            log = read(log_name, receipt["log_sha256"])
            exit_raw = read(str((directory / "native.exit").relative_to(ROOT)))
            if (
                receipt["revision"] != revision
                or receipt["plan"] is not False
                or receipt["exit_code"] != 0
                or exit_raw.strip() != b"0"
                or not log
                or len(log) != receipt["log_bytes"]
                or receipt["execution_inputs_unchanged"] is not True
                or receipt["inputs"].get(str(ROOT / target)) != unit["after_sha256"]
            ):
                raise ValueError("required native gate did not pass on accepted current bytes")
            command = ["just", "--verbose", "--no-dotenv", "--color", "never", recipe]
            if gate == "new-history":
                if receipt["command"][:6] != command or receipt["new_history_sidecars"] != {
                    unit["history_sidecar"]: unit["history_sidecar_sha256"]
                }:
                    raise ValueError("native new-history persistence differs")
                sidecars = receipt["new_history_sidecars"]
            else:
                command.append(
                    "history/records/" + Path(target).stem if gate == "history" else target
                )
                if gate == "strict":
                    command.extend(["--out", str((directory / "strict.tsv").relative_to(ROOT))])
                if command != receipt["command"]:
                    raise ValueError("actual native gate command scope differs")
            for name, expected in receipt["inputs"].items():
                location = Path(name)
                if not location.is_absolute():
                    raise ValueError("native runner input paths must be explicit")
                if location not in captured:
                    captured[location] = location.read_bytes()
                if core.sha(captured[location]) != expected:
                    raise ValueError("native gate captured input differs")
            for location in directory.iterdir():
                if location.is_file():
                    read(str(location.relative_to(ROOT)))
            check_id = prefix + gate
            evidence.append(
                {
                    "evidence_id": check_id,
                    "kind": "validation",
                    "reference": log_name,
                    "accessed_at": started,
                    "support": "supports",
                    "summary": "Actual native command passed for this accepted record with retained nonempty output and unchanged captured inputs.",
                }
            )
            checks.append(
                {
                    "check_id": check_id,
                    "name": recipe,
                    "status": "passed",
                    "required": True,
                    "summary": evidence[-1]["summary"],
                    "target_ids": [identity],
                    "command": shlex.join(receipt["command"]),
                    "exit_code": 0,
                    "expected_exit_code": 0,
                    "evidence_ids": [check_id],
                    "scope_note": "Scoped technical record gate, not whole-record scientific approval or corpus QC.",
                }
            )
        if sidecars is None:
            raise ValueError("actual native sidecar receipt required")
        sidecar_raw = read(unit["history_sidecar"], unit["history_sidecar_sha256"])
        sidecar = yaml.safe_load(sidecar_raw)
        if sidecar["target"]["path"] != target or not sidecar["events"]:
            raise ValueError("sidecar does not name the actual target")
        metadata_path = core.path(unit["source_metadata_output"])
        if (
            not metadata_path.is_relative_to(ROOT / "reports")
            or metadata_path.exists()
            or metadata_path in public
        ):
            raise ValueError("exclusive public metadata output required")
        metadata = {
            "contract": domain_contract.CONTRACT,
            "domain_proof": domain_item,
            "domain_observation": domain_document,
            "record": target,
            "record_id": identity,
            "source_inspection_sha256": proof_item["sha256"],
            "source_inputs": {
                name: source["inputs"][name] for name in row.get("input_paths", source["inputs"])
            },
            "occurrences": row["occurrences"],
            "primary_locators": [
                {key: item[key] for key in ("reference", "path", "character_offset", "line")}
                for item in row.get("primary_contexts", [])
            ],
            "database_observation": source.get("database_observation"),
            "historical_guard_assessment": row.get("historical_guard_assessment"),
            "scientific_review": False,
        }
        metadata_raw = (json.dumps(metadata, indent=2) + "\n").encode()
        if redactor.sanitize(metadata_raw.decode(), Counter()) != metadata_raw.decode():
            raise ValueError("public metadata contains private path or identity")
        public[metadata_path] = metadata_raw
        targets.append(
            {
                "target_id": identity,
                "path": target,
                "selector": unit["selector"],
                "label": unit["label"],
                "kind": "maintained",
                "ownership_note": "CommunityMech owns this record; only declared GTDB correspondence/status and actual provenance are assessed.",
            }
        )
        if not unit["assessments"] or any(
            item["target_ids"] != [identity] for item in unit["assessments"]
        ):
            raise ValueError("explicit authored assessments required for each exact target")
        evidence.extend({**item, "accessed_at": started} for item in unit["evidence"])
        assessments.extend(unit["assessments"])
    core.unchanged(captured, revision)
    output.mkdir(parents=True)
    for location, raw in public.items():
        location.parent.mkdir(parents=True, exist_ok=True)
        with location.open("xb") as stream:
            stream.write(raw)
        captured[location] = raw
    native = native_review()
    inspection = native.inspect_source(
        ROOT,
        targets,
        [str(location.relative_to(ROOT)) for location in captured if location.is_relative_to(ROOT)],
    )
    verify_inspection(inspection, captured, revision)
    (output / "inspection.json").write_text(json.dumps(inspection, indent=2) + "\n")
    authored = config["review"]
    review = {
        "schema_version": "1.0.0",
        "review_id": datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ") + "-" + authored["slug"],
        "kind": "record" if len(units) == 1 else "batch",
        "repository": "CultureBotAI/CommunityMech",
        "title": authored["title"],
        "started_at": started,
        "finished_at": now(),
        "reviewer": {
            "identity": "codex",
            "kind": "agent",
            "independence": "self_review",
            "independence_basis": authored["independence_basis"],
        },
        "skill": "curate-yaml-record",
        "completion": "completed",
        "verdict": "pass_with_limitations",
        "scientific_review": False,
        "summary": authored["summary"],
        "source": inspection["source"],
        "targets": targets,
        "scope": {
            "description": authored["scope_description"],
            "selection": authored["selection"],
            "coverage": "partial",
            "population_size": len(units),
            "reviewed_target_ids": [unit["target_id"] for unit in units],
            "exclusions": [
                {
                    "target": "Other scientific claims and records",
                    "reason": "Existing biology is preserved, not newly certified by this database diagnostic.",
                }
            ],
        },
        "checks": checks,
        "evidence": evidence,
        "assessments": assessments,
        "findings": authored.get("findings", []),
        "actions": [],
        "limitations": authored["limitations"],
        "links": authored["links"],
    }
    native.validate_review(review)
    core.unchanged(captured, revision)
    (output / "review.json").write_text(json.dumps(review, indent=2) + "\n")
    return {
        "review": str((output / "review.json").relative_to(ROOT)),
        "sha256": core.sha((output / "review.json").read_bytes()),
        "inputs": len(inspection["source"]["inputs"]),
        "targets": len(units),
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", required=True)
    parser.add_argument("--config-sha256", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--expected-revision", required=True)
    args = parser.parse_args()
    print(
        json.dumps(
            build(args.config, args.config_sha256, args.output, args.expected_revision), indent=2
        )
    )
