"""Keep Phase2 #1548 stock, assay and mechanism boundaries after curation.

These are current-record controls supplementing the historical batch61 ledger.
They preserve experimentally distinct scopes rather than prose layout. The gut
feedback signs are currently represented in prose, so that one assertion checks
normalized signed participant relations, not a whole sentence.
"""

import re
from copy import deepcopy
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]
BRACH = "LBNL_Brachypodium_Drought_SynCom15"
GUT = "LBNL_Human_Gut_Interaction_SynCom"
BRACH_TAXA = {
    "RCC-10": "NCBITaxon:3239227",
    "RCC-12": "NCBITaxon:3239226",
    "RCC-150": "NCBITaxon:3239231",
    "RCC-158": "NCBITaxon:3239220",
    "RCC-161.2": "NCBITaxon:3239219",
    "RCC-168": "NCBITaxon:3239221",
    "RCC-180": "NCBITaxon:3239224",
    "RCC-193": "NCBITaxon:3239218",
    "RCC-202": "NCBITaxon:3239222",
    "RCC-210": "NCBITaxon:3239217",
    "RCC-34": "NCBITaxon:3239230",
    "RCC-40": "NCBITaxon:3239225",
    "RCC-6.2": "NCBITaxon:3239223",
    "RCC-6.1": "NCBITaxon:3239229",
    "RCC-152.1": "NCBITaxon:3239228",
}
GUT_STOCKS = {
    "DSM 10507": "NCBITaxon:53443",
    "DSM 17677": "NCBITaxon:411483",
    "DSM 3979": "NCBITaxon:74426",
    "DSM 18205": "NCBITaxon:165179",
    "ATCC 33656": "NCBITaxon:39491",
    "ATCC 29098": "NCBITaxon:901",
    "DSM 6597": "NCBITaxon:820",
    "ATCC 8482": "NCBITaxon:821",
    "ATCC 29148": "NCBITaxon:818",
    "ATCC 8483": "NCBITaxon:28116",
    "DSM 13275": "NCBITaxon:89152",
    "DSM 2243": "NCBITaxon:84112",
}


def load_current(slug):
    return yaml.safe_load((ROOT / "kb" / "communities" / f"{slug}.yaml").read_text())


def stock_ids(record):
    rows = record["taxonomy"]
    result = {
        row["strain_designation"]["strain_name"]: row["taxon_term"]["term"]["id"] for row in rows
    }
    assert len(result) == len(rows), "duplicate stock row collapses the roster"
    return result


def check_brachypodium(record):
    assert record["id"] == "CommunityMech:000088"
    assert stock_ids(record) == BRACH_TAXA, "fifteen source stocks must not become aggregates"
    members = {row["member_id"] for row in record["taxonomy"]}
    assert len(members) == 15
    arms = {arm["id"]: arm for arm in record["treatment_arms"]}
    liquid = arms["liquid-ms"]
    assert liquid["membership_status"] == "DEFINED_MEMBERS"
    assert set(liquid["participant_member_ids"]) == members
    host_arms = [arm for key, arm in arms.items() if key.startswith("host-")]
    assert len(host_arms) == 8
    for arm in host_arms:
        assert arm["membership_status"] == "NOT_REPORTED", "Others prevents a complete host roster"
        assert not arm.get("participant_member_ids"), "inoculum is not the entire root microbiome"
    rcc150 = next(row for row in record["taxonomy"] if row["member_id"] == "rcc-150")
    assert rcc150["taxon_term"]["term"] == {
        "id": "NCBITaxon:3239231",
        "label": "bacterium RCC_150",
    }
    assert rcc150["taxon_term"]["gtdb_grounding_status"] == "UNRESOLVED"
    assert not rcc150["taxon_term"].get("gtdb_classification")
    assert rcc150["strain_designation"]["genome_accession"] == "GCA_041360635.1"
    nodes = record["ecological_interactions"]
    recovery = next(node for node in nodes if node.get("host_participation") == "HOST_IS_TARGET")
    assert recovery["scope"] == "COMMUNITY_LEVEL"
    assert set(recovery["treatment_arm_ids"]) == {
        "host-rewatered-syncom",
        "host-rewatered-buffer",
    }, "recovery is the rewatered contrast, not sustained drought or salinity"
    assert {item["evidence_source"] for item in recovery["evidence"]} == {"IN_VIVO"}
    assert not any(node.get("downstream") for node in nodes), "no demonstrated mediator chain"


