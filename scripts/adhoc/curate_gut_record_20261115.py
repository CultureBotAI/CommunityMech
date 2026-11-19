"""Stage/apply the reviewed 000122 corrections for #1548, 2026-11-15.

Inputs: pinned baseline record, primary XML and grounding/source receipts.
Outputs: exclusive .temp candidate/proof; explicit --apply-staged writes only the
named record after native closed-schema validation and exact concurrency checks.
Old history and the model-bounded three-node/one-edge graph are preserved.
"""

import argparse
import copy
import difflib
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
sys.path.insert(0, str(ROOT / "scripts"))
import gtdb_ground as native  # noqa: E402

from communitymech.curate.curation_event import record_curation_event  # noqa: E402
from communitymech.validation.write_validated import write_validated_community  # noqa: E402

STATE = ROOT / ".temp/phase2-gut-20261115"
TARGET = "kb/communities/LBNL_Human_Gut_Interaction_SynCom.yaml"
BEFORE = "aa02533254dbc2a5f78544e1d3155b49f65ba8cffaa2f88b99d625ebf91cd816"
PRIMARY = "9148ad1c34d3e0527d86bbd7d70c83792306c502deadde5c353c525ece318e08"
SUMMARY = "Grounded the twelve Methods stocks, retaining source names and the DSM17677 reclassification to Faecalibacterium duncaniae; replaced the aggregate Bacteria/CROSS_FEEDER placeholder. Distinguished laboratory and modeled gut environments, serial transfers and the shaken OD assay, and removed the unsupported acetate mediator assertion. Added full-community and single-dropout intended arm membership with the reported late BU contamination qualification; retained the model-bounded graph. CA GTDB remains unresolved and PC ambiguous; no stock-specific genome or molecular mediator inferred. Addresses the 000122 portion of #1548 only."


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def norm(text):
    return " ".join(unicodedata.normalize("NFKC", text).split())


class Loader(yaml.SafeLoader):
    def construct_mapping(self, node, deep=False):
        keys = [self.construct_object(key, deep=deep) for key, _ in node.value]
        if len(keys) != len(set(keys)):
            raise ValueError("duplicate YAML key")
        return super().construct_mapping(node, deep=deep)


def load(raw):
    return yaml.load(raw, Loader=Loader)  # noqa: S506 -- SafeLoader subclass


def evidence(quote, explanation, source="IN_VITRO"):
    return {
        "reference": "PMID:29930200",
        "supports": "SUPPORT",
        "evidence_source": source,
        "snippet": quote,
        "explanation": explanation,
    }


def replace(text, key, value):
    replacement = (
        ""
        if value is None
        else yaml.safe_dump({key: value}, sort_keys=False, allow_unicode=True, width=108)
    )
    result, count = re.subn(
        rf"(?ms)^{re.escape(key)}:.*?(?=^[A-Za-z_][A-Za-z_0-9]*:|\Z)", lambda _: replacement, text
    )
    if count != 1:
        raise ValueError("expected one original section: " + key)
    return result


def all_evidence(value):
    if isinstance(value, dict):
        if "snippet" in value and "reference" in value:
            yield value
        for child in value.values():
            yield from all_evidence(child)
    elif isinstance(value, list):
        for child in value:
            yield from all_evidence(child)


