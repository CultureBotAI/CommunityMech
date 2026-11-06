"""Bounded JSON-only correction of an optional-slot instruction in PR2043."""

import argparse
import hashlib
import json
import os
import subprocess
from datetime import datetime, timezone
from pathlib import Path

import yaml
from linkml_runtime.utils.schemaview import SchemaView

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / ".temp/pr2043/009-correction"
OLD_ID = "20261021T120426Z-kefir-community-model-record"
OLD = "reviews/structured/" + OLD_ID + "/review.yaml"
TARGET = "kb/communities/BioModels_MODEL2204300001_Kefir_Community_Model.yaml"
ID = "CommunityMech:000009"
PYTHON = (
    "/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/"
    ".temp/pr-2034-canary/.venv/bin/python"
)
SCHEMA = "src/communitymech/schema/communitymech.yaml"
INPUTS = [
    TARGET,
    OLD,
    SCHEMA,
    "src/communitymech/schema/mech_shared.yaml",
    "AGENTS.md",
    ".claude/skills/review-yaml-record/SKILL.md",
    "docs/record-reviews.md",
    "docs/record-review-profile.md",
    "conf/record_review.yaml",
    "schema/record_review.yaml",
    "scripts/record_review.py",
    "scripts/adhoc/pr2043_009_correction.py",
]


