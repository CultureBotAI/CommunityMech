"""Pin source-system boundaries, model assumptions and the complete graph ledger."""

import hashlib
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "reports/causal_graph_review/decisions/20261006-three-records-batch56.yaml"


def records():
    ledger = yaml.safe_load(LEDGER.read_text())
    return ledger, [yaml.safe_load((ROOT / r["path"]).read_text()) for r in ledger["records"]]


def test_explicit_participants_preserve_exact_canonical_subsets():
    _, docs = records()
    scopes = [[[0, 1, 2], [0, 1], [2]], [[0, 2]] * 3, [[0, 1], [2, 3], [0, 1, 2, 3]]]
    for doc, subsets in zip(docs, scopes, strict=True):
        for node, indexes in zip(doc["ecological_interactions"], subsets, strict=True):
            assert node["scope"] == "COMMUNITY_LEVEL"
            assert not {"interaction_type", "source_taxon", "target_taxon"} & node.keys()
            assert node["participating_taxa"] == [
                {
                    "preferred_term": doc["taxonomy"][i]["taxon_term"]["preferred_term"],
                    "term": doc["taxonomy"][i]["taxon_term"]["term"],
                }
                for i in indexes
            ]
    denitrifiers = docs[2]["ecological_interactions"][1]["participating_taxa"]
    assert len({p["preferred_term"] for p in denitrifiers}) == 2
    assert {p["term"]["id"] for p in denitrifiers} == {"NCBITaxon:2689614"}


def test_kb1_retains_positive_cofactor_support_and_field_endpoint():
    _, (doc, _, _) = records()
    outcome, acetogen, _ = doc["ecological_interactions"]
    assert "ethene accounted" in outcome["description"]
    assert "consortium outcomes" in outcome["description"]
    assert "positive community experiments" in acetogen["description"]
    assert "DMB did not rescue" in acetogen["description"]
    assert "#1526" in acetogen["description"]
    arrow = acetogen["downstream"][0]
    assert arrow["target"] == outcome["name"]
    assert arrow["description"].startswith("PARTIAL - ")
    assert "separate field" in arrow["description"]
    assert all(e["supports"] == "SUPPORT" for e in acetogen["evidence"])


def test_sporomusa_positive_rescue_does_not_substitute_external_recipients():
    _, (doc, _, _) = records()
    sporo = doc["ecological_interactions"][2]
    assert "BAV1, GT and FL2" in sporo["description"]
    assert "restored partner dechlorination and growth" in sporo["description"]
    assert "FL2 still produced both VC and ethene" in sporo["description"]
    assert "donor only" in sporo["description"]
    assert "downstream" not in sporo
    assert all(p["term"]["id"] != "GO:0015889" for p in sporo["biological_processes"])


def test_rfmia_imposed_constraint_is_not_independent_rescue_or_measured_mutualism():
    _, (_, doc, _) = records()
    architecture, dependency, information = doc["ecological_interactions"]
    assert architecture["name"] == "Model-Architecture-Dependent Information Flow"
    assert "not observed niche partitioning" in architecture["description"]
    assert "Community models grew on dextrin" in dependency["description"]
    assert "manually set to zero" in dependency["description"]
    assert "not independently predicted partner rescue" in dependency["description"]
    assert "concentration" not in dependency["metabolites"][0]
    assert "computed information-theoretic outputs" in information["description"]
    for node in doc["ecological_interactions"]:
        assert "abstract names different pairs" in node["description"]
        assert "downstream" not in node and "biological_processes" not in node
        assert all(e["evidence_source"] == "COMPUTATIONAL" for e in node["evidence"])


def test_ort_nitrogen_completion_is_explicitly_gapfilled():
    _, (_, _, doc) = records()
    nitrification, denitrification, carbon = doc["ecological_interactions"]
    assert "Neither MAG encoded nitrogen-gas production" in denitrification["description"]
    assert "N2O-to-N2 reaction was added by gapfilling" in denitrification["description"]
    assert "dissolved nitrogen" in denitrification["description"]
    assert "not experimentally measured partner transfer" in nitrification["description"]
    assert "not assigned to every denitrifier" in carbon["description"]
    assert len(denitrification["metabolites"]) == 2
    assert all(
        "concentration" not in m
        for n in doc["ecological_interactions"]
        for m in n.get("metabolites", [])
    )
    for node in [nitrification, carbon]:
        arrow = node["downstream"][0]
        assert arrow["target"] == denitrification["name"]
        assert arrow["description"].startswith("PARTIAL - ")
    assert "no high-resolution empirical time series" in doc["discussions"][-1]["rationale"]


def test_every_original_node_and_arrow_has_exactly_one_decision():
    ledger, docs = records()
    assert ledger["independent_approval"] is False
    assert ledger["issues"] == [1523, 1524, 1525]
    assert ledger["unresolved_non_graph_issues"] == [1526, 1527, 1528]
    for index, (row, doc) in enumerate(zip(ledger["records"], docs, strict=True)):
        assert row["status"] == "reviewed"
        assert hashlib.sha256((ROOT / row["path"]).read_bytes()).hexdigest() == row["record_sha256"]
        assert len(row["node_decisions"]) + len(row["removed_node_decisions"]) == [3, 5, 3][index]
        names = {n["name"] for n in doc["ecological_interactions"]}
        assert {d["node"] for d in row["node_decisions"]} == names
        rename = row["renamed_nodes"]
        before = {
            (rename.get(e["source"], e["source"]), rename.get(e["target"], e["target"]))
            for e in row["edges_before"]
        }
        kept = {(e["source"], e["target"]) for e in row["retained_edge_decisions"]}
        removed = {
            (rename.get(e["source"], e["source"]), rename.get(e["target"], e["target"]))
            for e in row["removed_edge_decisions"]
        }
        assert before == kept | removed and not kept & removed
        assert len(kept) == [1, 0, 2][index]
        assert doc["curation_history"][-1]["llm_assisted"] is True
        for discussion in doc["discussions"]:
            assert discussion["status"] == "OPEN"
            assert all(a.split("#", 1)[1] in names for a in discussion["attaches_to"])


def test_source_scope_does_not_certify_mismatching_cache_provenance():
    ledger, _ = records()
    for path, digest in ledger["reference_cache_original_hashes"].items():
        assert hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == digest
    assert all(not r["source_review"]["cache_provenance_certified"] for r in ledger["records"])
    assert ledger["issue_deduplication"]["ignored_hidden_local_search"] is True
    assert "field abstract only" in ledger["records"][0]["source_review"]["scope"]
    assert "No code/supplement/model-rerun" in ledger["records"][1]["source_review"]["scope"]
    assert "no figure pixels" in ledger["records"][2]["source_review"]["scope"]
