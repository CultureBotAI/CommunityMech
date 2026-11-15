"""The imported staging implementation is an immutable input (#2851, 2026-11-15)."""

import importlib.util
import json
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parents[1]
HELPERS = REPO / "scripts/adhoc"


def test_imported_helper_mutation_is_refused_then_restores(tmp_path, monkeypatch):
    """Positive, changed imported source, restored positive through one harness."""
    monkeypatch.syspath_prepend(str(HELPERS))
    spec = importlib.util.spec_from_file_location(
        "gtdb_stage_control", HELPERS / "stage_code006_gtdb_status_20261115.py"
    )
    stage = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(stage)
    root = tmp_path / "repo"
    state = root / ".temp/gtdb-code006-20261115"
    state.mkdir(parents=True)
    helper_dir = root / "scripts/adhoc"
    helper_dir.mkdir(parents=True)
    stager_path = helper_dir / "stage_code006_gtdb_status_20261115.py"
    stager_path.write_text("# test stager snapshot\n")
    imported = helper_dir / "inspect_code006_gtdb_route_20261115.py"
    imported.write_text("# original imported implementation\n")
    original_import = imported.read_bytes()
    target = root / "kb/communities/Acidic_Nitrification_Minimal_Consortium.yaml"
    target.parent.mkdir(parents=True)
    target.write_text(
        yaml.safe_dump(
            {
                "taxonomy": [{"taxon_term": {"gtdb_grounding_status": "UNRESOLVED"}}],
                "curation_history": [],
            }
        )
    )
    review = root / "review.yaml"
    review.write_text("historical: unchanged\n")
    table = root / "kg/data/raw/NCBI2GTDB.tsv.gz"
    table.parent.mkdir(parents=True)
    table.write_bytes(b"test source")
    db = root / "oaklib/ncbitaxon.db"
    db.parent.mkdir()
    db.write_bytes(b"test database")
    native = root / "scripts/gtdb_ground.py"
    # A deterministic writer double isolates the provenance boundary. Actual
    # maintained native execution is separately retained in candidate receipts.
    native.write_text("""import yaml
from pathlib import Path
def main(argv):
    candidate = Path(argv[1])
    doc = yaml.safe_load(candidate.read_bytes())
    doc["taxonomy"][0]["taxon_term"]["gtdb_grounding_status"] = "NOT_ATTEMPTED"
    doc["curation_history"].append({"action": "GTDB_SET_STATUS"})
    candidate.write_text(yaml.safe_dump(doc))
    marker = candidate.parent.parent / "mutate-import"
    if marker.exists():
        helper = candidate.parents[3] / "scripts/adhoc/inspect_code006_gtdb_route_20261115.py"
        helper.write_text("# changed during native operation\\n")
        assert helper.read_text() == "# changed during native operation\\n"
    print("native stage control completed")
    return 0
""")
    for key, value in {
        "ROOT": root,
        "STATE": state,
        "RECORD": target,
        "REVIEW": review,
        "TABLE": table,
        "TABLE_SHA": stage.sha(table),
        "DATABASE": db,
        "__file__": str(stager_path),
    }.items():
        monkeypatch.setattr(stage, key, value)
    monkeypatch.setattr(stage, "git", lambda *_args: stage.PIN)
    from communitymech import ontology_adapters

    monkeypatch.setattr(ontology_adapters, "_local_build", lambda *_args: object())
    monkeypatch.setattr(sys, "argv", ["stage", "--attempt", "001"])
    stage.main()
    assert json.loads((state / "status-candidate-001/receipt.json").read_bytes())["exit_code"] == 0
    (state / "mutate-import").touch()
    monkeypatch.setattr(sys, "argv", ["stage", "--attempt", "002"])
    with pytest.raises(ValueError, match="inputs changed"):
        stage.main()
    assert imported.read_bytes() != original_import, "mutation must actually occur"
    assert not (state / "status-candidate-002/receipt.json").exists()
    imported.write_bytes(original_import)
    (state / "mutate-import").unlink()
    monkeypatch.setattr(sys, "argv", ["stage", "--attempt", "003"])
    stage.main()
    assert (state / "status-candidate-003/receipt.json").stat().st_size > 0