def now():
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def write(name, value):
    (OUT / name).write_text(json.dumps(value, indent=2) + "\n")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("mode", choices=["inspect", "author"])
    mode = parser.parse_args().mode
    OUT.mkdir(parents=True, exist_ok=True)
    old = yaml.safe_load((ROOT / OLD).read_text())
    if mode == "inspect":
        write("started.json", {"started_at": now()})
        write("targets.json", {"targets": old["targets"]})
        command = [
            PYTHON,
            "scripts/record_review.py",
            "inspect",
            "--targets",
            str(OUT / "targets.json"),
        ]
        for path in INPUTS:
            command += ["--input", path]
        result = subprocess.run(
            command,
            cwd=ROOT,
            env={**os.environ, "PYTHONPATH": "src"},
            capture_output=True,
            text=True,
        )
        (OUT / "inspect.json").write_text(result.stdout)
        (OUT / "inspect.stderr").write_text(result.stderr)
        print(result.returncode, result.stderr)
        return
    inspection = json.loads((OUT / "inspect.json").read_text())
    slot = SchemaView(str(ROOT / SCHEMA)).induced_slot("ecological_state", "MicrobialCommunity")
    required = bool(slot.required)
    assert not required
    keys = [finding["issue_key"] for finding in old["findings"]]
    assert len(keys) == 5 and all(finding["status"] == "open" for finding in old["findings"])
    action = next(a for a in old["actions"] if a["action_id"] == "repair-model-community-scope")
    assert "required ecological state" in action["acceptance_checks"][1]
    write(
        "schema-receipt.json",
        {"required": required, "original_keys": keys, "original_action": action},
    )
    timestamp = now()
    evidence = []
    for eid, path, locator, summary in [
        (
            "schema",
            SCHEMA,
            "MicrobialCommunity.ecological_state and native SchemaView.induced_slot",
            "The induced slot has no required constraint; ecological_state is optional.",
        ),
        (
            "prior-action",
            OLD,
            "actions[repair-model-community-scope].acceptance_checks[1]; all five open findings",
            "The original action wrongly calls ecological_state required. This correction changes that premise only; all five scientific findings remain unresolved.",
        ),
        (
            "current-record",
            TARGET,
            "Entire current record; identity, state and qualified graph read without source reassessment",
            "The target is resolved and unchanged. No record field, graph qualifier or prior scientific finding is altered.",
        ),
    ]:
        evidence.append(
            {
                "evidence_id": eid,
                "kind": "authority" if eid == "schema" else "record_content",
                "reference": path,
                "locator": locator,
                "summary": summary,
                "support": "supports",
                "accessed_at": timestamp,
                "snapshot_sha256": hashlib.sha256((ROOT / path).read_bytes()).hexdigest(),
            }
        )
    corrected = (
        "For the natural community, replace unsupported engineered origin/design with source-backed "
        "provenance; assess ecological state independently. ecological_state is optional: omit it if "
        "no value is supported, rather than inventing a replacement. Do not automatically substitute "
        "ENGINEERED, TRANSIENT or STABLE, and do not equate laboratory propagation or model "
        "construction with ecological state or engineering."
    )
    record = {
        "schema_version": "1.0.0",
        "review_id": datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
        + "-pr2043-kefir-state-action-correction",
        "kind": "record",
        "repository": "CultureBotAI/CommunityMech",
        "title": "Kefir review action correction: ecological state is optional",
        "started_at": json.loads((OUT / "started.json").read_text())["started_at"],
        "finished_at": timestamp,
        "reviewer": {
            "identity": "codex",
            "kind": "agent",
            "independence": "self_review",
            "independence_basis": "Author of this bounded process correction; no independent scientific approval claimed.",
        },
        "skill": "review-yaml-record",
        "completion": "completed",
        "verdict": "needs_curation",
        "scientific_review": False,
        "summary": "Correct only the original action's required-state premise. The current schema permits omission of unsupported ecological_state. All five original scientific findings remain open, the qualified graph is preserved, and the natural-community follow-up on issue1262 remains unresolved.",
        "source": inspection["source"],
        "targets": inspection["targets"],
        "scope": {
            "description": "Bounded schema/process correction of original actions[repair-model-community-scope].acceptance_checks[1]; not a whole scientific re-review.",
            "selection": "Exactly CommunityMech:000009; all other targets excluded.",
            "coverage": "partial",
            "population_size": 1,
            "reviewed_target_ids": [ID],
        },
        "checks": [
            {
                "check_id": "slot-optionality",
                "name": "Native induced-slot optionality",
                "status": "passed",
                "required": True,
                "summary": "SchemaView.induced_slot('ecological_state','MicrobialCommunity').required is false or unset.",
                "target_ids": [ID],
                "evidence_ids": ["schema"],
            },
            {
                "check_id": "lineage-preservation",
                "name": "Bounded prior finding inventory",
                "status": "passed",
                "required": True,
                "summary": "Five original keys remain open; no terminal disposition or full-review supersession is emitted.",
                "target_ids": [ID],
                "evidence_ids": ["prior-action"],
            },
            {
                "check_id": "full-science",
                "name": "Full scientific reassessment",
                "status": "skipped",
                "required": False,
                "summary": "Outside this explicitly process-only correction; no literature, model payload or native full-record QC rerun claimed.",
                "target_ids": [ID],
                "evidence_ids": ["prior-action", "current-record"],
            },
        ],
        "evidence": evidence,
        "assessments": [
            {
                "assessment_id": "corrected-action",
                "area": "schema",
                "topic": "Optional ecological_state in the curation action",
                "outcome": "supported",
                "summary": "The source schema supports omission when ecological state is unsupported.",
                "target_ids": [ID],
                "evidence_ids": ["schema", "prior-action"],
                "details": "Replace only the required-state premise in "
                + OLD_ID
                + "/actions[repair-model-community-scope].acceptance_checks[1] with: "
                + corrected,
            },
            {
                "assessment_id": "unresolved-science",
                "area": "provenance",
                "topic": "Preserved scientific findings and access limits",
                "outcome": "unknown",
                "summary": "No prior scientific finding is resolved, superseded or reopened by this correction.",
                "target_ids": [ID],
                "evidence_ids": ["prior-action", "current-record"],
                "details": "The following five original keys remain unresolved: "
                + ", ".join(keys)
                + ". Preserve the qualified graph, original source-access limits, and all other action acceptance checks. Issue1262 continues to track model/community scope; this observation provides no new source certification.",
            },
        ],
        "findings": [],
        "actions": [
            {
                "action_id": "apply-corrected-state-acceptance",
                "description": "Use the corrected optional-state rule when later curating the still-open model-community-scope finding.",
                "finding_ids": [],
                "target_ids": [ID],
                "owner_paths": old["targets"][0]["owner_paths"],
                "acceptance_checks": [
                    corrected,
                    "Retain the other three original repair-model-community-scope acceptance checks and all five unresolved scientific finding lineages; do not treat this process correction as completed record curation.",
                ],
            }
        ],
        "limitations": [
            "Completion refers only to this schema/process correction; scientific_review is false. Full scientific source support and record-level QC were not reassessed.",
            "Empty new findings means no new unresolved finding in the narrow corrected-action scope. It does not close or retire any of the five original scientific findings.",
            "No kb record, history, cache, original bundle or generated product was edited; the original immutably retains its historical wording.",
        ],
        "related_reviews": [
            {
                "repository": "CultureBotAI/CommunityMech",
                "review_id": OLD_ID,
                "relationship": "Append-only correction of one acceptance-check premise only; no scientific supersession or terminal finding disposition.",
            }
        ],
        "notes": [
            "Schema receipt is .temp/pr2043/009-correction/schema-receipt.json; candidate JSON is saved only through the native validator/saver."
        ],
        "tags": ["record-review", "batch-07", "process-correction", "schema-optionality"],
    }
    write("candidate.json", record)
    print(record["review_id"])


if __name__ == "__main__":
    main()
