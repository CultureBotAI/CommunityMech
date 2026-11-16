#!/usr/bin/env python3
"""Read immutable Git corpora for PR2927 CI triage, 2026-11-16.

Inputs: exact CI/integration revisions and their tracked YAML/code bytes.
Output: exclusive JSON inventory; no tests, native grounding, or canonical writes.
This records observations, not scientific adjudication or a passing CI result.
"""

import argparse
import ast
import hashlib
import io
import json
import re
import subprocess
import tarfile
from collections import Counter, defaultdict
from pathlib import Path

import yaml

CI = "f3ecf5dba91f50c7b3c30daa4953c9cc7425f762"
CI_CHECKOUT = "de9b5a7c705ab5c9ce722df211f5bced96b2a94d"
INTEGRATION = "fb9be6d99daffd8ecf9c2cb7443d5b0022128d9e"
ROOTS = ("kb/communities", "data/isolates", "kb/taxa")
TESTS = (
    "test_gtdb_grounding_freshness.py",
    "test_gtdb_lineage_tree.py",
    "test_gtdb_near_tie_marker.py",
    "test_gtdb_support_counts.py",
    "test_is_reclassified_semantics.py",
    "test_label_drift_report_is_ignored.py",
    "test_phage_review_regressions.py",
    "test_stage6_infrastructure.py",
    "test_transwell_participants.py",
)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def git(root, *args):
    return subprocess.check_output(["git", *args], cwd=root)


def classify_function(raw):
    """Use only the exact maintained pure classifier definitions, not test calls."""
    names = {"_POLYPHYLY", "_PLACEHOLDER", "_normalise", "classify"}
    selected = []
    for node in ast.parse(raw).body:
        if isinstance(node, ast.FunctionDef) and node.name in names:
            selected.append(node)
        if isinstance(node, ast.Assign) and any(
            isinstance(target, ast.Name) and target.id in names for target in node.targets
        ):
            selected.append(node)
    assert len(selected) == 4
    namespace = {"re": re}
    exec(  # noqa: S102 - exact captured pure classifier AST; no imports or test calls.
        compile(ast.Module(body=selected, type_ignores=[]), "captured_classifier", "exec"),
        namespace,
    )
    return namespace["classify"]


def walk(node, path=""):
    if isinstance(node, dict):
        if isinstance(node.get("gtdb_classification"), dict):
            yield path, node
        for key, value in node.items():
            yield from walk(value, f"{path}.{key}" if path else key)
    elif isinstance(node, list):
        for index, value in enumerate(node):
            yield from walk(value, f"{path}[{index}]")


def snapshot(root, revision):
    raw = git(root, "archive", revision, *ROOTS)
    files = {}
    with tarfile.open(fileobj=io.BytesIO(raw)) as archive:
        for member in archive:
            path = Path(member.name)
            if member.isfile() and path.parent.as_posix() in ROOTS and path.suffix == ".yaml":
                files[member.name] = archive.extractfile(member).read()
    classifier_raw = git(root, "show", f"{revision}:tests/test_is_reclassified_semantics.py")
    classify = classify_function(classifier_raw)
    grounded, near, stale, special = [], [], [], []
    status_counts, classification_counts = Counter(), Counter()
    parents = defaultdict(lambda: defaultdict(list))
    for name, data in sorted(files.items()):
        document = yaml.safe_load(data)
        for entry in document.get("taxonomy") or []:
            status_counts[(entry.get("taxon_term") or {}).get("gtdb_grounding_status")] += 1
        for path, descriptor in walk(document):
            block = descriptor["gtdb_classification"]
            row = {
                "record": name,
                "record_sha256": sha(data),
                "path": path,
                "term": descriptor.get("term"),
                "preferred_term": descriptor.get("preferred_term"),
                "block": block,
            }
            grounded.append(row)
            if block.get("ncbi_source_id") != (descriptor.get("term") or {}).get("id"):
                stale.append(row)
            fraction = block.get("majority_fraction")
            if isinstance(fraction, (int, float)) and 0 < fraction < 0.55:
                near.append(row)
            if block.get("is_reclassified") is True:
                classification_counts[
                    classify(
                        (descriptor.get("term") or {}).get("label") or "",
                        block.get("gtdb_taxon") or "",
                    )
                ] += 1
            if block.get("ncbi_source_id") == "NCBITaxon:239935":
                special.append(row)
            lineage = block.get("gtdb_lineage")
            if isinstance(lineage, str):
                tokens = lineage.split(";")
                for index, token in enumerate(tokens):
                    parents[token][";".join(tokens[:index])].append({"record": name, "path": path})
    conflicts = {key: dict(value) for key, value in parents.items() if len(value) > 1}
    phages = {}
    for name, raw_record in files.items():
        if "Phage" in name and ("Alseth" in name or "PHA" in name):
            doc = yaml.safe_load(raw_record)
            phages[name] = {
                "record_sha256": sha(raw_record),
                "members": [
                    {
                        "term": r["taxon_term"]["term"],
                        "status": r["taxon_term"].get("gtdb_grounding_status"),
                    }
                    for r in doc["taxonomy"]
                ],
            }
    total = sum(classification_counts.values())
    not_different = total - classification_counts["different_name"]
    return {
        "revision": revision,
        "archive_sha256": sha(raw),
        "record_files": len(files),
        "record_sha256": {name: sha(data) for name, data in sorted(files.items())},
        "test_sha256": {name: sha(git(root, "show", f"{revision}:tests/{name}")) for name in TESTS},
        "classifier_sha256": sha(classifier_raw),
        "grounded_blocks": len(grounded),
        "taxonomy_status_counts": {str(k): v for k, v in status_counts.items()},
        "source_id_mismatches": stale,
        "near_tie_blocks": near,
        "reclassified_buckets": dict(classification_counts),
        "true_blocks": total,
        "not_different_name_blocks": not_different,
        "not_different_name_fraction": not_different / total,
        "lineage_conflicts": conflicts,
        "akkermansia_blocks": special,
        "phage_records": phages,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    ci = snapshot(args.repo, CI)
    checkout = snapshot(args.repo, CI_CHECKOUT)
    current = snapshot(args.repo, INTEGRATION)
    result = {
        "scope": "read-only immutable Git observations; no CI rerun or scientific adjudication",
        "helper_sha256": sha(Path(__file__).read_bytes()),
        "ci": ci,
        "ci_checkout": checkout,
        "integration": current,
        "failing_test_files_identical": (
            ci["test_sha256"] == checkout["test_sha256"] == current["test_sha256"]
        ),
        "tracked_ignored_reports_at_worktree_head": git(
            args.repo,
            "-c",
            "core.excludesFile=/dev/null",
            "ls-files",
            "--cached",
            "--ignored",
            "--exclude-per-directory=.gitignore",
            "--",
            "reports/",
        )
        .decode()
        .splitlines(),
        "observed_worktree_head": git(args.repo, "rev-parse", "HEAD").decode().strip(),
    }
    with args.output.open("x") as handle:
        json.dump(result, handle, indent=2, sort_keys=True)
        handle.write("\n")
    print(json.dumps({"output": str(args.output), "sha256": sha(args.output.read_bytes())}))


if __name__ == "__main__":
    main()
