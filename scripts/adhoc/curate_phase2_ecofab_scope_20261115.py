"""Stage source-scoped EcoFAB #1427/#2675 corrections, 2026-11-15.

Inputs: exact current000025, original PLOS main XML and separate S2 workbook.
Outputs: exclusive private native-validated plan, exact diff and evidence map.
Apply requires the same helper/source/original bytes and reconstructed candidate;
one atomic target write appends native inline history. Native sidecar is separate.
No source/cache, neighboring record, previous history or old-review mutation.
"""

import argparse
import copy
import difflib
import hashlib
import json
import re
import sys
import zipfile
from datetime import datetime, timezone
from pathlib import Path

import yaml
from curate_phase2_lbnl_canary_20261115 import load_document, replace_section
from curate_phase2_linked_stocks_20261115 import semantic_changes
from defusedxml import ElementTree

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))
from communitymech.curate.curation_event import (  # noqa: E402
    append_curation_event_text,
    record_curation_event,
)
from communitymech.validation.write_validated import write_validated_community  # noqa: E402

STATE = ROOT / ".temp/phase2-science-20261115"
TARGET = "kb/communities/EcoFAB_Ring_Trial_SynCom17.yaml"
BEFORE = "0adba2db63b8277d16d0a0e71db00a36009daf5e8ac6231b9081128421bd818c"
PEERS = {
    "kb/communities/LBNL_Switchgrass_Soil_SynCom16.yaml": "bb31b1df4a9be2241453528101fc5d55657c23eccf1d58ce1cc9639e5912b368",
    "kb/communities/Brachypodium_Natural_Variation_Dopamine_SynCom16.yaml": "304702c684faedb244d678e628ec174851dbdcafe46128eab86d824798e0482a",
}
SOURCES = {
    "linked-retained/ecofab-independent/ring-main-plos.xml": "8ab7d3de83f7b92e7dc6443db61d9ed31471d7ccdbdd1c8cf6c3d3b2efc6e947",
    "linked-retained/ecofab-independent/ring-s2.xlsx": "fd7882e673f62498ce2ac8c1215ece003edb7369fa780c106bfaa6db4b80e147",
}
SUMMARY = "Separated measured ring-trial outcomes from unproved OAS925-specific uptake, plant harm, competitive exclusion and member roles; retained all five graph nodes and four qualified arrows. Distinguished ring inoculum/host culture from reporter and isolate assays, removed unrelated nitrogen-study factor attribution, added four source-defined treatment arms and four arm/timepoint-specific relative 16S observations without converting reads to cells. Removed unverified OAP107 21 DPI abundance prose while preserving stock/grounding. Replaced the genome pseudo-range with 17 exact source stock-to-IMG/GOLD identifiers including Mycobacterium Gp0440934. Addresses #1427/#2675; source-only supplement/metadata limits remain explicit, all prior history and linked taxon mapping cores preserved."
CONTEXT = "Five-laboratory EcoFAB 2.0 Bd21-3 ring trial"
ARM_QUOTE = "Mock-inoculated axenic plant control, ii) SynCom16-inoculated plants, iii) SynCom17-inoculated plants, and iv) Mock-inoculated technical control (plant-free)"
COMPOSITION_QUOTE = "the root microbiome inoculated with SynCom17 was dominated by Paraburkholderia sp. OAS925 across all laboratories"


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def norm(text):
    return " ".join(text.split())


def ev(snippet, explanation, tier="IN_VIVO"):
    return {
        "reference": "PMID:40920748",
        "supports": "SUPPORT",
        "evidence_source": tier,
        "snippet": snippet,
        "explanation": explanation,
    }


def verify_sources():
    for name, expected in SOURCES.items():
        if digest((STATE / name).read_bytes()) != expected:
            raise ValueError("reviewed primary source changed: " + name)
    for name, expected in PEERS.items():
        if digest((ROOT / name).read_bytes()) != expected:
            raise ValueError("related scientific input changed: " + name)


