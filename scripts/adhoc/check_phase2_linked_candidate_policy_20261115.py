"""Read-only staged-cohort check with integrated native policy, 2026-11-15.

Inputs: exact integration revision, full native corpus index, reviewed private
three-record candidates. Output: exclusive private JSON with every input hash.
Serves #2700/#2806. Calls the maintained check_record API with three index
overrides; this is a candidate policy diagnostic, not full strict validation.
No canonical/cache/environment/provider writes.
"""

import argparse
import hashlib
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
STATE = ROOT / ".temp/phase2-science-20261115"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def revision(path):
    return subprocess.check_output(["git", "-C", str(path), "rev-parse", "HEAD"], text=True).strip()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--implementation-root", type=Path, required=True)
    parser.add_argument("--expected-revision", required=True)
    parser.add_argument("--plan", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    implementation = args.implementation_root.resolve()
    output, plan = args.output.resolve(), args.plan.resolve()
    if output.exists() or not output.is_relative_to(STATE) or not plan.is_relative_to(STATE):
        raise ValueError("exclusive private paths required")
    if revision(implementation) != args.expected_revision:
        raise ValueError("integrated revision changed")
    if subprocess.check_output(
        ["git", "-C", str(implementation), "status", "--porcelain"], text=True
    ).strip():
        raise ValueError("integrated checkout must be clean")
    sys.path.insert(0, str(implementation / "src"))
    from communitymech.validators import related_communities as native

    if (
        Path(native.__file__).resolve()
        != implementation / "src/communitymech/validators/related_communities.py"
    ):
        raise ValueError("wrong native implementation imported")
    files = list(native.record_files())
    source_files = [
        implementation / "src/communitymech/validators/related_communities.py",
        implementation / "src/communitymech/paths.py",
        implementation / "scripts/validate_strict.py",
        implementation / "src/communitymech/schema/communitymech.yaml",
    ]
    bound = {str(path.relative_to(implementation)): sha(path) for path in [*files, *source_files]}
    receipt_path = plan / "receipt.json"
    plan_hash = sha(receipt_path)
    receipt = json.loads(receipt_path.read_text())
    if set(receipt["targets"]) != {"ecofab", "dopamine", "lbnl"}:
        raise ValueError("unexpected reviewed candidate cohort")
    baseline, duplicates = native._corpus_index_and_duplicates()
    index = dict(baseline)
    candidates = {}
    for name, entry in receipt["targets"].items():
        path = plan / name / "candidate.yaml"
        if sha(path) != entry["after_sha256"]:
            raise ValueError("reviewed candidate changed")
        doc = yaml.safe_load(path.read_text())
        if doc["id"] != entry["id"]:
            raise ValueError("candidate identity differs")
        candidates[name] = (path, doc)
        index[doc["id"]] = (path, native.strain_roster(doc), native.record_links(doc))
    findings = {}
    for name, (_, doc) in candidates.items():
        findings[name] = [
            {"category": category, "message": message}
            for category, message in native.check_record(doc, index=index, duplicate_ids=duplicates)
        ]
    if revision(implementation) != args.expected_revision or any(
        sha(implementation / name) != expected for name, expected in bound.items()
    ):
        raise ValueError("native/corpus input changed during diagnostic")
    if sha(receipt_path) != plan_hash or any(
        sha(path) != receipt["targets"][name]["after_sha256"]
        for name, (path, _) in candidates.items()
    ):
        raise ValueError("candidate input changed during diagnostic")
    result = {
        "created_at": datetime.now(timezone.utc).isoformat(),
        "implementation_revision": args.expected_revision,
        "helper_sha256": sha(Path(__file__)),
        "plan_receipt_sha256": plan_hash,
        "native_index_records": len(baseline),
        "native_corpus_files": len(files),
        "native_duplicate_ids": {
            key: [str(path.relative_to(implementation)) for path in paths]
            for key, paths in duplicates.items()
        },
        "implementation_and_corpus_inputs": bound,
        "candidate_inputs": {
            name: {
                "id": entry["id"],
                "path": str(candidates[name][0].relative_to(ROOT)),
                "sha256": entry["after_sha256"],
            }
            for name, entry in receipt["targets"].items()
        },
        "findings": findings,
        "status": "PASSED" if not any(findings.values()) else "FAILED",
        "limitations": "Maintained related-community/host check only, using full corpus index with exactly three candidate overrides. Not full strict, reference, scientific or corpus QC approval.",
    }
    with output.open("x") as stream:
        stream.write(json.dumps(result, indent=2) + "\n")
    print(
        json.dumps(
            {
                key: result[key]
                for key in ("status", "native_index_records", "native_corpus_files", "findings")
            },
            indent=2,
        )
    )
    raise SystemExit(0 if result["status"] == "PASSED" else 1)


if __name__ == "__main__":
    main()