def build(before, grounding, environment):
    after = copy.deepcopy(before)
    after["description"] = (
        "A defined twelve-stock anaerobic human-gut model studied in laboratory serial-transfer cultures. Monospecies, pairwise and full/single-dropout assemblages support fitted effective ecological interactions and model-bounded coexistence analyses; metabolomics suggests candidate mechanisms rather than demonstrating specific interspecies metabolite transfer."
    )
    after["environment_term"] = {
        "preferred_term": "laboratory culture environment",
        "term": grounding["environment"]["term"],
        "notes": "Physical setting: anaerobic laboratory broth cultures. This is not a sampled intestine or an in vivo host experiment.",
    }
    after["modeled_environment"] = [
        {
            "preferred_term": "human gut",
            "term": next(
                item["term"]
                for item in environment["terms"]
                if item["term"]["id"] == "ENVO:2100002"
            ),
            "notes": "The source describes a synthetic human gut microbiome community; the modeled habitat is distinct from the laboratory culture environment.",
        }
    ]
    design = after["engineering_design"]
    design["objective"] = (
        "Infer effective ecological interaction structure and test model predictions in a defined twelve-stock human gut model."
    )
    design["assembly_strategy"] = (
        "The twelve Methods stocks were combined as monospecies, pairwise, full-community and single-species dropout assemblages. Full and dropout arms below describe intended inoculated membership, not an assertion of constant realized composition."
    )
    design["perturbation_design"] = (
        "PW1 used approximately equal initial OD600 contributions; PW2 used reciprocal 95:5 proportions, with Methods specifying major/minor inocula of 0.0158/0.0008 OD600. Full and all twelve single-stock dropout assemblages were monitored with serial 1:20 transfers every 24 h over 72 h."
    )
    design["evidence"].extend(
        [
            evidence(
                "For PW2, the major and minor strains were inoculated at 0.0158 and 0.0008 OD600, respectively.",
                "PW2 inoculation rule, separate from PW1 and full/dropout designs.",
            ),
            evidence(
                "time‐resolved measurements of relative abundance of the full (12‐member) and all single‐species dropout communities",
                "Defines the full and all single-dropout arm set; Figure3 and DatasetEV3 distinguish their membership.",
            ),
        ]
    )
    taxonomy = []
    for row in grounding["rows"]:
        abbreviation = row["member_id"]
        stock = row["collection"] + " " + row["accession"]
        short_name = row["source_name"].split()[0][0] + ". " + row["source_name"].split()[1]
        notes = f"Paper abbreviation {abbreviation}; source name {row['source_name']}; exact Methods stock {stock}. Current NCBI label is independently checked against the retained local ontology. GTDB mapping is species-level and does not identify this individual stock's genome."
        if abbreviation == "FP":
            notes += " DSMZ DSM17677 (A2-165) catalogue explicitly records reassignment from F. prausnitzii to F. duncaniae in May2022: https://www.dsmz.de/collection/catalogue/details/culture/DSM-17677 (inspected 2026-11-15). The historical FP abbreviation is retained."
        elif row["term"]["label"] != row["source_name"]:
            notes += " The source spelling is retained; the NCBI synonym assertion supports the current canonical species label."
        descriptor = {"preferred_term": row["term"]["label"], "term": row["term"], "notes": notes}
        gtdb = row["native_grounding"]
        if not gtdb:
            descriptor["gtdb_grounding_status"] = "UNRESOLVED"
            descriptor[
                "notes"
            ] += " The retained crosswalk produced no species grounding; no nearby taxon was substituted."
        elif gtdb.get("ambiguous"):
            descriptor["gtdb_grounding_status"] = "AMBIGUOUS"
            descriptor["gtdb_candidates"] = gtdb["gtdb_options"]
            descriptor[
                "notes"
            ] += " The crosswalk splits this species; no stock-specific genome assignment was made."
        else:
            descriptor["gtdb_grounding_status"] = "GROUNDED"
            descriptor["gtdb_classification"] = native._block(
                gtdb,
                "kg-microbe NCBI2GTDB.tsv.gz sha256:"
                + grounding["input_hashes"]["NCBI2GTDB.tsv.gz"]
                + "; release/build date not established",
            )
        taxonomy.append(
            {
                "member_id": abbreviation.lower(),
                "taxon_term": descriptor,
                "strain_designation": {
                    "strain_name": stock,
                    "culture_collections": [
                        {"collection": row["collection"], "accession": row["accession"]}
                    ],
                    "notes": f"{abbreviation} in the source; starter culture incubated {row['starter_incubation_hours']} h before community inoculation. This is starter timing, not community incubation time.",
                },
                "evidence": [
                    evidence(
                        f"{short_name} ({abbreviation}, {stock})",
                        "Methods: exact stock in the defined twelve-member roster. Current species naming and crosswalk interpretation are separately documented in taxon notes and the saved review.",
                    )
                ],
            }
        )
    after["taxonomy"] = taxonomy
    participants = [
        {"preferred_term": row["taxon_term"]["preferred_term"], "term": row["taxon_term"]["term"]}
        for row in taxonomy
    ]
    for item in after["ecological_interactions"]:
        item["participating_taxa"] = copy.deepcopy(participants)
    # #2815: the CH--ER feedback exemplar is not a twelve-organism feedback.
    feedback = after["ecological_interactions"][2]
    if feedback["name"] != "Modeled Pairwise Coexistence Feedback":
        raise ValueError("reviewed graph node changed")
    feedback.pop("participating_taxa")
    feedback["scope"] = "PAIRWISE"
    descriptors = {
        row["member_id"]: {
            "preferred_term": row["taxon_term"]["preferred_term"],
            "term": row["taxon_term"]["term"],
        }
        for row in taxonomy
    }
    feedback["source_taxon"] = descriptors["ch"]
    feedback["target_taxon"] = descriptors["er"]
    feedback["description"] = (
        "The fitted CH-ER pairwise gLV model contains a positive CH-to-ER coefficient and a negative ER-to-CH coefficient, forming the source's model-bounded negative-feedback coexistence motif (Figure4B/C). Source/target name the positive limb; the reverse inhibitory limb is part of the coupled motif. CH is Peptacetobacter hiranonis DSM13275 (paper Clostridium hiranonis); ER is Agathobacter rectalis ATCC33656 (paper Eubacterium rectale). The model comparison supports coexistence across broader tested growth-rate regimes than mutual inhibition, not a demonstrated molecular mediator or a feedback involving all twelve members."
    )
    feedback["evidence"].append(
        evidence(
            "The inferred pairwise network for the CH, ER community exhibited coupled positive and negative interactions",
            "Figure4B/C and retained CodeEV1 T3 specify the CH-ER motif. This is computational pairwise attribution, not twelve-member or molecular-transfer evidence.",
            source="COMPUTATIONAL",
        )
    )
    after["ecological_interactions"][1]["downstream"][0][
        "description"
    ] = "PARTIAL - the fitted CH-ER pair model uses coupled positive and negative effects to implement negative feedback and support coexistence across a broader tested growth-rate regime than mutual inhibition. This links the inferred topology to its specific pairwise model exemplar; it does not assert a twelve-member molecular feedback."
    after.pop("environmental_factors")
    after.pop("related_ingredients")
    medium = after["growth_media"][0]
    medium["evidence"][0][
        "explanation"
    ] = "Methods explicitly describes the 15mL starter culture, not the deep-well community working volume."
    medium["evidence"].append(
        evidence(
            "Serial transfers were performed at 24‐h intervals into fresh media using a 1:20 dilution.",
            "Repeated fresh-medium transfers distinguish the 72h experiment from one closed batch.",
        )
    )
    medium["evidence"].append(
        evidence(
            "The microbial communities were arrayed using a liquid‐handling robot (Biomek) into 96‐well deep‐well plates covered with a gas‐permeable seal (Breathe Easy) and incubated at 37°C without shaking",
            "Community culture vessel and incubation condition; the shaken absorbance assay is separate.",
        )
    )
    setup = after["cultivation_setup"][0]
    setup["cultivation_mode"] = "OTHER"
    setup["notes"] = (
        "Serial-transfer cultivation: fresh-medium transfers every 24 h at 1:20 over 72 h. OTHER is used because the controlled vocabulary has no exact serial-transfer mode; the paper does not specify same-vessel draw-and-fill. Total initial density scales with community size (0.01 OD600 per strain), with distinct PW2 major/minor inocula. Deep-well cultures were static; parallel 384-well aliquots were shaken for OD600 readings. Separate monospecies metabolomics cultures supplemented only ER and FP with 33 mM acetate; this is not evidence of acetate cross-feeding in the community."
    )
    setup["evidence"].extend(
        [
            evidence(
                "Serial transfers were performed at 24‐h intervals into fresh media using a 1:20 dilution.",
                "Exact repeated-transfer protocol; no continuous dilution rate or culture residence time inferred.",
            ),
            evidence(
                "In parallel, aliquots of the communities were transferred into a 384‐well absorbance plate and grown in a Tecan Infinite F200 Pro plate reader with shaking for OD600 measurements at 30‐min intervals.",
                "Shaking applies to the parallel optical measurement, not the static deep-well community culture.",
            ),
            evidence(
                "ER and FP were grown in ABB media supplemented with 33 mM acetate (Sigma).",
                "Bacterial culturing for metabolomics subsection only; no traced interspecies acetate transfer is shown.",
            ),
        ]
    )
    arm_quote = "time‐resolved measurements of relative abundance of the full (12‐member) and all single‐species dropout communities"
    ids = [row["member_id"] for row in taxonomy]
    arms = [
        {
            "id": "full",
            "name": "Full 12-member community (NONE in Dataset EV3)",
            "context": "full-and-single-dropout community time series",
            "membership_status": "DEFINED_MEMBERS",
            "participant_member_ids": ids,
            "description": "Intended full inoculum; species abundances vary across the 72h serial-transfer time series. No measured abundance values are pooled across sampling times.",
            "evidence": [
                evidence(
                    arm_quote,
                    "Results Model validation and DatasetEV3 identify the full community.",
                )
            ],
        }
    ]
    for row in grounding["rows"]:
        abbr = row["member_id"]
        description = f"Intended inoculum excludes {abbr} ({row['collection']} {row['accession']}); every other Methods stock is included. This arm definition is not proof that an omitted organism remained absent at every time point."
        evs = [
            evidence(
                arm_quote,
                f"All single-species dropout communities includes the {abbr}- arm, also explicitly labeled in DatasetEV3.",
            )
        ]
        if abbr == "BU":
            description += " BU contamination was detected at47.5h (0.4%) and persisted to72h (2%); the final three sampling points are not complete BU absence."
            evs.append(
                evidence(
                    "BU contamination was detected in the BU‐ consortium at 47.5 h (0.4% of the community) and BU persisted in the community until 72 h (2% of the community).",
                    "Explicit exception to intended dropout membership.",
                )
            )
        arms.append(
            {
                "id": "dropout_" + abbr.lower(),
                "name": abbr + "-",
                "context": "full-and-single-dropout community time series",
                "membership_status": "DEFINED_MEMBERS",
                "participant_member_ids": [item for item in ids if item != abbr.lower()],
                "comparator_arm_ids": ["full"],
                "description": description,
                "evidence": evs,
            }
        )
    after["treatment_arms"] = arms
    after["discussions"].append(
        {
            "discussion_id": "gut_roster_protocol_reassessment_20261115",
            "prompt": "Which stock-resolved molecular transfers explain the model-inferred signed interactions?",
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "attaches_to": ["taxonomy", "cultivation_setup", "ecological_interactions"],
            "rationale": "The November2026 reassessment replaces the old aggregate roster and unsupported acetate-mediator assertion. Main Methods, Appendix, EV1-EV4 and stock grounding were inspected. Monospecies metabolite depletion/secretion and conditioned-medium responses nominate mechanisms but do not demonstrate direct transfer between named stocks. Acetate addition is confined to the ER/FP metabolomics protocol; it does not establish a community-wide mediator. CA GTDB is unresolved and PC has two crosswalk candidates; no individual stock genome is assigned. The previous October discussion records its historical review scope and remains unchanged.",
            "evidence": [
                evidence(
                    "the metabolite profiles failed to predict the influential role of EL in mediating community assembly, fitness, and diversity",
                    "Explicit limit of the metabolomics-to-mechanism inference.",
                )
            ],
            "posed_by": "codex",
            "posed_date": "2026-11-15",
        }
    )
    return after


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--apply-staged", type=Path)
    parser.add_argument("--reviewed-candidate-sha256")
    parser.add_argument("--reviewed-receipt-sha256")
    args = parser.parse_args()
    output = args.output.resolve()
    if not output.is_relative_to(ROOT / ".temp") or output.exists():
        raise ValueError("exclusive private output required")
    original = (ROOT / TARGET).read_bytes()
    if digest(original) != BEFORE:
        raise ValueError("baseline changed")
    output.mkdir()
    if args.apply_staged:
        stage = args.apply_staged.resolve()
        if not stage.is_relative_to(STATE) or stage.is_symlink():
            raise ValueError("staged target must be beneath private state")
        receipt_raw = (stage / "receipt.json").read_bytes()
        candidate_raw = (stage / "candidate.yaml").read_bytes()
        # #2814: digests come from the independent review, never from this manifest.
        if (
            not args.reviewed_candidate_sha256
            or not args.reviewed_receipt_sha256
            or digest(candidate_raw) != args.reviewed_candidate_sha256
            or digest(receipt_raw) != args.reviewed_receipt_sha256
        ):
            raise ValueError("externally reviewed candidate/receipt digest differs")
        receipt = json.loads(receipt_raw)
        if receipt["target"] != TARGET:
            raise ValueError("staged target differs")
        if receipt["after_sha256"] != digest(candidate_raw) or receipt["before_sha256"] != BEFORE:
            raise ValueError("staged candidate differs")
        verify_inputs(receipt)
        after = load(candidate_raw)
        before = load(original)
        if after["id"] != "CommunityMech:000122" or before["id"] != after["id"]:
            raise ValueError("staged target identity differs")
        if after.get("curation_history", []) != before.get("curation_history", []) + [
            receipt["event"]
        ]:
            raise ValueError("reviewed append-only history differs")
    else:
        article_path = STATE / "primary-001/article.xml"
        if digest(article_path.read_bytes()) != PRIMARY:
            raise ValueError("primary source changed")
        grounding = json.loads((STATE / "grounding-roster-002.json").read_bytes())
        environment = json.loads((STATE / "environment-authority-001.json").read_bytes())
        if environment["sha256"] != grounding["input_hashes"]["envo.db"]:
            raise ValueError("environment authority does not match retained grounding")
        before = load(original)
        if before["id"] != "CommunityMech:000122" or len(grounding["rows"]) != 12:
            raise ValueError("unexpected target/roster")
        after = build(before, grounding, environment)
        source = norm("".join(ElementTree.fromstring(article_path.read_bytes()).itertext()))
        for item in all_evidence(after):
            if norm(item["snippet"]) not in source:
                raise ValueError("snippet absent from primary XML: " + item["snippet"])
        text = original.decode()
        for key in (
            "description",
            "engineering_design",
            "environment_term",
            "taxonomy",
            "ecological_interactions",
            "environmental_factors",
            "related_ingredients",
            "growth_media",
            "cultivation_setup",
            "discussions",
        ):
            text = replace(text, key, after.get(key))
        for key, anchor in (
            ("modeled_environment", "taxonomy:\n"),
            ("treatment_arms", "ecological_interactions:\n"),
        ):
            text = text.replace(
                anchor,
                yaml.safe_dump({key: after[key]}, sort_keys=False, allow_unicode=True, width=108)
                + anchor,
                1,
            )
        if load(text) != after or after["curation_history"] != before["curation_history"]:
            raise ValueError("bounded mutation or old history changed")
        event = record_curation_event(
            after, curator="codex", action="EDIT", changes=SUMMARY, llm_assisted=True
        )
        text = (
            text.rstrip()
            + "\n"
            + yaml.safe_dump([event], sort_keys=False, allow_unicode=True, width=108)
        )
        candidate_raw = text.encode()
        if load(candidate_raw) != after:
            raise ValueError("history append differs")
        source_inputs = [
            article_path,
            STATE / "grounding-roster-002.json",
            STATE / "environment-authority-001.json",
            STATE / "dsm17677-catalog-001/catalog.html",
            Path(__file__),
            ROOT / "src/communitymech/schema/communitymech.yaml",
            ROOT / "src/communitymech/schema/mech_shared.yaml",
            ROOT / "uv.lock",
            STATE / "primary-001/figure4.png",
        ]
        source_inputs.extend(
            path
            for path in STATE.glob("publisher-supplement-*/*")
            if path.suffix in {".pdf", ".xlsx", ".zip"}
        )
        receipt = {
            "target": TARGET,
            "before_sha256": BEFORE,
            "after_sha256": digest(candidate_raw),
            "inputs": {
                str(path.relative_to(ROOT)): digest(path.read_bytes()) for path in source_inputs
            },
            "event": event,
        }
    write_validated_community(after, output / "validated.yaml")
    if load((output / "validated.yaml").read_bytes()) != after:
        raise ValueError("native serialization differs")
    (output / "candidate.yaml").write_bytes(candidate_raw)
    (output / "before.yaml").write_bytes(original)
    (output / "diff.patch").write_text(
        "".join(
            difflib.unified_diff(
                original.decode().splitlines(True),
                candidate_raw.decode().splitlines(True),
                fromfile=TARGET,
                tofile=TARGET,
            )
        )
    )
    if args.apply_staged:
        # Validate first, then recheck the independently reviewed sources and
        # target immediately before canonical replacement. Never refresh hashes.
        verify_inputs(receipt)
        if (ROOT / TARGET).read_bytes() != original:
            raise ValueError("concurrent record change")
        (output / "replacement.yaml").write_bytes(candidate_raw)
        (output / "replacement.yaml").replace(ROOT / TARGET)
        if (ROOT / TARGET).read_bytes() != candidate_raw:
            raise ValueError("persisted bytes differ")
        receipt["reviewed_candidate_sha256"] = args.reviewed_candidate_sha256
        receipt["reviewed_receipt_sha256"] = args.reviewed_receipt_sha256
    receipt.update(
        created_at=datetime.now(timezone.utc).isoformat(), applied=bool(args.apply_staged)
    )
    (output / "receipt.json").write_text(json.dumps(receipt, indent=2) + "\n")
    print(json.dumps(receipt, indent=2))


def verify_inputs(receipt):
    if not receipt["inputs"]:
        raise ValueError("reviewed input manifest is empty")
    for name, expected in receipt["inputs"].items():
        path = ROOT / name
        if Path(name).is_absolute() or not path.resolve().is_relative_to(ROOT) or path.is_symlink():
            raise ValueError("reviewed input path is invalid")
        if digest(path.read_bytes()) != expected:
            raise ValueError("reviewed input changed: " + name)


if __name__ == "__main__":
    main()
