"""Plan and preserve exact private review inputs for Phase2, 2026-11-15.

Inputs: explicitly named saved native review YAML/Markdown pairs and only their
declared source.inputs. Outputs: exclusive private plan, namespaced immutable
snapshot and verified manifest. No discovery of secrets, ontology databases,
network transfer, source mutation or historical-byte substitution. A later M5
copy must canary one missing file with the same rsync path and verify hashes.
"""

import argparse
import hashlib
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path, PurePosixPath

import yaml

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts"))
from record_review import render_markdown, validate_review  # noqa: E402

MAX_FILE = 100 * 1024 * 1024
MAX_TOTAL = 250 * 1024 * 1024
REMOTE_HOST = "marcins-MacBook-Pro-3.local"
REMOTE_CHECKOUT = "/Users/marcin/agent-work/CommunityMech/phase2-completion-20261115"


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def relative_path(value):
    path = PurePosixPath(value)
    if (
        not value
        or path.is_absolute()
        or any(part in {"", ".", ".."} for part in value.split("/"))
        or "\n" in value
        or "\r" in value
        or "\0" in value
    ):
        raise ValueError("unsafe declared path")
    if any(part == ".env" or part.startswith(".env.") for part in path.parts):
        raise ValueError("environment/credential files are not permitted review inputs")
    return Path(*path.parts)


def input_bytes(root, relative):
    path = root / relative_path(relative)
    if not path.resolve().is_relative_to(root.resolve()):
        raise ValueError("declared source resolves outside its explicit checkout")
    if not path.is_file():
        raise ValueError("declared source is missing or not a regular file")
    if path.stat().st_size > MAX_FILE:
        raise ValueError("declared source exceeds bounded 100 MiB file limit")
    return path.read_bytes()


def private_output(path):
    path = path.absolute()
    if not path.resolve().is_relative_to(ROOT / ".temp"):
        raise ValueError("output must remain in this repository's private .temp")
    if path.exists() or path.is_symlink():
        raise ValueError("output already exists; choose a fresh attempt")
    return path


def plan_review(requested, optional=False):
    path = requested.resolve()
    if path.name != "review.yaml" or path.parent.parent.name != "structured":
        raise ValueError("explicit saved reviews/structured/ID/review.yaml required")
    root = path.parents[3]
    if path.parents[2].name != "reviews":
        raise ValueError("native review directory required")
    raw = path.read_bytes()
    review = yaml.safe_load(raw)
    validate_review(review)
    identifier = review["review_id"]
    if (
        not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_.-]+", identifier)
        or path.parent.name != identifier
    ):
        raise ValueError("native review namespace differs")
    markdown = path.with_name("review.md").read_bytes()
    if markdown.decode() != render_markdown(review):
        raise ValueError("saved Markdown differs from native rendering")
    declarations = [
        (item["path"], item["sha256"], "input") for item in review["source"]["inputs"]
    ] + [
        (str(path.relative_to(root)), digest(raw), "review_yaml"),
        (str(path.with_name("review.md").relative_to(root)), digest(markdown), "review_markdown"),
    ]
    rows, seen = [], set()
    for relative, expected, role in declarations:
        relative_path(relative)
        if relative in seen:
            raise ValueError("duplicate declared input path")
        seen.add(relative)
        destination = f"{identifier}/inputs/{relative}"
        row = {
            "original_path": relative,
            "snapshot_path": destination,
            "expected_sha256": expected,
            "role": role,
        }
        try:
            content = input_bytes(root, relative)
            row.update(actual_sha256=digest(content), bytes=len(content))
            row["status"] = "matched" if row["actual_sha256"] == expected else "changed"
        except (OSError, ValueError) as error:
            row.update(status="unavailable", detail=str(error))
        rows.append(row)
    ready = all(row["status"] == "matched" for row in rows)
    return {
        "review_id": identifier,
        "source_checkout": str(root),
        "optional": optional,
        "status": "ready" if ready else "blocked",
        "files": rows,
    }


