"""Actual fixed/shared successors preserve the immutable batch147 sample (#2861)."""

import hashlib
from pathlib import Path

import pytest
import test_causal_review_batch147 as caller

ROOT = Path(__file__).resolve().parents[1]


@pytest.mark.parametrize(
    "identity",
    [
        "CommunityMech:000552",
        "CommunityMech:000553",
        "CommunityMech:000554",
        "CommunityMech:000555",
    ],
)
def test_actual_joint_records_dispatch_current_and_historical_proofs(identity):
    row = caller.EXPECTED_BATCH147_RECORDS[identity]
    path, before = row["path"], row["record_sha256"]
    current = (ROOT / path).read_bytes()
    after = hashlib.sha256(current).hexdigest()
    assert after != before  # each actual corrected record must be present
    assert caller.current_record_sha256(ROOT, path, before) == after
    old = caller.historical_bytes(ROOT, path)
    assert old != current and hashlib.sha256(old).hexdigest() == before
    with pytest.raises(AssertionError):
        caller.current_record_sha256(
            ROOT, path, before, current=current + b"\n# forged successor\n"
        )
    assert caller.current_record_sha256(ROOT, path, before) == after


def test_unassigned_record_still_requires_exact_predecessor(tmp_path):
    path = "data/isolates/unassigned.yaml"
    target = tmp_path / path
    target.parent.mkdir(parents=True)
    original = b"id: immutable\n"
    target.write_bytes(original)
    expected = hashlib.sha256(original).hexdigest()
    assert caller.current_record_sha256(tmp_path, path, expected) == expected
    target.write_bytes(original + b"unreviewed: changed\n")
    with pytest.raises(AssertionError, match="no successor allowance"):
        caller.current_record_sha256(tmp_path, path, expected)
    target.write_bytes(original)
    assert caller.current_record_sha256(tmp_path, path, expected) == expected
