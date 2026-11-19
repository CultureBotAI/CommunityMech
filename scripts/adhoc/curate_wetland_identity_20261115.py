"""Stage/apply the fixed Wetland471 identity correction; #2898, 2026-11-15.

Inputs: reviewed source plan, exact record/source/code hashes and Git revision.
Outputs: exclusive private candidate/receipts; apply persists only the accepted
candidate through native validation. No acquisition, mapping or graph edits.
The executed taxonomy-note helper stays unchanged; its capture primitives are reused.
"""

from __future__ import annotations

import argparse
import copy
import difflib
import importlib.util
import json
import re
import textwrap
from datetime import datetime, timezone
from pathlib import Path

import yaml

from communitymech.curate.curation_event import record_curation_event
from communitymech.validation.write_validated import write_validated_community

ROOT = Path(__file__).resolve().parents[2]
BASE_HELPER = "scripts/adhoc/curate_gtdb_source_notes_20261115.py"
_spec = importlib.util.spec_from_file_location("wetland_capture", ROOT / BASE_HELPER)
assert _spec and _spec.loader
capture_core = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(capture_core)
sha = capture_core.sha
TARGET = "kb/communities/Wetland_Lindane_Degrading_Organochlorine_Consortium.yaml"
TARGET_ID = "CommunityMech:000471"
BEFORE = "2191214bbc8d7f8bb6341c6493344e2180eb63fe2098375f44aab9f49d35d199"
SOURCE = "references_cache/PMID_42663479.txt"
SOURCE_SHA = "489eb292cd49275ee0d480727b215360c2101e577aae884a4f52ff68fb7990eb"
SCOPE = "wetland471-source-identity-only"
FIELDS = {
    ("description",),
    ("taxonomy", 0, "taxon_term", "notes"),
    ("taxonomy", 0, "evidence", 0, "explanation"),
    ("taxonomy", 4, "taxon_term", "notes"),
}
DISCUSSION_ID = "wetland-m-y13-stock-and-roster-boundaries"


def path(name, *, private=False):
    return capture_core.path(name, private=private)


def get(document, selector):
    for key in selector:
        document = document[key]
    return document


def expected_document(original, plan, timestamp):
    before = yaml.safe_load(original)
    if before["id"] != TARGET_ID or sha(original) != BEFORE:
        raise ValueError("exact Wetland471 baseline required")
    changes = plan["changes"]
    if len(changes) != len(FIELDS) or {tuple(c["path"]) for c in changes} != FIELDS:
        raise ValueError("exact four identity fields required")
    expected = copy.deepcopy(before)
    for change in changes:
        selector = change["path"]
        after = change["after"]
        if (
            get(before, selector) != change["before"]
            or not isinstance(after, str)
            or not after.strip()
            or "\n" in after
            or after == change["before"]
        ):
            raise ValueError("exact existing scalar and substantive replacement required")
        get(expected, selector[:-1])[selector[-1]] = after
    discussion = plan["discussion"]
    if (
        before.get("discussions")
        or discussion.get("discussion_id") != DISCUSSION_ID
        or discussion.get("kind") != "CURATION_TODO"
        or discussion.get("status") != "OPEN"
        or not discussion.get("evidence")
    ):
        raise ValueError("one new open source-scope discussion required")
    expected["discussions"] = [copy.deepcopy(discussion)]
    if not re.fullmatch(r"\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ", timestamp):
        raise ValueError("explicit native timestamp required")
    event = record_curation_event(
        expected,
        curator="Codex",
        action="CORRECT_SOURCE_IDENTITY",
        changes=plan["event_changes"],
        llm_assisted=True,
        timestamp=timestamp,
    )
    return expected, event


