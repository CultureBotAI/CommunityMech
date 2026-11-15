"""Bounded one-genus candidate semantics, #2848, 2026-11-15."""

import copy
import importlib.util
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, ROOT / path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.fixture
def candidate():
    stage = load("genus_stage", "scripts/adhoc/stage_code006_genus_grounding_20261115.py")
    native = load("genus_native", "scripts/gtdb_ground.py")
    before = yaml.safe_load((ROOT / stage.TARGET).read_bytes())
    before["taxonomy"][1]["taxon_term"].pop("gtdb_classification", None)
    before["taxonomy"][1]["taxon_term"]["gtdb_grounding_status"] = "NOT_ATTEMPTED"
    block = {
        "gtdb_id": "GTDB:g__Mycobacterium",
        "gtdb_taxon": "Mycobacterium",
        "ncbi_source_id": "NCBITaxon:1763",
        "majority_fraction": 1.0,
        "support_genomes": 18589,
        "total_genomes": 18589,
        "is_reclassified": False,
    }
    after = copy.deepcopy(before)
    after["taxonomy"][1]["taxon_term"]["gtdb_classification"] = block.copy()
    after["taxonomy"][1]["taxon_term"]["gtdb_grounding_status"] = "GROUNDED"
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
    return stage, native, before, after, block


def test_exact_native_events_and_same_genus_payload_pass(candidate):
    stage, native, before, after, block = candidate
    assert len(stage.verify_semantics(before, after, native, block)) == 2


@pytest.mark.parametrize("mutation", ["species", "quote", "other_taxon", "history", "count"])
def test_unreviewed_change_is_rejected_then_restore_passes(candidate, mutation):
    stage, native, before, after, block = candidate
    original = copy.deepcopy(after)
    if mutation == "species":
        after["taxonomy"][1]["taxon_term"]["term"]["label"] = "Mycobacterium tuberculosis"
    elif mutation == "quote":
        after["taxonomy"][1]["evidence"][0]["snippet"] += " Unsupported species identity."
    elif mutation == "other_taxon":
        after["taxonomy"][0]["taxon_term"]["gtdb_grounding_status"] = "GROUNDED"
    elif mutation == "history":
        after["curation_history"][-1]["action"] = "GTDB_REFRESH"
    else:
        after["taxonomy"][1]["taxon_term"]["gtdb_classification"]["total_genomes"] = 18590
    assert after != original
    with pytest.raises(ValueError):
        stage.verify_semantics(before, after, native, block)
    assert len(stage.verify_semantics(before, original, native, block)) == 2
