"""Build the PR 2061 record 397 refresh for the native immutable saver.

Only scratch JSON is written. Public retrievals and focused validators were
run before this builder. Their concrete inputs are captured, without circular
pins for the final native inspection, candidate, or subsequent validation.
"""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

import yaml

OUT = Path(".temp/pr2061/refresh397")
SELF = Path("scripts/adhoc/pr2061_397_refresh.py")
OLD = Path(
    "reviews/structured/20261022T043046Z-defined-three-strain-nitrifying-record-review/review.yaml"
)
TARGET = "CommunityMech:000397"
REPO = "CultureBotAI/CommunityMech"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read(path: Path):
    return json.loads(path.read_text())


def prepare() -> None:
    old = yaml.safe_load(OLD.read_text())
    paths = {Path(i["path"]) for i in old["source"]["inputs"] if i["path"] != "CLAUDE.md"}
    paths.update({OLD, OLD.with_suffix(".md"), SELF})
    paths.update(p for p in OUT.rglob("*") if p.is_file())
    paths.update(Path(".temp/pr2061/root-checks").glob("initial-checks.json"))
    for label in ("native", "contracts", "audit-network", "check-network-quality"):
        paths.update(Path(".temp/pr2061/root-checks").glob(label + ".*"))
    paths.update(
        Path("history/records/Defined_ThreeStrain_Organic_Nitrogen_Nitrifying_Community").glob(
            "*.yaml"
        )
    )
    paths.update(Path(row["path"]) for row in read(OUT / "lineage-context.json"))
    paths.update(
        {
            Path("reports/causal_graph_review/decisions/20261031-c4s5-review-remediation.yaml"),
            Path("src/communitymech/ontology_adapters.py"),
            Path("scripts/adhoc/pr2058_294_refresh.py"),
            Path(".temp/pr2061/staleness.json"),
            OUT / "input-paths.json",
        }
    )
    excluded = {
        "final-inspection.json",
        "candidate.json",
        "native-save.stdout",
        "native-save.stderr",
    }
    paths = {
        p
        for p in paths
        if p.name not in excluded
        and not p.name.startswith("post-save-")
        and not p.name.startswith("candidate-validation")
    }
    manifest = {
        "targets": [TARGET],
        "paths": sorted(str(p) for p in paths),
        "boundaries": [
            "All concrete local source, authority, check, history and predecessor inputs used by the author are pinned.",
            "The external GTDB crosswalk is represented by its verified byte-identical local copy.",
            "The initial inspection informed assessment and is pinned; the final native inspection defines source.inputs and cannot hash itself.",
            "The generated candidate, native save and subsequent validation outputs are not inputs to the saved judgment.",
            "Historical purged scratch paths are retained only in the immutable predecessor; no recovery or current-use claim is made.",
            "Ignored files were included in scoped history/review/reusable-taxon discovery; nonmatching review files were discovery candidates, not scientific inputs.",
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
    owner = copy.deepcopy(old["targets"][0]["owner_paths"])
    evidence = []

    def ev(eid, path, locator, summary, kind="validation", support="supports"):
        evidence.append(
            {
                "evidence_id": eid,
                "kind": kind,
                "reference": str(path),
                "locator": locator,
                "summary": summary,
                "support": support,
                "accessed_at": now,
                "snapshot_sha256": digest(Path(path)),
            }
        )

    ev(
        "record",
        old["targets"][0]["path"],
        "Whole current maintained YAML",
        "Three defined NBRC stocks, one aggregate conversion node, no downstream arrows; only roles, abundance categories and October 31 history changed.",
        "record_content",
    )
    ev(
        "abstract",
        OUT / "sources/epmc.json",
        "PMID:42668143 / DOI:10.1093/bbb/zbag131; full MED abstract and metadata",
        "The three stocks, selected-condition nitrate endpoint and relative-abundance association are reported; carbon fixation is not a focal reported measurement.",
        "primary_source",
    )
    ev(
        "publisher",
        OUT / "sources/publisher-web.txt",
        "Public publisher Abstract and access notice; web-tool response captured locally",
        "The article identity matches. The public page exposes abstract, graphical abstract and supplementary link but states no access to the main article.",
        "primary_source",
    )
    ev(
        "supplement",
        OUT / "sources/supplement.pdf",
        "All three physical PDF pages: Figures S1, S2 and S3",
        "S1 repeat/refeeding, S2 Polypepton NF and delayed-inoculation arms, and S3 separate-isolate media/temperature tests were read and visually checked. These do not supply the complete focal protocol.",
        "primary_source",
    )
    ev(
        "graphical",
        OUT / "sources/graphical.jpeg",
        "Named three-stock conversion schematic and nitrogen/estimated-ratio time course",
        "The schematic supports organic-N transformation and sequential ammonium/nitrite utilization. It neither depicts carbon fixation nor establishes equal or time-invariant cell fractions.",
        "primary_source",
    )
    ev(
        "stock-carbon",
        OUT / "sources/nedo-carbon-stocks.pdf",
        "Printed slide 34, PDF physical page 35: NITE CO2-fixing stock list",
        "NBRC 14298 and 14297 appear in NITE's CO2-fixing-stock list. This is background stock-capability context, not measured carbon flux in the 2026 coculture.",
        "authority",
    )
    for n in (15713, 14298, 14297):
        ev(
            f"stock-{n}",
            OUT / f"sources/nbrc-{n}.html",
            f"NBRC {n} exact stock catalogue",
            "The stock identity resolves. Collection-maintenance conditions and stock sequence links are not the focal community protocol or study deposits.",
            "authority",
        )
    ev(
        "taxonomy",
        OUT / "sources/taxonomy.xml",
        "Fresh NCBI taxonomy efetch entries 1455, 915 and 913",
        "All three species labels resolve; Bacillus badius is a synonym of Pseudobacillus badius. Species identity does not certify an exact experimental genome.",
        "authority",
    )
    ev(
        "gtdb",
        OUT / "gtdb.stdout",
        "Actual current community-mode lookup against the locally copied crosswalk",
        "Pseudobacillus badius resolves by exact species ID at 1.0/26, Nitrosomonas europaea by species name at 1.0/2, and Nitrobacter winogradskyi_A by ID at 0.88/8. Existing upstream release/build wording is not established by a filesystem mtime.",
        "authority",
    )
    ev(
        "crosswalk",
        OUT / "gtdb-copy.json",
        "Source/copy SHA256 equality",
        "The source and local copy both hash to 761d5537a7edb4b0133e88e7bbc85570cf3cb6f2555b9f9ce6cca3e1056a0ddd; no new release date is inferred.",
    )
    ev(
        "schema",
        "src/communitymech/schema/communitymech.yaml",
        "AbundanceEnum, FunctionalRoleEnum, community, interaction and optional context slots",
        "ABUNDANT is qualitative major-member prominence, PRIMARY_PRODUCER means carbon fixation, and optional fields do not become mandatory merely because the schema permits them.",
        "authority",
    )
    ev(
        "snippets",
        OUT / "snippet-audit.json",
        "All 18 canonical snippet placements",
        "Seventeen placements match the fresh abstract and the remaining placement is exact DOI metadata; all 18 match the committed abstract cache. Lexical agreement does not prove the newly added carbon-fixation role.",
    )
    ev(
        "predecessor",
        OLD,
        "Original two findings and three actions / eight acceptance checks",
        "Both original finding keys and every original acceptance check are retained; the historical source-access limits are not rewritten.",
        "prior_review",
    )
    ev(
        "lineage",
        OUT / "lineage-context.json",
        "Ignored-inclusive discovery of exact 397 finding occurrences",
        "The Cycle 4 presence finding has its own resolved successor. This observation preserves that narrow presence disposition while assessing the new annotation's evidence separately.",
        "prior_review",
    )
    ev(
        "history",
        "history/records/Defined_ThreeStrain_Organic_Nitrogen_Nitrifying_Community/2026-10-31T234500Z-antigravity-2095.yaml",
        "events[0] details and matching canonical curation_history[3]",
        "The history accurately records the added enum values; its focal PMID citation does not supply separate carbon-fixation proof. No old history is edited.",
        "record_content",
    )
    ev(
        "delta",
        OUT / "target-diff.patch",
        "Original PR head to integrated current-main target diff",
        "Five role assignments, three abundance categories and one inline history event were added; all original experimental claims and evidence snippets are unchanged.",
    )
    ev(
        "reading",
        OUT / "source-reading.json",
        "Author's actual source reading and bounded-access notes",
        "Author read the complete current record, predecessor, fresh abstract, all three SI pages, graphical abstract, exact stock/NCBI authority, relevant NITE slide and local checks. This is not independent approval.",
    )
    ev(
        "checks",
        OUT / "checks/focused-checks.json",
        "Eight actual focused command/exit/stdout/stderr receipts",
        "All eight focused checks exited 0. They do not establish scientific completion.",
    )
    ev(
        "corpus",
        ".temp/pr2061/root-checks/initial-checks.json",
        "Parent-run current full-corpus diagnostics and native controls",
        "Both network diagnostics returned exit 1 with 48 warnings across 17 of 510 records and zero errors; these are nonrequired context. The author reuses the recorded parent run rather than claiming to rerun it.",
    )
    checks = []
    for row in read(OUT / "checks/focused-checks.json"):
        eid = "check-" + row["name"]
        ev(
            eid,
            OUT / "checks" / (row["name"] + ".json"),
            "Actual focused command and output paths",
            f"Actual exit {row['exit_code']}; output artifacts are independently pinned.",
        )
        checks.append(
            {
                "check_id": row["name"],
                "name": row["name"],
                "status": "passed" if row["exit_code"] == 0 else "failed",
                "required": True,
                "summary": f"Actual current command exit {row['exit_code']}.",
                "target_ids": [TARGET],
                "command": " ".join(row["command"]),
                "exit_code": row["exit_code"],
                "expected_exit_code": 0,
                "evidence_ids": [eid],
                "scope_note": "Focused record/history; cache-name preflight is corpus-wide.",
            }
        )
    for name in ("audit-network", "check-network-quality"):
        checks.append(
            {
                "check_id": name,
                "name": name,
                "status": "failed",
                "required": False,
                "summary": "Shared current corpus run: 48 warnings in 17 of 510 records, zero errors, actual exit 1; existing warning baseline retained.",
                "command": "just --no-dotenv " + name,
                "exit_code": 1,
                "expected_exit_code": 0,
                "evidence_ids": ["corpus"],
                "scope_note": "Parent-owned full corpus run, not a new author invocation.",
            }
        )
    assessments = []

    def assess(aid, area, topic, outcome, summary, eids, details):
        assessments.append(
            {
                "assessment_id": aid,
                "area": area,
                "topic": topic,
                "outcome": outcome,
                "summary": summary,
                "target_ids": [TARGET],
                "evidence_ids": eids,
                "details": details,
            }
        )

    assess(
        "identity",
        "identity",
        "Three-stock laboratory model",
        "supported",
        "The three source-named NBRC stocks remain a defined engineered laboratory community.",
        ["record", "abstract", "taxonomy", "stock-15713", "stock-14298", "stock-14297"],
        "Retain SYNTHETIC origin, ENGINEERED state and BIOTECHNOLOGY category. Source Bacillus badius and canonical Pseudobacillus badius refer to the same species; NBRC stock descriptors are distinct from species/genome classification. The soil analogy in the graphical abstract is not a natural origin or a live host experiment.",
    )
    assessments[-1]["dimensions"] = [
        {
            "name": "taxon_scope",
            "value": "NBRC 15713, 14298 and 14297",
            "definition": "Three exact collection stocks within their current NCBI species; no experimental-genome reassignment.",
            "evidence_ids": ["taxonomy", "stock-15713", "stock-14298", "stock-14297"],
        },
        {
            "name": "experimental_setting",
            "value": "Selected organic-nitrogen laboratory coculture",
            "definition": "Engineered model; source diagram's soil comparison is not the culture environment.",
            "evidence_ids": ["abstract", "graphical"],
        },
    ]
    assess(
        "node-0",
        "graph",
        "Sequential organic-nitrogen conversion",
        "supported",
        "Retain the single community-level CROSS_FEEDING node and its bounded selected-condition outcome.",
        ["record", "abstract", "graphical", "supplement", "snippets"],
        "Exact selector ecological_interactions[0]. All three participating taxa are canonical members, no pairwise source/target or downstream arrows are encoded. The two SUPPORT / IN_VITRO snippets are the abstract's construction and endpoint statements, hashes 0a1d0d1dfaa1379ba9df48f9ff7cde142aa2368507165e66cab0b42214c443c4 and 4faa31e56824f4e0abc9b81d22331b4d573b7b3e6deb98a8b1b0782dd5402b0a. Graphical arrows assign organic N to ammonium to nitrite to nitrate at the named functional stages. Retain aggregate sequential exchange without inferring donor-resolved flux, obligate reciprocity, necessity or all-substrate success. GO:0019329 ammonia oxidation denotes one component; ammonium/nitrite/nitrate CHEBI ions retain mg-N/L nitrogen-equivalent units.",
    )
    assess(
        "new-annotations",
        "evidence",
        "Added roles and qualitative abundance",
        "concern",
        "Nitrogen roles and qualitative major-partner prominence are supportable; the carbon-fixation role needs its own bounded evidence.",
        ["delta", "abstract", "graphical", "supplement", "stock-carbon", "schema", "history"],
        "PRIMARY_DEGRADER for B. badius fits the organic-N/Polypepton transformation and CROSS_FEEDER for the nitrifiers fits successive intermediate utilization. ABUNDANT is accepted only as qualitative prominence of these three central partners, not a percentage band, equal proportions, a fixed inoculum ratio or stability across days/arms. The graphical estimated-ratio time series and S1 absolute counts do not establish those stronger claims. PRIMARY_PRODUCER specifically means fixes carbon; the local taxon evidence currently quotes membership and nitrifier abundance association from the focal abstract, which does not make that assertion. NITE's exact-stock list supports background capacity, not focal community carbon flux; this narrows the new finding to local evidence/provenance rather than false organism identity or disproven physiology.",
    )
    assess(
        "cultivation",
        "completeness",
        "Supplementary context and unresolved main protocol",
        "concern",
        "The original supplementary-cultivation finding remains open with all three acceptance checks.",
        ["supplement", "publisher", "predecessor"],
        "S2 physical page 2 supports 2 g/L Polypepton NF and separately the nitrifiers' inoculation two days after B. badius. S1 physical page 1 supports repeated culture using post-nitrification cells and day 3 feeding. S3 physical page 3 concerns separate nitrifier cultures in HEPES/Boon media over 20–37 degrees C; it cannot supply a common community temperature. Main Figure 4(d), basal recipe, inoculum ratio, atmosphere and vessel remain unread or unresolved. Preserve the dated organic_nitrogen_cultivation_details KNOWLEDGE_GAP and trace later recovery; do not treat a schematic flask or collection maintenance recipe as the experimental protocol.",
    )
    assessments[-1]["dimensions"] = [
        {
            "name": "medium",
            "value": "S2 Polypepton NF 2 g/L; basal community formulation unresolved",
            "definition": "Arm-specific supplementary condition, not a universal recipe or proven mapping to the 56 mg-N/L abstract arm.",
            "evidence_ids": ["supplement"],
        },
        {
            "name": "environmental_context",
            "value": "ENVO:01001405 laboratory environment",
            "definition": "No mandatory host or soil annotation is inferred from optional current slots or an illustrative soil comparison.",
            "evidence_ids": ["record", "graphical", "schema"],
        },
    ]
    assess(
        "gtdb",
        "grounding",
        "Species mapping and immutable provenance",
        "concern",
        "The original mapping-completion and provenance finding remains open with exact existing acceptance.",
        ["gtdb", "crosswalk", "taxonomy", "predecessor"],
        "Fresh community-mode lookup reproduces all three mapping routes and denominators in the original action. Retain the Nitrobacter name difference as a name comparison, not a new taxonomic event. The copied crosswalk is byte-identical to the external source; its local mtime is not an upstream release/build date.",
    )
    assess(
        "resources",
        "evidence",
        "Publication and source/cache boundaries",
        "supported",
        "Both publication identifiers and all 18 existing snippets remain valid at their actual source tiers.",
        ["abstract", "publisher", "snippets", "reading"],
        "No full main-paper or raw dataset review is claimed. The cache is plain PubMed-format abstract text with no false full-text content_type claim. The inspected public abstract/SI/graphic declares no focal data deposit; main availability is unknown. Stock genome links are not silently promoted to focal deposits. No separate cache repair is inferred from successful fresh-source access. iModulonDB is not applicable because no gene, locus, regulator, pathway dataset or expression module is named in this target.",
    )
    assess(
        "lineage",
        "provenance",
        "Exact predecessor retention and Cycle 4 context",
        "supported",
        "Both original open findings are explicitly continued; the separate Cycle 4 missing-field disposition is not reopened or superseded.",
        ["predecessor", "lineage", "history", "delta"],
        "The October 31 enum additions satisfy the historical field-presence observation. This refresh does not retire, reopen or scientifically re-review other targets in the Cycle 4 reports. It separately distinguishes field presence from claim-local carbon-fixation support. All four history sidecars and inline events remain immutable; a later authorized curation must append its own exact source/claim scope.",
    )
    assess(
        "native",
        "schema",
        "Current focused validation and corpus context",
        "supported",
        "Eight focused checks passed; current shared network warnings remain explicit.",
        ["checks", "corpus", "schema"],
        "Passing schema, strict, labels, references, GTDB/domain, history and cache naming checks do not complete an access-limited scientific review. The historical 44-warning/477-record baseline is not reused as current; current parent receipts show 48 warnings across 17 of 510 records and no errors.",
    )
    assess(
        "access",
        "scope",
        "Actual author reading and unavailable main",
        "unknown",
        "The refresh remains partial and scientific_review is false.",
        ["reading", "publisher", "supplement"],
        "The accessible abstract, all three SI pages, graphical abstract and relevant authority pages were read. Main Methods/results, main figures and full treatment comparisons remain unavailable through the bounded public routes used. No paid access, contact, experiments, digitization or raw-data reanalysis occurred.",
    )
    assess(
        "metrics",
        "completeness",
        "Literal native metrics",
        "supported",
        "Completeness is 65; raw validation quality is 129 and capped quality is 100.",
        ["record", "schema", "corpus", "checks"],
        "These are structural rubric values, not evidence strength. Adding roles raises the literal required-field block while the new local evidence gap remains open.",
    )
    assessments[-1]["metrics"] = [
        {
            "name": "completeness",
            "value": 65,
            "unit": "points",
            "minimum": 0,
            "maximum": 100,
            "definition": "Required field/role block 50 + environment 5 + external resources 5 + interaction metabolites 5; fewer than 3 factors/nodes and absent growth_media/datasets add 0.",
        },
        {
            "name": "validation_quality",
            "value": 100,
            "unit": "points",
            "minimum": 0,
            "maximum": 100,
            "definition": "100 - 0 P1*50 - 0 P2*10 - 3 P3*2 + 20*min((2 evidence/1 node)/2,1) + 15 structural COMPLETE = 129 raw, capped at 100. One node, zero arrows; the corpus network auditor reports no focal issue.",
        },
    ] + [
        {
            "name": key,
            "value": val,
            "unit": "findings",
            "definition": "Native severity count in this scoped successor.",
        }
        for key, val in (("P1", 0), ("P2", 0), ("P3", 3), ("P4", 0))
    ]
    findings = copy.deepcopy(old["findings"])
    for item in findings:
        item["previous_occurrences"] = [
            {"repository": REPO, "review_id": old["review_id"], "finding_id": item["finding_id"]}
        ]
        item["evidence_ids"] = (
            ["supplement", "publisher", "reading"]
            if item["finding_id"] == "cultivation-context"
            else ["gtdb", "crosswalk", "taxonomy"]
        )
        item["ownership_note"] = (
            "The maintained record owns future authorized curation; this successor preserves the exact original finding and all original action acceptance checks."
        )
    findings.append(
        {
            "finding_id": "carbon-role-evidence",
            "issue_key": "cm-000397-carbon-role-evidence-scope",
            "category": "evidence",
            "severity": "minor",
            "native_severity": "P3",
            "normalization_reason": "Bounded claim-local evidence/provenance gap: exact-stock authority supports background capacity, but the focal nitrogen-study evidence does not itself establish carbon fixation in this community. No identity failure or disproven physiology is asserted.",
            "rule_id": "review-checklist.claim-specific-support-and-context",
            "status": "open",
            "certainty": "confirmed",
            "title": "Separate background carbon-fixation capacity from focal nitrogen evidence",
            "description": "taxonomy[1] and taxonomy[2] now include PRIMARY_PRODUCER, defined as carbon fixation, while their local PMID:42668143 evidence quotes only membership and nitrifier abundance association. The accessible focal abstract, graphical abstract and SI do not report carbon-fixation flux. NITE's exact-stock CO2-fixing list supports background capacity, which requires its own source and scope if retained; it is not a focal in-vitro carbon-flux result.",
            "target_ids": [TARGET],
            "field_paths": [
                "taxonomy[1].functional_role",
                "taxonomy[1].evidence",
                "taxonomy[2].functional_role",
                "taxonomy[2].evidence",
            ],
            "evidence_ids": [
                "record",
                "abstract",
                "graphical",
                "supplement",
                "stock-carbon",
                "schema",
            ],
            "owner_paths": owner,
        }
    )
    actions = copy.deepcopy(old["actions"])
    actions.append(
        {
            "action_id": "scope-carbon-role-evidence",
            "description": "Support or qualify the two optional PRIMARY_PRODUCER annotations without conflating background capacity and focal measured function.",
            "finding_ids": ["carbon-role-evidence"],
            "target_ids": [TARGET],
            "owner_paths": owner,
            "acceptance_checks": [
                "For taxonomy[1] NBRC 14298 and taxonomy[2] NBRC 14297, inspect appropriate exact-stock physiological evidence and attach an allowed stable reference, exact snippet and honest evidence tier to any retained carbon-fixation role; otherwise omit or qualify the optional role without declaring the organisms incapable of carbon fixation.",
                "Explicitly distinguish source-backed background stock capability from carbon fixation measured in the PMID:42668143 community. The inspected NITE stock list is printed slide 34 / PDF physical page 35; it cannot certify coculture carbon flux. Do not relabel the focal nitrogen-conversion abstract as carbon-fixation evidence.",
                "Retain supported PRIMARY_DEGRADER/CROSS_FEEDER nitrogen roles and the bounded three-member identity. ABUNDANT remains qualitative major-partner prominence; infer no percentage threshold, equal proportions, fixed inoculum ratio or abundance stable across treatment/time.",
                "For any separately authorized repair, append exact source/scope history while preserving the October 31 event, then run focused schema/strict/terms/references/GTDB/domain/history checks and regenerate/check derived docs. Keep unavailable main-protocol details explicitly unresolved.",
            ],
        }
    )
    result = {
        "schema_version": "1.0.0",
        "review_id": datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
        + "-defined-three-strain-nitrifying-current-main",
        "kind": "record",
        "repository": REPO,
        "title": "Current-main refresh of the defined three-strain nitrifying community review",
        "started_at": read(OUT / "started.json")["started_at"].replace("+00:00", "Z"),
        "finished_at": now,
        "reviewer": {
            "identity": "codex",
            "kind": "agent",
            "independence": "self_review",
            "independence_basis": "Author of this refresh; a separate agent performs the independent adversarial pass. This document claims no independent approval of itself.",
        },
        "skill": "review-yaml-record",
        "completion": "partial",
        "verdict": "needs_curation",
        "scientific_review": False,
        "summary": "Current-main roles and abundance annotations were reassessed against fresh abstract, public SI/graphical evidence and exact stock authorities. Both original findings remain open with their full acceptance; one minor local-evidence finding separates carbon-fixation capacity from focal nitrogen-study evidence. ABUNDANT is retained as qualitative prominence, not measured fraction. Eight focused checks pass, but the main manuscript remains inaccessible and scientific completion is false.",
        "source": inspection["source"],
        "targets": inspection["targets"],
        "scope": {
            "description": "Whole current maintained record, exact main delta, original findings/actions, accessible primary/SI/graphic, relevant current stock/taxonomic authorities, history and native controls; main manuscript unavailable.",
            "selection": "Only stale CommunityMech:000397 in PR #2061; other records and other review finding heads are not superseded.",
            "coverage": "partial",
            "population_size": 1,
            "reviewed_target_ids": [TARGET],
        },
        "checks": checks,
        "evidence": evidence,
        "assessments": assessments,
        "findings": findings,
        "actions": actions,
        "limitations": copy.deepcopy(old["limitations"])
        + [
            "The NITE/NEDO stock list is a background capability authority, not a substitute for focal community carbon-flux evidence. Exact stock physiology should be sourced and scoped before adding local support.",
            "The author reused parent-owned current corpus diagnostics with their true exit codes. This refresh is author work and is separately reviewed; no canonical record, cache, history or scientific status was changed.",
        ],
        "related_reviews": [
            {"repository": REPO, "review_id": old["review_id"]},
            {"repository": REPO, "review_id": "20261031T235500Z-c4s5-remediation-verification"},
        ],
        "notes": [
            "All original two keys, three actions and eight acceptance checks are retained; one additional key/action adds four checks. Original saved bundles remain immutable.",
            "All actual local inputs are native-pinned, including fresh sources, authority/validator receipts, helper, initial inspection and byte-identical GTDB copy. The final inspection, candidate and subsequent validation outputs are generated metadata, not circular inputs.",
            "No separate source-recovery action is invented: the existing cultivation action explicitly retains the main-protocol gap. No extra cache/header or study-deposit finding was established in the inspected source scope.",
        ],
        "tags": [
            "record-review",
            "nitrification",
            "syncom",
            "partial-source",
            "pr2061-current-main",
        ],
    }
    assert result["actions"][:3] == old["actions"]
    assert len(result["findings"]) == 3
    assert sum(len(a["acceptance_checks"]) for a in actions) == 12
    (OUT / "candidate.json").write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n")
    print(
        json.dumps(
            {
                "candidate": str(OUT / "candidate.json"),
                "sha256": digest(OUT / "candidate.json"),
                "inputs": len(inspection["source"]["inputs"]),
                "findings": 3,
                "actions": 4,
                "acceptance_checks": 12,
            }
        )
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("prepare", "build"))
    parser.add_argument("--inspection", type=Path)
    args = parser.parse_args()
    if args.command == "prepare":
        prepare()
    else:
        if args.inspection is None:
            parser.error("build requires --inspection")
        build(args.inspection)