def read_sources():
    xml = STATE / "linked-retained/ecofab-independent/ring-main-plos.xml"
    tree = ElementTree.fromstring(xml.read_bytes())
    article_body = tree.find("body")
    if article_body is None:
        raise ValueError("expected original article body")
    main_text = norm("".join(article_body.itertext()))
    workbook = STATE / "linked-retained/ecofab-independent/ring-s2.xlsx"
    ns = {"m": "http://schemas.openxmlformats.org/spreadsheetml/2006/main"}
    with zipfile.ZipFile(workbook) as archive:
        strings = [
            norm("".join(row.itertext()))
            for row in ElementTree.fromstring(archive.read("xl/sharedStrings.xml"))
        ]
        sheet = ElementTree.fromstring(archive.read("xl/worksheets/sheet1.xml"))
        rows = {}
        for row in sheet.findall(".//m:row", ns):
            number = int(row.get("r"))
            if not 2 <= number <= 18:
                continue
            cells = {}
            for cell in row.findall("m:c", ns):
                value = cell.find("m:v", ns)
                if value is None:
                    continue
                value = value.text
                if cell.get("t") == "s":
                    value = strings[int(value)]
                cells[re.sub(r"\d+$", "", cell.get("r"))] = value
            name = cells["A"]
            stock = name.split()[-1]
            if stock in rows:
                raise ValueError("duplicate source stock")
            quote = f"{name} ({cells['C']}, {cells['D']}"
            if norm(quote) not in main_text:
                raise ValueError("S2 stock/IMG/GOLD pair differs from mainMethods4.8: " + stock)
            if not re.fullmatch(r"\d{10}", cells["C"]) or not re.fullmatch(r"Gp\d{7}", cells["D"]):
                raise ValueError("unexpected source accession")
            if (
                cells["B"]
                != "https://img.jgi.doe.gov/cgi-bin/m/main.cgi?section=TaxonDetail&page=taxonDetail&taxon_oid="
                + cells["C"]
            ):
                raise ValueError("source IMG link does not match source ID")
            rows[stock] = {
                "row": number,
                "source_name": name,
                "img": cells["C"],
                "gold": cells["D"],
                "img_url": cells["B"],
                "reported_genbank": cells["E"],
                "ncbi_link_as_reported": cells["F"],
                "stock_medium": cells["J"],
                "syncom17": cells["K"],
                "syncom16": cells["L"],
                "main_quote": quote,
            }
    if len(rows) != 17 or any(row["syncom17"] != "1" for row in rows.values()):
        raise ValueError("source17 roster differs")
    if [stock for stock, row in rows.items() if row["syncom16"] == "0"] != ["OAS925"]:
        raise ValueError("source16 omission differs")
    return main_text, rows


