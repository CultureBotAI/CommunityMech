"""Reject an unlisted successor beside the actual two-occurrence 000388 proof.

#2848, 2026-11-15. Fixtures copy public evidence, pin the production registry,
and restore each mutation. No private inputs, native reruns or source writes.
"""

from types import SimpleNamespace

import pytest
import scoped_gtdb_successor as successor
import test_scoped_gtdb_actual_successor as controls
from gtdb_species_batch_successors_20261115 import ALLOWANCES

TARGET = "kb/communities/Rhizorhabdus_Cupriavidus_BDE47_Degradation_SynCom.yaml"


@pytest.fixture
def actual388(tmp_path, monkeypatch):
    pin = ALLOWANCES[TARGET]
    assert controls.CASES["388"] == (pin["manifest"]["path"], pin["manifest"]["sha256"], True)
    assert pin["baseline_revision"] == controls.BASE
    result = controls.actual.__wrapped__(tmp_path, monkeypatch, SimpleNamespace(param="388"))
    assert result[1]["target"] == TARGET
    assert result[2] == {TARGET: pin}
    return result


def test_unlisted_changed_record_cannot_reuse_species_proof(actual388):
    root, proof, _allowed, _retained, _historical_llm = actual388
    unrelated = "kb/communities/Unlisted_species_record.yaml"
    (root / unrelated).write_bytes((root / proof["target"]).read_bytes())
    with pytest.raises(AssertionError, match="unknown changed record"):
        successor.admit(root, unrelated, proof["before_sha256"], ALLOWANCES)
    assert controls.check(actual388).changed