def render_candidate(original, plan, timestamp):
    expected, event = expected_document(original, plan, timestamp)
    text = original.decode()
    root = yaml.compose(text)
    replacements = []
    for change in plan["changes"]:
        node = root
        for key in change["path"][:-1]:
            node = node.value[key] if isinstance(key, int) else capture_core.child(node, key)[1]
        key, value = capture_core.child(node, change["path"][-1])
        start = text.rfind("\n", 0, key.start_mark.index) + 1
        end = value.end_mark.index
        if end < len(text) and text[end] == "\n":
            end += 1
        indent = " " * key.start_mark.column
        replacement = indent + key.value + ": >-\n"
        replacement += (
            textwrap.fill(
                change["after"],
                width=110,
                initial_indent=indent + "  ",
                subsequent_indent=indent + "  ",
                break_long_words=False,
                break_on_hyphens=False,
            )
            + "\n"
        )
        replacements.append((start, end, replacement))
    history_key, history = capture_core.child(root, "curation_history")
    if (
        not history.value
        or text[history.end_mark.index :].strip()
        or history.start_mark.column != 0
    ):
        raise ValueError("existing final native block history required")
    insertion = text.rfind("\n", 0, history_key.start_mark.index) + 1
    replacements.append(
        (
            insertion,
            insertion,
            yaml.safe_dump(
                {"discussions": expected["discussions"]},
                sort_keys=False,
                allow_unicode=True,
                width=110,
            ),
        )
    )
    replacements.append(
        (
            history.end_mark.index,
            history.end_mark.index,
            yaml.safe_dump(
                [event],
                sort_keys=False,
                allow_unicode=True,
                width=110,
            ),
        )
    )
    for start, end, replacement in sorted(replacements, reverse=True):
        text = text[:start] + replacement + text[end:]
    if yaml.safe_load(text) != expected:
        raise ValueError("render changed undeclared content")
    return text.encode(), expected, event


def prepare(plan_name, plan_sha, revision):
    if capture_core.head() != revision or not re.fullmatch(r"[0-9a-f]{40}", revision):
        raise ValueError("exact current revision required")
    captured = {}
    plan = json.loads(capture_core.capture(captured, plan_name, plan_sha))
    if (
        plan.get("scope") != SCOPE
        or plan.get("scientific_review") is not False
        or plan.get("target") != TARGET
        or plan.get("target_id") != TARGET_ID
        or plan.get("before_sha256") != BEFORE
    ):
        raise ValueError("fixed source-identity scope required")
    if plan["inputs"].get(TARGET) != BEFORE or plan["inputs"].get(SOURCE) != SOURCE_SHA:
        raise ValueError("fixed record and primary source pins required")
    for name, digest in plan["inputs"].items():
        capture_core.capture(captured, name, digest)
    source = capture_core.capture(captured, SOURCE, SOURCE_SHA).decode()
    anchors = plan["source_anchors"]
    if not anchors or any(not a or a not in source for a in anchors):
        raise ValueError("every exact source anchor required")
    for change in plan["changes"]:
        indexes = change["source_anchor_indices"]
        if not indexes or any(type(i) is not int or not 0 <= i < len(anchors) for i in indexes):
            raise ValueError("each changed assertion requires captured source anchors")
    for evidence in plan["discussion"]["evidence"]:
        if (
            evidence.get("reference") != "PMID:42663479"
            or evidence.get("snippet") not in anchors
            or evidence.get("evidence_source") != "full_text"
        ):
            raise ValueError("discussion evidence must use captured primary anchors")
    for name in (*capture_core.REQUIRED, BASE_HELPER, str(Path(__file__).relative_to(ROOT))):
        capture_core.capture(captured, name)
    return plan, captured[path(TARGET)], captured


def stage(plan_name, plan_sha, output_name, revision, *, plan_only=False):
    output = path(output_name, private=True)
    if output.exists():
        raise ValueError("exclusive private output required")
    plan, original, captured = prepare(plan_name, plan_sha, revision)
    candidate, expected, event = render_candidate(
        original, plan, datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    )
    result = {
        "scope": SCOPE,
        "scientific_review": False,
        "target": TARGET,
        "target_id": TARGET_ID,
        "execution_revision": revision,
        "source_plan": {"path": plan_name, "sha256": plan_sha},
        "before_sha256": sha(original),
        "candidate_sha256": sha(candidate),
        "inputs": {str(p.relative_to(ROOT)): sha(raw) for p, raw in captured.items()},
        "appended_native_inline_history": event,
        "canonical_apply": False,
    }
    capture_core.unchanged(captured, revision)
    if plan_only:
        return {**result, "planned": True}
    output.mkdir(parents=True)
    write_validated_community(expected, output / "validated.yaml")
    if yaml.safe_load((output / "validated.yaml").read_bytes()) != expected:
        raise ValueError("native serialization differs")
    capture_core.unchanged(captured, revision)
    (output / Path(TARGET).name).write_bytes(candidate)
    diff = "".join(
        difflib.unified_diff(
            original.decode().splitlines(keepends=True),
            candidate.decode().splitlines(keepends=True),
            fromfile=TARGET,
            tofile="staged/" + Path(TARGET).name,
        )
    )
    (output / "candidate.diff").write_text(diff)
    result.update(
        source_inputs_unchanged=True,
        candidate_diff_sha256=sha(diff.encode()),
        completed_at=datetime.now(timezone.utc).isoformat(),
    )
    (output / "receipt.json").write_text(json.dumps(result, indent=2) + "\n")
    return result


