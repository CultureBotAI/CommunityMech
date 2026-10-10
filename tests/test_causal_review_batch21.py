"""Preserve supported conversion mechanisms without promoting assay inference."""

import hashlib
from collections import Counter
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "reports/causal_graph_review/decisions/20261005-three-records-batch21.yaml"
STEMS = [
    "Clostridium_Phytofermentans_Ecoli_Cellobiose_Biofilm_Consortium",
    "Clostridium_Saccharomyces_Cellulose_Ethanol_Coculture",
    "Clostridium_Thermoanaerobacter_Cellulosic_Bioethanol_Coculture",
]


def record(index):
    return yaml.safe_load((ROOT / "kb/communities" / f"{STEMS[index]}.yaml").read_text())


def assert_participants(node, doc, indices=None):
    selected = doc["taxonomy"]
    if indices is not None:
        selected = [selected[i] for i in indices]
    assert node["scope"] == "COMMUNITY_LEVEL"
    assert "source_taxon" not in node and "target_taxon" not in node
    assert node["participating_taxa"] == [
        {"preferred_term": t["taxon_term"]["preferred_term"], "term": t["taxon_term"]["term"]}
        for t in selected
    ]


def test_biofilm_keeps_glucose_controls_without_polymer_conversion_claim():
    sugar, _, _, output = record(0)["ecological_interactions"]
    assert sugar["interaction_type"] == "CROSS_FEEDING"
    assert "Glucose-addition and spent-medium enzyme assays" in sugar["description"]
    assert "cellobiose, not direct polymer-cellulose conversion" in sugar["description"]
    assert sugar["evidence"][0]["supports"] == "PARTIAL"
    for node in (sugar, output):
        assert "GO:0030245" not in {p["term"]["id"] for p in node["biological_processes"]}
    nodes = record(0)["ecological_interactions"]
    assert [n["downstream"][0]["target"] for n in nodes[:3]] == [output["name"]] * 3
    assert all(n["downstream"][0]["description"].startswith("PARTIAL") for n in nodes[:3])


def test_reciprocal_necromass_preserves_distinct_assays_and_viability_control():
    doc = record(0)
    node = doc["ecological_interactions"][1]
    assert_participants(node, doc)
    assert node["interaction_type"] == "CROSS_FEEDING"
    assert "biological_processes" not in node
    assert "aerobic E. coli growth" in node["description"]
    assert "anaerobic C. phytofermentans growth" in node["description"]
    assert "CFU measurements" in node["description"]
    assert "distinct assays" in node["description"]
    assert "do not isolate a specific peptide mediator" in node["metabolites"][0]["notes"]


def test_biofilm_oxygen_and_products_are_bounded_by_measurements():
    _, _, oxygen, output = record(0)["ecological_interactions"]
    assert "interaction_type" not in oxygen and "interaction_type" not in output
    assert "Oxygen microprofiles" in oxygen["description"]
    assert "first grow anoxically" in oxygen["description"]
    assert "Fully oxic inoculation did not" in oxygen["description"]
    assert "do not alone measure viability" in oxygen["description"]
    assert "more ethanol and biomass than the summed monocultures" in output["description"]
    assert "biomass plus extracellular material" in output["description"]
    assert "cellobiose use and ethanol output were not directly measured" in output["description"]


def test_yeast_keeps_conditional_mutualism_and_enzyme_assisted_productivity():
    sugar, oxygen, maintenance = record(1)["ecological_interactions"]
    assert sugar["interaction_type"] == "CROSS_FEEDING"
    assert "22 g/L ethanol result used added endoglucanase" in sugar["description"]
    assert "unsupplemented coculture did not" in sugar["description"]
    assert oxygen["interaction_type"] == "MUTUALISM"
    assert "respiratory protection" in oxygen["description"]
    assert (
        "not a claim that either organism universally requires its partner" in oxygen["description"]
    )
    for node in (sugar, oxygen):
        assert node["downstream"][0]["target"] == maintenance["name"]
        assert "PARTIAL" in node["downstream"][0]["description"]


