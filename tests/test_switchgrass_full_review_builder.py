"""Focused full-scope/current-byte/history controls for #1996/#2938, 2026-11-16.

Uses the public current record and authored assessment. The chain fixture retains
its actual scientific content but uses a distinct serialized fixture baseline;
no private source cache, historic Git fetch, saved review or network is required.
"""

import copy
import importlib.util
import json
import os
import sys
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts/adhoc"))
SPEC = importlib.util.spec_from_file_location(
    "switchgrass_full_builder",
    ROOT
    / os.environ.get(
        "SWITCHGRASS_REVIEW_BUILDER", "scripts/adhoc/build_switchgrass_full_review_20261116.py"
    ),
)
builder = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(builder)


@pytest.fixture
def scientific():
    authored = yaml.safe_load(
        (ROOT / "reports/switchgrass-full-review-20261116/authored-science-002.yaml").read_bytes()
    )
    return authored, (ROOT / builder.TARGET).read_bytes()


def test_complete_current_science(scientific):
    authored, current = scientific
    assert builder.validate_science(authored, current)["id"] == builder.IDENTITY


@pytest.mark.parametrize(
    "mutation",
    ["partial", "technical", "missing_section", "missing_stock", "wrong_stock", "record"],
)
def test_full_science_refuses_scope_or_identity_changes(scientific, mutation):
    authored, current = scientific
    if mutation == "partial":
        authored["coverage"] = "partial"
    elif mutation == "technical":
        authored["scientific_review"] = False
    elif mutation == "missing_section":
        authored["sections"].pop()
    elif mutation == "missing_stock":
        authored["stocks"].pop()
    elif mutation == "wrong_stock":
        authored["stocks"][1]["stock"] = "OAE603"
    else:
        current += b"\n# changed current record\n"
    with pytest.raises(ValueError):
        builder.validate_science(authored, current)


@pytest.fixture
def chain(scientific, monkeypatch):
    _, current = scientific
    original = yaml.safe_load(current)
    original["curation_history"].pop()
    for row in builder.locator.CELLS:
        original["discussions"][4]["evidence"][row].pop("source_locator")
    original = yaml.safe_dump(original, sort_keys=False, allow_unicode=True, width=110).encode()
    before_sha = builder.capture_core.sha(original)
    monkeypatch.setattr(builder.locator, "BEFORE", before_sha)
    plan = {"controls": {"selected": {"sha256": "a" * 64}}}
    candidate, _, event = builder.locator.render_candidate(original, plan, "2026-11-16T00:24:59Z")
    after_sha = builder.capture_core.sha(candidate)
    monkeypatch.setattr(builder, "AFTER", after_sha)
    old = [
        {"target": builder.TARGET, "before_sha256": builder.ORIGINAL, "after_sha256": "1" * 64},
        {"target": builder.TARGET, "before_sha256": "1" * 64, "after_sha256": "2" * 64},
        {"target": builder.TARGET, "before_sha256": "2" * 64, "after_sha256": before_sha},
    ]
    applied = {
        "applied": True,
        "target": builder.TARGET,
        "scope": builder.locator.SCOPE,
        "before_sha256": before_sha,
        "after_sha256": after_sha,
        "appended_native_inline_history": event,
    }
    return original, candidate, plan, applied, old


def test_exact_chain_then_historical_and_scientific_mutations_restore(chain):
    original, candidate, plan, applied, old = chain
    builder.validate_chain(*chain)
    for field in ("curation_history", "description"):
        document = yaml.safe_load(candidate)
        if field == "curation_history":
            document[field][0]["changes"] += " altered"
        else:
            document[field] += " invented biological claim"
        altered = yaml.safe_dump(document, sort_keys=False).encode()
        with pytest.raises(ValueError):
            builder.validate_chain(original, altered, plan, applied, old)
        builder.validate_chain(*chain)
    broken = copy.deepcopy(old)
    broken[1]["before_sha256"] = "3" * 64
    with pytest.raises(ValueError, match="not contiguous"):
        builder.validate_chain(original, candidate, plan, applied, broken)
    builder.validate_chain(*chain)


