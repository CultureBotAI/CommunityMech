"""Exercise actual maintained Wetland471 admission and caller guards, 2026-11-15.

Public evidence and actual Git originals drive the canary. Mutations affect
in-memory current bytes/documents only; persisted proofs remain unchanged.
"""

import copy
import json
from pathlib import Path

import pytest
import test_causal_review_batch133 as batch
import wetland_gtdb_successors as registry
import yaml

ROOT = Path(__file__).resolve().parents[1]


def admitted(**kwargs):
    return registry.admit_wetland_successor(ROOT, registry.TARGET, registry.BEFORE, **kwargs)


def test_actual_production_chain_uses_maintained_identity_and_original_history():
    allowed = registry.ALLOWANCES[registry.TARGET]
    proof = json.loads((ROOT / allowed["manifest"]["path"]).read_bytes())
    assert proof["intermediate_revision"] == registry.MAINTAINED_INTERMEDIATE
    assert proof["mapping_allowance"]["baseline_revision"] == registry.MAINTAINED_INTERMEDIATE
    intermediate = registry.guard.notes.historical_bytes(
        ROOT, registry.MAINTAINED_INTERMEDIATE, registry.TARGET
    )
    assert registry.guard.mapping.digest(intermediate) == registry.guard.INTERMEDIATE
    result = admitted()
    assert result.changed and result.current_sha256 == proof["after_sha256"]
    assert registry.guard.mapping.digest(result.historical_bytes) == registry.BEFORE
    assert result.historical_bytes != intermediate


def test_production_registry_refuses_changed_identity_and_unknown_target_then_restores():
    before = admitted()
    document = yaml.safe_load((ROOT / registry.TARGET).read_bytes())
    original_description = document["description"]
    document["description"] += " Unsupported additional identity claim."
    assert document["description"] != original_description
    with pytest.raises(AssertionError, match="exact original identity mapping chain"):
        admitted(current=yaml.safe_dump(document, sort_keys=False).encode())
    with pytest.raises(AssertionError, match="unknown identity-mapping"):
        registry.admit_wetland_successor(
            ROOT, "kb/communities/Unreviewed.yaml", registry.BEFORE, current=b"changed"
        )
    assert admitted() == before


@pytest.mark.parametrize("field", ["description", "curation_history", "ecological_interactions"])
def test_batch133_preserves_loaded_current_document_mutations(monkeypatch, field):
    ledger, rows, docs = batch.records()
    selected = next(i for i, row in enumerate(rows) if row["path"] == registry.TARGET)
    original = copy.deepcopy(docs[selected])
    monkeypatch.setattr(batch, "records", lambda: (ledger, rows, docs))
    check = batch.test_batch133_covers_all_fifteen_stage1_records_with_verified_hashes_and_history
    check()
    if field == "description":
        docs[selected][field] += " Fabricated current identity."
    elif field == "curation_history":
        docs[selected][field][-1]["changes"] += " Fabricated current event."
    else:
        docs[selected][field][0]["description"] += " Fabricated current mechanism."
    assert docs[selected] != original
    with pytest.raises(AssertionError):
        check()
    docs[selected] = original
    check()
