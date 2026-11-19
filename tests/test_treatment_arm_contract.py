"""Native strict arm/reference controls for #2796 and optional grounding #2429."""

import copy

import pytest
import test_phase2_validation_contracts as native_contracts
import yaml

from communitymech.paths import REPO_ROOT

native = native_contracts.native


@pytest.fixture
def arm_record():
    return yaml.safe_load((REPO_ROOT / "tests/data/treatment_arms.yaml").read_text())


def categories(native, doc):
    return {row["category"] for row in native(doc)}


def test_legacy_minimal_and_full_arm_fixture_pass(native, arm_record):
    assert native({"id": "CommunityMech:900001", "name": "Legacy optional fields"}) == []
    assert native(arm_record) == []
    assert len(arm_record["taxonomy"]) == 2
    assert len(arm_record["taxonomy"][0]["abundance_observations"]) == 2


@pytest.mark.parametrize("kind", ["member", "arm", "timepoint"])
def test_duplicate_local_ids_fail(native, arm_record, kind):
    assert native(arm_record) == []
    if kind == "member":
        arm_record["taxonomy"][1]["member_id"] = "ecoli"
    elif kind == "arm":
        arm_record["treatment_arms"].append(copy.deepcopy(arm_record["treatment_arms"][0]))
    else:
        points = arm_record["treatment_arms"][0]["timepoints"]
        points.append(copy.deepcopy(points[0]))
    assert "treatment_duplicate_id" in categories(native, arm_record)


@pytest.mark.parametrize(
    "target", ["participant", "comparator", "interaction", "observation", "timepoint"]
)
def test_dangling_refs_fail(native, arm_record, target):
    assert native(arm_record) == []
    if target == "participant":
        arm_record["treatment_arms"][0]["participant_member_ids"] = ["missing"]
    elif target == "comparator":
        arm_record["treatment_arms"][1]["comparator_arm_ids"] = ["missing"]
    elif target == "interaction":
        arm_record["ecological_interactions"][0]["treatment_arm_ids"] = ["missing"]
    else:
        key = "treatment_arm_id" if target == "observation" else "timepoint_id"
        arm_record["taxonomy"][0]["abundance_observations"][0][key] = "missing"
    assert "treatment_unknown_reference" in categories(native, arm_record)


@pytest.mark.parametrize("problem", ["self", "context"])
def test_comparator_boundaries(native, arm_record, problem):
    assert native(arm_record) == []
    if problem == "self":
        arm_record["treatment_arms"][1]["comparator_arm_ids"] = ["amended"]
    else:
        arm_record["treatment_arms"][0]["context"] = "different-assay"
    assert "treatment_comparator_scope" in categories(native, arm_record)


@pytest.mark.parametrize(
    "problem", ["empty-defined", "unknown-with-members", "sterile-with-members"]
)
def test_explicit_membership_states(native, arm_record, problem):
    assert native(arm_record) == []
    arm = arm_record["treatment_arms"][0]
    if problem == "empty-defined":
        arm["participant_member_ids"] = []
    else:
        arm["membership_status"] = (
            "NOT_REPORTED" if problem == "unknown-with-members" else "NO_MICROBES"
        )
    assert "treatment_membership_scope" in categories(native, arm_record)


@pytest.mark.parametrize("problem", ["missing-member-id", "excluded", "sterile"])
def test_observation_member_scope(native, arm_record, problem):
    assert native(arm_record) == []
    if problem == "missing-member-id":
        del arm_record["taxonomy"][0]["member_id"]
    elif problem == "excluded":
        arm_record["treatment_arms"][1]["participant_member_ids"] = ["bacillus"]
    else:
        arm = arm_record["treatment_arms"][1]
        arm["membership_status"] = "NO_MICROBES"
        arm.pop("participant_member_ids")
    assert "treatment_observation_scope" in categories(native, arm_record)


@pytest.mark.parametrize(
    "kind", ["missing-absolute-unit", "missing-relative-unit", "unit-without-value", "no-value"]
)
def test_abundance_requires_explicit_measure_and_units(native, arm_record, kind):
    assert native(arm_record) == []
    obs = arm_record["taxonomy"][0]["abundance_observations"]
    if kind == "missing-absolute-unit":
        del obs[0]["absolute_abundance_unit"]
    elif kind == "missing-relative-unit":
        del obs[1]["relative_abundance_unit"]
    elif kind == "unit-without-value":
        del obs[0]["absolute_abundance"]
    else:
        obs[0].pop("absolute_abundance")
        obs[0].pop("absolute_abundance_unit")
    assert "treatment_abundance_measure" in categories(native, arm_record)


