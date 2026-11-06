"""Build a bounded, JSON-only successor for the PR2061 cultivation locator.

The immutable original review and canonical record are never written. Native
inspect/validate/save own input capture and publication of the review pair.
"""

import argparse
import copy
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

import yaml
from bs4 import BeautifulSoup

OUT = Path(".temp/pr2061/199-correction")
SCIENCE = Path(".temp/pr2061/independent-secondary")
OLD = Path("reviews/structured/20261022T044407Z-dehalococcoides-desulfovibrio-record-review")
SELF = Path("scripts/adhoc/pr2061_199_cultivation_locator.py")
TARGET = "CommunityMech:000199"


def now():
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def read(path):
    return json.loads(Path(path).read_text())


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def write(name, value):
    (OUT / name).write_text(json.dumps(value, indent=2) + "\n")


def prepare():
    OUT.mkdir(parents=True, exist_ok=True)
    old = yaml.safe_load((OLD / "review.yaml").read_text())
    manifest = read(SCIENCE / "current-science-input-manifest.json")
    paths = set()
    for item in manifest["inputs"]:
        assert digest(item["path"]) == item["sha256"], item["path"]
        paths.add(item["path"])
    paths.update(
        str(p)
        for p in [
            SELF,
            SCIENCE / "current-science-input-manifest.json",
            OUT / "started.json",
            OUT / "targets.json",
            OUT / "input-paths.json",
            OUT / "full-lint.json",
            OUT / "full-lint.stdout",
            OUT / "full-lint.stderr",
            Path("schema/record_review.yaml"),
            Path("scripts/record_review.py"),
            Path("scripts/adhoc/pr2043_009_correction.py"),
            Path("scripts/adhoc/pr2058_020_authority_observation.py"),
        ]
    )
    write("started.json", {"started_at": now()})
    write("targets.json", {"targets": old["targets"]})
    write(
        "input-paths.json",
        {
            "targets": [TARGET],
            "paths": sorted(paths),
            "scope": "The frozen four-record science context is included in full for byte provenance. "
            "Only the 199 cultivation finding is reassessed by this successor; other records and "
            "findings retain their prior heads. The final inspection and candidate are outputs.",
        },
    )
    print(json.dumps({"input_count": len(paths)}))


