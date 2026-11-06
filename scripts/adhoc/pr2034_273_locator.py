"""Prepare an immutable PR2034/273 history-selector correction.

The existing scientific assessment and actual check receipts are preserved.
Only finding locators, explicit comparison context, and successor provenance
are updated. Native validation/save and immediate review gates run separately.
"""

from __future__ import annotations

import copy
import hashlib
import json
import subprocess
from datetime import datetime, timezone

import yaml
from pr2034_273_audit import ENV, ROOT, SCRATCH, TARGET, run, write

PRIOR_ID = "20261105T202342Z-pr2034-chromobacterium-helper-reconciliation"
PRIOR = f"reviews/structured/{PRIOR_ID}/review.yaml"
SELF = "scripts/adhoc/pr2034_273_locator.py"
EVENT = "history/records/Chromobacterium_Gold_Biocyanidation/" "2026-10-21T190000Z-claude-2050.yaml"
SELECTORS = [f"{EVENT}::events[0].summary", f"{EVENT}::events[0].details"]


class Dumper(yaml.SafeDumper):
    def ignore_aliases(self, data):
        return True


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def git(*args):
    return subprocess.check_output(["git", *args], cwd=ROOT, env=ENV, text=True).strip()


def prepare():
    started = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
    prior_raw = (ROOT / PRIOR).read_bytes()
    prior = yaml.safe_load(prior_raw)
    unchanged = []
    for row in prior["source"]["inputs"]:
        assert digest((ROOT / row["path"]).read_bytes()) == row["sha256"], row["path"]
        unchanged.append(row)
    target = yaml.safe_load((ROOT / TARGET).read_text())
    event = yaml.safe_load((ROOT / EVENT).read_text())["events"][0]
    assert "DSM 30191" in event["summary"] and "SYNTROPHIC_PARTNER" in event["summary"]
    assert "CommunityMech:000181" in event["details"]
    comparison = target["curation_history"][1]
    assert "waste-PCB study" in comparison["changes"]
    assert "DSM 30191" not in comparison["changes"]

    corpus = json.loads((SCRATCH / "network-corpus-inputs.json").read_text())
    current_paths = sorted(
        str(path.relative_to(ROOT))
        for directory in ["kb/communities", "data/isolates"]
        for path in (ROOT / directory).glob("*.yaml")
    )
    assert current_paths == sorted(row["path"] for row in corpus["inputs"])
    for row in corpus["inputs"]:
        assert digest((ROOT / row["path"]).read_bytes()) == row["sha256"], row["path"]
    revision = git("rev-parse", "HEAD")
    changed_paths = git(
        "diff", "--name-only", prior["source"]["git_revision"], revision
    ).splitlines()
    assert all(
        path.startswith(("reviews/structured/", "scripts/adhoc/pr2034_")) for path in changed_paths
    ), changed_paths
    for name, args in [
        ("locator-black-check", [".venv/bin/black", "--check", SELF]),
        ("locator-ruff-check", [".venv/bin/ruff", "check", SELF]),
    ]:
        result = run(name, args)
        assert result.returncode == 0, result.stderr.decode()

    args = [
        "uv",
        "run",
        "python",
        "scripts/record_review.py",
        "inspect",
        "--targets",
        str(SCRATCH / "targets.yaml"),
    ]
    inputs = {row["path"] for row in prior["source"]["inputs"] if row["role"] != "target"}
    inputs.update([PRIOR, SELF])
    for path in sorted(inputs):
        args.extend(["--input", path])
    result = run("inspect-locator-successor", args)
    assert result.returncode == 0, result.stderr.decode()
    inspection = json.loads(result.stdout)
    assert inspection["source"]["git_revision"] == revision
    write("inspection-locator-successor.json", inspection)

    doc = copy.deepcopy(prior)
    now = datetime.now(timezone.utc)
    stamp = now.isoformat().replace("+00:00", "Z")
    doc["review_id"] = now.strftime("%Y%m%dT%H%M%SZ") + "-pr2034-chromobacterium-history-locator"
    doc["started_at"], doc["finished_at"] = started, stamp
    doc["title"] = "Chromobacterium review: external history selectors corrected; science unchanged"
    doc["summary"] = "Administrative history-selector correction. " + prior["summary"]
    doc["source"] = inspection["source"]
    doc["notes"].append(
        "This successor corrects the history finding's field_paths to the external event's "
        "events[0].summary and events[0].details. The accurate embedded curation_history[1] "
        "is comparison context only, not a field requiring repair. All scientific conclusions, "
        "finding identities/statuses, actions, source evidence, and prior saved bytes are retained. "
        "All prior inputs and all 503 corpus records were rehashed unchanged. Since the prior "
        "check revision, Git changes affect only review bundles and PR2034 helper scripts; "
        "validator code and scientific data are unchanged. Actual prior focused/corpus checks "
        "are reused with their original execution times, commands, and outcomes, not rerun or "
        "relabeled as current executions. New helper lint, native inspect, and candidate gates "
        "are separate actual executions."
    )
    doc["related_reviews"].append(
        {
            "repository": doc["repository"],
            "review_id": PRIOR_ID,
            "relationship": "Immediate administrative successor correcting external history selectors; all six finding dispositions retained.",
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
        if finding["finding_id"] == "history":
            assert finding["field_paths"] == ["curation_history[1]"]
            finding["field_paths"] = SELECTORS
    history_assessment = next(x for x in doc["assessments"] if x["assessment_id"] == "history")
    history_assessment.setdefault("dimensions", []).append(
        {
            "name": "embedded-history-comparison-only",
            "value": comparison["changes"],
            "definition": f"{TARGET}::curation_history[1].changes is accurate comparison context only. The defect belongs to {EVENT}::events[0].summary and events[0].details; preserve the embedded entry.",
            "evidence_ids": ["current", "history-event", "delta"],
        }
    )
    proof = {
        "prior_path": PRIOR,
        "prior_sha256": digest(prior_raw),
        "prior_git_revision": prior["source"]["git_revision"],
        "current_git_revision": revision,
        "unchanged_prior_inputs": unchanged,
        "unchanged_corpus_count": len(corpus["inputs"]),
        "corpus_manifest_sha256": digest((SCRATCH / "network-corpus-inputs.json").read_bytes()),
        "intervening_changed_paths": changed_paths,
        "old_finding_selectors": ["curation_history[1]"],
        "corrected_selectors": SELECTORS,
        "external_event_values": {key: event[key] for key in ["summary", "details"]},
        "comparison_only": {"selector": f"{TARGET}::curation_history[1]", "value": comparison},
        "reused_check_ids": [x["check_id"] for x in prior["checks"]],
        "all_six_findings_link_immediate_predecessor": True,
        "scientific_conclusions_and_dispositions_unchanged": True,
    }
    write("history-locator-proof.json", proof)
    doc["evidence"].append(
        {
            "evidence_id": "history-locator-reconciliation",
            "kind": "validation",
            "reference": SELF,
            "locator": "history-locator-proof.json; exact external event and embedded comparison selectors, unchanged input/corpus hashes, and preserved finding lineage",
            "summary": "The erroneous event's two external fields are now selected for append-only correction. Embedded curation_history[1] remains comparison context. All scientific inputs and finding dispositions are unchanged.",
            "support": "supports",
            "accessed_at": stamp,
            "snapshot_sha256": digest((SCRATCH / "history-locator-proof.json").read_bytes()),
        }
    )
    for key in ["locator-black-check", "locator-ruff-check"]:
        receipt = json.loads((SCRATCH / f"{key}.json").read_text())
        doc["checks"].append(
            {
                "check_id": key,
                "name": key,
                "status": "passed",
                "required": True,
                "summary": "The new locator-correction helper passes the repository formatting/lint gate.",
                "target_ids": ["CommunityMech:000273"],
                "command": receipt["command"],
                "exit_code": 0,
                "expected_exit_code": 0,
                "evidence_ids": [key],
                "scope_note": "Only scripts/adhoc/pr2034_273_locator.py; no record or history mutation.",
            }
        )
        doc["evidence"].append(
            {
                "evidence_id": key,
                "kind": "validation",
                "reference": receipt["command"],
                "locator": f"Executed {receipt['started_at']} through {receipt['finished_at']}; stdout SHA256 {receipt['stdout_sha256']}; stderr SHA256 {receipt['stderr_sha256']}",
                "summary": "Exit 0.",
                "support": "context_only",
                "accessed_at": stamp,
                "snapshot_sha256": digest((SCRATCH / f"{key}.json").read_bytes()),
            }
        )
    assert doc["actions"] == prior["actions"]
    assert doc["checks"][: len(prior["checks"])] == prior["checks"]
    assert doc["evidence"][: len(prior["evidence"])] == prior["evidence"]
    for original, successor in zip(prior["findings"], doc["findings"], strict=True):
        compared = copy.deepcopy(successor)
        compared["previous_occurrences"] = compared["previous_occurrences"][:-1]
        if compared["finding_id"] == "history":
            compared["field_paths"] = original["field_paths"]
        assert compared == original
    path = SCRATCH / "candidate-locator-successor.yaml"
    with path.open("x") as stream:
        yaml.dump(doc, stream, Dumper=Dumper, sort_keys=False, allow_unicode=True, width=100)
    print(
        json.dumps(
            {"review_id": doc["review_id"], "path": str(path), "sha256": digest(path.read_bytes())}
        )
    )


if __name__ == "__main__":
    prepare()
