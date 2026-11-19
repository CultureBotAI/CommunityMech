"""Native controls for primitive arm references silently losing non-string values (#2807)."""

import copy

import pytest
import test_treatment_arm_contract as arm_contract

native = arm_contract.native
arm_record = arm_contract.arm_record


@pytest.mark.parametrize("bad", [7, None, {"id": "ecoli"}])
@pytest.mark.parametrize(
    "slot", ["participant_member_ids", "comparator_arm_ids", "treatment_arm_ids"]
)
def test_reference_lists_reject_non_string_items(native, arm_record, slot, bad):
    assert native(arm_record) == []
    target = (
        arm_record["ecological_interactions"][0]
        if slot == "treatment_arm_ids"
        else arm_record["treatment_arms"][1]
    )
    original = copy.deepcopy(target[slot])
    target[slot].append(bad)
    assert any(
        row["category"] == "treatment_reference_type" for row in native(arm_record)
    ), f"{slot} silently dropped {bad!r}"
    target[slot] = original
    assert native(arm_record) == []


@pytest.mark.parametrize("bad", [7, None, {"id": "ecoli"}])
def test_microbe_free_arm_cannot_silently_discard_a_bad_participant(native, arm_record, bad):
    assert native(arm_record) == []
    arm_record["treatment_arms"][2]["participant_member_ids"] = [bad]
    assert any(row["category"] == "treatment_reference_type" for row in native(arm_record))
    arm_record["treatment_arms"][2].pop("participant_member_ids")
    assert native(arm_record) == []


@pytest.mark.parametrize("bad", [7, {"id": "ecoli"}])
def test_unreferenced_member_id_must_be_a_string(native, arm_record, bad):
    doc = {
        "id": "CommunityMech:900001",
        "name": "unreferenced identifier control",
        "taxonomy": [
            {
                "member_id": "ecoli",
                "taxon_term": copy.deepcopy(arm_record["taxonomy"][0]["taxon_term"]),
            }
        ],
    }
    assert native(doc) == []
    doc["taxonomy"][0]["member_id"] = bad
    assert any(row["category"] == "treatment_reference_type" for row in native(doc))
    doc["taxonomy"][0]["member_id"] = "ecoli"
    assert native(doc) == []
