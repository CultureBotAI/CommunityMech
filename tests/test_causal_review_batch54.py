"""Pin infant-gut causal strength, taxon ownership and positive interventions."""

import hashlib
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "reports/causal_graph_review/decisions/20261006-infant-gut-batch54.yaml"


def records():
    ledger = yaml.safe_load(LEDGER.read_text())
    return ledger, [yaml.safe_load((ROOT / r["path"]).read_text()) for r in ledger["records"]]


def test_explicit_canonical_participants_do_not_assert_pairwise_transfer():
    _, docs = records()
    expected = [[[0, 1], [0], [0], [0, 1]], [[0, 1, 2, 3], [2, 3], [2, 3]], [[2], [1], [0, 1]]]
    for doc, scopes in zip(docs, expected, strict=True):
        for node, indexes in zip(doc["ecological_interactions"], scopes, strict=True):
            assert node["scope"] == "COMMUNITY_LEVEL"
            assert not {"source_taxon", "target_taxon", "interaction_type"} & node.keys()
            assert node["participating_taxa"] == [
                {
                    "preferred_term": doc["taxonomy"][i]["taxon_term"]["preferred_term"],
                    "term": doc["taxonomy"][i]["taxon_term"]["term"],
                }
                for i in indexes
            ]


def test_phage_associations_keep_denominators_and_heterogeneous_recoding():
    _, (doc, _, _) = records()
    maternal, recoding, richness, stable = doc["ecological_interactions"]
    assert "155 of 1801" in maternal["description"]
    assert "40 infants" in stable["description"]
    assert "not all measured phages" in maternal["description"]
    assert "including decreases" in recoding["description"]
    assert recoding["evidence"][0]["supports"] == "SUPPORT"
    assert recoding["evidence"][1]["supports"] == "PARTIAL"
    assert "nucleotide diversity" in richness["description"]
    assert "downstream" not in richness
    assert "99 percent" in stable["description"]


def test_prebiotic_omission_retains_positive_effect_in_the_correct_direction():
    _, (_, doc, _) = records()
    network, hub, inhibition = doc["ecological_interactions"]
    assert "cross-experiment subset" in network["description"]
    assert "P. dorei and L. rhamnosus" in network["description"]
    assert "higher E. coli activity with P. vulgatus present" in hub["description"]
    assert "without an abundance change in that assay" in hub["description"]
    assert "not proof of direct two-member" in hub["description"]
    assert "did not differ between GOS and glucose" in hub["description"]
    assert all(ev["supports"] == "SUPPORT" for ev in hub["evidence"])
    assert [e["target"] for e in network["downstream"]] == [inhibition["name"]]
    assert all("not a demonstrated molecule transferred" in t["notes"] for t in hub["metabolites"])


def test_acid_challenge_is_positive_without_an_invented_ph_clamp():
    _, (_, doc, _) = records()
    node = doc["ecological_interactions"][2]
    assert "stronger inhibition" in node["description"]
    assert "E. coli less affected" in node["description"]
    assert "additive effects of pH and acid identity" in node["description"]
    assert "exact acid-challenge protocol is not in the main Methods" in node["description"]
    assert node["evidence"][0]["supports"] == "SUPPORT"
    assert (
        "selective lactate depletion/rescue"
        in doc["ecological_interactions"][0]["downstream"][0]["description"]
    )


def test_bacterial_traits_belong_to_the_measured_taxon_not_every_persister():
    _, (_, _, doc) = records()
    seeding, traits, persistence = doc["ecological_interactions"]
    assert "Bifidobacterium strains often lacked a maternal match" in seeding["description"]
    assert "12 Bifidobacterium persisters and 18 non-persisters" in traits["description"]
    assert [p["term"]["id"] for p in traits["biological_processes"]] == ["GO:0005975"]
    assert traits["evidence"][0]["evidence_source"] == "COMPUTATIONAL"
    assert traits["evidence"][0]["supports"] == "SUPPORT"
    assert "59 of 560" in persistence["description"]
    assert "month eight or later" in persistence["description"]
    assert "99.999 percent" in persistence["description"]
    assert "biological_processes" not in persistence
    assert "three persisters versus 25 non-persisters" in doc["discussions"][-1]["rationale"]


def test_all_retained_arrows_are_qualified_and_research_gaps_stay_open():
    ledger, docs = records()
    assert ledger["unresolved_research_issues"] == [1514, 1515]
    assert [r["status"] for r in ledger["records"]] == [
        "reviewed",
        "needs_research",
        "needs_research",
    ]
    all_edges = [
        e for d in docs for n in d["ecological_interactions"] for e in n.get("downstream", [])
    ]
    assert len(all_edges) == 5
    assert all(e["description"].startswith("PARTIAL - ") for e in all_edges)
    assert "PEA was below detection" in docs[1]["discussions"][-1]["rationale"]
    assert "#1514" in docs[1]["discussions"][-1]["rationale"]
    assert "#1515" in docs[2]["discussions"][-1]["rationale"]


def test_cache_appendix_preserves_prefix_and_short_primary_verified_quotes():
    ledger, _ = records()
    update = ledger["reference_cache_update"]
    raw = (ROOT / update["path"]).read_bytes()
    original, marker, extra = raw.partition(b"\n\n## Primary-Source Excerpts (2026-10-06)")
    assert marker and extra
    assert hashlib.sha256(original).hexdigest() == update["original_sha256"]
    assert hashlib.sha256(raw).hexdigest() == update["updated_sha256"]
    assert update["primary_xml_sha256"].encode() in extra
    assert b"not a complete full-text cache" in extra
    assert sum(len(q.split()) for q in update["verified_excerpts"]) == update["quoted_words"] == 16
    assert all(q.encode() in extra for q in update["verified_excerpts"])


def test_every_original_node_and_arrow_has_a_hash_bound_decision():
    ledger, docs = records()
    assert ledger["independent_approval"] is False
    assert ledger["issues"] == [1511, 1512, 1513]
    assert ledger["issue_deduplication"]["ignored_hidden_local_search"] is True
    for i, (row, doc) in enumerate(zip(ledger["records"], docs, strict=True)):
        nodes = doc["ecological_interactions"]
        names = {n["name"] for n in nodes}
        assert len(nodes) == [4, 3, 3][i]
        assert {d["node"] for d in row["node_decisions"]} == names
        assert row["removed_node_decisions"] == []
        assert len(row["edges_before"]) == [3, 2, 2][i]
        assert len(row["retained_edge_decisions"]) == [2, 1, 2][i]
        assert len(row["removed_edge_decisions"]) == [1, 1, 0][i]
        for n in nodes:
            assert all(e["target"] in names for e in n.get("downstream", []))
        assert all(
            a.split("#", 1)[1] in names for d in doc["discussions"] for a in d["attaches_to"]
        )
        assert hashlib.sha256((ROOT / row["path"]).read_bytes()).hexdigest() == row["record_sha256"]
        assert len(row["history_files"]) == 1 and (ROOT / row["history_files"][0]).is_file()
        assert doc["curation_history"][-1]["llm_assisted"] is True
