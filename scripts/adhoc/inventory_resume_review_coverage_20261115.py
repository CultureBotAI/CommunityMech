"""Inventory retained review coverage for the resumed M5 scope (2026-11-15).

Inputs: exact Git record inventory, native validated list, immutable reviews.
Outputs: JSON on stdout only; caller owns exclusive evidence/report destinations.
Supports the broad-scope recovery follow-up to PR #2775. No provider calls,
canonical edits, review saves, or historical batch reconstruction are performed.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.metadata
import json
import platform
import subprocess
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path, PurePosixPath

import yaml

ROOTS = ("kb/communities", "data/isolates")
CONTEXT = (
    "scripts/record_review.py",
    "schema/record_review.yaml",
    ".claude/skills/review-yaml-record/SKILL.md",
    "docs/record-review-profile.md",
    "docs/record-reviews.md",
    "conf/record_review.yaml",
    "pyproject.toml",
    "uv.lock",
    ".python-version",
)
LIST_KEYS = (
    "review_id",
    "repository",
    "kind",
    "finished_at",
    "completion",
    "verdict",
    "scientific_review",
    "scope",
    "targets",
)


def digest(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def encoded(value: object) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":")).encode()


def now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")


def git(root: Path, *args: str) -> bytes:
    return subprocess.check_output(["git", "-C", str(root), *args], stderr=subprocess.PIPE)


def read_regular(root: Path, relative: str) -> bytes:
    path = PurePosixPath(relative)
    if path.is_absolute() or ".." in path.parts:
        raise ValueError(f"unsafe repository-relative path: {relative}")
    current = root
    for part in path.parts:
        current /= part
        if current.is_symlink():
            raise ValueError(f"symlink input refused: {relative}")
    if not current.is_file():
        raise FileNotFoundError(relative)
    return current.read_bytes()


def review_paths(root: Path) -> list[str]:
    """Ordinary directory listing includes hidden and ignored entries."""
    result = []
    for directory in sorted((root / "reviews/structured").iterdir()):
        if directory.is_symlink() or not directory.is_dir():
            raise ValueError("unsafe entry in structured reviews")
        if sorted(p.name for p in directory.iterdir()) != ["review.md", "review.yaml"]:
            raise ValueError(f"incomplete review bundle: {directory.name}")
        result.append(f"reviews/structured/{directory.name}/review.yaml")
    return result


def validation_context(root: Path) -> dict:
    paths = list(CONTEXT)
    for relative in review_paths(root):
        paths.extend((relative, relative.removesuffix(".yaml") + ".md"))
    return {p: digest(read_regular(root, p)) for p in sorted(paths)}


def capture_native(root: Path, expected_revision: str) -> dict:
    revision = git(root, "rev-parse", "HEAD").decode().strip()
    if revision != expected_revision:
        raise ValueError("HEAD does not match expected revision")
    before = validation_context(root)
    started = now()
    command = [sys.executable, "scripts/record_review.py", "list"]
    process = subprocess.run(command, cwd=root, capture_output=True, check=False)
    after = validation_context(root)
    if before != after or git(root, "rev-parse", "HEAD").decode().strip() != revision:
        raise ValueError("native validation inputs or HEAD changed during validation")
    return {
        "format": "m5-native-review-list-capture-v1",
        "revision": revision,
        "started_at": started,
        "finished_at": now(),
        "command": [".venv/bin/python", "scripts/record_review.py", "list"],
        "python": platform.python_version(),
        "packages": {
            name: importlib.metadata.version(name)
            for name in ("linkml", "linkml-runtime", "jsonschema", "PyYAML")
        },
        "exit_code": process.returncode,
        "stdout_sha256": digest(process.stdout),
        "stdout": process.stdout.decode(),
        "stderr_sha256": digest(process.stderr),
        "stderr": process.stderr.decode(),
        "validation_inputs": before,
        "before_after_inputs_equal": True,
    }


def validated_metadata(root: Path, capture: dict, expected_revision: str) -> list[dict]:
    if (
        capture.get("format") != "m5-native-review-list-capture-v1"
        or capture.get("revision") != expected_revision
        or capture.get("command") != [".venv/bin/python", "scripts/record_review.py", "list"]
        or capture.get("exit_code") != 0
        or capture.get("before_after_inputs_equal") is not True
    ):
        raise ValueError("missing, failed, wrong-command or wrong-revision native capture")
    if (
        digest(capture["stdout"].encode()) != capture["stdout_sha256"]
        or digest(capture["stderr"].encode()) != capture["stderr_sha256"]
    ):
        raise ValueError("native capture byte hashes disagree")
    if capture["validation_inputs"] != validation_context(root):
        raise ValueError("native validation context changed")
    metadata = json.loads(capture["stdout"])
    if not isinstance(metadata, list):
        raise ValueError("native list is not an array")
    if sorted(row["path"] for row in metadata) != review_paths(root):
        raise ValueError("native list does not cover the exact retained review set")
    for row in metadata:
        review = yaml.safe_load(read_regular(root, row["path"]))
        actual = {"path": row["path"], **{key: review[key] for key in LIST_KEYS}}
        if row != actual:
            raise ValueError(f"native metadata disagrees with immutable bundle: {row['path']}")
    return metadata


def record_inventory(root: Path, revision: str, expected_count: int) -> list[dict]:
    if git(root, "rev-parse", "HEAD").decode().strip() != revision:
        raise ValueError("HEAD does not match inventory revision")
    entries = git(root, "ls-tree", "-r", "-z", revision, "--", *ROOTS)
    selected = {}
    for entry in entries.split(b"\0"):
        if not entry:
            continue
        metadata, raw_path = entry.split(b"\t", 1)
        path = raw_path.decode()
        pure = PurePosixPath(path)
        if str(pure.parent) not in ROOTS or pure.suffix != ".yaml":
            continue
        mode, kind, blob = metadata.decode().split()
        if mode not in {"100644", "100755"} or kind != "blob":
            raise ValueError(f"nonregular Git record: {path}")
        selected[path] = blob
    disk_paths = sorted(
        str(p.relative_to(root)) for directory in ROOTS for p in (root / directory).glob("*.yaml")
    )
    if disk_paths != sorted(selected):
        raise ValueError("Git and ignore-independent filesystem record inventories differ")
    if len(selected) != expected_count:
        raise ValueError(f"record count changed: expected {expected_count}, found {len(selected)}")
    result = []
    for path, blob in sorted(selected.items()):
        raw = read_regular(root, path)
        original = git(root, "cat-file", "blob", blob)
        if raw != original:
            raise ValueError(f"record working bytes differ from frozen revision: {path}")
        record = yaml.safe_load(raw)
        if not isinstance(record, dict) or not isinstance(record.get("id"), str):
            raise ValueError(f"record lacks a stable string ID: {path}")
        result.append(
            {
                "path": path,
                "record_id": record["id"],
                "git_blob": blob,
                "sha256": digest(raw),
                "reviews": [],
            }
        )
    return result


def occurrence(review: dict, target: dict, record: dict) -> dict:
    inputs = {item["path"]: item["sha256"] for item in review["source"]["inputs"]}
    if target["path"] not in inputs:
        raise ValueError("validated target has no saved input hash")
    listed_id = target["target_id"]
    assessed = listed_id in review["scope"]["reviewed_target_ids"]
    identity_match = listed_id == record["record_id"]
    scientific = (
        assessed
        and identity_match
        and review["scientific_review"]
        and review["completion"] != "failed"
    )
    full_declared = (
        scientific and review["completion"] == "completed" and review["scope"]["coverage"] == "full"
    )
    full_record_declared = (
        full_declared and review["kind"] == "record" and not target.get("selector")
    )
    matches = inputs[target["path"]] == record["sha256"]
    return {
        "review_id": review["review_id"],
        "finished_at": review["finished_at"],
        "listed_target_id": listed_id,
        "target_id_matches_current": identity_match,
        "selector": target.get("selector"),
        "actually_assessed": assessed,
        "scientific_assessed": scientific,
        "declared_full_scientific_scope": full_declared,
        "declared_full_record_scientific_scope": full_record_declared,
        "saved_record_sha256": inputs[target["path"]],
        "current_record_bytes_match": matches,
    }


def summarize(records: list[dict]) -> dict:
    predicates = {
        "listed_in_validated_bundle": lambda o: True,
        "actually_assessed_matching_identity": lambda o: o["actually_assessed"]
        and o["target_id_matches_current"],
        "scientific_assessed": lambda o: o["scientific_assessed"],
        "declared_full_scientific_scope_any_kind": lambda o: o["declared_full_scientific_scope"],
        "declared_full_record_scientific_scope": lambda o: o[
            "declared_full_record_scientific_scope"
        ],
        "current_bytes_any_validated_bundle": lambda o: o["current_record_bytes_match"],
        "current_bytes_scientific_assessed": lambda o: o["current_record_bytes_match"]
        and o["scientific_assessed"],
        "current_bytes_declared_full_record_scientific_scope": lambda o: o[
            "current_record_bytes_match"
        ]
        and o["declared_full_record_scientific_scope"],
    }
    summary = {
        name: sum(any(predicate(o) for o in record["reviews"]) for record in records)
        for name, predicate in predicates.items()
    }
    summary["not_listed_in_any_validated_bundle"] = sum(not r["reviews"] for r in records)
    summary["listed_but_no_current_bytes_occurrence"] = sum(
        bool(r["reviews"]) and not any(o["current_record_bytes_match"] for o in r["reviews"])
        for r in records
    )
    summary["non_record_id_target_occurrences"] = sum(
        not o["target_id_matches_current"] for r in records for o in r["reviews"]
    )
    return summary


def inventory(root: Path, capture_path: Path, revision: str, expected_count: int) -> dict:
    capture_relative = str(capture_path.resolve().relative_to(root))
    capture_raw = capture_path.read_bytes()
    capture = json.loads(capture_raw)
    metadata = validated_metadata(root, capture, revision)
    records = record_inventory(root, revision, expected_count)
    by_path = {record["path"]: record for record in records}
    reviews, outside = [], []
    for item in metadata:
        review = yaml.safe_load(read_regular(root, item["path"]))
        reviews.append(
            {
                "path": item["path"],
                "sha256": digest(read_regular(root, item["path"])),
                **{key: review[key] for key in LIST_KEYS if key not in {"targets", "scope"}},
                "scope_coverage": review["scope"]["coverage"],
                "scope_description": review["scope"]["description"],
                "population_size": review["scope"]["population_size"],
                "source_revision": review["source"]["git_revision"],
                "source_state": review["source"]["state"],
                "source_input_manifest_sha256": digest(encoded(review["source"]["inputs"])),
                "native_provenance_strength": (
                    "historical_git_input_bytes_verified"
                    if review["source"]["state"] == "git_commit"
                    else "working_tree_input_hash_attestation_with_existing_git_base"
                ),
            }
        )
        for target in review["targets"]:
            if target["path"] in by_path:
                record = by_path[target["path"]]
                record["reviews"].append(occurrence(review, target, record))
            else:
                outside.append({"review_id": review["review_id"], **target})
    for record in records:
        record["reviews"].sort(key=lambda o: (o["finished_at"], o["review_id"]))
    record_hashes = [
        {key: record[key] for key in ("path", "record_id", "git_blob", "sha256")}
        for record in records
    ]
    if (
        git(root, "rev-parse", "HEAD").decode().strip() != revision
        or validation_context(root) != capture["validation_inputs"]
        or any(digest(read_regular(root, r["path"])) != r["sha256"] for r in records)
    ):
        raise ValueError("frozen inventory or validated inputs changed while deriving coverage")
    return {
        "format": "m5-resume-review-coverage-v1",
        "generated_at": now(),
        "revision": revision,
        "generator": {
            "path": "scripts/adhoc/inventory_resume_review_coverage_20261115.py",
            "sha256": digest(Path(__file__).read_bytes()),
        },
        "record_globs": [f"{path}/*.yaml" for path in ROOTS],
        "record_inventory_sha256": digest(encoded(record_hashes)),
        "record_count": len(records),
        "valid_review_count": len(reviews),
        "native_capture_sha256": digest(capture_raw),
        "native_capture_path": capture_relative,
        "native_validation": {
            key: capture[key]
            for key in (
                "revision",
                "started_at",
                "finished_at",
                "command",
                "python",
                "packages",
                "exit_code",
                "stdout_sha256",
                "stderr_sha256",
                "before_after_inputs_equal",
            )
        },
        "validation_input_manifest_sha256": digest(encoded(capture["validation_inputs"])),
        "bundle_kind_counts": dict(Counter(r["kind"] for r in reviews)),
        "bundle_completion_counts": dict(Counter(r["completion"] for r in reviews)),
        "bundle_scientific_flag_counts": dict(
            Counter(str(r["scientific_review"]).lower() for r in reviews)
        ),
        "coverage": summarize(records),
        "coverage_by_record_root": {
            prefix: {
                "record_count": sum(
                    str(PurePosixPath(r["path"]).parent) == prefix for r in records
                ),
                **summarize([r for r in records if str(PurePosixPath(r["path"]).parent) == prefix]),
            }
            for prefix in ROOTS
        },
        "records_without_validated_bundle": [r["path"] for r in records if not r["reviews"]],
        "records": records,
        "reviews": reviews,
        "targets_outside_declared_record_set": outside,
        "limitations": [
            "Native list validates bundle structure, Markdown and retained Git provenance; it does not verify scientific truth.",
            "The historical goal counted a target listed in a valid bundle; stronger subsets do not redefine that criterion.",
            "Full scientific coverage is a saved declaration, not an independently re-audited all-claims conclusion.",
            "Full batch/category population coverage does not establish whole-record claim coverage.",
            "Synthetic cohort/claim target IDs may intentionally differ from a record ID; those occurrences are retained but excluded from canonical-ID scientific coverage.",
            "Current-byte matches apply only to the target record, not all evidence, dependencies, or finding acceptance.",
            "Working-tree source hashes are reviewer attestations; native validation checks their Git base exists.",
            "No provider requests, scientific reviews, curation changes, issue closure or historical batch reconstruction occurred.",
        ],
    }


def render_summary(ledger: dict) -> str:
    if ledger.get("format") != "m5-resume-review-coverage-v1":
        raise ValueError("not a resume coverage ledger")
    coverage = ledger["coverage"]
    labels = {
        "listed_in_validated_bundle": "Listed in any validated bundle (historical goal criterion)",
        "actually_assessed_matching_identity": "Actually assessed, with matching current record identity",
        "scientific_assessed": "Has an assessed scientific-review declaration",
        "declared_full_scientific_scope_any_kind": "Completed scientific review declaring full scope, any kind",
        "declared_full_record_scientific_scope": "Completed scientific record review declaring full scope, no selector",
        "current_bytes_any_validated_bundle": "Record bytes match at least one validated bundle",
        "current_bytes_scientific_assessed": "Record bytes match at least one assessed scientific declaration",
        "current_bytes_declared_full_record_scientific_scope": "Record bytes match a completed full-scope scientific record declaration",
        "not_listed_in_any_validated_bundle": "Not listed in any validated bundle",
        "listed_but_no_current_bytes_occurrence": "Listed, but record bytes match no retained occurrence",
    }
    lines = [
        "# Retained review coverage for resumed M5 work",
        "",
        f"Generated {ledger['generated_at']} against `{ledger['revision']}`.",
        "",
        f"The exact Git inventory contains **{ledger['record_count']} records**; the native list "
        f"validated **{ledger['valid_review_count']} immutable bundles**. This is a coverage "
        "inventory, not a new scientific assessment.",
        "",
        "| Distinct current records | Count |",
        "| --- | ---: |",
    ]
    lines.extend(f"| {label} | {coverage[key]} |" for key, label in labels.items())
    lines.extend(
        [
            "",
            "The rows overlap and must not be added. A full-scope declaration is the author's "
            "saved scope; this inventory does not certify all claims were adequately assessed. "
            "Batch/category population coverage stays separate from full record declarations. "
            "A target-byte match is not a source-cache, dependency, or finding-resolution check.",
            "",
            f"There are {coverage['non_record_id_target_occurrences']} target occurrences whose "
            "review-local ID differs from the canonical record ID. These include intentional "
            "cohort selectors; they are not automatically identity defects. They contribute "
            "to the weak path-presence count but not canonical-ID scientific coverage.",
            "",
            "| Record root | Records | Any validated bundle | Scientific declaration | Full record declaration | Current bytes + full record declaration |",
            "| --- | ---: | ---: | ---: | ---: | ---: |",
        ]
    )
    for prefix, counts in ledger["coverage_by_record_root"].items():
        lines.append(
            f"| `{prefix}` | {counts['record_count']} | "
            f"{counts['listed_in_validated_bundle']} | {counts['scientific_assessed']} | "
            f"{counts['declared_full_record_scientific_scope']} | "
            f"{counts['current_bytes_declared_full_record_scientific_scope']} |"
        )
    lines.extend(
        [
            "",
            "Every current path, stable ID, Git blob and SHA-256 is retained in "
            "[coverage.json](coverage.json), together with every matching historical review occurrence, "
            "its saved target hash, assessed-target membership, selector and declared coverage. "
            "Historical reviews and findings are not rewritten or superseded by this report.",
            "",
            "Native validation used the frozen development environment and unchanged review/schema/"
            "script/config/lock inputs before and after the run. The bound private capture is "
            f"`{ledger['native_capture_path']}`; its SHA-256 is "
            f"`{ledger['native_capture_sha256']}`. The public ledger preserves the command, timestamps, "
            "exit code, runtime versions, stdout/stderr hashes and validation-input-manifest digest.",
            "",
            "Both filesystem record enumeration and native bundle enumeration include ignored/hidden "
            "entries. The record inventory agrees exactly with the two declared Git path globs. "
            "Records under `kb/taxa/` are outside the original campaign's declared record set.",
            "",
            "The original criterion counted presence in a validated bundle. Actual scientific work "
            "must also examine the scope, evidence and retained findings; it must not turn the presence "
            "count into a whole-corpus scientific approval. See [scope recovery](scope-recovery.md).",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, default=Path.cwd())
    parser.add_argument("--expected-revision")
    commands = parser.add_subparsers(dest="mode", required=True)
    commands.add_parser("capture-native")
    build = commands.add_parser("inventory")
    build.add_argument("--capture", type=Path, required=True)
    build.add_argument("--expected-record-count", type=int, default=549)
    render = commands.add_parser("render-summary")
    render.add_argument("--ledger", type=Path, required=True)
    args = parser.parse_args()
    root = args.repo_root.resolve()
    try:
        if args.mode == "render-summary":
            print(render_summary(json.loads(args.ledger.read_bytes())), end="")
            return 0
        if not args.expected_revision:
            raise ValueError("--expected-revision is required for capture and inventory")
        if args.mode == "capture-native":
            result = capture_native(root, args.expected_revision)
        else:
            result = inventory(
                root, args.capture, args.expected_revision, args.expected_record_count
            )
        print(json.dumps(result, indent=2, ensure_ascii=False))
        return result.get("exit_code", 0)
    except (ValueError, OSError, KeyError, subprocess.CalledProcessError) as exc:
        print(f"inventory refused: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
