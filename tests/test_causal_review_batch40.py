"""Keep observed responses distinct from inferred causal mediation."""

import hashlib
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "reports/causal_graph_review/decisions/20261006-three-records-batch40.yaml"


def records():
    ledger = yaml.safe_load(LEDGER.read_text())
    return ledger, [yaml.safe_load((ROOT / r["path"]).read_text()) for r in ledger["records"]]


def test_electrosynthetic_routes_remain_partial_not_contact_only():
    _, docs = records()
    biofilm, planktonic, output = docs[0]["ecological_interactions"]
    for node in [biofilm, planktonic]:
        assert node["description"].startswith("PARTIAL:")
        assert node["evidence"][0]["supports"] == "PARTIAL"
        assert node["downstream"][0]["target"] == output["name"]
        assert node["downstream"][0]["description"].startswith("PARTIAL:")
    assert "diffusible mediator" in biofilm["description"]
    assert "selective cytochrome necessity" in biofilm["description"]
    assert "hydrogen was detected in both" in planktonic["description"]
    assert "not cumulative mass-balanced flux fractions" in planktonic["description"]
    assert all("interaction_type" not in n for n in [biofilm, planktonic, output])


def test_electrosynthetic_output_roster_is_alternative_pairs():
    _, docs = records()
    output = docs[0]["ecological_interactions"][2]
    assert len(output["participating_taxa"]) == 3
    assert "not one three-member community" in output["description"]
    assert "acetogens were alternatives" in output["description"]
    assert "applied cell voltage" in output["description"]
    assert "not voltage-only" in output["description"]
    assert "1.16 g/L versus 0.62 g/L" in output["description"]
    assert docs[0]["taxonomy"][1]["taxon_term"]["term"]["label"] == "Andreesenella acetica"


def test_emiliania_removes_workflow_and_precursor_biosynthesis_claim():
    _, docs = records()
    nutrients, tryptophan, response = docs[1]["ecological_interactions"]
    assert "downstream" not in nutrients
    assert nutrients["interaction_type"] == "CROSS_FEEDING"
    assert "rosettes rather than single cells" in nutrients["description"]
    assert "CFU may include rosettes" in nutrients["evidence"][-1]["snippet"]
    assert all("biological_processes" not in n for n in [nutrients, tryptophan])
    assert "not a community member" in tryptophan["description"]
    assert tryptophan["downstream"][0]["target"] == response["name"]
    assert tryptophan["downstream"][0]["description"].startswith("HYPOTHESIZED:")
    assert len(docs[1]["taxonomy"]) == 2


def test_emiliania_iaa_exposure_and_necessity_are_unresolved():
    _, docs = records()
    response = docs[1]["ecological_interactions"][2]
    assert "Proposed IAA Mediation" in response["name"]
    assert "interaction_type" not in response
    assert "not measured coculture exposures" in response["description"]
    assert "IAA was undetectable in coculture" in response["description"]
    assert "mutants still produced IAA" in response["description"]
    assert response["evidence"][0]["supports"] == "PARTIAL"
    assert "94% dead in coculture versus 21%" in response["description"]
    assert "not establish IAA necessity" in response["description"]
    assert "CCMP372 cannot be assigned to CCMP3266" in docs[1]["discussions"][-1]["rationale"]


def test_gut_net_inference_is_not_measured_all_to_all_mutualism():
    _, docs = records()
    exchange, shift, evenness = docs[2]["ecological_interactions"]
    assert "not complete measured all-to-all transfer" in exchange["description"]
    assert "B. fragilis was not rescued" in exchange["description"]
    assert [p["term"]["id"] for p in exchange["biological_processes"]] == ["GO:0008652"]
    assert "interaction_type" not in shift and "interaction_type" not in evenness
    assert "model-inferred net effects" in shift["description"]
    assert shift["evidence"][-1]["evidence_source"] == "COMPUTATIONAL"
    assert (
        "in-vitro network inference does not measure in-vivo exchange"
        in shift["downstream"][0]["description"]
    )
    assert docs[2]["taxonomy"][3]["taxon_term"]["gtdb_grounding_status"] == "AMBIGUOUS"


def test_gut_evenness_is_a_diet_specific_composition_endpoint():
    _, docs = records()
    evenness = docs[2]["ecological_interactions"][2]
    assert "day-10 fecal strain-specific DNA-qPCR" in evenness["description"]
    assert "standard-diet trend was not statistically significant" in evenness["description"]
    assert "not longitudinal stability" in evenness["description"]
    assert "does not directly measure amino-acid flux" in evenness["description"]
    assert evenness["evidence"][-1]["evidence_source"] == "IN_VIVO"


def test_batch40_complete_dispositions_canonical_participants_and_history():
    ledger, docs = records()
    assert ledger["independent_approval"] is False
    assert ledger["issues"] == [1452, 1453, 1454]
    assert ledger["open_nongraph_followups"] == [1455, 1456, 1457]
    assert sum(len(r["node_decisions"]) for r in ledger["records"]) == 9
    assert sum(len(r["retained_edge_decisions"]) for r in ledger["records"]) == 5
    assert sum(len(r["removed_edge_decisions"]) for r in ledger["records"]) == 1
    for row, doc in zip(ledger["records"], docs, strict=True):
        assert hashlib.sha256((ROOT / row["path"]).read_bytes()).hexdigest() == row["record_sha256"]
        assert row["status"] == "reviewed"
        assert len(row["history_files"]) == 1
        assert (ROOT / row["history_files"][0]).is_file()
        assert doc["curation_history"][-1]["llm_assisted"] is True
        canonical = {t["taxon_term"]["term"]["id"]: t["taxon_term"] for t in doc["taxonomy"]}
        names = {n["name"] for n in doc["ecological_interactions"]}
        for node in doc["ecological_interactions"]:
            participants = node.get("participating_taxa", [])
            participants += [node[k] for k in ["source_taxon", "target_taxon"] if k in node]
            for term in participants:
                assert term["term"] == canonical[term["term"]["id"]]["term"]
            assert all(
                e["target"] in names and e["target"] != node["name"]
                for e in node.get("downstream", [])
            )
        assert all(a.split("#", 1)[1] in names for a in doc["discussions"][-1]["attaches_to"])


def test_batch40_preserves_original_aliases_and_source_access_limits():
    ledger, _ = records()
    text = (ROOT / ledger["records"][1]["path"]).read_text()
    assert "&coculture_design" in text and "*coculture_design" in text
    for path, expected in ledger["reference_cache_original_hashes"].items():
        assert hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == expected
    assert ledger["edison"]["status"] == "not_required_for_existing_structure_repairs"
    assert "no provider job or spend" in ledger["edison"]["rationale"]
    assert all(
        "No figure images, separate supplements or raw data reviewed"
        in next(iter(r["source_review"].values()))["scope"]
        for r in ledger["records"]
    )
