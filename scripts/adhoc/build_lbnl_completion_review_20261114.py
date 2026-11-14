#!/usr/bin/env python3
"""Assemble the source-assessed 000087 recovery review, 2026-11-14.

Inputs: full frozen record, inspected primary XML/figures, prior reviews, and
seven M5 native receipts. Output: staging review YAML and metrics for the native
immutable saver. Serves existing issue1548. No canonical/history/cache edits.
Scientific judgments below are authored assessments, never validator inference.
"""

from __future__ import annotations

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
TARGET_ID = "CommunityMech:000087"
TARGET = "kb/communities/LBNL_Switchgrass_Soil_SynCom16.yaml"
PAPER = "https://pmc.ncbi.nlm.nih.gov/articles/PMC9765266/"
ISSUE = "https://github.com/CultureBotAI/CommunityMech/issues/1548"
PRIOR = "reviews/structured/20261106T094000Z-c8s4-record-deep-audit/review.yaml"
GRAPH_PRIOR = "reports/causal_graph_review/decisions/20261006-lbnl-batch61.yaml"
ROSTER = (
    "Arthrobacter OAP107 (DSM113524); Bosea OAE506 (DSM113628); "
    "Bradyrhizobium OAE829 (DSM113701); Brevibacillus OAP136 (DSM113525); "
    "Burkholderia OAS925 (DSM113627); Chitinophaga OAE865 (DSM113563); "
    "Lysobacter OAE881 (DSM113522); Marmoricola OAE513 (DSM114042); "
    "Mucilaginibacter OAE612 (DSM113562); Methylobacterium OAE515 (DSM113602); "
    "Mycobacterium OAE908 (DSM113539); Niastella OAS944 (DSM113593); "
    "Paenibacillus OAE614 (DSM113526); Rhizobium OAE497 (DSM113517); "
    "Rhodococcus OAS809 (DSM113518); Variovorax OAS795 (DSM113622)"
)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    initial = json.loads((STATE / "lbnl-initial-inspection.json").read_text())
    for item in initial["source"]["inputs"]:
        if digest(ROOT / item["path"]) != item["sha256"]:
            raise ValueError(f"Initially assessed input changed: {item['path']}")
    inputs = {item["path"] for item in initial["source"]["inputs"]}
    inputs.update(
        {
            PRIOR,
            GRAPH_PRIOR,
            "docs/record-reviews.md",
            "conf/record_review.yaml",
            "justfile",
            ".claude/skills/review-communities/reference/validation-rules.md",
            ".claude/skills/review-communities/reference/execution-protocol.md",
            ".claude/skills/curate-yaml-record/references/review-checklist.md",
            "kb/communities/EcoFAB_Ring_Trial_SynCom17.yaml",
            "kb/communities/Brachypodium_Natural_Variation_Dopamine_SynCom16.yaml",
            "reports/m5-completion-20261114/scope.json",
        }
    )
    for pattern in ("lbnl-*.json", "lbnl-*.log", "shared-network*.json", "shared-network*.log"):
        inputs.update(
            str(p.relative_to(ROOT))
            for p in STATE.glob(pattern)
            if not any(s in p.name for s in ("inspection", "completion", ".launch."))
        )
    for directory in ("lbnl-sources", "ecofab-relations"):
        inputs.update(
            str(p.relative_to(ROOT)) for p in (STATE / directory).glob("*") if p.is_file()
        )
    inputs.update(
        str((STATE / filename).relative_to(ROOT))
        for filename in (
            "ecofab-relations.md",
            "ecofab-independent/ring-main-plos.xml",
            "ecofab-independent/ring-s2.xlsx",
            "ecofab-independent/ring-s2.txt",
        )
    )
    command = [
        sys.executable,
        "scripts/record_review.py",
        "inspect",
        "--targets",
        str(STATE / "lbnl-targets.yaml"),
    ]
    for filename in sorted(inputs):
        command.extend(["--input", filename])
    result = subprocess.run(command, cwd=ROOT, text=True, capture_output=True, check=True)
    inspected = json.loads(result.stdout)
    (STATE / "lbnl-final-inspection.json").write_text(result.stdout)
    record = yaml.safe_load((ROOT / TARGET).read_text())
    if record["id"] != TARGET_ID:
        raise ValueError("Unexpected review target")
    nodes = record["ecological_interactions"]
    if len(nodes) != 3 or any(n.get("downstream") for n in nodes):
        raise ValueError("Assessed graph changed")
    prior_context = json.loads((STATE / "lbnl-prior-context.json").read_text())
    if any(row["findings"] for row in prior_context["reviews"]):
        raise ValueError("Reassess structured predecessor findings before saving")
    finished = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    primary_hash = digest(STATE / "ecofab-relations/PMC9765266.xml")
    evidence = []

    def ev(key, kind, reference, locator, summary, support="context_only", quote=None, sha=None):
        item = {
            "evidence_id": key,
            "kind": kind,
            "reference": reference,
            "locator": locator,
            "accessed_at": finished,
            "support": support,
            "summary": summary,
        }
        if quote:
            item["quote"] = quote
        if sha:
            item["snapshot_sha256"] = sha
        evidence.append(item)

    ev(
        "record",
        "record_content",
        TARGET,
        "entire285-line record; exact input SHA256",
        "Read all identity, design, taxonomy, related communities, three nodes, medium, history and Discussion fields. Canonical taxonomy and each node participant are one domain-level Bacteria aggregate; there are zero downstream arrows.",
        sha=digest(ROOT / TARGET),
    )
    ev(
        "identity",
        "primary_source",
        PAPER,
        "Abstract; Results Strain selection(s2-1); Methods Isolate selection(s4-1)",
        "Coker et al., DOI10.1128/msystems.00951-22, PMID36472419, describe a synthetic rhizosphere model with a final16-stock collection, developed from larger experimental panels. Soil denotes the source habitat; actual growth assays use defined liquid media and plant EcoFABs.",
        "supports",
        "final 16-member community",
        primary_hash,
    )
    ev(
        "roster",
        "primary_source",
        PAPER,
        "Methods Isolate selection(s4-1), paragraph0; explicit DSMZ strain list",
        "The final deposited collection is explicitly enumerated: "
        + ROSTER
        + ". Sphingomonas OAE905 and Pseudomonas simiae wcs417 are outside this final16. This stock list is not a species-resolution NCBI/GTDB mapping, nor a claim that figure16S labels uniquely name deposited isolates.",
        "supports",
        "DSM 113524",
        primary_hash,
    )
    ev(
        "nutrient",
        "primary_source",
        PAPER,
        "Results α-diversity of the SynCom is enhanced through low-nutrient conditions (s2-3), paragraph0; Fig2C-E; FigS1D caption",
        "An equal18-strain inoculum grown3days in1x/0.2x/0.1xR2A shows lowerOD600 but greater Shannon diversity and evenness as medium is diluted. Pseudomonas remains relatively dominant. This supports a community response, not increased absolute live numbers, final16 specificity, mutualism or a taxon-pair mechanism.",
        "supports",
        "all 18 strains",
        primary_hash,
    )
    ev(
        "ratios",
        "primary_source",
        PAPER,
        "Results α-diversity of the SynCom is maximized through adjustment of starting community ratios (s2-4), paragraphs0-2; Discussion(s3), paragraph5; Fig3A-C; FigS3D caption",
        "The tested17/18 panels include or exclude Pseudomonas and compare equal inocula with adjusted starting ratios. The2x/3xcutoff conditions increase Shannon/evenness in the Pseudomonas-absent comparisons at2/6days. Later16-stock dropouts are a separate experiment. Neither optimality for arbitrary communities nor a unique competitive mechanism follows.",
        "supports",
        "2× cutoff",
        primary_hash,
    )
    ev(
        "plant",
        "primary_source",
        PAPER,
        "Results The SynCom is able to colonize the rhizosphere in an EcoFAB system(s2-7), paragraphs0-1; Methods Plant colonization experiment (s4-6); Fig5A-B",
        "Sterile Brachypodium distachyon Bd21-3 seedlings enter EcoFABs at3days, receive equal17/18-isolate mixtures at12days and are harvested7days later. Root communities differ from original inoculum (pairwisePERMANOVA P=.036); Pseudomonas± groups do not differ in overall composition. A single inoculum batch prevents taxon-wise before/after significance testing. This is in-vivo colonization/composition evidence, not reciprocal benefit or the final16 inoculum.",
        "supports",
        "17 or 18",
        primary_hash,
    )
    ev(
        "measurement",
        "primary_source",
        PAPER,
        "Results Extracellular DNA affects community composition in early time points (s2-5); Discussion(s3), paragraphs4/6-7; Methods16S analysis",
        "Relative16S profiles, PMA treatments and spike-in checks do not turn every taxon abundance into a viable-cell count. Lysobacter facilitation and three-fast-grower competition remain proposed explanations of dropout outcomes, not newly supported directed graph edges.",
        "supports",
        sha=primary_hash,
    )
    ev(
        "conditions",
        "primary_source",
        PAPER,
        "Methods s4-2 individual culture; s4-3 community growth; s4-6 EcoFAB; s4-7 freezing; Results s2-8 and Fig5C-D",
        "Isolates use3-5mL1xR2A in14mL tubes at30C without shaking; communities use200uL in96well plates at30C aerobically without shaking. Plant chambers use24C and16h/8h, with0.1xMS medium.20%glycerol at-80C followed by0.1xR2A regrowth recapitulates composition better than glycerol/MS; biomass alone is insufficient. These are distinct protocols, not one universal final16 growth condition.",
        "partial",
        sha=primary_hash,
    )
    ev(
        "nongraph",
        "record_content",
        TARGET,
        "description; engineering_design; environmental_factors[0]; growth_media[0]",
        "The non-graph description/design still attributes optimization and EcoFAB outcomes to an undifferentiated16-member community. One medium block pools isolate/community cultivation, cryostorage and live-plant conditions. The graph and Discussion already distinguish18 nutrient and17/18 plant assays. Existing issue1548 explicitly retains this non-graph discrepancy.",
        "refutes",
    )
    ev(
        "grounding",
        "record_content",
        TARGET,
        "taxonomy[0].taxon_term; all3 participating_taxa entries",
        "NCBITaxon2 and GTDB:d__Bacteria agree at domain rank; the label Bacteria exists and all term/coherence checks pass. This does not identify16 stocks or establish individual roles. The historical latest/build mapping with1603049 support_genomes is not reconstructed by those checks. An ignored/hidden-inclusive search of this checkout for NCBI2GTDB artifacts found the comparison script, not the cited mapping snapshot.",
        "partial",
    )
    ev(
        "relations",
        "primary_source",
        PAPER,
        "s4-1 final16 DSM list compared with Ring2025 S2rows2-18 and Ding2026 Methods bacterial strains(Sec9, paragraph0)",
        "Stock-code comparison supports MEMBER_SUBSET_OF000025: ring17=Cokerfinal16+OAE603; and OVERLAPPING_MEMBERSHIP000516:15shared, CokerOAE829 versus dopamineOAE603. This record's descriptions and current target IDs preserve the distinctions. Host-genotype experiments from the dopamine paper are not imported into Coker Bd21-3.",
        "supports",
        sha=primary_hash,
    )
    ev(
        "ring-roster",
        "primary_source",
        "https://journals.plos.org/plosbiology/article/file?id=10.1371/journal.pbio.3003358.s013&type=supplementary",
        "S2Table Sheet1 rows2-18; strains and identifiers",
        "Directly inspected17-stock source table supports the extraOAE603 stock relative to Cokerfinal16. The final16 already includes OAE829.",
        "supports",
        sha=digest(STATE / "ecofab-independent/ring-s2.xlsx"),
    )
    ev(
        "dopamine-roster",
        "primary_source",
        "https://pmc.ncbi.nlm.nih.gov/articles/PMC13522444/",
        "Ding et al. DOI10.1038/s41467-026-76211-1; PMID42660928; Methods Sec9 paragraph0 and Sec8",
        "The explicitly named16 stocks containOAE603 and omitOAE829. Ten-line host experiments and Bd21-3 follow-up belong to this distinct study; only membership overlap is assessed here.",
        "supports",
        sha=digest(STATE / "ecofab-relations/PMC13522444.xml"),
    )
    ev(
        "cache",
        "record_content",
        "references_cache/PMID_36472419.txt; references_cache/pmc_full_pmid_36472419.txt",
        "abstract/full-text boundary markers and source passages",
        "Cached excerpts match inspected open primary text, and the abstract-to-full-text boundary is explicit. No cache metadata finding is asserted for this target. Lexical matching alone did not establish these scientific judgments.",
        "supports",
    )
    ev(
        "prior",
        "prior_review",
        GRAPH_PRIOR,
        "000087 retained nodes, removed workflow nodes, source_review and issue1548",
        "The October6 graph audit retained exactly these three bounded observations and zero arrows while explicitly leaving roster/non-graph scope open. Historical original images and supplements were not read; this review adds direct Fig2/3/5 inspection without claiming all supplements.",
        sha=digest(ROOT / GRAPH_PRIOR),
    )
    ev(
        "prior-native",
        "prior_review",
        PRIOR,
        "assessment assess-communitymech-000087; no findings for this target",
        "The prior26-target audit records85/100 proportional completeness and zero network warnings. Its metric definition differs from the current literal native rubric. It neither resolves the independently documented issue1548 nor supplies claim-level scientific clearance.",
        sha=digest(ROOT / PRIOR),
    )
    ev(
        "prior-search",
        "search",
        ".temp/m5-completion-20261114/lbnl-prior-context.json",
        "all reviews/structured/**/review.yaml including hidden/ignored files",
        "Exactly one structured review declares000087 as a target, with no000087 finding object. Existing issue1548 and the older graph decision are therefore context, not fabricated structured previous_occurrences. Other-target or category findings are not superseded.",
        sha=digest(STATE / "lbnl-prior-context.json"),
    )
    evidence[-1]["search_scope"] = (
        prior_context["search_scope"]
        + "; exact target ID CommunityMech:000087, then inspected target declarations and affected findings. This search excludes external repositories and remote-only reviews."
    )
    ev(
        "issue",
        "prior_review",
        ISSUE,
        "body and OPEN status inspected2026-11-14",
        "Existing issue1548 owns the roster and non-graph protocol scope for three LBNL-associated records. This review addresses only000087 and leaves000088/000122 explicitly unassessed; no duplicate issue or closure is made.",
        "supports",
    )
    for name, locator, summary in (
        (
            "fig2",
            "Fig2C,D,E original pixels plus full caption",
            "Inspected medium concentration/OD600/time axes, Shannon ordering and relative-abundance heatmap. ReducedOD600 and greater Shannon in dilutedR2A are distinct outcomes; heatmap labels are not exact deposited-stock identities.",
        ),
        (
            "fig3",
            "Fig3A-F original pixels plus full caption, focusedA-C",
            "Inspected inoculum composition and Shannon panels separated by Pseudomonas presence, plus41h/140h trajectory labels and PMA context. Inoculum absolute cell estimates and resulting relativeDNA abundances are not conflated.",
        ),
        (
            "fig5",
            "Fig5A-D original pixels plus full caption",
            "Inspected PCoA groups and starting-inoculum single observations, relative-abundance heatmap, and medium-dependent freeze-thaw OD/relativeDNA correlations. No taxon-level causal effect is read from visual separation alone.",
        ),
    ):
        path = STATE / "lbnl-sources" / (name + ".gif")
        receipt = json.loads(path.with_suffix(".gif.source.json").read_text())
        ev(name, "primary_source", receipt["url"], locator, summary, "supports", sha=digest(path))
        evidence[-1]["accessed_at"] = receipt["retrieved_at"].replace("+00:00", "Z")

    checks = []
    for name in ("schema", "strict", "terms", "references", "gtdb", "domain", "history"):
        receipt = json.loads((STATE / f"lbnl-{name}.json").read_text())
        log = STATE / f"lbnl-{name}.log"
        if receipt.get("exit_code") is None or digest(log) != receipt["log_sha256"]:
            raise ValueError(f"Incomplete or changed check: {name}")
        ev(
            "check-" + name,
            "validation",
            str(log.relative_to(ROOT)),
            "entire fresh M5 native log plus paired JSON receipt",
            f"Exit{receipt['exit_code']}; {receipt['status']}; M5 base{receipt['head']}. This validates its declared technical scope, not whole-record scientific support.",
            sha=receipt["log_sha256"],
        )
        checks.append(
            {
                "check_id": name,
                "name": "Native " + name,
                "status": "passed" if receipt["exit_code"] == 0 else "failed",
                "required": True,
                "summary": f"M5 exit{receipt['exit_code']}; complete receipt retained.",
                "target_ids": [TARGET_ID],
                "command": shlex.join(receipt["command"]),
                "exit_code": receipt["exit_code"],
                "expected_exit_code": 0,
                "evidence_ids": ["check-" + name],
            }
        )
    for name in ("shared-network", "shared-network-quality"):
        receipt = json.loads((STATE / (name + ".json")).read_text())
        log = STATE / (name + ".log")
        if digest(log) != receipt["log_sha256"]:
            raise ValueError("Shared log changed")
        ev(
            name,
            "validation",
            str(log.relative_to(ROOT)),
            "fresh full-corpus diagnostic; no LBNL_Switchgrass_Soil_SynCom16 issue listed",
            "Corpus549records,48warnings in17records, zeroerrors; focal record has no listed network finding. Domain-level placeholder membership can be structurally complete while biologically incomplete.",
            sha=receipt["log_sha256"],
        )
        checks.append(
            {
                "check_id": name,
                "name": name,
                "status": "passed" if receipt["exit_code"] == 0 else "failed",
                "required": False,
                "summary": "Shared corpus diagnostic; focal target has no listed issue.",
                "target_ids": [TARGET_ID],
                "command": shlex.join(receipt["command"]),
                "exit_code": receipt["exit_code"],
                "expected_exit_code": 0,
                "evidence_ids": [name],
                "scope_note": "Corpus-wide; not a focal scientific verdict.",
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
        "Final16 collection and experimental variants",
        "supported",
        "The record resolves uniquely to the intended Coker soil SynCom collection; it is synthetic, engineered and rhizosphere-associated.",
        ["record", "identity", "roster"],
    )
    identity["dimensions"] = [
        {
            "name": "source_identity",
            "value": "CommunityMech:000087; PMID36472419; DOI10.1128/msystems.00951-22",
            "definition": "Maintained identity and primary article",
            "evidence_ids": ["record", "identity"],
        },
        {
            "name": "source_strains",
            "value": ROSTER,
            "definition": "Final16 deposited stocks explicitly enumerated in main Methods; species identities are not inferred",
            "evidence_ids": ["roster"],
        },
        {
            "name": "community_scope",
            "value": "Final16 versus18 nutrient,17/18 ratio/EcoFAB and separate16 dropout assays",
            "definition": "Distinct inocula and endpoints from one source paper",
            "evidence_ids": ["identity", "nutrient", "ratios", "plant"],
        },
        {
            "name": "taxon_rank",
            "value": "Canonical NCBITaxon2 / GTDB:d__Bacteria domain aggregate",
            "definition": "Coherent broad identity; not a16-member strain roster",
            "evidence_ids": ["grounding", "check-terms", "check-gtdb", "check-domain"],
        },
        {
            "name": "experimental_setting",
            "value": "LiquidR2A30C community assays; sterile-start Bd21-3 in0.1xMS EcoFAB24C16h/8h",
            "definition": "Source soil is distinguished from actual growth media and host context",
            "evidence_ids": ["conditions", "plant"],
        },
    ]
    assess(
        "member-identity",
        "grounding",
        "Domain placeholder and strain representation",
        "concern",
        "The domain grounding is coherent but materially underrepresents the explicitly named16-stock community; individual functional roles are not established by the abstract.",
        ["record", "roster", "grounding", "issue", "check-terms", "check-gtdb"],
    )
    assess(
        "nongraph-scope",
        "scope",
        "Description, engineering design and cultivation context",
        "concern",
        "Non-graph fields still merge final16 identity with18-strain nutrient and17/18 EcoFAB evidence. Preserve correct measured conditions while attaching each to its own experiment.",
        ["nongraph", "conditions", "nutrient", "plant", "issue"],
    )
    for index, (source, context, figure) in enumerate(
        (
            (
                "nutrient",
                "Source participants: equally mixed18-strain assay, including Pseudomonas. Target: aggregate community Shannon/evenness after3days; medium dilution increases diversity while loweringOD600. IN_VITRO; no species-pair direction or mechanism is asserted. GO0040007 is the broad growth process. Participant stock resolution remains finding member-roster.",
                "fig2",
            ),
            (
                "ratios",
                "Source participants:17/18-strain panels with/without Pseudomonas;2x/3xcutoff and relative-abundance-adjusted starts compared with equal starts. Target: diversity at2/6days. IN_VITRO; inoculum-ratio response is supported within those comparisons, not a universal optimum. GO0040007 remains broad; no unique competitive mediator is claimed.",
                "fig3",
            ),
            (
                "plant",
                "Source participants:17/18 equal isolates Pseudomonas± plus living Brachypodium Bd21-3, sterile only before inoculation. Target: rhizosphere community composition7days after12day-plant inoculation. IN_VIVO; direction is inoculation followed by measured composition, not reciprocal benefit or causal taxon exclusion. GO0044419 is compatible with this bounded host-community observation.",
                "fig5",
            ),
        )
    ):
        node = nodes[index]
        assess(
            f"node-{index}",
            "graph",
            node["name"],
            "supported",
            "The exact node description and its evidence support the bounded observation and preserve variant/measurement limits.",
            ["record", source, figure, "measurement", "check-terms"],
            f"Field ecological_interactions[{index}]. PMID36472419 / DOI10.1128/msystems.00951-22; linked primary evidence contains inspected short verbatim snippet and exact section/figure locator. "
            + context,
        )
    assess(
        "arrows",
        "graph",
        "Complete directed-edge inventory",
        "supported",
        "All3 nodes contain zero downstream arrows. No workflow transition, taxon facilitation or competition edge is invented from the experimental sequence.",
        ["record", "prior", "measurement", "shared-network"],
        "Source and target participant/direction/mediator review is complete for the existing edge population0. Node-level treatment-to-observation contexts are recorded separately above.",
    )
    assess(
        "relations",
        "identity",
        "Current links to000025 and000516",
        "supported",
        "The two typed membership relations and their descriptions are supported by primary stock-code comparisons. These three communities remain distinct.",
        ["relations", "ring-roster", "dopamine-roster", "record"],
    )
    assess(
        "evidence",
        "evidence",
        "Claim-local sources, evidence tiers and cache boundaries",
        "supported",
        "All5 graph excerpts were checked against primary main text, withIN_VITRO for liquid assays andIN_VIVO for host observations. Media snippets also match their narrow Methods claims; abstract design support is insufficient for assay-specific final16 attribution.",
        ["nutrient", "ratios", "plant", "conditions", "cache", "check-references"],
    )
    assess(
        "history",
        "provenance",
        "Prior scientific scope and append-only history",
        "supported",
        "History passes. The October graph repair and current Discussion preserve mechanistic uncertainty; the native November metric observation has no000087 findings to supersede. Existing three-record issue1548 remains open.",
        ["prior", "prior-native", "prior-search", "issue", "check-history"],
    )

    owner = {"repository": "CultureBotAI/CommunityMech", "path": TARGET, "role": "canonical_record"}
    findings = [
        {
            "finding_id": "member-roster",
            "issue_key": "cm-000087-member-roster",
            "category": "grounding",
            "severity": "major",
            "native_severity": "P2",
            "normalization_reason": "The sixteen defined source stocks collapse to one domain placeholder, preventing strain-specific membership/grounding reuse; this is material identity incompleteness rather than an invalid domain identifier.",
            "rule_id": "P2.3; review-checklist.claim-specific-support-and-context",
            "status": "open",
            "certainty": "confirmed",
            "title": "Replace the aggregate placeholder with a source-resolved final16 roster",
            "description": "The main Methods already enumerate16 deposited stocks, but taxonomy and all3 participant sets retain only NCBITaxon2. Preserve exact stock/DSM identity and uncertainty while resolving canonical labels and reproducible NCBI/GTDB mapping. Do not infer member functional roles, substitute close species, or use the separate17/18 assay roster as final16. Historical latest/build mapping provenance is not established by current coherence checks.",
            "target_ids": [TARGET_ID],
            "field_paths": [
                "taxonomy[0]",
                "ecological_interactions[0].participating_taxa",
                "ecological_interactions[1].participating_taxa",
                "ecological_interactions[2].participating_taxa",
            ],
            "owner_paths": [owner],
            "evidence_ids": ["record", "roster", "grounding", "issue", "prior"],
            "external_issues": [ISSUE],
        },
        {
            "finding_id": "assay-scope",
            "issue_key": "cm-000087-assay-scope",
            "category": "scope",
            "severity": "major",
            "native_severity": "P2",
            "normalization_reason": "Pooling distinct inoculum sizes and culture/host protocols changes the biological unit to which experimental outcomes are attributed; correct graph qualifiers do not repair these non-graph fields.",
            "rule_id": "review-checklist.claim-specific-support-and-context",
            "status": "open",
            "certainty": "confirmed",
            "title": "Separate final16 identity from18-strain nutrient and17/18 host assay metadata",
            "description": "Description, design and environmental-factor prose treat nutrient/ratio/EcoFAB results as undifferentiated16-member optimization. Growth_media combines isolate preparation, community cultivation, glycerol storage and plant chamber conditions. Specify the tested variant and assay for each claim, retain positive methodological results, and preserve the graph's relativeDNA and mechanism limits. The paper's broad abstract does not override its explicit Methods inocula.",
            "target_ids": [TARGET_ID],
            "field_paths": [
                "description",
                "engineering_design",
                "environmental_factors[0]",
                "growth_media[0]",
            ],
            "owner_paths": [owner],
            "evidence_ids": [
                "nongraph",
                "identity",
                "nutrient",
                "ratios",
                "plant",
                "conditions",
                "issue",
            ],
            "external_issues": [ISSUE],
        },
    ]
    excerpts = sum(len(node.get("evidence", [])) for node in nodes)
    required_present = all(
        record.get(k)
        for k in ("id", "name", "description", "taxonomy", "ecological_state", "community_category")
    ) and all(t.get("functional_role") for t in record["taxonomy"])
    completeness = (
        50 * required_present
        + 5 * bool(record.get("environment_term"))
        + 10 * (len(record.get("environmental_factors", [])) >= 3)
        + 10 * (len(nodes) >= 3)
        + 5 * bool(record.get("external_resources"))
        + 10 * bool(record.get("growth_media"))
        + 5 * bool(record.get("associated_datasets"))
        + 5 * any("metabolites" in n for n in nodes)
    )
    counts = {p: sum(f["native_severity"] == p for f in findings) for p in ("P1", "P2", "P3", "P4")}
    graph_complete = all(
        t["term"]["id"] in {m["taxon_term"]["term"]["id"] for m in record["taxonomy"]}
        for n in nodes
        for t in n.get("participating_taxa", [])
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
        "Literal native scores and their limits",
        "supported",
        "Completeness25/100 and capped validation quality100/100 are reproducible rubric outputs, not scientific approval. Missing roles withhold the all-required50points; unsupported roles must not be invented to raise the score.",
        ["record", "grounding", "prior-native"],
    )
    metric["metrics"] = [
        {
            "name": "completeness",
            "value": completeness,
            "unit": "points",
            "minimum": 0,
            "maximum": 100,
            "definition": "Literal native rubric:50all required fields+member roles;5environment+10three factors+10three nodes+5resources+10medium+5datasets+5node metabolites. Current0+5+0+10+0+10+0+0=25; distinct from prior proportional85.",
        },
        {
            "name": "validation_quality",
            "value": max(0, min(100, raw_quality)),
            "unit": "points",
            "minimum": 0,
            "maximum": 100,
            "definition": f"100-50P1-10P2-2P3+20min(({excerpts}/{len(nodes)})/2,1)+15structural completeness; capped0..100. Raw={raw_quality}; structural placeholder membership does not prove scientific completeness.",
            "denominator": len(nodes),
        },
        {
            "name": "evidence_per_interaction",
            "value": excerpts / len(nodes),
            "unit": "excerpts per node",
            "denominator": len(nodes),
            "definition": "5graph evidence entries divided by3interaction nodes; not an assertion-coverage percentage.",
        },
    ]
    metric["metrics"].extend(
        {
            "name": p,
            "value": count,
            "unit": "findings",
            "definition": "Native severity count for this record review.",
        }
        for p, count in counts.items()
    )
    actions = [
        {
            "action_id": "resolve-final-roster",
            "description": "Curate exact source stock identities and transparent taxonomic grounding without unsupported member roles.",
            "finding_ids": ["member-roster"],
            "target_ids": [TARGET_ID],
            "owner_paths": [owner],
            "acceptance_checks": [
                "Reconcile all16 main-Methods stock/DSM pairs; verify strain identity against primary/deposit sources and NCBI with unresolved ranks retained. Pin actual GTDB mapping input/version rather than inheriting latest.",
                "Preserve18 nutrient and17/18 ratio/EcoFAB participant scope; do not force final16 membership onto those observations. If the current schema cannot encode variant membership faithfully, document the bounded representation decision.",
                "Run schema, strict, term, reference, GTDB/domain and network checks after curation, append native history, and save a new source-backed reassessment. Issue1548 still covers000088/000122.",
            ],
        },
        {
            "action_id": "partition-assay-metadata",
            "description": "Attach non-graph conditions/outcomes to the explicit tested inoculum and assay while retaining valid graph observations.",
            "finding_ids": ["assay-scope"],
            "target_ids": [TARGET_ID],
            "owner_paths": [owner],
            "acceptance_checks": [
                "Description/design distinguish final16 collection from18-strain nutrient and17/18 EcoFAB tests; media/protocol notes separate individual culture, community growth, cryopreservation and host chamber settings with local Methods evidence.",
                "Retain all3 bounded graph observations and zero unsupported workflow/mechanism arrows; preserve single-inoculum-batch statistics and relativeDNA limitations.",
                "Validate modified record and append history; independently review final scientific claims. Do not close the three-record issue1548 on this target's evidence alone.",
            ],
        },
    ]
    review = {
        "schema_version": "1.0.0",
        "review_id": stamp + "-m5-lbnl-switchgrass-completion",
        "kind": "record",
        "repository": "CultureBotAI/CommunityMech",
        "title": "Current LBNL Switchgrass SynCom16 scientific recovery review",
        "started_at": datetime.fromtimestamp(
            (STATE / "lbnl-initial-inspection.json").stat().st_mtime, timezone.utc
        ).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "finished_at": finished,
        "reviewer": {
            "identity": "codex-community-m5",
            "kind": "agent",
            "independence": "independent",
            "independence_basis": "Not the author of canonical inputs or prior reviews; fresh whole-record, full-main-text and targeted original-figure inspection. Root performs a separate review of this new bundle.",
        },
        "skill": "review-yaml-record",
        "completion": (
            "completed"
            if all(c["status"] == "passed" for c in checks if c["required"])
            else "partial"
        ),
        "verdict": "needs_curation",
        "scientific_review": True,
        "summary": "All3 existing nodes and0 downstream edges received claim-specific scientific assessment;7focused M5 checks pass. Two major findings remain under existing issue1548: missing final16 member representation and pooled non-graph assay scope. Saving this review completes assessment, not those curation actions or full repository QC.",
        "source": inspected["source"],
        "targets": inspected["targets"],
        "scope": {
            "description": "Entire current000087 record, all3nodes/0arrows, primary stock relations and retained issue1548 scope.",
            "selection": "Frozen four-record M5 recovery scope from PR2102;000087 reviewed individually after the EcoFAB canary.",
            "coverage": "full",
            "population_size": 1,
            "reviewed_target_ids": [TARGET_ID],
        },
        "checks": checks,
        "evidence": evidence,
        "assessments": assessments,
        "findings": findings,
        "actions": actions,
        "limitations": [
            "Source inspection covers the complete primary main body/captions and original Fig2/3/5, plus RingS2 and relevant Ding Methods for relations. Coker TableS1 publisher returned403 and PMC returned non-DOCX content; no claim of inspecting that supplement, other original supplemental figures/protocol or raw sequencing data is made. The final16 list is explicit in main Methods.",
            "No new16-stock NCBI/GTDB curation or reconstruction of the historical latest/build mapping was performed. Current broad-term/coherence checks cannot establish stock-level identities or historical1603049-genome counts.",
            "No raw-data statistical reanalysis, absolute viable-cell assay or causal mediator experiment was performed. Figure inspection does not overcome compositional or replicate limitations.",
            "Reference validation reports issues rather than coverage; native Discussion evidence checks remain incomplete(#476). Scientific assessments explicitly inspected the Discussion's source claims.",
            "iModulonDB is not applicable: this record has no exact gene/locus/regulator/transcriptomic claim and no strain-resolved dataset identity. Lack of adapter use is not evidence against the biology.",
            "Optional media/resource links and detailed factors may be enriched after scope repair; their absence is recorded in completeness rather than used to invent mechanisms or force roles.",
            "Full required repository QC is coordinated separately. Shared corpus network receipts have wider scope and warnings; this review does not certify the repository.",
            "Initial assessment and M5 checks use76aa644cd6803ea2c9545d4c704276ede219d354. The final inspector records the actual local Git base; every initial scientific input hash is rechecked unchanged before saving.",
            "The other two records covered by issue1548 remain outside this single-record assessment. No canonical record/cache/history or prior review was changed, and no old finding or GitHub issue was closed.",
        ],
        "related_reviews": [
            {
                "repository": "CultureBotAI/CommunityMech",
                "review_id": "20261106T094000Z-c8s4-record-deep-audit",
                "relationship": "Adds claim-level scientific assessment to prior metric observation; supersedes no multi-target finding",
            }
        ],
    }
    output = STATE / "lbnl-completion-review.yaml"
    # Shared owner dictionaries are serialized as values, never YAML anchors.
    output.write_text(
        yaml.safe_dump(
            json.loads(json.dumps(review)), sort_keys=False, allow_unicode=True, width=100
        )
    )
    (STATE / "lbnl-completion-metrics.json").write_text(
        json.dumps(
            {
                "completeness": completeness,
                "raw_quality": raw_quality,
                "counts": counts,
                "nodes": len(nodes),
                "edges": 0,
                "excerpts": excerpts,
            },
            indent=2,
        )
        + "\n"
    )
    print(output)


if __name__ == "__main__":
    main()
