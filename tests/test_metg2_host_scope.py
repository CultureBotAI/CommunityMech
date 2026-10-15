"""Keep the sugarcane host separate from microbial transcription (#1847)."""

import hashlib
import json
import subprocess
import xml.etree.ElementTree as ET
from copy import deepcopy
from pathlib import Path

import pytest
import yaml

from communitymech.network.auditor import NetworkIntegrityAuditor

ROOT = Path(__file__).resolve().parents[1]
RECORD = "kb/communities/SynCom_MetG2_Rhizobacteria_Sugarcane_Stress_Resilience.yaml"
BASE = "737a95eed17f606b30dd99fbec7dc82c19ad3f40"
LEDGER = "reports/causal_graph_review/decisions/20261015-metg2-host.yaml"


def current():
    return yaml.safe_load((ROOT / RECORD).read_text())


def assert_host_scope(doc):
    host = doc["taxonomy"][0]["taxon_term"]
    phylum = doc["taxonomy"][1]["taxon_term"]
    colonization, functions, response = doc["ecological_interactions"]
    assert host["term"] == {"id": "NCBITaxon:4546", "label": "Saccharum"}
    assert host["preferred_term"] == "sugarcane (Saccharum; species unresolved)"
    assert "parent-rank anchor" in host["notes"]
    assert "not a genus-wide" in host["notes"]
    assert "cultivar" in host["notes"] and "unverified" in host["notes"]
    assert host["gtdb_grounding_status"] == "NO_GTDB_EQUIVALENT"
    assert response.get("participating_taxa") == [{k: host[k] for k in ("preferred_term", "term")}]
    assert colonization.get("participating_taxa") == [
        {k: phylum[k] for k in ("preferred_term", "term")}
    ]
    assert "species and cultivar remain unverified" in response["description"]
    assert "not by themselves" in response["description"]
    assert functions["downstream"][0]["description"].startswith("HYPOTHESIZED/PARTIAL:")
    assert "not assigned exclusively" in functions["description"]
    assert doc["discussions"][0]["status"] == "OPEN"
    assert "Chiliseed2" in doc["discussions"][0]["rationale"]
    assert "Chileseed2" in doc["discussions"][0]["rationale"]


def test_host_grounding_and_expression_participants():
    assert_host_scope(current())


@pytest.mark.parametrize("mutation", ["species", "all_host", "bacterial_host", "closed"])
def test_control_mutation_restoration(mutation):
    control = current()
    assert_host_scope(control)
    changed = deepcopy(control)
    if mutation == "species":
        changed["taxonomy"][0]["taxon_term"]["term"] = {
            "id": "NCBITaxon:4547",
            "label": "Saccharum officinarum",
        }
    elif mutation == "all_host":
        del changed["ecological_interactions"][2]["participating_taxa"]
    elif mutation == "bacterial_host":
        changed["ecological_interactions"][2]["participating_taxa"] = deepcopy(
            changed["ecological_interactions"][0]["participating_taxa"]
        )
    else:
        changed["discussions"][0]["status"] = "RESOLVED"
    assert changed != control
    with pytest.raises(AssertionError):
        assert_host_scope(changed)
    assert_host_scope(control)


@pytest.mark.parametrize("index,disconnected", [(0, "NCBITaxon:4546"), (2, "NCBITaxon:1224")])
def test_native_auditor_does_not_credit_the_other_kingdom(tmp_path, index, disconnected):
    doc = current()
    doc["ecological_interactions"] = [doc["ecological_interactions"][index]]
    original = deepcopy(doc)
    path = tmp_path / "metg2.yaml"
    path.write_text(yaml.safe_dump(doc))
    issues = NetworkIntegrityAuditor().audit_community(path)
    assert {i["taxon_id"] for i in issues if i["type"] == "DISCONNECTED"} == {disconnected}
    # Prove this behavioral check distinguishes absent (all-member) participants.
    del doc["ecological_interactions"][0]["participating_taxa"]
    path.write_text(yaml.safe_dump(doc))
    assert not any(
        i["type"] == "DISCONNECTED" for i in NetworkIntegrityAuditor().audit_community(path)
    )
    path.write_text(yaml.safe_dump(original))
    restored = NetworkIntegrityAuditor().audit_community(path)
    assert {i["taxon_id"] for i in restored if i["type"] == "DISCONNECTED"} == {disconnected}


def test_genus_source_and_unchanged_abstract_are_hash_bound():
    source = ROOT / "reports/causal_graph_review/sources/20261015-metg2-host"
    manifest = json.loads((source / "manifest.json").read_text())
    raw = (source / "ncbi-taxonomy.xml").read_bytes()
    assert (
        hashlib.sha256(raw).hexdigest()
        == manifest["ncbi_sha256"]
        == ("4d93c64556be377014f2deb493de13b74a43fd4a087b7479f106d1bb20bda2aa")
    )
    root = ET.fromstring(raw)  # noqa: S314 - SHA-256-pinned repository fixture
    taxa = {t.findtext("TaxId"): t for t in root.findall("Taxon")}
    assert taxa["4546"].findtext("ScientificName") == "Saccharum"
    assert taxa["4546"].findtext("Rank") == "genus"
    assert taxa["4547"].findtext("ScientificName") == "Saccharum officinarum"
    assert taxa["4547"].findtext("Rank") == "species"
    cache = (ROOT / manifest["article"]["cache"]).read_bytes()
    assert hashlib.sha256(cache).hexdigest() == manifest["article"]["sha256"]
    assert "Sugarcane plants also exhibited dynamic responses" in cache.decode()


def test_successor_preserves_topology_evidence_and_unresolved_membership():
    old_bytes = subprocess.check_output(["git", "show", f"{BASE}:{RECORD}"], cwd=ROOT)
    old, doc = yaml.safe_load(old_bytes), current()
    ledger = yaml.safe_load((ROOT / LEDGER).read_text())
    row = ledger["records"][0]
    assert row["id"] == doc["id"] == "CommunityMech:000302"
    assert row["original_sha256"] == hashlib.sha256(old_bytes).hexdigest()
    assert row["record_sha256"] == hashlib.sha256((ROOT / RECORD).read_bytes()).hexdigest()
    prior = yaml.safe_load((ROOT / row["supersedes_review"]["review_file"]).read_text())
    prior_row = next(r for r in prior["records"] if r["id"] == doc["id"])
    assert row["supersedes_review"]["record_sha256"] == prior_row["record_sha256"]
    assert row["original_sha256"] == prior_row["record_sha256"]
    assert {k for k in doc if doc[k] != old[k]} == set(row["allowed_changed_fields"])
    for before, after in zip(
        old["ecological_interactions"], doc["ecological_interactions"], strict=True
    ):
        assert before["name"] == after["name"]
        assert before["evidence"] == after["evidence"]
        assert before.get("downstream") == after.get("downstream")
    assert doc["ecological_interactions"][1] == old["ecological_interactions"][1]
    assert doc["taxonomy"][1:] == old["taxonomy"][1:]
    assert doc["curation_history"][:-1] == old["curation_history"]
    assert row["status"] == "needs_research" and row["issues"] == [1847]
    assert doc["curation_history"][-1]["llm_assisted"] is True
    assert len(row["history_files"]) == 1
    assert not ledger["independent_approval"]
    assert ledger["edison"]["provider_submissions"] == 0
