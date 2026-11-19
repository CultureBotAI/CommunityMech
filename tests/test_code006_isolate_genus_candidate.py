"""Same-genus candidates cannot change biology or old history (#2848)."""

import copy
import importlib.util
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, ROOT / path)
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


@pytest.fixture(
    params=[
        ("Pelagerythrobacter_N7_Halophilic_Pyrene_Oxidation_Isolate_Baseline", 16),
        ("Salinicola_A11_Halophilic_Bioemulsifier_Decarboxylase_Isolate_Baseline", 46),
    ]
)
def candidate(request):
    stage = module("isolate_stage", "scripts/adhoc/stage_code006_isolate_genus_20261115.py")
    native = module("isolate_native", "scripts/gtdb_ground.py")
    filename, count = request.param
    before = yaml.safe_load((ROOT / f"data/isolates/{filename}.yaml").read_bytes())
    term = before["taxonomy"][0]["taxon_term"]
    term.pop("gtdb_classification", None)
    term["gtdb_grounding_status"] = "UNRESOLVED"
    block = {
        "gtdb_id": "GTDB:g__" + term["term"]["label"],
        "gtdb_taxon": term["term"]["label"],
        "ncbi_source_id": term["term"]["id"],
        "total_genomes": count,
        "support_genomes": count,
        "majority_fraction": 1.0,
        "is_reclassified": False,
    }
    after = copy.deepcopy(before)
    after["taxonomy"][0]["taxon_term"].update(
        gtdb_classification=block.copy(), gtdb_grounding_status="GROUNDED"
    )
    for action, changes in (
        ("GTDB_GROUND", "Added 1 gtdb_classification block(s) from NCBI2GTDB.tsv.gz (#395)."),
        ("GTDB_SET_STATUS", "Wrote gtdb_grounding_status on 1 taxonomy entries (#294, #395)."),
    ):
        native.record_curation_event(
            after,
            curator="gtdb_ground.py",
            action=action,
            changes=changes,
            timestamp="2026-11-15T00:00:00Z",
        )
    return stage, native, before, after, block, {"record_id": before["id"]}


def test_exact_native_same_genus_candidate(candidate):
    stage, native, before, after, block, row = candidate
    assert len(stage.verify_semantics(before, after, native, block, row)) == 2


@pytest.mark.parametrize(
    "mutation", ["species", "evidence", "graph", "old_history", "new_history", "count"]
)
def test_unreviewed_mutation_fails_then_restore_passes(candidate, mutation):
    stage, native, before, after, block, row = candidate
    assert stage.verify_semantics(before, after, native, block, row)
    original = copy.deepcopy(after)
    if mutation == "species":
        after["taxonomy"][0]["taxon_term"]["term"]["label"] += " invented_species"
    elif mutation == "evidence":
        after["taxonomy"][0]["evidence"][0]["snippet"] += " Invented support."
    elif mutation == "graph":
        after["ecological_interactions"][0]["description"] += " Invented causal mechanism."
    elif mutation == "old_history":
        after["curation_history"][0]["changes"] = "Rewritten previous observation"
    elif mutation == "new_history":
        after["curation_history"][-1]["action"] = "GTDB_REFRESH"
    else:
        after["taxonomy"][0]["taxon_term"]["gtdb_classification"]["support_genomes"] += 1
    assert after != original
    with pytest.raises(ValueError):
        stage.verify_semantics(before, after, native, block, row)
    assert stage.verify_semantics(before, original, native, block, row)