def build(original, main_text, source_rows, timestamp=None):
    before = load_document(original)
    if before["id"] != "CommunityMech:000025" or len(before["ecological_interactions"]) != 5:
        raise ValueError("unexpected target identity or graph")
    after = copy.deepcopy(before)
    stocks = [item["strain_designation"]["strain_name"] for item in after["taxonomy"]]
    if len(stocks) != 17 or set(stocks) != set(source_rows):
        raise ValueError("source/canonical stock mismatch")
    after["description"] = (
        "A 17-member synthetic bacterial inoculum used in a five-laboratory EcoFAB 2.0 ring trial with Brachypodium distachyon Bd21-3. SynCom17, SynCom16 lacking OAS925, axenic plants and plant-free medium were compared under standardized protocols. At 22 days after inoculation, OAS925 accounted for 98 ± 0.03% of root bacterial 16S reads in SynCom17; the omission treatment had more variable relative profiles. Whole-treatment differences in plant biomass and bulk spent-medium metabolites do not identify OAS925-specific uptake, toxicity, competitive exclusion or absolute loss of other stocks. Separate genomic, isolate-culture and reporter-plant assays identify candidate colonization traits, not selectively demonstrated mechanisms in SynCom17. The 17 stocks originate from the source switchgrass isolate collection; physical cultivation here is a laboratory hydroponic model, not native soil."
    )
    design = after["engineering_design"]
    design["assembly_strategy"] = (
        "Seventeen source stocks were grown separately, washed with half-strength MS and combined using OD600-to-CFU conversions into equal-cell concentrated stocks in 20% glycerol. The inoculation calculation assumed 50% freeze-thaw survival and a theoretical 1e5 CFU per plant; neither equal realized abundance nor actual post-thaw survival is inferred."
    )
    design["measurement_endpoints"] = [
        "Relative 16S read composition of root and unfiltered medium samples",
        "Net extracellular LC-MS metabolite profiles in filtered spent medium",
        "Whole-treatment plant fresh/dry biomass and root-development readouts",
        "Separate isolate-culture traits and computational genome annotations",
    ]
    design["perturbation_design"] = (
        "Four ring-trial arms: SynCom17, SynCom16 omitting OAS925, mock-inoculated axenic plant control, and mock-inoculated plant-free medium control. The nitrogen-form/starvation study is a separate sterile-plant experiment, not this trial's factorial intervention."
    )
    design["notes"] = (
        "Ring-trial Methods 4.1–4.2 and S2 Table define inoculum/arm identity. Physical device culture, isolate stock preparation, separate RFP-isolate microscopy and computational genomic analysis remain distinct. Ring-trial Methods"
        + before["engineering_design"]["notes"].split("Ring-trial Methods", 1)[1]
    )
    design["evidence"][0] = ev(
        ARM_QUOTE,
        "Methods 4.2 names the four actual ring-trial arms; no competitive-exclusion mechanism or nitrogen/light factorial is implied.",
    )
    after["environment_term"][
        "notes"
    ] = "Sterile EcoFAB 2.0 laboratory hydroponic devices containing 9 mL half-strength MS plus 1 mL inoculum or mock at inoculation. Methods 4.2 specifies 14 h light at 26 °C and 10 h dark at 20 °C (16 h light for laboratory C), 110–140 µmol/m2/s PPFD and 70% humidity if tunable. Chamber deviations are reported separately in S1 Table; these conditions are not uniform measured exposures or the reporter-isolate protocol."
    observations = {
        "OAS925": (98.0, 0.03, "syncom17", COMPOSITION_QUOTE),
        "OAS809": (68.0, 33.0, "syncom16-minus-oas925", "Rhodococcus sp. OAS809 (68 ± 33%)"),
        "OAE908": (14.0, 27.0, "syncom16-minus-oas925", "Mycobacterium sp. OAE908 (14 ± 27%)"),
        "OAE515": (15.0, 20.0, "syncom16-minus-oas925", "Methylobacterium sp. OAE515 (15 ± 20%)"),
    }
    for index, item in enumerate(after["taxonomy"]):
        stock = item["strain_designation"]["strain_name"]
        item["member_id"] = stock.lower()
        item.pop("functional_role", None)
        item.pop("abundance_level", None)
        item.pop("abundance_value", None)
        if stock in observations:
            mean, sd, arm, quote = observations[stock]
            item["abundance_observations"] = [
                {
                    "treatment_arm_id": arm,
                    "timepoint_id": "harvest-22dai",
                    "replicate": "Across five laboratories; reported mean ± SD",
                    "measurement_basis": "Relative bacterial 16S rRNA amplicon read abundance in root samples",
                    "relative_abundance": mean,
                    "relative_abundance_unit": "PERCENT",
                    "description": f"Source Results 2.4 reports mean {mean:g}% ± {sd:g} percentage points SD at 22 DAI in the named arm. Relative reads are not absolute cell numbers, viable counts, growth rates or competitive extinction.",
                    "evidence": [
                        ev(
                            quote,
                            "Results 2.4 reports this arm-specific root relative-read composition at 22 DAI.",
                        )
                    ],
                }
            ]
            item["taxon_term"]["notes"] = (
                "In SynCom17, OAS925 averaged 98 ± 0.03% of root 16S reads at 22 DAI. Separate genomic annotations and isolate assays motivate traits, but do not establish a selective mechanism or OAS925-only plant harm. Formerly classified as Burkholderia sp. OAS925."
                if stock == "OAS925"
                else f"In the OAS925-omission SynCom16 arm, {stock} averaged {mean:g} ± {sd:g}% of root 16S reads at 22 DAI; no unscoped default abundance or functional role is inferred."
            )
        elif stock == "OAP107":
            old = item["taxon_term"]["notes"]
            prefix = "Low relative abundance (<0.2%) at 21 DPI. "
            if not old.startswith(prefix):
                raise ValueError("expected unverified OAP107 abundance selector changed")
            item["taxon_term"]["notes"] = old[len(prefix) :]
        for evidence in item.get("evidence", []):
            if evidence["snippet"].startswith(
                "All participating laboratories observed"
            ) or evidence["snippet"].startswith("Paraburkholderia sp. OAS925 could"):
                evidence["evidence_source"] = "IN_VIVO"
        if item["taxon_term"].get("gtdb_classification") != before["taxonomy"][index][
            "taxon_term"
        ].get("gtdb_classification"):
            raise ValueError("numeric taxonomic classification changed")
    arms = []
    for key, name, members, comparators in (
        (
            "syncom17",
            "SynCom17-inoculated plants",
            stocks,
            ["syncom16-minus-oas925", "axenic-mock", "plant-free-mock"],
        ),
        (
            "syncom16-minus-oas925",
            "SynCom16-inoculated plants (OAS925 omitted)",
            [x for x in stocks if x != "OAS925"],
            ["syncom17", "axenic-mock", "plant-free-mock"],
        ),
        (
            "axenic-mock",
            "Mock-inoculated axenic plant control",
            [],
            ["syncom17", "syncom16-minus-oas925", "plant-free-mock"],
        ),
        (
            "plant-free-mock",
            "Mock-inoculated technical control (plant-free)",
            [],
            ["syncom17", "syncom16-minus-oas925", "axenic-mock"],
        ),
    ):
        arm = {
            "id": key,
            "name": name,
            "context": CONTEXT,
            "membership_status": "DEFINED_MEMBERS" if members else "NO_MICROBES",
            "comparator_arm_ids": comparators,
            "conditions": [
                {
                    "name": "Host presence",
                    "value": "B. distachyon Bd21-3" if key != "plant-free-mock" else "No plant",
                    "description": "Source-defined host condition, not microbial taxonomy membership.",
                }
            ],
            "timepoints": [
                {
                    "id": "harvest-22dai",
                    "name": "22 days after inoculation",
                    "reference_event": "Inoculation with SynCom or mock",
                    "description": "Final plant harvest/sampling and medium sterility check; plant-free arm has no plant harvest.",
                }
            ],
            "description": "Source-defined intended sterile/microbial status; occasional contamination diagnostics do not redefine the intended arm. Laboratory variation is preserved separately. Inoculum stocks are not equated with realized final composition.",
            "evidence": [
                ev(
                    ARM_QUOTE,
                    "Methods 4.2 four arms; S2 Table columns K/L independently confirm 17 stocks and omission of OAS925 only.",
                ),
                ev(
                    "Plant harvest and sampling happened at 22 DAI.",
                    "Methods 4.2 final sampling anchor.",
                ),
            ],
        }
        if members:
            arm["participant_member_ids"] = [x.lower() for x in members]
        arms.append(arm)
    after["treatment_arms"] = arms
    for index, node in enumerate(after["ecological_interactions"]):
        if index != 1:
            node["treatment_arm_ids"] = ["syncom17"]
            for evidence in node["evidence"]:
                evidence["evidence_source"] = "IN_VIVO"
        else:
            node["evidence"][1]["evidence_source"] = "IN_VIVO"
    after["environmental_factors"] = [
        {
            "name": "Ring-trial host growth medium",
            "value": "Half-strength Murashige-Skoog basal salts",
            "description": "Common hydroponic medium, not a nitrogen-form intervention. 9 mL before addition of 1 mL inoculum/mock.",
            "evidence": [
                ev(
                    "9 mL of ½ MS basal salts (pH 5.5–6.0)",
                    "Methods 4.2 device medium before inoculation.",
                )
            ],
        },
        {
            "name": "Ring-trial photoperiod and temperature",
            "value": "14 h light 26 °C /10 h dark 20 °C; laboratory C 16 h light",
            "description": "Reported prescribed protocol, retaining the laboratory C exception without inferring its unstated dark duration. S1 Table and logger measurements report deviations.",
            "evidence": [
                ev(
                    "a 14 h photoperiod (16 h for lab C) at 26 °C and 10 h dark at 20 °C",
                    "Methods 4.2 laboratory protocol.",
                )
            ],
        },
        {
            "name": "Ring-trial illumination and humidity",
            "value": "110–140 µmol/m2/s PPFD; 70% humidity if tunable",
            "description": "Protocol targets, not a claim all chambers achieved identical measured values.",
            "evidence": [
                ev(
                    "110–140 µmol/m2/s and 70% humidity if tunable",
                    "Methods 4.2 target conditions; S1 Table reports chamber variation.",
                )
            ],
        },
    ]
    plant_ev = ev(
        "Plant harvest and sampling happened at 22 DAI.",
        "Ring-trial final harvest, distinct from the reporter microscopy 1/3 DAI.",
    )
    after["growth_media"] = [
        {
            "name": "Half-strength MS basal salts: ring-trial hydroponic host culture",
            "vessel_type": "EcoFAB 2.0 device",
            "light_regime": "14 h light (16 h for lab C); 10 h dark as source protocol, lab C dark duration not separately stated",
            "light_intensity": "110-140",
            "light_intensity_unit": "µmol/m²/s",
            "protocol_url": before["growth_media"][0]["protocol_url"],
            "preparation_notes": "Surface-sterilized Bd21-3 seed was stratified 3 days at 4 °C, germinated 3 days and transferred into devices with 9 mL half MS; 4 days later 1 mL inoculum/mock was added. Results calls these 10-day seedlings. Ring harvest 22 DAI; growth chamber 26 °C light/20 °C dark, 70% humidity if tunable. No bacterial shaking or reporter 3-day-plant condition applies to this host culture.",
            "evidence": [
                plant_ev,
                ev(
                    "The cells were resuspended and added to 10-day-old B. distachyon seedlings",
                    "Results 2.4 describes ring inoculation age.",
                ),
            ],
        },
        {
            "name": "Separate ring inoculum stock preparation: R2A, 0.1x R2A or LB by strain",
            "temperature": "27",
            "temperature_unit": "°C",
            "preparation_notes": "Methods 4.1: single colonies grown 2–8 days in preferred medium, washed with half MS, mixed using OD-to-CFU conversions and stored in 20% glycerol at −80 °C. S2 Table: OAE497/OAE829/OAE908/OAS944 use 0.1x R2A; OAE603 LB; other 12 R2A. This is separate from Methods 4.8 genomic-DNA cultivation and Methods 4.7 NLDM assays; no global 200 rpm speed is inferred.",
            "evidence": [
                ev(
                    "After 2–8 days at 27 °C",
                    "Methods 4.1 stock cultivation; separate S2 Table assigns strain-specific medium.",
                    "IN_VITRO",
                )
            ],
        },
        {
            "name": "Separate RFP-OAS925 reporter preculture and microscopy",
            "temperature": "27",
            "temperature_unit": "°C",
            "shaking_speed": "200",
            "shaking_speed_unit": "rpm",
            "preparation_notes": "Methods 4.9: reporter OAS925 overnight in 7 mL R2A with kanamycin 20 mg/L; washed into half MS and inoculated separately onto 3-day plants at OD600 0.01. Microscopy 1/3 DAI. These are not the ring inoculum or ring host timing.",
            "evidence": [
                ev(
                    "The Paraburkholderia sp. OAS925 expressing RFP was grown overnight in 7 mL of R2A medium with Kan 20 mg/L, shaken at 200 rpm at 27 °C.",
                    "Methods 4.9 reporter preculture.",
                    "IN_VITRO",
                )
            ],
        },
    ]
    after["related_ingredients"][0][
        "relevance"
    ] = "An amino-acid-rich metabolite cluster had lower net extracellular abundance under the whole SynCom17 treatment. The bulk spent-medium comparison does not identify OAS925-specific uptake, donor-recipient cross-feeding or plant versus microbial production/consumption."
    after["related_ingredients"][0]["evidence"][0][
        "explanation"
    ] = "Results 2.5 identifies an amino-acid-rich cluster with lower relative concentrations in SynCom17 spent medium; no individual taxon's flux is isolated."
    datasets = copy.deepcopy(before["associated_datasets"][:5])
    for stock in stocks:
        row = source_rows[stock]
        datasets.append(
            {
                "title": "Genome annotation: " + row["source_name"],
                "dataset_type": "GENOMICS",
                "repository": "JGI_IMG",
                "accession": row["img"],
                "url": row["img_url"],
                "organism": row["source_name"],
                "description": f"Source Methods 4.8 and S2 Table row {row['row']} associate stock {stock} with IMG/M taxon {row['img']} and GOLD project {row['gold']}. This is an exact source identifier pair, not a synthetic accession range or a claim that the study stock's GTDB placement was independently recomputed from this genome.",
                "publication": "PMID:40920748",
                "notes": f"Source GOLD Project ID: {row['gold']}. Current repository availability and genome sequence quality were not revalidated.",
                "evidence": [
                    ev(
                        row["main_quote"],
                        f"Main Methods 4.8 exact stock/IMG/GOLD pair; corroborated by separate S2 Table row {row['row']} columns A–D.",
                        "COMPUTATIONAL",
                    )
                ],
            }
        )
    after["associated_datasets"] = datasets
    # Verify only newly authored evidence against the actual main-body bytes;
    # separate S2 facts remain explicitly sourced to the retained workbook.
    old_snippets = {item["snippet"] for item in walk_evidence(before)}
    for item in walk_evidence(after):
        if (
            item["reference"] == "PMID:40920748"
            and item["snippet"] not in old_snippets
            and norm(item["snippet"]) not in main_text
        ):
            raise ValueError("new quotation absent from original main body: " + item["snippet"])
    if (
        before["related_communities"] != after["related_communities"]
        or before["host"] != after["host"]
    ):
        raise ValueError("unreviewed linked identity changed")
    for old, new in zip(
        before["ecological_interactions"], after["ecological_interactions"], strict=True
    ):
        if old.get("downstream") != new.get("downstream"):
            raise ValueError("previously reviewed causal arrow changed")
    text = original.decode()
    for key in (
        "description",
        "engineering_design",
        "environment_term",
        "taxonomy",
        "ecological_interactions",
        "environmental_factors",
        "associated_datasets",
        "related_ingredients",
        "growth_media",
    ):
        text = replace_section(text, key, after[key])
    block = yaml.safe_dump({"treatment_arms": arms}, sort_keys=False, allow_unicode=True, width=108)
    if "\ntreatment_arms:" in text or text.count("ecological_interactions:\n") != 1:
        raise ValueError("unexpected arm insertion anchor")
    text = text.replace("ecological_interactions:\n", block + "ecological_interactions:\n", 1)
    if load_document(text) != after:
        raise ValueError("bounded text candidate differs from scientific object")
    event = record_curation_event(
        after,
        curator="codex",
        action="EDIT",
        changes=SUMMARY,
        llm_assisted=True,
        **({"timestamp": timestamp} if timestamp else {}),
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
    old_event = yaml.safe_dump([unmarked], sort_keys=False, allow_unicode=True, width=108).rstrip()
    if text.count(old_event) != 1:
        raise ValueError("native append anchor differs")
    text = text.replace(
        old_event,
        yaml.safe_dump([event], sort_keys=False, allow_unicode=True, width=108).rstrip(),
        1,
    )
    if load_document(text) != after:
        raise ValueError("native inline event differs")
    return before, after, text, event


def walk_evidence(value):
    if isinstance(value, dict):
        if "snippet" in value and "reference" in value:
            yield value
        for child in value.values():
            yield from walk_evidence(child)
    elif isinstance(value, list):
        for child in value:
            yield from walk_evidence(child)


def plan(directory):
    if directory.exists() or not directory.is_relative_to(STATE):
        raise ValueError("new private plan directory required")
    verify_sources()
    original = (ROOT / TARGET).read_bytes()
    if digest(original) != BEFORE:
        raise ValueError("target changed since source assessment")
    main_text, rows = read_sources()
    before, after, text, event = build(original, main_text, rows)
    directory.mkdir()
    write_validated_community(after, directory / "native-validated.yaml")
    if load_document((directory / "native-validated.yaml").read_bytes()) != after:
        raise ValueError("native validated candidate differs")
    (directory / "before.yaml").write_bytes(original)
    (directory / "candidate.yaml").write_text(text)
    (directory / "diff.patch").write_text(
        "".join(
            difflib.unified_diff(
                original.decode().splitlines(True),
                text.splitlines(True),
                fromfile=TARGET,
                tofile=TARGET,
            )
        )
    )
    receipt = {
        "created_at": datetime.now(timezone.utc).isoformat(),
        "applied": False,
        "target": TARGET,
        "before_sha256": BEFORE,
        "after_sha256": digest(text.encode()),
        "source_inputs": SOURCES,
        "peer_inputs": PEERS,
        "helper_sha256": digest(Path(__file__).read_bytes()),
        "event": event,
        "source_genome_rows": rows,
        "semantic_changes": semantic_changes(before, after),
    }
    verify_sources()
    if (ROOT / TARGET).read_bytes() != original:
        raise ValueError("target changed during staging")
    (directory / "receipt.json").write_text(json.dumps(receipt, indent=2) + "\n")
    print(
        json.dumps(
            {
                "plan": str(directory.relative_to(ROOT)),
                "after_sha256": receipt["after_sha256"],
                "applied": False,
                "genome_rows": len(rows),
            }
        )
    )


def apply(directory):
    if not directory.is_relative_to(STATE):
        raise ValueError("private reviewed plan required")
    verify_sources()
    receipt = json.loads((directory / "receipt.json").read_text())
    original = (ROOT / TARGET).read_bytes()
    if (
        digest(original) != BEFORE
        or receipt["before_sha256"] != BEFORE
        or receipt["target"] != TARGET
        or receipt["applied"]
    ):
        raise ValueError("original target or reviewed plan changed")
    if (
        receipt["helper_sha256"] != digest(Path(__file__).read_bytes())
        or receipt["source_inputs"] != SOURCES
        or receipt["peer_inputs"] != PEERS
    ):
        raise ValueError("helper/source plan binding changed")
    main_text, rows = read_sources()
    _, after, text, event = build(
        original, main_text, rows, timestamp=receipt["event"]["timestamp"]
    )
    if (
        digest(text.encode()) != receipt["after_sha256"]
        or text.encode() != (directory / "candidate.yaml").read_bytes()
        or rows != receipt["source_genome_rows"]
        or event != receipt["event"]
    ):
        raise ValueError("candidate differs from bounded source reconstruction")
    audit = directory / "apply"
    audit.mkdir()
    write_validated_community(after, audit / "native-validated.yaml")
    if load_document((audit / "native-validated.yaml").read_bytes()) != after:
        raise ValueError("native revalidation changed candidate")
    verify_sources()
    if (ROOT / TARGET).read_bytes() != original:
        raise ValueError("canonical changed before replacement")
    (audit / "replacement.yaml").write_text(text)
    (audit / "replacement.yaml").replace(ROOT / TARGET)
    if (ROOT / TARGET).read_bytes() != text.encode():
        raise ValueError("persisted canonical bytes differ")
    result = {
        "applied_at": datetime.now(timezone.utc).isoformat(),
        "target": TARGET,
        "before_sha256": BEFORE,
        "after_sha256": digest(text.encode()),
        "plan_receipt_sha256": digest((directory / "receipt.json").read_bytes()),
        "history_sidecar_required": True,
    }
    (audit / "receipt.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--plan", type=Path, required=True)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    if args.apply:
        apply(args.plan.resolve())
    else:
        plan(args.plan.resolve())


if __name__ == "__main__":
    main()
