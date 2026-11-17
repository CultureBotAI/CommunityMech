"""Save-ready field addendum for CommunityMech000087, 2026-11-14.

Inputs: current record, schema, Coker primary XML, prior immutable review and
its seven M5 receipts. Output: a native partial-field review candidate for #2776.
No canonical, cache, history or prior review is modified.
"""

import hashlib
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
STATE = ROOT / ".temp/m5-completion-20261114"
TARGET = "kb/communities/LBNL_Switchgrass_Soil_SynCom16.yaml"
TARGET_ID = "CommunityMech:000087"
PRIOR_ID = "20261114T213343Z-m5-lbnl-switchgrass-completion"
PRIOR = f"reviews/structured/{PRIOR_ID}/review.yaml"
XML = ".temp/m5-completion-20261114/ecofab-relations/PMC9765266.xml"
SCHEMA = "src/communitymech/schema/communitymech.yaml"


def digest(path):
    return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()


def main():
    started = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    prior = yaml.safe_load((ROOT / PRIOR).read_text())
    target_hash = next(i["sha256"] for i in prior["source"]["inputs"] if i["path"] == TARGET)
    if digest(TARGET) != target_hash:
        raise ValueError("Canonical input changed since independently reviewed source")
    inputs = [
        TARGET,
        SCHEMA,
        XML,
        PRIOR,
        "docs/record-review-profile.md",
        ".claude/skills/curate-yaml-record/references/review-checklist.md",
        ".claude/skills/review-communities/reference/metrics-and-reports.md",
        str(Path(__file__).relative_to(ROOT)),
    ]
    for name in ("schema", "strict", "terms", "references", "gtdb", "domain", "history"):
        inputs.extend(f".temp/m5-completion-20261114/lbnl-{name}.{ext}" for ext in ("json", "log"))
    command = [
        sys.executable,
        "scripts/record_review.py",
        "inspect",
        "--targets",
        str(STATE / "lbnl-targets.yaml"),
    ]
    for path in inputs:
        command.extend(["--input", path])
    result = subprocess.run(command, cwd=ROOT, capture_output=True, text=True, check=True)
    inspected = json.loads(result.stdout)
    (STATE / "lbnl-environment-addendum-inspection.json").write_text(result.stdout)
    now = datetime.now(timezone.utc)
    finished = now.strftime("%Y-%m-%dT%H:%M:%SZ")
    evidence = [
        {
            "evidence_id": "record",
            "kind": "record_content",
            "reference": TARGET,
            "locator": "environment_term; source soil note, lines28-34",
            "accessed_at": finished,
            "support": "refutes",
            "snapshot_sha256": digest(TARGET),
            "summary": "The typed physical setting is ENVO00001998 soil; notes describe the source habitat. The record is an engineered collection tested in liquid medium and EcoFAB chambers.",
        },
        {
            "evidence_id": "schema",
            "kind": "record_content",
            "reference": SCHEMA,
            "locator": "MicrobialCommunity.environment_term and modeled_environment, lines2338-2350",
            "accessed_at": finished,
            "support": "refutes",
            "snapshot_sha256": digest(SCHEMA),
            "summary": "environment_term denotes the physical studied setting; modeled_environment separately records the habitat from which a synthetic community derives or which it represents.",
            "quote": "Environment where community exists",
        },
        {
            "evidence_id": "primary",
            "kind": "primary_source",
            "reference": "https://pmc.ncbi.nlm.nih.gov/articles/PMC9765266/",
            "locator": "Coker PMID36472419, DOI10.1128/msystems.00951-22: Methods Soil isolate growth conditions(s4-2); Synthetic community growth conditions(s4-3); Plant colonization experiment(s4-6)",
            "accessed_at": finished,
            "support": "supports",
            "snapshot_sha256": digest(XML),
            "summary": "Individual cultures are3-5mL liquidR2A in14mL tubes; community assays use200microlitres liquidR2A in96well plates at30C; plant assays use B.distachyonBd21-3 in EcoFAB chambers containing0.1MS at24C. Switchgrass-associated soil is source habitat, not the physical matrix of these experiments.",
            "quote": "200 μL of liquid R2A medium",
        },
        {
            "evidence_id": "prior",
            "kind": "prior_review",
            "reference": PRIOR,
            "locator": "identity evidence; findings member-roster and assay-scope; all three node assessments and seven focused checks",
            "accessed_at": finished,
            "support": "context_only",
            "snapshot_sha256": digest(PRIOR),
            "summary": "Original review correctly retains two major findings under1548 and distinguishes source habitat in prose, but omits the environment_term field mismatch. This addendum preserves the original and adds one minor finding; no earlier finding is resolved or superseded.",
        },
    ]
    checks = []
    for check in prior["checks"]:
        if not check["required"]:
            continue
        name = check["check_id"]
        receipt_path = f".temp/m5-completion-20261114/lbnl-{name}.json"
        log_path = f".temp/m5-completion-20261114/lbnl-{name}.log"
        receipt = json.loads((ROOT / receipt_path).read_text())
        if receipt["exit_code"] != 0 or receipt["log_sha256"] != digest(log_path):
            raise ValueError("M5 receipt mismatch: " + name)
        if datetime.fromisoformat(receipt["finished_at"]) > now:
            raise ValueError("Receipt later than assessment")
        evidence.append(
            {
                "evidence_id": "check-" + name,
                "kind": "validation",
                "reference": log_path,
                "locator": "Full M5 log and paired JSON receipt; original review binds unchanged target hash",
                "accessed_at": finished,
                "support": "context_only",
                "snapshot_sha256": digest(log_path),
                "summary": "Previously executed focused gate passed on fresh M5 revision76aa644c; reused against unchanged canonical bytes. Not rerun and not semantic proof of this field.",
            }
        )
        checks.append(
            dict(
                check,
                summary="Verified existing passed receipt against unchanged target; no rerun.",
            )
        )
    finding = {
        "finding_id": "source-versus-studied-environment",
        "issue_key": "cm-000087-source-versus-studied-environment",
        "category": "scope",
        "severity": "minor",
        "native_severity": "P3",
        "normalization_reason": "A bounded physical-setting versus source-habitat mismatch affects typed reuse; explicit synthetic identity and measured results remain interpretable.",
        "rule_id": "review-checklist.environment-physical-versus-modeled-context",
        "status": "open",
        "certainty": "confirmed",
        "title": "Separate source soil from the physical laboratory setting",
        "description": "environment_term currently describes source soil although the source assays are liquid cultures/EcoFABs. Use a verified laboratory term for the physical setting and preserve source soil/rhizosphere under modeled_environment, without changing16/17/18 variant scope.",
        "target_ids": [TARGET_ID],
        "field_paths": ["environment_term", "modeled_environment"],
        "owner_paths": [
            {"repository": "CultureBotAI/CommunityMech", "path": TARGET, "role": "canonical_record"}
        ],
        "evidence_ids": ["record", "schema", "primary", "prior"],
        "external_issues": ["https://github.com/CultureBotAI/CommunityMech/issues/2776"],
    }
    review = {
        "schema_version": "1.0.0",
        "review_id": now.strftime("%Y%m%dT%H%M%SZ") + "-m5-lbnl-environment-addendum",
        "kind": "record",
        "repository": "CultureBotAI/CommunityMech",
        "title": "LBNL SynCom16 environment field addendum",
        "started_at": started,
        "finished_at": finished,
        "reviewer": {
            "identity": "codex-independent-review",
            "kind": "agent",
            "independence": "independent",
            "independence_basis": "Not author of canonical record or original000087 review; independently compared full record and saved assessment to primary main text and Figures2/3/5, then isolated this omitted typed-field defect.",
        },
        "skill": "review-yaml-record",
        "completion": "completed",
        "verdict": "needs_curation",
        "scientific_review": True,
        "summary": "Additive field-scoped assessment identifies source-versus-studied environment mismatch2776. Original roster/assay findings1548 remain open. Prior seven checks pass on unchanged bytes; full record review remains in the original immutable bundle.",
        "source": inspected["source"],
        "targets": inspected["targets"],
        "scope": {
            "description": "Only environment_term and modeled_environment semantics are newly assessed by this addendum; no full-record re-clearance or supersession.",
            "selection": "Omitted field mismatch found by independent review of the saved000087 full assessment.",
            "coverage": "partial",
            "population_size": 1,
            "reviewed_target_ids": [TARGET_ID],
        },
        "checks": checks,
        "evidence": evidence,
        "assessments": [
            {
                "assessment_id": "environment",
                "area": "scope",
                "topic": "Source habitat versus physical studied environment",
                "outcome": "concern",
                "summary": "Soil is the isolate source/model habitat. Actual source experiments use liquidR2A and EcoFAB chambers. The current typed field conflates those roles.",
                "target_ids": [TARGET_ID],
                "evidence_ids": ["record", "schema", "primary", "prior"],
                "details": "Exact selectors environment_term and modeled_environment. No ecological node, edge, functional role or stock identity is changed or newly certified. Physical laboratory setting is directly supported by Methods; select and validate a canonical ontology term during curation.",
            },
            {
                "assessment_id": "metric-context",
                "area": "completeness",
                "topic": "Native metrics with retained findings visible",
                "outcome": "supported",
                "summary": "Unchanged record has native completeness25. Combined open findings are two priorP2 plus thisP3; capped quality remains100 and does not clear any finding.",
                "target_ids": [TARGET_ID],
                "evidence_ids": ["record", "prior"],
                "metrics": [
                    {
                        "name": "completeness",
                        "value": 25,
                        "unit": "points",
                        "minimum": 0,
                        "maximum": 100,
                        "definition": "Native unchanged-record rubric:0required-with-all-member-roles+5environment+0three-factors+10three-nodes+0resources+10medium+0datasets+0node-metabolites=25. Missing optional roles are not invented.",
                    },
                    {
                        "name": "validation_quality",
                        "value": 100,
                        "unit": "points",
                        "minimum": 0,
                        "maximum": 100,
                        "denominator": 3,
                        "definition": "Combined context:100-50*0P1-10*2retainedP2-2*1newP3+20min((5/3)/2,1)+15structural completeness=109.6666666667 capped100. Prior two findings remain in original bundle, not silently resolved by this field-only addendum.",
                    },
                    {
                        "name": "retained_P2",
                        "value": 2,
                        "unit": "findings",
                        "definition": "Two original000087 findings under1548; not superseded.",
                    },
                    {
                        "name": "new_P3",
                        "value": 1,
                        "unit": "findings",
                        "definition": "Environment mismatch newly recorded here.",
                    },
                ],
            },
        ],
        "findings": [finding],
        "actions": [
            {
                "action_id": "separate-environment-roles",
                "description": "Use a source-supported physical laboratory setting and preserve modeled soil/rhizosphere separately.",
                "finding_ids": [finding["finding_id"]],
                "target_ids": [TARGET_ID],
                "owner_paths": [
                    {
                        "repository": "CultureBotAI/CommunityMech",
                        "path": TARGET,
                        "role": "canonical_record",
                    }
                ],
                "acceptance_checks": [
                    "Verify the chosen ENVO identifier and label; distinguish physical setting from source/model habitat with claim-local source evidence.",
                    "Preserve16/17/18 assay distinctions and unresolved roster1548; append history, run focused term/strict/reference checks and generated-doc checks, then save a new current-input assessment.",
                ],
            }
        ],
        "limitations": [
            "This completed assessment has partial field coverage; it does not replace or claim full-record clearance beyond the original review.",
            "No canonical, cache, history or existing review was edited. No speculative ontology ID was adopted; an existing laboratory term elsewhere in the corpus is only a candidate until curation validation.",
            "No new paid/provider call or raw-data reanalysis. The source paper and schema already establish the experimental setting; unrelated record claims remain with the original review.",
            "Issue1548 also covers two other records; they remain outside this addendum, and neither1548 nor its prior findings is closed or superseded.",
        ],
        "related_reviews": [
            {
                "repository": "CultureBotAI/CommunityMech",
                "review_id": PRIOR_ID,
                "relationship": "Additive independent field-semantics amendment; preserves original bundle and all prior open findings.",
            }
        ],
    }
    output = STATE / "lbnl-environment-addendum.yaml"
    output.write_text(yaml.safe_dump(review, sort_keys=False, allow_unicode=True, width=100))
    print(output)


if __name__ == "__main__":
    main()