def test_rehashed_history_change_is_not_admitted(chain, monkeypatch):
    original, candidate, plan, applied, old = chain
    changed = yaml.safe_load(candidate)
    changed["curation_history"][0]["changes"] += " altered old event"
    changed = yaml.safe_dump(changed, sort_keys=False).encode()
    monkeypatch.setattr(builder, "AFTER", builder.capture_core.sha(changed))
    applied["after_sha256"] = builder.AFTER
    with pytest.raises(ValueError, match="candidate bytes or native event"):
        builder.validate_chain(original, changed, plan, applied, old)


@pytest.fixture
def measured(scientific):
    _, current = scientific
    # Exact current normal-configuration result, byte-identical on both hosts.
    # Metadata contains assertion hashes/identities/counters, not source bodies.
    raw = (ROOT / "tests/fixtures/switchgrass-current-measurement-20261116.json").read_bytes()
    assert (
        builder.capture_core.sha(raw)
        == "b7db232076e7d7d53e969011d53b5f0a770bbd553575b6e902a5b321f81dff66"
    )
    result = json.loads(raw)
    receipt = {
        "revision": "a" * 40,
        "selected_records": [builder.TARGET],
        "inputs_unchanged": True,
        "changed_input_paths": [],
        "exit_code": 0,
        "input_sha256": {builder.TARGET: builder.AFTER},
        "cases": [result],
    }
    return receipt, result, current, "a" * 40


def test_full_current_measurement(measured):
    builder.validate_coverage(*measured)


@pytest.mark.parametrize("mutation", ["target", "coverage", "exit", "surface", "source"])
def test_consistently_changed_measurement_cannot_claim_full_success(measured, mutation):
    receipt, result, current, revision = measured
    if mutation == "target":
        result["records"][0]["record"] = "kb/communities/other.yaml"
    elif mutation == "coverage":
        result["assertion_coverage_complete"] = False
    elif mutation == "exit":
        result["native_exit_code"] = 1
    elif mutation == "surface":
        result["records"][0]["assertions"][0]["text_sha256"] = "b" * 64
    else:
        result["records"][0]["assertions"][0]["source_binding_consistent"] = False
    # Both result and final receipt agree; consistency alone must not admit them.
    assert json.loads(json.dumps(receipt))["cases"] == [result]
    with pytest.raises(ValueError):
        builder.validate_coverage(receipt, result, current, revision)


@pytest.mark.parametrize(
    "mutation",
    [
        "compared",
        "valid",
        "validated_text",
        "validated_path",
        "validated_reference",
        "validator_calls",
        "matcher_calls",
        "substring_calls",
        "substring_parts_compared",
        "aggregate_calls",
        "aggregate_completed",
        "errors",
        "native_validation",
        "processing",
        "record_completed",
        "record_issues",
        "title_only",
        "changed_inputs",
    ],
)
def test_actual_measurement_counter_refusal_and_restoration(measured, mutation):
    receipt, result, current, revision = measured
    builder.validate_coverage(*measured)
    original_receipt, original_result = copy.deepcopy(receipt), copy.deepcopy(result)
    assertion = result["records"][0]["assertions"][0]
    if mutation == "compared":
        assertion["actually_compared"] = False
    elif mutation == "valid":
        assertion["is_valid"] = False
    elif mutation.startswith("validated_"):
        assertion[mutation] = "different"
        if mutation == "validated_text":
            assertion["validated_text_sha256"] = "b" * 64
    elif mutation in {
        "validator_calls",
        "matcher_calls",
        "substring_calls",
        "substring_parts_compared",
    }:
        assertion[mutation] = 0
    elif mutation == "aggregate_calls":
        result["counts"]["matcher_calls"] = 0
    elif mutation == "aggregate_completed":
        result["counts"]["records_completed"] = 0
    elif mutation == "errors":
        result["errors"] = ["native error"]
    elif mutation == "native_validation":
        result["native_validation_passed"] = False
    elif mutation == "processing":
        result["record_processing_complete"] = False
    elif mutation == "record_completed":
        result["records"][0]["completed"] = False
    elif mutation == "record_issues":
        result["records"][0]["native_issue_count"] = 1
    elif mutation == "title_only":
        result["records"][0]["title_only"] = ["unexpected title"]
    else:
        receipt["changed_input_paths"] = [builder.TARGET]
    # Preserve result/final-receipt agreement and recompute their byte digests.
    assert receipt["cases"] == [result]
    assert builder.capture_core.sha(json.dumps(receipt).encode())
    assert builder.capture_core.sha(json.dumps(result).encode())
    with pytest.raises(ValueError):
        builder.validate_coverage(receipt, result, current, revision)
    original_receipt["cases"] = [original_result]
    builder.validate_coverage(original_receipt, original_result, current, revision)


