"""Protect real genus science/history and strict successor proof boundaries (#2848)."""

import copy
import json
import subprocess
from pathlib import Path

import pytest
import scoped_gtdb_successor as successor
import yaml

ROOT = Path(__file__).resolve().parents[1]
BASE = "68699871415fda3c9eebf20382a315f9f3c7b17a"


@pytest.fixture(params=["000552", "000553"])
def actual_genus(request):
    directory = ROOT / f"reports/gtdb-code006-20261115/isolate-{request.param}-001"
    route = json.loads((directory / "native-recomputation.json").read_bytes())
    before_raw = subprocess.check_output(["git", "show", f"{BASE}:{route['target']}"], cwd=ROOT)
    before = yaml.safe_load(before_raw)
    after = yaml.safe_load((ROOT / route["target"]).read_bytes())
    source = {
        "occurrences": [
            {
                "taxonomy_index": 0,
                "term": before["taxonomy"][0]["taxon_term"]["term"],
                "strain_name": before["taxonomy"][0]["strain_designation"]["strain_name"],
                "existing_descriptor": before["taxonomy"][0]["taxon_term"],
                "native_result": route["result"],
            }
        ]
    }
    return before, after, source


def test_actual_two_genus_successors_preserve_original_science_and_history(actual_genus):
    before, after, source = actual_genus
    successor.verify_projection(before, after, source, [0])
    assert before["curation_history"][-1]["llm_assisted"] is True
    assert after["curation_history"][-1]["curator"] == "gtdb_ground.py"
    # The historical event remains present; callers must not fabricate an LLM
    # flag on the new native event to satisfy an old last-event assertion.
    assert (
        after["curation_history"][: len(before["curation_history"])] == before["curation_history"]
    )


@pytest.mark.parametrize(
    "mutation",
    [
        "biology",
        "stock",
        "old_history",
        "native_event",
        "denominator",
        "provenance",
        "wrong_source_id",
        "withheld",
        "descriptor",
        "duplicate_selector",
        "extra_selector",
    ],
)
def test_actual_projection_mutation_refuses_and_restores(actual_genus, mutation):
    before, after, source = actual_genus
    successor.verify_projection(before, after, source, [0])
    old, new, proof = copy.deepcopy((before, after, source))
    indices = [0]
    if mutation == "biology":
        new["description"] += " Invented ecological mechanism."
    elif mutation == "stock":
        new["taxonomy"][0]["strain_designation"]["strain_name"] = "unreviewed-stock"
    elif mutation == "old_history":
        new["curation_history"][0]["changes"] += " Unreviewed alteration."
    elif mutation == "native_event":
        new["curation_history"][-1]["changes"] = "Wrote status on 99 taxa."
    elif mutation == "denominator":
        new["taxonomy"][0]["taxon_term"]["gtdb_classification"]["total_genomes"] += 1
    elif mutation == "provenance":
        new["taxonomy"][0]["taxon_term"]["gtdb_classification"]["mapping_source"] += " unreviewed"
    elif mutation == "wrong_source_id":
        proof["occurrences"][0]["native_result"]["ncbi_source_id"] = "NCBITaxon:2"
    elif mutation == "withheld":
        old["taxonomy"][0]["taxon_term"]["gtdb_grounding_status"] = "WITHHELD"
        proof["occurrences"][0]["existing_descriptor"] = copy.deepcopy(
            old["taxonomy"][0]["taxon_term"]
        )
    elif mutation == "descriptor":
        proof["occurrences"][0]["existing_descriptor"]["notes"] += " invented"
    elif mutation == "duplicate_selector":
        proof["occurrences"].append(copy.deepcopy(proof["occurrences"][0]))
    else:
        indices = [0, 1]
    assert (old, new, proof, indices) != (before, after, source, [0])
    with pytest.raises(AssertionError):
        successor.verify_projection(old, new, proof, indices)
    successor.verify_projection(before, after, source, [0])


