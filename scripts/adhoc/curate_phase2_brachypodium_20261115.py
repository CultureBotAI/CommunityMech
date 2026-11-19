"""Stage/apply the source-backed 000088 correction for #1548, 2026-11-15.

Inputs: exact baseline, publisher XML/S1 and read-only authority receipts.
Outputs: exclusive private candidate/proof; applying requires the exact reviewed
candidate SHA. Only the named record may change. Native closed-schema validation
and curation events are mandatory; old history, other records and caches survive.
"""

import argparse
import copy
import hashlib
import json
import re
import sys
import unicodedata
from datetime import datetime, timezone
from pathlib import Path

import yaml
from defusedxml import ElementTree

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))
from communitymech.curate.curation_event import (  # noqa: E402
    append_curation_event_text,
    record_curation_event,
)
from communitymech.validation.write_validated import write_validated_community  # noqa: E402

STATE = ROOT / ".temp/phase2-brachypodium-20261115"
TARGET = "kb/communities/LBNL_Brachypodium_Drought_SynCom15.yaml"
BEFORE = "a7e41d95bc05106486f450153065da247369b854b757d68d451bea5e64e0b8e4"
SOURCE_SHA = {
    "sources/frontiers-1649750.xml": "36e66b7e040c63f7f6f549f8a2ef9b8546ba5d25802fd42b82679ad7a3d80db6",
    "sources/supplementary-tables.xlsx": "a211278cce04d6293896949eb171f842f17ca13cc2c65e1526722ef6cecab669",
    "sources/supplementary-figures.docx": "0c2f4ca3ab49f6e5169023078e9e157f186164f6a9bb97d7410bf9c87063ae33",
    "sources/ncbi-bioproject.html": "346d5bfd0d68dc83636fcd94c0dd62c89767feb62e5f55fe13e047a808eecb0b",
    "sources/ncbi-study-biosamples.xml": "a7f44544d2a94e22f76272c91d882467a0184eb7ddcced7774a11b559e1e5a59",
}
SUMMARY = (
    "Resolved the 15 source-designated inoculum stocks to source-linked BioSamples, current assemblies and verified NCBI sequence-record taxa; "
    "RCC-150 retains the source MA-N2 name and attributed Micrococcaceae classification, with an exact unclassified-bacterium taxon and unresolved biological genus/species. "
    "Separated isolation, isolate preparation, liquid culture and plant protocols; corrected 0.1X R2A and the two differently scoped inoculum cell counts. "
    "Removed unsupported CROSS_FEEDER and realized osmoprotectant mediation claims. Added source-defined arms, explicit host context and three mean 16S abundance observations. "
    "Host-arm membership remains NOT_REPORTED because observed root profiles contain other bacteria; taxonomy describes the administered SynCom. "
    "Preserved five qualified nodes and zero arrows. Current linked assemblies are not asserted as exact versions used in the paper; later project Pantoea is excluded. Addresses only the 000088 portion of multi-record #1548; biological classification and analysis-version uncertainty remain."
)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def norm(text):
    return " ".join(unicodedata.normalize("NFKC", text).split())


class CanonicalLoader(yaml.SafeLoader):
    """Reject duplicate keys without rejecting harmless old YAML aliases."""

    def construct_mapping(self, node, deep=False):
        keys = [self.construct_object(key, deep=deep) for key, _ in node.value]
        if len(keys) != len(set(keys)):
            raise ValueError("duplicate YAML key")
        return super().construct_mapping(node, deep=deep)


def load(raw):
    return yaml.load(raw, Loader=CanonicalLoader)  # noqa: S506 -- SafeLoader subclass


def evidence(snippet, explanation, source="IN_VITRO", support="SUPPORT"):
    return {
        "reference": "PMID:40862137",
        "supports": support,
        "evidence_source": source,
        "snippet": snippet,
        "explanation": explanation,
    }


def condition(name, value, unit=None):
    result = {"name": name, "value": str(value)}
    if unit:
        result["unit"] = unit
    return result


