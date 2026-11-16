"""Stage/apply exactly three Switchgrass source locators; #1996, 2026-11-15.

Inputs: externally pinned plan, five completed consumer controls, retained source
bytes and exact revision. Outputs: exclusive private candidates/receipts/backups.
Apply alone replaces the fixed canonical record; separate native sidecar follows.
Reuses the maintained validated writer and native curation-event contract, with
text-preserving staging like curate_gtdb_source_notes_20261115.py. No acquisition,
configuration change, scientific promotion or source-text publication.
"""

from __future__ import annotations

import argparse
import difflib
import inspect
import json
import re
import subprocess
from collections import Counter
from copy import deepcopy
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path

import yaml

from communitymech.curate.curation_event import record_curation_event
from communitymech.validation.write_validated import write_validated_community

ROOT = Path(__file__).resolve().parents[2]
TARGET = "kb/communities/LBNL_Switchgrass_Soil_SynCom16.yaml"
BEFORE = "bb31b1df4a9be2241453528101fc5d55657c23eccf1d58ce1cc9639e5912b368"
SCOPE = "switchgrass-three-source-locators-only-v1"
DISCUSSION = "methods_final16_vs_supplement_table_s1"
ASSET = "msystems.00951-22-s0006.docx"
ASSET_SHA = "5bfa02fdb94538e9405fb0ec7d7b0dad338791a5ca0b4b651589f33148c8e0e7"
VALIDATOR = "6b71e7f4b353b5b36000fda03da78b61734e3fc8"
PREPARER = "scripts/adhoc/prepare_switchgrass_consumer_canary_20261115.py"
RUNNER = "scripts/adhoc/run_switchgrass_consumer_canary_20261115.py"
HELPER_PINS = {
    PREPARER: "888d5f3ad40c0d7250e86b0488000835cc25f003fc02d3b0f03114c8ad94e06b",
    RUNNER: "289d3d95c482a4165eaefd15211d0e4c3f103f2e622749953aed82a8048de118",
}
REQUIRED = (
    TARGET,
    PREPARER,
    RUNNER,
    "src/communitymech/curate/curation_event.py",
    "src/communitymech/validation/write_validated.py",
    "src/communitymech/schema/communitymech.yaml",
    "src/communitymech/schema/mech_shared.yaml",
    "src/communitymech/schema/history.yaml",
    "pyproject.toml",
    "uv.lock",
)
CELLS = {2: (12, 2, "OAE516"), 3: (18, 1, "Bacillus"), 4: (18, 2, "OAE603")}
COUNTS = {
    "selected": (37, 37, 37, 0, 0),
    "article-only": (37, 37, 35, 2, 0),
    "wrong-cell": (37, 37, 36, 1, 0),
    "wrong-parent": (37, 36, 36, 0, 1),
    "restored": (37, 37, 37, 0, 0),
}
COUNT_KEYS = (
    "native_validation_calls",
    "native_comparisons",
    "native_matches",
    "native_mismatches",
    "source_selection_failures",
)


class Captured(dict):
    """Captured bytes plus complete runtime member sets for final drift checks."""

    def __init__(self):
        super().__init__()
        self.memberships = {}
        self.revisions = {}


def sha(raw):
    return sha256(raw).hexdigest()


def encoded(value):
    return (json.dumps(value, indent=2, sort_keys=True) + "\n").encode()


def head():
    return subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip()


def local(name, *, private=False):
    relative = Path(name)
    result = ROOT / relative
    if (
        relative.is_absolute()
        or ".." in relative.parts
        or not result.resolve().is_relative_to(ROOT.resolve())
        or (private and relative.parts[:1] != (".temp",))
    ):
        raise ValueError("safe repository-relative private path required")
    if any(p.is_symlink() for p in (result, *result.parents)):
        raise ValueError("symlink path refused")
    return result


