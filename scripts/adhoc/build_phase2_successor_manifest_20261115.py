"""Bind completed Phase 2 scientific successors for #2816, 2026-11-15.

Inputs: exact clean Git revision, explicit native review YAML paths and preserved
baseline68699871. Output: one exclusive manifest of actual record/review/history
hashes. No old review, record or source changes; no scientific approval inferred.
All five affected records must have independently reviewed full assessments
before invoking this builder. The separate adversarial review is a human/agent
assessment; this script checks persistence and the native review contract only.
"""

import argparse
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "tests"))
from phase2_review_successor import (  # noqa: E402
    BASELINE,
    MANIFEST,
    TARGETS,
    current_record_sha256,
    digest,
    historical_bytes,
    validate_assessment,
)

from scripts.record_review import render_markdown, validate_review  # noqa: E402


def git(*args):
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()


def artifact(path):
    return {"path": str(path.relative_to(ROOT)), "sha256": digest(path.read_bytes())}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--expected-revision", required=True)
    parser.add_argument("--review", type=Path, action="append", required=True)
    parser.add_argument("--receipt", type=Path, action="append", required=True)
    args = parser.parse_args()
    if git("rev-parse", "HEAD") != args.expected_revision or git("diff", "--name-only", "HEAD"):
        parser.error("exact clean tracked revision required")
    output = ROOT / MANIFEST
    if output.exists():
        parser.error("successor manifest already exists; preserve it")
    reviews = {}
    for requested in args.review:
        path = requested.resolve()
        if not path.is_relative_to(ROOT / "reviews/structured") or path.name != "review.yaml":
            parser.error("explicit native saved review.yaml required")
        raw = path.read_bytes()
        review = yaml.safe_load(raw)
        validate_review(review)
        markdown = path.with_name("review.md")
        if markdown.read_text() != render_markdown(review):
            raise ValueError("saved Markdown differs from native renderer")
        for target in review["targets"]:
            relative = target["path"]
            if relative not in TARGETS:
                continue
            if relative in reviews:
                raise ValueError("multiple final assessments selected for one record")
            validate_assessment(review, relative, digest((ROOT / relative).read_bytes()))
            reviews[relative] = (artifact(path), artifact(markdown), review)
    if set(reviews) != set(TARGETS):
        raise ValueError("all five affected records require exact final full assessments")
    receipts = {path: [] for path in TARGETS}
    for requested in args.receipt:
        path = requested.resolve()
        if not path.is_relative_to(ROOT / "reports"):
            raise ValueError("published retained apply receipt required")
        receipt = yaml.safe_load(path.read_bytes())
        target = receipt.get("path", receipt.get("target"))
        if target not in receipts:
            raise ValueError("receipt outside the five-record scope")
        if not (receipt.get("applied") is True or receipt.get("applied_at")):
            raise ValueError("staged or unapplied receipt cannot prove curation")
        receipts[target].append((receipt, artifact(path)))
    changed = git("diff", "--name-only", BASELINE, "HEAD", "--", "history/records").splitlines()
    result = {
        "schema_version": 1,
        "issue": 2816,
        "created_at": datetime.now(timezone.utc).isoformat(),
        "source_baseline": BASELINE,
        "recorded_revision": args.expected_revision,
        "independent_approval": False,
        "scope": "Persistence/lineage proof only; full current scientific assessments retain their individual verdicts and unresolved findings.",
        "generator": artifact(Path(__file__).resolve()),
        "records": [],
    }
    for relative, identifier in TARGETS.items():
        sidecars = []
        directory = Path("history/records") / Path(relative).stem
        for name in changed:
            if Path(name).parent != directory:
                continue
            # Existing historical sidecars may never be rewritten into successors.
            old = subprocess.run(
                ["git", "cat-file", "-e", f"{BASELINE}:{name}"],
                cwd=ROOT,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )
            if old.returncode == 0:
                raise ValueError("historical sidecar changed: " + name)
            sidecars.append(artifact(ROOT / name))
        review, markdown, assessment = reviews[relative]
        previous_hash = digest(historical_bytes(ROOT, relative))
        remaining = list(receipts[relative])
        ordered_receipts = []
        while remaining:
            next_steps = [item for item in remaining if item[0]["before_sha256"] == previous_hash]
            if len(next_steps) != 1:
                raise ValueError("ambiguous or disconnected actual curation chain")
            receipt, retained_artifact = next_steps[0]
            raw_inputs = [
                item
                for item in assessment["source"]["inputs"]
                if item["sha256"] == retained_artifact["sha256"]
                and item["path"].startswith(".temp/")
            ]
            if len(raw_inputs) != 1:
                raise ValueError(
                    "exact applied receipt must be a unique inspected raw review input"
                )
            retained_artifact = {
                **retained_artifact,
                "raw_path": raw_inputs[0]["path"],
                "raw_sha256": raw_inputs[0]["sha256"],
            }
            ordered_receipts.append(retained_artifact)
            remaining.remove(next_steps[0])
            previous_hash = receipt["after_sha256"]
        result["records"].append(
            {
                "id": identifier,
                "path": relative,
                "before_sha256": digest(historical_bytes(ROOT, relative)),
                "after_sha256": digest((ROOT / relative).read_bytes()),
                "scientific_review": review,
                "review_markdown": markdown,
                "history_sidecars": sidecars,
                "curation_receipts": ordered_receipts,
            }
        )
    for row in result["records"]:
        current_record_sha256(ROOT, row["path"], row["before_sha256"], manifest=result)
    if git("rev-parse", "HEAD") != args.expected_revision or git("diff", "--name-only", "HEAD"):
        raise ValueError("tracked inputs changed during manifest construction")
    # Final direct hashes bind every persisted artifact after all native checks.
    for row in result["records"]:
        if digest((ROOT / row["path"]).read_bytes()) != row["after_sha256"]:
            raise ValueError("record changed during manifest construction")
        for item in [
            row["scientific_review"],
            row["review_markdown"],
            *row["history_sidecars"],
            *row["curation_receipts"],
        ]:
            if digest((ROOT / item["path"]).read_bytes()) != item["sha256"]:
                raise ValueError("review/history changed during manifest construction")
    with output.open("x") as stream:
        yaml.safe_dump(result, stream, sort_keys=False, allow_unicode=True)
    persisted = yaml.safe_load(output.read_bytes())
    if persisted != result:
        raise ValueError("persisted lineage manifest differs")
    print(
        json.dumps(
            {
                "path": MANIFEST,
                "records": len(result["records"]),
                "sha256": digest(output.read_bytes()),
            }
        )
    )


if __name__ == "__main__":
    main()
