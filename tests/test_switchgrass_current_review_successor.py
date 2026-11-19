"""Reuse actual lineage refusals for the new full current Switchgrass review.

#1996/#2816, 2026-11-16. Only public bytes enter this isolated fixture. The
strict core and original historical canary remain unchanged apart from the
numbered production manifest path.
"""

from copy import deepcopy
from pathlib import Path

import phase2_review_successor as successor
import pytest
import yaml
from test_phase2_review_successor import (
    test_broken_successor_evidence_cannot_be_promoted,  # noqa: F401
)

ROOT = Path(__file__).resolve().parents[1]
TARGET = "kb/communities/LBNL_Switchgrass_Soil_SynCom16.yaml"
AFTER = "bcc2759c9da7c4059330726a1b154df600ec394d1106be2dcc1f4d247eed5eb9"


@pytest.fixture
def lineage(tmp_path, monkeypatch):
    manifest = yaml.safe_load((ROOT / successor.MANIFEST).read_bytes())
    row = next(item for item in manifest["records"] if item["path"] == TARGET)
    assert row["after_sha256"] == AFTER
    assert row["scientific_review"]["sha256"] == (
        "83d4aa59145ddd04383bb61c29f19dc73c778a6d54967bedbb3db7b97ebfba0d"
    )
    before = successor.historical_bytes(ROOT, TARGET)
    for name in [
        TARGET,
        row["scientific_review"]["path"],
        row["review_markdown"]["path"],
        *[item["path"] for item in row["curation_receipts"]],
        *[item["path"] for item in row["history_sidecars"]],
    ]:
        destination = tmp_path / name
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_bytes((ROOT / name).read_bytes())
    manifest = deepcopy(manifest)
    manifest["records"] = [deepcopy(row)]
    monkeypatch.setattr(successor, "TARGETS", {TARGET: "CommunityMech:000087"})
    monkeypatch.setattr(successor, "historical_bytes", lambda root, path: before)
    return tmp_path, manifest


def test_current_full_review_and_four_actual_transitions_admit(lineage):
    root, manifest = lineage
    row = manifest["records"][0]
    assert len(row["curation_receipts"]) == 4
    assert len(row["history_sidecars"]) == 5
    assert (
        successor.current_record_sha256(root, TARGET, row["before_sha256"], manifest=manifest)
        == AFTER
    )


def test_other_four_scientific_rows_remain_exact():
    old = yaml.safe_load(
        (
            ROOT / "reports/phase2-completion-20261115/scientific-successor-provenance-002.yaml"
        ).read_bytes()
    )
    new = yaml.safe_load((ROOT / successor.MANIFEST).read_bytes())
    assert [r for r in old["records"] if r["path"] != TARGET] == [
        r for r in new["records"] if r["path"] != TARGET
    ]
    for row in new["records"]:
        assert (
            successor.current_record_sha256(ROOT, row["path"], row["before_sha256"])
            == row["after_sha256"]
        )
