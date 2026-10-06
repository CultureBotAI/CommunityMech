"""Preserve positive observations without assay, mediator or roster overclaims."""

import hashlib
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "reports/causal_graph_review/decisions/20261006-coculture-hosts-batch63.yaml"
G = "Leptolyngbya_Pseudomonas_Mangrove_Coculture"
L = "Lotus_LjSC3"
R = "Lunar_Martian_Simulant_PGPB_Lettuce_SynCom"


def records():
    ledger = yaml.safe_load(LEDGER.read_text())
    rows = {Path(r["path"]).stem: r for r in ledger["records"]}
    docs = {name: yaml.safe_load((ROOT / r["path"]).read_text()) for name, r in rows.items()}
    return ledger, rows, docs


def test_mangrove_maxima_are_not_matched_time_or_partner_resolved():
    _, _, docs = records()
    growth = docs[G]["ecological_interactions"][0]
    assert "day 6" in growth["description"] and "day 9" in growth["description"]
    assert "not a matched-time comparison" in growth["description"]
    assert "resolve each partner separately" in growth["description"]
    assert "interaction_type" not in growth
    assert growth["evidence"][1]["supports"] == "PARTIAL"
    assert all("does not establish transfer" in m["notes"] for m in growth["metabolites"])


def test_mangrove_association_is_not_contact_necessity_or_new_structure():
    _, rows, docs = records()
    association = docs[G]["ecological_interactions"][1]
    assert "not a selective test that contact is required" in association["description"]
    assert rows[G]["edges_before"] == rows[G]["edges_after"] == []
    assert "abstract" in association["description"]
    assert len(docs[G]["discussions"]) == 2


def test_lotus_relative_priority_and_root_specific_association_remain_distinct():
    _, rows, docs = records()
    preference, priority, invasion = docs[L]["ecological_interactions"]
    assert "SC3 mono-association" in preference["description"]
    assert "four weeks" in priority["description"] and "two weeks" in priority["description"]
    assert "higher relative proportions" in priority["description"]
    assert "did not significantly increase total bacterial load" in priority["description"]
    assert "absent in rhizosphere samples" in invasion["description"]
    assert "association, not selective manipulation" in invasion["description"]
    assert len(rows[L]["removed_edge_decisions"]) == 2


def test_lotus_does_not_certify_unverified_bacterial_roster():
    _, _, docs = records()
    for node in docs[L]["ecological_interactions"]:
        assert [t["term"]["id"] for t in node["participating_taxa"]] == ["NCBITaxon:34305"]
        assert "interaction_type" not in node and "downstream" not in node
        assert all(e["evidence_source"] == "IN_VIVO" for e in node["evidence"])
    text = docs[L]["discussions"][-1]["rationale"]
    assert "SC1" in text and "SC2" in text and "SC3" in text
    assert "connectivity warnings" in text and "#1559" in text


def test_lettuce_screen_is_not_commensalism_or_establishment():
    _, _, docs = records()
    screen = docs[R]["ecological_interactions"][0]
    assert "no inhibition zones" in screen["description"]
    assert "not demonstrated commensalism" in screen["description"]
    assert all(e["evidence_source"] == "IN_VITRO" for e in screen["evidence"])
    assert "interaction_type" not in screen and "downstream" not in screen


def test_lettuce_gene_copies_are_not_expression_flux_or_strain_tracking():
    _, _, docs = records()
    genes = docs[R]["ecological_interactions"][1]
    assert "amended simulants did not show significant" in genes["description"]
    assert "not expression, nitrogen-fixation flux or phosphate release" in genes["description"]
    assert "could not distinguish environmental from inoculated strains" in genes["description"]
    assert "no direct fixation-rate measurement" in genes["biological_processes"][0]["notes"]
    assert all(e["evidence_source"] == "IN_VIVO" for e in genes["evidence"])
    assert "interaction_type" not in genes and "downstream" not in genes


def test_lettuce_plant_benefits_are_retained_without_hormone_or_mutualism_claim():
    _, rows, docs = records()
    outcome = docs[R]["ecological_interactions"][2]
    assert "35% overall" in outcome["description"] and "26% on average" in outcome["description"]
    assert "significantly only for P and K" in outcome["description"]
    assert "no significant overall inoculum effect" in outcome["description"]
    assert "do not establish IAA mediation" in outcome["description"]
    assert outcome["biological_processes"][0]["term"]["id"] == "GO:0044419"
    assert all(e["evidence_source"] == "IN_VIVO" for e in outcome["evidence"])
    assert "interaction_type" not in outcome and "downstream" not in outcome
    assert len(rows[R]["removed_edge_decisions"]) == 2
    for node in docs[R]["ecological_interactions"]:
        assert [t["term"]["id"] for t in node["participating_taxa"]] == [
            "NCBITaxon:353",
            "NCBITaxon:1404",
            "NCBITaxon:223967",
            "NCBITaxon:1646340",
        ]


def test_batch63_caches_and_canonical_participants_are_not_rewritten():
    ledger, _, docs = records()
    for path, digest in ledger["reference_cache_original_hashes"].items():
        assert hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == digest
    for doc in docs.values():
        canonical = {
            t["taxon_term"]["preferred_term"]: t["taxon_term"]["term"] for t in doc["taxonomy"]
        }
        for node in doc["ecological_interactions"]:
            taxa = node.get("participating_taxa", []) + [
                node[k] for k in ["source_taxon", "target_taxon"] if k in node
            ]
            for taxon in taxa:
                assert canonical[taxon["preferred_term"]] == taxon["term"]
        assert "#1559" in doc["discussions"][-1]["rationale"]
    assert ledger["unresolved_non_graph_issues"] == [1559]
    assert ledger["primary_graph_snippet_count"] == 12


def test_batch63_all_nodes_arrows_anchors_histories_and_limits_are_recorded():
    ledger, rows, docs = records()
    assert ledger["independent_approval"] is False
    assert ledger["issues"] == [1556, 1557, 1558]
    assert ledger["edison"]["provider_submissions"] == ledger["edison"]["credits_spent"] == 0
    assert sum(len(r["node_decisions"]) for r in rows.values()) == 8
    assert sum(len(r["edges_before"]) for r in rows.values()) == 4
    assert sum(len(r["edges_after"]) for r in rows.values()) == 0
    assert sum(len(r["removed_edge_decisions"]) for r in rows.values()) == 4
    for name, row in rows.items():
        doc = docs[name]
        assert hashlib.sha256((ROOT / row["path"]).read_bytes()).hexdigest() == row["record_sha256"]
        assert doc["curation_history"][-1]["llm_assisted"] is True
        assert len(row["history_files"]) == 1 and row["status"] == "reviewed"
        names = {n["name"] for n in doc["ecological_interactions"]}
        assert {d["node"] for d in row["node_decisions"]} == names
        assert {a.split("#", 1)[1] for a in doc["discussions"][-1]["attaches_to"]} == names
        assert doc["discussions"][-1]["status"] == "OPEN"
