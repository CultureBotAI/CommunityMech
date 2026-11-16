"""Bind a new full Switchgrass assessment to exact current evidence, 2026-11-16.

Inputs: pinned authored judgments, source/application/history artifacts, completed
native commands and current Git-bound reference coverage (#1996/#1548/#2938).
Output: one exclusive private native inspection/review draft. No canonical, cache,
history, saved-review or existing assessment mutation; native save stays separate.
"""

import argparse
import importlib.util
import json
import shlex
from datetime import datetime, timezone
from pathlib import Path

import curate_switchgrass_source_locators_20261115 as locator
import gtdb_batch_curation_20261115 as capture_core
import yaml
from build_gtdb_batch_diagnostic_20261115 import native_review, verify_inspection

ROOT = Path(__file__).resolve().parents[2]
TARGET = locator.TARGET
IDENTITY = "CommunityMech:000087"
AFTER = "bcc2759c9da7c4059330726a1b154df600ec394d1106be2dcc1f4d247eed5eb9"
ORIGINAL = "58bb996c6056821c2e5bf3d3494108826b3f836c79fc95f0c07db967e65b04e4"
PRIOR = "reviews/structured/20261115T031503Z-phase2-three-record-final-science/review.yaml"
PRIOR_SHA = "8c0858a89c224421ab05a9a7a02cdb882e501f687fe5fef24a7d56ef4fc26563"
APPLICATION_SHA = "54eead0a6475128efde3a1afb2250b7ba75ff369b1c2253a53650caeed7f2983"
OLD_CHAIN = (
    (
        ".temp/phase2-science-20261115/curation-applied-001/receipt.json",
        "c6e08b2fe8c7e26f49ff1c0f2032887d60973e017a16788c63e6733a6ce49fd3",
    ),
    (
        ".temp/phase2-science-20261115/mapping-note-applied-001/receipt.json",
        "9034e937ade286fd15fda8e174e52b3363417aaac68c9c975a9e5ac4ed22cb5e",
    ),
    (
        ".temp/phase2-science-20261115/linked-stock-plan-003/lbnl/apply/receipt.json",
        "5aeb0e2a5b9e97f5ec9eb7f8251f9bc481bc26d70ec5c0136bda74b9cd9d7ec9",
    ),
)
SECTIONS = {
    "identity",
    "environment",
    "media",
    "nutrient",
    "ratios",
    "host",
    "mechanisms",
    "source-locators",
    "relations",
    "taxonomy-populations",
}
RECIPES = {
    "schema": "validate",
    "strict": "validate-strict",
    "new-history": "new-history",
    "history": "validate-history",
    "gtdb": "validate-gtdb",
    "domain": "validate-gtdb-domain",
    "scalars": "validate-scalars",
    "terms": "validate-terms",
    "references": "validate-references",
    "network": "audit-network-json",
}


def now():
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def validate_science(authored, current):
    """Full coverage cannot be supplied by a taxonomy-only or stale document."""
    record = yaml.safe_load(current)
    if (
        authored["target"] != IDENTITY
        or authored["path"] != TARGET
        or authored["after_sha256"] != AFTER
        or capture_core.sha(current) != AFTER
        or authored["before_sha256"] != locator.BEFORE
        or authored["coverage"] != "full"
        or authored["scientific_review"] is not True
        or authored["verdict"] != "needs_curation"
        or record["id"] != IDENTITY
    ):
        raise ValueError("exact current whole-record scientific assessment required")
    sections = authored["sections"]
    if len(sections) != len(SECTIONS) or {s["id"] for s in sections} != SECTIONS:
        raise ValueError("all separately authored scientific sections required")
    covered = {p.split(".")[0].split("[")[0] for s in sections for p in s["fields"]}
    if set(record) - covered - {"curation_history"}:
        raise ValueError("populated top-level fields lack scientific assessment")
    stocks = authored["stocks"]
    if len(stocks) != 16 or [s["index"] for s in stocks] != list(range(16)):
        raise ValueError("all sixteen individually indexed stock assessments required")
    if len(record["taxonomy"]) != 16 or record.get("ecological_interactions"):
        raise ValueError("reviewed sixteen-stock zero-node scope changed")
    for stock, taxon in zip(stocks, record["taxonomy"], strict=True):
        term, strain = taxon["taxon_term"], taxon["strain_designation"]
        if (
            term["term"]["id"] != stock["ncbi"]
            or term["gtdb_grounding_status"] != stock["status"]
            or strain["strain_name"] != stock["stock"]
            or [(c["collection"], str(c["accession"])) for c in strain["culture_collections"]]
            != [("DSM", stock["dsm"])]
        ):
            raise ValueError("authored stock/deposit/taxon identity differs")
    return record