def test_ambiguous_options_are_complete_and_no_species_is_chosen():
    term = {
        "term": {"id": "NCBITaxon:123", "label": "Example species"},
        "gtdb_grounding_status": "UNRESOLVED",
    }
    before = {
        "id": "CommunityMech:000001",
        "taxonomy": [{"taxon_term": term}],
        "curation_history": [],
    }
    source = {
        "occurrences": [
            {
                "taxonomy_index": 0,
                "term": term["term"],
                "strain_name": None,
                "existing_descriptor": copy.deepcopy(term),
                "native_result": {
                    "ambiguous": True,
                    "ncbi_source_id": "NCBITaxon:123",
                    "gtdb_options": ["GTDB:s__Example_species_A", "GTDB:s__Example_species_B"],
                },
            }
        ]
    }
    after = copy.deepcopy(before)
    after["taxonomy"][0]["taxon_term"].update(
        gtdb_grounding_status="AMBIGUOUS",
        gtdb_candidates=source["occurrences"][0]["native_result"]["gtdb_options"],
    )
    after["curation_history"] = [
        {
            "timestamp": "2026-11-15T06:00:00Z",
            "curator": "gtdb_ground.py",
            "action": "GTDB_SET_STATUS",
            "changes": "Wrote gtdb_grounding_status on 1 taxonomy entries (#294, #395).",
        }
    ]
    successor.verify_projection(before, after, source, [0])
    mutated = copy.deepcopy(after)
    mutated["taxonomy"][0]["taxon_term"]["gtdb_candidates"].pop()
    with pytest.raises(AssertionError, match="scientific content"):
        successor.verify_projection(before, mutated, source, [0])
    successor.verify_projection(before, after, source, [0])


def test_artifact_hash_and_snapshot_mutation_refuse_then_restore(tmp_path):
    path = tmp_path / "proof.json"
    raw = b'{"version":1}\n'
    path.write_bytes(raw)
    item = {"path": path.name, "sha256": successor.digest(raw)}
    artifacts = successor.Artifacts(tmp_path)
    assert artifacts.read(item) == raw
    artifacts.verify()
    path.write_bytes(b'{"version":2}\n')
    with pytest.raises(AssertionError, match="changed during"):
        artifacts.verify()
    with pytest.raises(AssertionError, match="hash differs"):
        successor.Artifacts(tmp_path).read(item)
    path.write_bytes(raw)
    assert artifacts.read(item) == raw
    artifacts.verify()


def test_unknown_record_needs_no_exception_until_it_changes(tmp_path):
    path = tmp_path / "record.yaml"
    raw = b"id: CommunityMech:000001\n"
    path.write_bytes(raw)
    expected = successor.digest(raw)
    result = successor.admit(tmp_path, path.name, expected, {})
    assert result.historical_bytes == raw and not result.changed
    path.write_bytes(raw + b"description: unreviewed\n")
    with pytest.raises(AssertionError, match="unknown changed"):
        successor.admit(tmp_path, path.name, expected, {})
    path.write_bytes(raw)
    assert successor.admit(tmp_path, path.name, expected, {}).current_sha256 == expected


def test_native_serialization_matches_real_preserved_result(actual_genus):
    from scripts.gtdb_ground import _block

    assert successor.digest((ROOT / successor.NATIVE).read_bytes()) == successor.NATIVE_SHA
    _before, after, source = actual_genus
    native_result = source["occurrences"][0]["native_result"]
    actual = after["taxonomy"][0]["taxon_term"]["gtdb_classification"]
    base = actual["mapping_source"].split(" [grounded at", 1)[0]
    assert (
        successor.expected_block(native_result, actual["mapping_source"])
        == _block(native_result, base)
        == actual
    )


def population(size):
    identities = [f"CommunityMech:{index:06d}" for index in range(size)]
    return {
        "kind": "record" if size == 1 else "batch",
        "targets": [
            {"target_id": identity, "path": f"kb/communities/unit-{index}.yaml"}
            for index, identity in enumerate(identities)
        ],
        "scope": {"population_size": size, "reviewed_target_ids": identities},
    }


@pytest.mark.parametrize("size", [1, 2, 10])
def test_exact_bounded_population_positive(size):
    successor.verify_population(population(size))


@pytest.mark.parametrize(
    "mutation",
    ["eleven", "zero", "kind", "population", "boolean", "ids", "duplicate_id", "duplicate_path"],
)
def test_population_contract_refuses_then_restores(mutation):
    original = population(2)
    successor.verify_population(original)
    altered = copy.deepcopy(original)
    if mutation == "eleven":
        altered = population(11)
    elif mutation == "zero":
        altered = population(0)
    elif mutation == "kind":
        altered["kind"] = "record"
    elif mutation == "population":
        altered["scope"]["population_size"] = 3
    elif mutation == "boolean":
        altered = population(1)
        altered["scope"]["population_size"] = True
    elif mutation == "ids":
        altered["scope"]["reviewed_target_ids"] = ["CommunityMech:999999", "CommunityMech:000001"]
    elif mutation == "duplicate_id":
        altered["targets"][1]["target_id"] = altered["targets"][0]["target_id"]
        altered["scope"]["reviewed_target_ids"] = [row["target_id"] for row in altered["targets"]]
    else:
        altered["targets"][1]["path"] = altered["targets"][0]["path"]
    assert altered != original
    with pytest.raises(AssertionError, match="review population"):
        successor.verify_population(altered)
    successor.verify_population(original)
