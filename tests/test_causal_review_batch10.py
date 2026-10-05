"""Keep measured outcomes distinct from model, transcript and assay-context claims."""

import hashlib
from collections import Counter
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "reports/causal_graph_review/decisions/20261005-ten-records-batch10.yaml"


def record(stem):
    return yaml.safe_load((ROOT / "kb/communities" / f"{stem}.yaml").read_text())


def test_california_keeps_relative_metric_and_two_hypotheses():
    doc = record("California_Grassland_Precipitation_Legacy_Soil_Community")
    recycling, allocation, turnover = doc["ecological_interactions"]
    assert recycling["description"].startswith("HYPOTHESIZED")
    assert allocation["description"].startswith("HYPOTHESIZED")
    assert "scaled to the observed maximum" in turnover["description"]
    assert "not absolute carbon-use efficiency" in turnover["description"]
    assert "nonsignificant, not equivalent" in turnover["description"]
    assert len(turnover["downstream"]) == 2
    assert all(e["description"].startswith("HYPOTHESIZED") for e in turnover["downstream"])
    assert all(
        e["evidence_source"] == "IN_VITRO"
        for n in doc["ecological_interactions"]
        for e in n["evidence"]
    )


def test_candida_removes_workflow_not_the_partial_exchange_hypothesis():
    doc = record("Candida_Parapsilosis_Hospitalized_Infant_Microbiome")
    codetect, succession, exchange, expression = doc["ecological_interactions"]
    assert len(doc["ecological_interactions"]) == 4
    assert all("interaction_type" not in n for n in (codetect, succession, expression))
    assert exchange["interaction_type"] == "CROSS_FEEDING"
    assert all(e["supports"] == "PARTIAL" for e in exchange["evidence"])
    assert exchange["source_taxon"]["term"]["label"] == "Lodderomyces parapsilosis"
    assert "another fungal strain" in exchange["description"]
    assert "absolute fungal decline or eradication" in succession["description"]
    assert "biological_processes" not in expression
    assert not any(n.get("downstream") for n in doc["ecological_interactions"])


def test_caragana_forage_keeps_both_proposed_mechanisms():
    doc = record("Caragana_Korshinskii_CrossKingdom_Forage_SynCom")
    degradation, suppression, acidification = doc["ecological_interactions"]
    assert all("interaction_type" not in n for n in doc["ecological_interactions"])
    assert degradation["downstream"][0]["target"] == acidification["name"]
    assert acidification["downstream"][0]["target"] == suppression["name"]
    assert all(
        e["description"].startswith("HYPOTHESIZED")
        for n in doc["ecological_interactions"]
        for e in n.get("downstream", [])
    )
    assert "every treatment including the control exceeded 95%" in suppression["description"]
    assert "three inoculants, not excluded genera" in suppression["description"]
    assert "Tax4Fun" in acidification["description"]
    assert "not expression or measured pyruvate flux" in acidification["description"]


def test_syncom15_does_not_inherit_syncom5_mechanisms():
    doc = record("Caragana_Wheat_Drought_SynCom15")
    growth, genes = doc["ecological_interactions"]
    assert "non-sterile pot assays" in growth["description"]
    assert "DNA abundance is not expression" in genes["description"]
    assert "cannot be assigned to SynCom15" in genes["description"]
    assert all(
        e["supports"] == "PARTIAL" and e["evidence_source"] == "COMPUTATIONAL"
        for e in genes["evidence"]
    )
    assert len(doc["taxonomy"]) == 15
    assert any(d["discussion_id"] == "syncom5_membership_text_gap" for d in doc["discussions"])
    assert not any(n.get("downstream") for n in doc["ecological_interactions"])


def test_cellulomonas_keeps_acid_class_and_net_yield_not_fixation():
    transfer, hydrogen, mutant = record(
        "Cellulomonas_Rhodobacter_Cellulose_Photohydrogen_Coculture"
    )["ecological_interactions"]
    assert transfer["interaction_type"] == "CROSS_FEEDING"
    assert transfer["metabolites"][1]["term"] == {"id": "CHEBI:64709", "label": "organic acid"}
    assert "interaction_type" not in hydrogen and "interaction_type" not in mutant
    assert "biological_processes" not in hydrogen
    assert hydrogen["name"] == "Nitrogenase-Dependent Net Photohydrogen Yield"
    assert (
        transfer["downstream"][0]["target"] == mutant["downstream"][0]["target"] == hydrogen["name"]
    )
    assert "gross nitrogenase production increased" in mutant["downstream"][0]["description"]


def test_cellulose_panel_keeps_model_provenance_and_donor_direction():
    rewiring, acetate, hydrogen = record("Cellulose_Methane_Combinatorial_SynCom_Panel")[
        "ecological_interactions"
    ]
    assert "MIP/MRO" in rewiring["description"]
    assert "not measured reciprocal fitness" in rewiring["description"]
    assert "assemblies containing that methanogen" in acetate["description"]
    assert (
        acetate["evidence"][1]["snippet"].strip()
        == "This was followed by the acetate exchange flux "
        "between R. cellulolyticum and M. concilii"
    )
    assert hydrogen["interaction_type"] == "SYNTROPHY"
    assert "Low H2 can favor donor lactate oxidation" in hydrogen["description"]
    assert all(e["supports"] == "PARTIAL" for e in hydrogen["evidence"])
    assert not any(n.get("downstream") for n in (rewiring, acetate, hydrogen))