@pytest.fixture
def full_payload(scientific):
    authored, current = scientific
    config = yaml.safe_load(
        (ROOT / "reports/switchgrass-full-review-20261116/review-config-004.yaml").read_bytes()
    )
    accessed = builder.now()
    evidence = [
        {
            "evidence_id": key,
            "kind": spec["kind"],
            "reference": spec["path"],
            "snapshot_sha256": spec["sha256"],
            "accessed_at": accessed,
            "locator": spec["locator"],
            "support": spec.get("support", "supports"),
            "summary": spec["summary"],
        }
        for key, spec in config["evidence"].items()
    ]
    checks = []
    for name, recipe in builder.RECIPES.items():
        evidence.append(
            {
                "evidence_id": "check-" + name,
                "kind": "validation",
                "reference": "fixture",
                "accessed_at": accessed,
                "support": "supports",
                "summary": "Native payload shape fixture; no execution claimed.",
            }
        )
        checks.append(
            {
                "check_id": name,
                "name": recipe,
                "required": True,
                "target_ids": [builder.IDENTITY],
                "status": "failed" if name == "network" else "passed",
                "command": "fixture command",
                "exit_code": 1 if name == "network" else 0,
                "expected_exit_code": 0,
                "summary": "Shape fixture",
                "evidence_ids": ["check-" + name],
            }
        )
    assessments = [
        {
            "assessment_id": "lbnl-" + section["id"],
            "target_ids": [builder.IDENTITY],
            "area": section["area"],
            "topic": section["topic"],
            "outcome": section["outcome"],
            "summary": section["summary"],
            "evidence_ids": section["evidence"],
        }
        for section in authored["sections"]
    ]
    assessments.extend(
        {
            "assessment_id": "lbnl-stock-" + stock["stock"].lower(),
            "target_ids": [builder.IDENTITY],
            "area": "grounding",
            "topic": f"{stock['stock']}: {stock['genus']} / DSM {stock['dsm']}",
            "outcome": "supported",
            "summary": stock["detail"] + " " + authored["stock_scope"],
            "evidence_ids": ["record", "primary", "grounding"],
            "details": (
                f"taxonomy[{stock['index']}]; {stock['ncbi']}; "
                f"native stored status {stock['status']}"
            ),
        }
        for stock in authored["stocks"]
    )
    source = {
        "git_revision": "a" * 40,
        "state": "working_tree",
        "inputs": [{"path": builder.TARGET, "sha256": builder.AFTER, "role": "target"}],
    }
    return builder.make_review(
        config,
        authored,
        yaml.safe_load(current),
        source,
        evidence,
        assessments,
        checks,
        {"review_id": "20261115T031503Z-phase2-three-record-final-science"},
        accessed,
    )


def test_complete_native_payload_is_schema_and_semantics_valid(full_payload):
    assert len(full_payload["assessments"]) == 30
    assert len(full_payload["checks"]) == 10
    builder.native_review().validate_review(full_payload)


@pytest.mark.parametrize(
    "mutation", ["target_owner", "finding_owner", "action_owner", "terminal_lineage", "issue_key"]
)
def test_native_payload_retains_owner_and_true_lineage_contract(full_payload, mutation):
    native = builder.native_review()
    native.validate_review(full_payload)
    changed = copy.deepcopy(full_payload)
    if mutation.endswith("owner"):
        item = changed[
            {"target_owner": "targets", "finding_owner": "findings", "action_owner": "actions"}[
                mutation
            ]
        ][0]
        item.pop("owner_paths")
        item.pop("ownership_note")
    elif mutation == "terminal_lineage":
        changed["findings"][1].pop("previous_occurrences")
    else:
        changed["findings"][1].pop("issue_key")
    with pytest.raises(native.ReviewError):
        native.validate_review(changed)
    native.validate_review(full_payload)