def check_gut(record):
    assert record["id"] == "CommunityMech:000122"
    assert stock_ids(record) == GUT_STOCKS, "twelve Methods stocks must not become aggregates"
    members = {row["member_id"] for row in record["taxonomy"]}
    taxa = set(GUT_STOCKS.values())
    arms = {arm["id"]: arm for arm in record["treatment_arms"]}
    assert arms["full"]["membership_status"] == "DEFINED_MEMBERS"
    assert set(arms["full"]["participant_member_ids"]) == members
    for member in members:
        arm = arms[f"dropout_{member}"]
        assert arm["membership_status"] == "DEFINED_MEMBERS"
        assert set(arm["participant_member_ids"]) == members - {member}
    nodes = record["ecological_interactions"]
    pairwise = [node for node in nodes if node.get("scope") == "PAIRWISE"]
    assert len(pairwise) == 1
    feedback = pairwise[0]
    assert feedback["source_taxon"]["term"]["id"] == "NCBITaxon:89152", "positive limb starts at CH"
    assert feedback["target_taxon"]["term"]["id"] == "NCBITaxon:39491", "positive limb ends at ER"
    assert not feedback.get("participating_taxa"), "pairwise feedback is not a twelve-member edge"
    assert {item["evidence_source"] for item in feedback["evidence"]} == {"COMPUTATIONAL"}
    relation_text = re.sub(r"[^a-z0-9]+", " ", feedback["description"].lower())
    assert re.search(r"\bpositive ch to er\b", relation_text)
    assert re.search(r"\bnegative er to ch\b", relation_text)
    assert not re.search(r"\bnegative ch to er\b|\bpositive er to ch\b", relation_text)
    community_nodes = [node for node in nodes if node.get("scope") == "COMMUNITY_LEVEL"]
    assert len(community_nodes) == 2
    for node in community_nodes:
        assert {row["term"]["id"] for row in node["participating_taxa"]} == taxa
    edges = [edge for node in nodes for edge in node.get("downstream", [])]
    assert len(edges) == 1 and edges[0]["target"] == feedback["name"]
    assert not any(node.get("metabolites") for node in nodes), "no demonstrated metabolite mediator"
    assert not record.get(
        "related_ingredients"
    ), "acetate supplementation is not universal mediation"
    assert all(
        "CROSS_FEEDER" not in (row.get("functional_role") or []) for row in record["taxonomy"]
    )


def mutate_brachypodium(record, case):
    if case == "aggregate_taxon":
        record["taxonomy"][0]["taxon_term"]["term"]["id"] = "NCBITaxon:2"
    elif case == "host_complete_roster":
        record["treatment_arms"][1]["membership_status"] = "DEFINED_MEMBERS"
        record["treatment_arms"][1]["participant_member_ids"] = ["rcc-150"]
    elif case == "axenic_buffer":
        record["treatment_arms"][2]["membership_status"] = "NO_MICROBES"
    elif case == "liquid_member_loss":
        record["treatment_arms"][0]["participant_member_ids"].pop()
    elif case == "family_as_stock":
        record["taxonomy"][2]["taxon_term"]["term"]["id"] = "NCBITaxon:1268"
    elif case == "drought_as_recovery":
        record["ecological_interactions"][3]["treatment_arm_ids"] = ["host-drought-syncom"]
    elif case == "predicted_causal_arrow":
        record["ecological_interactions"][0]["downstream"] = [
            {"target": record["ecological_interactions"][3]["name"]}
        ]
    else:
        raise ValueError(case)


def mutate_gut(record, case):
    if case == "aggregate_taxon":
        record["taxonomy"][0]["taxon_term"]["term"]["id"] = "NCBITaxon:2"
    elif case == "dropout_keeps_omitted_stock":
        record["treatment_arms"][1]["participant_member_ids"].append("bh")
    elif case == "reverse_positive_limb":
        feedback = record["ecological_interactions"][2]
        feedback["source_taxon"], feedback["target_taxon"] = (
            feedback["target_taxon"],
            feedback["source_taxon"],
        )
    elif case == "feedback_sign_reversal":
        feedback = record["ecological_interactions"][2]
        feedback["description"] = feedback["description"].replace(
            "positive CH-to-ER", "negative CH-to-ER"
        )
        assert "negative CH-to-ER" in feedback["description"]
    elif case == "whole_community_feedback":
        record["ecological_interactions"][2]["scope"] = "COMMUNITY_LEVEL"
    elif case == "acetate_mediator":
        record["ecological_interactions"][0]["metabolites"] = [
            {"term": {"id": "CHEBI:30089", "label": "acetate"}}
        ]
    elif case == "computational_as_in_vivo":
        record["ecological_interactions"][2]["evidence"][0]["evidence_source"] = "IN_VIVO"
    elif case == "cross_feeder_role_list":
        record["taxonomy"][0]["functional_role"] = ["CROSS_FEEDER"]
    else:
        raise ValueError(case)


BRACH_MUTATIONS = (
    "aggregate_taxon",
    "host_complete_roster",
    "axenic_buffer",
    "liquid_member_loss",
    "family_as_stock",
    "drought_as_recovery",
    "predicted_causal_arrow",
)
GUT_MUTATIONS = (
    "aggregate_taxon",
    "dropout_keeps_omitted_stock",
    "reverse_positive_limb",
    "feedback_sign_reversal",
    "whole_community_feedback",
    "acetate_mediator",
    "computational_as_in_vivo",
    "cross_feeder_role_list",
)


def assert_mutation_rejected(check, mutate, record, case):
    check(record)
    altered = deepcopy(record)
    mutate(altered, case)
    assert altered != record, "mutation must actually change the record"
    with pytest.raises(AssertionError):
        check(altered)
    check(record)


def test_current_brachypodium_scientific_boundaries():
    check_brachypodium(load_current(BRACH))


def test_current_gut_scientific_boundaries():
    check_gut(load_current(GUT))


@pytest.mark.parametrize("case", BRACH_MUTATIONS)
def test_brachypodium_guard_can_fail(case):
    assert_mutation_rejected(check_brachypodium, mutate_brachypodium, load_current(BRACH), case)


@pytest.mark.parametrize("case", GUT_MUTATIONS)
def test_gut_guard_can_fail(case):
    assert_mutation_rejected(check_gut, mutate_gut, load_current(GUT), case)
