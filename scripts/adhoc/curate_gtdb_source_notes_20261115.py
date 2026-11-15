"""Stage/apply one source-pinned taxonomy-note correction; #2869, 2026-11-15.

Inputs: reviewed JSON plan, immutable record/source hashes and exact Git revision.
Outputs: exclusive private stage/application evidence; apply alone replaces the
named canonical record through native validation. This is the note-only first
transition; database correction, sidecars, final gates and review follow separately.
No source acquisition. Existing mapping-only engine and successor core are untouched.
"""

from __future__ import annotations

import argparse
import copy
import difflib
import hashlib
import json
import re
import subprocess
import textwrap
from datetime import datetime, timezone
from pathlib import Path

import yaml

from communitymech.curate.curation_event import record_curation_event
from communitymech.validation.write_validated import write_validated_community

ROOT = Path(__file__).resolve().parents[2]
ACTION = "CLARIFY_GTDB_SOURCE_SCOPE"
CURATOR = "Codex"
REQUIRED = (
    "src/communitymech/curate/curation_event.py",
    "src/communitymech/validation/write_validated.py",
    "src/communitymech/schema/communitymech.yaml",
    "src/communitymech/schema/mech_shared.yaml",
    "src/communitymech/schema/history.yaml",
    "pyproject.toml",
    "uv.lock",
)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def head():
    return subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip()


def path(name, *, private=False):
    relative = Path(name)
    result = ROOT / relative
    if (
        relative.is_absolute()
        or ".." in relative.parts
        or not result.resolve().is_relative_to(ROOT.resolve())
        or (private and not name.startswith(".temp/"))
        or result.is_symlink()
    ):
        raise ValueError("safe repository-relative path required")
    return result


def capture(captured, name, expected=None):
    location = path(name)
    if location not in captured:
        captured[location] = location.read_bytes()
    raw = captured[location]
    if expected is not None and sha(raw) != expected:
        raise ValueError("accepted input differs: " + name)
    return raw


def unchanged(captured, revision):
    if head() != revision or any(p.read_bytes() != raw for p, raw in captured.items()):
        raise ValueError("captured input or revision changed")


def expected_document(original, plan, timestamp):
    before = yaml.safe_load(original)
    if before["id"] != plan["target_id"] or sha(original) != plan["before_sha256"]:
        raise ValueError("exact known original required")
    expected = copy.deepcopy(before)
    seen = set()
    for change in plan["notes"]:
        index = change["taxonomy_index"]
        if type(index) is not int or index < 0 or index in seen:
            raise ValueError("unique explicit taxonomy index required")
        seen.add(index)
        member = expected["taxonomy"][index]
        if (
            member["taxon_term"] != change["existing_descriptor"]
            or member.get("strain_designation") != change["existing_stock"]
            or member["taxon_term"].get("notes") != change["before"]
            or not isinstance(change["after"], str)
            or not change["after"].strip()
            or "\n" in change["after"]
            or change["before"] == change["after"]
        ):
            raise ValueError("exact existing note, descriptor and stock required")
        member["taxon_term"]["notes"] = change["after"]
    if not seen or not re.fullmatch(r"\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ", timestamp):
        raise ValueError("substantive note correction and explicit native timestamp required")
    event = record_curation_event(
        expected,
        curator=CURATOR,
        action=ACTION,
        changes=plan["event_changes"],
        llm_assisted=True,
        timestamp=timestamp,
    )
    return expected, event


def child(node, key):
    matches = [(k, v) for k, v in node.value if k.value == key]
    if len(matches) != 1:
        raise ValueError("one unambiguous YAML mapping key required: " + key)
    return matches[0]


