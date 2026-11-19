"""Guard regression tests for the 000087 source-scoped correction (2026-11-15)."""

import importlib.util
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "phase2_lbnl_guard", ROOT / "scripts/adhoc/curate_phase2_lbnl_canary_20261115.py"
)
guard = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(guard)


def test_duplicate_canonical_keys_are_rejected():
    with pytest.raises(ValueError, match="duplicate"):
        guard.load_document("id: first\nid: second\n")


def test_existing_legacy_alias_is_preserved_without_unsafe_tags():
    assert guard.load_document("one: &sample\n  text: source\ntwo: *sample\n") == {
        "one": {"text": "source"},
        "two": {"text": "source"},
    }
    with pytest.raises(guard.yaml.constructor.ConstructorError):
        guard.load_document("thing: !!python/object:os.system {}")


def test_missing_section_anchor_refuses_insertion():
    with pytest.raises(ValueError, match="expected one original"):
        guard.replace_section("id: a\n", "taxonomy", [])


def test_section_replacement_preserves_surrounding_history_text():
    original = (
        "id: a\ntaxonomy:\n- old: true\ncuration_history:\n- changes: 'preserve exact spaces'\n"
    )
    result = guard.replace_section(original, "taxonomy", [{"new": "value"}])
    assert result.startswith("id: a\ntaxonomy:\n- new: value\n")
    assert result.endswith("curation_history:\n- changes: 'preserve exact spaces'\n")


def test_wrong_record_bytes_refuse_before_output_or_source_access(tmp_path, monkeypatch):
    monkeypatch.setattr(guard, "ROOT", tmp_path)
    monkeypatch.setattr(guard, "TARGET", "record.yaml")
    (tmp_path / "record.yaml").write_text("id: wrong-record\n")
    output = tmp_path / ".temp" / "proposed"
    monkeypatch.setattr("sys.argv", ["curate", "--output", str(output), "--apply"])
    with pytest.raises(ValueError, match="record changed"):
        guard.main()
    assert not output.exists()
    assert (tmp_path / "record.yaml").read_text() == "id: wrong-record\n"


def test_existing_receipt_directory_refuses_before_any_write(tmp_path, monkeypatch):
    monkeypatch.setattr(guard, "ROOT", tmp_path)
    output = tmp_path / ".temp" / "retained"
    output.mkdir(parents=True)
    marker = output / "receipt.json"
    marker.write_text("retained\n")
    monkeypatch.setattr("sys.argv", ["curate", "--output", str(output), "--apply"])
    with pytest.raises(ValueError, match="new repository"):
        guard.main()
    assert marker.read_text() == "retained\n"