def capture(captured, location, expected=None):
    location = Path(location).absolute()
    if any(p.is_symlink() for p in (location, *location.parents)) or not location.is_file():
        raise ValueError("regular captured input required")
    if location not in captured:
        captured[location] = location.read_bytes()
    raw = captured[location]
    if expected is not None and (
        not re.fullmatch(r"[0-9a-f]{64}", expected) or sha(raw) != expected
    ):
        raise ValueError("pinned input differs: " + str(location))
    return raw


def unchanged(captured, revision, replacement=None):
    replacement = replacement or {}
    if head() != revision or any(
        any(part.is_symlink() for part in (p, *p.parents))
        or p.read_bytes() != replacement.get(p, raw)
        for p, raw in captured.items()
    ):
        raise ValueError("captured input or revision changed")
    for package, expected in captured.memberships.items():
        if {p.relative_to(package) for p in package.rglob("*.py")} != expected:
            raise ValueError("captured runtime membership changed")
    for root, expected in captured.revisions.items():
        if (
            subprocess.check_output(
                ["git", "-C", str(root), "rev-parse", "HEAD"], text=True
            ).strip()
            != expected
        ):
            raise ValueError("captured runtime revision changed")


def runtime_inputs(report, captured, extractor):
    """Verify complete source/installed membership rather than a declared count."""
    sources = [
        Path(name).parent
        for name in report["inputs"]
        if name.endswith("/src/linkml_reference_validator/__init__.py")
    ]
    if len(sources) != 1:
        raise ValueError("one exact reviewed runtime source package required")
    source = sources[0]
    installed = Path(report["installed_package"])
    source_root = source.parent.parent
    if installed == source or installed.name != "linkml_reference_validator":
        raise ValueError("separate installed runtime package required")
    actual_head = subprocess.check_output(
        ["git", "-C", str(source_root), "rev-parse", "HEAD"], text=True
    ).strip()
    if actual_head != VALIDATOR:
        raise ValueError("reviewed runtime revision differs")
    captured.revisions[source_root] = VALIDATOR
    relative = {p.relative_to(source) for p in source.rglob("*.py")}
    if (
        len(relative) != 49
        or {p.relative_to(installed) for p in installed.rglob("*.py")} != relative
    ):
        raise ValueError("complete runtime Python membership differs")
    for package in (source, installed):
        if package in captured.memberships and captured.memberships[package] != relative:
            raise ValueError("runtime membership changed between controls")
        captured.memberships.setdefault(package, relative)
    for name in relative:
        for package in (source, installed):
            member = package / name
            if str(member) not in report["inputs"]:
                raise ValueError("control omits a runtime Python member")
            capture(captured, member, report["inputs"][str(member)])
        if captured[source / name] != captured[installed / name]:
            raise ValueError("installed runtime bytes differ from reviewed source")
    active_extractor = Path(inspect.getfile(extractor)).absolute()
    if capture(captured, active_extractor) != captured[source / "etl/source_locator.py"]:
        raise ValueError("active projection extractor differs from reviewed runtime")
    return {str(package / name) for package in (source, installed) for name in relative}


def surfaces(value, path=""):
    if isinstance(value, dict):
        for key, child in value.items():
            nested = f"{path}.{key}" if path else key
            if key == "snippet" and isinstance(child, str):
                yield nested, child, value.get("reference")
            yield from surfaces(child, nested)
    elif isinstance(value, list):
        for index, child in enumerate(value):
            yield from surfaces(child, f"{path}[{index}]")