def apply(stage_name, candidate_sha, receipt_sha, output_name, revision, *, plan_only=False):
    output, staged = path(output_name, private=True), path(stage_name, private=True)
    if output.exists():
        raise ValueError("exclusive private output required")
    captured = {}
    receipt_name = str((staged / "receipt.json").relative_to(ROOT))
    receipt = json.loads(capture_core.capture(captured, receipt_name, receipt_sha))
    if (
        receipt.get("scope") != SCOPE
        or receipt.get("canonical_apply") is not False
        or receipt.get("source_inputs_unchanged") is not True
        or receipt.get("execution_revision") != revision
        or receipt.get("candidate_sha256") != candidate_sha
    ):
        raise ValueError("exact completed same-revision stage required")
    item = receipt["source_plan"]
    plan, original, inputs = prepare(item["path"], item["sha256"], revision)
    expected_inputs = {str(p.relative_to(ROOT)): sha(raw) for p, raw in inputs.items()}
    if (
        receipt["inputs"] != expected_inputs
        or receipt["target"] != TARGET
        or receipt["target_id"] != TARGET_ID
        or receipt["before_sha256"] != BEFORE
    ):
        raise ValueError("stage input coverage or baseline differs")
    for location, raw in inputs.items():
        if location in captured and captured[location] != raw:
            raise ValueError("input changed between captures")
        captured.setdefault(location, raw)
    candidate = capture_core.capture(
        captured, str((staged / Path(TARGET).name).relative_to(ROOT)), candidate_sha
    )
    expected, event = expected_document(
        original, plan, receipt["appended_native_inline_history"]["timestamp"]
    )
    rendered, _, _ = render_candidate(original, plan, event["timestamp"])
    if candidate != rendered or yaml.safe_load(candidate) != expected:
        raise ValueError("candidate differs from exact declared identity correction")
    if event != receipt["appended_native_inline_history"]:
        raise ValueError("native event differs")
    capture_core.unchanged(captured, revision)
    if plan_only:
        return {"planned": True, "target": TARGET, "candidate_sha256": candidate_sha}
    output.mkdir(parents=True)
    (output / "before.yaml").write_bytes(original)
    write_validated_community(expected, output / "validated.yaml")
    if yaml.safe_load((output / "validated.yaml").read_bytes()) != expected:
        raise ValueError("native serialization differs")
    capture_core.unchanged(captured, revision)
    (output / "replacement.yaml").write_bytes(candidate)
    (output / "replacement.yaml").replace(path(TARGET))
    if path(TARGET).read_bytes() != candidate:
        raise ValueError("persisted candidate differs")
    result = {
        "applied": True,
        "target": TARGET,
        "target_id": TARGET_ID,
        "execution_revision": revision,
        "scope": SCOPE,
        "scientific_review": False,
        "before_sha256": BEFORE,
        "after_sha256": candidate_sha,
        "source_plan": item,
        "reviewed_receipt": {"path": receipt_name, "sha256": receipt_sha},
        "appended_native_inline_history": event,
        "inputs": expected_inputs,
        "helper_sha256": sha(inputs[Path(__file__)]),
        "created_at": datetime.now(timezone.utc).isoformat(),
        "sidecar_status": "PENDING native scaffold and validation",
        "limitations": "Identity correction only; roster and graph findings remain explicit. Mapping and final QC are separate.",
    }
    (output / "receipt.json").write_text(json.dumps(result, indent=2) + "\n")
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
