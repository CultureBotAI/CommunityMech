"""Prove the fixed471 source correction before ordinary mapping admission.

#2898/#2899/#2910, 2026-11-15. Inputs are exact public identity and mapping
proofs plus immutable Git baselines. No source acquisition, record writes or
scientific approval. Existing notes-only and mapping-only guards stay unchanged.
"""

import copy
import json
import re
import shlex
import sys
from pathlib import Path

import scoped_gtdb_successor as mapping
import source_note_gtdb_successor as notes
import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts/adhoc"))
import build_wetland_identity_diagnostic_20261115 as diagnostic  # noqa: E402
import export_wetland_identity_evidence_20261115 as publisher  # noqa: E402

TARGET = diagnostic.identity.TARGET
BEFORE = diagnostic.identity.BEFORE
INTERMEDIATE = diagnostic.AFTER
IDENTITY_SCHEMA = "wetland471-identity-intermediate-v1"
PUBLISHER_SHA = "86c8bd068e1c4da5537ceb691d6a657177092e6c89dfe135c809d44acc9a926b"
REFERENCE_IMPLEMENTATION = "scripts/reference_assertion_coverage.py"
REFERENCE_IMPLEMENTATION_ARCHIVE = (
    "tests/fixtures/wetland_reference_assertion_coverage_af80bc09.py.txt"
)
REFERENCE_HISTORICAL_SHA = "363cffb652bdd18733cd5c8c2d22abf663cb3314410ef237e531a8b2f3298908"
REFERENCE_SUCCESSOR_SHA = "8f5121eb9954dcbcb205f8af3a7a2a167aa65817004a24cc698a4ccbe247798d"


def encoded(value):
    return (json.dumps(value, indent=2) + "\n").encode()


def raw_artifact(artifacts, review, item, *, identical=False):
    """Bind original raw hashes independently of any redacted public encoding."""
    mapping.bound(review, item["raw_path"], item["raw_sha256"])
    if identical:
        mapping.require(item["sha256"] == item["raw_sha256"], "exact raw bytes required")
    return artifacts.read(item)


def verify_public_references(artifacts, review, proof, intermediate):
    """Reuse the accepted semantic verifier after narrowly normalizing redaction.

    First retain and verify every raw digest against the immutable review and
    original receipt links. Only SHA/length fields for redacted JSON/log bytes
    are then derived on copies. These derived fields are never raw provenance.
    """
    command_proofs = proof["reference_commands"]
    mapping.require(
        set(command_proofs) == {"references", "reference-measurement"},
        "exact reference commands required",
    )
    commands = {}
    for name, items in command_proofs.items():
        mapping.require(set(items) == {"json", "log", "exit"}, "reference triplet required")
        receipt = json.loads(raw_artifact(artifacts, review, items["json"]))
        log = raw_artifact(artifacts, review, items["log"])
        exit_raw = raw_artifact(artifacts, review, items["exit"], identical=True)
        checks = [x for x in review["checks"] if x["check_id"] == "000471-" + name]
        evidence = {row["evidence_id"]: row for row in review["evidence"]}
        mapping.require(
            len(checks) == 1
            and shlex.split(checks[0]["command"]) == receipt["command"]
            and checks[0]["target_ids"] == [diagnostic.identity.TARGET_ID]
            and receipt["log_sha256"] == items["log"]["raw_sha256"]
            and exit_raw.strip() == b"0"
            and receipt["exit_code"] == 0
            and any(
                evidence[key]["reference"] == items["log"]["raw_path"]
                for key in checks[0]["evidence_ids"]
            ),
            "reference raw command links differ",
        )
        prefix = items["json"]["raw_path"].removesuffix(".json")
        mapping.require(
            items["json"]["raw_path"] == prefix + ".json"
            and items["log"]["raw_path"] == prefix + ".log"
            and items["exit"]["raw_path"] == prefix + ".exit",
            "reference triplet paths differ",
        )
        normalized = copy.deepcopy(receipt)
        normalized.update(log_sha256=mapping.digest(log), log_bytes=len(log))
        commands[name] = (normalized, log)

    items = proof["reference_measurement"]
    mapping.require(
        set(items) == {"started.json", "receipt.json", "measurement.json", "measurement.log"},
        "complete measured reference artifact set required",
    )
    raw = {name: raw_artifact(artifacts, review, item) for name, item in items.items()}
    started, receipt, result = (
        json.loads(raw[name]) for name in ("started.json", "receipt.json", "measurement.json")
    )
    directory = str(Path(items["receipt.json"]["raw_path"]).parent)
    mapping.require(
        all(item["raw_path"] == directory + "/" + name for name, item in items.items())
        and receipt["measurement_sha256"] == items["measurement.json"]["raw_sha256"]
        and receipt["log_sha256"] == items["measurement.log"]["raw_sha256"]
        and raw["receipt.json"] == commands["reference-measurement"][1],
        "measured reference raw publication links differ",
    )
    for assertion in result["records"][0]["assertions"]:
        cache = assertion["cache"]
        mapping.require(
            cache["loaded"] is True
            and cache["requested_path"] == diagnostic.identity.SOURCE
            and cache["sha256"] == diagnostic.identity.SOURCE_SHA
            and receipt["input_sha256"].get(diagnostic.identity.SOURCE)
            == diagnostic.identity.SOURCE_SHA,
            "actually loaded identity source differs",
        )
    normalized_receipt = copy.deepcopy(receipt)
    normalized_receipt["measurement_sha256"] = mapping.digest(encoded(result))
    normalized_log = encoded(normalized_receipt)
    outer = copy.deepcopy(commands["reference-measurement"][0])
    outer.update(log_sha256=mapping.digest(normalized_log), log_bytes=len(normalized_log))
    commands["reference-measurement"] = (outer, normalized_log)
    diagnostic.verify_references(
        intermediate, directory, started, normalized_receipt, result, commands
    )


