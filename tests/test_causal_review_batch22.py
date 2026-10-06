"""Bound treatment effects and product associations without erasing controls."""

import hashlib
from collections import Counter
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "reports/causal_graph_review/decisions/20261005-three-records-batch22.yaml"
STEMS = [
    "Clostridium_Thermoanaerobacterium_JN4_GD17_Cellulosic_Biofuel_Coculture",
    "Clostridium_Thermocellum_Saccharoperbutylacetonicum_Cellulosic_Butanol_Coculture",
    "Coastal_Forested_Wetland_Seawater_Ion_Microcosm_Community",
]


def record(index):
    return yaml.safe_load((ROOT / "kb/communities" / f"{STEMS[index]}.yaml").read_text())


def assert_participants(node, doc):
    assert node["scope"] == "COMMUNITY_LEVEL"
    assert "source_taxon" not in node and "target_taxon" not in node
    assert "interaction_type" not in node
    assert node["participating_taxa"] == [
        {"preferred_term": t["taxon_term"]["preferred_term"], "term": t["taxon_term"]["term"]}
        for t in doc["taxonomy"]
    ]


def test_jn4_output_and_conversion_keep_positive_evidence_without_harm_enum():
    doc = record(0)
    output, conversion, inhibition = doc["ecological_interactions"]
    assert_participants(output, doc)
    assert "more lactate, acetate and ethanol" in output["description"]
    assert "without improved overall cellulose utilization" in output["description"]
    assert "separate monoculture assays" in conversion["description"]
    assert "do not directly partition partner carbon flux" in conversion["description"]
    for node in (conversion, inhibition):
        assert node["scope"] == "PAIRWISE"
        assert node["source_taxon"]["term"]["id"] == "NCBITaxon:1517"
        assert node["target_taxon"]["term"]["id"] == "NCBITaxon:1515"
        assert "interaction_type" not in node
        assert node["downstream"][0]["target"] == output["name"]
        assert node["downstream"][0]["description"].startswith("PARTIAL")


def test_jn4_growth_and_stimulants_are_not_viable_counts_or_carbon_partition():
    node = record(0)["ecological_interactions"][2]
    assert "estimated from total protein and genomic community proportions" in node["description"]
    assert "not a direct viable-cell count" in node["description"]
    assert "largely stopped cellulose use" in node["description"]
    assert "adds carbon and changes sampling time" in node["description"]
    assert (
        "not a measured reduction of total fermentation products"
        in node["downstream"][0]["description"]
    )


def test_butanol_staging_and_output_do_not_become_donation_or_exclusive_flux():
    doc = record(1)
    supply, output, _ = doc["ecological_interactions"]
    assert supply["interaction_type"] == "CROSS_FEEDING"
    assert supply["scope"] == "PAIRWISE"
    assert "timing and temperature are coupled" in supply["description"]
    assert "inoculum medium contains glucose" in supply["description"]
    assert "staged-versus-simultaneous comparison" in supply["downstream"][0]["description"]
    assert supply["downstream"][0]["target"] == output["name"]
    assert_participants(output, doc)
    assert "acetone-addition control" in output["description"]
    assert "retain acetone-pathway enzyme activities" in output["description"]
    assert "not butanol donation or proof of pathway shutdown" in output["description"]


def test_butanol_hydrogen_retains_only_a_hypothesized_redox_contribution():
    doc = record(1)
    _, output, hydrogen = doc["ecological_interactions"]
    assert_participants(hydrogen, doc)
    assert "2013 abstract" in hydrogen["description"]
    assert "future hydrogenase selection" in hydrogen["description"]
    assert "2011 Discussion proposes redox allocation" in hydrogen["description"]
    assert "interspecies hydrogen donation" in hydrogen["description"]
    assert hydrogen["downstream"][0]["target"] == output["name"]
    assert hydrogen["downstream"][0]["description"].startswith("HYPOTHESIZED")
    assert all(e["supports"] == "PARTIAL" for e in hydrogen["evidence"])


def test_wetland_treatment_and_dna_response_are_not_niche_or_activity_claims():
    nodes = record(2)["ecological_interactions"]
    exposure, _, genes, flux = nodes
    for node in nodes:
        assert node["scope"] == "COMMUNITY_LEVEL"
        assert (
            not {"interaction_type", "source_taxon", "target_taxon", "participating_taxa"}
            & node.keys()
        )
    assert "does not isolate sodium chloride" in exposure["description"]
    assert "relative abundances" in genes["description"]
    assert "not transcript abundance, pathway activity" in genes["description"]
    assert [e["target"] for e in exposure["downstream"]] == [genes["name"], flux["name"]]
    assert all("PARTIAL" in e["description"] for e in exposure["downstream"])


def test_wetland_null_and_gases_preserve_temporal_and_statistical_distinctions():
    _, sulfate, _, flux = record(2)["ecological_interactions"]
    assert "increased porewater sulfate" in sulfate["description"]
    assert "at week 12" in sulfate["description"]
    assert "Hydrogen sulfide was detected" in sulfate["description"]
    assert "at day 14" in sulfate["description"]
    assert "does not establish inactive sulfate reduction" in sulfate["description"]
    assert "no significant individual pairwise contrasts" in flux["description"]
    assert "complete artificial seawater was intermediate" in flux["description"]
    assert "including sulfate-only" in flux["description"]
    assert "do not directly partition microbial production and consumption" in flux["description"]


def test_batch22_adds_exactly_two_mixed_scope_records_with_named_pairs():
    for index in (0, 1):
        doc = record(index)
        nodes = doc["ecological_interactions"]
        assert len(doc["taxonomy"]) == 2
        assert {n["scope"] for n in nodes} == {"PAIRWISE", "COMMUNITY_LEVEL"}
        pairs = [n for n in nodes if n["scope"] == "PAIRWISE"]
        assert {
            n[role]["term"]["id"] for n in pairs for role in ("source_taxon", "target_taxon")
        } == {t["taxon_term"]["term"]["id"] for t in doc["taxonomy"]}
    assert all(n["scope"] == "COMMUNITY_LEVEL" for n in record(2)["ecological_interactions"])


def test_batch22_ledger_accounts_for_every_node_arrow_and_cache():
    ledger = yaml.safe_load(LEDGER.read_text())
    assert ledger["independent_approval"] is False
    assert len(ledger["reference_cache_original_hashes"]) == 7
    rows = ledger["records"]
    assert len(rows) == 3
    assert sum(len(r["node_decisions"]) for r in rows) == 10
    assert sum(len(r["retained_edge_decisions"]) for r in rows) == 6
    assert sum(len(r["removed_edge_decisions"]) for r in rows) == 0
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
        assert any(d["kind"] == "KNOWLEDGE_GAP" for d in doc["discussions"])
        assert all(
            a.split("#", 1)[1] in names
            for d in doc["discussions"]
            for a in d["attaches_to"]
            if a.startswith("ecological_interactions#")
        )
    for path, expected in ledger["reference_cache_original_hashes"].items():
        assert hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == expected
