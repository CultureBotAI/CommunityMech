"""Build the PR 2058 record 294 refresh as JSON for the native immutable saver.

Only scratch JSON is written. Source retrieval and focused checks were run
read-only before this builder; every concrete input is captured by prepare.
"""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

import yaml

OUT = Path(".temp/pr2058/294-author")
SELF = Path("scripts/adhoc/pr2058_294_refresh.py")
OLD = Path(
    "reviews/structured/20261022T011317Z-corynebacterium-shewanella-record-review/review.yaml"
)
TARGET = "CommunityMech:000294"
STAGE4 = Path("reviews/structured/20261025T113600Z-c2s4-frozen-cohort-review/review.yaml")
STAGE5 = Path("reviews/structured/20261025T161500Z-c2s5-remediation-verification/review.yaml")


def read(path: Path):
    return json.loads(path.read_text())


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def prepare(network_manifest: Path) -> None:
    old = yaml.safe_load(OLD.read_text())
    paths = {Path(i["path"]) for i in old["source"]["inputs"] if i["path"] != "CLAUDE.md"}
    paths.update({OLD, OLD.with_suffix(".md"), SELF, STAGE4, STAGE5, network_manifest})
    paths.update(OUT.iterdir())
    paths.update(Path(p) for p in read(network_manifest)["paths"])
    paths.update(
        Path(
            "history/records/Corynebacterium_glutamicum_Shewanella_oneidensis_Succinic_Acid_Coculture"
        ).glob("*.yaml")
    )
    paths.add(Path("scripts/adhoc/pr2054_180_input_provenance.py"))
    paths.add(Path(".temp/pr2058/staleness.json"))
    paths.add(OUT / "input-paths.json")
    # New inspection/candidate/save/post-save logs are outputs, not inputs.
    excluded = {
        "final-inspection.json",
        "candidate.json",
        "native-save.stdout",
        "native-save.stderr",
    }
    paths = {p for p in paths if p.name not in excluded and not p.name.startswith("post-save-")}
    manifest = {
        "target": TARGET,
        "paths": sorted(str(p) for p in paths),
        "boundaries": [
            "All concrete author source, authority, check and context inputs are pinned.",
            "The external GTDB source is represented by its verified byte-identical scratch copy.",
            "The new native inspection defines source.inputs and cannot hash itself.",
            "The generated candidate and subsequent validation/save/check outputs are not judgment inputs.",
            "Historical original input paths remain history; no purged scratch was recovered.",
        ],
    }
    (OUT / "input-paths.json").write_text(json.dumps(manifest, indent=2) + "\n")
    print(json.dumps({"manifest": str(OUT / "input-paths.json"), "count": len(paths)}))


