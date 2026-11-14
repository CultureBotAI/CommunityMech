"""Assemble the assessed EcoFAB recovery review, 2026-11-14.

Inputs: inspected current record, prior finding identities, M5 check receipts,
and the explicitly authored source assessments below. Outputs: a staging YAML
for the native immutable saver plus a metrics receipt. Serves #1427/#2674-2676.
This script does not curate records or infer scientific judgments from checks.
"""

from __future__ import annotations

import copy
import hashlib
import json
import shlex
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
STATE = ROOT / ".temp/m5-completion-20261114"
PRIOR_ID = "20261106T211930Z-ecofab-ring-trial-current-main"
TARGET_ID = "CommunityMech:000025"
TARGET = "kb/communities/EcoFAB_Ring_Trial_SynCom17.yaml"
PAPER = "https://pmc.ncbi.nlm.nih.gov/articles/PMC12416739/"
NITROGEN = "https://pmc.ncbi.nlm.nih.gov/articles/PMC10776018/"


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def now():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def main():
    initial = json.loads((STATE / "ecofab-initial-inspection.json").read_text())
    for item in initial["source"]["inputs"]:
        if digest(ROOT / item["path"]) != item["sha256"]:
            raise ValueError(f"initially assessed input changed: {item['path']}")
    inputs = {item["path"] for item in initial["source"]["inputs"]}
    inputs.update(
        {
            "docs/record-reviews.md",
            "conf/record_review.yaml",
            "justfile",
            ".claude/skills/review-yaml-record/SKILL.md",
            ".claude/skills/review-communities/reference/metrics-and-reports.md",
            ".claude/skills/review-communities/reference/validation-rules.md",
            ".claude/skills/review-communities/reference/execution-protocol.md",
            ".claude/skills/curate-yaml-record/references/review-checklist.md",
        }
    )
    for pattern in ("ecofab-*.log", "ecofab-*.json", "shared-network*.log", "shared-network*.json"):
        inputs.update(
            str(p.relative_to(ROOT))
            for p in STATE.glob(pattern)
            if "inspection" not in p.name
            and "completion" not in p.name
            and ".launch." not in p.name
        )
    inputs.update(
        str(p.relative_to(ROOT)) for p in (STATE / "ecofab-independent").glob("*") if p.is_file()
    )
    inputs.add(str((STATE / "ecofab-relations.md").relative_to(ROOT)))
    inputs.update(
        str(p.relative_to(ROOT)) for p in (STATE / "ecofab-relations").glob("*") if p.is_file()
    )
    command = [
        sys.executable,
        "scripts/record_review.py",
        "inspect",
        "--targets",
        str(STATE / "ecofab-targets.yaml"),
    ]
    for name in sorted(inputs):
        command.extend(["--input", name])
    result = subprocess.run(command, cwd=ROOT, text=True, capture_output=True, check=True)
    inspected = json.loads(result.stdout)
    (STATE / "ecofab-final-inspection.json").write_text(result.stdout)
    prior = yaml.safe_load((ROOT / f"reviews/structured/{PRIOR_ID}/review.yaml").read_text())
    record = yaml.safe_load((ROOT / TARGET).read_text())
    if record["id"] != TARGET_ID:
        raise ValueError("unexpected target")
    for item in inspected["source"]["inputs"]:
        if digest(ROOT / item["path"]) != item["sha256"]:
            raise ValueError(f"assessed input changed: {item['path']}")
    finished = now()
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    accessed = finished
    main_hash = digest(ROOT / "references_cache/PMID_40920748.md")
    evidence = []

    def ev(key, kind, reference, locator, summary, support="context_only", quote=None, sha=None):
        row = {
            "evidence_id": key,
            "kind": kind,
            "reference": reference,
            "locator": locator,
            "accessed_at": accessed,
            "support": support,
            "summary": summary,
        }
        if quote:
            row["quote"] = quote
        if sha:
            row["snapshot_sha256"] = sha
        evidence.append(row)

    ev(
        "record",
        "record_content",
        TARGET,
        "entire record; input SHA256",
        "Read the complete current canonical record, including all 17 members, five interaction nodes, four downstream arrows, host, conditions, datasets and history.",
        sha=digest(ROOT / TARGET),
    )
    ev(
        "design",
        "primary_source",
        PAPER,
        "Results 2.1; Fig1; Methods4.1-4.2",
        "The intended experimental unit is the five-laboratory SynCom17 comparison with SynCom16, axenic plants and plant-free medium; host is Brachypodium Bd21-3.",
        "supports",
        "four treatments",
        main_hash,
    )
    ev(
        "outcomes",
        "primary_source",
        PAPER,
        "Results2.3-2.5; Figs2-4; Methods4.6",
        "Plant effects are whole-treatment outcomes. Sequencing reports relative composition; spent-medium chemistry does not isolate a taxon's uptake or establish competitive extinction.",
        "refutes",
        "relative abundance",
        main_hash,
    )
    ev(
        "traits",
        "primary_source",
        PAPER,
        "Results2.7; Methods4.7-4.9; S8-S11 figure descriptions",
        "Genome annotation, isolate culture assays and RFP-isolate host imaging are separate evidence tiers. The source reports high motility and sixth-ranked biofilm; no selective trait intervention establishes necessity in SynCom17.",
        "partial",
        "sixth-highest biofilm formation",
        main_hash,
    )
    ev(
        "cultivation",
        "primary_source",
        PAPER,
        "Results2.4; Methods4.1-4.2 versus4.8-4.9",
        "The ring trial inoculates ten-day seedlings and harvests22DAI; three-day seedlings and200rpm refer to separate RFP microscopy preparation. Main methods specify14h light with labC deviation,9mL medium plus1mL inoculum, and a theoretical freeze-thaw-adjusted inoculum.",
        "refutes",
        "10-day-old",
        main_hash,
    )
    ev(
        "nitrogen",
        "primary_source",
        NITROGEN,
        "Materials and methods: Plant growth and harvest",
        "The nitrogen-form/starvation experiment uses sterile plants, distinct medium formulations and a five-week harvest. It is not a nitrogen/light factorial arm of the SynCom17 ring trial.",
        "refutes",
        "sterility",
        digest(ROOT / "references_cache/doi_10.1126_sciadv.adg7888.md"),
    )
    ev(
        "genomes",
        "primary_source",
        PAPER,
        "Methods4.8 and Data Availability; S2Table locator",
        "The source provides explicit stock-to-IMG/GOLD pairs and a genome collection. Mycobacterium OAE908 uses Gp0440934, which the record's pseudo-range omits.",
        "refutes",
        "Gp0440934",
        main_hash,
    )
    ev(
        "grounding",
        "record_content",
        TARGET,
        "taxonomy[9] and four participant copies; mapping_source fields",
        "The source stock code is preserved, but the record retains the Arthrobacter-sp. placeholder and an unpinned latest/build assertion. Native term/coherence checks do not reproduce the historical mapping snapshot.",
        "partial",
    )
    ev(
        "cache",
        "record_content",
        "references_cache/PMID_40920748.md; references_cache/doi_10.1126_sciadv.adg7888.md",
        "front matter and appended EuropePMC article markers",
        "Both headers declare abstract_only although article Methods/Results are appended. Preserve article/supplement boundaries when correcting metadata.",
        "refutes",
    )
    ev(
        "prior",
        "prior_review",
        f"reviews/structured/{PRIOR_ID}/review.yaml",
        "findings and actions",
        "Retain all five stable keys and all acceptance conditions. Successful focused diagnostics do not supersede their scientific dispositions.",
    )
    for key, locator, summary, quote in (
        (
            "edge-assembly",
            "Results2.4 paragraph1; Fig3 caption; Methods4.6 final sentence",
            "All17 inoculum stocks lead to the OAS925-dominated root relative-read profile at22DAI, versus the OAS925-omission SynCom16. This does not measure absolute disappearance or identify an exclusion mechanism.",
            "98 ± 0.03%",
        ),
        (
            "edge-metabolites",
            "Results2.5 paragraph1; Fig4 caption; Methods4.4-4.5",
            "Whole SynCom17 treatment changes bulk spent-medium LC-MS profiles. Microbial or plant production/uptake and extracellular enzymes remain alternatives; no donor-recipient or OAS925-specific flux is established.",
            "lower relative concentrations",
        ),
        (
            "edge-growth",
            "Results2.3 paragraph1; Fig2b-c caption",
            "SynCom17 versus axenic plants reduces pooled-laboratory shoot fresh/dry biomass and root development from14DAI onward, with laboratory variation. It does not isolate a single causal stock.",
            "consistent decrease",
        ),
        (
            "edge-traits",
            "Discussion paragraph3; Results2.7; Methods4.7-4.10; S8-S11",
            "Separate genome and isolate assays motivate trait-mediated colonization, but no selective perturbation/rescue establishes the mechanism. Combined acid-resistance profile differs from unique individual genes; OAS925 shares a top growth significance group, ranks sixth for biofilm, and motility comparisons depend on pH/time/comparator.",
            "might facilitate",
        ),
    ):
        ev(
            key,
            "primary_source",
            PAPER,
            locator,
            summary,
            "partial" if key == "edge-traits" else "supports",
            quote,
            main_hash,
        )
    ev(
        "relations",
        "primary_source",
        "https://pmc.ncbi.nlm.nih.gov/articles/PMC9765266/",
        "Coker Methods Isolate selection; compared with ring S2rows2-18 and Ding Methods Bacterial strains and synthetic community inoculation (PMID42660928)",
        "The ring17 adds OAE603 to Cokerfinal16 and OAE829 to dopamine16. Both typed supersets are supported, but the first description erroneously adds OAE829 to SynCom17 itself. These16sets and ringSynCom16 lacking OAS925 are distinct.",
        "partial",
        sha=digest(STATE / "ecofab-relations/PMC9765266.xml"),
    )
    ev(
        "dopamine-roster",
        "primary_source",
        "https://www.nature.com/articles/s41467-026-76211-1",
        "Methods Bacterial strains and synthetic community inoculation, Sec9 paragraph0; Plant materials and plant growth, Sec8",
        "The enumerated dopamine16 stocks include OAE603 and exclude OAE829; ten-host-line experiments and Bd21-3 follow-up are distinct from ring-trial Bd21-3. Ring AXENIC host status applies only before inoculation.",
        "supports",
        sha=digest(STATE / "ecofab-relations/PMC13522444.xml"),
    )
    supplements = STATE / "ecofab-independent"
    for key, filename, locator, summary in (
        (
            "stock-table",
            "ring-s2.xlsx",
            "Sheet1 rows2-18; columnsA-F,J-L",
            "All17 stocks and exact IMG/GOLD pairs are explicit. Stock media are1/10R2A for OAE497/OAE829/OAE908/OAS944, LB for OAE603, and R2A for the other12. These are stock-preparation conditions, not genomic-DNA culture or host cultivation.",
        ),
        (
            "chambers",
            "ring-s1.xlsx",
            "Sheet1 rows2-6, columnsE-O",
            "Laboratory settings and recorded timings differ. LaboratoryE's logger date differs from the experimental dates; preserve source reporting rather than harmonizing it.",
        ),
        (
            "trait-table",
            "ring-s9.xlsx",
            "Sheet1 rows2-3; columnsA-D",
            "Surveyed T3SS signatures M00660 and M00542 occur in OAS925 and not the other16 mean. This is computational annotation, not proof of expressed virulence or trait necessity.",
        ),
        (
            "rank",
            "arthrobacter-taxonomy.xml",
            "Taxon1663 and Taxon1667; compared with S2row13",
            "NCBI1663 is the Arthrobacter genus;1667 is an unclassified Arthrobacter-sp. species placeholder. The source stock is OAP107; refining to genus must retain species uncertainty.",
        ),
    ):
        metadata = json.loads((supplements / (filename + ".source.json")).read_text())
        ev(
            key,
            "database" if key == "rank" else "primary_source",
            metadata["url"],
            locator,
            summary,
            "supports",
            sha=digest(supplements / filename),
        )
        evidence[-1]["accessed_at"] = metadata["retrieved_at"].replace("+00:00", "Z")

    checks = []
    for name in ("schema", "strict", "terms", "references", "gtdb", "domain", "history-corrected"):
        receipt = json.loads((STATE / f"ecofab-{name}.json").read_text())
        if "exit_code" not in receipt:
            raise ValueError(f"check still running: {name}")
        log = STATE / f"ecofab-{name}.log"
        if digest(log) != receipt["log_sha256"]:
            raise ValueError(f"log changed: {name}")
        key = "check-" + name
        ev(
            key,
            "validation",
            str(log.relative_to(ROOT)),
            "complete M5 native log and paired JSON exit receipt",
            f"Exit{receipt['exit_code']}; status{receipt['status']}. Reference issue counts are not counts of checked assertions.",
            "context_only",
            sha=receipt["log_sha256"],
        )
        if datetime.fromisoformat(receipt["finished_at"]) > datetime.fromisoformat(accessed):
            raise ValueError(f"assessment predates check artifact: {name}")
        checks.append(
            {
                "check_id": name,
                "name": "Native " + name,
                "status": "passed" if receipt["status"] == "PASSED" else "failed",
                "required": True,
                "summary": f"M5 exit{receipt['exit_code']}; retained full receipt.",
                "target_ids": [TARGET_ID],
                "command": shlex.join(receipt["command"]),
                "exit_code": receipt["exit_code"],
                "expected_exit_code": 0,
                "evidence_ids": [key],
            }
        )
    for name in ("shared-network", "shared-network-quality"):
        receipt = json.loads((STATE / f"{name}.json").read_text())
        log = STATE / f"{name}.log"
        if digest(log) != receipt["log_sha256"]:
            raise ValueError(f"log changed: {name}")
        ev(
            name,
            "validation",
            str(log.relative_to(ROOT)),
            "full corpus audit; no EcoFAB-specific issue listed",
            "The corpus audit reports48 warnings in17of549 records and no errors. This is wider than the focal record and is not a scientific endorsement.",
            sha=receipt["log_sha256"],
        )
        checks.append(
            {
                "check_id": name,
                "name": name,
                "status": "passed" if receipt["exit_code"] == 0 else "failed",
                "required": False,
                "summary": "Wider corpus diagnostic retained separately from focal acceptance.",
                "target_ids": [TARGET_ID],
                "command": shlex.join(receipt["command"]),
                "exit_code": receipt["exit_code"],
                "expected_exit_code": 0,
                "evidence_ids": [name],
                "scope_note": "Corpus-wide;48 warnings in17of549 records, zero errors.",
            }
        )

    assessments = []

    def assess(key, area, topic, outcome, summary, ids, details=None):
        item = {
            "assessment_id": key,
            "area": area,
            "topic": topic,
            "outcome": outcome,
            "summary": summary,
            "target_ids": [TARGET_ID],
            "evidence_ids": ids,
        }
        if details:
            item["details"] = details
        assessments.append(item)
        return item

    identity = assess(
        "identity",
        "identity",
        "Defined ring-trial community and host",
        "supported",
        "The record identifies the intended 17-stock synthetic community and host experiment.",
        ["record", "design", "genomes", "stock-table"],
    )
    identity["dimensions"] = [
        {
            "name": "experimental_scope",
            "value": "Five laboratories; SynCom17 and SynCom16 versus axenic and plant-free controls",
            "definition": "Experimental unit, distinct from a natural community or a single-isolate assay.",
            "evidence_ids": ["design"],
        },
        {
            "name": "source_identity",
            "value": "CommunityMech:000025; PMID:40920748; DOI:10.1371/journal.pbio.3003358",
            "definition": "Stable record and primary study identity.",
            "evidence_ids": ["record", "design"],
        },
    ]
    identity["dimensions"].append(
        {
            "name": "source_strains",
            "value": "; ".join(t["strain_designation"]["strain_name"] for t in record["taxonomy"]),
            "definition": "The17 explicitly named inoculum stocks, independently checked against S2rows2-18.",
            "evidence_ids": ["record", "stock-table"],
        }
    )
    assess(
        "nongraph",
        "evidence",
        "Member roles and causal attribution",
        "concern",
        "Competitive exclusion, member-specific amino-acid uptake and plant harm exceed the cited treatment-level evidence; optional role tags lack member-local support.",
        ["record", "outcomes", "traits"],
    )
    assess(
        "conditions",
        "scope",
        "Assay-specific cultivation and environmental conditions",
        "concern",
        "Ring-trial, reporter-isolate, genomic culture and separate nitrogen-study conditions remain pooled.",
        ["record", "cultivation", "nitrogen", "stock-table", "chambers"],
    )
    assess(
        "grounding",
        "grounding",
        "Taxon labels and reproducible mapping provenance",
        "concern",
        "Native terms and GTDB coherence pass, but OAP107 rank and unpinned mapping provenance still require the retained source-supported correction.",
        ["grounding", "rank", "check-terms", "check-gtdb", "check-domain", "prior"],
    )
    assess(
        "resources",
        "provenance",
        "Genome identifiers and article-cache declarations",
        "concern",
        "The source's explicit collection supersedes the pseudo-range as a correction target; both cache content declarations remain inaccurate.",
        ["genomes", "cache"],
    )
    nodes = record["ecological_interactions"]
    stock_names = ", ".join(t["strain_designation"]["strain_name"] for t in record["taxonomy"])
    contexts = [
        (
            "design",
            "The17-stock inoculum is the experimental perturbation; Bd21-3 host, half-MS EcoFAB2.0, ten-day seedlings, five laboratories,22DAI. Controls are axenic plants, omissionSynCom16 and plant-free medium.",
        ),
        (
            "edge-traits",
            "OAS925-specific computational gene potential, isolate growth/biofilm/motility, and separate reporter-strain host colonization are distinct assays. Predicted T3SS and acid-resistance potential are not necessary/expressed mechanisms. OAS925 is not uniquely highest-growth and its biofilm ranks sixth.",
        ),
        (
            "edge-assembly",
            "Root16S relative composition at22DAI is community-level; OAS925 dominates relative reads, not proven absolute elimination of other stocks. OmissionSynCom16 is a distinct inoculum.",
        ),
        (
            "edge-metabolites",
            "Filtered bulk spent medium at harvest, targeted/untargetedLC-MS. Net extracellular abundance in the host-community system; amino-acid identity CHEBI33709 is a class, not measured taxon-specific uptake.",
        ),
        (
            "edge-growth",
            "Bd21-3 shoot fresh/dry biomass pooled across laboratories and root development from14DAI; whole-treatment response with laboratory variation. GO0040007 growth does not name a microbial toxicity mechanism.",
        ),
    ]
    for index, node in enumerate(nodes):
        source_id, context = contexts[index]
        assess(
            f"node-{index}",
            "graph",
            node["name"],
            "concern",
            context + " Existing pooled IN_VITRO evidence tagging remains a curation concern.",
            ["record", source_id, "stock-table", "traits"],
            f"Selector ecological_interactions[{index}]. Source participants: "
            + ("OAS925" if index == 1 else stock_names)
            + ". Host context: Brachypodium distachyon Bd21-3 (NCBITaxon15368). "
            + "PMID40920748; exact locator and inspected quotation are in the linked evidence. Host-associated outcomes require IN_VIVO; isolated cultures IN_VITRO; annotations COMPUTATIONAL.",
        )
    for source_index, edge_index, target_index, evidence_id in (
        (0, 0, 2, "edge-assembly"),
        (0, 1, 3, "edge-metabolites"),
        (0, 2, 4, "edge-growth"),
        (1, 0, 2, "edge-traits"),
    ):
        edge = nodes[source_index]["downstream"][edge_index]
        if edge["target"] != nodes[target_index]["name"]:
            raise ValueError("assessed edge target changed")
        assess(
            f"edge-{source_index}-{edge_index}",
            "graph",
            edge["target"],
            "supported" if source_index == 0 else "unknown",
            (
                "Treatment direction is supported within the measured endpoint."
                if source_index == 0
                else "Retain HYPOTHESIZED trait mediation; causal necessity is untested."
            ),
            ["record", evidence_id, "stock-table"],
            f"Selector ecological_interactions[{source_index}].downstream[{edge_index}]. "
            f"Direction: {nodes[source_index]['name']} -> {nodes[target_index]['name']}. "
            + "Source stocks: "
            + (stock_names if source_index == 0 else "OAS925")
            + "; target community stocks: "
            + stock_names
            + ". "
            + contexts[target_index][1]
            + " PMID40920748; linked evidence supplies exact locator and inspected quotation. "
            + (
                "No identified molecular mediator or donor-recipient flux."
                if source_index == 0
                else contexts[1][1]
            ),
        )
    assess(
        "related-communities",
        "identity",
        "Three distinct16-stock comparators",
        "concern",
        "Both membership links are supported; the dopamine subset prose requires correction without changing direction or membership.",
        ["relations", "dopamine-roster", "stock-table"],
        "Selectors related_communities[0:2]; host.microbial_status applies to the sterile start only.",
    )

    findings = copy.deepcopy(prior["findings"])
    evidence_map = {
        "causal-role-evidence": ["record", "outcomes", "traits", "trait-table", "stock-table"],
        "study-stage-scope": ["record", "cultivation", "nitrogen", "stock-table", "chambers"],
        "grounding-provenance": ["grounding", "rank", "check-terms", "check-gtdb", "prior"],
        "genome-identifiers": ["record", "genomes", "stock-table"],
        "cache-content-type": ["cache", "check-references"],
    }
    issue_map = {
        "causal-role-evidence": 1427,
        "study-stage-scope": 1427,
        "grounding-provenance": 2674,
        "genome-identifiers": 2675,
        "cache-content-type": 2676,
    }
    for finding in findings:
        key = finding["finding_id"]
        finding["evidence_ids"] = evidence_map[key]
        finding["previous_occurrences"] = [
            {"repository": "CultureBotAI/CommunityMech", "review_id": PRIOR_ID, "finding_id": key}
        ]
        finding["external_issues"] = [
            f"https://github.com/CultureBotAI/CommunityMech/issues/{issue_map[key]}"
        ]
    findings.append(
        {
            "finding_id": "relation-description",
            "issue_key": "cm-000025-dopamine-relation-description",
            "category": "scope",
            "severity": "minor",
            "native_severity": "P3",
            "normalization_reason": "The typed relation and stock sets are correct; the prose operation is wrong.",
            "rule_id": "review-checklist.claim-specific-support-and-context",
            "status": "open",
            "certainty": "confirmed",
            "title": "Correct the dopamine subset description",
            "description": "OAE829 already belongs to SynCom17; the dopamine16 plus OAE829 equals ring17.",
            "target_ids": [TARGET_ID],
            "field_paths": ["related_communities[0].description"],
            "owner_paths": [
                {
                    "repository": "CultureBotAI/CommunityMech",
                    "path": TARGET,
                    "role": "canonical_record",
                }
            ],
            "evidence_ids": ["relations", "dopamine-roster", "stock-table"],
            "external_issues": ["https://github.com/CultureBotAI/CommunityMech/issues/2772"],
        }
    )

    nodes = record["ecological_interactions"]
    excerpts = sum(len(node.get("evidence", [])) for node in nodes)
    counts = {p: sum(f["native_severity"] == p for f in findings) for p in ("P1", "P2", "P3", "P4")}
    required = all(
        record.get(k)
        for k in ("id", "name", "description", "taxonomy", "ecological_state", "community_category")
    ) and all(t.get("functional_role") for t in record["taxonomy"])
    completeness = (
        50 * required
        + 5 * bool(record.get("environment_term"))
        + 10 * (len(record.get("environmental_factors", [])) >= 3)
        + 10 * (len(nodes) >= 3)
        + 5 * bool(record.get("external_resources"))
        + 10 * bool(record.get("growth_media"))
        + 5 * bool(record.get("associated_datasets"))
        + 5 * any(n.get("metabolites") for n in nodes)
    )
    node_names = {n["name"] for n in nodes}
    graph_complete = all(
        edge["target"] in node_names for node in nodes for edge in node.get("downstream", [])
    )
    raw_quality = (
        100
        - 50 * counts["P1"]
        - 10 * counts["P2"]
        - 2 * counts["P3"]
        + min(excerpts / len(nodes) / 2, 1) * 20
        + 15 * graph_complete
    )
    metric = assess(
        "metrics",
        "completeness",
        "Native completeness and validation-quality metrics",
        "supported",
        "These literal rubric scores do not certify scientific support.",
        ["record", "prior"],
    )
    metric["metrics"] = [
        {
            "name": "completeness",
            "value": completeness,
            "unit": "points",
            "minimum": 0,
            "maximum": 100,
            "definition": "Native rubric:50 only when required fields and all member roles exist;5environment+10three factors+10three nodes+5external resources+10medium+5datasets+5node metabolites.",
        },
        {
            "name": "validation_quality",
            "value": max(0, min(100, raw_quality)),
            "unit": "points",
            "minimum": 0,
            "maximum": 100,
            "definition": f"Native rubric:100-50P1-10P2-2P3+20min(({excerpts}/{len(nodes)})/2,1)+15structural network completeness; capped0..100. Raw={raw_quality}.",
            "denominator": len(nodes),
        },
    ]
    metric["metrics"].extend(
        {
            "name": p,
            "value": count,
            "unit": "findings",
            "definition": "Retained native-severity count.",
        }
        for p, count in counts.items()
    )
    review = {
        "schema_version": "1.0.0",
        "review_id": stamp + "-m5-ecofab-completion-canary",
        "kind": "record",
        "repository": "CultureBotAI/CommunityMech",
        "title": "Current EcoFAB scientific recovery canary",
        "started_at": datetime.fromtimestamp(
            (STATE / "ecofab-initial-inspection.json").stat().st_mtime, timezone.utc
        ).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "finished_at": finished,
        "reviewer": {
            "identity": "codex",
            "kind": "agent",
            "independence": "independent",
            "independence_basis": "Fresh inspection and primary-source reassessment; not the author of the existing canonical record or prior review. Separate agent also checks primary evidence.",
        },
        "skill": "review-yaml-record",
        "completion": (
            "completed"
            if all(c["status"] == "passed" for c in checks if c["required"])
            else "partial"
        ),
        "verdict": "needs_curation",
        "scientific_review": True,
        "summary": "The current scientific assessment retains four prior curation findings and one cache-provenance finding, and adds a source-verified relation-prose finding, despite passing focused validators. This is the saved canary for the recovered four-record scope, not full repository QC completion.",
        "source": inspected["source"],
        "targets": inspected["targets"],
        "scope": {
            "description": "Entire current EcoFAB record, all five nodes/four arrows and the five surviving finding keys.",
            "selection": "Explicit surviving four-finding review named in M5 recovery; also one of four PR2102 records.",
            "coverage": "full",
            "population_size": 1,
            "reviewed_target_ids": [TARGET_ID],
        },
        "checks": checks,
        "evidence": evidence,
        "assessments": assessments,
        "findings": findings,
        "actions": copy.deepcopy(prior["actions"]),
        "limitations": [
            "Full required repository QC is a separate task and is not certified by this record bundle.",
            "The reference validator reports issues, not assertion coverage, and does not fully validate Discussion evidence (#476). Exact lexical agreement does not establish semantic support.",
            "The initial history invocation targeted the community YAML and failed because that recipe expects append-only history records; the corrected history-directory invocation is the assessment gate. Both receipts are retained.",
            "The historical GTDB mapping file is not reconstructed here; coherence and current canonical-label checks do not establish its release/build provenance. That finding remains open.",
            "No raw-genome, metabolomics or numerical-workbook reanalysis; this review preserves unresolved trait mediation and exact experimental scope.",
            "No canonical record, cache, existing review or history was changed by this canary.",
        ],
        "related_reviews": [
            {
                "repository": "CultureBotAI/CommunityMech",
                "review_id": PRIOR_ID,
                "relationship": "Current-input scientific reassessment preserving every unresolved finding",
            }
        ],
    }
    review["actions"].append(
        {
            "action_id": "repair-relation-description",
            "description": "Correct the dopamine subset prose while preserving the typed relation.",
            "finding_ids": ["relation-description"],
            "target_ids": [TARGET_ID],
            "owner_paths": [
                {
                    "repository": "CultureBotAI/CommunityMech",
                    "path": TARGET,
                    "role": "canonical_record",
                }
            ],
            "acceptance_checks": [
                "State that SynCom17 is dopamine16 plus OAE829; retain the separate Coker16 and ringSynCom16 identities, validate strict membership and append curation history."
            ],
        }
    )
    output = STATE / "ecofab-completion-canary.yaml"
    output.write_text(yaml.safe_dump(review, sort_keys=False, allow_unicode=True, width=100))
    (STATE / "ecofab-completion-metrics.json").write_text(
        json.dumps(
            {
                "completeness": completeness,
                "raw_quality": raw_quality,
                "counts": counts,
                "nodes": len(nodes),
                "excerpts": excerpts,
            },
            indent=2,
        )
        + "\n"
    )
    print(output)


if __name__ == "__main__":
    main()
