"""Append a provenance successor after formatting PR2034/273 helpers.

Keeps the first saved pair immutable. Reuses the same scientific assessment and
actual focused checks only after all non-helper input hashes are reverified.
This command prepares a candidate; native validation and serialized save follow.
"""

from __future__ import annotations

import argparse
import ast
import copy
import hashlib
import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path

import yaml
from pr2034_273_audit import ENV, run

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / ".temp/pr2034/273"
PRIOR_ID = "20261105T202038Z-pr2034-chromobacterium-gold-successor"
PRIOR = f"reviews/structured/{PRIOR_ID}/review.yaml"
HELPERS = [f"scripts/adhoc/pr2034_273_{name}.py" for name in ["audit", "sources", "build_review"]]


class Dumper(yaml.SafeDumper):
    def ignore_aliases(self, data):
        return True


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def normalized_ast(raw):
    """Disregard import ordering, but retain every imported name and code node."""
    tree = ast.parse(raw)
    imports = sorted(
        ast.dump(node) for node in tree.body if isinstance(node, (ast.Import, ast.ImportFrom))
    )
    tree.body = [node for node in tree.body if not isinstance(node, (ast.Import, ast.ImportFrom))]
    return {"imports": imports, "body": ast.dump(tree)}


def write(name, data):
    with (OUT / name).open("x") as stream:
        json.dump(data, stream, indent=2, ensure_ascii=False)
        stream.write("\n")


def capture():
    write(
        "helper-before-format.json",
        [
            {
                "path": p,
                "sha256": digest((ROOT / p).read_bytes()),
                "ast": normalized_ast((ROOT / p).read_text()),
            }
            for p in HELPERS
        ],
    )


