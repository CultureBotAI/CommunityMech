"""Keep CHK0059 isolate identities and measured endpoints distinct from mechanisms."""

import hashlib
from collections import Counter
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "reports/causal_graph_review/decisions/20261005-two-records-batch14.yaml"
KEYSTONE = ROOT / "kb/communities/Chlorella_Keystone_Taxa_Antifungal_SynCom.yaml"


def record():
    return yaml.safe_load(KEYSTONE.read_text())


def test_four_isolates_are_not_confused_with_three_taxonomy_entries():
    doc = record()
    assert "four-isolate" in doc["description"]
    alga, pseudo, ft, brev = doc["taxonomy"][:4]
    assert "TWO distinct" in pseudo["taxon_term"]["notes"]
    assert all(s in pseudo["taxon_term"]["notes"] for s in ("8C3D12", "6C7F4"))
    assert ft["taxon_term"]["term"] == {
        "id": "NCBITaxon:2666085",
        "label": "Pseudoduganella rivuli",
    }
    assert ft["strain_designation"]["strain_name"] == "FT92W"
    assert "Duganella network ASV" in ft["taxon_term"]["notes"]
    assert "stream-water isolate" in ft["taxon_term"]["notes"]
    assert ft["taxon_term"]["gtdb_grounding_status"] == "UNRESOLVED"
    assert "gtdb_classification" not in ft["taxon_term"]
    assert brev["taxon_term"]["term"]["id"] == "NCBITaxon:1696"
    assert brev["strain_designation"]["strain_name"] == "REN4"
    assert (
        "absent from the four-bacterium Treat8 but added in Treat9" in alga["taxon_term"]["notes"]
    )


def test_all_inoculated_ft92w_participants_use_the_correct_species():
    nodes = record()["ecological_interactions"]
    for node in nodes[1:5]:
        ids = {t["term"]["id"] for t in node["participating_taxa"]}
        assert "NCBITaxon:2666085" in ids
        assert "NCBITaxon:75654" not in ids
    for node in (nodes[1], nodes[3], nodes[4]):
        assert "NCBITaxon:3073" in {t["term"]["id"] for t in node["participating_taxa"]}
    assert "NCBITaxon:3073" not in {t["term"]["id"] for t in nodes[2]["participating_taxa"]}


def test_proxy_screens_do_not_become_direct_flux_or_facilitation():
    pgp = record()["ecological_interactions"][2]
    assert "positive FT92W Salkowski/IAA screen" in pgp["description"]
    assert "not measured nitrogen flux" in pgp["description"]
    assert "not chemically resolved IAA" in pgp["description"]
    assert all(k not in pgp for k in ("interaction_type", "biological_processes", "metabolites"))
    assert all(e["supports"] == "PARTIAL" for e in pgp["evidence"])
    assert all(e["evidence_source"] == "IN_VITRO" for e in pgp["evidence"])


def test_fraction_response_is_in_vitro_relative_abundance_not_algal_transfer():
    doc = record()
    restructure, *_, mannitol = doc["ecological_interactions"]
    assert "In-vitro" in restructure["description"]
    assert "Only Pseudomonas" in restructure["description"]
    assert "relative abundance" in mannitol["description"]
    assert "lower relative abundance in live and sterilized CHK0059" in mannitol["description"]
    assert "not absolute Pseudomonas growth" in mannitol["description"]
    assert "HYPOTHESIZED" in mannitol["description"]
    assert mannitol["evidence"][0]["evidence_source"] == "IN_VITRO"
    assert doc["environmental_factors"][0]["evidence"][0]["evidence_source"] == "IN_VITRO"


def test_disease_observations_do_not_create_duplicate_causal_arrows():
    nodes = record()["ecological_interactions"]
    assert len(nodes) == 6
    assert all("downstream" not in n and "interaction_type" not in n for n in nodes)
    assert all("biological_processes" not in n for n in nodes)
    assert "week 5" in nodes[3]["description"]
    assert "single-isolate Treat3 mean was 2.24 g" in nodes[3]["description"]
    assert "Treat8" in nodes[4]["description"] and "Treat9" in nodes[4]["description"]
    assert "Single-isolate FT92W Treat2" in nodes[4]["description"]
    assert "overlapping post-hoc groups" in nodes[4]["description"]


def test_batch14_ledger_covers_all_structure_and_byte_unchanged_whey():
    ledger = yaml.safe_load(LEDGER.read_text())
    assert ledger["independent_approval"] is False
    assert ledger["issues"] == [1305, 1306]
    keystone, whey = ledger["records"]
    assert len(keystone["history_files"]) == 2
    assert len(keystone["removed_edge_decisions"]) == 2
    assert keystone["curation_events_added"] == 2
    assert whey["outcome"] == "no_change"
    assert whey["record_sha256"] == whey["original_sha256"]
    assert whey["history_files"] == []
    for row in ledger["records"]:
        raw = (ROOT / row["path"]).read_bytes()
        assert hashlib.sha256(raw).hexdigest() == row["record_sha256"]
        doc = yaml.safe_load(raw)
        names = {n["name"] for n in doc["ecological_interactions"]}
        assert Counter(d["node"] for d in row["node_decisions"]) == Counter(names)
        assert row["edges_after"] == []
        assert all(
            a.split("#", 1)[1] in names
            for discussion in doc["discussions"]
            for a in discussion["attaches_to"]
            if a.startswith("ecological_interactions#")
        )
    for path, expected in ledger["reference_cache_original_hashes"].items():
        assert hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == expected