def build(original, grounding, studies):
    before = load(original)
    after = copy.deepcopy(before)
    after["description"] = (
        "The defined 15-stock bacterial inoculum assembled from Brachypodium rhizobiome isolates. "
        "In plant experiments it improved measured growth endpoints after drought followed by rewatering; sustained drought did not show those improvements. "
        "The administered SynCom is not the complete observed root microbiome, which also contained other bacteria. Liquid-culture persistence was unequal."
    )
    design = after["engineering_design"]
    design["objective"] = (
        "Test a network- and cultivation-guided 15-stock bacterial inoculum for persistence and effects on Brachypodium under drought, rewatering and salinity."
    )
    design["inoculation_strategy"] = (
        "Distinct preparations: 5 mL liquid-assay inoculum contained 4x10^7 cells of each member and was added to 45 mL 0.2X MS. "
        "For plant experiments, individual suspensions were adjusted to 4.1x10^7 cells before final inoculum preparation; plants received 1 mL of mixed inoculum in 30 mM phosphate buffer. "
        "The preparation count is not asserted as cells/mL or a per-plant dose."
    )
    design["perturbation_design"] = (
        "Separate three-week weekly-transfer liquid assay and host control/drought/rewatered-drought/salinity arms with SynCom or buffer."
    )
    after["environment_term"] = {
        "preferred_term": "laboratory environment",
        "term": {"id": "ENVO:01001405", "label": "laboratory environment"},
        "notes": "Physical setting of chamber-grown liquid cultures and potted Brachypodium in autoclaved calcined clay; original rhizobiome provenance is not the liquid assay substrate.",
    }
    after["modeled_environment"] = [
        {
            "preferred_term": "rhizosphere",
            "term": {"id": "ENVO:00005801", "label": "rhizosphere"},
            "notes": "Original isolate provenance and the plant-associated ecological context modeled by this administered inoculum.",
        }
    ]
    after["host"] = {
        "preferred_term": "Brachypodium distachyon",
        "term": {"id": "NCBITaxon:15368", "label": "Brachypodium distachyon"},
        "genotypes": [{"name": "Bd 21–3"}],
        "anatomical_sites": [
            {
                "preferred_term": "root tip and root base",
                "description": "Separate 2 cm root-tip and root-base samples after three weeks of stress induction; no unverified anatomical CURIE assigned.",
            }
        ],
        "microbial_status": "NOT_REPORTED",
        "description": "Seed surface sterilization and sterile materials are reported, but absence of detectable resident microbes before inoculation was not established. Figures 4B/5B include other bacterial groups. This host is not a microbial member.",
        "evidence": [
            evidence(
                "seeds were dehusked and sterilized",
                "Methods/Seed germination and SynCom preparation names Brachypodium distachyon (Bd 21–3); sterility procedures alone do not establish an axenic starting host.",
                "IN_VIVO",
            )
        ],
    }
    taxa = []
    stocks = {row["paper_stock"]: row for row in studies["roster"]}
    for row in grounding["roster"]:
        stock = stocks[row["strain"]]
        term = {
            "preferred_term": row["source_name"],
            "term": {"id": stock["taxon_id"], "label": stock["taxon_name"]},
            "notes": f"Source Table S1 {row['source_cell']}; exact sequence-record taxon verified through BioSample {stock['biosample']} with sample name {stock['sample']['sample_name']}, stock {stock['strain']}, host and project PRJNA1127609. NCBI species rank here is a sequence taxon, not formal biological species delineation. Separately verified {row['rank']} context: {row['term']['id']} {row['term']['label']}. Source GTDB-tk analysis: {row['source_gtdb_tk_classification']}; not a current crosswalk or reanalysis of the linked assembly.",
        }
        mapping = stock["native_sequence_taxon_mapping"]
        if mapping is None:
            term["gtdb_grounding_status"] = "UNRESOLVED"
        elif mapping.get("ambiguous"):
            term["gtdb_grounding_status"] = "AMBIGUOUS"
            term["gtdb_candidates"] = mapping["gtdb_options"]
        else:
            term["gtdb_grounding_status"] = "GROUNDED"
            term["gtdb_classification"] = {
                k: v for k, v in mapping.items() if k not in {"via", "n_alt"}
            }
            term["gtdb_classification"][
                "mapping_source"
            ] = f"kg-microbe NCBI2GTDB.tsv.gz sha256:{studies['mapping_sha256']}; native sequence-record taxon mapping, named species only; release/build not independently established"
        if row["strain"] == "RCC-150":
            term[
                "notes"
            ] += " MA-N2 is the source GTDB genus label. Table S1!I5 attributes this stock to Micrococcaceae but leaves SILVA genus empty. NCBITaxon:3239231 is bacterium RCC_150 under unclassified Bacteria; the source family classification is not asserted as the NCBI lineage. Biological genus/species remain unresolved; no inferred alias."
        if row["strain"] == "RCC-152.1":
            term[
                "notes"
            ] += " The source names bacterial Bosea; the linked sample's sequence taxon is Allobosea sp. RCC_152_1. Native Allobosea85413 records synonym Bosea Das et al. 1996 and Bacteria ancestry; unrelated plant homonym Bosea169215 is excluded."
        taxa.append(
            {
                "member_id": row["strain"].lower().replace(".", "-"),
                "taxon_term": term,
                "strain_designation": {
                    "strain_name": row["strain"],
                    "genome_accession": stock["assembly"],
                    "genome_url": stock["assembly_url"],
                    "isolation_source": "Brachypodium rhizobiome enrichment collection described in Methods/Microbial isolation and identification.",
                    "notes": f"Exact paper stock name preserved. Primary BioSample https://www.ncbi.nlm.nih.gov/biosample/{stock['biosample']} independently links {stock['strain']} to sample name {stock['sample']['sample_name']}, Brachypodium host and the paper's BioProject; linkage is not based on punctuation alone. Assembly is the current project-linked accession verified 2026-11-15, not necessarily the version used in 2025 (particularly Leifsonia RCC-180). Figure 2 closest-reference genomes are not copied to this stock.",
                },
                "evidence": [
                    evidence(
                        row["source_name"],
                        f"Table S1 {row['source_cell']} lists the stock and source classifications; main tables/figures also name it. This quotation supports the paper stock name. Current taxon/assembly identity is separately supported by BioSample {stock['biosample']} and its linked BioProject, as recorded in strain_designation notes; those accessions are not claimed to appear in this paper quotation.",
                    )
                ],
            }
        )
    if len(taxa) != 15 or len({t["member_id"] for t in taxa}) != 15:
        raise ValueError("source roster multiplicity changed")
    after["taxonomy"] = taxa
    after["associated_datasets"] = [
        {
            "accession": "PRJNA1127609",
            "title": "A stable 15-member bacterial SynCom promotes Brachypodium growth under drought stress",
            "dataset_type": "GENOMICS",
            "repository": "NCBI_BIOPROJECT",
            "url": "https://www.ncbi.nlm.nih.gov/bioproject/PRJNA1127609",
            "publication": "PMID:40862137",
            "description": "Publication-linked sequence project. Fifteen source-stock BioSamples were individually reconciled; current project also contains Pantoea RCC30.1/SAMN57447891, absent from the paper's Table S1 and excluded from this SynCom. Current assembly versions may postdate the paper and are not asserted as exact inputs to its genome analysis.",
            "evidence": [
                {"reference": "PMID:40862137", "supports": "SUPPORT", "snippet": "PRJNA1127609"}
            ],
        }
    ]
    ids = [t["member_id"] for t in taxa]
    arms = [
        {
            "id": "liquid-ms",
            "name": "Weekly-transfer 0.2X MS liquid culture",
            "context": "in-vitro three-week liquid persistence assay",
            "membership_status": "DEFINED_MEMBERS",
            "participant_member_ids": ids,
            "conditions": [
                condition("medium", "0.2X MS"),
                condition("temperature", 24, "degrees Celsius"),
                condition("light duration", 16, "hours"),
                condition("relative humidity", 50, "percent"),
            ],
            "timepoints": [
                {"id": "inoculum", "name": "Initial inoculum before weekly transfers"},
                {
                    "id": "week-three",
                    "name": "End of week 3",
                    "reference_event": "start of the liquid culture experiment",
                },
            ],
            "description": "Complete administered 15-stock culture roster, not a claim that all members remained detectable. Each week 5 mL was transferred into 45 mL fresh medium. Equal input cell numbers do not imply equal sequencing-read fractions.",
            "evidence": [
                evidence(
                    "At the end of each week",
                    "Methods/Testing the persistence of the SynCom in vitro specifies 5 mL into 45 mL, weekly transfer, 4x10^7 input cells per member and three-week follow-up.",
                )
            ],
        }
    ]
    host_context = "potted Bd 21–3 stress and recovery experiment"
    schedules = {
        "control": "80% saturation weight throughout",
        "drought": "40% saturation weight for 21 days after stress induction",
        "rewatered": "14 days drought at 40% saturation weight, then 80% during the final week",
        "salinity": "80% saturation weight with 60 mM NaCl in 0.2X MS",
    }
    for label, schedule in schedules.items():
        for amendment in ("syncom", "buffer"):
            arm_id = f"host-{label}-{amendment}"
            other = "buffer" if amendment == "syncom" else "syncom"
            arms.append(
                {
                    "id": arm_id,
                    "name": f"{label.capitalize()} with {'SynCom' if amendment == 'syncom' else 'buffer only'}",
                    "context": host_context,
                    "membership_status": "NOT_REPORTED",
                    "comparator_arm_ids": [f"host-{label}-{other}"],
                    "conditions": [
                        condition("water/stress schedule", schedule),
                        condition("host line", "Bd 21–3"),
                        condition(
                            "amendment",
                            (
                                "1 mL mixed SynCom in 30 mM phosphate buffer"
                                if amendment == "syncom"
                                else "1 mL 30 mM phosphate buffer"
                            ),
                        ),
                        condition("temperature", 24, "degrees Celsius"),
                        condition("light duration", 16, "hours"),
                        condition("relative humidity", 50, "percent"),
                    ],
                    "timepoints": [
                        {
                            "id": "harvest",
                            "name": "Harvest 21 days after stress induction",
                            "reference_event": "stress induction, three days after SynCom or buffer inoculation",
                        }
                    ],
                    "description": "Seven plant replicates per set; rewatered 16S analysis had five successful samples (Figure 4 caption). "
                    + (
                        "The administered inoculum comprises the 15 stocks in taxonomy; this does not enumerate every observed root microbe. "
                        if amendment == "syncom"
                        else "Buffer-only amendment does not establish a microbe-free host. "
                    )
                    + "Complete host-associated microbial membership is NOT_REPORTED: Figures 4B/5B explicitly include Others. Source Supplementary Figure S4 mentions an additional low-salt set whose results were not included; that set is not reconstructed here.",
                    "evidence": [
                        evidence(
                            "Each experimental set contained 7 plant replicates",
                            "Methods/Inoculation of SynCom and induction of environmental stresses; the following paragraph specifies control, drought, rewatering and 60 mM salinity schedules and the harvest anchor.",
                            "IN_VIVO",
                        )
                    ],
                }
            )
    after["treatment_arms"] = arms
    for taxon in taxa:
        observations = [
            {
                "treatment_arm_id": "liquid-ms",
                "timepoint_id": "inoculum",
                "measurement_basis": "source-reported cell count in the 5 mL starting inoculum; not a concentration, viable count or 16S read fraction",
                "absolute_abundance": 40000000.0,
                "absolute_abundance_unit": "cells per member in the starting 5 mL inoculum",
                "description": "Methods reports equal 4x10^7 cells of each member for the liquid assay. This is distinct from the 4.1x10^7 preparation count for plant inoculation.",
                "evidence": [
                    evidence(
                        "containing equal cell numbers",
                        "Methods/Testing the persistence of the SynCom in vitro gives the 4x10^7 cell count in the 5 mL inoculum; no concentration conversion is made.",
                    )
                ],
            }
        ]
        means = {"rcc-150": 60.0, "rcc-158": 26.0, "rcc-12": 8.0}
        if taxon["member_id"] in means:
            observations.append(
                {
                    "treatment_arm_id": "liquid-ms",
                    "timepoint_id": "week-three",
                    "replicate": "reported mean of the two liquid replicates",
                    "measurement_basis": "16S rRNA amplicon relative abundance; not absolute viable abundance",
                    "relative_abundance": means[taxon["member_id"]],
                    "relative_abundance_unit": "PERCENT",
                    "description": "Rounded mean reported in Results and Figure 3; individual replicate values were not digitized from bars.",
                    "evidence": [
                        evidence(
                            "average relative abundance of 60, 26 and 8%",
                            "Results/SynCom persistence and growth: respectively MA-N2 RCC-150, Paraburkholderia RCC-158 and Chitinophaga RCC-12 at week 3.",
                        )
                    ],
                }
            )
        taxon["abundance_observations"] = observations
    nodes = after["ecological_interactions"]
    if len(nodes) != 5 or any(node.get("downstream") for node in nodes):
        raise ValueError("unexpected baseline graph")
    participants = [
        {
            "preferred_term": t["taxon_term"]["preferred_term"],
            "term": copy.deepcopy(t["taxon_term"]["term"]),
        }
        for t in taxa
    ]
    for node in nodes:
        node["participating_taxa"] = copy.deepcopy(participants)
    for index in (0, 1, 2, 4):
        nodes[index].pop("biological_processes", None)
    nodes[0][
        "description"
    ] += " The panel comprises all 15 sequenced isolates; individual genes and positive traits differ by strain (Table 1), so no trait is assigned uniformly to every member."
    nodes[1][
        "description"
    ] += " Table 2 reports strain-specific assay outcomes; inclusion in the screened panel does not mean every member was positive for each trait."
    nodes[2]["treatment_arm_ids"] = ["liquid-ms"] + [
        arm["id"] for arm in arms if arm["id"].endswith("-syncom")
    ]
    nodes[3]["treatment_arm_ids"] = ["host-rewatered-syncom", "host-rewatered-buffer"]
    nodes[3]["host_participation"] = "HOST_IS_TARGET"
    nodes[4]["treatment_arm_ids"] = [arm["id"] for arm in arms if arm["id"].endswith("-syncom")]
    nodes[4][
        "description"
    ] += " The 15 entries identify the sequenced panel, not a uniform root-tip preference. No movement of individually tracked cells was measured."
    after["environmental_factors"] = [
        {
            "name": "assay context",
            "value": "distinct liquid persistence and host stress/recovery experiments",
            "description": "Named treatment_arms preserve schedules and comparators; the host profiles include other bacteria beyond the administered 15-stock SynCom.",
            "evidence": [
                evidence(
                    "while all other bacterial groups are combined into the",
                    "Figures 4B and 5B captions identify the separate Others category; this record does not claim complete observed root membership.",
                    "IN_VIVO",
                )
            ],
        }
    ]
    for ingredient in after["related_ingredients"]:
        ingredient["relevance"] = (
            "Genome-predicted osmoprotectant biosynthetic potential in the isolate panel. Production, transfer to the host and necessary mediation of recovery were not established."
        )
        for item in ingredient["evidence"]:
            item["supports"] = "PARTIAL"
            item["explanation"] = (
                "Supports encoded biosynthetic potential only; the paper calls for gene-expression and metabolite-production experiments."
            )
    after["growth_media"] = [
        {
            "name": "0.1X R2A or supplemented RCH2 agar for original isolation",
            "temperature": "30",
            "temperature_unit": "°C",
            "incubation_time": "7",
            "incubation_time_unit": "days",
            "light_regime": "dark",
            "preparation_notes": "Methods uses 0.1X R2A and RCH2 minimal medium supplemented with glutamine or mixed carbon to recover colonies on corresponding agar plates. This is the original isolation stage, not the temperature of later individual-isolate preparation.",
            "evidence": [
                evidence(
                    "0.1X R2A",
                    "Methods/Microbial isolation and identification specifies corresponding agar plates at 30°C in the dark for seven days.",
                )
            ],
        },
        {
            "name": "R2A for individual-isolate inoculum preparation",
            "incubation_time": "24-72",
            "incubation_time_unit": "h",
            "preparation_notes": "Individual isolates were grown to log phase, purity checked, washed three times and resuspended in 30 mM phosphate buffer. SYBR-green flow cytometry informed equal cell-number adjustment to 4.1x10^7 cells for the final plant inoculum. The source does not specify the temperature of this preparation step; plant chamber conditions are not borrowed.",
            "evidence": [
                evidence(
                    "Individual SynCom isolates were cultivated in R2A media",
                    "Methods/Seed germination and SynCom preparation and Figure S8; duration 24–72 h, not the original seven-day isolation protocol.",
                )
            ],
        },
        {
            "name": "0.2X MS for weekly-transfer liquid community culture",
            "temperature": "24",
            "temperature_unit": "°C",
            "light_regime": "16 h light (reported)",
            "preparation_notes": "5 mL inoculum into 45 mL 0.2X MS; weekly 5-to-45 mL transfers for three weeks; 50% relative humidity. Initial inoculum contains 4x10^7 cells per member. Agitation and the unreported dark interval are not inferred.",
            "evidence": [
                evidence(
                    "The mixture was incubated in a plant growth chamber",
                    "Methods/Testing the persistence of the SynCom in vitro; 16-h light, 24°C and 50% humidity apply to this liquid assay.",
                )
            ],
        },
        {
            "name": "0.2X MS watering medium for potted Brachypodium",
            "temperature": "24",
            "temperature_unit": "°C",
            "light_regime": "16 h light (reported)",
            "preparation_notes": "Sterilized pots with autoclaved calcined clay; seedlings germinated separately on 0.5X MS plus 0.4% phytagel for 3–5 days. Pot watering schedules and SynCom/buffer amendment are scoped in treatment_arms. Host chamber humidity was 50%; this temperature is not asserted for isolate preparation.",
            "evidence": [
                evidence(
                    "The clay was saturated with 0.2X MS media",
                    "Methods/Seed germination and SynCom preparation establishes the pot substrate and watering medium; following stress Methods gives chamber conditions.",
                    "IN_VIVO",
                )
            ],
        },
    ]
    after["discussions"].append(
        {
            "discussion_id": "brachypodium_source_stock_identity",
            "prompt": "What biological genus/species describes MA-N2 RCC-150, and which assembly versions were used in the original analysis?",
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "attaches_to": ["taxonomy"],
            "rationale": "The 2026-11-15 follow-up inspected the publisher article, Figures 1–6, separate Table S1/supplement captions, linked BioProject and all 15 corresponding BioSamples. It supersedes the older discussion's historical coverage limitation for those sources. Exact stocks now have verified sequence-record taxa and current project-linked assemblies. RCC-150 is NCBI bacterium RCC_150/3239231, BioSample SAMN42017417 (sample name Isolate MA-N2), assembly GCA_041360635.1; this identifies the sequence record without resolving biological genus/species. Source SILVA Micrococcaceae and GTDB-tk MA-N2 are attributed analyses, not the NCBI unclassified-Bacteria lineage. Current Leifsonia assembly differs in time from the paper; exact analysis versions remain unverified. Figure 2 closest-reference accessions are not study-stock assemblies. #1548 remains open for these boundaries and other records. No raw sequence reanalysis or selective mediation experiment was performed.",
            "evidence": [
                evidence(
                    "MA-N2 sp. RCC-150",
                    "Table S1!A5/I5/J5: source designation and attributed SILVA/GTDB-tk classifications. Independently inspected BioSample SAMN42017417 links sample name Isolate MA-N2, strain RCC_150, host and project to the exact sequence taxon/assembly; biological classification remains unresolved.",
                )
            ],
            "posed_by": "codex",
            "posed_date": "2026-11-15",
        }
    )
    if after["curation_history"] != before["curation_history"]:
        raise ValueError("old history changed")
    return before, after


