"""Guard measured plant outcomes and mixture-versus-member assay contrasts."""

import hashlib
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "reports/causal_graph_review/decisions/20261008-four-records-batch121.yaml"


def records():
    ledger = yaml.safe_load(LEDGER.read_text())
    rows = ledger["records"]
    return ledger, rows, [yaml.safe_load((ROOT / row["path"]).read_text()) for row in rows]


def test_tomato_complementarity_is_not_reciprocal_mutualism():
    _, _, docs = records()
    nodes = docs[0]["ecological_interactions"]
    assert all("interaction_type" not in n for n in nodes)
    assert "biofilm and host defense" in nodes[0]["name"]
    assert "similar protective effects" in nodes[0]["evidence"][1]["snippet"]
    assert "do not measure reciprocal bacterial fitness" in nodes[0]["description"]


def test_tomato_biofilm_mediation_remains_partial():
    _, _, docs = records()
    a, b, c = docs[0]["ecological_interactions"]
    assert len(a["downstream"]) == len(b["downstream"]) == 1
    assert a["downstream"][0]["target"] == b["name"]
    assert b["downstream"][0]["target"] == c["name"]
    assert "PARTIAL for biofilm formation as the mediator" in a["downstream"][0]["description"]
    assert "not microbial mutualism" in b["description"]


def test_tomato_retains_positive_biosynthesis_perturbation():
    _, _, docs = records()
    nodes = docs[0]["ecological_interactions"]
    evidence = nodes[2]["evidence"][0]
    assert "fully abolished" in evidence["snippet"]
    assert evidence["supports"] == "SUPPORT"
    assert "biosynthesis perturbation" in nodes[1]["description"]
    assert "inhibiting their biosynthesis abolished" in nodes[1]["downstream"][0]["description"]
    assert "independently indispensable" in nodes[2]["description"]


def test_tomato_retains_complementary_overexpression_evidence():
    _, _, docs = records()
    node = docs[0]["ecological_interactions"][2]
    assert "overexpressing SlLOX5 and SlDES1" in node["evidence"][1]["snippet"]
    assert "stronger resistance" in node["evidence"][1]["snippet"]
    assert all(e["evidence_source"] == "IN_VIVO" for e in node["evidence"])
    assert len(docs[0]["discussions"][-1]["evidence"]) == 1


def test_wheat_c1_assembly_is_metadata_not_an_ecological_node():
    _, rows, docs = records()
    nodes = docs[1]["ecological_interactions"]
    assert len(nodes) == 2 and len(rows[1]["removed_node_decisions"]) == 1
    assert all("interaction_type" not in n for n in nodes)
    assert not any(n.get("downstream") for n in nodes)
    assert "persistence" in docs[1]["discussions"][-1]["evidence"][2]["snippet"]


def test_wheat_c1_retains_whole_mixture_plate_inhibition():
    _, _, docs = records()
    node = docs[1]["ecological_interactions"][0]
    assert "37.00%" in node["description"]
    assert "37.00" in node["evidence"][1]["snippet"]
    assert "not evidence that both bacterial and fungal fitness declined" in node["description"]


def test_wheat_c1_host_benefit_is_not_best_strain_superiority():
    _, _, docs = records()
    node = docs[1]["ecological_interactions"][1]
    assert "reduced root-rot scores and increased fresh root weight" in node["description"]
    assert (
        node["evidence"][1]["snippet"]
        == "None of them was significantly better than a single strain"
    )
    assert "Only B5" in node["description"]
    assert "no antifungal activity from any SynCom" in docs[1]["discussions"][-1]["rationale"]


def test_wheat_c6_preserves_direct_plate_inhibition_without_workflow_arrows():
    _, rows, docs = records()
    nodes = docs[2]["ecological_interactions"]
    assert len(nodes) == 5 and len(rows[2]["removed_node_decisions"]) == 1
    assert not any(n.get("downstream") for n in nodes)
    assert "34.48%" in nodes[0]["description"]
    assert "34.48" in nodes[0]["evidence"][1]["snippet"]


def test_wheat_c6_salkowski_is_not_resolved_delivery_or_mutualism():
    _, _, docs = records()
    node = docs[2]["ecological_interactions"][1]
    assert "interaction_type" not in node and "biological_processes" not in node
    assert "Salkowski" in node["name"]
    assert "11.76" in node["evidence"][1]["snippet"]
    assert "not structural identification" in node["description"]
    assert (
        "not independently resolved molecular identity or plant delivery"
        in node["metabolites"][0]["notes"]
    )