def test_cellulose_quad_preserves_supported_routes_and_open_gap():
    doc = record("Cellulose_Methane_Quad_Culture_SynCom")
    overall, acetate, lactate, hydrogen, feedback, competition = doc["ecological_interactions"]
    assert (
        overall["evidence"][0]["snippet"]
        == "cooperated via cross-feeding to produce methane using cellulose"
    )
    assert acetate["downstream"][0]["target"] == overall["name"]
    assert acetate["evidence"][1]["evidence_source"] == "COMPUTATIONAL"
    assert lactate["downstream"][0]["target"] == hydrogen["name"]
    assert hydrogen["interaction_type"] == "SYNTROPHY"
    assert hydrogen["name"].startswith("Proposed")
    assert not feedback.get("downstream")
    assert feedback["evidence"][0]["supports"] == "PARTIAL"
    assert competition["interaction_type"] == "COMPETITION"
    assert competition["downstream"][0]["target"] == hydrogen["name"]
    assert "proteome fraction remained 3%" in competition["description"]
    assert sum(len(n.get("downstream", [])) for n in doc["ecological_interactions"]) == 5
    gap = next(
        d
        for d in doc["discussions"]
        if d["discussion_id"] == "kg-dv-acetate-co2-to-mc-methanogenesis"
    )
    assert gap["status"] == "OPEN"


def test_cembio_separates_colonization_development_and_member_odor():
    colonization, development, metabolism, odor = record(
        "CeMbio_Caenorhabditis_Elegans_Microbiome"
    )["ecological_interactions"]
    assert not colonization.get("downstream")
    assert (
        "interaction_type" not in colonization
        and "interaction_type" not in development
        and "interaction_type" not in odor
    )
    assert "developmental timing" in development["description"]
    assert all(p["term"]["id"] != "GO:0040007" for p in development["biological_processes"])
    assert metabolism["interaction_type"] == "NICHE_PARTITIONING"
    assert metabolism["downstream"][0]["description"].startswith("HYPOTHESIZED")
    assert "Inaccessible bacteria on the lid" in odor["description"]
    assert all(
        n["evidence"][0]["evidence_source"] == "IN_VIVO" for n in (colonization, development, odor)
    )


def test_pmsx_keeps_partial_exchange_and_correct_cmc():
    spatial, exchange = record("Carbon_Substrate_PMSX_Biofilm_SynCom")["ecological_interactions"]
    assert "interaction_type" not in spatial
    assert spatial["metabolites"][1]["term"] == {
        "id": "CHEBI:85146",
        "label": "carboxymethylcellulose",
    }
    assert exchange["interaction_type"] == "CROSS_FEEDING"
    assert all(e["supports"] == "PARTIAL" for e in exchange["evidence"])
    assert exchange["evidence"][0]["computational_provenance"]["tools"][0]["tool_name"] == "SMETANA"
    assert "Spatial mediation remains unproven" in exchange["description"]
    assert not spatial.get("downstream") and not exchange.get("downstream")


def test_cheese_retains_research_gap_without_borrowing_abstract_evidence():
    doc = record("Cheese_Rind_InSitu_InVitro_Model_Community")
    assembly, deacidification, succession = doc["ecological_interactions"]
    assert all("interaction_type" not in n for n in doc["ecological_interactions"])
    assert not assembly.get("evidence") and not deacidification.get("evidence")
    assert succession["evidence"][0]["reference"] == "PMID:25036636"
    assert not any(n.get("downstream") for n in doc["ecological_interactions"])
    row = next(r for r in yaml.safe_load(LEDGER.read_text())["records"] if r["id"] == doc["id"])
    assert row["status"] == "needs_research" and row["open_issue"] == 765


def test_batch10_ledger_hashes_nodes_and_directions_are_complete():
    rows = yaml.safe_load(LEDGER.read_text())["records"]
    assert len(rows) == 10
    assert Counter(r["status"] for r in rows) == {"reviewed": 9, "needs_research": 1}
    assert sum(len(r["node_decisions"]) for r in rows) == 33
    assert sum(len(r.get("removed_node_rationales", {})) for r in rows) == 1
    assert sum(len(r["removed_edge_decisions"]) for r in rows) == 2
    assert sum(len(r["retained_edge_decisions"]) for r in rows) == 12
    for row in rows:
        raw = (ROOT / row["path"]).read_bytes()
        assert hashlib.sha256(raw).hexdigest() == row["record_sha256"]
        doc = yaml.safe_load(raw)
        assert Counter(d["node"] for d in row["node_decisions"]) == Counter(
            n["name"] for n in doc["ecological_interactions"]
        )
        actual = [
            {"source": n["name"], **e}
            for n in doc["ecological_interactions"]
            for e in n.get("downstream", [])
        ]
        assert row["edges_after"] == actual
        assert {(e["source"], e["target"]) for e in actual} == {
            (d["source"], d["target"]) for d in row["retained_edge_decisions"]
        }
