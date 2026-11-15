#!/usr/bin/env python3
"""Inventory all local prior 000087 review findings, including ignored files.

Inputs: structured reviews and the frozen canonical target. Output: ignored
context receipt for the scientific reassessment serving #1548, 2026-11-14.
This filesystem walk does not apply Git ignore rules and mutates no old input.
"""

import hashlib
import json
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
STATE = ROOT / ".temp/m5-completion-20261114"
TARGET = "CommunityMech:000087"


def main():
    rows = []
    for path in sorted((ROOT / "reviews/structured").rglob("review.yaml")):
        raw = path.read_text()
        if TARGET not in raw:
            continue
        content = yaml.load(raw, Loader=yaml.CSafeLoader)
        if TARGET not in {r["target_id"] for r in content.get("targets", [])}:
            continue
        findings = [
            finding
            for finding in content.get("findings", [])
            if TARGET in finding.get("target_ids", [])
        ]
        assessments = [
            assessment
            for assessment in content.get("assessments", [])
            if assessment.get("target_ids") == [TARGET]
        ]
        rows.append(
            {
                "path": str(path.relative_to(ROOT)),
                "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
                "review_id": content["review_id"],
                "scientific_review": content["scientific_review"],
                "kind": content["kind"],
                "findings": findings,
                "assessments": assessments,
            }
        )
    output = {
        "search_scope": "All reviews/structured/**/review.yaml via Path.rglob; includes hidden/ignored directories",
        "target_id": TARGET,
        "review_count": len(rows),
        "reviews": rows,
    }
    path = STATE / "lbnl-prior-context.json"
    path.write_text(json.dumps(output, indent=2) + "\n")
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