def snapshot(plan, output):
    output = private_output(output)
    if plan["status"] != "ready":
        raise ValueError("required review inputs are not ready")
    selected = [row for row in plan["reviews"] if row["status"] == "ready"]
    names = [row["review_id"] for row in selected]
    if not names or len(set(names)) != len(names):
        raise ValueError("nonempty unique review namespaces required")
    # Verify every byte before creating the snapshot directory.
    captured = []
    captured_bytes = 0
    for review in selected:
        for row in review["files"]:
            raw = input_bytes(Path(review["source_checkout"]), row["original_path"])
            if digest(raw) != row["expected_sha256"] or len(raw) != row["bytes"]:
                raise ValueError("input changed after planning: " + row["original_path"])
            captured_bytes += len(raw)
            if captured_bytes > MAX_TOTAL:
                raise ValueError("snapshot exceeds bounded 250 MiB total limit")
            destination = str(relative_path(row["snapshot_path"]))
            if destination != f"{review['review_id']}/inputs/{row['original_path']}":
                raise ValueError("input destination does not preserve its review namespace")
            captured.append((review["review_id"], row, raw))
    total = sum(len(raw) for _, _, raw in captured)
    if total > MAX_TOTAL:
        raise ValueError("snapshot exceeds bounded 250 MiB total limit")
    output.mkdir(parents=True)
    files = []
    for identifier, row, raw in captured:
        target = output / row["snapshot_path"]
        target.parent.mkdir(parents=True, exist_ok=True)
        with target.open("xb") as stream:
            stream.write(raw)
        if target.read_bytes() != raw:
            raise ValueError("snapshot did not persist exact bytes")
        files.append(
            {
                "review_id": identifier,
                "original_path": row["original_path"],
                "path": row["snapshot_path"],
                "sha256": row["expected_sha256"],
                "bytes": len(raw),
                "role": row["role"],
            }
        )
    manifest = {
        "schema_version": 1,
        "created_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "status": "complete",
        "plan_sha256": digest(json.dumps(plan, sort_keys=True).encode()),
        "review_ids": names,
        "file_count": len(files),
        "total_bytes": total,
        "scope": "Exact reviewed source bytes plus native saved YAML/Markdown; private preservation, not new scientific approval.",
        "files": files,
    }
    with (output / "manifest.json").open("x") as stream:
        json.dump(manifest, stream, indent=2)
        stream.write("\n")
    return verify(output)


def verify(directory):
    directory = directory.resolve()
    manifest_raw = (directory / "manifest.json").read_bytes()
    manifest = json.loads(manifest_raw)
    if manifest["status"] != "complete":
        raise ValueError("incomplete snapshot")
    expected = {"manifest.json"}
    total = 0
    for row in manifest["files"]:
        name = str(relative_path(row["path"]))
        if name in expected:
            raise ValueError("duplicate snapshot artifact")
        expected.add(name)
        path = directory / name
        if path.is_symlink() or not path.resolve().is_relative_to(directory):
            raise ValueError("snapshot artifact symlink or path escape")
        raw = path.read_bytes()
        if digest(raw) != row["sha256"] or len(raw) != row["bytes"]:
            raise ValueError("snapshot artifact hash or size differs: " + name)
        total += len(raw)
    discovered = list(directory.rglob("*"))
    if any(path.is_symlink() for path in discovered):
        raise ValueError("snapshot contains an unexpected symlink")
    actual = {str(path.relative_to(directory)) for path in discovered if path.is_file()}
    if actual != expected or len(manifest["files"]) != manifest["file_count"]:
        raise ValueError("snapshot membership differs")
    if total != manifest["total_bytes"]:
        raise ValueError("snapshot total bytes differs")
    return {
        "snapshot": str(directory),
        "manifest_sha256": digest(manifest_raw),
        "files_verified": len(manifest["files"]),
        "bytes_verified": total,
        "status": "verified",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    plan_parser = commands.add_parser("plan")
    plan_parser.add_argument("--review", type=Path, action="append", required=True)
    plan_parser.add_argument("--optional-review", type=Path, action="append", default=[])
    plan_parser.add_argument("--output", type=Path, required=True)
    snapshot_parser = commands.add_parser("snapshot")
    snapshot_parser.add_argument("--plan", type=Path, required=True)
    snapshot_parser.add_argument("--output", type=Path, required=True)
    verify_parser = commands.add_parser("verify")
    verify_parser.add_argument("snapshot", type=Path)
    args = parser.parse_args()
    if args.command == "plan":
        output = private_output(args.output)
        reviews = [plan_review(path) for path in args.review]
        reviews += [plan_review(path, optional=True) for path in args.optional_review]
        names = [review["review_id"] for review in reviews]
        if len(set(names)) != len(names):
            raise ValueError("review namespace collision")
        ready = all(review["optional"] or review["status"] == "ready" for review in reviews)
        total = sum(row.get("bytes", 0) for review in reviews for row in review["files"])
        if total > MAX_TOTAL:
            raise ValueError("planned inputs exceed bounded total limit")
        result = {
            "schema_version": 1,
            "created_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            "status": "ready" if ready else "blocked",
            "network_actions_performed": False,
            "remote_host": REMOTE_HOST,
            "remote_checkout": REMOTE_CHECKOUT,
            "transfer_contract": "Copy only verified snapshot beneath private .temp, preserving review-ID namespaces. Before transfer, refuse conflicting existing bytes. Canary exactly one missing nonempty file with the same rsync --ignore-existing --from0 --files-from path as the rest; verify remote SHA and bytes before remaining files. No delete, overwrite, source publication or ontology-directory copy.",
            "reviews": reviews,
        }
        output.parent.mkdir(parents=True, exist_ok=True)
        with output.open("x") as stream:
            json.dump(result, stream, indent=2)
            stream.write("\n")
        print(json.dumps({"plan": str(output), "status": result["status"], "reviews": names}))
        return int(not ready)
    if args.command == "snapshot":
        print(json.dumps(snapshot(json.loads(args.plan.read_bytes()), args.output)))
    else:
        print(json.dumps(verify(args.snapshot)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