def build(inspection_path):
    old = yaml.safe_load((OLD / "review.yaml").read_text())
    inspection = read(inspection_path)
    assert set(read(OUT / "input-paths.json")["paths"]) == {
        i["path"] for i in inspection["source"]["inputs"]
    }
    for item in inspection["source"]["inputs"]:
        assert digest(item["path"]) == item["sha256"], item["path"]
    html = SCIENCE / "sources/21881617-main.html"
    article = BeautifulSoup(html.read_text(), "html.parser")
    discussion = article.find(id="sec26")
    paragraphs = [p.get_text(" ", strip=True) for p in discussion.find_all("p", recursive=False)]
    assert "unshaken" not in paragraphs[1]
    assert "unshaken conditions" in paragraphs[4]
    finding = copy.deepcopy(next(f for f in old["findings"] if f["finding_id"] == "cultivation"))
    assert finding["issue_key"] == "cm-000199-cultivation" and finding["status"] == "open"
    finding["previous_occurrences"] = [
        {
            "repository": old["repository"],
            "review_id": old["review_id"],
            "finding_id": "cultivation",
        }
    ]
    finding["evidence_ids"] = ["current-record", "culture-2012", "culture-2014", "culture-2017"]
    actions = copy.deepcopy(
        [a for a in old["actions"] if a["action_id"] in ["enrich-cultivation", "validate-curation"]]
    )
    original_phrase = "Discussion paragraph2 states unshaken conditions."
    corrected_phrase = (
        "Discussion section #sec26, fifth direct paragraph, states unshaken conditions "
        "(the paragraph beginning 'Another possible reason for more robust growth')."
    )
    assert original_phrase in actions[0]["acceptance_checks"][0]
    actions[0]["acceptance_checks"][0] = actions[0]["acceptance_checks"][0].replace(
        original_phrase, corrected_phrase
    )
    actions[1]["finding_ids"] = ["cultivation"]
    timestamp = now()
    evidence = []
    for eid, kind, path, locator, summary in [
        (
            "current-record",
            "record_content",
            Path(old["targets"][0]["path"]),
            "growth_media[0], cultivation_setup, discussions[0]; unchanged exact target bytes",
            "The source-specific cultivation omissions remain open; no canonical field is repaired.",
        ),
        (
            "prior-review",
            "prior_review",
            OLD / "review.yaml",
            "evidence[cultivation].locator and actions[enrich-cultivation].acceptance_checks[0]",
            "The original paragraph-2 locator is wrong. All five scientific findings and their "
            "acceptance scopes remain unresolved; only cultivation receives a new open occurrence.",
        ),
        (
            "culture-2012",
            "primary_source",
            html,
            "PMID:21881617 / PMC3260503: culture Methods #sec3; Discussion #sec26 fifth direct "
            "paragraph, not second; complete scientific narrative and Table1 inspected",
            "The fifth paragraph explicitly describes unshaken conditions. Methods separately "
            "supports vessel, working volume, gas, amendments and transfer stages; 5 m typography "
            "is not silently normalized into a direct concentration quote.",
        ),
        (
            "culture-2014",
            "primary_source",
            SCIENCE / "sources/24463969-main.html",
            "PMID:24463969 / PMC3993147: #sec2-1 sole direct culture Methods paragraph",
            "Pair and triculture cultivation are source-specific; pure-PfR7 pH and bioassay "
            "conditions must not migrate into the pair.",
        ),
        (
            "culture-2017",
            "primary_source",
            SCIENCE / "sources/28159790-main.html",
            "PMID:28159790 / PMC5377507: culture Methods and donor-excess/donor-limited Results",
            "Maintenance, acceptor-limited pair and donor-limited triculture remain separate; "
            "the original ancillary-mechanism and threshold limitations are preserved.",
        ),
        (
            "focused-qc",
            "validation",
            SCIENCE / "000199-focused-checks.json",
            "Seven actual focused commands, with concrete stdout/stderr inputs also frozen",
            "All seven focused schema/strict/terms/references/GTDB/domain/history checks exited0. "
            "Their deterministic success is distinct from this source-based locator correction.",
        ),
        (
            "science-context",
            "validation",
            SCIENCE / "independent-science-four-records.json",
            "Earlier independent read-only pass, frozen before switching to author role",
            "Records the locator defect and bounded scientific source scope. This author does "
            "not claim independent approval of the new successor.",
        ),
    ]:
        evidence.append(
            {
                "evidence_id": eid,
                "kind": kind,
                "reference": str(path),
                "locator": locator,
                "summary": summary,
                "support": "supports",
                "accessed_at": timestamp,
                "snapshot_sha256": digest(path),
            }
        )
    checks = []
    for i, receipt in enumerate(read(SCIENCE / "000199-focused-checks.json")):
        assert receipt["exit_code"] == 0
        checks.append(
            {
                "check_id": f"focused-{i + 1}",
                "name": receipt["argv"][2],
                "status": "passed",
                "required": True,
                "target_ids": [TARGET],
                "command": " ".join(receipt["argv"]),
                "exit_code": 0,
                "expected_exit_code": 0,
                "evidence_ids": ["focused-qc"],
                "summary": "Actual current-target check executed during the preceding read-only "
                "pass; target and validator inputs remain unchanged and are frozen here.",
            }
        )
    result = {
        "schema_version": "1.0.0",
        "review_id": datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
        + "-dhc-dvh-cultivation-locator-correction",
        "kind": "record",
        "repository": old["repository"],
        "title": "Correct the Dhc195/DvH cultivation source locator while retaining open curation",
        "started_at": read(OUT / "started.json")["started_at"],
        "finished_at": timestamp,
        "reviewer": {
            "identity": "codex",
            "kind": "agent",
            "independence": "self_review",
            "independence_basis": "Author of this bounded successor after a separate read-only "
            "science pass. A different reviewer must approve this new document.",
        },
        "skill": "review-yaml-record",
        "completion": "completed",
        "verdict": "needs_curation",
        "scientific_review": True,
        "summary": "Correct the 2012 unshaken-culture locator from Discussion paragraph2 to "
        "#sec26 direct paragraph5. The statement is supported, and the cultivation omissions "
        "remain open. This bounded scientific observation replaces only the cultivation finding "
        "occurrence; the four other original findings and their original actions remain active.",
        "source": inspection["source"],
        "targets": inspection["targets"],
        "scope": {
            "description": "Source-based reassessment of the cultivation finding and its exact "
            "source locator only; completion applies to this bounded scope, not a new whole-record "
            "scientific certification or canonical repair.",
            "selection": "Exactly CommunityMech:000199 and cm-000199-cultivation; other original "
            "findings and the other three records in the frozen context are not superseded.",
            "coverage": "partial",
            "population_size": 1,
            "reviewed_target_ids": [TARGET],
        },
        "checks": checks,
        "evidence": evidence,
        "assessments": [
            {
                "assessment_id": "cultivation-source",
                "area": "evidence",
                "topic": "Exact culture-source paragraph and treatment separation",
                "outcome": "supported",
                "summary": "Fresh primary text supports unshaken conditions in Discussion "
                "#sec26 direct paragraph5 and the remaining source-bounded cultivation guidance.",
                "target_ids": [TARGET],
                "evidence_ids": ["culture-2012", "culture-2014", "culture-2017", "prior-review"],
                "details": "This explicitly corrects both the original evidence locator and "
                "enrich-cultivation acceptance check. The corrected phrase is: " + corrected_phrase,
            },
            {
                "assessment_id": "retained-curation",
                "area": "completeness",
                "topic": "Still-open source-specific cultivation and independent finding heads",
                "outcome": "concern",
                "summary": "The current target still lacks the bounded culture details. No "
                "record change, terminal disposition or status promotion occurs.",
                "target_ids": [TARGET],
                "evidence_ids": ["current-record", "prior-review", "focused-qc"],
                "details": "The original dvh-roles, dataset-type, omics-evidence and "
                "gtdb-provenance heads retain their original complete actions. The shared "
                "validate-curation acceptance is repeated here for the cultivation head only.",
            },
        ],
        "findings": [finding],
        "actions": actions,
        "related_reviews": [
            {
                "repository": old["repository"],
                "review_id": old["review_id"],
                "relationship": "Bounded open cultivation successor; corrects its source "
                "locator only, preserving four other original finding heads and all history.",
            }
        ],
        "limitations": [
            "Historical unpublished scratch inputs were not recovered. Current concrete sources "
            "are not reconstructed historical bytes; the original review is immutable.",
            "No new full-record scientific verdict, source-stage harmonization, full medium "
            "recipe reconstruction, raw-data analysis, graph revision or KB edit is claimed.",
            "2012/2014/2017 declared supplementary routes returned access/error bodies. This "
            "locator and culture finding is supported by the complete primary main text; "
            "unread supplements are not claimed inspected.",
            "The earlier source-reviewer now authors this correction; independent approval "
            "must come from another reviewer on the final committed bytes.",
        ],
        "notes": ["PR #2061 bundle remediation issue #2635; canonical cultivation stays open."],
        "tags": ["pr2061", "append-only", "source-locator-correction", "bounded-science"],
    }
    write("candidate.json", result)
    print(
        json.dumps(
            {"review_id": result["review_id"], "inputs": len(inspection["source"]["inputs"])}
        )
    )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=["prepare", "build"])
    parser.add_argument("--inspection", default=str(OUT / "inspection.json"))
    args = parser.parse_args()
    if args.mode == "prepare":
        prepare()
    else:
        build(args.inspection)


if __name__ == "__main__":
    main()