def prepare():
    began = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
    prior = yaml.safe_load((ROOT / PRIOR).read_text())
    before = json.loads((OUT / "helper-before-format.json").read_text())
    helper_proof = []
    for row in before:
        raw = (ROOT / row["path"]).read_bytes()
        assert normalized_ast(raw.decode()) == row["ast"], row["path"]
        helper_proof.append(
            {
                "path": row["path"],
                "before_sha256": row["sha256"],
                "after_sha256": digest(raw),
                "ast_equal_except_import_order": True,
            }
        )
    unchanged = []
    for row in prior["source"]["inputs"]:
        if row["path"] not in HELPERS:
            assert digest((ROOT / row["path"]).read_bytes()) == row["sha256"], row["path"]
            unchanged.append(row)
    for name, command in [
        (
            "helper-black-check",
            [".venv/bin/black", "--check", *HELPERS, "scripts/adhoc/pr2034_273_reconcile.py"],
        ),
        (
            "helper-ruff-check",
            [".venv/bin/ruff", "check", *HELPERS, "scripts/adhoc/pr2034_273_reconcile.py"],
        ),
    ]:
        result = run(name, command)
        assert result.returncode == 0, result.stderr.decode()
    arguments = [
        "uv",
        "run",
        "python",
        "scripts/record_review.py",
        "inspect",
        "--targets",
        str(OUT / "targets.yaml"),
    ]
    inputs = {row["path"] for row in prior["source"]["inputs"] if row["role"] != "target"}
    inputs.update([PRIOR, "scripts/adhoc/pr2034_273_reconcile.py"])
    for path in sorted(inputs):
        arguments.extend(["--input", path])
    result = run("inspect-helper-successor", arguments)
    assert result.returncode == 0
    inspection = json.loads(result.stdout)
    assert inspection["source"]["git_revision"] == prior["source"]["git_revision"]
    write("inspection-helper-successor.json", inspection)
    doc = copy.deepcopy(prior)
    now = datetime.now(timezone.utc)
    stamp = now.isoformat().replace("+00:00", "Z")
    doc["review_id"] = (
        now.strftime("%Y%m%dT%H%M%SZ") + "-pr2034-chromobacterium-helper-reconciliation"
    )
    doc["started_at"], doc["finished_at"] = began, stamp
    doc["title"] = "Chromobacterium review: helper provenance reconciliation; science unchanged"
    doc["source"] = inspection["source"]
    doc["summary"] = "Helper-only provenance successor. " + prior["summary"]
    doc["notes"].append(
        "This observation changes helper formatting/import ordering and captures their final "
        "hashes. Every non-helper input, scientific assessment, finding disposition and source "
        "limitation was rechecked against the immediately previous saved review and retained. "
        "The prior review pair remains immutable. Its actual focused/corpus checks are reused "
        "at unchanged Git revision and scientific input bytes; they were not rerun or relabeled "
        "as new executions. Helper Black/Ruff checks ran for this successor."
    )
    doc["related_reviews"].append(
        {
            "repository": doc["repository"],
            "review_id": PRIOR_ID,
            "relationship": "Immediate successor for helper-input provenance "
            "only; all six finding identities and dispositions retained.",
        }
    )
    for finding in doc["findings"]:
        finding.setdefault("previous_occurrences", []).append(
            {
                "repository": doc["repository"],
                "review_id": PRIOR_ID,
                "finding_id": finding["finding_id"],
            }
        )
    proof = {
        "prior_path": PRIOR,
        "prior_sha256": digest((ROOT / PRIOR).read_bytes()),
        "helpers": helper_proof,
        "unchanged_nonhelper_inputs": unchanged,
        "reused_checks": [x["check_id"] for x in prior["checks"]],
        "finding_dispositions_unchanged": True,
        "scientific_assessments_unchanged": True,
    }
    write("helper-reconciliation-proof.json", proof)
    doc["evidence"].append(
        {
            "evidence_id": "helper-reconciliation",
            "kind": "validation",
            "reference": "scripts/adhoc/pr2034_273_reconcile.py",
            "locator": "helper-reconciliation-proof.json; AST comparison "
            "disregards only top-level import ordering; all other inputs rehashed",
            "summary": "All scientific input bytes and old finding dispositions "
            "are unchanged. Only three helper files were formatted/reordered.",
            "support": "supports",
            "accessed_at": stamp,
            "snapshot_sha256": digest((OUT / "helper-reconciliation-proof.json").read_bytes()),
        }
    )
    for key in ["helper-black-check", "helper-ruff-check"]:
        receipt = json.loads((OUT / f"{key}.json").read_text())
        doc["checks"].append(
            {
                "check_id": key,
                "name": key,
                "status": "passed",
                "required": True,
                "summary": "Final helper code passes the " "repository's formatting/lint gate.",
                "target_ids": ["CommunityMech:000273"],
                "command": receipt["command"],
                "exit_code": 0,
                "expected_exit_code": 0,
                "evidence_ids": [key],
                "scope_note": "Four PR2034/273 helper scripts; no record mutation.",
            }
        )
        doc["evidence"].append(
            {
                "evidence_id": key,
                "kind": "validation",
                "reference": receipt["command"],
                "locator": f"Executed "
                f"{receipt['started_at']} through {receipt['finished_at']}; "
                f"stdout SHA256 {receipt['stdout_sha256']}; stderr SHA256 "
                f"{receipt['stderr_sha256']}",
                "summary": "Exit 0.",
                "support": "context_only",
                "accessed_at": stamp,
                "snapshot_sha256": digest((OUT / f"{key}.json").read_bytes()),
            }
        )
    doc["assessments"].append(
        {
            "assessment_id": "helper-provenance",
            "area": "provenance",
            "topic": "Formatting-only input reconciliation",
            "outcome": "supported",
            "summary": "No new source investigation or record curation. "
            "The author rechecked all scientific inputs and retained all "
            "prior assessments/dispositions, with exact immediate-predecessor "
            "references for every finding.",
            "target_ids": ["CommunityMech:000273"],
            "evidence_ids": ["helper-reconciliation", "helper-black-check", "helper-ruff-check"],
        }
    )
    path = OUT / "candidate-helper-successor.yaml"
    with path.open("x") as stream:
        yaml.dump(doc, stream, Dumper=Dumper, sort_keys=False, allow_unicode=True, width=100)
    print(
        json.dumps(
            {"review_id": doc["review_id"], "path": str(path), "sha256": digest(path.read_bytes())}
        )
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("step", choices=["capture", "prepare"])
    arguments = parser.parse_args()
    globals()[arguments.step]()
