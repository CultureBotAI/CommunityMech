"""Assemble the source-assessed 000515 completion review, 2026-11-14.

Inputs: inspected canonical soil record, Ding primary article/figures/workbook,
seven actual M5 gate receipts and authored judgments below. Outputs: a staging
native review YAML; no canonical mutation. Serves retained #2708 and #2709.
"""

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
TARGET = "kb/communities/Yolo_Silt_Loam_Soil_Dopamine_Amendment_Microcosm.yaml"
IDENT = "CommunityMech:000515"
PAPER = "https://pmc.ncbi.nlm.nih.gov/articles/PMC13522444/"
SUPP = "https://static-content.springer.com/esm/art%3A10.1038%2Fs41467-026-76211-1/MediaObjects/41467_2026_76211_MOESM1_ESM.pdf"


class ReviewDumper(yaml.SafeDumper):
    def ignore_aliases(self, data):
        return True


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    initial = json.loads((STATE / "yolo-initial-inspection.json").read_text())
    inputs = {item["path"] for item in initial["source"]["inputs"]}
    for item in initial["source"]["inputs"]:
        if sha(ROOT / item["path"]) != item["sha256"]:
            raise ValueError("assessed input changed: " + item["path"])
    inputs.update(
        {
            "docs/record-reviews.md",
            "conf/record_review.yaml",
            "justfile",
            ".claude/skills/review-yaml-record/SKILL.md",
            ".claude/skills/review-communities/reference/validation-rules.md",
            ".claude/skills/curate-yaml-record/references/review-checklist.md",
        }
    )
    for pattern in ("yolo-*.log", "yolo-*.json", "shared-network*.log", "shared-network*.json"):
        inputs.update(
            str(p.relative_to(ROOT))
            for p in STATE.glob(pattern)
            if "inspection" not in p.name and ".launch." not in p.name
        )
    inputs.update(
        str(p.relative_to(ROOT)) for p in (STATE / "yolo-sources").glob("*") if p.is_file()
    )
    for filename in ("supplement.pdf", "supplement.txt", "supplement.pdf.source.json"):
        path = STATE / "dopamine-syncom-sources" / filename
        if path.exists():
            inputs.add(str(path.relative_to(ROOT)))
    command = [
        sys.executable,
        "scripts/record_review.py",
        "inspect",
        "--targets",
        str(STATE / "yolo-targets.yaml"),
    ]
    for path in sorted(inputs):
        command.extend(["--input", path])
    result = subprocess.run(command, cwd=ROOT, capture_output=True, text=True, check=True)
    inspected = json.loads(result.stdout)
    (STATE / "yolo-final-inspection.json").write_text(result.stdout)
    record = yaml.safe_load((ROOT / TARGET).read_text())
    assert record["id"] == IDENT and len(record["ecological_interactions"]) == 2
    assert sum(len(n.get("downstream", [])) for n in record["ecological_interactions"]) == 0
    stamp = datetime.now(timezone.utc)
    accessed = stamp.strftime("%Y-%m-%dT%H:%M:%SZ")
    owner = [
        {"repository": "CultureBotAI/CommunityMech", "path": TARGET, "role": "canonical_record"}
    ]
    evidence = []

    def ev(key, kind, reference, locator, summary, support="supports", quote=None, snapshot=None):
        item = {
            "evidence_id": key,
            "kind": kind,
            "reference": reference,
            "locator": locator,
            "accessed_at": accessed,
            "support": support,
            "summary": summary,
        }
        if quote:
            item["quote"] = quote
        if snapshot:
            item["snapshot_sha256"] = sha(snapshot)
        evidence.append(item)

    xml = STATE / "ecofab-relations/PMC13522444.xml"
    ev(
        "record",
        "record_content",
        TARGET,
        "complete354-line record; six taxa; two nodes; no downstream arrows",
        "Entire maintained soil record read, including source/conditions, mapping metadata, relation and history.",
        snapshot=ROOT / TARGET,
    )
    ev(
        "identity",
        "primary_source",
        PAPER,
        "Methods Soil treatment, Sec15/Par38; Results Sec5/Par17",
        "Naturally derived Yolo agricultural soil microcosms are a separate experiment from the same paper's hydroponic SynCom16. No plant host or defined isolate roster is asserted for these soil microcosms.",
        quote="Yolo silt loam",
        snapshot=xml,
    )
    ev(
        "conditions",
        "primary_source",
        PAPER,
        "Methods Soil treatment, Sec15/Par38",
        "Room-dried soil stored4C for2-3months,2mm sieve,20g aliquots,1.5/3.0mg dry catecholamine,6.5mL starting water, approximately24.5% reported water content, twice-weekly treatment for6weeks,foil,roomtemperature,three replicates. Controls receive same handling/water without catecholamine. No sterilization treatment is described; NONE represents the native community protocol, not absence of prior ecological disturbance.",
        quote="without solvent dissolution",
        snapshot=xml,
    )
    ev(
        "abundances",
        "primary_source",
        PAPER,
        "Results Exogenous application of dopamine alters soil microbiota, Sec5/Par18; Fig4b; Methods Sec16-17",
        "Six control phylum means are31.3/16.0/13.5/12.5/10.2/10.2percent. V4/V5 16S read composition is neither absolute biomass nor a measurement of function. RDP names in source differ from current NCBI labels without implying different source organisms.",
        snapshot=xml,
    )
    ev(
        "node-0-source",
        "primary_source",
        PAPER,
        "Sec5/Par18; Fig4b; SupplementaryFig16c",
        "At3.0mg, dopamine and norepinephrine increase Actinobacteria relative abundance versus control, with dopamine greater than norepinephrine. No microbial donor, recipient, uptake or substrate-use mechanism is identified.",
        quote="only Actinobacteria",
        snapshot=xml,
    )
    ev(
        "node-1-source",
        "primary_source",
        PAPER,
        "Sec5/Par18; SupplementaryFig16d",
        "High norepinephrine lowers Acidobacteria relative abundance versus control. Dopamine-high is intermediate and not significantly different from either group; the record correctly limits its depletion claim to norepinephrine versus control.",
        quote="Acidobacteria significantly decreased",
        snapshot=xml,
    )
    ev(
        "supplement",
        "primary_source",
        SUPP,
        "SupplementaryFig16, PDFpage16: panelsc/d and legend; viewed renderedpixels",
        "Actinobacteria labels control=c,dopamine-high=a,norepinephrine-high=b. Acidobacteria control=a,norepinephrine-high=b,dopamine-high=ab. Three independent replicates; one-wayANOVA/TukeyP<0.05. Other phylum shifts are not generalized to functional capacity.",
        snapshot=STATE / "dopamine-syncom-sources/supplement.pdf",
    )
    ev(
        "figure",
        "primary_source",
        "https://cdn.ncbi.nlm.nih.gov/pmc/blobs/5106/13522444/7db46ccc68fc/41467_2026_76211_Fig4_HTML.webp",
        "Fig4a-c; inspected original image",
        "Treatment legend, compositional phylum bars andzOTUresponse context agree with bounded record descriptions. Ordination coordinates are not mechanistic evidence.",
        snapshot=STATE / "yolo-sources/figure4.webp",
    )
    workbook = STATE / "yolo-sources/soil-data5.xlsx"
    ev(
        "workbook",
        "primary_source",
        "https://static-content.springer.com/esm/art%3A10.1038%2Fs41467-026-76211-1/MediaObjects/41467_2026_76211_MOESM7_ESM.xlsx",
        "SupplementaryData5 sheet1: B-D controlcounts, Qphylum; rows4/14/19/25 Thaumarchaeota annotations",
        "Workbook has three replicates per arm. Recomputed control phylum means round to all six record values. Thaumarchaeota rows include Nitrososphaera assignments; these16S taxonomic annotations do not measure amoA expression or ammonia oxidation.",
        snapshot=workbook,
    )
    ev(
        "calculation",
        "validation",
        ".temp/m5-completion-20261114/yolo-sources/source-comparison.json",
        "verify_yolo_sources_20261114.py summarize; explicit formula and sourcehash",
        "Control totals1107/1170/1572 reads; mean per-replicate phylum fractions reproduce the six rounded values. DMS conversion reproduces latitude38.538028 andlongitude-121.766722. This is an arithmetic cross-check, not a statistical reanalysis.",
        "context_only",
        snapshot=STATE / "yolo-sources/source-comparison.json",
    )
    ev(
        "mapping",
        "record_content",
        TARGET,
        "taxonomy[4].taxon_term.gtdb_classification.curation_note; mapping_source fields",
        "The note claims this record ties Thaumarchaeota to amoA ammonia oxidation. Its actual source experiment measures 16S relative abundance, and the inspected workbook supplies taxonomy, not amoA evidence. The mapping numbers reproduce, but they do not establish a measured ecological function or a release/build date.",
        "refutes",
    )
    ev(
        "mapping-reproduction",
        "validation",
        ".temp/m5-completion-20261114/yolo-sources/mapping-comparison.json",
        "Native aggregate denominator, named species only; original crosswalk SHA256 761d5537a7edb4b0133e88e7bbc85570cf3cb6f2555b9f9ce6cca3e1056a0ddd",
        "Five ordinary mapping cores reproduce exactly. The curated Nitrososphaeria vote also reproduces: 57 rows/552 genomes versus 8 rows/79 genomes for Nitrososphaeria_A, denominator 631 and rounded fraction0.875. Native rank-for-rank output is the broader Thermoproteota631/631, so it must not overwrite the curated class. Bacillota_A remains a near-tie, non-type clade; this is mapping evidence, not functional proof. Filesystem mtime is not release metadata.",
        "context_only",
        snapshot=STATE / "yolo-sources/mapping-comparison.json",
    )
    ev(
        "cache",
        "record_content",
        "references_cache/PMID_42660928.md",
        "frontmatter content_type and appended PMC13522444 article",
        "The cache header saysabstract_only despite full-main Results/Methods appended. This does not invalidate genuine quoted source content; metadata correction must preserve boundaries and provenance.",
        "refutes",
        snapshot=ROOT / "references_cache/PMID_42660928.md",
    )
    checks = []
    for name in ("schema", "strict", "terms", "references", "gtdb", "domain", "history"):
        receipt = json.loads((STATE / f"yolo-{name}.json").read_text())
        log = STATE / f"yolo-{name}.log"
        assert receipt["log_sha256"] == sha(log)
        assert datetime.fromisoformat(receipt["finished_at"]) <= datetime.fromisoformat(accessed)
        key = "check-" + name
        ev(
            key,
            "validation",
            str(log.relative_to(ROOT)),
            "complete M5 native log and paired JSON/exit receipt",
            f"Exit{receipt['exit_code']}; {receipt['status']}; baseline76aa644c. Focused lexical/structural checks do not certify source semantics.",
            "context_only",
            snapshot=log,
        )
        checks.append(
            {
                "check_id": name,
                "name": "Native " + name,
                "status": "passed" if receipt["status"] == "PASSED" else "failed",
                "required": True,
                "summary": f"M5 exit{receipt['exit_code']}; exact receipt retained.",
                "command": shlex.join(receipt["command"]),
                "exit_code": receipt["exit_code"],
                "expected_exit_code": 0,
                "target_ids": [IDENT],
                "evidence_ids": [key],
            }
        )
    for name in ("shared-network", "shared-network-quality"):
        receipt = json.loads((STATE / (name + ".json")).read_text())
        log = STATE / (name + ".log")
        assert receipt["log_sha256"] == sha(log)
        ev(
            name,
            "validation",
            str(log.relative_to(ROOT)),
            "corpus549records; zeroerrors,48warningsin17records",
            "Shared corpus diagnostics are wider than this two-node scientific assessment. Disconnected measured effects do not justify inventing mechanistic arrows.",
            "context_only",
            snapshot=log,
        )
        checks.append(
            {
                "check_id": name,
                "name": name,
                "status": "failed",
                "required": False,
                "summary": "Native corpus diagnostic exit1 with warnings; retained separately.",
                "command": shlex.join(receipt["command"]),
                "exit_code": receipt["exit_code"],
                "expected_exit_code": 0,
                "evidence_ids": [name],
                "target_ids": [IDENT],
            }
        )
    assessments = []

    def assess(key, area, topic, outcome, summary, ids, details=None):
        row = {
            "assessment_id": key,
            "area": area,
            "topic": topic,
            "outcome": outcome,
            "summary": summary,
            "target_ids": [IDENT],
            "evidence_ids": ids,
        }
        if details:
            row["details"] = details
        assessments.append(row)
        return row

    identity = assess(
        "identity",
        "identity",
        "Natural soil microcosm rather than hydroponic SynCom",
        "supported",
        "Record identity, naturalorigin,perturbation and SAME_STUDY_AS000516 are source-supported.",
        ["identity", "record"],
    )
    identity["dimensions"] = [
        {
            "name": "scope",
            "value": "Six reported control phyla from native Yolo agriculturalsoil; no strain-level roster or host added",
            "definition": "Unit is the6weeksoil amendment experiment, not the study's16-isolate hydroponic system.",
            "evidence_ids": ["identity", "abundances"],
        },
        {
            "name": "environment",
            "value": "ENVO00002259 agriculturalsoil; ENVO06105275 siltyloam; UC Davis38.538028,-121.766722",
            "definition": "Source soil identity and coordinates, checked against Methods and arithmetic conversion.",
            "evidence_ids": ["conditions", "calculation", "check-terms"],
        },
    ]
    assess(
        "conditions",
        "scope",
        "Handling, amendment arms and measurement context",
        "supported",
        "All recorded mass/time/water/sieve/storage/incubation details match Methods. Preserve reported24.5% rather than silently changing the moisture convention; no pH or exact roomtemperature is invented.",
        ["conditions", "calculation", "check-terms"],
        "Selectors soils[0], environmental_factors[0], cultivation_setup[0]; UO0000016 millimeter andUO0000187percent; catecholamine dose is mass per20gsoil, not aqueous concentration.",
    )
    assess(
        "abundance",
        "evidence",
        "All six control phylum fractions",
        "supported",
        "SupplementaryData5 independently reproduces all six rounded control means. No absolute abundance, persistence, function or treatment-invariant fraction is inferred.",
        ["abundances", "workbook", "calculation"],
        "Selectors taxonomy[0:6].relative_abundance; NCBI1224/1239/201174/57723/651137/976 retain sourcephylum meaning under current labels. Source aliases are preserved; Nitrososphaerota is archaeal.",
    )
    assess(
        "grounding",
        "grounding",
        "Ontology identities and bounded GTDB provenance",
        "concern",
        "Native term/domain/coherence checks pass. CHEBI18243 dopamine and33569 noradrenaline identify the tested compounds; ENVO/UO terms match source units/environment. All six numerical mapping cores reproduce from the recovered crosswalk, including the curated class vote. The copied amoA rationale remains unsupported, and latest/build wording exceeds the verified file identity.",
        [
            "mapping",
            "mapping-reproduction",
            "workbook",
            "check-terms",
            "check-domain",
            "check-gtdb",
        ],
    )
    for index, name, direction, source_id, participant, compound in (
        (
            0,
            "High-dose Actinobacteria enrichment",
            "INCREASES",
            "node-0-source",
            "Actinomycetota NCBITaxon201174",
            "dopamine CHEBI18243 or noradrenaline CHEBI33569",
        ),
        (
            1,
            "High-dose norepinephrine Acidobacteria depletion",
            "DECREASES",
            "node-1-source",
            "Acidobacteriota NCBITaxon57723",
            "noradrenaline CHEBI33569",
        ),
    ):
        assess(
            f"node-{index}",
            "graph",
            name,
            "supported",
            "The intervention-to-relative-composition direction is supported at the high dose and scoped endpoint; molecular mechanism remains unspecified.",
            [source_id, "supplement", "figure", "conditions"],
            f"Selector ecological_interactions[{index}]. Source intervention={compound},3.0mgper20gdriedsoil twiceweekly6weeks; target participant={participant}; direction={direction} versus water-handled control,three replicates,16Srelative abundance. No microbial donor/recipient or plant host is specified. PMID42660928 ResultsSec5/Par18 and SupplementaryFig16 panel{'c' if index == 0 else 'd'}; exact inspected quotation in linked evidence. Zero downstream edges in entire record; no unassessed arrows.",
        )
    assess(
        "cache",
        "provenance",
        "Article-cache boundaries",
        "concern",
        "Correct the metadata without changing source content or treating article text as supplements.",
        ["cache"],
    )
    metrics = assess(
        "metrics",
        "completeness",
        "Native rubric scores do not grant scientific approval",
        "supported",
        "Two distinct metrics, computed literally with the record's missing optional roles preserved.",
        ["record"],
    )
    metrics["metrics"] = [
        {
            "name": "completeness",
            "value": 10,
            "unit": "points",
            "minimum": 0,
            "maximum": 100,
            "definition": "Native formula:0requiredblock(no memberroles)+5environment+0threefactors+0threenodes+0externalresources+0growthmedia+0datasets+5nodemetabolites=10. Missing optional roles are not a reason to invent function.",
        },
        {
            "name": "validation_quality",
            "value": 100,
            "unit": "points",
            "minimum": 0,
            "maximum": 100,
            "denominator": 2,
            "definition": "100-50P1-10P2-2P3+20min((2excerpts/2nodes)/2,1)+15structuraledgeclosure; P1=0,P2=0,P3=2,P4=0; raw121,capped100. Zero edges means no dangling targets, not mechanistic completeness.",
        },
    ]
    metrics["metrics"].extend(
        {"name": key, "value": value, "unit": "findings", "definition": "Native severity count"}
        for key, value in (("P1", 0), ("P2", 0), ("P3", 2), ("P4", 0))
    )
    findings = []
    for key, issuekey, title, description, paths, ids, number, owners in (
        (
            "copied-mechanism-provenance",
            "cm-000515-gtdb-copied-mechanism-provenance",
            "Remove copied record-specific amoA mechanism rationale",
            "The mapping note attributes archaeal amoA ammonia oxidation to this record, but the actual soil study supports 16S taxonomy and relative treatment responses. All six numerical mapping cores reproduce; the correction must preserve them without asserting measured function or unsupported release/build provenance.",
            ["taxonomy[4].taxon_term.gtdb_classification.curation_note"],
            ["mapping", "mapping-reproduction", "workbook", "abundances"],
            2709,
            owner,
        ),
        (
            "cache-content-type",
            "cm-pmid42660928-cache-content-type",
            "Align Ding cache declaration with appended full-main article",
            "abstract_only is inconsistent with the available main-text payload; preserve article/supplement boundaries and provenance.",
            ["references_cache/PMID_42660928.md:front_matter.content_type"],
            ["cache"],
            2708,
            [
                {
                    "repository": "CultureBotAI/CommunityMech",
                    "path": "references_cache/PMID_42660928.md",
                    "role": "reference_cache",
                }
            ],
        ),
    ):
        findings.append(
            {
                "finding_id": key,
                "issue_key": issuekey,
                "category": "provenance",
                "severity": "minor",
                "native_severity": "P3",
                "normalization_reason": "Bounded provenance correction; core experiment and treatment observations are supported.",
                "rule_id": "review-checklist.claim-specific-support-and-context",
                "status": "open",
                "certainty": "confirmed",
                "title": title,
                "description": description,
                "target_ids": [IDENT],
                "field_paths": paths,
                "evidence_ids": ids,
                "owner_paths": owners,
                "external_issues": [
                    f"https://github.com/CultureBotAI/CommunityMech/issues/{number}"
                ],
            }
        )
    actions = [
        {
            "action_id": "repair-" + f["finding_id"],
            "description": f["title"],
            "finding_ids": [f["finding_id"]],
            "target_ids": [IDENT],
            "owner_paths": f["owner_paths"],
            "acceptance_checks": [
                "Apply only source-supported corrections, preserve reproduced numerical mapping cores and scientific boundaries, replace unsupported build claims with verified crosswalk identity, append native history for record changes, and rerun schema/strict/terms/references/GTDB/domain/history and generated-doc gates."
            ],
        }
        for f in findings
    ]
    review = {
        "schema_version": "1.0.0",
        "review_id": stamp.strftime("%Y%m%dT%H%M%SZ") + "-m5-yolo-scientific-completion",
        "kind": "record",
        "repository": "CultureBotAI/CommunityMech",
        "title": "Yolo soil microcosm source-backed completion assessment",
        "started_at": datetime.fromtimestamp(
            (STATE / "yolo-initial-inspection.json").stat().st_mtime, timezone.utc
        ).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "finished_at": accessed,
        "reviewer": {
            "identity": "codex",
            "kind": "agent",
            "independence": "independent",
            "independence_basis": "Fresh complete-record and primary-source assessment; not author of existing record.",
        },
        "skill": "review-yaml-record",
        "completion": (
            "completed"
            if all(c["status"] == "passed" for c in checks if c["required"])
            else "partial"
        ),
        "verdict": "needs_curation",
        "scientific_review": True,
        "summary": "Both measured soil-treatment directions and six control abundances are source-supported; copiedamoA provenance and cache declaration remain open. Passing focusedchecks does not close eitherfinding or certify fullrepositoryQC.",
        "source": inspected["source"],
        "targets": inspected["targets"],
        "scope": {
            "description": "Entire000515record,sixphylum entries,twointeractionnodes,no downstreamarrows,all current conditions and metadata",
            "selection": "Recovered four-record PR2102scope",
            "coverage": "full",
            "population_size": 1,
            "reviewed_target_ids": [IDENT],
        },
        "checks": checks,
        "evidence": evidence,
        "assessments": assessments,
        "findings": findings,
        "actions": actions,
        "limitations": [
            "Mapping votes reproduce from the hash-identified crosswalk; its file mtime does not prove a GTDB release or build date. Mapping a broad phylum does not establish every organism's physiology.",
            "No rawsequencereanalysis or statistical significance recalculation; primary figures and published supplementary data were inspected directly.",
            "Previous broad cohort metrics do not supersede this claim-level assessment; ignore-independent search of reviews/structured found no stable cm-000515 findingkey. Historical partial audit remains in GitHub2709; missing scratch was not reconstructed.",
            "This single-record observation does not close sharedissue2708 for any unassessed consumer. Rootintegration retains all otheraffectedtargets.",
            "Native reference issuecount is not assertioncoverage; fullQC and wider schema/exportfindings remain separate.",
        ],
    }
    path = STATE / "yolo-completion-review.yaml"
    path.write_text(
        yaml.dump(review, Dumper=ReviewDumper, sort_keys=False, allow_unicode=True, width=100)
    )
    print(path)


if __name__ == "__main__":
    main()