def selection(original):
    before = yaml.safe_load(original)
    if sha(original) != BEFORE or before.get("id") != "CommunityMech:000087":
        raise ValueError("exact Switchgrass original required")
    indexes = [
        i for i, item in enumerate(before["discussions"]) if item["discussion_id"] == DISCUSSION
    ]
    if len(indexes) != 1 or len(list(surfaces(before))) != 37:
        raise ValueError("exact discussion and 37 snippet surfaces required")
    index = indexes[0]
    selected = deepcopy(before)
    paths = []
    for entry, (row, cell, text) in CELLS.items():
        evidence = selected["discussions"][index]["evidence"][entry]
        if (
            evidence.get("reference") != "PMID:36472419"
            or evidence.get("snippet") != text
            or evidence.get("evidence_source") != "supplement_table_S1"
            or "source_locator" in evidence
        ):
            raise ValueError("exact untouched source evidence required")
        evidence["source_locator"] = {
            "kind": "supplement",
            "asset_id": ASSET,
            "version": "published",
            "table": 1,
            "row": row,
            "cell": cell,
        }
        paths.append(f"discussions[{index}].evidence[{entry}].snippet")
    return before, selected, index, paths


def control_record(original, mode):
    before, selected, index, paths = selection(original)
    record = deepcopy(before if mode == "article-only" else selected)
    evidence = record["discussions"][index]["evidence"]
    if mode == "wrong-parent":
        evidence[2]["reference"] = "PMID:12345"
    elif mode == "wrong-cell":
        evidence[3]["source_locator"].update(row=12, cell=1)
    return record, index, paths


def verify_control(report, mode, record, paths, catalog_raw, projection):
    expected_mode = "selected" if mode == "restored" else mode
    if (
        report.get("mode") != expected_mode
        or report.get("control_passed") is not True
        or any(report.get(key) != [] for key in ("errors", "changed_inputs", "network_attempts"))
        or report.get("validator_revision") != VALIDATOR
        or report.get("runtime_python_members") != 49
        or report.get("independent_snippet_surfaces") != 37
    ):
        raise ValueError("successful actual consumer control required")
    events = report["comparisons"]
    expected = {path: (text, reference) for path, text, reference in surfaces(record)}
    if len(expected) != 37 or Counter(e["path"] for e in events) != Counter(expected.keys()):
        raise ValueError("actual control path census differs")
    wanted = {
        "selected": set(),
        "restored": set(),
        "article-only": {paths[0], paths[2]},
        "wrong-cell": {paths[1]},
        "wrong-parent": {paths[0]},
    }[mode]
    if (
        report.get("native_exit_code") != bool(wanted)
        or type(report.get("native_exit_code")) is not int
        or report.get("native_failures") != len(wanted)
        or {e["path"] for e in events if not e["is_valid"]} != wanted
    ):
        raise ValueError("precise native control failure set differs")
    counts = (
        len(events),
        sum(e["matched"] is not None for e in events),
        sum(e["matched"] is True for e in events),
        sum(e["matched"] is False for e in events),
        sum(
            e["matched"] is None
            and not e["is_valid"]
            and e["message"].startswith("Source selection failed:")
            for e in events
        ),
    )
    if (
        counts != COUNTS[mode]
        or tuple(report.get(key) for key in COUNT_KEYS) != counts
        or any(type(report.get(key)) is not int for key in COUNT_KEYS)
    ):
        raise ValueError("actual comparison denominator differs")
    source = json.loads(catalog_raw)["sources"][0]
    identities = 0
    # Locate the fixed discussion without trusting receipt-supplied coordinates.
    evidence = next(d for d in record["discussions"] if d["discussion_id"] == DISCUSSION)[
        "evidence"
    ]
    for event in events:
        text, reference = expected[event["path"]]
        if event["reference"] != reference or event["text_sha256"] != sha(text.encode()):
            raise ValueError("actual dispatched quotation/reference differs")
        expected_match = event["path"] not in wanted
        if mode == "wrong-parent" and event["path"] == paths[0]:
            expected_match = None
        if event["matched"] is not expected_match or event["is_valid"] is not (
            event["path"] not in wanted
        ):
            raise ValueError("exact per-path native comparison outcome differs")
        needs_identity = event["path"] in paths and mode != "article-only"
        needs_identity &= not (mode == "wrong-parent" and event["path"] == paths[0])
        if event["matched"] is None and (
            mode != "wrong-parent"
            or event["path"] != paths[0]
            or event["is_valid"]
            or event["severity"] != "ERROR"
        ):
            raise ValueError("unexpected soft skip or source failure")
        if not needs_identity:
            if event.get("source_identity") is not None:
                raise ValueError("unexpected source identity")
            continue
        entry = tuple(CELLS)[paths.index(event["path"])]
        locator = evidence[entry]["source_locator"]
        cell = projection["tables"][locator["table"] - 1][locator["row"] - 1][locator["cell"] - 1]
        if cell.get("status") != "supported":
            raise ValueError("selected control cell unsupported")
        identity = {
            "reference": source["reference"],
            "asset_id": source["asset_id"],
            "version": source["version"],
            "asset_sha256": source["asset_sha256"],
            "extraction_sha256": source["extraction_sha256"],
            "catalog_sha256": sha(catalog_raw),
            "extractor": projection["format"],
            "locator": locator,
            "selected_sha256": sha(cell["text"].encode()),
        }
        if event.get("source_identity") != identity:
            raise ValueError("exact native selected identity differs")
        identities += 1
    if report.get("established_source_identities") != identities:
        raise ValueError("source identity denominator differs")