def test_yeast_maintenance_is_a_separate_viable_count_arm():
    doc = record(1)
    maintenance = doc["ecological_interactions"][2]
    assert_participants(maintenance, doc)
    assert "interaction_type" not in maintenance
    assert "30-, 40- and 50-day samples" in maintenance["description"]
    assert "below detection before day 30" in maintenance["description"]
    assert "25 mL medium and 150 g/L" in maintenance["description"]
    assert "distinct from the enzyme-assisted ethanol experiment" in maintenance["description"]


def test_x514_product_output_is_not_ethanol_donation_or_directly_traced_sugar():
    doc = record(2)
    supply, output, _ = doc["ecological_interactions"]
    assert supply["interaction_type"] == "CROSS_FEEDING"
    assert "not directly traced transfer" in supply["description"]
    assert "does not imply universally improved cellulose utilization" in supply["description"]
    assert supply["downstream"][0]["target"] == output["name"]
    assert_participants(output, doc)
    assert "interaction_type" not in output
    assert "not demonstrated ethanol donation" in output["description"]
    assert "multiple coculture comparisons" in output["evidence"][0]["explanation"]
    assert "The 2011 abstract" in output["description"]
    assert "separate LQRI-X514 fed-batch study" in output["description"]


def test_x514_b12_preserves_39e_control_without_claiming_vitamin_donation():
    doc = record(2)
    _, output, vitamin = doc["ecological_interactions"]
    assert vitamin["scope"] == "PAIRWISE"
    canonical = doc["taxonomy"][1]["taxon_term"]
    assert vitamin["source_taxon"] == {
        "preferred_term": canonical["preferred_term"],
        "term": canonical["term"],
    }
    assert "target_taxon" not in vitamin and "participating_taxa" not in vitamin
    assert "interaction_type" not in vitamin
    assert "supplementation improved 39E ethanol production" in vitamin["description"]
    assert "not demonstrated vitamin donation" in vitamin["description"]
    assert "fed-batch study supplied vitamins" in vitamin["description"]
    assert vitamin["downstream"][0]["target"] == output["name"]
    assert vitamin["downstream"][0]["description"].startswith("HYPOTHESIZED")
    assert all(e["supports"] == "PARTIAL" for e in vitamin["evidence"])


def test_batch21_ledger_accounts_for_every_node_arrow_and_cache():
    ledger = yaml.safe_load(LEDGER.read_text())
    assert ledger["independent_approval"] is False
    assert len(ledger["reference_cache_original_hashes"]) == 4
    rows = ledger["records"]
    assert len(rows) == 3
    assert sum(len(r["node_decisions"]) for r in rows) == 10
    assert sum(len(r["retained_edge_decisions"]) for r in rows) == 7
    assert sum(len(r["removed_edge_decisions"]) for r in rows) == 0
    assert sum(len(r["renamed_nodes"]) for r in rows) == 5
    for row in rows:
        raw = (ROOT / row["path"]).read_bytes()
        assert hashlib.sha256(raw).hexdigest() == row["record_sha256"]
        doc = yaml.safe_load(raw)
        nodes = doc["ecological_interactions"]
        names = {n["name"] for n in nodes}
        assert Counter(d["node"] for d in row["node_decisions"]) == Counter(names)
        edges = [{"source": n["name"], **e} for n in nodes for e in n.get("downstream", [])]
        assert row["edges_after"] == edges
        renames = row["renamed_nodes"]
        before = {
            (renames.get(e["source"], e["source"]), renames.get(e["target"], e["target"]))
            for e in row["edges_before"]
        }
        assert before == {(e["source"], e["target"]) for e in row["retained_edge_decisions"]}
        assert all(e["target"] in names for e in edges)
        assert any(d["kind"] == "KNOWLEDGE_GAP" for d in doc["discussions"])
        assert all(
            a.split("#", 1)[1] in names
            for d in doc["discussions"]
            for a in d["attaches_to"]
            if a.startswith("ecological_interactions#")
        )
    for path, expected in ledger["reference_cache_original_hashes"].items():
        assert hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == expected
