"""Required adapter coverage and immutable provenance controls for #2817."""

import importlib
import sys
from pathlib import Path

import pytest
import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts/adhoc"))
runner = importlib.import_module("check_phase2_linked_records_20261115")


@pytest.fixture
def adapters(tmp_path):
    result = {}
    for prefix in runner.REQUIRED_ONTOLOGIES:
        path = tmp_path / (prefix.lower() + ".db")
        path.write_bytes(b"hash-binding fixture: " + prefix.encode())
        result[prefix] = path
    return result


def test_complete_config_binds_all_six_local_inputs(tmp_path, adapters):
    config = tmp_path / "oak.yaml"
    before = runner.prepare_ontology_config(config, adapters)
    assert set(before) == {"NCBITaxon", "ENVO", "PO", "UBERON", "CHEBI", "GO"}
    assert yaml.safe_load(config.read_text())["ontology_adapters"] == {
        prefix: "sqlite:" + str(path) for prefix, path in adapters.items()
    }
    assert runner.ontology_manifest(adapters) == before


@pytest.mark.parametrize("missing", ["PO", "UBERON", "CHEBI", "GO"])
def test_omitted_prefix_rejected_before_config_write(tmp_path, adapters, missing):
    del adapters[missing]
    config = tmp_path / "oak.yaml"
    with pytest.raises(ValueError, match="missing required ontology prefixes"):
        runner.prepare_ontology_config(config, adapters)
    assert not config.exists()


def test_missing_local_database_rejected_before_config_write(tmp_path, adapters):
    adapters["PO"].unlink()
    config = tmp_path / "oak.yaml"
    with pytest.raises(ValueError, match="prerequisite is missing"):
        runner.prepare_ontology_config(config, adapters)
    assert not config.exists()


def test_existing_config_cannot_be_replaced(tmp_path, adapters):
    config = tmp_path / "oak.yaml"
    config.write_text("retained\n")
    with pytest.raises(ValueError, match="already exists"):
        runner.prepare_ontology_config(config, adapters)
    assert config.read_text() == "retained\n"


def test_ontology_byte_mutation_changes_bound_manifest(adapters):
    before = runner.ontology_manifest(adapters)
    adapters["PO"].write_bytes(b"changed ontology")
    after = runner.ontology_manifest(adapters)
    assert after != before
    assert after["PO"]["sha256"] != before["PO"]["sha256"]
