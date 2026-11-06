"""Read-only controls for exact partial-review lineage and action preservation.

Only a new JSON receipt is written under the PR scratch directory. Mutations are
in-memory copies; maintained reviews, source inputs and records are never edited.
"""

import copy
import importlib.util
import json
from pathlib import Path
from unittest.mock import patch

import yaml

HELPER = Path("scripts/adhoc/batch_review_input_provenance.py")
ORIGINAL = Path(
    "reviews/structured/20261022T044407Z-dehalococcoides-desulfovibrio-record-review/review.yaml"
)
CURRENT = Path(
    "reviews/structured/20261106T192226Z-dhc-dvh-cultivation-locator-correction/review.yaml"
)
OUT = Path(".temp/pr2061/process-controls.json")
TARGET = "CommunityMech:000199"


def main():
    spec = importlib.util.spec_from_file_location("provenance_helper", HELPER)
    helper = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(helper)
    original = yaml.safe_load(ORIGINAL.read_text())
    current = yaml.safe_load(CURRENT.read_text())
    keys = {f["issue_key"] for f in original["findings"]}
    active = [(original, str(ORIGINAL), keys)]
    selected = helper.apply_partial_successors(active, [str(CURRENT)], TARGET)
    assert selected[0][2] == keys - {"cm-000199-cultivation"}
    assert selected[1][2] == {"cm-000199-cultivation"}
    actions = [
        (r["review_id"], a)
        for r, _, retained in selected
        for a in helper.retained_actions(r, retained)
    ]
    native = json.loads(Path(".temp/pr2061/199-correction/native-cohort-triage.json").read_text())
    expected = [
        (a["review_id"], a["action"])
        for a in native["planning_inputs"]
        if set(a["for_issues"]) & keys
    ]

    def identity(row):
        return row[0], row[1]["action_id"]

    assert sorted(actions, key=identity) == sorted(expected, key=identity)
    assert len(actions) == 7
    assert sum(len(a["acceptance_checks"]) for _, a in actions) == 15

    cases = {}
    for name in ["missing-lineage", "wrong-finding", "lost-target", "unconfigured-new-key"]:
        altered = copy.deepcopy(current)
        if name == "missing-lineage":
            altered["findings"][0]["previous_occurrences"] = []
        elif name == "wrong-finding":
            altered["findings"][0]["previous_occurrences"][0]["finding_id"] = "omics-evidence"
        elif name == "lost-target":
            altered["findings"][0]["target_ids"] = []
        else:
            altered["findings"][0]["issue_key"] = "unconfigured-key"
        assert altered != current
        with patch.object(helper, "read_review", return_value=altered):
            try:
                helper.apply_partial_successors(active, [str(CURRENT)], TARGET)
            except ValueError as exc:
                cases[name] = str(exc)
            else:
                raise AssertionError(f"Invalid partial successor accepted: {name}")
        # Immediate unmutated control verifies the harness, not merely a red.
        assert helper.apply_partial_successors(active, [str(CURRENT)], TARGET) == selected

    duplicate = active + [(copy.deepcopy(original), "duplicate", keys)]
    try:
        helper.apply_partial_successors(duplicate, [str(CURRENT)], TARGET)
    except ValueError as exc:
        cases["ambiguous-predecessors"] = str(exc)
    else:
        raise AssertionError("Ambiguous predecessor heads accepted")
    assert helper.apply_partial_successors(active, [str(CURRENT)], TARGET) == selected

    synthetic = copy.deepcopy(original)
    prerequisite = copy.deepcopy(synthetic["actions"][0])
    prerequisite["action_id"] = "prerequisite-fixture"
    prerequisite["finding_ids"] = ["cultivation"]
    synthetic["actions"].append(prerequisite)
    surviving = next(a for a in synthetic["actions"] if "omics-evidence" in a["finding_ids"])
    surviving["depends_on"] = ["prerequisite-fixture"]
    retained = helper.retained_actions(synthetic, keys - {"cm-000199-cultivation"})
    assert prerequisite in retained
    assert original == yaml.safe_load(ORIGINAL.read_text())
    assert current == yaml.safe_load(CURRENT.read_text())
    receipt = {
        "exact_native_199_actions": len(actions),
        "exact_native_199_acceptance_checks": 15,
        "exact_action_objects_preserved": True,
        "negative_controls": cases,
        "prerequisite_closure": True,
        "all_immediate_unmutated_controls_passed": True,
        "scope": "Read-only process controls; no literature or scientific verdict reassessment.",
    }
    if OUT.exists():
        raise ValueError(f"Refusing to overwrite control receipt: {OUT}")
    OUT.write_text(json.dumps(receipt, indent=2) + "\n")
    print(json.dumps(receipt))


if __name__ == "__main__":
    main()