@pytest.mark.parametrize("slot", ["absolute_abundance", "relative_abundance"])
@pytest.mark.parametrize("value", [float("inf"), float("-inf"), float("nan"), -0.1])
def test_abundances_finite_nonnegative(native, arm_record, slot, value):
    assert native(arm_record) == []
    obs = arm_record["taxonomy"][0]["abundance_observations"][
        0 if slot.startswith("absolute") else 1
    ]
    obs[slot] = value
    assert "treatment_abundance_value" in categories(native, arm_record)


@pytest.mark.parametrize("unit, limit", [("FRACTION", 1.0), ("PERCENT", 100.0)])
def test_relative_scales_are_explicit(native, arm_record, unit, limit):
    obs = arm_record["taxonomy"][0]["abundance_observations"][1]
    obs.update(relative_abundance_unit=unit, relative_abundance=limit)
    assert native(arm_record) == []
    obs["relative_abundance"] = limit + 0.1
    assert "treatment_abundance_value" in categories(native, arm_record)


def test_elapsed_needs_anchor_and_finiteness(native, arm_record):
    assert native(arm_record) == []
    point = arm_record["treatment_arms"][0]["timepoints"][0]
    point["elapsed"]["value"] = float("inf")
    assert "quantity_nonfinite" in categories(native, arm_record)
    point["elapsed"]["value"] = 24.0
    del point["reference_event"]
    assert "treatment_timepoint_anchor" in categories(native, arm_record)


def test_optional_factor_term_preserves_legacy_values(native, arm_record):
    arm_record["environmental_factors"] = [{"name": "temperature", "value": "25", "unit": "C"}]
    assert native(arm_record) == []
    arm_record["environmental_factors"][0]["term"] = {"id": "PATO:0000146", "label": "temperature"}
    assert native(arm_record) == []


def test_new_enum_roots_and_binding_are_checked_not_arbitrary_strings():
    schema = yaml.safe_load((REPO_ROOT / "src/communitymech/schema/communitymech.yaml").read_text())
    factor = schema["enums"]["EnvironmentalFactorTerm"]["reachable_from"]
    assert factor["source_nodes"] == ["CHEBI:24431", "PATO:0000001", "ENVO:01000203"]
    assert factor["include_self"] is False
    assert schema["classes"]["EnvironmentalFactor"]["attributes"]["term"]["bindings"] == [
        {"binds_value_of": "id", "range": "EnvironmentalFactorTerm", "obligation_level": "REQUIRED"}
    ]


def test_generated_model_preserves_arm_observations(arm_record):
    from linkml_runtime.dumpers import yaml_dumper
    from linkml_runtime.loaders import yaml_loader

    from communitymech.datamodel.communitymech import (
        AbundanceObservation,
        MicrobialCommunity,
        TreatmentArm,
    )

    loaded = MicrobialCommunity(**copy.deepcopy(arm_record))
    assert loaded.taxonomy[0].member_id == "ecoli"
    assert len(loaded.taxonomy[0].abundance_observations) == 2
    assert loaded.taxonomy[0].abundance_observations[0].absolute_abundance_unit == "CFU/mL"
    assert loaded.treatment_arms[1].comparator_arm_ids == ["vehicle"]
    assert loaded.treatment_arms[1].timepoints[0].elapsed.value == 24
    dumped = yaml_dumper.dumps(loaded)
    payload = yaml.safe_load(dumped)
    assert (
        payload["taxonomy"][0]["abundance_observations"]
        == arm_record["taxonomy"][0]["abundance_observations"]
    )
    assert payload["treatment_arms"] == arm_record["treatment_arms"]
    # Full-record reload is the pre-existing scope-enum default defect #1703.
    # The new model components must actually survive dump/reload unchanged.
    for arm in loaded.treatment_arms:
        serialized = yaml_dumper.dumps(arm)
        reloaded = yaml_loader.loads(serialized, target_class=TreatmentArm)
        assert yaml.safe_load(yaml_dumper.dumps(reloaded)) == yaml.safe_load(serialized)
    for observation in loaded.taxonomy[0].abundance_observations:
        serialized = yaml_dumper.dumps(observation)
        reloaded_observation = yaml_loader.loads(serialized, target_class=AbundanceObservation)
        assert yaml.safe_load(yaml_dumper.dumps(reloaded_observation)) == yaml.safe_load(serialized)
    assert loaded.taxonomy[0].relative_abundance == 0.5


