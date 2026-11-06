"""Serialize the assessed PR2034/273 successor; never save or edit records.

Requires the independently read publisher projection and actual audit receipts
under .temp/pr2034/273. Scientific judgments below are explicit author decisions,
not conclusions inferred from validator success. Run native validate before save.
"""

from __future__ import annotations

import copy
import hashlib
import json
import shlex
import subprocess
from datetime import datetime, timezone
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / ".temp/pr2034/273"
TARGET = "data/isolates/Chromobacterium_Gold_Biocyanidation.yaml"
TID = "CommunityMech:000273"
REPO = "CultureBotAI/CommunityMech"
OLDID = "20261019T233358Z-chromobacterium-gold-record"
OLDPATH = f"reviews/structured/{OLDID}/review.yaml"
URL = "https://link.springer.com/article/10.1007/s10163-014-0276-4"
HISTORY = (
    "history/records/Chromobacterium_Gold_Biocyanidation/" "2026-10-21T190000Z-claude-2050.yaml"
)
SCHEMA = "src/communitymech/schema/communitymech.yaml"


class Dumper(yaml.SafeDumper):
    def ignore_aliases(self, data):
        return True


def load(name):
    return json.loads((OUT / name).read_text())


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    now = datetime.now(timezone.utc)
    stamp = now.isoformat().replace("+00:00", "Z")
    old = yaml.safe_load((ROOT / OLDPATH).read_text())
    record = yaml.safe_load((ROOT / TARGET).read_text())
    inspection = load("inspection.json")
    replay = load("direct-replay.json")
    publisher = load("publisher.json")
    assert digest(ROOT / TARGET) == replay["target_sha256"]
    assert (replay["count"], replay["raw_count"], replay["whitespace_count"]) == (15, 10, 14)
    assert replay["target_network_issues"] == []
    assert load("record-delta.json")["graphs_equal"]
    # Final native input capture adds the executed helper and focal remediation
    # decision, without changing any previously inspected input or Git base.
    import sys

    sys.path.insert(0, str(ROOT / "scripts/adhoc"))
    from pr2034_273_audit import ENV

    inputs = [x["path"] for x in inspection["source"]["inputs"] if x["role"] != "target"]
    inputs += [
        "scripts/adhoc/pr2034_273_sources.py",
        "scripts/adhoc/pr2034_273_build_review.py",
        "reports/causal_graph_review/decisions/20261021-stage5-review-remediation.yaml",
        ".claude/skills/evidence-curation/SKILL.md",
    ]
    command = [
        "uv",
        "run",
        "python",
        "scripts/record_review.py",
        "inspect",
        "--targets",
        str(OUT / "targets.yaml"),
    ]
    for path in sorted(set(inputs)):
        command += ["--input", path]
    result = subprocess.run(command, cwd=ROOT, env=ENV, capture_output=True, check=True)
    current = json.loads(result.stdout)
    assert current["source"]["git_revision"] == inspection["source"]["git_revision"]
    for item in inspection["source"]["inputs"]:
        assert item in current["source"]["inputs"]
    (OUT / "inspection-final-v3.json").write_bytes(result.stdout)
    owner = old["targets"][0]["owner_paths"]
    doc = {
        "schema_version": "1.0.0",
        "review_id": now.strftime("%Y%m%dT%H%M%SZ") + "-pr2034-chromobacterium-gold-successor",
        "kind": "record",
        "repository": REPO,
        "title": "Chromobacterium PCB bioleaching: current successor and finding reconciliation",
        "started_at": load("inspect.json")["started_at"],
        "finished_at": stamp,
        "reviewer": {
            "identity": "codex-pr2034-273-author",
            "kind": "agent",
            "independence": "unknown",
            "independence_basis": "Did not author or modify the target in this canary. "
            "Historical curation and the predecessor use Codex identities; "
            "person-level independence is not established. Separate adversarial review "
            "is coordinated by the parent agent and is not claimed here.",
        },
        "skill": "review-yaml-record",
        "completion": "partial",
        "verdict": "needs_curation",
        "scientific_review": True,
        "summary": "The current record removes the old ore, detoxification, density and operating "
        "overclaims while preserving four supported PCB graph nodes and two bounded arrows. "
        "Three major findings remain: two source-unverified precision claims, unsupported role "
        "enums, and mine-tailing grounding. One new minor finding identifies a wrong-target "
        "history event. Two historical finding lineages are explicitly resolved. All eight "
        "focused checks pass; corpus network recipes report warnings elsewhere. Full Methods "
        "were unavailable, so this is a partial scientific review, not full-paper certification.",
        "source": current["source"],
        "targets": copy.deepcopy(old["targets"]),
        "scope": {
            "description": "Whole current YAML, all 15 evidence placements, four interaction "
            "nodes, two arrows, four environmental factors, two history events and every "
            "finding previously assigned to this stable target.",
            "selection": "PR2034 canary stale-review refresh for CommunityMech:000273 only.",
            "coverage": "full",
            "population_size": 1,
            "reviewed_target_ids": [TID],
        },
        "checks": [],
        "evidence": [],
        "assessments": [],
        "findings": [],
        "actions": [],
        "limitations": [
            "The complete current publisher abstract and title were read, but Methods, source "
            "strain and supplements were not available. Unsupported in this inspected scope "
            "does not mean experimentally false. The 45.5% comparator remains unresolved.",
            "The tracked cache explicitly contains selected, abbreviated or reworded text. "
            "Reference-validator success is not primary-source authenticity.",
            "GTDB checks establish internal lineage/domain coherence. The stated 78-genome, "
            "0.97 aggregate was not regenerated from its historical mapping release.",
            "The required corpus network commands returned 1 for 44 warnings in 16 of 503 "
            "records and zero errors; the selected record has no native network issue.",
            "Source inspection used the public web-rendered publisher page; direct urllib "
            "returned a challenge page that was not used as scientific content.",
        ],
        "notes": [
            "The initial native inspection rejected the CLAUDE.md symlink. A successful "
            "retry captured its regular AGENTS.md target with the same guidance. This was "
            "an administrative inspection failure, not a record validator failure.",
            "All historical bundles and per-record history are preserved. Proposed actions "
            "are not curation already performed. Root owns any issue and Git operations.",
            "Scratch receipts are audit artifacts, not committed source caches; their hashes, "
            "commands, conclusions and precise locators are recorded here.",
        ],
        "related_reviews": [
            {
                "repository": REPO,
                "review_id": item["review_id"],
                "relationship": "Current target-specific successor; exact finding "
                "lineages are reconciled through previous_occurrences.",
            }
            for item in load("lineage.json")
        ],
        "tags": ["pr2034-canary", "record-review", "isolate", "pcb-bioleaching", "successor"],
    }

    def evidence(eid, kind, reference, locator, summary, support="supports", snapshot=None):
        item = {
            "evidence_id": eid,
            "kind": kind,
            "reference": reference,
            "locator": locator,
            "summary": summary,
            "support": support,
            "accessed_at": stamp,
        }
        if snapshot:
            item["snapshot_sha256"] = digest(OUT / snapshot)
        doc["evidence"].append(item)
        return item

    evidence(
        "current",
        "record_content",
        TARGET,
        "Whole YAML; current source.inputs digest",
        "Current PCB-specific record; environmental factors reduced from eleven to four. "
        "Four nodes and two arrows are byte-equivalent as parsed data to the predecessor.",
    )
    evidence(
        "publisher",
        "primary_source",
        URL,
        "Complete Abstract, five displayed text lines 36–40 and article title; "
        "local publisher.json contains only this projection",
        "Primary experimental context and intervention direction were reassessed. "
        "No full Methods access is claimed.",
        snapshot="publisher.json",
    )
    evidence(
        "cache",
        "record_content",
        "references_cache/doi_10.1007_s10163-014-0276-4.md",
        "Front matter content_type/source_review_note and complete selected-excerpts body",
        "The cache declares rewording and cannot alone authenticate quotations.",
    )
    evidence(
        "snippet-replay",
        "validation",
        "scripts/adhoc/pr2034_273_audit.py",
        "replay step; all 15 recursive placements; direct-replay.json",
        "10 raw publisher matches; four further matches after whitespace normalization. "
        "The engineering snippet alone changes initial lowercase gold to uppercase Gold. "
        "All 15 match the selected-excerpts cache; no Discussion EvidenceItems occur.",
        snapshot="direct-replay.json",
    )
    evidence(
        "schema-roles",
        "authority",
        SCHEMA,
        "FunctionalRoleEnum and AbundanceEnum; taxonomy descriptor semantics",
        "PRIMARY_PRODUCER requires carbon fixation and PRIMARY_DEGRADER requires complex "
        "substrate degradation. DOMINANT is ordinal prominence, not a measured proportion.",
    )
    evidence(
        "envo",
        "authority",
        "sqlite:obo:envo",
        "ENVO:00000003 label and definition, " "queried using oaklib.get_adapter; envo.json",
        "The class concerns material remaining from separation of ore and gangue, "
        "which differs from a PCB laboratory leaching culture.",
        snapshot="envo.json",
    )
    evidence(
        "old-review",
        "record_content",
        OLDPATH,
        "Whole old review, findings scope, " "organism-mechanism, roles and envo",
        "All four old issue keys retained; "
        "current conclusions were reached from present bytes and source inspection.",
    )
    evidence(
        "delta",
        "record_content",
        TARGET,
        "git show a4611c913c8da9619673df63a0c2cce3aa206a83 target versus current; "
        "record-delta.json verifies the predecessor target SHA before comparison",
        "Removed general ore, named gene/enzyme, detoxification, pigment, CFU and "
        "unsupported operating prose; retained graph unchanged.",
        snapshot="record-delta.json",
    )
    evidence(
        "history-event",
        "record_content",
        HISTORY,
        "Whole event, especially events[0] " "summary/details and target.path",
        "Target path names 273, but the event narrates "
        "000181, DSM 30191 and SYNTROPHIC_PARTNER changes absent from the actual record "
        "delta and contradictory to embedded curation_history[1].",
        support="refutes",
    )
    evidence(
        "stage5",
        "record_content",
        "reviews/structured/20261021T193000Z-stage5-remediation-verification/review.yaml",
        "findings[finding_id=stage4-isolate-000273-unverified-ore-prose] and its two "
        "Stage4 previous_occurrences",
        "The separate ore-specific lineage was resolved "
        "after the October repair. That bounded resolution is retained, without "
        "adopting its unsupported assertion that every current number is source-certified.",
    )
    evidence(
        "discovery",
        "search",
        "Local owned PR2034 worktree",
        "Exact stable ID, slug, "
        "DOI and Chromobacterium search; structured YAML finding selection by target ID",
        "Found one focal selected-excerpts carrier and four structured reviews containing "
        "findings for this stable target. Historical reports are not new primary evidence.",
        support="context_only",
    )["search_scope"] = (
        "rg --no-ignore --hidden over reviews, history, reports, tests, references_cache "
        "and scripts in this worktree; exact ID/slug/DOI. All structured review YAMLs "
        "were parsed for target findings. No other checkout or old scratch was used."
    )
    commands = [
        "validate",
        "validate-strict",
        "validate-terms",
        "validate-gtdb",
        "validate-gtdb-domain",
        "validate-history",
        "normalize-cache-names",
        "validate-references-explained",
        "audit-network",
        "check-network-quality",
    ]
    for key in commands:
        receipt = load(key + ".json")
        corpus = key in {"audit-network", "check-network-quality"}
        summary = (
            "Actual corpus result: 503 records, 44 warnings in 16 records, zero errors. "
            "No issue is attributed to this target."
            if corpus
            else "Focused command completed with exit 0; actual stdout/stderr hashes retained."
        )
        if key == "normalize-cache-names":
            summary = "Read-only repository cache-name diagnostic passed."
        if key == "validate-references-explained":
            summary = "No reported reference issues against the selected-excerpts cache; "
            summary += "independent publisher replay is separately assessed."
        environment = " ".join(f"{k}={shlex.quote(v)}" for k, v in receipt["environment"].items())
        doc["checks"].append(
            {
                "check_id": key,
                "name": key,
                "status": "passed" if receipt["exit_code"] == 0 else "failed",
                "required": True,
                "summary": summary,
                "target_ids": [TID],
                "command": environment + " " + receipt["command"],
                "exit_code": receipt["exit_code"],
                "expected_exit_code": 0,
                "evidence_ids": ["check-" + key],
                "scope_note": (
                    "Corpus diagnostic; target result isolated separately."
                    if corpus
                    else "Single record or its history directory; cache-name check is repository-wide."
                ),
            }
        )
        evidence(
            "check-" + key,
            "validation",
            receipt["command"],
            f"Executed {receipt['started_at']} through {receipt['finished_at']}; "
            f"stdout SHA256 {receipt['stdout_sha256']}; stderr SHA256 {receipt['stderr_sha256']}",
            summary,
            support="context_only",
            snapshot=key + ".json",
        )
    doc["checks"].append(
        {
            "check_id": "primary-methods",
            "name": "Primary Methods access",
            "status": "unavailable",
            "required": True,
            "summary": "The public publisher page "
            "provides the abstract and identifies subscription content. No Methods support was "
            "established for the 45.5% comparator or exact oxygen-start timing.",
            "target_ids": [TID],
            "evidence_ids": ["publisher"],
            "scope_note": "Partial completion reflects this specific material evidence gap; "
            "the DOI itself resolves and is not an invalid-reference finding.",
        }
    )

    def assess(aid, area, topic, outcome, summary, eids, **kw):
        doc["assessments"].append(
            {
                "assessment_id": aid,
                "area": area,
                "topic": topic,
                "outcome": outcome,
                "summary": summary,
                "target_ids": [TID],
                "evidence_ids": eids,
                **kw,
            }
        )

    assess(
        "identity",
        "identity",
        "Current source, organism and experimental scope",
        "supported",
        "Single-species PCB leaching stage remains distinct from the prior separately "
        "applied biooxidation. ENGINEERED describes the process design, not proven genetic "
        "engineering. No exact strain has been authenticated.",
        ["current", "publisher"],
        dimensions=[
            {
                "name": "source_tier",
                "value": "Primary publisher abstract; "
                "selected-excerpts local cache; Methods unavailable",
                "definition": "Actual access scope of this successor, not inherited "
                "full-paper coverage.",
                "evidence_ids": ["publisher", "cache"],
            },
            {
                "name": "source_strain",
                "value": "Species-level identification only",
                "definition": "No strain inferred from a wrong-target history event.",
                "evidence_ids": ["publisher", "history-event"],
            },
        ],
    )
    assess(
        "taxonomy",
        "grounding",
        "Taxonomy, abundance and roles",
        "concern",
        "Species label and GTDB/domain validators pass. DOMINANT and monoculture wording "
        "are retained as the modeled single-member composition, not a viability/purity "
        "measurement. Neither declared functional role is established by the cited function.",
        [
            "current",
            "schema-roles",
            "publisher",
            "check-validate-terms",
            "check-validate-gtdb",
            "check-validate-gtdb-domain",
        ],
    )
    assess(
        "source-precision",
        "evidence",
        "Engineering, environmental and snippet scope",
        "concern",
        "The broad old claims are removed. The remaining 45.5% comparator and the claimed "
        "oxygen-addition start after depletion lack support in the inspected abstract. "
        "A lowercase source initial was capitalized in the engineering evidence.",
        ["current", "publisher", "snippet-replay", "delta"],
    )
    assess(
        "environment",
        "grounding",
        "Environment ontology application",
        "concern",
        "Correctly resolved ENVO label still describes ore-processing residue rather than "
        "this PCB assay. Updated notes do not repair the ontology assignment.",
        ["current", "envo", "publisher"],
    )
    assess(
        "cultivation",
        "completeness",
        "Cultivation and external resources",
        "supported",
        "Medium constituents are already described in evidence and environmental factors. "
        "No growth_media, cultivation_setup, external_resources or associated_datasets block "
        "is present. These optional omissions do not justify fabricated recipes, exact "
        "medium identifiers or a biological-absence claim. Source strain and protocol "
        "details remain limited by access.",
        ["current", "publisher"],
    )
    node_summaries = [
        "Retain cyanogenesis and the reported supplemented medium; no traced substrate flux, "
        "specific enzyme mechanism or concentration is inferred.",
        "Retain PCB gold dissolution and combined-treatment endpoint; no specific dissolved "
        "complex, ore recovery or purification yield is claimed.",
        "Retain oxygen-supported leaching and respiration context, without a partner-benefit claim.",
        "Retain separate pretreatment and particle-size context; do not convert it into a coculture "
        "or separate the contributions of combined interventions.",
    ]
    locators = [
        "Abstract first paragraph",
        "Abstract second and final paragraphs",
        "Abstract second paragraph",
        "Abstract pretreatment/particle-size paragraph",
    ]
    for i, node in enumerate(record["ecological_interactions"]):
        dimensions = []
        for j, item in enumerate(node.get("evidence", [])):
            locator = locators[i]
            if i == 1:
                locator = "Abstract first paragraph" if j == 0 else "Abstract final paragraph"
            dimensions.append(
                {
                    "name": f"node-{i}-evidence-{j}",
                    "value": item["snippet"],
                    "definition": f"Exact inspected record snippet at ecological_interactions[{i}]"
                    f".evidence[{j}]; {locator} in DOI 10.1007/s10163-014-0276-4. "
                    "Whitespace normalization is disclosed in snippet-replay.",
                    "evidence_ids": ["current", "publisher", "snippet-replay"],
                }
            )
        assess(
            f"node-{i}",
            "graph",
            f"ecological_interactions[{i}] {node['name']}",
            "supported",
            node_summaries[i],
            ["current", "publisher", "snippet-replay"],
            dimensions=dimensions,
        )
        for j, edge in enumerate(node.get("downstream", [])):
            assess(
                f"edge-{i}-{j}",
                "graph",
                f"ecological_interactions[{i}].downstream[{j}]",
                "supported",
                "Current arrow target and description retained after independent "
                "primary-source reassessment. The model does not assert reciprocal fitness "
                "or a separate simultaneous recipient organism.",
                ["current", "publisher"],
                dimensions=[
                    {
                        "name": "target",
                        "value": edge["target"],
                        "definition": "Exact current target name resolves to node 1.",
                        "evidence_ids": ["current"],
                    },
                    {
                        "name": "description",
                        "value": edge["description"],
                        "definition": "Exact current directed assertion; source context is "
                        + (
                            "Abstract first/second paragraphs: cyanogenic culture and "
                            "gold/cyanide reaction."
                            if i == 0
                            else "Abstract pretreatment paragraph: separately biooxidized material "
                            "then improved PCB leaching and particle-size result."
                        ),
                        "evidence_ids": ["current", "publisher"],
                    },
                ],
            )
    assess(
        "history",
        "provenance",
        "Exact old/current changes and finding lineages",
        "concern",
        "The target hash matches the Stage5 remediation result. That change removed the "
        "old mechanism and ore prose while leaving graph/roles/ENVO unchanged. The appended "
        "history event instead records unrelated identifiers and changes; append a correction "
        "rather than rewriting provenance. Every old issue key is explicitly dispositioned.",
        ["delta", "history-event", "old-review", "stage5"],
    )
    assess(
        "adapters",
        "evidence",
        "Gene/regulatory adapter applicability",
        "not_applicable",
        "The current record no longer makes gene/regulatory/module claims. No iModulonDB "
        "or related-organism module query is needed to reassess the removed mechanism "
        "finding; no database-coverage absence claim is made.",
        ["current", "delta"],
    )
    assess(
        "validation",
        "schema",
        "Actual validators and isolated native network",
        "supported",
        "Eight focused commands passed. Independently invoking the native auditor on this "
        "record returned no issues; four graph discussion anchors and both targets resolve. "
        "Corpus warnings remain actual failures, not target defects.",
        ["snippet-replay"] + ["check-" + x for x in commands],
    )
    assess(
        "scores",
        "completeness",
        "Native scores and current unresolved findings",
        "concern",
        "Completeness 80; raw validation quality 100.5, capped 100. These presence/penalty "
        "scores do not certify the science or override the three open major findings.",
        ["current", "snippet-replay", "schema-roles"],
        metrics=[
            {
                "name": "completeness",
                "value": 80,
                "unit": "points",
                "minimum": 0,
                "maximum": 100,
                "definition": "Native rubric: 50 required +5 environment "
                "+10 at least three environmental factors +10 at least three interactions "
                "+0 external resources +0 growth media +0 datasets +5 metabolites =80.",
            },
            {
                "name": "validation_quality_raw",
                "value": 100.5,
                "unit": "points",
                "definition": "100-50*0 P1-10*3 open P2-2*1 open P3 +17.5 evidence bonus "
                "(7 direct items/4 nodes, mean1.75, divided by2 times20) +15 complete native "
                "participant/reference network =100.5. Resolved findings are not re-penalized.",
            },
            {
                "name": "validation_quality",
                "value": 100,
                "unit": "points",
                "minimum": 0,
                "maximum": 100,
                "definition": "Clamp raw 100.5 to [0,100]. This does not "
                "override source limitations, ontology meaning or any failing required check.",
            },
            {
                "name": "interaction_evidence",
                "value": 1.75,
                "unit": "items per node",
                "denominator": 4,
                "definition": "Seven directly attached evidence items "
                "across four nodes, all from one paper; not seven independent experiments.",
            },
        ],
    )

    def previous(review, finding):
        return {"repository": REPO, "review_id": review, "finding_id": finding}

    for original in old["findings"]:
        finding = copy.deepcopy(original)
        fid = finding["finding_id"]
        finding["previous_occurrences"] = [previous(OLDID, fid)]
        finding["evidence_ids"] = ["current", "old-review", "delta", "publisher"]
        if fid == "scope":
            finding.update(
                title="Residual comparator and oxygen timing remain source-unverified",
                description="The broad refractory-ore, CFU, safety, cost and operating "
                "claims were removed. Description and environmental_factors[3] still "
                "assert a 45.5% direct-bioleaching comparator absent from the inspected "
                "abstract and cache. environmental_factors[2].value asserts oxygen "
                "supplementation after 24 h depletion, whereas the abstract states "
                "depletion without supplementation and does not establish the start "
                "time. These are unverified claims, not demonstrated false results.",
                field_paths=[
                    "description",
                    "environmental_factors[3].description",
                    "environmental_factors[2].value",
                ],
                disposition_reason="Open successor with substantially narrowed scope: "
                "most prior defects are repaired, but claim-level numerical/protocol "
                "support is still incomplete. No inference that the full paper lacks it.",
            )
        elif fid == "organism-mechanism":
            finding.update(
                status="resolved",
                title="Unsupported organism-mechanism claims removed",
                description="Current whole-record inspection and exact Git delta "
                "confirm removal of hcnABC/enzyme, detoxification guarantee, pigment "
                "readout and CFU claims. The qualified graph remains unchanged.",
                disposition_reason="Resolved by removal in the October 21 repair, "
                "independently confirmed now. This disposition does not claim the "
                "biology is impossible or certify the removed claims in another strain.",
                field_paths=[
                    "taxonomy[0].taxon_term.notes",
                    "taxonomy[0].abundance_value",
                    "description",
                    "environment_term.notes",
                    "environmental_factors",
                ],
            )
        elif fid == "roles":
            finding.update(
                title="Role enums remain unsupported by the source-defined function",
                description="The current PRIMARY_PRODUCER and PRIMARY_DEGRADER "
                "assignments remain unchanged. The schema requires carbon fixation "
                "and complex-substrate degradation respectively; cyanide generation "
                "and mobilizing metal from PCB material do not establish those roles.",
                disposition_reason="Open: the October repair changed notes, not these "
                "role enum assignments.",
            )
            finding["evidence_ids"].append("schema-roles")
        elif fid == "envo":
            finding.update(
                description="ENVO:00000003 still denotes mine tailing. Its current "
                "OAK definition is ore/gangue separation residue; updated PCB notes "
                "do not make that material class applicable to the laboratory assay.",
                disposition_reason="Open: ID and label are unchanged despite the "
                "source-bounded note repair.",
            )
            finding["evidence_ids"].append("envo")
        doc["findings"].append(finding)
    ore_key = "communitymech-stage4-000273-unverified-ore-prose"
    ore = next(
        f for item in load("lineage.json") for f in item["findings"] if f["issue_key"] == ore_key
    )
    finding = copy.deepcopy(ore)
    finding.update(
        finding_id="ore-lineage",
        status="resolved",
        title="Parallel ore-specific remediation remains resolved",
        description="The targeted arsenopyrite/pyrite scope and old un-evidenced "
        "ore operating ranges are absent from the current record. Retaining this "
        "resolution does not endorse the Stage5 report's 45.5% attribution.",
        evidence_ids=["current", "delta", "stage5"],
        disposition_reason="Independently confirmed removal of the exact old "
        "ore-scope defects, reconciling both Stage4 observations and the Stage5 "
        "resolved observation. Remaining comparator/timing precision is tracked "
        "under the original broader scope issue key.",
        previous_occurrences=[
            previous(item["review_id"], f["finding_id"])
            for item in load("lineage.json")
            for f in item["findings"]
            if f["issue_key"] == ore_key
        ],
    )
    doc["findings"].append(finding)
    doc["findings"].append(
        {
            "finding_id": "history",
            "issue_key": "cm-000273-history-2050-wrong-record-and-change",
            "category": "provenance",
            "severity": "minor",
            "status": "open",
            "certainty": "confirmed",
            "title": "Per-record history narrates a different target and absent changes",
            "description": "The October 21 event is filed under 273, but its details name "
            "CommunityMech:000181 and claim DSM 30191 and SYNTROPHIC_PARTNER additions. "
            "Neither appears in 273's current record or actual change. Embedded history describes "
            "the PCB prose repair instead. Schema validity does not establish historical truth.",
            "target_ids": [TID],
            "field_paths": ["curation_history[1]"],
            "evidence_ids": ["history-event", "delta", "current"],
            "rule_id": "review-checklist:audit",
            "native_severity": "P3",
            "normalization_reason": "Bounded provenance defect; it does not change the currently modeled organism.",
            "owner_paths": [
                {
                    "repository": REPO,
                    "path": "history/records/Chromobacterium_Gold_Biocyanidation",
                    "role": "append_only_correction_owner",
                }
            ],
        }
    )
    actions = {
        "scope": (
            "Verify or qualify the remaining comparator and timing; repair the small "
            "engineering-snippet capitalization discrepancy from the publisher.",
            [
                "Locate exact primary Results/figure/table support for the 45.5% comparison "
                "or remove/qualify that number in both current placements.",
                "Do not infer supplementation start time from an unsupplemented depletion endpoint.",
                "Use the exact lowercase source excerpt at engineering_design.evidence[0] "
                "or a different verified contiguous source snippet; rerun strict/reference checks.",
            ],
        ),
        "roles": (
            "Remove or replace role enums only with a directly supported function and "
            "the actual schema meaning.",
            [
                "No autotrophy inferred from chemical production.",
                "No complex-substrate degradation inferred solely from gold dissolution.",
                "Rerun strict, term and network validation after separately authorized curation.",
            ],
        ),
        "envo": (
            "Reconcile environment grounding with the actual PCB experiment.",
            [
                "Verify any replacement ID, label and definition; do not guess a neighboring term.",
                "Align environmental notes and rerun term/strict checks.",
            ],
        ),
        "history": (
            "Append an explicit correction to the erroneous historical event.",
            [
                "Preserve the old event bytes; cite its exact filename and explain the "
                "wrong ID/strain/role narrative using the actual record delta.",
                "State the real 273 PCB prose repair, then validate history.",
            ],
        ),
    }
    for fid, (description, acceptance) in actions.items():
        finding = next(f for f in doc["findings"] if f["finding_id"] == fid)
        doc["actions"].append(
            {
                "action_id": "fix-" + fid,
                "description": description,
                "finding_ids": [fid],
                "target_ids": [TID],
                "owner_paths": finding.get("owner_paths", owner),
                "acceptance_checks": acceptance,
            }
        )
    destination = OUT / "candidate-v3.yaml"
    with destination.open("x") as stream:
        yaml.dump(doc, stream, Dumper=Dumper, allow_unicode=True, sort_keys=False, width=100)
    print(
        json.dumps(
            {
                "review_id": doc["review_id"],
                "path": str(destination),
                "sha256": digest(destination),
                "findings": len(doc["findings"]),
            }
        )
    )


if __name__ == "__main__":
    main()
