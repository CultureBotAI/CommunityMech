"""Protect source-defined rosters, assay scope and read abundance (#1427/#1548/#2675).

Expected rosters come from Coker Methods, Ding Methods and the ring-trial S2
table; the four root-read means come from ring-trial Results 2.4. These checks
supplement immutable scientific reviews and do not infer new biological claims.
"""

from copy import deepcopy
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]
PATHS = {
    "ring": "EcoFAB_Ring_Trial_SynCom17",
    "soil": "LBNL_Switchgrass_Soil_SynCom16",
    "dopamine": "Brachypodium_Natural_Variation_Dopamine_SynCom16",
}
COKER = {
    "OAP107",
    "OAE506",
    "OAE829",
    "OAP136",
    "OAS925",
    "OAE865",
    "OAE881",
    "OAE513",
    "OAE612",
    "OAE515",
    "OAE908",
    "OAS944",
    "OAE614",
    "OAE497",
    "OAS809",
    "OAS795",
}


def records():
    return {
        key: yaml.safe_load((ROOT / "kb/communities" / (name + ".yaml")).read_bytes())
        for key, name in PATHS.items()
    }


def check_records(documents):
    rosters = {
        key: {row["strain_designation"]["strain_name"]: row for row in doc["taxonomy"]}
        for key, doc in documents.items()
    }
    assert set(rosters["soil"]) == COKER
    assert set(rosters["ring"]) == COKER | {"OAE603"}
    assert set(rosters["dopamine"]) == (COKER - {"OAE829"}) | {"OAE603"}
    cohort_ids = {doc["id"] for doc in documents.values()}
    for key, roster in rosters.items():
        assert len(roster) == len(documents[key]["taxonomy"])
        assert roster["OAP107"]["taxon_term"]["term"]["id"] == "NCBITaxon:1663"
        deposits = roster["OAS925"]["strain_designation"]["culture_collections"]
        assert any(
            row["collection"] == "DSM" and str(row["accession"]) == "113627" for row in deposits
        )
        assert all(str(row["accession"]) != "200000SY" for row in deposits)
        links = [
            row for row in documents[key]["related_communities"] if row["identifier"] in cohort_ids
        ]
        assert {row["identifier"] for row in links} == cohort_ids - {documents[key]["id"]}
        assert all(row["basis"] == "SHARED_STRAIN_DESIGNATIONS" for row in links)

    soil = documents["soil"]
    assert not soil.get(
        "ecological_interactions"
    ), "earlier assays cannot become final-16 graph claims"
    discussions = {row["discussion_id"]: row for row in soil["discussions"]}
    for name in (
        "earlier18_nutrient_response",
        "earlier17_18_ratio_response",
        "earlier17_18_ecofab_colonization",
    ):
        assert name in discussions
        assert discussions[name]["evidence"], "measured earlier observations must remain preserved"
        assert all(row["snippet"] and row["reference"] for row in discussions[name]["evidence"])
    assert "methods_final16_vs_supplement_table_s1" in discussions

    ring = documents["ring"]
    arms = {row["id"]: row for row in ring["treatment_arms"]}
    assert set(arms) == {"syncom17", "syncom16-minus-oas925", "axenic-mock", "plant-free-mock"}
    expected_members = {name.lower() for name in rosters["ring"]}
    for name, members in (
        ("syncom17", expected_members),
        ("syncom16-minus-oas925", expected_members - {"oas925"}),
    ):
        assert arms[name]["membership_status"] == "DEFINED_MEMBERS"
        assert set(arms[name]["participant_member_ids"]) == members
    for name in ("axenic-mock", "plant-free-mock"):
        assert arms[name]["membership_status"] == "NO_MICROBES"
        assert not arms[name].get("participant_member_ids")
    observations = {
        name: row["abundance_observations"]
        for name, row in rosters["ring"].items()
        if row.get("abundance_observations")
    }
    assert set(observations) == {"OAS925", "OAS809", "OAE908", "OAE515"}
    for name, mean in {"OAS925": 98, "OAS809": 68, "OAE908": 14, "OAE515": 15}.items():
        assert len(observations[name]) == 1
        observation = observations[name][0]
        arm = "syncom17" if name == "OAS925" else "syncom16-minus-oas925"
        assert observation["treatment_arm_id"] == arm
        assert observation["relative_abundance"] == mean
        assert observation["relative_abundance_unit"] == "PERCENT"
        basis = observation["measurement_basis"].lower()
        assert "relative" in basis and "16s" in basis and "read" in basis
        timepoint = next(
            row for row in arms[arm]["timepoints"] if row["id"] == observation["timepoint_id"]
        )
        assert timepoint["name"] == "22 days after inoculation"
    assert all(not row.get("functional_role") for row in ring["taxonomy"])
    genomes = [row for row in ring["associated_datasets"] if row["repository"] == "JGI_IMG"]
    assert len(genomes) == len({row["accession"] for row in genomes}) == 17
    assert {row["organism"].split()[-1] for row in genomes} == set(rosters["ring"])
    assert all(
        str(row["accession"]).isdigit() and len(str(row["accession"])) == 10 for row in genomes
    )
    mycobacterium = next(row for row in genomes if row["organism"].endswith("OAE908"))
    assert mycobacterium["accession"] == "2852593896"
    assert "Gp0440934" in mycobacterium["evidence"][0]["snippet"]


def test_current_linked_scientific_boundaries():
    check_records(records())


@pytest.mark.parametrize(
    "mutation",
    [
        "wrong_roster",
        "consortium_deposit",
        "transferred_assay",
        "lost_observation",
        "wrong_arm",
        "absolute_count",
        "omitted_genome",
        "invented_role",
    ],
)
def test_linked_scientific_boundaries_reject_regression(mutation):
    original = records()
    changed = deepcopy(original)
    ring = changed["ring"]
    if mutation == "wrong_roster":
        changed["soil"]["taxonomy"][0]["strain_designation"]["strain_name"] = "OAE603"
    elif mutation == "consortium_deposit":
        row = next(
            row for row in ring["taxonomy"] if row["strain_designation"]["strain_name"] == "OAS925"
        )
        row["strain_designation"]["culture_collections"][0]["accession"] = "200000SY"
    elif mutation == "transferred_assay":
        changed["soil"]["ecological_interactions"] = [
            {"name": "Earlier assay transferred to final 16"}
        ]
    elif mutation == "lost_observation":
        changed["soil"]["discussions"] = [
            row
            for row in changed["soil"]["discussions"]
            if row["discussion_id"] != "earlier18_nutrient_response"
        ]
    elif mutation in {"wrong_arm", "absolute_count"}:
        row = next(
            row for row in ring["taxonomy"] if row["strain_designation"]["strain_name"] == "OAS809"
        )
        observation = row["abundance_observations"][0]
        observation["treatment_arm_id" if mutation == "wrong_arm" else "measurement_basis"] = (
            "syncom17" if mutation == "wrong_arm" else "Absolute viable cells"
        )
    elif mutation == "omitted_genome":
        ring["associated_datasets"] = [
            row
            for row in ring["associated_datasets"]
            if not row.get("organism", "").endswith("OAE908")
        ]
    else:
        ring["taxonomy"][0]["functional_role"] = ["PRIMARY_DEGRADER"]
    assert changed != original
    with pytest.raises(AssertionError):
        check_records(changed)
    check_records(original)