def test_legacy_taxonomy_and_deposits_materialize_without_key_collapsing():
    from communitymech.datamodel.communitymech import MicrobialCommunity

    path = REPO_ROOT / "kb/communities/EcoFAB_Ring_Trial_SynCom17.yaml"
    original = yaml.safe_load(path.read_text())
    loaded = MicrobialCommunity(**copy.deepcopy(original))
    assert len(loaded.taxonomy) == len(original["taxonomy"])
    for before, after in zip(original["taxonomy"], loaded.taxonomy, strict=True):
        assert after.taxon_term.preferred_term == before["taxon_term"]["preferred_term"]
        assert after.strain_designation.strain_name == before["strain_designation"]["strain_name"]
        expected = before["strain_designation"].get("culture_collections") or []
        assert [
            (str(item.collection), item.accession)
            for item in after.strain_designation.culture_collections
        ] == [(item["collection"], item["accession"]) for item in expected]


@pytest.mark.parametrize("term", ["CHEBI:24431", "PATO:0000001", "ENVO:01000203"])
@pytest.mark.parametrize("location", ["record", "arm"])
def test_new_factor_roots_are_rejected_by_strict_guard(native, arm_record, term, location):
    assert native(arm_record) == []
    factors = [{"name": "generic factor", "term": {"id": term, "label": "generic root"}}]
    if location == "record":
        arm_record["environmental_factors"] = factors
    else:
        arm_record["treatment_arms"][0]["conditions"] = factors
    assert "environmental_factor_generic_root" in categories(native, arm_record)


def test_time_root_is_rejected_by_strict_guard(native, arm_record):
    assert native(arm_record) == []
    arm_record["treatment_arms"][0]["timepoints"][0]["elapsed"]["unit"] = {
        "id": "UO:0000003",
        "label": "time unit",
    }
    assert "time_quantity_generic_root" in categories(native, arm_record)


@pytest.mark.parametrize("value", [None, "", "   "])
def test_measurement_basis_cannot_be_null_or_blank(native, arm_record, value):
    assert native(arm_record) == []
    arm_record["taxonomy"][0]["abundance_observations"][0]["measurement_basis"] = value
    assert native(arm_record)


@pytest.mark.parametrize(
    "slot", ["participant_member_ids", "comparator_arm_ids", "treatment_arm_ids"]
)
def test_duplicate_references_fail(native, arm_record, slot):
    assert native(arm_record) == []
    target = (
        arm_record["ecological_interactions"][0]
        if slot == "treatment_arm_ids"
        else arm_record["treatment_arms"][1]
    )
    target[slot].append(target[slot][0])
    assert "treatment_duplicate_reference" in categories(native, arm_record)


def test_malformed_optional_structures_report_errors_without_crashing(native, arm_record):
    assert native(arm_record) == []
    arm_record["treatment_arms"][0]["membership_status"] = {"bad": "shape"}
    arm_record["taxonomy"][0]["abundance_observations"][0]["absolute_abundance_unit"] = {
        "bad": "unit"
    }
    assert native(arm_record)


@pytest.mark.parametrize("field", ["id", "name", "context", "membership_status"])
def test_arm_required_fields_cannot_be_null(native, arm_record, field):
    assert native(arm_record) == []
    arm_record["treatment_arms"][2][field] = None
    assert "treatment_required_value" in categories(native, arm_record)


@pytest.mark.parametrize("field", ["id", "name"])
def test_timepoint_required_fields_cannot_be_null(native, arm_record, field):
    assert native(arm_record) == []
    arm_record["treatment_arms"][0]["timepoints"][0][field] = None
    assert "treatment_required_value" in categories(native, arm_record)


def test_elapsed_value_cannot_be_null(native, arm_record):
    assert native(arm_record) == []
    arm_record["treatment_arms"][0]["timepoints"][0]["elapsed"]["value"] = None
    assert "quantity_invalid_value" in categories(native, arm_record)
