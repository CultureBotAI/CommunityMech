import sys
from pathlib import Path

import pytest
import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "scripts"))
import scout_communities as scout  # noqa: E402


def _hit(**overrides):
    hit = {
        "pmid": "12345678",
        "doi": "10.1000/fallback",
        "title": "A sourced synthetic community",
        "abstract": "A defined two-member community was assembled and tested.",
        "year": "2026",
        "journal": "Example Journal",
    }
    hit.update(overrides)
    return hit


def test_stub_requires_a_publication_reference(tmp_path: Path):
    with pytest.raises(ValueError, match="without a PMID or DOI"):
        scout.emit_stub(_hit(pmid="", doi=""), tmp_path)


def test_stub_records_its_primary_source(tmp_path: Path):
    path = scout.emit_stub(_hit(), tmp_path)
    doc = yaml.safe_load(path.read_text())

    assert doc["id"] == "CommunityMech:XXXXXX"
    assert doc["_scout"]["source_reference"] == "PMID:12345678"


def test_stub_queue_entry_is_batch_compatible(tmp_path: Path):
    path = scout.emit_stub(_hit(), tmp_path)
    entry = scout.stub_queue_entry(_hit(), path)

    assert entry["file_path"] == str(path.resolve())
    assert entry["reference"] == "PMID:12345678"
    assert entry["title"] == "A sourced synthetic community"