def prepare(plan_name, plan_sha, revision):
    if not re.fullmatch(r"[0-9a-f]{40}", revision) or head() != revision:
        raise ValueError("exact current revision required")
    captured = Captured()
    plan = json.loads(capture(captured, local(plan_name), plan_sha))
    if (
        set(plan) != {"scope", "target", "before_sha256", "preparation", "controls", "inputs"}
        or plan["scope"] != SCOPE
        or plan["target"] != TARGET
        or plan["before_sha256"] != BEFORE
        or set(plan["controls"]) != set(COUNTS)
        or not set(REQUIRED).issubset(plan["inputs"])
    ):
        raise ValueError("closed fixed-target plan and all five controls required")
    for name, expected in plan["inputs"].items():
        capture(captured, local(name), expected)
    for name, expected in HELPER_PINS.items():
        capture(captured, local(name), expected)
    capture(captured, Path(__file__))
    original = capture(captured, local(TARGET), BEFORE)
    _, selected, _, paths = selection(original)
    prep_item = plan["preparation"]
    prep_path = local(prep_item["path"], private=True)
    prep = json.loads(capture(captured, prep_path, prep_item["sha256"]))
    if (
        prep.get("plan") is not False
        or prep.get("schema_bytes_unchanged") is not True
        or prep.get("record_content_unchanged_except_three_locators") is not True
        or prep.get("selected_paths") != paths
        or prep.get("asset_sha256") != ASSET_SHA
        or prep["inputs"].get(str(local(PREPARER))) != HELPER_PINS[PREPARER]
    ):
        raise ValueError("actual accepted consumer preparation required")
    for name, expected in prep["inputs"].items():
        capture(captured, Path(name), expected)
    for name, expected in prep["outputs"].items():
        capture(
            captured,
            local(str((prep_path.parent / name).relative_to(ROOT)), private=True),
            expected,
        )
    directory = prep_path.parent
    if (
        capture(captured, directory / "original.yaml") != original
        or json.loads(capture(captured, directory / "selected.json")) != selected
    ):
        raise ValueError("prepared records differ from fixed selection")
    catalog_raw = capture(captured, directory / "catalog.json")
    catalog = json.loads(catalog_raw)
    projection_raw = capture(captured, directory / "extractions/table-s1.json")
    asset = capture(captured, directory / "assets" / ASSET, ASSET_SHA)
    if catalog != {
        "version": 1,
        "sources": [
            {
                "reference": "PMID:36472419",
                "asset_id": ASSET,
                "version": "published",
                "asset_path": f"assets/{ASSET}",
                "asset_sha256": ASSET_SHA,
                "extraction_path": "extractions/table-s1.json",
                "extraction_sha256": sha(projection_raw),
            }
        ],
    }:
        raise ValueError("fixed source catalog identity differs")
    from linkml_reference_validator.etl.source_locator import extract_docx_tables

    projection = json.loads(projection_raw)
    if extract_docx_tables(asset) != projection:
        raise ValueError("source projection replay differs")
    controls = []
    common_environment = None
    for mode, item in plan["controls"].items():
        receipt_path = local(item["path"], private=True)
        controls.append(receipt_path)
        report = json.loads(capture(captured, receipt_path, item["sha256"]))
        for name, expected in report["inputs"].items():
            capture(captured, Path(name), expected)
        runtime_names = runtime_inputs(report, captured, extract_docx_tables)
        record_path = receipt_path.parent / "record.json"
        expected_record, _, _ = control_record(original, mode)
        record_raw = capture(captured, record_path)
        if (
            report["inputs"].get(str(record_path)) != sha(record_raw)
            or report["inputs"].get(str(prep_path)) != prep_item["sha256"]
            or report["inputs"].get(str(local(RUNNER))) != HELPER_PINS[RUNNER]
            or json.loads(record_raw) != expected_record
        ):
            raise ValueError("control record/preparation/runner binding differs")
        for name, expected in prep["inputs"].items():
            if report["inputs"].get(name) != expected:
                raise ValueError("control omits prepared source input")
        for name, expected in prep["outputs"].items():
            if report["inputs"].get(str(directory / name)) != expected:
                raise ValueError("control omits prepared artifact")
        expected_names = (
            set(prep["inputs"])
            | {str(directory / n) for n in prep["outputs"]}
            | {str(prep_path), str(local(RUNNER)), str(record_path)}
            | runtime_names
        )
        if set(report["inputs"]) != expected_names:
            raise ValueError("exact complete consumer input coverage differs")
        if report["native_argv"] != [
            "data",
            str(record_path),
            "--schema",
            str(directory / "schema/communitymech.yaml"),
            "--target-class",
            "MicrobialCommunity",
            "--config",
            str(directory / "config.json"),
            "--no-full-text",
        ]:
            raise ValueError("native consumer command differs")
        capture(captured, receipt_path.parent / "native.log", report["log_sha256"])
        if (
            capture(captured, receipt_path.parent / "native.exit")
            != f"{report['native_exit_code']}\n".encode()
        ):
            raise ValueError("native exit artifact differs")
        environment = {
            key: report[key] for key in ("executable", "installed_package", "dependencies")
        }
        if common_environment is not None and environment != common_environment:
            raise ValueError("consumer environments differ across controls")
        common_environment = environment
        verify_control(report, mode, expected_record, paths, catalog_raw, projection)
    if len(set(controls)) != 5:
        raise ValueError("five distinct actual control receipts required")
    unchanged(captured, revision)
    return plan, original, captured