def verify_identity(artifacts, proof, original, intermediate):
    """Reconstruct the original-to-identity leg and verify its actual native proof."""
    mapping.require(
        proof["schema_version"] == IDENTITY_SCHEMA
        and proof["target"] == TARGET
        and proof["target_id"] == diagnostic.identity.TARGET_ID
        and proof["before_sha256"] == mapping.digest(original) == BEFORE
        and proof["after_sha256"] == mapping.digest(intermediate) == INTERMEDIATE
        and proof["execution_revision"] == diagnostic.REVISION
        and proof["scientific_review"] is False
        and proof["verdict"] == "needs_curation",
        "fixed identity intermediate required",
    )
    review = yaml.safe_load(artifacts.read(proof["diagnostic_review"]))
    for module in (
        diagnostic,
        diagnostic.identity,
        diagnostic.measured,
        diagnostic.measured.native,
    ):
        name = str(Path(module.__file__).resolve().relative_to(ROOT))
        rows = [x for x in review["source"]["inputs"] if x["path"] == name]
        mapping.require(len(rows) == 1, "exact retained verifier implementation required")
        if name == REFERENCE_IMPLEMENTATION:
            # #2957: the saved review attests the actual af80bc09 implementation,
            # not the later supplement-aware tracer. Authenticate both without
            # replacing an original input hash. Historical proof verification
            # calls only raw_reference/snippet_surfaces, whose ASTs are unchanged;
            # dedicated controls bind that call boundary and both exact sources.
            mapping.require(
                rows[0]["sha256"] == REFERENCE_HISTORICAL_SHA,
                "exact historical tracer input required",
            )
            artifacts.read(
                {"path": REFERENCE_IMPLEMENTATION_ARCHIVE, "sha256": REFERENCE_HISTORICAL_SHA}
            )
            artifacts.read({"path": name, "sha256": REFERENCE_SUCCESSOR_SHA})
        else:
            artifacts.read({"path": name, "sha256": rows[0]["sha256"]})
    # The publisher was added after the saved review; bind its separately
    # reviewed implementation explicitly rather than inventing a review input.
    artifacts.read(
        {"path": str(Path(publisher.__file__).resolve().relative_to(ROOT)), "sha256": PUBLISHER_SHA}
    )
    mapping.validate_review(review)
    mapping.verify_population(review)
    publisher.verify_review(review)
    mapping.require(
        review["repository"] == "CultureBotAI/CommunityMech"
        and proof["review_inputs_verified"] == len(review["source"]["inputs"])
        and proof["required_checks"] == [row["check_id"] for row in review["checks"]]
        and mapping.render_markdown(review).encode() == artifacts.read(proof["review_markdown"]),
        "exact saved identity pair and declared checks required",
    )
    mapping.bound(review, TARGET, INTERMEDIATE)
    plan_item, apply_item, stage_item = (
        proof[key] for key in ("source_plan", "application_receipt", "staged_receipt")
    )
    mapping.bound(review, plan_item["path"], plan_item["sha256"])
    plan = json.loads(artifacts.read(plan_item))
    applied = json.loads(raw_artifact(artifacts, review, apply_item, identical=True))
    stage = json.loads(raw_artifact(artifacts, review, stage_item, identical=True))
    mapping.require(
        applied["source_plan"] == stage["source_plan"] == plan_item
        and applied["reviewed_receipt"]
        == {"path": stage_item["raw_path"], "sha256": stage_item["raw_sha256"]}
        and applied["helper_sha256"]
        == applied["inputs"].get("scripts/adhoc/curate_wetland_identity_20261115.py"),
        "actual identity plan/stage/writer links differ",
    )
    mapping.bound(review, str(Path(apply_item["raw_path"]).with_name("before.yaml")), BEFORE)
    for name, expected in applied["inputs"].items():
        mapping.bound(review, name, INTERMEDIATE if name == TARGET else expected)
    for name, expected in plan["inputs"].items():
        mapping.require(applied["inputs"].get(name) == expected, "identity source omitted")
    diagnostic.verify_chain(original, intermediate, applied, stage, plan)
    sidecar = proof["history_sidecar"]
    mapping.bound(review, sidecar["path"], sidecar["sha256"])
    history = yaml.safe_load(artifacts.read(sidecar))
    events = history.get("events", [])
    links = [
        pair
        for event in events
        for pair in re.findall(
            r"Actual apply receipt (\S+)\s+sha256:([0-9a-f]{64})(?:\.|\s|$)",
            event.get("details", ""),
        )
    ]
    mapping.require(
        history["target"] == {"kind": "record", "path": TARGET, "slug": Path(TARGET).stem}
        and len(events) == 1
        and events[0]["type"] == "EDIT"
        and events[0]["outcome"] == "changed"
        and events[0]["sections"] == diagnostic.gate_tool.SECTIONS.split(",")
        and links == [(apply_item["raw_path"], apply_item["raw_sha256"])],
        "exact native identity sidecar link differs",
    )
    mapping.require(set(proof["check_evidence"]) == set(mapping.RECIPES), "eight identity gates")
    for gate, item in proof["check_evidence"].items():
        mapping.verify_gate(artifacts, review, proof, gate, item)
    verify_public_references(artifacts, review, proof, intermediate)
    return review