def render_candidate(original, plan, timestamp):
    expected, event = expected_document(original, plan, timestamp)
    text = original.decode()
    root_node = yaml.compose(text)
    taxonomy = child(root_node, "taxonomy")[1]
    replacements = []
    for change in plan["notes"]:
        descriptor = child(taxonomy.value[change["taxonomy_index"]], "taxon_term")[1]
        key, value = child(descriptor, "notes")
        start = text.rfind("\n", 0, key.start_mark.index) + 1
        end = value.end_mark.index
        if end < len(text) and text[end] == "\n":
            end += 1
        indent = " " * key.start_mark.column
        new = indent + "notes: >-\n"
        new += (
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
        replacements.append((start, end, new))
    history = child(root_node, "curation_history")[1]
    if not history.value or text[history.end_mark.index :].strip():
        raise ValueError("existing final block history required")
    if history.start_mark.column != 0:
        raise ValueError("native column-zero history sequence required")
    replacements.append(
        (
            history.end_mark.index,
            history.end_mark.index,
            yaml.safe_dump([event], sort_keys=False, allow_unicode=True, width=110),
        )
    )
    for start, end, new in sorted(replacements, reverse=True):
        text = text[:start] + new + text[end:]
    if yaml.safe_load(text) != expected:
        raise ValueError("text-preserving candidate changes undeclared content")
    return text.encode(), expected, event


def verify_candidate(original, candidate, plan):
    before, after = yaml.safe_load(original), yaml.safe_load(candidate)
    added = after.get("curation_history", [])[len(before.get("curation_history", [])) :]
    if len(added) != 1:
        raise ValueError("exactly one native event required")
    expected, event = expected_document(original, plan, added[0].get("timestamp", ""))
    if after != expected or added != [event]:
        raise ValueError("candidate changes undeclared content or native history")
    return after, event


def prepare(plan_name, plan_sha, revision):
    if head() != revision or not re.fullmatch(r"[0-9a-f]{40}", revision):
        raise ValueError("exact current revision required")
    captured = {}
    plan = json.loads(capture(captured, plan_name, plan_sha))
    if (
        plan.get("scope") != "taxonomy-notes-only"
        or plan.get("scientific_review") is not False
        or not plan["target"].startswith(("kb/communities/", "data/isolates/"))
    ):
        raise ValueError("explicit single-record note-only plan required")
    for name, digest in plan["inputs"].items():
        capture(captured, name, digest)
    if plan["inputs"].get(plan["target"]) != plan["before_sha256"]:
        raise ValueError("plan must bind actual original record")
    for item in plan["source_anchors"]:
        if item["path"] not in plan["inputs"] or not item["text"]:
            raise ValueError("bound nonempty source anchor required")
        if item["text"] not in capture(captured, item["path"]).decode():
            raise ValueError("source anchor absent from captured bytes")
    if not plan["source_anchors"]:
        raise ValueError("source-backed note correction required")
    for name in (*REQUIRED, str(Path(__file__).relative_to(ROOT))):
        capture(captured, name)
    original = capture(captured, plan["target"], plan["before_sha256"])
    return plan, original, captured


def stage(plan_name, plan_sha, output_name, revision, *, plan_only=False):
    output = path(output_name, private=True)
    if output.exists():
        raise ValueError("exclusive private output required")
    plan, original, captured = prepare(plan_name, plan_sha, revision)
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    candidate, expected, event = render_candidate(original, plan, timestamp)
    metadata = {
        "target": plan["target"],
        "target_id": plan["target_id"],
        "execution_revision": revision,
        "source_plan": {"path": plan_name, "sha256": plan_sha},
        "before_sha256": sha(original),
        "inputs": {str(p.relative_to(ROOT)): sha(raw) for p, raw in captured.items()},
        "scope": "taxonomy-notes-only",
        "scientific_review": False,
        "intermediate_state": "Note correction only; database mapping correction and final QC pending.",
    }
    if plan_only:
        unchanged(captured, revision)
        return {**metadata, "planned": True}
    output.mkdir(parents=True)
    write_validated_community(expected, output / "validated.yaml")
    if yaml.safe_load((output / "validated.yaml").read_bytes()) != expected:
        raise ValueError("native serialization differs")
    unchanged(captured, revision)
    (output / Path(plan["target"]).name).write_bytes(candidate)
    diff = "".join(
        difflib.unified_diff(
            original.decode().splitlines(keepends=True),
            candidate.decode().splitlines(keepends=True),
            fromfile=plan["target"],
            tofile="staged/" + Path(plan["target"]).name,
        )
    )
    (output / "candidate.diff").write_text(diff)
    result = {
        **metadata,
        "candidate_sha256": sha(candidate),
        "candidate_diff_sha256": sha(diff.encode()),
        "native_serialization_sha256": sha((output / "validated.yaml").read_bytes()),
        "source_inputs_unchanged": True,
        "canonical_apply": False,
        "completed_at": datetime.now(timezone.utc).isoformat(),
        "appended_native_inline_history": event,
    }
    (output / "receipt.json").write_text(json.dumps(result, indent=2) + "\n")
    return result


def apply(stage_name, candidate_sha, receipt_sha, output_name, revision, *, plan_only=False):
    stage_dir, output = path(stage_name, private=True), path(output_name, private=True)
    if output.exists():
        raise ValueError("exclusive private output required")
    captured = {}
    receipt_name = str((stage_dir / "receipt.json").relative_to(ROOT))
    receipt = json.loads(capture(captured, receipt_name, receipt_sha))
    if (
        receipt.get("canonical_apply") is not False
        or receipt.get("source_inputs_unchanged") is not True
        or receipt.get("execution_revision") != revision
        or receipt.get("candidate_sha256") != candidate_sha
        or receipt.get("scope") != "taxonomy-notes-only"
    ):
        raise ValueError("exact completed same-revision note stage required")
    item = receipt["source_plan"]
    plan, original, inputs = prepare(item["path"], item["sha256"], revision)
    for location, raw in inputs.items():
        if location in captured and captured[location] != raw:
            raise ValueError("input changed between captures")
        captured.setdefault(location, raw)
    expected_inputs = {str(p.relative_to(ROOT)): sha(raw) for p, raw in inputs.items()}
    if receipt["inputs"] != expected_inputs or receipt["target"] != plan["target"]:
        raise ValueError("stage input coverage or target differs")
    if receipt["target_id"] != plan["target_id"] or receipt["before_sha256"] != sha(original):
        raise ValueError("actual target baseline differs")
    candidate_name = str((stage_dir / Path(plan["target"]).name).relative_to(ROOT))
    candidate = capture(captured, candidate_name, candidate_sha)
    after, event = verify_candidate(original, candidate, plan)
    if event != receipt["appended_native_inline_history"]:
        raise ValueError("reviewed native event differs")
    unchanged(captured, revision)
    if plan_only:
        return {"planned": True, "target": plan["target"], "candidate_sha256": candidate_sha}
    output.mkdir(parents=True)
    (output / "before.yaml").write_bytes(original)
    write_validated_community(after, output / "validated.yaml")
    if yaml.safe_load((output / "validated.yaml").read_bytes()) != after:
        raise ValueError("native serialization differs")
    unchanged(captured, revision)
    (output / "replacement.yaml").write_bytes(candidate)
    (output / "replacement.yaml").replace(path(plan["target"]))
    if path(plan["target"]).read_bytes() != candidate:
        raise ValueError("persisted candidate differs")
    result = {
        "applied": True,
        "target": plan["target"],
        "target_id": plan["target_id"],
        "execution_revision": revision,
        "before_sha256": sha(original),
        "after_sha256": sha(candidate),
        "source_plan": item,
        "reviewed_receipt": {"path": receipt_name, "sha256": receipt_sha},
        "appended_native_inline_history": event,
        "inputs": expected_inputs,
        "helper_sha256": sha(inputs[Path(__file__)]),
        "created_at": datetime.now(timezone.utc).isoformat(),
        "scientific_review": False,
        "scope": "taxonomy-notes-only",
        "intermediate_state": receipt["intermediate_state"],
        "sidecar_status": "PENDING separate native scaffold and validation",
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
