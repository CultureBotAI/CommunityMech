"""Build the immutable current-input EcoFAB 025 review for PR 2062.

This helper writes scratch JSON only. The native review saver owns YAML and
Markdown. Actual source retrievals and checks precede the frozen input capture;
the final inspection, candidate and subsequent checks are noncircular outputs.
"""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

import yaml

OUT = Path(".temp/pr2062/refresh025")
SELF = Path("scripts/adhoc/pr2062_025_refresh.py")
OLD = Path("reviews/structured/20261022T094134Z-ecofab-ring-trial-record-review-v2/review.yaml")
TARGET = "CommunityMech:000025"
REPO = "CultureBotAI/CommunityMech"


def read(path):
    return json.loads(Path(path).read_text())


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def prepare():
    old = yaml.safe_load(OLD.read_text())
    paths = {Path(i["path"]) for i in old["source"]["inputs"] if i["path"] != "CLAUDE.md"}
    paths.update({OLD, OLD.with_suffix(".md"), SELF})
    paths.update(p for p in OUT.rglob("*") if p.is_file())
    paths.update(Path(".temp/pr2062/root-checks").glob("*"))
    paths.update(Path("history/records/EcoFAB_Ring_Trial_SynCom17").glob("*.yaml"))
    paths.update(Path(x["path"]) for x in read(OUT / "lineage-context.json"))
    paths.update(
        Path(x)
        for x in [
            "docs/HOST_SOIL_AND_RELATED_COMMUNITIES.md",
            "kb/communities/Brachypodium_Natural_Variation_Dopamine_SynCom16.yaml",
            "kb/communities/LBNL_Switchgrass_Soil_SynCom16.yaml",
            "references_cache/PMID_36472419.txt",
            "references_cache/PMID_42660928.md",
            "reports/causal_graph_review/decisions/20261029-host-soil-related-communities-paper-test.yaml",
            "src/communitymech/ontology_adapters.py",
            "scripts/adhoc/pr2061_397_refresh.py",
            ".temp/pr2062/staleness.json",
            ".temp/pr2062/review-inventory.json",
        ]
    )
    paths.add(OUT / "input-paths.json")
    excluded = {
        "final-inspection.json",
        "final-inspection.stderr",
        "candidate.json",
        "input-manifest.json",
    }
    paths = {
        p
        for p in paths
        if p.name not in excluded
        and not p.name.startswith(("post-save-", "candidate-validation", "native-save"))
    }
    result = {
        "targets": [TARGET],
        "paths": sorted(str(p) for p in paths),
        "boundaries": [
            "All concrete sources, current checks, author reading receipts, helper and relevant maintained context are pinned.",
            "The external GTDB crosswalk is represented by its verified byte-identical local copy.",
            "Initial inspection informed assessment and is pinned. Final inspection defines source.inputs and cannot hash itself.",
            "Candidate, native save and subsequent QC outputs are generated outputs, not inputs to this judgment.",
            "Historical purged scratch locations are not recovered or claimed as current inputs.",
        ],
    }
    (OUT / "input-paths.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({"input_paths": len(paths)}))


def build(inspection_path):
    old = yaml.safe_load(OLD.read_text())
    inspection = read(inspection_path)
    assert {i["path"] for i in inspection["source"]["inputs"]} == set(
        read(OUT / "input-paths.json")["paths"]
    )
    for item in inspection["source"]["inputs"]:
        assert digest(item["path"]) == item["sha256"], item["path"]
    now = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
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
                "snapshot_sha256": digest(path),
            }
        )

    ev(
        "record",
        old["targets"][0]["path"],
        "Whole current maintained target",
        "Seventeen microbial stocks, five nodes and four arrows; main adds host, two member-set links and append-only history, without resolving the four original findings.",
        "record_content",
    )
    for eid, locator, summary in [
        (
            "design",
            "PMID:40920748 / DOI:10.1371/journal.pbio.3003358; Results 2.1 and Figure 1",
            "Five laboratories compare SynCom17, the OAS925-omission SynCom16, axenic plants and plant-free medium controls, with seven replicates per treatment.",
        ),
        (
            "cultivation",
            "Methods 4.1, 4.2, 4.8, 4.9 and 4.10; Figure 1",
            "Stock preparation, genomic DNA cultures, host ring trial, reporter microscopy and motility precultures are distinct experimental stages.",
        ),
        (
            "host",
            "Methods 4.2; surface sterilization and EcoFAB inoculation; Figure 1",
            "Bd21-3 Brachypodium seedlings are prepared axenically before deliberate SynCom inoculation. Roots are the sampled host tissue.",
        ),
        (
            "outcomes",
            "Results 2.3–2.5; visually inspected Figures 2, 3 and 4",
            "Plant outcomes belong to the whole treatment. Relative dominance and net bulk exometabolites do not demonstrate extinction, member-specific flux or a necessary trait.",
        ),
        (
            "traits",
            "Results 2.7 and separately inspected S8–S11 figures",
            "Genomic modules and isolate assays support candidate traits. Combined acid-related profiles differ from individual genes; neither necessity nor uniquely highest OAS925 biomass is established.",
        ),
        (
            "genomes",
            "Methods 4.8; exact 17 IMG/GOLD pairs, especially Mycobacterium OAE908",
            "Gp0440934 is explicitly listed for OAE908; the encoded Gp0588949-Gp0589682 pseudo-range is not the complete project set.",
        ),
        (
            "data",
            "Data Availability, section notes1; S2 Table",
            "The study identifies BioProject, Figshare, GNPS, MassIVE, NMDC, protocol and annotated-genome deposits with distinct scopes.",
        ),
        (
            "collection",
            "Methods 4.1 and S2 Table, source-reported DSM200000SY collection",
            "DSM200000SY denotes a collection rather than one stock. Two guessed catalogue routes were blocked; no successful live collection-page retrieval is claimed.",
        ),
    ]:
        ev(eid, OUT / "sources/ring.xml", locator, summary, "primary_source")
    ev(
        "nitrogen",
        OUT / "sources/nitrogen.xml",
        "PMID:38170767; Abstract, relevant Results, Discussion and Methods sections 16–23",
        "The nitrogen intervention concerns sterile plants and separate 14-isolate bioassays; it is not the SynCom17 ring-trial nitrogen/light factorial.",
        "primary_source",
    )
    ev(
        "stock-table",
        OUT / "sources/ring-s013.json",
        "Complete S2 stock table, 17 stock rows; original XLSX independently pinned",
        "Exact stock names, medium assignments and genome projects were read. Rhizobium, Bradyrhizobium, Mycobacterium and Niastella use 1/10 R2A; Gottfriedia uses LB; other stocks use R2A.",
        "primary_source",
    )
    ev(
        "trait-table",
        OUT / "sources/ring-s020.json",
        "S9 genomic-module table, especially M00660/M00542 T3SS signatures",
        "Module annotations are computational potential; they do not prove a necessary colonization mediator or isolate-level pathogenicity in this community.",
        "primary_source",
    )
    ev(
        "protocol",
        OUT / "sources/protocol.pdf",
        "DOI:10.17504/protocols.io.kxygxyydkl8j/v1; 17-page protocol, steps 1–11",
        "Protocol text distinguishes preparation, 9 mL half-MS plus 1 mL inoculum, pH 5.7, default chamber settings, sterility checks, weekly scans and day-22 harvest; it does not erase paper/laboratory timing deviations.",
        "primary_source",
    )
    ev(
        "ontology",
        OUT / "sources/taxonomy.xml",
        "Fresh NCBI taxonomy efetch: 17 member labels, Arthrobacter genus and Brachypodium host",
        "Current IDs/ranks resolve; 1667 is an unnamed species placeholder and 1663 the Arthrobacter genus. Allobosea 85413 preserves the source Bosea alias.",
        "authority",
    )
    ev(
        "rank",
        OUT / "sources/dsm-oap107.html",
        "DSM 113524 catalogue core: Arthrobacter sp., strain designation OAP107",
        "Exact stock metadata supports genus-level Arthrobacter without resolving its species. A generic unrelated footer link is not used as stock identity evidence.",
        "authority",
    )
    ev(
        "gtdb",
        OUT / "gtdb.stdout",
        "Whole-community lookup; gtdb-genus-context.stdout supplies legacy Bosea/genus follow-up",
        "Fourteen ordinary mapping cores reproduce; source-name Bosea context reproduces 34/34 for the fifteenth. Arthrobacter genus has 11 alternatives and Paenibacillus remains ambiguous. This is not strain genome assignment.",
        "authority",
    )
    ev(
        "crosswalk",
        OUT / "gtdb-copy.json",
        "Verified source/copy SHA256 equality and community-mode command receipts",
        "Crosswalk SHA256 is 761d5537a7edb4b0133e88e7bbc85570cf3cb6f2555b9f9ce6cca3e1056a0ddd. Local mtime is not an upstream release/build date; legacy Bosea lookup does not override current Allobosea authority.",
    )
    ev(
        "semantics",
        "src/communitymech/schema/communitymech.yaml",
        "FunctionalRoleEnum, evidence tiers, HostMicrobialStatusEnum and RelatedCommunity schema",
        "Optional role fields require claim-local support. AXENIC explicitly describes the host before community introduction; optional host/soil fields do not become mandatory.",
        "authority",
    )
    for eid, name, locator, summary in [
        (
            "snippets",
            "snippet-audit.json",
            "All 35 current snippet placements, exact selectors and hashes",
            "Thirty-four match fresh XML after inline/whitespace normalization; one nitrogen-abstract placement differs only by hyphen versus en dash. Lexical support does not certify causal scope.",
        ),
        (
            "source-audit",
            "source-reading.json",
            "Actual author source/figure/SI reading, checks and limitations",
            "This is author reassessment, not independent approval. Full focal main and selected critical figures/tables support the retained findings and graph limits.",
        ),
        (
            "support",
            "source-reading.json",
            "Current graph and literal rubric calculation",
            "Five nodes/four arrows remain qualified; completeness 45, quality raw 101/capped 100 with two P2 and three P3 findings.",
        ),
        (
            "relations",
            "relation-context.json",
            "Current 025/516/087 member sets and inverse relation context",
            "025 equals dopamine 516 plus OAE829 and Coker final 087 plus OAE603. Shared membership does not transfer study conditions or outcomes.",
        ),
        (
            "cache",
            "cache-scope.json",
            "Two cache headers and appended main-article/Methods payloads",
            "Both content_type values say abstract_only despite full main text; this is provenance inconsistency rather than proof that sources or snippets are unavailable.",
        ),
        (
            "delta",
            "target-diff.patch",
            "Original frozen record versus current main record",
            "Host, member-set links and append-only history changed; all four original scientific findings remain unresolved.",
        ),
        (
            "lineage",
            "lineage-context.json",
            "Ignored-inclusive exact-target finding discovery and selected Cycle 8 context",
            "The four exact original finding occurrences are continued. The separate Cycle 8 assessment is context only, not superseded.",
        ),
        (
            "adapter",
            "adapter-discovery.json",
            "Installed console lookup and three bounded expected CLAW checkout roots",
            "No structured-source runner was available in those locations. This is an optional adapter limitation, not negative gene evidence or failed required QC.",
        ),
    ]:
        ev(eid, OUT / name, locator, summary)
    ev(
        "resources",
        OUT / "sources/resource-additional-retrievals.json",
        "Actual public resource responses, including exact GNPS status and genome DOI",
        "Five encoded study resources resolve to the ring trial; GNPS exact task is DONE. Hugging Face genome DOI resolves despite viewer parsing error. Raw datasets and all individual IMG projects were not reanalyzed.",
    )
    ev(
        "coker-roster",
        OUT / "sources/coker.xml",
        "PMID:36472419; Methods, Isolate selection, final 16 deposited DSM stocks",
        "The final 16-stock roster lacks OAE603 and includes OAE829. Later plant colonization uses other inoculum sizes and must not be conflated with this final-stock relation.",
        "primary_source",
    )
    ev(
        "dopamine-roster",
        OUT / "sources/dopamine.xml",
        "PMID:42660928; Methods paragraph Par30, 16-strain inoculum roster",
        "The source-named 16-stock set differs from ring SynCom17 only by OAE829; later recovery or abundance does not redefine inoculum membership.",
        "primary_source",
    )
    ev(
        "predecessor",
        OLD,
        "Four exact original finding keys, four action objects and 11 acceptance checks",
        "All original scientific heads and action checks are retained. Historical scratch evidence and independent roles are not represented as current access or approval.",
        "prior_review",
    )
    ev(
        "corpus",
        ".temp/pr2062/root-checks/initial-checks.json",
        "Parent-owned current corpus diagnostics and native controls",
        "Both network commands returned exit 1: 48 warnings across 17 of 510 communities, zero errors. These recorded warning-only diagnostics are not author reruns.",
    )
    checks = []
    for row in read(OUT / "checks/focused-checks.json"):
        eid = "check-" + row["name"]
        ev(
            eid,
            OUT / "checks/focused-checks.json",
            "Entry " + row["name"] + "; exact command, timestamps and separately pinned logs",
            f"Actual current exit {row['exit_code']}.",
        )
        checks.append(
            {
                "check_id": row["name"],
                "name": row["name"],
                "status": "passed" if row["exit_code"] == 0 else "failed",
                "required": True,
                "summary": f"Actual current exit {row['exit_code']}.",
                "target_ids": [TARGET],
                "command": " ".join(row["command"]),
                "exit_code": row["exit_code"],
                "expected_exit_code": 0,
                "evidence_ids": [eid],
                "scope_note": "Focused target/history; cache naming check is corpus-wide.",
            }
        )
    for name in ("audit-network", "check-network-quality"):
        checks.append(
            {
                "check_id": name,
                "name": name,
                "status": "failed",
                "required": False,
                "summary": "Shared corpus: 48 warnings across 17 of 510 records, zero errors, actual exit 1.",
                "target_ids": [TARGET],
                "command": "just --no-dotenv " + name,
                "exit_code": 1,
                "expected_exit_code": 0,
                "evidence_ids": ["corpus"],
                "scope_note": "Actual parent-run receipt; historical 44-warning baseline is not claimed as current.",
            }
        )
    retain = {"identity", "nongraph", "cultivation", "grounding", "graph-topology"}
    assessments = [
        copy.deepcopy(a)
        for a in old["assessments"]
        if a["assessment_id"] in retain or a["assessment_id"].startswith(("node-", "edge-"))
    ]

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
        "new-host",
        "scope",
        "Current host block and pre-inoculation status",
        "supported",
        "The added Brachypodium Bd21-3 root host context is supported.",
        ["host", "protocol", "ontology", "semantics", "snippets"],
        "NCBITaxon:15368 and PO:0009005 describe the plant and root; Bd21-3 is the cultivar. AXENIC follows the schema's explicit before-inoculation meaning and does not assert permanent sterility after SynCom addition. Sterilized devices and surface-sterilized seedlings support the preparation context. No mandatory host_participation or soil field is inferred, and the host is not added to the microbial roster.",
    )
    assess(
        "new-relations",
        "identity",
        "Exact related-community member sets",
        "supported",
        "Both added MEMBER_SUPERSET_OF links are supported at their stated membership basis.",
        ["relations", "coker-roster", "dopamine-roster", "stock-table", "semantics"],
        "Ring SynCom17 equals the 000516 dopamine-study 16-stock inoculum plus Bradyrhizobium OAE829; OAE829 is already in SynCom17. The first description is redundant, but the stored superset relation is true. Ring SynCom17 equals Coker's final deposited 000087 16-stock set plus Gottfriedia/Bacillus OAE603. Coker's separate 17/18-member plant assay is not that final-set identity. Source aliases and final current target IDs 000516/000087 remain explicit. Membership overlap does not transfer dopamine, nitrogen, plant-outcome or cultivation claims between studies.",
    )
    assess(
        "evidence",
        "evidence",
        "Current snippet placement and source tiers",
        "concern",
        "All 35 placements have source support, while the original claim-scope and evidence-tier repairs remain needed.",
        ["snippets", "cultivation", "outcomes", "traits", "nitrogen", "semantics"],
        "Thirty-four snippets match fresh XML after whitespace and inline-element reconstruction. The remaining nitrogen abstract differs only in amino acids-peptides versus the XML en dash. Source lexical support is not stronger causal proof. Exact stocks belong to S2/Methods 4.8; living-host outcomes are IN_VIVO, genomic annotations COMPUTATIONAL, and separate isolate phenotype assays IN_VITRO. No supplement is silently merged into an article cache.",
    )
    assess(
        "resources",
        "evidence",
        "Study resources and incomplete genome identifier set",
        "concern",
        "The five encoded study deposits resolve; the genome pseudo-range still needs exact identifiers.",
        ["resources", "data", "genomes", "stock-table"],
        "PRJNA1151037, the exact GNPS task, MSV000095476, NMDC study and Figshare collection identify this ring trial. The public genome DOI additionally identifies SynCom17_EcoFab; its viewer parsing error is not absence of the deposit. Gp0588949-Gp0589682 omits Mycobacterium OAE908 Gp0440934 and is not an enumeration of all 17 projects. IMG taxon IDs are not NCBITaxon IDs. Metadata resolution is not validation of raw spectra, genomes, annotation function or assay mechanism.",
    )
    assess(
        "cache-provenance",
        "provenance",
        "Cache content declarations",
        "concern",
        "Two cache headers incorrectly describe appended full-main content as abstract only.",
        ["cache", "snippets", "check-validate-references-explained"],
        "PMID_40920748.md has content_type at line 46 and its PMC12416739 main-text marker at line 134. doi_10.1126_sciadv.adg7888.md has content_type at line 20 and its PMC10776018 marker at line 32. Both payloads include Results and Methods. The reference check passes; no missing-snippet claim, supplement-completeness claim or expanded source trust follows. Metadata repair belongs outside this review PR.",
    )
    assess(
        "lineage",
        "provenance",
        "Current-input successor and immutable history",
        "supported",
        "The four old open findings continue with their exact keys and acceptance; host/link additions do not resolve them.",
        ["predecessor", "delta", "lineage", "relations"],
        "All seven history sidecars and inline events remain immutable. Earlier link IDs describe append-only renumbering steps rather than current target identity. The Cycle 8 audit is context only: its proportional completeness figure is not substituted for this profile's literal rubric or treated as scientific clearance. No grouped finding or other target disposition is retired. The existing OPEN ecofab_syncom17_mediation_and_study_scope KNOWLEDGE_GAP remains covered by retained causal-scope acceptance without requesting experiments.",
    )
    assess(
        "coverage",
        "scope",
        "Actual current author reading",
        "supported",
        "The focal record received a complete scientific assessment with explicit source and SI boundaries.",
        ["source-audit", "adapter", "predecessor", "protocol"],
        "The author read the full focal main, all five main figures, critical selected SI figures and S1/S2/S9 table content, plus the protocol text and bounded related-source roster/nitrogen evidence. Videos, all numerical matrices, related-study SI and raw omics were not exhaustively inspected or reanalyzed. No historical scratch was recovered and no predecessor independent-review role is inherited. The optional structured adapter was unavailable in the documented locations; primary-source interpretation does not infer negative module evidence.",
    )
    assess(
        "validation",
        "schema",
        "Focused native checks and current corpus context",
        "supported",
        "Eight focused required checks passed; shared corpus warning exits are preserved.",
        ["check-validate", "check-validate-strict", "check-validate-terms", "corpus"],
        "All current focused commands returned zero; strict report has no rows, terms passed, references reported no issues and history passed. Both current corpus network diagnostics returned one with 48 warnings in 17 of 510 records and zero errors. Deterministic success does not resolve the scientific or cache-provenance findings.",
    )
    metric = copy.deepcopy(next(a for a in old["assessments"] if a["assessment_id"] == "metrics"))
    metric["summary"] = "Completeness 45; quality 100 after capping raw 101."
    metric["metrics"][1]["definition"] = (
        "100 - 10*2 P2 - 2*3 P3 + 20*min((6/5)/2,1) + 15 = 101, capped at 100. "
        "Six excerpts across five nodes; evidence bonus 12 and COMPLETE structural bonus 15. "
        "The added cache provenance finding changes quality arithmetic, not scientific strength."
    )
    next(m for m in metric["metrics"] if m["name"] == "P3")["value"] = 3
    assessments.append(metric)
    findings = copy.deepcopy(old["findings"])
    for finding in findings:
        finding["previous_occurrences"] = [
            {
                "repository": REPO,
                "review_id": old["review_id"],
                "finding_id": finding["finding_id"],
            }
        ]
    cache_owners = [
        {"repository": REPO, "path": row["path"], "role": "reference_cache"}
        for row in read(OUT / "cache-scope.json")
    ]
    findings.append(
        {
            "finding_id": "cache-content-type",
            "issue_key": "cm-000025-cache-content-type",
            "category": "provenance",
            "severity": "minor",
            "native_severity": "P3",
            "normalization_reason": "Bounded metadata inconsistency: actual article text and snippet support are present; no missing-source or wrong-study failure is asserted.",
            "rule_id": "review-checklist.claim-specific-support-and-context",
            "status": "open",
            "certainty": "confirmed",
            "title": "Align two cache content declarations with their actual article payloads",
            "description": "Both PMID_40920748.md and doi_10.1126_sciadv.adg7888.md declare content_type: abstract_only, but contain appended PMC main articles including Results and Methods. Their headers should accurately describe the available source content while preserving source provenance and supplement boundaries.",
            "target_ids": [TARGET],
            "field_paths": [
                "references_cache/PMID_40920748.md:front_matter.content_type",
                "references_cache/doi_10.1126_sciadv.adg7888.md:front_matter.content_type",
            ],
            "evidence_ids": ["cache", "snippets", "check-validate-references-explained"],
            "owner_paths": cache_owners,
        }
    )
    actions = copy.deepcopy(old["actions"])
    actions.append(
        {
            "action_id": "repair-cache-content-type",
            "description": "Reconcile the two article-cache metadata declarations with their actual source payloads in separately authorized cache curation.",
            "finding_ids": ["cache-content-type"],
            "target_ids": [TARGET],
            "owner_paths": cache_owners,
            "acceptance_checks": [
                "Inspect references_cache/PMID_40920748.md (PMC12416739 marker line 134) and references_cache/doi_10.1126_sciadv.adg7888.md (PMC10776018 marker line 32); make content_type and retrieval/source metadata accurately describe the actual main-article payload, without claiming complete supplements or importing separate supplementary material into article text.",
                "Preserve exact reference identities, supported snippets and prior provenance. Document the separately authorized cache correction and any retrieval changes without rewriting old history or broadening source trust solely to make validation pass.",
                "Rerun focused references validation for CommunityMech:000025, cache-name checks and applicable cache/provenance tests. Keep semantic claim-scope findings open independently of successful lexical validation.",
            ],
        }
    )
    result = {
        "schema_version": "1.0.0",
        "review_id": datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
        + "-ecofab-ring-trial-current-main",
        "kind": "record",
        "repository": REPO,
        "title": "Current-main refresh of the EcoFAB Ring Trial SynCom17 review",
        "started_at": read(OUT / "source-reading.json")["started_at"].replace("+00:00", "Z"),
        "finished_at": now,
        "reviewer": {
            "identity": "codex",
            "kind": "agent",
            "independence": "self_review",
            "independence_basis": "Author of the refreshed review; a separate agent performs independent adversarial review. This document does not approve itself.",
        },
        "skill": "review-yaml-record",
        "completion": "completed",
        "verdict": "needs_curation",
        "scientific_review": True,
        "summary": "Current host and related-member-set additions are supported at their exact source and pre-inoculation scopes. All four original findings and their 11 acceptance checks remain open. A new minor finding tracks two abstract_only cache headers that conflict with appended main articles. Fresh focal main/critical figure/SI review and eight focused checks support this bounded current-input assessment; no canonical content is changed.",
        "source": inspection["source"],
        "targets": inspection["targets"],
        "scope": {
            "description": "Whole current target, exact main delta, original findings/actions, focal primary study and critical figures/SI, bounded related-study roster/nitrogen context, current authorities, caches, history and native checks.",
            "selection": "Only stale CommunityMech:000025 in PR #2062; other records and grouped finding dispositions are not superseded.",
            "coverage": "full",
            "population_size": 1,
            "reviewed_target_ids": [TARGET],
        },
        "checks": checks,
        "evidence": evidence,
        "assessments": assessments,
        "findings": findings,
        "actions": actions,
        "limitations": read(OUT / "source-reading.json")["limitations"]
        + [
            "Relative reads, bulk metabolites, isolate phenotypes and genome annotations do not establish member-specific flux, obligate cross-feeding or trait necessity.",
            "Source laboratory/timing differences remain explicit, including S1 laboratory E's logger date and day-21 figure labels versus day-22 harvest; they are not silently harmonized.",
            "Related Coker/dopamine records are used only for exact source-set context. No whole-literature assessment of those records or universal portability of cultivation conditions is claimed.",
            "No exhaustive numerical workbook, raw-genome, sequencing, metabolomic or video reanalysis; no paid source access, contact or experimental request.",
        ],
        "related_reviews": [
            {
                "repository": REPO,
                "review_id": old["review_id"],
                "relationship": "Current-input successor retaining all four original open keys and exact actions/acceptance checks.",
            },
            {
                "repository": REPO,
                "review_id": "20261106T094000Z-c8s4-record-deep-audit",
                "relationship": "Context only; no grouped finding or other target disposition is superseded.",
            },
        ],
        "notes": [
            "Four original keys/four actions/11 checks are preserved verbatim; one cache provenance key/action adds three checks, giving five/five/14.",
            "Every actual local source/check/helper input is native-pinned. Final inspection/candidate/save and subsequent QC are generated outputs, avoiding circular self-hashes.",
            "This refresh addresses review staleness #2668 only. Scientific and cache curation remain outside this PR, with all original bundles and canonical files untouched.",
        ],
        "tags": ["record-review", "ecofab", "syncom17", "pr2062-current-main"],
    }
    assert actions[:4] == old["actions"]
    assert len(findings) == 5
    assert sum(len(a["acceptance_checks"]) for a in actions) == 14
    ids = {e["evidence_id"] for e in evidence}

    def check_refs(value):
        if isinstance(value, dict):
            assert set(value.get("evidence_ids", [])) <= ids, value.get("evidence_ids")
            for child in value.values():
                check_refs(child)
        elif isinstance(value, list):
            for child in value:
                check_refs(child)

    check_refs(result)
    (OUT / "candidate.json").write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"candidate": str(OUT / "candidate.json"), "inputs": len(ids)}))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=["prepare", "build"])
    parser.add_argument("--inspection", type=Path)
    args = parser.parse_args()
    if args.command == "prepare":
        prepare()
    else:
        if args.inspection is None:
            parser.error("build requires --inspection")
        build(args.inspection)
