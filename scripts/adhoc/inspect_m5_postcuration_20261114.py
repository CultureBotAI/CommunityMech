#!/usr/bin/env python3
"""Capture native current-input inspection after frozen curation, 2026-11-14.

Inputs: prepared acceptance map, three records, cited sources, new receipts and
history. Output: initial native inspection for the later immutable delta review.
No canonical edits; the coordinator confirms writes complete before invocation.
"""

import json
import subprocess
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
STATE = ROOT / ".temp/m5-completion-20261114"


def main():
    destination = STATE / "postcuration-initial-inspection.json"
    if destination.exists():
        raise ValueError("Preserve initial inspection; reassess any subsequently changed inputs")
    acceptance = STATE / "postcuration-acceptance-map.json"
    mapping = json.loads(acceptance.read_text())
    target_file = STATE / "postcuration-targets.yaml"
    target_file.write_text(yaml.safe_dump({"targets": mapping["targets"]}, sort_keys=False))
    inputs = {
        "src/communitymech/schema/communitymech.yaml",
        "docs/record-review-profile.md",
        "docs/record-reviews.md",
        "docs/HOST_SOIL_AND_RELATED_COMMUNITIES.md",
        "conf/record_review.yaml",
        ".claude/skills/review-yaml-record/SKILL.md",
        ".claude/skills/review-communities/reference/metrics-and-reports.md",
        ".claude/skills/review-communities/reference/validation-rules.md",
        ".claude/skills/curate-yaml-record/references/review-checklist.md",
        "references_cache/PMID_40920748.md",
        "references_cache/doi_10.1126_sciadv.adg7888.md",
        "references_cache/PMID_42660928.md",
        "justfile",
        "scripts/adhoc/apply_m5_completion_corrections_20261114.py",
    }
    inputs.update(source["path"] for source in mapping["prior_review_inputs"])
    inputs.add(str(acceptance.relative_to(ROOT)))
    for relative in (
        "ecofab-independent/ring-main-plos.xml",
        "ecofab-independent/ring-s2.xlsx",
        "ecofab-independent/ring-s2.txt",
        "ecofab-relations/PMC9765266.xml",
        "ecofab-relations/PMC13522444.xml",
        "yolo-sources/mapping-comparison.json",
        "yolo-sources/source-comparison.json",
        "yolo-sources/soil-data5.xlsx",
        "dopamine-syncom-sources/fig2.png",
        "dopamine-syncom-sources/fig3.png",
        "dopamine-syncom-sources/supplement.pdf",
    ):
        inputs.add(str((STATE / relative).relative_to(ROOT)))
    inputs.update(str(path.relative_to(ROOT)) for path in (STATE / "curation").glob("*.json"))
    inputs.update(
        str(path.relative_to(ROOT)) for path in (ROOT / "history").rglob("2026-11-14*.yaml")
    )
    command = [sys.executable, "scripts/record_review.py", "inspect", "--targets", str(target_file)]
    for filename in sorted(inputs):
        command.extend(["--input", filename])
    result = subprocess.run(command, cwd=ROOT, text=True, capture_output=True, check=True)
    destination.write_text(result.stdout)
    print(destination)


if __name__ == "__main__":
    main()