def replace_section(text, key, value):
    pattern = rf"(?ms)^{re.escape(key)}:.*?(?=^[A-Za-z_][A-Za-z_0-9]*:|\Z)"
    replacement = yaml.safe_dump({key: value}, sort_keys=False, allow_unicode=True, width=108)
    result, count = re.subn(pattern, lambda _: replacement, text)
    if count != 1:
        raise ValueError(f"expected one original section: {key}")
    return result


def verify_quotes(value, source):
    if isinstance(value, dict):
        if "snippet" in value and norm(value["snippet"]) not in norm(source):
            raise ValueError(f"quotation absent from primary XML: {value['snippet']}")
        for item in value.values():
            verify_quotes(item, source)
    elif isinstance(value, list):
        for item in value:
            verify_quotes(item, source)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--apply-candidate", type=Path)
    parser.add_argument("--expected-candidate-sha256")
    args = parser.parse_args()
    output = args.output.resolve()
    if not output.is_relative_to(STATE) or output.exists() or output.is_symlink():
        raise ValueError("fresh output directory under record state required")
    canonical = ROOT / TARGET
    original = canonical.read_bytes()
    if sha(original) != BEFORE:
        raise ValueError("canonical record changed since inspection")
    for relative, expected in SOURCE_SHA.items():
        if sha((STATE / relative).read_bytes()) != expected:
            raise ValueError(f"primary input changed: {relative}")
    if args.apply_candidate:
        candidate_path = args.apply_candidate.resolve()
        if not candidate_path.is_relative_to(STATE) or not args.expected_candidate_sha256:
            raise ValueError("apply requires private reviewed candidate and explicit hash")
        text = candidate_path.read_text()
        if sha(text.encode()) != args.expected_candidate_sha256:
            raise ValueError("candidate differs from independently reviewed bytes")
        staged_proof = json.loads(candidate_path.with_name("receipt.json").read_text())
        if (
            staged_proof["before_sha256"] != BEFORE
            or staged_proof["after_sha256"] != args.expected_candidate_sha256
        ):
            raise ValueError("staging receipt does not bind candidate")
        for relative, expected in staged_proof["inputs"].items():
            if sha((ROOT / relative).read_bytes()) != expected:
                raise ValueError(f"staged input changed: {relative}")
        candidate = load(text)
        if (
            candidate["id"] != "CommunityMech:000088"
            or candidate["curation_history"][:-1] != load(original)["curation_history"]
        ):
            raise ValueError("reviewed candidate target/history mismatch")
        inputs = staged_proof["inputs"]
    else:
        if args.expected_candidate_sha256:
            raise ValueError("candidate hash is only an apply guard")
        grounding_path = STATE / "grounding-roster-004.json"
        grounding = json.loads(grounding_path.read_text())
        if (
            grounding["table_sha256"] != SOURCE_SHA["sources/supplementary-tables.xlsx"]
            or not grounding["ontology"]["sha256"]
        ):
            raise ValueError("unbound source/authority grounding")
        if any(
            row["verified_domain_ancestors"] != [["NCBITaxon:2"]] for row in grounding["roster"]
        ):
            raise ValueError("every source stock requires verified bacterial ancestry")
        study_path = STATE / "study-mapping-001.json"
        identity_path = STATE / "study-accessions-003.json"
        studies = json.loads(study_path.read_bytes())
        identities = json.loads(identity_path.read_bytes())
        if studies["identity_receipt_sha256"] != sha(identity_path.read_bytes()) or studies[
            "authority_receipt_sha256"
        ] != sha(grounding_path.read_bytes()):
            raise ValueError("study mapping is not bound to verified identities/authority")
        if len(studies["roster"]) != 15 or any(
            row["verified_domain_ancestors"] != [["NCBITaxon:2"]] for row in studies["roster"]
        ):
            raise ValueError("study sequence-record taxa lack complete bacterial grounding")
        for relative, expected in identities["input_sha256"].items():
            if sha((ROOT / relative).read_bytes()) != expected:
                raise ValueError("study identity primary input changed")
        before, candidate = build(original, grounding, studies)
        source = "".join(
            ElementTree.fromstring(
                (STATE / "sources/frontiers-1649750.xml").read_bytes()
            ).itertext()
        )
        verify_quotes(candidate, source)
        text = original.decode()
        for key in before:
            if before[key] != candidate[key]:
                text = replace_section(text, key, candidate[key])
        for key in candidate.keys() - before.keys():
            text += "\n" + yaml.safe_dump(
                {key: candidate[key]}, sort_keys=False, allow_unicode=True, width=108
            )
        if load(text) != candidate:
            raise ValueError("bounded edits changed semantics")
        event = record_curation_event(
            candidate, curator="codex", action="EDIT", changes=SUMMARY, llm_assisted=True
        )
        text = append_curation_event_text(
            text,
            curator="codex",
            action="EDIT",
            changes=SUMMARY,
            timestamp=event["timestamp"],
            width=108,
        )
        unmarked = {key: value for key, value in event.items() if key != "llm_assisted"}
        old = yaml.safe_dump([unmarked], sort_keys=False, allow_unicode=True, width=108).rstrip()
        if text.count(old) != 1:
            raise ValueError("native event anchor changed")
        text = text.replace(
            old, yaml.safe_dump([event], sort_keys=False, allow_unicode=True, width=108).rstrip(), 1
        )
        if load(text) != candidate:
            raise ValueError("native event append changed semantics")
        paths = [STATE / key for key in SOURCE_SHA] + [
            grounding_path,
            study_path,
            identity_path,
            ROOT / "src/communitymech/schema/communitymech.yaml",
            ROOT / "references_cache/PMID_40862137.txt",
            Path(__file__),
        ]
        inputs = {str(path.relative_to(ROOT)): sha(path.read_bytes()) for path in paths}
    output.mkdir()
    write_validated_community(candidate, output / "validated.yaml")
    if load((output / "validated.yaml").read_bytes()) != candidate:
        raise ValueError("native persisted validation form differs")
    (output / "candidate.yaml").write_text(text)
    (output / "before.yaml").write_bytes(original)
    proof = {
        "created_at": datetime.now(timezone.utc).isoformat(),
        "target": TARGET,
        "before_sha256": BEFORE,
        "after_sha256": sha(text.encode()),
        "inputs": inputs,
        "applied": bool(args.apply_candidate),
        "scope": "000088 only; 15 administered stocks with verified sequence-record taxa/current assemblies; complete host microbiome, biological species and exact original analysis versions remain unresolved",
    }
    if args.apply_candidate:
        # Native validation can take time; preserve the reviewed source state
        # through the last moment before canonical replacement (#2814).
        for relative, expected in inputs.items():
            if sha((ROOT / relative).read_bytes()) != expected:
                raise ValueError(f"reviewed input changed during validation: {relative}")
        if canonical.read_bytes() != original:
            raise ValueError("concurrent canonical change")
        replacement = output / "replacement.yaml"
        replacement.write_text(text)
        replacement.replace(canonical)
        if canonical.read_bytes() != text.encode():
            raise ValueError("persisted canonical candidate differs")
    (output / "receipt.json").write_text(json.dumps(proof, indent=2) + "\n")
    print(json.dumps(proof, indent=2))


if __name__ == "__main__":
    main()
