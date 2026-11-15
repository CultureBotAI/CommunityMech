"""Author full source-based 000088 assessment for #1548, 2026-11-15.

Inputs: exact applied candidate, original sources, authority output and nine fresh
native gate receipts. Output: exclusive staged review plus native input inventory.
No canonical/cache edits or provider calls. Native validate/save is separate.
"""

import argparse
import hashlib
import json
import shlex
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts/adhoc"))
from check_phase2_brachypodium_20261115 import BASE, CACHES, GATES, HISTORY, TARGET  # noqa: E402
from curate_phase2_brachypodium_20261115 import SOURCE_SHA, STATE, load  # noqa: E402

TARGET_ID = "CommunityMech:000088"
REPOSITORY = "CultureBotAI/CommunityMech"
PAPER = "https://www.frontiersin.org/journals/microbiology/articles/10.3389/fmicb.2025.1649750/full"
PRIOR = "reports/causal_graph_review/decisions/20261006-lbnl-batch61.yaml"


class NoAliasDumper(yaml.SafeDumper):
    def ignore_aliases(self, data):
        return True


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--curation-receipt", type=Path, required=True)
    parser.add_argument("--run", required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    output = args.output.resolve()
    if output.exists() or output.is_symlink() or not output.is_relative_to(STATE):
        raise ValueError("fresh private output required")
    correction = json.loads(args.curation_receipt.read_bytes())
    if not correction["applied"] or correction["after_sha256"] != sha(ROOT / TARGET):
        raise ValueError("review requires exact applied candidate")
    for relative, expected in correction["inputs"].items():
        if sha(ROOT / relative) != expected:
            raise ValueError("curation input changed: " + relative)
    for relative, expected in SOURCE_SHA.items():
        if sha(STATE / relative) != expected:
            raise ValueError("assessed primary source changed")
    record = load((ROOT / TARGET).read_bytes())
    grounding = json.loads((STATE / "grounding-roster-004.json").read_bytes())
    studies = json.loads((STATE / "study-mapping-001.json").read_bytes())
    stock_ids = {row["paper_stock"]: row for row in studies["roster"]}
    if (
        len(record["taxonomy"]) != 15
        or len(record["ecological_interactions"]) != 5
        or any(n.get("downstream") for n in record["ecological_interactions"])
        or len(record["treatment_arms"]) != 9
    ):
        raise ValueError("assessed scope changed")
    receipts = {}
    for gate in (*GATES, "references", "network"):
        name = f"brachypodium-{gate}-{args.run}"
        receipt = json.loads((STATE / (name + ".json")).read_bytes())
        log = ROOT / receipt["log"]
        if (
            receipt["head"] != BASE
            or receipt["gate"] != gate
            or receipt["status"] != "PASSED"
            or receipt["exit_code"] != 0
            or (STATE / (name + ".exit")).read_text().strip() != "0"
        ):
            raise ValueError("required native gate incomplete or failed: " + gate)
        if (
            sha(log) != receipt["log_sha256"]
            or log.stat().st_size != receipt["log_bytes"]
            or not receipt["log_bytes"]
        ):
            raise ValueError("native log hash/bytes differ: " + gate)
        if not receipt["inputs_unchanged"] or any(
            sha(ROOT / relative) != expected for relative, expected in receipt["inputs"].items()
        ):
            raise ValueError("current native gate inputs differ: " + gate)
        expected = list(GATES[gate]) if gate in GATES else None
        if gate == "strict":
            expected += ["--out", str((STATE / (name + ".tsv")).relative_to(ROOT))]
        if gate == "terms":
            expected = [
                "uv",
                "run",
                "--no-sync",
                "linkml-term-validator",
                "validate-data",
                TARGET,
                "-s",
                "src/communitymech/schema/communitymech.yaml",
                "--labels",
                "--config",
                str((STATE / (name + "-oak.yaml")).relative_to(ROOT)),
                "--cache-dir",
                str((STATE / (name + "-labels")).relative_to(ROOT)),
            ]
        if gate == "references":
            expected = [
                "uv",
                "run",
                "--no-sync",
                "linkml-reference-validator",
                "validate",
                "data",
                TARGET,
                "-s",
                "src/communitymech/schema/communitymech.yaml",
                "--config",
                "conf/reference_validator.yaml",
                "--cache-dir",
                str((STATE / (name + "-cache")).relative_to(ROOT)),
                "--no-full-text",
            ]
            if not receipt["private_cache_unchanged"]:
                raise ValueError("private source cache changed")
        if gate == "network":
            expected = [
                "uv",
                "run",
                "--no-sync",
                "communitymech",
                "audit-network",
                "--communities-dir",
                str((STATE / (name + "-records")).relative_to(ROOT)),
                "--json",
            ]
            if (
                receipt["private_record_sha256"] != sha(ROOT / TARGET)
                or json.loads(log.read_text()) != {}
            ):
                raise ValueError("single-record network result differs")
        if receipt["command"] != expected:
            raise ValueError("native command scope differs: " + gate)
        receipts[gate] = receipt
    inputs = {
        TARGET,
        PRIOR,
        "docs/record-review-profile.md",
        "docs/record-reviews.md",
        "conf/record_review.yaml",
        "conf/reference_validator.yaml",
        "src/communitymech/schema/communitymech.yaml",
        "src/communitymech/schema/mech_shared.yaml",
        "uv.lock",
        "justfile",
        ".claude/skills/curate-yaml-record/SKILL.md",
        ".claude/skills/curate-yaml-record/references/review-checklist.md",
        ".claude/skills/review-communities/reference/metrics-and-reports.md",
        *CACHES.values(),
        str(args.curation_receipt.resolve().relative_to(ROOT)),
    }
    inputs.update(correction["inputs"])
    for pattern in (
        "brachypodium-*.json",
        "brachypodium-*.log",
        "brachypodium-*.exit",
        "brachypodium-*-oak.yaml",
        "candidate-*.log",
        "candidate-*-strict.tsv",
        "grounding-*.json",
        "initial-inspection.json",
        "review-validate-003.log",
        "review-save-003.log",
    ):
        inputs.update(
            str(path.relative_to(ROOT)) for path in STATE.glob(pattern) if path.stat().st_size
        )
    inputs.update(str(path.relative_to(ROOT)) for path in (ROOT / HISTORY).glob("*.yaml"))
    for name in (
        "frontiers-1649750.xml",
        "frontiers-1649750.xml.receipt.json",
        "Data_Sheet_1.zip",
        "Data_Sheet_1.zip.receipt.json",
        "supplementary-tables.xlsx",
        "supplementary-tables.xlsx.extraction.json",
        "supplementary-figures.docx",
        "supplementary-figures.docx.extraction.json",
        "supplementary-figures.txt",
        "ncbi-rcc150-search.json",
        "ncbi-rcc150-search.json.receipt.json",
        "ncbi-bioproject.html.receipt.json",
        "ncbi-study-biosamples.xml.receipt.json",
        "ncbi-rcc150-biosample.xml",
        "ncbi-rcc150-biosample.xml.receipt.json",
    ):
        inputs.add(str((STATE / "sources" / name).relative_to(ROOT)))
    for number in range(1, 7):
        for suffix in (".webp", ".webp.receipt.json"):
            inputs.add(str((STATE / "sources" / (f"figure{number}" + suffix)).relative_to(ROOT)))
    inputs.update(
        str(path.relative_to(ROOT))
        for path in (ROOT / "scripts/adhoc").glob("*brachypodium*20261115.py")
    )
    output.mkdir()
    command = [
        sys.executable,
        "scripts/record_review.py",
        "inspect",
        "--targets",
        str(STATE / "targets.yaml"),
    ]
    for name in sorted(inputs):
        command += ["--input", name]
    inspected_raw = subprocess.check_output(command, cwd=ROOT, text=True)
    (output / "inspection.json").write_text(inspected_raw)
    inspected = json.loads(inspected_raw)
    finished = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    evidence, assessments, checks = [], [], []
    owner = {"repository": REPOSITORY, "path": TARGET, "role": "canonical_record"}

    def ev(key, kind, reference, locator, summary, path, quote=None, support="supports"):
        item = {
            "evidence_id": key,
            "kind": kind,
            "reference": reference,
            "locator": locator,
            "accessed_at": finished,
            "support": support,
            "summary": summary,
            "snapshot_sha256": sha(ROOT / path),
        }
        if quote:
            item["quote"] = quote
        evidence.append(item)

    def assess(key, area, topic, summary, ids, fields, outcome="supported"):
        item = {
            "assessment_id": key,
            "target_ids": [TARGET_ID],
            "area": area,
            "topic": topic,
            "outcome": outcome,
            "summary": summary,
            "evidence_ids": ids,
            "details": "Exact current selectors: " + ", ".join(fields),
        }
        assessments.append(item)
        return item

    xml = str((STATE / "sources/frontiers-1649750.xml").relative_to(ROOT))
    ev(
        "record",
        "record_content",
        TARGET,
        "Entire current record",
        "Fifteen administered stocks, nine arms, eighteen abundance observations, five qualified nodes, zero arrows, four growth-media contexts and preserved earlier history read in full.",
        TARGET,
    )
    ev(
        "prior",
        "prior_review",
        PRIOR,
        "000088 row; source/evidence boundaries",
        "Historical October causal review removed workflow arrows and qualified five biological nodes. It did not inspect original figure pixels or separate supplements. No earlier structured000088 finding head was found in the ignored-inclusive review search or exact coverage ledger; no predecessor is fabricated.",
        PRIOR,
        support="context_only",
    )
    ev(
        "curation",
        "record_content",
        str(args.curation_receipt.resolve().relative_to(ROOT)),
        "Guarded candidate receipt and new history",
        "Exact before/after bytes, native validation and reviewed candidate hash bind the one-record correction; previous inline and sidecar history remain unchanged.",
        str(args.curation_receipt.resolve().relative_to(ROOT)),
    )
    ev(
        "methods",
        "primary_source",
        PAPER,
        "Methods/Microbial isolation and identification; Testing persistence in vitro; Seed germination and SynCom preparation; Inoculation and stress induction",
        "Isolation0.1X R2A/RCH2 agar at30°C seven dark days differs from24–72h R2A isolate preparation of unstated temperature, weekly-transfer liquid0.2X MS at24°C, and host pots of calcined clay. Liquid4×10^7 cells per member differs from plant preparation4.1×10^7;1mL administered aliquot is not enough to infer a per-plant cell dose.",
        xml,
        "Individual SynCom isolates were cultivated in R2A media",
    )
    ev(
        "roster",
        "primary_source",
        PAPER + "#supplementary-material",
        "Original Data Sheet1 ZIP / Supplementary Tables.xlsx / Table S1 rows3–17, columnsA/I/J",
        "All15 stock names are explicit. Row5 identifies MA-N2 RCC-150 with SILVA Micrococcaceae family and blank genus; GTDB-tk MA-N2 species is unfilled. Other GTDB-tk species predictions are computational source analyses, not verified NCBI study-stock identities.",
        str((STATE / "sources/supplementary-tables.xlsx").relative_to(ROOT)),
        "MA-N2 sp. RCC-150",
    )
    ev(
        "authority",
        "database",
        str((STATE / "grounding-roster-004.json").relative_to(ROOT)),
        "Read-only NCBI labels/ranks/ancestry and native hash-bound crosswalk",
        "Earlier genus/family grounding is preserved as context, with all terms verified under Bacteria. Bacterial Bosea has explicit synonym Bosea Das et al.1996 under Allobosea85413; plant homonym169215 is rejected. Final exact sequence-record taxon identities are independently verified in the study metadata receipt. No GTDB latest release/build date is inferred.",
        str((STATE / "grounding-roster-004.json").relative_to(ROOT)),
        support="context_only",
    )
    ev(
        "identity-search",
        "database",
        "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=taxonomy&term=RCC-150&retmode=json",
        "Exact RCC-150 taxonomy search",
        "Early hyphenated RCC-150 query returned0; later actual BioProject/BioSample metadata positively resolves RCC_150. The negative query is historical only and does not support an absence claim.",
        str((STATE / "sources/ncbi-rcc150-search.json").relative_to(ROOT)),
        support="context_only",
    )
    ev(
        "study-identities",
        "database",
        "https://www.ncbi.nlm.nih.gov/bioproject/PRJNA1127609",
        "Current assembly table plus all15 independently retrieved linked BioSamples",
        "Each paper strain maps through its exact numeric designation, BioSample sample-name genus, host and project to one current linked assembly and a native NCBI bacterial sequence taxon. RCC150 sample name Isolate MA-N2 supplies the independent naming link. Pantoea RCC30.1/SAMN57447891 is absent from source S1 and excluded. Current assemblies, particularly the newer Leifsonia accession, are not asserted as the exact versions analyzed in2025.",
        str((STATE / "study-accessions-003.json").relative_to(ROOT)),
    )
    ev(
        "study-mapping",
        "database",
        str((STATE / "study-mapping-001.json").relative_to(ROOT)),
        "Native exact sequence-taxonomy mapping against unchanged crosswalk",
        "All15 sequence-record taxa remain UNRESOLVED under the native named-species mapping policy. Earlier genus/family correspondence is not substituted for a stock-level mapping. Source GTDB-tk predictions remain attributed notes; no missing current crosswalk is fabricated.",
        str((STATE / "study-mapping-001.json").relative_to(ROOT)),
        support="context_only",
    )
    ev(
        "prediction",
        "primary_source",
        PAPER,
        "Table1; genomic-analysis Methods; concluding Discussion",
        "Annotations provide predicted osmoprotectant/transport potential; Table2 tests selected isolate phenotypes. No knockout, complementation, host metabolite transfer or necessary mediation experiment is reported. Positive association networks are correlation estimates rather than demonstrated interstrain cooperation.",
        xml,
        "future experiments exploring gene-expression and metabolite production are needed to confirm",
    )
    ev(
        "liquid",
        "primary_source",
        PAPER,
        "Results/SynCom persistence; original Figure3",
        "Six members were undetectable or below0.1% after3weeks; reported mean16S relative abundances are60% RCC150,26% RCC158 and8% RCC12. Figure3 duplicate bars confirm unequal inoculum/read profiles despite equal input cell counts; none is an absolute viable-cell estimate.",
        xml,
        "average relative abundance of 60, 26 and 8%",
    )
    ev(
        "host",
        "primary_source",
        PAPER,
        "Methods/stress induction; Results; Figures4A–D,5A–C",
        "No significant growth-endpoint benefit under sustained drought; all four measured endpoints improve following rewatering. Salt has a reported shoot-height benefit only, outside the named drought-recovery node. Figures4B/5B include Others, so known inoculum membership cannot be promoted to the entire observed root microbiome. Seven plants/set; five successful rewatered sequencing samples are explicit.",
        xml,
        "No significant differences were observed between SynCom-amended and unamended plants",
    )
    ev(
        "spatial",
        "primary_source",
        PAPER,
        "Results/root spatial localization; Figure6",
        "RCC150 is enriched at tips under drought/rewatering/salt; other strains and conditions differ. Relative16S compartment comparisons do not track migration, prove exudate-guided recruitment, or establish returned osmoprotectants as the cause of recovery.",
        xml,
        "MA-N2 sp. RCC-150 was significantly enriched at the root tip",
    )
    ev(
        "supplement",
        "primary_source",
        PAPER + "#supplementary-material",
        "Supplementary Figures.docx captionsS1–S8; TableS3",
        "S1/S2 are carbon-utilization OD600 assays; S3 compares relative abundance; S5 redundancy and S6 correlation networks are computational. S4 names unreported low-salt results and uses image-day labels distinct from main stress timing; neither omitted conditions nor timing reconciliation is invented. S8 reports triplicate R2A growth curves without specifying isolate-preparation temperature.",
        str((STATE / "sources/supplementary-figures.docx").relative_to(ROOT)),
        support="context_only",
    )
    for number, scope in {
        1: "Selection network displays estimated correlations, not causal arrows.",
        2: "All15 isolate labels and closest-reference tree contextualize phylogeny; reference-genome accessions are not the isolate assemblies.",
        3: "Duplicate liquid16S profiles, strongly unequal week3 abundances.",
        4: "Drought/recovery endpoint contrasts, observed Others and root profiles.",
        5: "Salt endpoint/read-profile contrasts, observed Others and nonsignificant taxon fold changes.",
        6: "Root-tip/base relative abundances differ by stock and condition.",
    }.items():
        ev(
            f"figure{number}",
            "primary_source",
            PAPER,
            f"Original publisher Figure{number}, actual image pixels inspected",
            scope,
            str((STATE / f"sources/figure{number}.webp").relative_to(ROOT)),
        )
    for gate, receipt in receipts.items():
        ev(
            "check-" + gate,
            "validation",
            receipt["log"],
            "Exact native argv and current input/hash receipt",
            "Fresh scoped diagnostic passed; not a full-QC or scientific approval claim.",
            receipt["log"],
            support="context_only",
        )
        checks.append(
            {
                "check_id": gate,
                "name": "Native " + gate,
                "status": "passed",
                "required": True,
                "summary": "Exact current record and retained inputs passed the scoped command.",
                "target_ids": [TARGET_ID],
                "command": shlex.join(receipt["command"]),
                "exit_code": 0,
                "expected_exit_code": 0,
                "evidence_ids": ["check-" + gate],
            }
        )
    checks.append(
        {
            "check_id": "manual-science",
            "name": "Full source and field assessment",
            "status": "passed",
            "required": True,
            "summary": "All present claims,15stock rows,9arms,18observations,5nodes and0arrows assessed against actual primary sources. Passing this check means assessment completed, not all uncertainty resolved.",
            "target_ids": [TARGET_ID],
            "evidence_ids": [
                "record",
                "methods",
                "roster",
                "prediction",
                "liquid",
                "host",
                "spatial",
                "supplement",
            ],
        }
    )
    assess(
        "scope",
        "scope",
        "Administered SynCom and source scope",
        "Identity/category/engineering design denote the15-stock introduced consortium, not every root bacterium. Laboratory setting is physical context; rhizosphere is source/modeled context. No strain roles are invented. Host Bd21–3 is separate from microbial taxonomy and its pre-inoculation microbiological status remains unestablished.",
        ["record", "methods", "host", "authority"],
        [
            "id",
            "name",
            "description",
            "ecological_state",
            "community_origin",
            "community_category",
            "engineering_design",
            "environment_term",
            "modeled_environment",
            "host",
        ],
    )
    for index, row in enumerate(grounding["roster"]):
        stock = stock_ids[row["strain"]]
        stock_assessment = assess(
            f"stock-{index}",
            "grounding",
            row["source_name"],
            f"Table S1 {row['source_cell']} establishes the stock name. BioSample {stock['biosample']} has sample name {stock['sample']['sample_name']}, strain {stock['strain']}, Brachypodium host and project PRJNA1127609; this independently connects the source designation to current assembly {stock['assembly']} and verified sequence taxon {stock['taxon_id']} / {stock['taxon_name']}. NCBI species rank does not imply formal biological species delineation. Prior {row['rank']} context {row['term']['id']} remains attributed separately; source GTDB-tk predictions and current native mapping are distinct. No collection deposit or functional_role is inferred.",
            ["roster", "authority", "study-identities", "study-mapping", "figure2"],
            [
                f"taxonomy[{index}].member_id",
                f"taxonomy[{index}].taxon_term",
                f"taxonomy[{index}].strain_designation",
                f"taxonomy[{index}].evidence",
            ],
            "concern" if row["strain"] == "RCC-150" else "supported",
        )
        stock_assessment["dimensions"] = [
            {
                "name": "source_stock",
                "value": row["source_name"],
                "definition": "Exact paper Table S1 stock designation; not a collection deposit.",
                "evidence_ids": ["roster"],
            },
            {
                "name": "sequence_identity",
                "value": f"{stock['taxon_id']} / {stock['biosample']} / {stock['assembly']}",
                "definition": "Current independently joined study sequence identity; biological species and original analysis versions are separate assertions.",
                "evidence_ids": ["study-identities", "study-mapping"],
            },
        ]
    assess(
        "abundance",
        "scope",
        "Eighteen scoped numerical observations",
        "All15 input observations preserve4×10^7 cells per member in the5mL liquid inoculum, not cells/mL or viable counts. Only three supported week3 mean16S percentages are added (60/26/8); no per-replicate bar values are digitized and no host abundances are assigned through incomplete membership.",
        ["methods", "liquid", "figure3"],
        [f"taxonomy[{index}].abundance_observations" for index in range(15)],
    )
    for index, arm in enumerate(record["treatment_arms"]):
        assess(
            "arm-" + arm["id"],
            "scope",
            arm["name"],
            "Source context, conditions and sampling anchor checked against Methods. "
            + (
                "DEFINED_MEMBERS refers to the complete input15-stock liquid culture, with no assertion of equal later detectability."
                if index == 0
                else "Host membership is NOT_REPORTED and no participant IDs are supplied; known15-stock administration is described without excluding observed Others. Same-condition SynCom/buffer contrast is explicit; buffer-only does not mean axenic. Main stress-day anchor is used without silently reconciling S4 image-day labels."
            ),
            ["methods", "host", "figure3" if index == 0 else "figure4", "supplement"],
            [f"treatment_arms[{index}]"],
        )
    node_summaries = [
        "All15 genomes are the analysis panel, not a claim that all carry every listed gene. Trehalose/betaine and ion transport are predictions; no producer→recipient exchange or realized host mediation is asserted. COMPUTATIONAL/PARTIAL support is appropriate; generic interspecies GO annotation removed because this assay alone establishes none.",
        "All15 isolates form the screened panel; individual positive Table2 assay results differ by strain. IN_VITRO support is appropriate for colorimetric/substrate readouts, not necessary in-planta benefit. No causal transition from annotation to phenotype or host recovery is retained.",
        "All15 are tracked across distinct liquid and host contexts. More balanced host-associated16S profiles coexist with loss/low detection in liquid; the comparison is not a host-only causal perturbation and does not establish absolute viability, reciprocal mutualism, or equal stability.",
        "SynCom versus buffer under rewatered drought directly measures shoot wet weight/height, root length and leaf number. Host is the measured target; GOgrowth is appropriate. Sustained-drought nonbenefit remains in prose, and no gene/metabolite mediator is asserted. Participants identify the administered15-stock community, not all observed root organisms.",
        "All15 comprise the sampled panel; explicit strain/condition qualifications prevent a uniform root-tip preference. Spatial relative16S supports localization, not traced migration, root-exudate recruitment or metabolic exchange. No source→target causal arrow or unsupported effect_direction is introduced.",
    ]
    ids = [
        ["prediction", "figure2"],
        ["prediction", "supplement"],
        ["liquid", "host", "figure3", "figure4", "figure5"],
        ["host", "figure4"],
        ["spatial", "figure6"],
    ]
    for index, (summary, references) in enumerate(zip(node_summaries, ids, strict=True)):
        node = record["ecological_interactions"][index]
        locator = [
            "Genomic-analysis Methods and Table 1",
            "Abstract; Table 2 and phenotypic-assay Methods",
            "Results/SynCom persistence; Figures 3 and 4",
            "Results/Drought recovery; Figure 4A",
            "Abstract; Results/root spatial localization and Figure 6",
        ][index]
        quote_ids = []
        for position, item in enumerate(node["evidence"]):
            key = f"node-{index}-quote-{position}"
            quote_ids.append(key)
            ev(
                key,
                "primary_source",
                PAPER,
                f"{locator}; ecological_interactions[{index}].evidence[{position}]",
                f"Inspected verbatim support classified {item['evidence_source']}/{item['supports']}; the node assessment retains its participant and causal limits.",
                xml,
                item["snippet"],
            )
        node_assessment = assess(
            f"node-{index}",
            "evidence",
            record["ecological_interactions"][index]["name"],
            summary,
            references + quote_ids,
            [
                f"ecological_interactions[{index}]",
                f"ecological_interactions[{index}].participating_taxa",
                f"ecological_interactions[{index}].evidence",
            ],
        )
        node_assessment["dimensions"] = [
            {
                "name": "evidence_tier",
                "value": "; ".join(
                    f"{item['evidence_source']}/{item['supports']}" for item in node["evidence"]
                ),
                "definition": "Assertion-specific evidence tiers, not a causal promotion.",
                "evidence_ids": quote_ids,
            },
            {
                "name": "participants_direction",
                "value": "All fifteen named study stocks form the assessed panel; "
                + (
                    "host is the measured target under rewatered drought."
                    if index == 3
                    else "no pairwise source-to-target direction or causal arrow is assigned."
                ),
                "definition": "Panel membership does not assign every strain every phenotype or imply complete observed host membership.",
                "evidence_ids": references + ["roster"],
            },
            {
                "name": "experimental_context",
                "value": ", ".join(node.get("treatment_arm_ids", [])) or locator,
                "definition": "Exact scoped assay context; preparation, genomic prediction and host benefit remain distinct.",
                "evidence_ids": references + ["methods"],
            },
        ]
    assess(
        "edges",
        "evidence",
        "Zero downstream causal edges",
        "All five nodes have zero downstream arrows. Prior seven workflow edges remain absent; selection/network correlation, genomic potential, isolate assays, persistence and host benefit are not fabricated sequential mechanisms.",
        ["record", "prior", "prediction", "figure1"],
        ["ecological_interactions[*].downstream"],
    )
    assess(
        "protocols",
        "scope",
        "Four distinct cultivation contexts and one liquid setup",
        "Original isolation0.1X R2A/RCH2 and30°C/dark7d are distinct from R2A24–72h isolate preparation with no reported temperature; liquid0.2XMS50mL weeklytransfer24°C differs from host calcined-clay watering/stress. No8h dark phase or shaker speed is inferred. Existing cultivation_setup is correctly scoped to the liquid experiment.",
        ["methods", "supplement"],
        ["growth_media", "cultivation_setup", "environmental_factors"],
    )
    assess(
        "ingredients",
        "evidence",
        "Potential osmoprotectants versus realized mechanism",
        "CHEBItrehalose27082 and glycinebetaine17750 preserve molecule identity. Relevance now describes genome-predicted potential; neither metabolite is asserted to be produced/transferred or required for host recovery. Native term validation supports identity, not function.",
        ["prediction", "check-terms"],
        ["related_ingredients", "ecological_interactions[0].metabolites"],
    )
    assess(
        "discussions",
        "evidence",
        "Historical coverage and current identity boundary",
        "Older discussion retains its historical date and causal-review account. New discussion records inspected primary/supplement/figure coverage and actual15BioSample/assembly resolution. RCC150's biological genus/species and exact original analysis versions remain unknown; the earlier negative name query is superseded by positive study metadata. PRJNA1127609 is added with exact scope; KBase135275 remained inaccessible and is not promoted to inspected evidence.",
        [
            "prior",
            "roster",
            "identity-search",
            "study-identities",
            "study-mapping",
            "figure2",
            "prediction",
        ],
        ["discussions", "associated_datasets"],
    )
    assess(
        "history",
        "provenance",
        "Append-only one-record curation",
        "Exact reviewed bytes applied through native validation, with new inline event and sidecar. Initial candidate002's plant-Bosea failure is preserved; bacterial synonym/ancestry correction was validated rather than bypassing the #365 domain guard.",
        ["curation", "check-history", "authority"],
        ["curation_history", HISTORY],
    )
    ev(
        "coverage-gap",
        "record_content",
        "src/communitymech/schema/mech_shared.yaml",
        "SupportingReference.snippet / Discussion.evidence",
        "At this exact base, discussion snippets lack native source-excerpt annotations. Automated success covers annotated EvidenceItem surfaces; all present discussion assertions were separately manually assessed. Total checks is an issue/result counter, not an excerpt-count denominator.",
        "src/communitymech/schema/mech_shared.yaml",
        support="context_only",
    )
    assess(
        "machine-boundary",
        "evidence",
        "Native coverage boundary",
        "Nine focused diagnostics do not imply full QC, automated discussion coverage, or scientific approval. Reference gate uses unchanged private cache with --no-full-text and native cache-hit preflight. #476 belongs to upstream shared schema integration, not a local source waiver.",
        ["coverage-gap", "check-references", "check-network"],
        ["discussions", "ecological_interactions"],
        "concern",
    )
    findings = []
    for key, severity, native, title, description, fields, ids, issue in [
        (
            "stock-identity",
            "minor",
            "P3",
            "Biological classification and original analysis versions remain bounded",
            "All15 exact sequence-record taxa and current stock assemblies are verified through primary BioSamples. RCC150 remains biologically unclassified at genus/species despite sequence taxon3239231; source SILVA/GTDB-tk labels are attributed analyses. Current linked assembly versions, especially newer Leifsonia, are not independently established as the exact2025analysis inputs. #1548 remains open;000087/000122 are outside this review.",
            ["taxonomy[2]", "discussions[1]"],
            ["roster", "authority", "study-identities", "study-mapping", "figure2"],
            1548,
        ),
        (
            "native-discussion-coverage",
            "minor",
            "P3",
            "Native matcher does not traverse discussion snippets at this base",
            "Manual full-source assessment does not close the existing shared-schema SupportingReference annotation gap or turn the misleading Total checks counter into an assertion count.",
            ["discussions"],
            ["coverage-gap", "check-references"],
            476,
        ),
    ]:
        findings.append(
            {
                "finding_id": key,
                "issue_key": "cm-000088-" + key,
                "category": "grounding" if key == "stock-identity" else "evidence",
                "severity": severity,
                "native_severity": native,
                "normalization_reason": (
                    "Remaining classification and original-analysis-version limits are explicit; stock sequence identities are now verified and no false precision is introduced."
                    if key == "stock-identity"
                    else "Confirmed automated coverage gap, with separate manual source checking; not a demonstrated biological falsehood."
                ),
                "rule_id": "review-checklist.claim-specific-support-and-context",
                "status": "open",
                "certainty": "confirmed",
                "title": title,
                "description": description,
                "target_ids": [TARGET_ID],
                "field_paths": fields,
                "owner_paths": [owner],
                "evidence_ids": ids,
                "external_issues": [
                    f"https://github.com/CultureBotAI/CommunityMech/issues/{issue}"
                ],
            }
        )
    actions = [
        {
            "action_id": "followup-" + item["finding_id"],
            "description": item["description"],
            "finding_ids": [item["finding_id"]],
            "target_ids": [TARGET_ID],
            "owner_paths": [owner],
            "acceptance_checks": [
                "For1548, resolve RCC150biological classification and exact original analysis versions if primary evidence permits; preserve verified current stock identities and other records' unresolved scope.",
                "For476, integrate the canonical shared annotation fix and measure actual assertion traversal; retain source identity/quality boundaries and recheck this record.",
            ],
        }
        for item in findings
    ]
    avg = sum(len(node.get("evidence", [])) for node in record["ecological_interactions"]) / 5
    score = max(0, min(100, 100 - 4 + min(avg / 2, 1) * 20 + 15))
    metric = assess(
        "metrics",
        "completeness",
        "Literal native metrics",
        "Completeness35/100 does not reward invented roles/resources. Validation-quality100/100 follows the capped formula despite retained findings; it is not a scientific clearance score.",
        ["record", "check-network"],
        ["taxonomy", "ecological_interactions"],
    )
    metric["metrics"] = [
        {
            "name": "completeness",
            "value": 35,
            "unit": "points",
            "minimum": 0,
            "maximum": 100,
            "definition": "Required role block0; environment5; ≥3factors0; ≥3nodes10; resources0; media10; verified dataset5; node metabolites5.",
        },
        {
            "name": "validation_quality",
            "value": score,
            "unit": "points",
            "minimum": 0,
            "maximum": 100,
            "definition": "Clamp0–100 of100−50*P1−10*P2−2*P3+min((evidence/node)/2,1)*20+15if network complete; review counts P1=0,P2=0,P3=2, native network={} passes. This is not a scientific verdict.",
        },
        {
            "name": "evidence_per_interaction",
            "value": avg,
            "denominator": 5,
            "unit": "evidence items per node",
            "definition": "Eight annotated EvidenceItems over five actual biological nodes; no downstream arrows.",
        },
        {
            "name": "source_stock_roster",
            "value": 15,
            "denominator": 15,
            "unit": "source stock names",
            "definition": "15Table S1stocks independently linked to15BioSamples/current assemblies and native NCBI sequence taxa; not biological species delineation or proof of original analysis versions.",
        },
    ]
    review = {
        "schema_version": "1.0.0",
        "review_id": stamp + "-phase2-brachypodium-drought",
        "kind": "record",
        "repository": REPOSITORY,
        "title": "Brachypodium15 source-stock, assay and mechanistic-scope reassessment",
        "started_at": datetime.fromtimestamp(
            (STATE / "initial-inspection.json").stat().st_mtime, timezone.utc
        ).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "finished_at": finished,
        "reviewer": {
            "identity": "codex-pr-review",
            "kind": "agent",
            "independence": "self_review",
            "independence_basis": "Authored bounded curation after independent primary inspection; parent separately reviews the staged candidate and final bundle.",
        },
        "skill": "curate-yaml-record",
        "completion": "completed",
        "verdict": "needs_curation",
        "scientific_review": True,
        "summary": "All present000088 claims assessed against the actual primary article, Figures1–6, relevant separate supplements and15primary BioSamples;15source stocks now have verified current assemblies and sequence taxa. Protocol/arm contexts remain distinct. Five qualified nodes and zero causal arrows retained. Nine scoped native gates passed. Biological classification/original-version limits and native SupportingReference coverage remain explicit; no full-corpus/Phase2 completion or issue closure is claimed.",
        "source": inspected["source"],
        "targets": inspected["targets"],
        "scope": {
            "description": "Entire current000088:15stock rows,18scoped numerical observations,9arms,5nodes,0arrows,4growth-media contexts,1liquid setup,2discussions and append-only history.",
            "selection": "Explicit Phase2 #1548 target after the separate000087 end-to-end canary; not the all-record campaign.",
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
            "Current study-stock assemblies and sequence-record taxa are verified. RCC150biological genus/species and exact original analysis versions remain unresolved; no reference-genome accession, collection deposit or ecological role is invented.",
            "Main article and all6primary figures inspected; original S1/S3tables and all supplemental captions inspected. Separate supplemental figure pixels and raw sequencing/statistical reanalysis are outside this assessment.",
            "Native exact sequence-taxon mappings are unresolved for all15under the unchanged named-species policy. Earlier genus/family correspondence and paper GTDB-tk analyses remain separate provenance; no current stock mapping or release/build date is invented.",
            "Host inoculum is known but complete observed root microbiomes are not; all host arms use NOT_REPORTED and buffer controls are never called microbe-free.",
            "Main21-day post-stress anchor differs from S4image-day labels; excluded low-salt results and any apparent timing discrepancy are not reconstructed.",
            "Native discussion/dataset SupportingReference coverage remains #476 at this base. New database metadata were manually verified through exact source artifacts; a native lexical pass is not database-identity validation. Actual publisher XML and supplements were inspected independently of the existing cache.",
            "Whole-record generated Python YAMLreload #1703 remains an independent infrastructure blocker; native closed-schema/strict success is not a claim that this separate roundtrip defect is resolved.",
            "Initial grounding request failed on disambiguated Bacillus label and a later staged candidate failed the correct plant-Bosea domain guard (#365). Failed artifacts remain retained; final ancestry verification and native gates use corrected exact bytes.",
            "An initial review draft used invalid target kind record instead of maintained; native validate/save rejected it. The source record and scientific judgments were unchanged, and final review metadata uses the native enum.",
            "No canonical cache edits, other-record curation, paid providers, issue closure, merge, or global scientific approval is performed. The000087/000122 parts of1548 and all-record campaign remain outside scope.",
        ],
        "links": [
            PAPER,
            "https://github.com/CultureBotAI/CommunityMech/issues/1548",
            "https://github.com/CultureBotAI/CommunityMech/issues/365",
            "https://github.com/CultureBotAI/CommunityMech/issues/476",
            "https://github.com/CultureBotAI/CommunityMech/issues/1703",
        ],
    }
    (output / "review.yaml").write_text(
        yaml.dump(review, Dumper=NoAliasDumper, sort_keys=False, allow_unicode=True, width=106)
    )
    print(
        json.dumps(
            {
                "review_id": review["review_id"],
                "assessments": len(assessments),
                "checks": len(checks),
                "open_findings": len(findings),
                "output": str((output / "review.yaml").relative_to(ROOT)),
            }
        )
    )


if __name__ == "__main__":
    main()
