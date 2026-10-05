"""Keep thermophile phenotypes distinct from proposed mechanisms and fitness."""

from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]


def record(stem):
    return yaml.safe_load((ROOT / "kb/communities" / f"{stem}.yaml").read_text())


def test_caldibacillus_preserves_partial_exchange_and_protection():
    doc = record("Caldibacillus_Clostridium_Aerotolerant_Cellulose_Coculture")
    protection, conversion, lactate = doc["ecological_interactions"]
    assert "interaction_type" not in protection
    assert "interaction_type" not in lactate
    assert conversion["interaction_type"] == "CROSS_FEEDING"
    assert conversion["evidence"][1]["supports"] == "PARTIAL"
    assert protection["downstream"][0]["target"] == conversion["name"]
    assert protection["downstream"][0]["description"].startswith("PARTIAL")
    assert "bulk oxygen persisted" in protection["description"]
    assert "5.5 mM at 72 h, below detection at 168 h" in conversion["description"]
    assert "B4-1 enrichment results are distinct" in conversion["description"]
    assert "not resolved coculture flux" in conversion["description"]
    assert "then less at 168 h" in lactate["description"]
    assert not conversion.get("downstream") and not lactate.get("downstream")
    assert protection["target_taxon"]["term"]["label"] == "Acetivibrio thermocellus"


def test_caldicellulosiruptor_preserves_hypothesis_not_yield_mediation():
    doc = record("Caldicellulosiruptor_TwoSpecies_Hydrogen_Coculture")
    stable, supernatant, hydrogen = doc["ecological_interactions"]
    assert all("interaction_type" not in n for n in (stable, supernatant, hydrogen))
    assert not stable.get("downstream") and not hydrogen.get("downstream")
    assert supernatant["downstream"][0]["target"] == stable["name"]
    assert supernatant["downstream"][0]["description"].startswith("HYPOTHESIZED")
    assert "Maximum specific growth rate did not significantly change" in supernatant["description"]
    assert supernatant["evidence"][0]["supports"] == "PARTIAL"
    assert hydrogen["name"] == "Enhanced Glucose-Limited Hydrogen Yield"
    assert "3.7 mol/mol glucose at dilution 0.06/h" in hydrogen["description"]
    assert "not volumetric productivity" in hydrogen["description"]
    assert "secretion-versus-lysis" in supernatant["description"]
    assert supernatant["target_taxon"]["term"]["label"] == "Caldicellulosiruptor acetigenus I77R1B"
    assert "C. kristjanssonii outgrowing C. saccharolyticus" in doc["cultivation_setup"][0]["notes"]


def test_batch9_ledger_covers_each_retained_and_removed_direction():
    ledger = yaml.safe_load(
        (
            ROOT / "reports/causal_graph_review/decisions/20261005-thermophile-pair-batch9.yaml"
        ).read_text()
    )
    rows = ledger["records"]
    assert {r["id"] for r in rows} == {"CommunityMech:000179", "CommunityMech:000185"}
    assert all(r["status"] == "reviewed" for r in rows)
    assert sum(len(r["node_decisions"]) for r in rows) == 6
    assert sum(len(r["removed_edge_decisions"]) for r in rows) == 1
    assert sum(len(r["retained_edge_decisions"]) for r in rows) == 2
    for row in rows:
        assert len(row["edges_before"]) == len(row["edges_after"]) + len(
            row["removed_edge_decisions"]
        )
        assert {(d["source"], d["target"]) for d in row["retained_edge_decisions"]} == {
            (e["source"], e["target"]) for e in row["edges_after"]
        }