def validate_chain(original, current, plan, applied, old_receipts):
    previous = ORIGINAL
    if len(old_receipts) != 3:
        raise ValueError("three immutable prior applications required")
    for receipt in old_receipts:
        if receipt["target"] != TARGET or receipt["before_sha256"] != previous:
            raise ValueError("original-to-prior application chain is not contiguous")
        previous = receipt["after_sha256"]
    if previous != locator.BEFORE or capture_core.sha(original) != locator.BEFORE:
        raise ValueError("exact immediately preceding record required")
    if (
        applied.get("applied") is not True
        or applied["target"] != TARGET
        or applied["scope"] != locator.SCOPE
        or applied["before_sha256"] != locator.BEFORE
        or applied["after_sha256"] != AFTER
        or capture_core.sha(current) != AFTER
    ):
        raise ValueError("actual locator application differs")
    _, event = locator.verify_candidate(original, current, plan)
    if event != applied["appended_native_inline_history"]:
        raise ValueError("new inline event differs from the actual receipt")


def validate_coverage(receipt, result, current, revision):
    if (
        receipt["revision"] != revision
        or receipt["selected_records"] != [TARGET]
        or receipt.get("inputs_unchanged") is not True
        or receipt.get("changed_input_paths") != []
        or receipt["exit_code"] != 0
        or receipt["input_sha256"].get(TARGET) != AFTER
        or receipt["cases"] != [result]
        or result["case"] != "measurement"
        or result["input_sha256"] != {TARGET: AFTER}
        or result.get("measurement_valid") is not True
        or result.get("validation_passed") is not True
        or result.get("native_validation_passed") is not True
        or result.get("record_processing_complete") is not True
        or result.get("assertion_coverage_complete") is not True
        or result["native_exit_code"] != 0
        or result.get("errors") != []
        or result["assertion_status_counts"] != {"matched": 37}
        or result["counts"]
        != {
            "records_selected": 1,
            "records_completed": 1,
            "snippet_surfaces": 37,
            "snippet_occurrences_compared": 37,
            "excerpt_validator_invocations": 37,
            "matcher_calls": 37,
            "substring_calls": 37,
            "substring_parts_compared": 37,
            "title_only_invocations": 0,
            "native_issues": 0,
        }
        or len(result["records"]) != 1
        or result["records"][0]["record"] != TARGET
        or result["records"][0].get("completed") is not True
        or result["records"][0].get("native_issue_count") != 0
        or result["records"][0].get("title_only") != []
    ):
        raise ValueError("complete current 37-surface native measurement required")
    expected = {
        p: (capture_core.sha(text.encode()), reference)
        for p, text, reference in locator.surfaces(yaml.safe_load(current))
    }
    assertions = result["records"][0]["assertions"]
    actual = {a["path"]: (a["text_sha256"], a["expected_reference"]) for a in assertions}
    if (
        len(assertions) != 37
        or actual != expected
        or any(
            a["status"] != "matched"
            or a.get("actually_compared") is not True
            or a.get("is_valid") is not True
            or any(
                a.get(field) != 1
                for field in (
                    "validator_calls",
                    "matcher_calls",
                    "substring_calls",
                    "substring_parts_compared",
                )
            )
            or a.get("reference_binding_consistent") is not True
            or a.get("source_binding_consistent") is not True
            or a.get("validated_path") != a["path"]
            or a.get("validated_text_sha256") != a["text_sha256"]
            or a.get("validated_reference") != a["expected_reference"]
            for a in assertions
        )
    ):
        raise ValueError("measured paths, texts, references or source bindings differ")