def child(node, key):
    matches = [(k, v) for k, v in node.value if k.value == key]
    if len(matches) != 1:
        raise ValueError("one unambiguous YAML key required")
    return matches[0]


def line_boundary(text, index):
    start = text.rfind("\n", 0, index) + 1
    if text[start:index].strip():
        raise ValueError("unsupported YAML insertion boundary")
    return start


def render_candidate(original, plan, timestamp):
    _, expected, index, _ = selection(original)
    if not re.fullmatch(r"\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ", timestamp):
        raise ValueError("native timestamp required")
    event = record_curation_event(
        expected,
        curator="Codex",
        action="ADD_SUPPLEMENT_SOURCE_LOCATORS",
        llm_assisted=True,
        timestamp=timestamp,
        changes=(
            "Added three explicit Table S1 cell locators for unchanged OAE516, Bacillus and OAE603 "
            "snippets under PMID:36472419. Actual consumer selected/restored controls matched all "
            "37 unchanged quotations; wrong-cell and wrong-parent controls refused their exact targets. "
            "Only lexical source routing changed; stock identities, final16/earlier panel disagreement, "
            "all biological content and prior history remain unchanged. The documented scientific "
            "panel-correspondence issue1548 is not resolved by this lexical correction. "
            "Bound selected receipt SHA256=" + plan["controls"]["selected"]["sha256"] + "."
        ),
    )
    text = original.decode()
    root = yaml.compose(text)
    discussion = child(root, "discussions")[1].value[index]
    evidence = child(discussion, "evidence")[1]
    inserts = []
    for entry in CELLS:
        node = evidence.value[entry]
        indent = child(node, "snippet")[0].start_mark.column
        block = yaml.safe_dump(
            {"source_locator": expected["discussions"][index]["evidence"][entry]["source_locator"]},
            sort_keys=False,
        )
        inserts.append(
            (
                line_boundary(text, node.end_mark.index),
                "".join(" " * indent + line + "\n" for line in block.splitlines()),
            )
        )
    history = child(root, "curation_history")[1]
    if not history.value or history.start_mark.column != 0:
        raise ValueError("existing native history sequence required")
    inserts.append(
        (
            line_boundary(text, history.end_mark.index),
            yaml.safe_dump([event], sort_keys=False, allow_unicode=True, width=110),
        )
    )
    for position, addition in sorted(inserts, reverse=True):
        text = text[:position] + addition + text[position:]
    if yaml.safe_load(text) != expected:
        raise ValueError("candidate changes undeclared content")
    return text.encode(), expected, event


