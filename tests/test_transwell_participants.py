"""Keep the two Transwell demonstrations and their strains distinct (#1467)."""

import hashlib
import json
import subprocess
from collections import Counter
from copy import deepcopy
from pathlib import Path

import pytest
import yaml

from communitymech.network.auditor import NetworkIntegrityAuditor

ROOT = Path(__file__).resolve().parents[1]
RECORD = ROOT / "kb/communities/GLBRC_Exometabolite_Transwell_SynCom.yaml"


def current():
    return yaml.safe_load(RECORD.read_text())


def assert_scope(doc):
    members = {t["strain_designation"]["strain_name"]: t for t in doc["taxonomy"]}
    assert set(members) == {"Cv017", "Cv026", "SC11,378 (ATCC 31532)", "E264", "DC3000"}
    assert len(doc["taxonomy"]) == 5
    for member in members.values():
        term = member["taxon_term"]
        assert term["gtdb_grounding_status"] == "UNRESOLVED"
        assert "lookup did not complete" in term["notes"]
        assert "not evidence of no GTDB counterpart" in term["notes"]
        assert "gtdb_classification" not in term
    for strain in ["Cv017", "Cv026", "SC11,378 (ATCC 31532)"]:
        assert members[strain]["taxon_term"]["term"] == {
            "id": "NCBITaxon:251747",
            "label": "Chromobacterium subtsugae",
        }
    assert members["E264"]["taxon_term"]["term"]["id"] == "NCBITaxon:271848"
    assert members["DC3000"]["taxon_term"]["term"]["id"] == "NCBITaxon:223283"
    reporter, series = doc["ecological_interactions"]
    assert reporter["scope"] == "PAIRWISE"
    for role, strain in [("source_taxon", "Cv017"), ("target_taxon", "Cv026")]:
        assert reporter[role]["preferred_term"] == members[strain]["taxon_term"]["preferred_term"]
        assert reporter[role]["term"] == members[strain]["taxon_term"]["term"]
    assert "participating_taxa" not in reporter
    assert series["scope"] == "COMMUNITY_LEVEL"
    assert {t["preferred_term"] for t in series["participating_taxa"]} == {
        members[s]["taxon_term"]["preferred_term"]
        for s in ["SC11,378 (ATCC 31532)", "E264", "DC3000"]
    }
    assert all("downstream" not in n for n in [reporter, series])
    assert "SC11,368" in members["SC11,378 (ATCC 31532)"]["strain_designation"]["notes"]
    assert doc["discussions"][-1]["status"] == "OPEN"
    assert "not resolved" in doc["discussions"][-1]["rationale"]
    assert "977 features are not 977 identified metabolites" in series["description"]
    assert "does not selectively establish the cause" in series["description"]


def test_exact_assay_scope():
    assert_scope(current())


@pytest.mark.parametrize("mutation", ["reverse", "all_members", "reporter_in_series", "species"])
def test_control_mutation_restoration(mutation):
    control = current()
    assert_scope(control)
    changed = deepcopy(control)
    reporter, series = changed["ecological_interactions"]
    if mutation == "reverse":
        reporter["source_taxon"], reporter["target_taxon"] = (
            reporter["target_taxon"],
            reporter["source_taxon"],
        )
    elif mutation == "all_members":
        del series["participating_taxa"]
    elif mutation == "reporter_in_series":
        series["participating_taxa"][0] = deepcopy(reporter["source_taxon"])
    else:
        changed["taxonomy"][0]["taxon_term"]["term"] = {
            "id": "NCBITaxon:536",
            "label": "Chromobacterium violaceum",
        }
    assert changed != control
    with pytest.raises((AssertionError, KeyError)):
        assert_scope(changed)
    assert_scope(control)


def test_native_auditor_distinguishes_strains_sharing_a_taxon_id(tmp_path):
    doc = current()
    doc["ecological_interactions"] = [doc["ecological_interactions"][1]]
    path = tmp_path / "transwell.yaml"

    def disconnected(candidate):
        path.write_text(yaml.safe_dump(candidate))
        return [
            i
            for i in NetworkIntegrityAuditor().audit_community(path)
            if i["type"] == "DISCONNECTED"
        ]

    control = disconnected(doc)
    assert len(control) == 2
    assert {i["taxon_id"] for i in control} == {"NCBITaxon:251747"}
    changed = deepcopy(doc)
    del changed["ecological_interactions"][0]["participating_taxa"]
    assert changed != doc
    assert disconnected(changed) == []
    assert disconnected(doc) == control


def test_source_and_successor_hashes_are_bound():
    ledger = yaml.safe_load(
        (ROOT / "reports/causal_graph_review/decisions/20261015-transwell-ci.yaml").read_text()
    )
    row = ledger["records"][0]
    assert row["id"] == current()["id"] == "CommunityMech:000091"
    assert row["record_sha256"] == hashlib.sha256(RECORD.read_bytes()).hexdigest()
    prior = yaml.safe_load((ROOT / row["supersedes_review"]["review_file"]).read_text())
    previous = next(r for r in prior["records"] if r["id"] == row["id"])
    assert previous["record_sha256"] == row["original_sha256"]
    assert row["status"] == "needs_research" and row["issues"] == [1467, 2014]
    assert row["edges_before"] == row["edges_after"] == []
    assert not ledger["independent_approval"]
    assert ledger["edison"]["provider_submissions"] == 0
    manifest = json.loads((ROOT / ledger["source_manifest"]).read_text())
    for source in manifest:
        assert hashlib.sha256((ROOT / source["path"]).read_bytes()).hexdigest() == source["sha256"]


def test_only_transwell_accounts_for_gtdb_distribution_change(monkeypatch):
    def census():
        counts = Counter()
        for directory in ("kb/communities", "data/isolates"):
            for path in sorted((ROOT / directory).glob("*.yaml")):
                for entry in yaml.safe_load(path.read_text()).get("taxonomy") or []:
                    counts[(entry.get("taxon_term") or {}).get("gtdb_grounding_status")] += 1
        return counts

    old = subprocess.check_output(
        ["git", "show", f"616a2806e363f01a3727ea57dcf3bcd019999943:{RECORD.relative_to(ROOT)}"],
        cwd=ROOT,
        text=True,
    )
    ledger = yaml.safe_load(
        (ROOT / "reports/causal_graph_review/decisions/20261015-transwell.yaml").read_text()
    )
    assert hashlib.sha256(old.encode()).hexdigest() == ledger["records"][0]["original_sha256"]
    before_members = yaml.safe_load(old)["taxonomy"]
    assert len(before_members) == 1
    assert before_members[0]["taxon_term"]["gtdb_grounding_status"] == "GROUNDED"
    current_counts = census()
    assert current_counts["UNRESOLVED"] == 494
    expected_previous = current_counts.copy()
    expected_previous["UNRESOLVED"] -= 5
    expected_previous["GROUNDED"] += 1
    original_read = Path.read_text

    def predecessor_only(path, *args, **kwargs):
        return old if path == RECORD else original_read(path, *args, **kwargs)

    with monkeypatch.context() as context:
        context.setattr(Path, "read_text", predecessor_only)
        assert RECORD.read_text() == old
        assert census() == expected_previous
    assert RECORD.read_text() != old
    assert census() == current_counts
