"""Keep phage treatment outcomes, mediation and model diagnostics distinct."""

import hashlib
import subprocess
from copy import deepcopy
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]
BASE = "b68d71e702200cd7ce9afdec001705dc8b0890fd"
ALSETH = "kb/communities/Alseth_FourSpecies_Pathogen_Phage_Community.yaml"
PHA = "kb/communities/PHA_MixedCulture_Phage_Succession_Community.yaml"
MODEL = "Model-Inferred Context Dependence of Community Interactions"
MODEL_QUOTES = (
    "reasonably fit the data in the absence of phage",
    "the interaction coefficients did not generalise quantitatively to 4-species data",
)


def contract(doc):
    nodes = doc["ecological_interactions"]
    assert len(nodes) == 5
    assert nodes[0]["interaction_type"] == "LYTIC_INFECTION"
    assert nodes[0]["scope"] == "PAIRWISE"
    assert nodes[1]["interaction_type"] == "COMPETITIVE_RELEASE"
    assert all("interaction_type" not in node for node in nodes[2:])
    assert "phenotype-based classification" in nodes[2]["description"]
    assert "were not sequenced in this study" in nodes[2]["description"]
    assert "were not sequenced in this study" in doc["description"]
    assert nodes[2]["evidence"][-1]["snippet"] == (
        "Further sequencing of receptor mutants was not done"
    )
    edges = [
        (node["name"], edge["target"]) for node in nodes for edge in node.get("downstream", [])
    ]
    assert edges == [
        (nodes[0]["name"], nodes[1]["name"]),
        (nodes[0]["name"], nodes[2]["name"]),
        (nodes[1]["name"], nodes[3]["name"]),
    ]
    assert nodes[0]["downstream"][1]["description"].startswith("PARTIAL:")
    assert "does not" in nodes[0]["downstream"][1]["description"]
    assert nodes[1]["downstream"][0]["description"].startswith("PARTIAL:")
    assert "necessary or sufficient mediator" in nodes[1]["downstream"][0]["description"]
    assert nodes[4]["name"] == MODEL
    assert nodes[4]["description"].startswith("PARTIAL:")
    assert "absence of phage" in nodes[4]["description"]
    assert "failed to generalize quantitatively" in nodes[4]["description"]
    assert "not reconstructible" not in doc["description"]
    assert all(e["evidence_source"] == "COMPUTATIONAL" for e in nodes[4]["evidence"])
    assert all(e["supports"] == "PARTIAL" for e in nodes[4]["evidence"][:2])
    assert {e["snippet"] for e in nodes[4]["evidence"][2:]} == set(MODEL_QUOTES)
    discussions = {d["discussion_id"]: d for d in doc["discussions"]}
    gap = discussions["alseth_diversity_mediation_unresolved"]
    assert gap["status"] == "OPEN" and gap["kind"] == "KNOWLEDGE_GAP"
    assert gap["evidence"][0]["supports"] == "PARTIAL"
    names = {node["name"] for node in nodes}
    for discussion in doc["discussions"]:
        for anchor in discussion.get("attaches_to", []):
            if anchor.startswith("ecological_interactions#"):
                assert anchor.split("#", 1)[1] in names


def test_alseth_graph_semantics():
    contract(yaml.safe_load((ROOT / ALSETH).read_text()))


@pytest.mark.parametrize(
    "mutation",
    [
        "infection_type",
        "competition_type",
        "genotype_overclaim",
        "cost_arrow",
        "diversity_arrow",
        "model_condition",
        "model_quote",
        "model_modality",
        "model_certainty",
        "reversed_arrow",
        "missing_node",
        "dangling_anchor",
    ],
)
def test_control_mutation_and_immediate_restoration(mutation):
    original = yaml.safe_load((ROOT / ALSETH).read_text())
    contract(original)
    changed = deepcopy(original)
    nodes = changed["ecological_interactions"]
    if mutation == "infection_type":
        nodes[3]["interaction_type"] = "LYTIC_INFECTION"
    elif mutation == "competition_type":
        nodes[2]["interaction_type"] = "COMPETITION"
    elif mutation == "genotype_overclaim":
        nodes[2]["description"] = "Specific resistance genotypes were sequenced."
    elif mutation == "cost_arrow":
        nodes[0]["downstream"][1]["description"] = "Receptor targeting causes the fitness cost."
    elif mutation == "diversity_arrow":
        nodes[1]["downstream"][0]["description"] = "Release is the established diversity mechanism."
    elif mutation == "model_condition":
        nodes[4]["description"] = "The fitted model predicts four-species dynamics."
    elif mutation == "model_quote":
        nodes[4]["evidence"][2]["snippet"] = "Invented model success"
    elif mutation == "model_modality":
        nodes[4]["evidence"][0]["evidence_source"] = "IN_VITRO"
    elif mutation == "model_certainty":
        nodes[4]["evidence"][0]["supports"] = "SUPPORT"
    elif mutation == "reversed_arrow":
        nodes[0]["downstream"][0]["target"] = nodes[0]["name"]
    elif mutation == "missing_node":
        nodes.pop()
    else:
        changed["discussions"][0]["attaches_to"] = ["ecological_interactions#missing"]
    assert changed != original
    with pytest.raises(AssertionError):
        contract(changed)
    contract(original)


def test_unreviewed_fields_pha_and_article_caches_are_preserved():
    original = yaml.safe_load(
        subprocess.check_output(["git", "show", f"{BASE}:{ALSETH}"], cwd=ROOT)
    )
    current = yaml.safe_load((ROOT / ALSETH).read_text())
    allowed = {"description", "ecological_interactions", "discussions", "curation_history"}
    assert {k: v for k, v in original.items() if k not in allowed} == {
        k: v for k, v in current.items() if k not in allowed
    }
    assert current["curation_history"][-1]["curator"] == "codex"
    assert current["curation_history"][-1]["llm_assisted"] is True
    for path, expected in {
        PHA: "aebd6497b6d5a6f49e9e9ef956d4ec0847960acc0fd2413dce5e0960ed748488",
        "references_cache/PMID_38648198.txt": (
            "babc54ddb60c3ed882e817d1970ff9c7ba24069b0b06d67730e12eb974b58df3"
        ),
        "references_cache/PMID_40152616.txt": (
            "65e30e4f8aed4b1c7cde1fb173376207bbf90d92306c7f59997fd41bfeddbe8b"
        ),
    }.items():
        assert hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == expected


def test_saved_graph_decisions_cover_both_records():
    rel = "reports/causal_graph_review/decisions/20261014-phage-graphs-batch130.yaml"
    ledger = yaml.safe_load((ROOT / rel).read_text())
    assert ledger["independent_approval"] is False
    assert {r["path"] for r in ledger["records"]} == {ALSETH, PHA}
    for row in ledger["records"]:
        raw = (ROOT / row["path"]).read_bytes()
        doc = yaml.safe_load(raw)
        assert row["status"] == "reviewed"
        assert row["record_sha256"] == hashlib.sha256(raw).hexdigest()
        assert [d["node"] for d in row["node_decisions"]] == [
            n["name"] for n in doc["ecological_interactions"]
        ]
        edges = [
            {"source": node["name"], **edge}
            for node in doc["ecological_interactions"]
            for edge in node.get("downstream", [])
        ]
        assert row["edges_after"] == edges
        assert len(row["retained_edge_decisions"]) == len(edges)
        assert all(d["rationale"] and d["source_locator"] for d in row["node_decisions"])