def verify_candidate(original, candidate, plan):
    before, after = yaml.safe_load(original), yaml.safe_load(candidate)
    added = after.get("curation_history", [])[len(before["curation_history"]) :]
    if len(added) != 1:
        raise ValueError("exactly one native event required")
    rendered, expected, event = render_candidate(original, plan, added[0].get("timestamp", ""))
    if candidate != rendered or after != expected or added != [event]:
        raise ValueError("candidate bytes or native event differ")
    return expected, event


def publish(path, raw):
    with path.open("xb") as handle:
        handle.write(raw)
    if path.read_bytes() != raw:
        raise ValueError("persisted artifact differs")


def stage(plan_name, plan_sha, output_name, revision, *, plan_only=False):
    output = local(output_name, private=True)
    if output.exists():
        raise ValueError("exclusive private stage required")
    plan, original, captured = prepare(plan_name, plan_sha, revision)
    candidate, expected, event = render_candidate(
        original, plan, datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    )
    metadata = {
        "scope": SCOPE,
        "target": TARGET,
        "before_sha256": BEFORE,
        "execution_revision": revision,
        "source_plan": {"path": plan_name, "sha256": plan_sha},
        "inputs": {str(p): sha(raw) for p, raw in captured.items()},
        "scientific_review": False,
    }
    if plan_only:
        unchanged(captured, revision)
        return {**metadata, "plan": True}
    output.mkdir(parents=True)
    write_validated_community(expected, output / "validated.yaml")
    if yaml.safe_load((output / "validated.yaml").read_bytes()) != expected:
        raise ValueError("native serialization differs")
    unchanged(captured, revision)
    diff = "".join(
        difflib.unified_diff(
            original.decode().splitlines(True),
            candidate.decode().splitlines(True),
            fromfile=TARGET,
            tofile="staged/" + Path(TARGET).name,
        )
    )
    publish(output / Path(TARGET).name, candidate)
    publish(output / "candidate.diff", diff.encode())
    result = {
        **metadata,
        "canonical_apply": False,
        "source_inputs_unchanged": True,
        "candidate_sha256": sha(candidate),
        "candidate_diff_sha256": sha(diff.encode()),
        "native_serialization_sha256": sha((output / "validated.yaml").read_bytes()),
        "appended_native_inline_history": event,
    }
    unchanged(captured, revision)
    publish(output / "receipt.json", encoded(result))
    return result


