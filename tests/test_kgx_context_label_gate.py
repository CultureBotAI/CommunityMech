"""Keep descriptor identity distinct from ontology-label claims (#2844)."""

import csv
import importlib.util
from pathlib import Path

import oaklib
import pytest
import yaml

from communitymech.export import kgx_export

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location(
    "context_label_gate", ROOT / "scripts/validate_id_label_correspondence.py"
)
gate = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gate)


class SoilAdapter:
    def entities(self):
        return iter(["ENVO:00001998"])

    def label(self, identifier):
        return "soil" if identifier == "ENVO:00001998" else None

    def entity_alias_map(self, identifier):
        return {}


@pytest.mark.parametrize(
    "old,new,verdict",
    [
        ("uuid:", "uuidtypo:", "UNKNOWN_PREFIX"),
        ("ENVO:00001998", "CHBEI:00001998", "UNKNOWN_PREFIX"),
        ("\tsoil\t", "\tincorrect ontology label\t", "MISMATCH"),
        ("ENVO:00001998", "ENVO:99999999", "ID_NOT_FOUND"),
    ],
)
def test_native_export_identity_and_ontology_claims(
    tmp_path, monkeypatch, capsys, old, new, verdict
):
    source = tmp_path / "source"
    source.mkdir()
    document = {
        "id": "CommunityMech:999991",
        "name": "Context control",
        "soils": [
            {"preferred_term": "soil in pot", "term": {"id": "ENVO:00001998", "label": "soil"}}
        ],
    }
    (source / "record.yaml").write_text(yaml.safe_dump(document))
    output = tmp_path / "output/kgx"
    kgx_export.export_kgx(source, output)
    nodes = output / "nodes.tsv"
    original = nodes.read_text()
    rows = list(csv.DictReader(original.splitlines(), delimiter="\t"))
    assert len(rows) == 3
    assert [row["name"] for row in rows if row["id"].startswith("uuid:")] == ["soil in pot"]

    config = yaml.safe_load((ROOT / "conf/id_label_targets.yaml").read_text())
    config["targets"] = [target for target in config["targets"] if target["name"] == "kgx_nodes"]
    assert len(config["targets"]) == 1 and config["targets"][0]["required"]
    config_path = tmp_path / "config.yaml"
    config_path.write_text(yaml.safe_dump(config))
    monkeypatch.setattr(gate, "REPO_ROOT", tmp_path)
    monkeypatch.setattr(oaklib, "get_adapter", lambda selector: SoilAdapter())

    assert gate.run(config_path, report_path=None) == 0
    capsys.readouterr()
    assert original.count(old) == 1
    nodes.write_text(original.replace(old, new))
    assert nodes.read_text().count(new) == 1
    assert gate.run(config_path, report_path=None) == 2
    assert verdict in capsys.readouterr().out
    nodes.write_text(original)
    assert nodes.read_text() == original
    assert gate.run(config_path, report_path=None) == 0