def build(inspection_path: Path) -> None:
    old = yaml.safe_load(OLD.read_text())
    inspection = read(inspection_path)
    assert {i["path"] for i in inspection["source"]["inputs"]} == set(
        read(OUT / "input-paths.json")["paths"]
    )
    for item in inspection["source"]["inputs"]:
        assert digest(Path(item["path"])) == item["sha256"], item["path"]
    now = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
    result = copy.deepcopy(old)
    result.update(
        review_id=datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
        + "-corynebacterium-shewanella-current-main",
        title="Current-main refresh of the Corynebacterium–Shewanella succinate review",
        started_at="2026-11-06T15:31:42.952400Z",
        finished_at=now,
        source=inspection["source"],
        targets=inspection["targets"],
        completion="partial",
        verdict="needs_curation",
        scientific_review=False,
        summary="The added MR-1 reusable-taxon link is supported at the indexed primary publisher source tier and by current NCBI strain ancestry. All three original findings remain open: categorical roles, non-graph causal wording, and GTDB provenance. Seven snippets match the fresh abstract. Full Methods, Results, figures and authenticated supplements remain unavailable; the refresh remains partial. No canonical record was edited.",
        reviewer={
            "identity": "codex",
            "kind": "agent",
            "independence": "self_review",
            "independence_basis": "Author of this refresh; another agent performs the independent adversarial pass. No self-approval is claimed.",
        },
        scope={
            "description": "Current maintained 000294 record, its sole main delta, fresh abstract/indexed publisher sections, current MR-1 reference scope, authorities, local checks and exact predecessor lineage. Full main/SI unavailable.",
            "selection": "Only stale CommunityMech:000294 in PR #2058; other records and grouped findings are not scientifically superseded.",
            "coverage": "partial",
            "population_size": 1,
            "reviewed_target_ids": [TARGET],
        },
    )
    evidence = []

    def ev(eid, path, locator, summary, kind="validation"):
        evidence.append(
            {
                "evidence_id": eid,
                "kind": kind,
                "reference": str(path),
                "locator": locator,
                "summary": summary,
                "support": "supports",
                "accessed_at": now,
                "snapshot_sha256": digest(Path(path)),
            }
        )

    ev(
        "record",
        inspection["targets"][0]["path"],
        "Whole current record",
        "Two species, three untyped nodes and two qualified arrows; new taxonomy[1].common_taxon plus its history entry.",
        "record_content",
    )
    ev(
        "abstract",
        OUT / "pmid42203120.json",
        "PMID:42203120 / DOI:10.1016/j.biortech.2026.134987, complete abstract",
        "Reported production improvements and externally added riboflavin; transcript-based interpretation is distinct from demonstrated flux or donation direction.",
        "primary_source",
    )
    ev(
        "indexed",
        OUT / "web-indexed-primary-sections.json",
        "ScienceDirect S0960852426010692, Cell cultivation; Establishment and functional validation; Conclusion",
        "Indexed primary sections identify ATCC 13032 and MR-1 as the constructed pair; seed and conclusion snippets are truncated context, not complete Methods.",
        "primary_source",
    )
    ev(
        "schema",
        "src/communitymech/schema/communitymech.yaml",
        "FunctionalRoleEnum; TaxonomicComposition.common_taxon; ecological_state",
        "Roles retain literal meanings, common_taxon shares organism reference annotations, and ecological_state is optional.",
        "record_content",
    )
    ev(
        "taxonomy",
        OUT / "ncbi-taxonomy.xml",
        "Taxa 1718, 70863, 196627 and 211586",
        "Current NCBI verifies species and exact parent-stock strains; MR-1 is a strain under S. oneidensis 70863.",
        "authority",
    )
    ev(
        "reusable",
        "kb/taxa/Shewanella_oneidensis_MR1.yaml",
        "Identity and all five gene annotation blocks",
        "The referenced MR-1 record includes other-study electrochemical, bioleaching and computational annotations. None is focal evidence for succinate-coculture electron direction, a solid acceptor or K1 assay identity.",
        "record_content",
    )
    ev(
        "gtdb",
        OUT / "gtdb-replay-explicit.stdout",
        "Current community-mode replay with explicit kg-microbe location",
        "Species mappings reproduce: C. glutamicum 0.99/159; S. oneidensis name fallback 1.0/3. Snapshot identity and mtime do not establish a release or build date.",
        "validation",
    )
    ev(
        "gtdb-rows",
        OUT / "gtdb-exact-rows.json",
        "Whole snapshot row scan; exact IDs and candidate stock rows",
        "No exact 70863 row in this snapshot; 1718 is exact, 196627 gives 1.0/15 and 211586 gives 1.0/3. These counts are crosswalk support, not study abundance.",
        "validation",
    )
    ev(
        "snippets",
        OUT / "snippet-audit.json",
        "All seven canonical excerpt selectors and hashes",
        "All seven match the fresh abstract after Unicode/whitespace normalization; exact text match does not establish causal entailment.",
        "validation",
    )
    ev(
        "delta",
        OUT / "main-record-diff.txt",
        "Frozen e117e3d to main 5086593a record diff",
        "The only community additions are the common_taxon link and its history event; no measured outcome or graph changed.",
        "validation",
    )
    ev(
        "lineage",
        STAGE5,
        "c2s4-shewanella-common-taxon-linkage-gap",
        "The grouped historical resolved disposition is context only. This refresh confirms only 000294 linkage and does not supersede 000288 or the reusable-record target.",
        "prior_review",
    )
    ev(
        "access",
        OUT / "elsevier.xml",
        "Anonymous public Elsevier response",
        "Only coredata was returned; direct publisher retrieval was an access-error page. No full Methods, figures, tables, authenticated SI or complete bibliography was inspected.",
        "primary_source",
    )
    ev(
        "checks",
        OUT / "focused-checks.json",
        "Eight current focused commands",
        "All eight commands returned 0; the original bundle validation is a native contract check, not fresh scientific approval.",
        "validation",
    )
    ev(
        "network",
        OUT / "network-inputs.json",
        "Root's shared read-only current corpus diagnostic receipts",
        "Actual corpus diagnostic outputs are pinned separately; warnings remain contextual and are not hidden by a passing focused record gate.",
        "validation",
    )
    result["checks"] = []
    for row in read(OUT / "focused-checks.json"):
        result["checks"].append(
            {
                "check_id": row["label"],
                "name": row["label"],
                "status": "passed" if row["exit_code"] == 0 else "failed",
                "required": True,
                "summary": f"Current command exit {row['exit_code']}; stdout/stderr pinned.",
                "target_ids": [TARGET],
                "command": " ".join(row["command"]),
                "exit_code": row["exit_code"],
                "expected_exit_code": 0,
                "evidence_ids": ["checks"],
                "scope_note": "Current focused command; no historical output replayed as a fresh run.",
            }
        )
    for row in read(OUT / "network-inputs.json")["checks"]:
        result["checks"].append(
            {
                "check_id": row["check_id"],
                "name": row["name"],
                "status": "failed" if row["exit_code"] else "passed",
                "required": False,
                "summary": row["summary"],
                "target_ids": [TARGET],
                "command": row["command"],
                "exit_code": row["exit_code"],
                "expected_exit_code": 0,
                "evidence_ids": ["network"],
                "scope_note": "Shared current full-corpus diagnostic executed by root; not a focal-record failure or a scientific review.",
            }
        )
    result["assessments"] = []

    def assess(aid, area, summary, details, ids, outcome="supported"):
        result["assessments"].append(
            {
                "assessment_id": aid,
                "area": area,
                "topic": aid.replace("-", " "),
                "outcome": outcome,
                "summary": summary,
                "details": details,
                "target_ids": [TARGET],
                "evidence_ids": ids,
            }
        )

    assess(
        "current-identity-and-link",
        "identity",
        "The added MR-1 link is supported within explicit source limits.",
        "Current species 1718 and 70863 remain appropriate. Indexed primary Establishment text names ATCC 13032 and MR-1, and live NCBI places strain 211586 beneath species 70863. common_taxon 000001 therefore refers to the matching stock. K1 remains an ldhA-deleted derivative; neither this linkage nor other-study MR-1 gene annotations assign every assay to K1 or establish the focal mechanism. No catalogue growth protocol is imported.",
        ["record", "indexed", "taxonomy", "reusable", "delta"],
    )
    assess(
        "roles",
        "scope",
        "The original categorical-role finding remains open.",
        "PRIMARY_PRODUCER means autotrophy, not industrial succinate production. Accessible focal evidence does not establish ELECTROGEN's solid extracellular acceptor or ELECTRON_DONOR's donation direction. Optional roles may be omitted while keeping source-qualified electroactivity; no substitute role is required.",
        ["abstract", "schema", "reusable"],
        "concern",
    )
    assess(
        "non-graph",
        "evidence",
        "The original prose-scope finding remains open.",
        "Restore the source's not-markedly qualifier for glucose consumption, identify flux redistribution as transcript-based interpretation, and qualify the Shewanella transfer/redox note. Measured production gains remain valid at their separate comparison scopes.",
        ["abstract", "record", "indexed"],
        "concern",
    )
    record = yaml.safe_load(Path(inspection["targets"][0]["path"]).read_text())
    node_details = [
        "Community-level externally supplied 0.1 mM riboflavin response; both species participate. SUPPORT/IN_VITRO concerns the additive intervention, not endogenous mediator secretion or directed transfer.",
        "Source-only PAIRWISE C. glutamicum transcript response; PARTIAL/IN_VITRO supports interpretation without direct carbon/electron flux. No recipient, obligatory syntrophy or unreported K1 assay assignment is added.",
        "Community-level production outcome, both species: separate parent 0.169 g/g and 45.65% comparison from K1 0.686 g/g and up to 23.4%. SUPPORT/IN_VITRO concerns measured output, not a uniquely demonstrated electron-transfer pathway.",
    ]
    for i, node in enumerate(record["ecological_interactions"]):
        assess(
            f"node-{i}",
            "graph",
            f"Retain {node['name']}.",
            f"ecological_interactions[{i}]: {node_details[i]} Exact evidence selector/hashes are in the seven-excerpt audit; PMID:42203120 abstract is the inspected source.",
            ["record", "abstract", "snippets"],
        )
        for j, edge in enumerate(node.get("downstream", [])):
            assess(
                f"edge-{i}-{j}",
                "graph",
                "Retain the explicitly qualified causal arrow.",
                f"ecological_interactions[{i}].downstream[{j}] from {node['name']} to {edge['target']}: {edge['description']} Accessible abstract does not supply selective blockade, rescue or direct flux proving this mediation.",
                ["record", "abstract"],
            )
    assess(
        "grounding",
        "grounding",
        "Current ontology identities and mapping results remain consistent; provenance wording still needs repair.",
        "Focused term checks pass. C. glutamicum species exact-ID 0.99/159 and S. oneidensis name route 1.0/3 reproduce; exact stock candidates 196627 and 211586 remain separate. The full snapshot SHA is pinned, release/build remains unknown, and filesystem mtime is not a build date.",
        ["taxonomy", "gtdb", "gtdb-rows", "checks"],
        "concern",
    )
    assess(
        "cultivation-and-resources",
        "completeness",
        "Production protocol and focal deposited data remain incompletely assessed.",
        "Anaerobic glucose-associated production and external riboflavin are supported. Indexed 20 mL BHI seed preparation and 24 h transfer cannot supply production medium, temperature, pH, vessel, gas regimen or mode; indexed 36 h conclusion context is bounded. No complete main/SI or focal accession audit was possible. Reusable assembly/protein IDs are reference context, not focal experimental deposits.",
        ["abstract", "indexed", "access", "reusable"],
        "unknown",
    )
    assess(
        "lineage-context",
        "provenance",
        "Only the original single-record scientific findings receive new occurrences.",
        "The existing c2s4 grouped linkage finding and its resolved Stage 5 disposition remain intact; only the 000294 link is checked here. Other grouped targets and issue states are not reassessed. The historic graph repair remains qualified; no old review, record, cache or append-only history was rewritten.",
        ["lineage", "delta", "record"],
    )
    assess(
        "checks-and-inputs",
        "provenance",
        "Current checks and every concrete author input are frozen.",
        "Eight focused commands pass. An initial optional GTDB replay failed because the nested worktree could not discover kg-microbe; the documented explicit-directory replay then succeeded, and both receipts remain. Corpus diagnostics retain their actual warning exits. New inspection/candidate/post-save outputs are excluded from their own input set to avoid self-reference. Partial source access prevents complete scientific status.",
        ["checks", "network", "gtdb", "access"],
    )
    metrics = copy.deepcopy(old["assessments"][-1])
    metrics["evidence_ids"] = ["record", "checks", "network"]
    metrics["details"] = (
        "Recomputed from current record: required-field/roles block 50, environment 5, three nodes 10, medium 10, node metabolites 5 = 80. Three node evidence items / three nodes = 1 average; 2 P2 and 1 P3, network COMPLETE, raw quality 103 capped 100. Literal scoring does not validate the disputed roles or remove access limits."
    )
    result["assessments"].append(metrics)
    result["assessments"][0]["dimensions"] = [
        {
            "name": "source_tier",
            "value": "Fresh complete abstract; indexed primary sections; full main/SI unavailable",
            "definition": "Actual reviewed primary-source scope",
            "evidence_ids": ["abstract", "indexed", "access"],
        },
        {
            "name": "strain_scope",
            "value": "ATCC 13032 / MR-1 parent stocks; reported C. glutamicum K1 derivative",
            "definition": "Indexed parent-stock identity remains separate from unresolved assay-specific derivative use",
            "evidence_ids": ["indexed", "taxonomy"],
        },
        {
            "name": "community_scope",
            "value": "ENGINEERED, SYNTHETIC laboratory coculture",
            "definition": "Neither a natural assemblage nor a universal species interaction",
            "evidence_ids": ["record", "abstract"],
        },
        {
            "name": "culture_context",
            "value": "Anaerobic glucose-associated production; seed protocol is a separate indexed context",
            "definition": "Do not extrapolate truncated seed conditions to the production assay",
            "evidence_ids": ["abstract", "indexed"],
        },
    ]
    for finding in result["findings"]:
        finding["previous_occurrences"] = finding.get("previous_occurrences", []) + [
            {
                "repository": result["repository"],
                "review_id": old["review_id"],
                "finding_id": finding["finding_id"],
            }
        ]
        finding["evidence_ids"] = [
            "record",
            "abstract",
            "schema",
            "indexed",
            "reusable",
            "gtdb",
            "gtdb-rows",
        ]
        finding["ownership_note"] = (
            "The focal community record owns this still-open repair. This refresh neither edits canonical data nor closes any curation issue."
        )
    # Preserve all action acceptance, repairing only spacing in inherited prose.
    replacements = {
        "ATCC13032": "ATCC 13032",
        "separate0.169": "separate 0.169",
        "supplied0.1": "supplied 0.1",
        "up-to23.4": "up-to 23.4",
        "Any36": "Any 36",
        "of45.65": "of 45.65",
        "glutamicum1718": "glutamicum 1718",
        "oneidensis70863": "oneidensis 70863",
        "species70863": "species 70863",
        "SHA256761": "SHA256 761",
        "node1": "node 1",
    }
    for action in result["actions"]:
        for i, check in enumerate(action["acceptance_checks"]):
            for before, after in replacements.items():
                check = check.replace(before, after)
            action["acceptance_checks"][i] = check
    result["evidence"] = evidence
    result["limitations"] = [
        "Only the complete fresh abstract and bounded indexed primary sections were available. Direct publisher retrieval failed and the anonymous API supplied coredata; no full Methods, Results, figures, tables, authenticated SI or full bibliography was inspected.",
        "The stock link is supported at indexed source tier. K1 assay assignment, directed electron transfer, solid-acceptor evidence, direct flux and selective mediation remain unresolved. Other-study reusable annotations are not focal proof.",
        "Seed preparation is distinct from production; indexed conclusion timing is not a recovered full protocol. A historical Highlight/Abstract attribution discrepancy is not silently harmonized, and missing accessible data is not global absence.",
        "Fresh whole-snapshot GTDB replay verifies mapping results but not an upstream release/build. Optional fields, including ecological_state, are not made mandatory by a rubric score.",
        "Only 000294 is scientifically refreshed. Grouped linkage findings retain their full original target scopes and dispositions. Root and independent reviewers own issue-state checks and final adversarial approval.",
    ]
    result["notes"] = [
        "Refresh for stale-review issue #2569. Original bundle remains immutable; historical local-source provenance limitation is separately tracked by #2570.",
        "All local input bytes used by this author are included through native --input, including public source bodies/receipts, initial inspection, mapping copy, checks, guidance and this frozen JSON builder. No YAML writer is introduced.",
    ]
    result["related_reviews"] = [
        {
            "repository": result["repository"],
            "review_id": old["review_id"],
            "relationship": "Immutable current-main successor preserving all three open finding keys and all four actions after the MR-1 common_taxon addition.",
        }
    ]
    result["tags"] = ["pr2058", "staleness-refresh", "current-main", "partial-source-access"]
    (OUT / "candidate.json").write_text(json.dumps(result, indent=2) + "\n")
    print(
        json.dumps(
            {
                "candidate": str(OUT / "candidate.json"),
                "review_id": result["review_id"],
                "inputs": len(result["source"]["inputs"]),
            }
        )
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("mode", choices=["prepare", "build"])
    parser.add_argument("path", type=Path)
    args = parser.parse_args()
    if args.mode == "prepare":
        prepare(args.path)
    else:
        build(args.path)