def admitted_stage(stage_name, candidate_sha, receipt_sha, revision):
    directory = local(stage_name, private=True)
    captured = Captured()
    receipt = json.loads(capture(captured, directory / "receipt.json", receipt_sha))
    if (
        receipt.get("scope") != SCOPE
        or receipt.get("canonical_apply") is not False
        or receipt.get("source_inputs_unchanged") is not True
        or receipt.get("execution_revision") != revision
        or receipt.get("target") != TARGET
        or receipt.get("before_sha256") != BEFORE
        or receipt.get("candidate_sha256") != candidate_sha
    ):
        raise ValueError("exact completed same-revision locator stage required")
    source = receipt["source_plan"]
    plan, original, inputs = prepare(source["path"], source["sha256"], revision)
    if receipt["inputs"] != {str(p): sha(raw) for p, raw in inputs.items()}:
        raise ValueError("stage captured-input coverage differs")
    for p, raw in inputs.items():
        if p in captured and captured[p] != raw:
            raise ValueError("captured overlap differs")
        captured.setdefault(p, raw)
    captured.memberships.update(inputs.memberships)
    captured.revisions.update(inputs.revisions)
    candidate = capture(captured, directory / Path(TARGET).name, candidate_sha)
    expected, event = verify_candidate(original, candidate, plan)
    if event != receipt["appended_native_inline_history"]:
        raise ValueError("reviewed native event differs")
    capture(captured, directory / "candidate.diff", receipt["candidate_diff_sha256"])
    validated = capture(
        captured, directory / "validated.yaml", receipt["native_serialization_sha256"]
    )
    if yaml.safe_load(validated) != expected:
        raise ValueError("staged native serialization differs")
    unchanged(captured, revision)
    return receipt, original, candidate, expected, captured


def apply(stage_name, candidate_sha, receipt_sha, output_name, revision, *, plan_only=False):
    output = local(output_name, private=True)
    if output.exists():
        raise ValueError("exclusive private application output required")
    receipt, original, candidate, expected, captured = admitted_stage(
        stage_name, candidate_sha, receipt_sha, revision
    )
    if plan_only:
        return {"plan": True, "target": TARGET, "candidate_sha256": candidate_sha}
    output.mkdir(parents=True)
    publish(output / "before.yaml", original)
    write_validated_community(expected, output / "validated.yaml")
    if yaml.safe_load((output / "validated.yaml").read_bytes()) != expected:
        raise ValueError("native serialization differs")
    publish(output / "replacement.yaml", candidate)
    unchanged(captured, revision)
    target = local(TARGET)
    (output / "replacement.yaml").replace(target)
    unchanged(captured, revision, {target: candidate})
    result = {
        "applied": True,
        "scope": SCOPE,
        "target": TARGET,
        "before_sha256": BEFORE,
        "after_sha256": candidate_sha,
        "execution_revision": revision,
        "reviewed_receipt": {"path": str(Path(stage_name) / "receipt.json"), "sha256": receipt_sha},
        "inputs": receipt["inputs"],
        "appended_native_inline_history": receipt["appended_native_inline_history"],
        "scientific_review": False,
        "sidecar_status": "PENDING separate native just new-history",
    }
    publish(output / "receipt.json", encoded(result))
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    staging = commands.add_parser("stage")
    staging.add_argument("--source-plan", required=True)
    staging.add_argument("--source-sha256", required=True)
    application = commands.add_parser("apply")
    application.add_argument("--stage", required=True)
    application.add_argument("--candidate-sha256", required=True)
    application.add_argument("--receipt-sha256", required=True)
    for command in (staging, application):
        command.add_argument("--output", required=True)
        command.add_argument("--expected-revision", required=True)
        command.add_argument("--plan", action="store_true")
    args = parser.parse_args()
    if args.command == "stage":
        result = stage(
            args.source_plan,
            args.source_sha256,
            args.output,
            args.expected_revision,
            plan_only=args.plan,
        )
    else:
        result = apply(
            args.stage,
            args.candidate_sha256,
            args.receipt_sha256,
            args.output,
            args.expected_revision,
            plan_only=args.plan,
        )
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
