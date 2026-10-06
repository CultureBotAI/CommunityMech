"""Keep cellulose-conversion outcomes distinct from untested mediation."""

import hashlib
from collections import Counter
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "reports/causal_graph_review/decisions/20261005-three-records-batch19.yaml"


def load(stem):
    return yaml.safe_load((ROOT / "kb/communities" / (stem + ".yaml")).read_text())


def test_mfc_current_does_not_require_demonstrated_spatial_separation():
    doc = load("Clostridium_Cellulolyticum_Geobacter_Cellulose_MFC_Coculture")
    supply, current, spatial = doc["ecological_interactions"]
    assert supply["interaction_type"] == "CROSS_FEEDING"
    assert "does not demonstrate obligate growth dependence" in supply["description"]
    assert "especially ethanol" in supply["description"]
    assert supply["evidence"][1]["supports"] == "PARTIAL"
    assert all("residual metabolite" in m["notes"] for m in supply["metabolites"][1:])
    assert supply["downstream"][0]["target"] == current["name"]
    assert "42%" in current["description"] and "64%" in current["description"]
    assert "interaction_type" not in current
    assert "interaction_type" not in spatial and "downstream" not in spatial
    assert spatial["name"] == "Observed Substrate-Dependent Spatial Distribution"
    assert "With soluble CMC, both organisms" in spatial["description"]


def test_abe_cosubstrate_supply_is_not_upstream_saccharification_or_competition():
    doc = load("Clostridium_Cellulovorans_Beijerinckii_AECC_ABE_Coculture")
    sugar, acid, dynamics = doc["ecological_interactions"]
    assert all("downstream" not in n for n in (sugar, acid, dynamics))
    assert sugar["interaction_type"] == acid["interaction_type"] == "CROSS_FEEDING"
    assert acid["description"].startswith("PARTIAL")
    assert "without external butyric-acid addition" in acid["description"]
    assert "isolate butyrate necessity" in acid["description"]
    assert all(e["supports"] == "PARTIAL" for e in acid["evidence"])
    assert "interaction_type" not in dynamics
    assert dynamics["description"].startswith("PARTIAL")
    assert "RNA extraction and cDNA" in dynamics["description"]
    assert "not direct cell counts" in dynamics["description"]
    assert dynamics["evidence"][1]["evidence_source"] == "IN_VITRO"
    assert "molecular mechanism unresolved" in dynamics["description"]
    assert doc["taxonomy"][1]["taxon_term"]["gtdb_grounding_status"] == "WITHHELD"


def test_methane_preserves_formate_controls_and_qualifies_feedback():
    doc = load("Clostridium_Cellulovorans_Methanosarcina_Cellulose_Methane_Coculture")
    supply, methane, feedback = doc["ecological_interactions"]
    assert supply["downstream"][0]["target"] == methane["name"]
    assert methane["downstream"][0]["target"] == feedback["name"]
    assert methane["source_taxon"]["term"]["id"] == "NCBITaxon:269797"
    assert methane["target_taxon"]["term"]["id"] == "NCBITaxon:573061"
    assert "not donation" in methane["description"]
    assert "did not grow with formate alone after nine months" in methane["description"]
    assert "1.5 mM of 10 mM" in methane["description"]
    assert methane["downstream"][0]["description"].startswith("HYPOTHESIZED")
    assert (
        "changed C. cellulovorans fermentation pattern" in methane["downstream"][0]["description"]
    )
    assert "13.8%" in feedback["description"]
    assert "cell growth was not significantly improved" in feedback["description"]
    assert "reported growth yields were similar" in feedback["description"]
    assert "interaction_type" not in feedback
    assert {t["taxon_term"]["term"]["id"] for t in doc["taxonomy"]} == {
        "NCBITaxon:573061",
        "NCBITaxon:269797",
    }


def test_batch19_hashes_scope_and_complete_graph_accounting():
    ledger = yaml.safe_load(LEDGER.read_text())
    assert ledger["independent_approval"] is False
    assert ledger["issues"] == [1324, 1325, 1326]
    assert ledger["open_nongraph_followups"] == [1327]
    assert len(ledger["records"]) == 3
    totals = Counter()
    for row in ledger["records"]:
        raw = (ROOT / row["path"]).read_bytes()
        assert hashlib.sha256(raw).hexdigest() == row["record_sha256"]
        doc = yaml.safe_load(raw)
        names = {n["name"] for n in doc["ecological_interactions"]}
        assert len(names) == 3
        assert Counter(d["node"] for d in row["node_decisions"]) == Counter(names)
        renames = row["renamed_nodes"]
        before = {
            (renames.get(e["source"], e["source"]), renames.get(e["target"], e["target"]))
            for e in row["edges_before"]
        }
        after = {(e["source"], e["target"]) for e in row["edges_after"]}
        removed = {
            (renames.get(e["source"], e["source"]), renames.get(e["target"], e["target"]))
            for e in row["removed_edge_decisions"]
        }
        assert before == after | removed and not after & removed
        assert after == {(e["source"], e["target"]) for e in row["retained_edge_decisions"]}
        assert after == {
            (n["name"], e["target"])
            for n in doc["ecological_interactions"]
            for e in n.get("downstream", [])
        }
        assert set(row["allowed_changed_fields"]) == {
            "ecological_interactions",
            "discussions",
            "curation_history",
        }
        assert row["curation_events_added"] == 1 and len(row["history_files"]) == 1
        assert all((ROOT / p).is_file() for p in row["history_files"])
        assert all(
            a.split("#", 1)[1] in names
            for d in doc["discussions"]
            for a in d.get("attaches_to", [])
            if a.startswith("ecological_interactions#")
        )
        totals.update(
            before=len(before), after=len(after), removed=len(removed), renames=len(renames)
        )
    assert totals == {"before": 6, "after": 3, "removed": 3, "renames": 4}
    assert len(ledger["reference_cache_original_hashes"]) == 5
    for path, expected in ledger["reference_cache_original_hashes"].items():
        assert hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == expected
