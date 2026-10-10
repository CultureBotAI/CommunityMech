"""Pin positive results, experimental scope and every original graph decision."""

import hashlib
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "reports/causal_graph_review/decisions/20261006-three-records-batch55.yaml"


def records():
    ledger = yaml.safe_load(LEDGER.read_text())
    return ledger, [yaml.safe_load((ROOT / r["path"]).read_text()) for r in ledger["records"]]


def test_explicit_participants_preserve_canonical_subsets_and_strain_names():
    _, docs = records()
    scopes = [
        [[3, 4], [0, 2, 5, 6], list(range(7)), [5, 6], [1]],
        [list(range(4))] * 4,
        [list(range(3))] * 2,
    ]
    for doc, indexes_by_node in zip(docs, scopes, strict=True):
        for node, indexes in zip(doc["ecological_interactions"], indexes_by_node, strict=True):
            assert node["scope"] == "COMMUNITY_LEVEL"
            assert not {"interaction_type", "source_taxon", "target_taxon"} & node.keys()
            assert node["participating_taxa"] == [
                {
                    "preferred_term": doc["taxonomy"][i]["taxon_term"]["preferred_term"],
                    "term": doc["taxonomy"][i]["taxon_term"]["term"],
                }
                for i in indexes
            ]
    strains = docs[2]["ecological_interactions"][0]["participating_taxa"]
    assert len({p["preferred_term"] for p in strains}) == 3
    assert {p["term"]["id"] for p in strains} == {"NCBITaxon:2"}


def test_ree_retains_positive_wall_perturbation_without_active_transport():
    _, (doc, _, _) = records()
    binding, _, field, _, acido = doc["ecological_interactions"]
    assert "65.5 to 17.8 percent" in binding["description"]
    assert "residual binding remained" in binding["description"]
    assert "passive surface binding" in binding["description"]
    assert "biological_processes" not in binding
    assert all(e["evidence_source"] == "IN_VITRO" for e in binding["evidence"])
    assert all(e["supports"] == "SUPPORT" for e in binding["evidence"])
    assert {m["term"]["id"] for m in binding["metabolites"]} == {"CHEBI:49962", "CHEBI:49980"}
    assert "elemental sums" in field["description"] and "45 m" in field["description"]
    assert "metabolites" not in field and "biological_processes" not in field
    assert "generally decreased with depth" in acido["description"]
    assert "metabolites" not in acido and "downstream" not in acido


def test_ree_proposed_weathering_and_field_mediation_remain_qualified():
    _, (doc, _, _) = records()
    binding, weather, field, fungi, _ = doc["ecological_interactions"]
    assert binding["downstream"][0]["target"] == field["name"]
    assert binding["downstream"][0]["description"].startswith("PARTIAL - ")
    for node in [weather, fungi]:
        assert node["description"].startswith("HYPOTHESIZED - ")
        assert all(e["supports"] == "PARTIAL" for e in node["evidence"])
        assert node["downstream"][0]["target"] == binding["name"]
        assert node["downstream"][0]["description"].startswith("HYPOTHESIZED - ")
    assert "#1520" in doc["discussions"][-1]["rationale"]


def test_maize_assay_specificity_and_unperformed_challenge_are_explicit():
    _, (_, doc, _) = records()
    traits, defense, seedling, field = doc["ecological_interactions"]
    assert "Salkowski chemistry is not specific identification" in traits["description"]
    assert "nitrogenase proxy" in traits["description"]
    assert "Helminthosporium was hardly inhibited" in defense["description"]
    assert (
        "did not test induced systemic resistance with a fungal challenge" in defense["description"]
    )
    assert "shoot/root dry weights were 2.3/3" in seedling["description"]
    assert "Conejo" in seedling["description"] and "CPL9105W" in field["description"]
    assert (
        "11 to 16 tons/ha" in field["description"] and "12.5 to 8 percent" in field["description"]
    )
    assert all(
        "subset of the reported six-strain" in n["description"]
        for n in doc["ecological_interactions"]
    )
    assert all(
        e["supports"] == "SUPPORT" for n in doc["ecological_interactions"] for e in n["evidence"]
    )


def test_maize_workflow_removed_but_candidate_mediation_retained():
    ledger, (_, doc, _) = records()
    traits, defense, seedling, field = doc["ecological_interactions"]
    assert "downstream" not in seedling and "downstream" not in field
    assert traits["downstream"][0]["target"] == seedling["name"]
    assert defense["downstream"][0]["target"] == field["name"]
    assert all(
        n["downstream"][0]["description"].startswith("PARTIAL - ") for n in [traits, defense]
    )
    assert len(ledger["records"][1]["removed_edge_decisions"]) == 3
    assert "#1521" in doc["discussions"][-1]["rationale"]


def test_jiangshui_positive_formulation_effect_and_access_limits():
    _, (_, _, doc) = records()
    fermentation, products = doc["ecological_interactions"]
    assert fermentation["name"] == "Three-Strain 2:3:1 Jiangshui Fermentation"
    arrow = fermentation["downstream"][0]
    assert arrow["target"] == products["name"]
    assert "positive formulation-level intervention" in arrow["description"]
    assert not arrow["description"].startswith("PARTIAL")
    assert "72.20 percent" in products["description"] and "61.13 percent" in products["description"]
    assert "not identified compound flux" in products["description"]
    assert len(doc["curation_history"]) == 3
    assert "no primary full body was inspected" in doc["discussions"][-1]["rationale"]
    assert len(doc["discussions"]) >= 2


def test_all_original_nodes_and_arrows_are_partitioned_into_decisions():
    ledger, docs = records()
    assert ledger["independent_approval"] is False
    assert ledger["issues"] == [1517, 1518, 1519]
    assert ledger["unresolved_non_graph_issues"] == [1520, 1521]
    assert ledger["issue_deduplication"]["ignored_hidden_local_search"] is True
    for i, (row, doc) in enumerate(zip(ledger["records"], docs, strict=True)):
        assert row["status"] == "reviewed"
        assert hashlib.sha256((ROOT / row["path"]).read_bytes()).hexdigest() == row["record_sha256"]
        assert len(row["node_decisions"]) + len(row["removed_node_decisions"]) == [5, 5, 3][i]
        assert {d["node"] for d in row["node_decisions"]} == {
            n["name"] for n in doc["ecological_interactions"]
        }
        rename = row["renamed_nodes"]
        old_edges = {
            (rename.get(e["source"], e["source"]), rename.get(e["target"], e["target"]))
            for e in row["edges_before"]
        }
        retained = {(e["source"], e["target"]) for e in row["retained_edge_decisions"]}
        removed = {
            (rename.get(e["source"], e["source"]), rename.get(e["target"], e["target"]))
            for e in row["removed_edge_decisions"]
        }
        assert old_edges == retained | removed and not retained & removed
        names = {n["name"] for n in doc["ecological_interactions"]}
        for d in doc.get("discussions", []):
            assert all(
                a.split("#", 1)[1] in names
                for a in d.get("attaches_to", [])
                if a.startswith("ecological_interactions#")
            )


def test_caches_unchanged_and_spot_check_does_not_claim_full_second_reading():
    ledger, _ = records()
    for path, digest in ledger["reference_cache_original_hashes"].items():
        assert hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == digest
    check = ledger["primary_spot_check"]
    assert not check["cache_changed"]
    assert sum(len(q.split()) for q in check["verified_excerpts"]) == check["quoted_words"] == 22
    assert "not a complete second" in check["scope"]