def admit(root, path, predecessor_sha256, allowances, *, current=None):
    """Admit only the fixed original->identity->mapping chain; no default allowance."""
    root = Path(root).resolve()
    mapping.require(
        not Path(path).is_absolute()
        and ".." not in Path(path).parts
        and (root / path).resolve().is_relative_to(root),
        "safe canonical target required",
    )
    supplied = current is not None
    current = (root / path).read_bytes() if current is None else current
    actual = mapping.digest(current)
    if actual == predecessor_sha256:
        return mapping.Admission(actual, current, False)
    mapping.require(path == TARGET and path in allowances, "unknown identity-mapping successor")
    artifacts = mapping.Artifacts(root)
    if not supplied:
        artifacts.captured[(root / path).resolve()] = current
    entry = allowances[path]
    proof = json.loads(artifacts.read(entry["manifest"]))
    original = notes.historical_bytes(root, entry["baseline_revision"], path)
    intermediate = notes.historical_bytes(root, proof["intermediate_revision"], path)
    mapping.require(
        proof["target"] == path
        and proof["before_sha256"] == predecessor_sha256 == BEFORE == mapping.digest(original)
        and proof["intermediate_sha256"] == INTERMEDIATE == mapping.digest(intermediate)
        and proof["after_sha256"] == actual
        and proof["scientific_review"] is False
        and proof["mapping_allowance"]["baseline_revision"] == proof["intermediate_revision"],
        "exact original identity mapping chain required",
    )
    final_manifest = json.loads(artifacts.read(proof["mapping_allowance"]["manifest"]))
    final_review = yaml.safe_load(artifacts.read(final_manifest["diagnostic_review"]))
    identity = json.loads(artifacts.read(proof["identity_manifest"]))
    mapping.bound(
        final_review, proof["identity_manifest"]["path"], proof["identity_manifest"]["sha256"]
    )
    for key in (
        "diagnostic_review",
        "review_markdown",
        "source_plan",
        "history_sidecar",
        "application_receipt",
    ):
        mapping.bound(final_review, identity[key]["path"], identity[key]["sha256"])
    verify_identity(artifacts, identity, original, intermediate)
    result = mapping.admit(
        root, path, INTERMEDIATE, {path: proof["mapping_allowance"]}, current=current
    )
    mapping.require(
        result.changed and result.historical_bytes == intermediate, "mapping leg differs"
    )
    artifacts.verify()
    return mapping.Admission(actual, original, True)
