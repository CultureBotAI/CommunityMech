"""Preserve omics measurement limits, tested partners and positive outcomes."""

import hashlib
from collections import Counter
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "reports/causal_graph_review/decisions/20261005-three-records-batch23.yaml"
STEMS = [
    "Community_G_GenX_Biodegradation_Consortium",
    "Composting_SynCom_Lignocellulose_Degradation_Humus",
    "Coniochaeta_Sphingobacterium_Citrobacter_Wheat_Straw_Consortium",
]


def record(index):
    return yaml.safe_load((ROOT / "kb/communities" / f"{STEMS[index]}.yaml").read_text())


def assert_participants(node, doc, indices):
    assert node["scope"] == "COMMUNITY_LEVEL"
    assert not {"source_taxon", "target_taxon", "interaction_type"} & node.keys()
    assert node["participating_taxa"] == [
        {
            "preferred_term": doc["taxonomy"][i]["taxon_term"]["preferred_term"],
            "term": doc["taxonomy"][i]["taxon_term"]["term"],
        }
        for i in indices
    ]


def test_genx_relative_profiles_do_not_establish_competition_or_degrader_identity():
    doc = record(0)
    (node,) = doc["ecological_interactions"]
    assert_participants(node, doc, range(6))
    assert not node.get("downstream")
    assert "relative enrichment" in node["description"]
    assert "an observed subset, not the complete consortium" in node["description"]
    assert "Bulk GenX loss and fluoride release support community activity" in node["description"]
    assert "do not establish absolute viable expansion or extinction" in node["description"]
    assert "reciprocal competitive harm" in node["description"]
    assert node["evidence"][0]["supports"] == "PARTIAL"
    assert any("GENIA" in d.get("rationale", "") for d in doc["discussions"])


def test_compost_metagenomics_and_native_genera_are_not_activity_or_inoculant_roster():
    native, genes, output = record(1)["ecological_interactions"]
    for node in (native, genes, output):
        assert node["scope"] == "COMMUNITY_LEVEL"
        assert (
            not {"interaction_type", "participating_taxa", "source_taxon", "target_taxon"}
            & node.keys()
        )
    assert "not the five inoculant identities" in native["description"]
    assert (
        "not a direct measurement of enzyme expression or catalytic activity"
        in genes["description"]
    )
    assert genes["evidence"][0]["evidence_source"] == "COMPUTATIONAL"
    assert native["downstream"][0]["target"] == genes["name"]
    assert genes["downstream"][0]["target"] == output["name"]
    assert all(
        n["downstream"][0]["description"].startswith("HYPOTHESIZED") for n in (native, genes)
    )


def test_compost_retains_positive_treatment_outcome_and_abstract_access_limit():
    doc = record(1)
    output = doc["ecological_interactions"][2]
    assert "higher humus content than the control" in output["description"]
    assert "earlier maturation" in output["description"]
    assert output["evidence"][0]["supports"] == "SUPPORT"
    assert "full experimental details were unavailable" in output["evidence"][0]["explanation"]
    assert any("full body" in d.get("rationale", "") for d in doc["discussions"])


def test_straw_fungal_capacity_is_source_only_and_not_measured_catalysis():
    doc = record(2)
    fungus = doc["ecological_interactions"][0]
    assert fungus["scope"] == "PAIRWISE"
    assert fungus["source_taxon"]["term"]["id"] == "NCBITaxon:1571157"
    assert not {"target_taxon", "participating_taxa", "interaction_type"} & fungus.keys()
    assert "not directly measured enzyme activity" in fungus["description"]
    assert all(e["supports"] == "PARTIAL" for e in fungus["evidence"])


def test_straw_bacterial_roles_do_not_assert_directed_or_exclusive_vitamin_donation():
    doc = record(2)
    bacteria = doc["ecological_interactions"][1]
    assert_participants(bacteria, doc, [1, 2])
    assert "RibE is encoded by all three members" in bacteria["description"]
    assert "the medium supplies riboflavin" in bacteria["description"]
    assert "so4 ribE expression increases late at 60 rpm" in bacteria["description"]
    assert "exclusive w15 vitamin B2 donation is not established" in bacteria["description"]


def test_straw_pair_effect_and_output_keep_control_and_condition_boundaries():
    doc = record(2)
    fungus, bacteria, inhibition, output = doc["ecological_interactions"]
    for node in (inhibition, output):
        assert_participants(node, doc, [0, 1, 2])
    assert "bacterial pair, not isolated w15" in inhibition["description"]
    assert "lower degradation" in inhibition["description"]
    assert "not established reciprocal competitive harm" in inhibition["description"]
    assert "60 rpm (27.1 +/- 2.4%)" in output["description"]
    assert "180 rpm (16.2 +/- 1.7%)" in output["description"]
    assert "not selectively demonstrated enzyme synergism" in output["description"]
    for node in (fungus, bacteria):
        assert node["downstream"][0]["target"] == output["name"]
        assert node["downstream"][0]["description"].startswith("PARTIAL")


def test_batch23_source_scope_does_not_claim_inaccessible_bodies_were_read():
    ledger = yaml.safe_load(LEDGER.read_text())
    rows = ledger["records"]
    assert "Complete abstract only" in rows[1]["source_review"]["PMID:41297400"]["reviewed_scope"]
    assert (
        "Full Methods/Results not read"
        in rows[2]["source_review"]["PMID:31769802"]["reviewed_scope"]
    )
    assert (
        "Complete primary main body" in rows[2]["source_review"]["PMID:36991472"]["reviewed_scope"]
    )


def test_batch23_ledger_accounts_for_every_node_arrow_and_cache():
    ledger = yaml.safe_load(LEDGER.read_text())
    assert ledger["independent_approval"] is False
    assert len(ledger["reference_cache_original_hashes"]) == 6
    rows = ledger["records"]
    assert len(rows) == 3
    assert sum(len(r["node_decisions"]) for r in rows) == 8
    assert sum(len(r["retained_edge_decisions"]) for r in rows) == 4
    assert not any(r["removed_edge_decisions"] for r in rows)
    assert sum(len(r["renamed_nodes"]) for r in rows) == 6
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
        assert len(row["history_files"]) == 1
        assert any(d["kind"] == "KNOWLEDGE_GAP" for d in doc["discussions"])
        assert all(
            a.split("#", 1)[1] in names
            for d in doc["discussions"]
            for a in d["attaches_to"]
            if a.startswith("ecological_interactions#")
        )
    for path, expected in ledger["reference_cache_original_hashes"].items():
        assert hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == expected