def read_gate(name, spec, read):
    receipt = json.loads(read(spec["prefix"] + ".json", spec["receipt_sha256"]))
    log = read(spec["prefix"] + ".log", receipt["log_sha256"])
    exit_raw = read(spec["prefix"] + ".exit")
    command = receipt["command"]
    indexes = [i for i, token in enumerate(command) if Path(token).name == "just"]
    if len(indexes) != 1:
        raise ValueError("one actual native just invocation required")
    suffix = command[indexes[0] + 1 :]
    expected_exit = 1 if name == "network" else 0
    expected_status = "FAILED" if expected_exit else "PASSED"
    if (
        suffix[:5] != ["--verbose", "--no-dotenv", "--color", "never", RECIPES[name]]
        or receipt["head"] != spec["execution_revision"]
        or receipt["status"] != expected_status
        or receipt["exit_code"] != expected_exit
        or exit_raw.strip() != str(expected_exit).encode()
        or len(log) != receipt["log_bytes"]
        or not log
    ):
        raise ValueError("native command identity or persisted result differs")
    if name not in {"new-history", "history", "network"} and TARGET not in suffix[5:]:
        raise ValueError("native command does not name the exact current record")
    if name == "network" and suffix[5:]:
        raise ValueError("actual full-corpus network recipe required")
    if name == "network":
        prefix = b"===> Running recipe `audit-network-json`...\nuv run communitymech audit-network --json\n"
        tail = b"error: Recipe `audit-network-json` failed on line 603 with exit code 1\n"
        if not log.startswith(prefix) or not log.endswith(tail):
            raise ValueError("retained native network stdout framing differs")
        report = json.loads(log[len(prefix) : -len(tail)])
        if not isinstance(report, dict) or not report or Path(TARGET).stem in report:
            raise ValueError("expected corpus warnings and no Switchgrass finding")
        # Native per-finding overrides distinguish community-level unresolved
        # participants from error-level unknown targets. Do not copy a type list.
        auditor_path = ROOT / "src/communitymech/network/auditor.py"
        auditor_raw = read(str(auditor_path.relative_to(ROOT)))
        read("src/communitymech/paths.py")
        auditor_spec = importlib.util.spec_from_file_location(
            "captured_network_severity", auditor_path
        )
        auditor = importlib.util.module_from_spec(auditor_spec)
        exec(compile(auditor_raw, str(auditor_path), "exec"), auditor.__dict__)  # noqa: S102
        if any(
            auditor.issue_severity(item) != "warning" for rows in report.values() for item in rows
        ):
            raise ValueError("network report contains a different finding severity")
    if name == "history" and suffix[5:] != ["history/records/LBNL_Switchgrass_Soil_SynCom16"]:
        raise ValueError("native history command names a different namespace")
    if name == "new-history" and any(
        flag not in suffix or suffix[suffix.index(flag) + 1] != value
        for flag, value in {
            "--kind": "record",
            "--slug": "LBNL_Switchgrass_Soil_SynCom16",
            "--target-root": "kb/communities",
            "--event": "EDIT",
            "--outcome": "changed",
            "--sections": "discussions,curation_history",
        }.items()
    ):
        raise ValueError("native new-history command scope differs")
    return receipt


