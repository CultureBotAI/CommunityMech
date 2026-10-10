"""Bound coculture products and flocculation to their measured assay scope."""

import hashlib
from collections import Counter
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "reports/causal_graph_review/decisions/20261005-two-records-batch13.yaml"


def record(stem):
    return yaml.safe_load((ROOT / "kb/communities" / f"{stem}.yaml").read_text())


def test_ecoli_mutualism_distinguishes_viability_from_total_biomass():
    growth = record("Chlorella_Ecoli_Mixotrophic_Biofuel_Coculture")["ecological_interactions"][0]
    assert growth["interaction_type"] == "MUTUALISM"
    assert growth["description"].startswith("PARTIAL")
    assert "viable CFU" in growth["description"]
    assert "total dry biomass was not uniformly enhanced" in growth["description"]
    assert "10 g/L" in growth["description"]
    assert "biological_processes" not in growth
    assert growth["evidence"][-1]["supports"] == "PARTIAL"


def test_ecoli_bulk_uptake_is_not_directed_cross_feeding():
    consumption = record("Chlorella_Ecoli_Mixotrophic_Biofuel_Coculture")[
        "ecological_interactions"
    ][1]
    assert "interaction_type" not in consumption
    assert consumption["scope"] == "COMMUNITY_LEVEL"
    assert "source_taxon" not in consumption and "target_taxon" not in consumption
    assert {t["term"]["id"] for t in consumption["participating_taxa"]} == {
        "NCBITaxon:3071",
        "NCBITaxon:562",
    }
    assert "not measured algal-to-bacterial carbon transfer" in consumption["description"]
    assert consumption["downstream"][0]["description"].startswith("HYPOTHESIZED")


def test_ecoli_products_retain_antibiotic_and_bulk_assay_limits():
    growth, consumption, product = record("Chlorella_Ecoli_Mixotrophic_Biofuel_Coculture")[
        "ecological_interactions"
    ]
    assert "interaction_type" not in product
    assert "combined-biomass endpoints" in product["description"]
    assert "kanamycin suppressed starch" in product["description"]
    assert "not wholly attributable" in product["description"]
    assert "biomass and lipid benefits remain supported" in product["description"]
    assert growth["downstream"][0]["description"].startswith("PARTIAL")
    assert all(n["downstream"][0]["target"] == product["name"] for n in (growth, consumption))


def test_rhizobium_removes_unsupported_carbon_supply_and_polymer_specificity():
    doc = record("Chlorella_Rhizobium_Bioflocculation")
    flocculation, harvesting = doc["ecological_interactions"]
    assert all("interaction_type" not in n for n in doc["ecological_interactions"])
    assert flocculation["name"] == "Bioflocculant Production and Cell Aggregation"
    assert "metabolites" not in flocculation
    assert [p["term"]["id"] for p in flocculation["biological_processes"]] == ["GO:0098743"]
    assert flocculation["description"].startswith("PARTIAL")
    assert flocculation["downstream"][0]["target"] == harvesting["name"]
    assert flocculation["downstream"][0]["description"].startswith("PARTIAL")
    assert "45-50%" in harvesting["description"]
    assert "0.2%" in harvesting["description"]
    assert "not over 90%" in harvesting["description"]
    assert "not mutualism" in harvesting["description"]


def test_cache_metadata_describes_actual_access_without_full_text_overclaim():
    ecoli = (ROOT / "references_cache/PMID_24805253.md").read_text()
    emeta = yaml.safe_load(ecoli.split("---", 2)[1])
    assert emeta["content_type"] == "abstract_and_full_text"
    assert "version not specified" in emeta["license"]
    assert "figure images" in emeta["excerpt_scope"]
    rhizobium = (ROOT / "references_cache/doi_10.1111_lam.12403.md").read_text()
    rmeta = yaml.safe_load(rhizobium.split("---", 2)[1])
    assert rmeta["content_type"] == "abstract_and_significance_excerpts"
    assert "not a complete abstract or full article body" in rmeta["excerpt_scope"]
    assert "license" not in rmeta
    assert "harvesting efficiency reached 45\u00b70\u201350\u00b70%" in rhizobium


def test_batch13_ledger_covers_all_retained_and_removed_structure():
    ledger = yaml.safe_load(LEDGER.read_text())
    assert ledger["independent_approval"] is False
    rows = ledger["records"]
    assert len(rows) == 2
    assert sum(len(r["node_decisions"]) for r in rows) == 5
    assert sum(len(r.get("removed_node_decisions", [])) for r in rows) == 1
    assert sum(len(r["retained_edge_decisions"]) for r in rows) == 3
    assert sum(len(r["removed_edge_decisions"]) for r in rows) == 1
    for row in rows:
        raw = (ROOT / row["path"]).read_bytes()
        assert hashlib.sha256(raw).hexdigest() == row["record_sha256"]
        doc = yaml.safe_load(raw)
        nodes = doc["ecological_interactions"]
        names = {n["name"] for n in nodes}
        assert Counter(d["node"] for d in row["node_decisions"]) == Counter(names)
        edges = [{"source": n["name"], **e} for n in nodes for e in n.get("downstream", [])]
        assert row["edges_after"] == edges
        assert all(e["target"] in names for e in edges)
        assert {(e["source"], e["target"]) for e in row["edges_before"]} == {
            (e["source"], e["target"])
            for e in row["retained_edge_decisions"] + row["removed_edge_decisions"]
        }
        assert any(d["kind"] == "KNOWLEDGE_GAP" for d in doc["discussions"])
        assert all(
            a.split("#", 1)[1] in names
            for d in doc["discussions"]
            for a in d["attaches_to"]
            if a.startswith("ecological_interactions#")
        )