def test_wheat_c6_primary_root_shortening_is_not_growth_promotion():
    _, _, docs = records()
    node = docs[2]["ecological_interactions"][2]
    assert "primary-root shortening" in node["name"]
    assert "not demonstrated growth promotion" in node["description"]
    assert "does not establish IAA as the necessary mediator" in node["description"]
    assert node["evidence"][0]["evidence_source"] == "IN_VIVO"
    assert "except C5" in node["evidence"][0]["snippet"]


def test_wheat_c6_cell_free_member_positives_do_not_erase_mixture_null():
    _, _, docs = records()
    node = docs[2]["ecological_interactions"][3]
    assert "interaction_type" not in node and len(node["participating_taxa"]) == 4
    assert "significantly inhibited" in node["evidence"][1]["snippet"]
    assert "10 SynComs did not show any antifungal activities" in node["evidence"][2]["snippet"]
    assert (
        "individual secretion-associated inhibition cannot be assigned to the mixed culture"
        in node["description"]
    )


def test_wheat_c6_volatile_positive_list_is_not_a_mixture_benefit():
    _, _, docs = records()
    node = docs[2]["ecological_interactions"][4]
    assert "interaction_type" not in node and len(node["participating_taxa"]) == 4
    assert "SynComs C2-4, C7" in node["evidence"][2]["snippet"]
    assert "C6 was not one of the four significantly inhibitory mixtures" in node["description"]
    assert "Each of the four C6 member strains inhibited AG8" in node["description"]
    assert "does not identify C6" in node["evidence"][0]["explanation"]


def test_crown_rot_retains_positive_disease_and_grain_outcomes():
    _, _, docs = records()
    node = docs[3]["ecological_interactions"][0]
    assert "interaction_type" not in node
    assert "86.45%" in node["description"] and "25.93%" in node["description"]
    assert node["evidence"][1]["snippet"] == "SMC+Fp increased TKW by 10.39% relative to Fp"
    assert "not multilocation field validation" in node["description"]


def test_crown_rot_profiles_and_compound_assays_do_not_prove_necessity():
    ledger, _, docs = records()
    node = docs[3]["ecological_interactions"][1]
    assert "interaction_type" not in node and "biological_processes" not in node
    assert "not absolute viable abundance" in node["description"]
    assert "Total DNA was extracted" in node["evidence"][1]["snippet"]
    discussion = docs[3]["discussions"][-1]
    assert (
        discussion["evidence"][1]["snippet"]
        == "showed no direct antifungal activity of either compound"
    )
    assert discussion["evidence"][2]["snippet"] == "significantly reduced DSI"
    assert "not their necessity in the intact SMC" in discussion["rationale"]
    assert ledger["cache_changes"][0]["license"] == "CC BY-NC-ND 4.0"


def test_review_accounts_for_nodes_arrows_and_append_only_cache():
    ledger, rows, docs = records()
    counts = ledger["reviewed_counts"]
    assert (counts["original_nodes"], counts["retained_nodes"], counts["removed_nodes"]) == (
        14,
        12,
        2,
    )
    assert counts["renamed_nodes"] == 6
    assert (counts["original_arrows"], counts["retained_arrows"], counts["removed_arrows"]) == (
        2,
        2,
        0,
    )
    assert (counts["graph_quotations"], counts["discussion_quotations"]) == (24, 10)
    assert not ledger["independent_approval"] and ledger["edison"]["new_nodes_or_directions"] == 0
    (change,) = ledger["cache_changes"]
    assert change["old_prefix_preserved"] and change["added_quotation_words"] == 21
    assert (
        hashlib.sha256((ROOT / change["path"]).read_bytes()).hexdigest() == change["after_sha256"]
    )
    assert ledger["unresolved_non_graph_issues"] == [1943, 1944, 1945]
    for row, doc in zip(rows, docs, strict=True):
        assert hashlib.sha256((ROOT / row["path"]).read_bytes()).hexdigest() == row["record_sha256"]
        names = [n["name"] for n in doc["ecological_interactions"]]
        assert [r["node"] for r in row["node_decisions"]] == names
        assert len(row["history_files"]) == 1 and doc["curation_history"][-1]["llm_assisted"]
        assert len(doc["discussions"]) == 1
        assert all(
            a.removeprefix("ecological_interactions#") in names
            for a in doc["discussions"][0]["attaches_to"]
        )
        for node in doc["ecological_interactions"]:
            assert "downstream" not in node or node["downstream"]
            assert all(e["target"] in names for e in node.get("downstream", []))