def make_review(config, authored, record, source, evidence, assessments, checks, prior, started):
    """Assemble the same complete native payload for production and contract tests."""
    final_assessments = config["final_assessments"]
    if (
        len(final_assessments) != 4
        or {a["assessment_id"] for a in final_assessments}
        != {"lbnl-history", "lbnl-current-coverage", "lbnl-metrics", "lbnl-native-corpus-boundary"}
        or any(a["target_ids"] != [IDENTITY] for a in final_assessments)
        or not any(
            f["finding_id"] == "cm-000087-member-roster"
            and f["status"] == "open"
            and f["target_ids"] == [IDENTITY]
            and "https://github.com/CultureBotAI/CommunityMech/issues/1548" in f["external_issues"]
            for f in config["findings"]
        )
    ):
        raise ValueError(
            "complete provenance/coverage/metric assessments and open roster finding required"
        )
    finished = now()
    return {
        "schema_version": "1.0.0",
        "review_id": datetime.fromisoformat(finished.replace("Z", "+00:00")).strftime(
            "%Y%m%dT%H%M%SZ"
        )
        + "-switchgrass-full-source-successor",
        "kind": "record",
        "repository": "CultureBotAI/CommunityMech",
        "title": "Full Switchgrass assessment after explicit supplement source routing",
        "started_at": started,
        "finished_at": finished,
        "reviewer": {
            "identity": "codex",
            "kind": "agent",
            "independence": "self_review",
            "independence_basis": authored["independence_basis"],
        },
        "skill": "review-yaml-record",
        "completion": "completed",
        "verdict": authored["verdict"],
        "scientific_review": True,
        "summary": authored["summary"],
        "source": source,
        "targets": [review_target(record)],
        "scope": {
            "description": authored["scope_description"],
            "selection": "One complete current record after direct primary-source reread and a bounded locator-only correction.",
            "coverage": "full",
            "population_size": 1,
            "reviewed_target_ids": [IDENTITY],
        },
        "checks": checks,
        "evidence": evidence,
        "assessments": assessments + final_assessments,
        "findings": config["findings"],
        "actions": config["actions"],
        "limitations": authored["limitations"] + config["execution_limitations"],
        "notes": config["correction_notes"],
        "related_reviews": [
            {
                "repository": "CultureBotAI/CommunityMech",
                "review_id": prior["review_id"],
                "relationship": "Full current successor; preserves historical failures and evidence, corrects two prior prose errors, and retains the open stock-correspondence finding.",
            }
        ],
        "links": [
            f"https://github.com/CultureBotAI/CommunityMech/issues/{i}"
            for i in (1996, 1548, 2938, 2940, 2941, 2942, 2943, 2944)
        ],
    }


def review_target(record):
    return {
        "target_id": IDENTITY,
        "path": TARGET,
        "label": record["name"],
        "kind": "maintained",
        "owner_paths": [
            {
                "repository": "CultureBotAI/CommunityMech",
                "path": TARGET,
                "role": "maintained record",
            }
        ],
        "ownership_note": "Scientific content is maintained in this record; the new review does not edit it.",
    }