@pytest.mark.parametrize("mutation", [None, "target_finding", "error_type", "success_exit"])
def test_corpus_warning_gate_cannot_be_promoted_or_hide_target_failure(mutation):
    report = {"Other_Record": [{"type": "DISCONNECTED"}]}
    if mutation == "target_finding":
        report[Path(builder.TARGET).stem] = [{"type": "DISCONNECTED"}]
    elif mutation == "error_type":
        report["Other_Record"][0]["type"] = "UNKNOWN_PARTICIPANT"
    prefix = (
        b"===> Running recipe `audit-network-json`...\nuv run communitymech audit-network --json\n"
    )
    tail = b"error: Recipe `audit-network-json` failed on line 603 with exit code 1\n"
    log = prefix + json.dumps(report).encode() + b"\n" + tail
    receipt = {
        "command": ["just", "--verbose", "--no-dotenv", "--color", "never", "audit-network-json"],
        "head": "a" * 40,
        "status": "FAILED",
        "exit_code": 0 if mutation == "success_exit" else 1,
        "log_sha256": builder.capture_core.sha(log),
        "log_bytes": len(log),
    }
    receipt_raw = json.dumps(receipt).encode()
    files = {"gate.json": receipt_raw, "gate.log": log, "gate.exit": b"1\n"}

    def read(name, expected=None):
        raw = files[name] if name in files else (ROOT / name).read_bytes()
        assert expected is None or builder.capture_core.sha(raw) == expected
        return raw

    spec = {
        "prefix": "gate",
        "receipt_sha256": builder.capture_core.sha(receipt_raw),
        "execution_revision": "a" * 40,
    }
    if mutation:
        with pytest.raises(ValueError):
            builder.read_gate("network", spec, read)
    else:
        assert builder.read_gate("network", spec, read)["exit_code"] == 1


@pytest.mark.parametrize("mutation", [None, "native_error", "unknown_type"])
def test_retained_network_report_honors_native_override_and_refuses_errors(mutation):
    raw = (ROOT / "tests/fixtures/switchgrass-network-audit-20261116.log").read_bytes()
    assert (
        builder.capture_core.sha(raw)
        == "63fb4c218806e2e94157fe71ed0554bca87d859880cbeed60f26cbb202285ac7"
    )
    prefix = (
        b"===> Running recipe `audit-network-json`...\nuv run communitymech audit-network --json\n"
    )
    tail = b"error: Recipe `audit-network-json` failed on line 603 with exit code 1\n"
    report = json.loads(raw[len(prefix) : -len(tail)])
    override = next(
        row for rows in report.values() for row in rows if row["type"] == "UNKNOWN_TARGET"
    )
    assert override["severity"] == "warning"
    if mutation:
        override.pop("severity")
        if mutation == "unknown_type":
            override["type"] = "UNKNOWN_NEW_TYPE"
        raw = prefix + json.dumps(report).encode() + b"\n" + tail
    receipt = {
        "command": ["just", "--verbose", "--no-dotenv", "--color", "never", "audit-network-json"],
        "head": "a" * 40,
        "status": "FAILED",
        "exit_code": 1,
        "log_sha256": builder.capture_core.sha(raw),
        "log_bytes": len(raw),
    }
    receipt_raw = json.dumps(receipt).encode()
    files = {"gate.json": receipt_raw, "gate.log": raw, "gate.exit": b"1\n"}

    def read(name, expected=None):
        data = files[name] if name in files else (ROOT / name).read_bytes()
        assert expected is None or builder.capture_core.sha(data) == expected
        return data

    spec = {
        "prefix": "gate",
        "receipt_sha256": builder.capture_core.sha(receipt_raw),
        "execution_revision": "a" * 40,
    }
    if mutation:
        with pytest.raises(ValueError, match="finding severity"):
            builder.read_gate("network", spec, read)
        restored = (ROOT / "tests/fixtures/switchgrass-network-audit-20261116.log").read_bytes()
        receipt.update(log_sha256=builder.capture_core.sha(restored), log_bytes=len(restored))
        files.update({"gate.json": json.dumps(receipt).encode(), "gate.log": restored})
        spec["receipt_sha256"] = builder.capture_core.sha(files["gate.json"])
        assert builder.read_gate("network", spec, read)["exit_code"] == 1
    else:
        assert builder.read_gate("network", spec, read)["exit_code"] == 1