def build(config_name, config_sha, output_name, revision):
    output = capture_core.path(output_name, private=True)
    if output.exists() or capture_core.head() != revision:
        raise ValueError("exclusive private output and frozen inspection revision required")
    captured = {}

    def read(name, expected=None):
        return capture_core.capture(captured, name, expected)

    config = yaml.safe_load(read(config_name, config_sha))
    authored = yaml.safe_load(read(config["authored"]["path"], config["authored"]["sha256"]))
    for name, expected in config["inputs"].items():
        read(name, expected)
    for name in (
        str(Path(__file__).relative_to(ROOT)),
        str(Path(capture_core.__file__).relative_to(ROOT)),
        str(Path(locator.__file__).relative_to(ROOT)),
        "scripts/adhoc/build_gtdb_batch_diagnostic_20261115.py",
        "scripts/record_review.py",
        "schema/record_review.yaml",
        "pyproject.toml",
        "uv.lock",
    ):
        read(name)
    current = read(TARGET, AFTER)
    record = validate_science(authored, current)
    prior = yaml.safe_load(read(PRIOR, PRIOR_SHA))
    old = [json.loads(read(name, expected)) for name, expected in OLD_CHAIN]
    application = config["application"]
    applied_raw = read(application["path"], APPLICATION_SHA)
    applied = json.loads(applied_raw)
    read(
        str(Path(locator.__file__).relative_to(ROOT)),
        applied["inputs"][str(Path(locator.__file__).absolute())],
    )
    original = read(application["before_path"], locator.BEFORE)
    plan = json.loads(read(application["plan_path"], application["plan_sha256"]))
    validate_chain(original, current, plan, applied, old)
    stage = json.loads(
        read(applied["reviewed_receipt"]["path"], applied["reviewed_receipt"]["sha256"])
    )
    if (
        stage["inputs"] != applied["inputs"]
        or stage["appended_native_inline_history"] != applied["appended_native_inline_history"]
    ):
        raise ValueError("reviewed stage and actual application differ")
    sidecar = yaml.safe_load(read(config["sidecar"]["path"], config["sidecar"]["sha256"]))
    if sidecar["target"]["path"] != TARGET or not any(
        event["type"] == "EDIT"
        and event["outcome"] == "changed"
        and set(event["sections"]) == {"discussions", "curation_history"}
        and application["path"] in event["details"]
        and APPLICATION_SHA in event["details"]
        and AFTER in event["details"]
        for event in sidecar["events"]
    ):
        raise ValueError("actual native sidecar does not bind this locator transition")
    history_dir = ROOT / "history/records/LBNL_Switchgrass_Soil_SynCom16"
    history_names = {str(p.relative_to(ROOT)) for p in history_dir.glob("*.yaml")}
    if history_names != set(config["history_inputs"]):
        raise ValueError("complete current native history namespace required")
    for name, expected in config["history_inputs"].items():
        read(name, expected)
    for item in prior["source"]["inputs"]:
        if item["path"].startswith("history/records/LBNL_Switchgrass_Soil_SynCom16/"):
            read(item["path"], item["sha256"])
    if set(config["gates"]) != set(RECIPES):
        raise ValueError("all ten actual native command observations required")
    gates = {name: read_gate(name, spec, read) for name, spec in config["gates"].items()}
    coverage = config["coverage"]
    measured = json.loads(read(coverage["receipt"], coverage["receipt_sha256"]))
    result = json.loads(read(coverage["result"], coverage["result_sha256"]))
    read(coverage["log"], coverage["log_sha256"])
    validate_coverage(measured, result, current, coverage["revision"])
    # Use the existing native complete-input inventory on the exact declared
    # record set. Only explicitly loaded scientific sources are archived below.
    measurement_path = ROOT / "scripts/reference_assertion_coverage.py"
    measurement_raw = read(str(measurement_path.relative_to(ROOT)), measured["script_sha256"])
    module_spec = importlib.util.spec_from_file_location(
        "switchgrass_measured_inventory", measurement_path
    )
    measurement = importlib.util.module_from_spec(module_spec)
    # Execute the exact hash-bound local native module snapshot, avoiding a second
    # uncaptured filesystem read by the import loader.
    exec(  # noqa: S102
        compile(measurement_raw, str(measurement_path), "exec"), measurement.__dict__
    )
    measured_revision, declared = measurement.declared_records(ROOT)
    if (
        measured_revision != coverage["revision"]
        or declared != measured["declared_records"]
        or measurement.input_manifest(ROOT, declared) != measured["input_sha256"]
    ):
        raise ValueError("complete current measurement inventory differs")
    # Bind every reviewed current configuration/loaded source/measurement helper
    # explicitly; the complete runtime inventory remains an independently checked
    # receipt, not a claim that unrelated cache bodies were manually inspected.
    for name in coverage["required_current_inputs"]:
        if name not in measured["input_sha256"]:
            raise ValueError("measurement omits a required current source/configuration")
        read(name, measured["input_sha256"][name])
    started = now()
    evidence = []
    for identifier, spec in config["evidence"].items():
        raw = read(spec["path"], spec["sha256"])
        evidence.append(
            {
                "evidence_id": identifier,
                "kind": spec["kind"],
                "reference": spec["path"],
                "snapshot_sha256": capture_core.sha(raw),
                "accessed_at": started,
                "locator": spec["locator"],
                "support": spec.get("support", "supports"),
                "summary": spec["summary"],
            }
        )
    assessments = [
        {
            "assessment_id": "lbnl-" + s["id"],
            "target_ids": [IDENTITY],
            "area": s["area"],
            "topic": s["topic"],
            "outcome": s["outcome"],
            "summary": s["summary"],
            "evidence_ids": s["evidence"],
            "details": "Assessed fields: " + ", ".join(s["fields"]),
        }
        for s in authored["sections"]
    ]
    for stock in authored["stocks"]:
        assessments.append(
            {
                "assessment_id": "lbnl-stock-" + stock["stock"].lower(),
                "target_ids": [IDENTITY],
                "area": "grounding",
                "topic": f"{stock['stock']}: {stock['genus']} / DSM {stock['dsm']}",
                "outcome": "supported",
                "summary": stock["detail"] + " " + authored["stock_scope"],
                "evidence_ids": ["record", "primary", "grounding"],
                "details": f"taxonomy[{stock['index']}]; {stock['ncbi']}; native stored status {stock['status']}",
            }
        )
    checks = []
    for name, receipt in gates.items():
        evidence.append(
            {
                "evidence_id": "check-" + name,
                "kind": "validation",
                "reference": config["gates"][name]["prefix"] + ".log",
                "snapshot_sha256": receipt["log_sha256"],
                "accessed_at": started,
                "support": "supports",
                "summary": (
                    "The actual corpus network command exited one for warnings; "
                    "Switchgrass has no reported network finding."
                    if name == "network"
                    else "Actual native command and original execution revision are preserved."
                ),
            }
        )
        checks.append(
            {
                "check_id": name,
                "name": RECIPES[name],
                "status": "failed" if name == "network" else "passed",
                "required": True,
                "target_ids": [IDENTITY],
                "command": shlex.join(receipt["command"]),
                "exit_code": receipt["exit_code"],
                "expected_exit_code": 0,
                "evidence_ids": ["check-" + name],
                "scope_note": "The network recipe covers the corpus; other commands cover the stated record/history. The native recorder records execution, not a per-input hash capture.",
                "summary": (
                    "Corpus network audit returned warning exit one; the target has no reported network finding."
                    if name == "network"
                    else "Actual completed native command passed; scientific interpretation is assessed separately."
                ),
            }
        )
    capture_core.unchanged(captured, revision)
    targets = [review_target(record)]
    native = native_review()
    inspection = native.inspect_source(ROOT, targets, [str(p.relative_to(ROOT)) for p in captured])
    verify_inspection(inspection, captured, revision)
    review = make_review(
        config,
        authored,
        record,
        inspection["source"],
        evidence,
        assessments,
        checks,
        prior,
        started,
    )
    native.validate_review(review)
    capture_core.unchanged(captured, revision)
    if {str(p.relative_to(ROOT)) for p in history_dir.glob("*.yaml")} != history_names:
        raise ValueError("current history namespace changed during review preparation")
    if measurement.input_manifest(ROOT, declared) != measured["input_sha256"]:
        raise ValueError("complete measurement inventory changed during review preparation")
    output.mkdir(parents=True)
    for name, value in (("inspection.json", inspection), ("review.json", review)):
        with (output / name).open("x") as handle:
            json.dump(value, handle, indent=2)
            handle.write("\n")
    return {
        "review": str((output / "review.json").relative_to(ROOT)),
        "sha256": capture_core.sha((output / "review.json").read_bytes()),
        "inputs": len(inspection["source"]["inputs"]),
        "assessments": len(review["assessments"]),
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    for option in ("config", "config-sha256", "output", "expected-revision"):
        parser.add_argument("--" + option, required=True)
    args = parser.parse_args()
    print(
        json.dumps(
            build(args.config, args.config_sha256, args.output, args.expected_revision), indent=2
        )
    )
