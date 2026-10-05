"""Keep supported mutualisms while separating assay contexts and IAA roles."""

import hashlib
from collections import Counter
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "reports/causal_graph_review/decisions/20261005-four-records-batch11.yaml"


def record(stem):
    return yaml.safe_load((ROOT / "kb/communities" / f"{stem}.yaml").read_text())


def test_bl6_keeps_host_phenotype_without_competition_or_strain_persistence():
    doc = record("Chicken_BL6_AntiSalmonella_SynCom")
    node = doc["ecological_interactions"][0]
    assert len(doc["ecological_interactions"]) == 1
    assert "interaction_type" not in node and not node.get("downstream")
    assert "day 7, not day 14" in node["description"]
    assert "not direct permeability measurements" in node["description"]
    assert "does not establish persistence" in node["description"]
    assert len(doc["taxonomy"]) == 6
    assert all(e["evidence_source"] == "IN_VIVO" for e in node["evidence"])
    assert any(
        d["discussion_id"] == "bl6_protection_mediators_and_strain_persistence"
        and d["status"] == "OPEN"
        for d in doc["discussions"]
    )


def test_cdg_keeps_partial_staging_not_bulk_endpoint_partitioning():
    doc = record("Chinese_Distillers_Grains_Dual_Fungal_Lignin_Consortium")
    temporal, endpoint = doc["ecological_interactions"]
    assert temporal["interaction_type"] == "NICHE_PARTITIONING"
    assert temporal["description"].startswith("PARTIAL")
    assert "not measured population dominance" in temporal["description"]
    assert all(e["supports"] == "PARTIAL" for e in temporal["evidence"])
    assert "interaction_type" not in endpoint
    assert "58.66%" in endpoint["description"]
    assert "day 10" in endpoint["description"] and "day 15" in endpoint["description"]
    assert not any(n.get("downstream") for n in (temporal, endpoint))
    assert doc["engineering_design"]["evidence"][1]["supports"] == "SUPPORT"
    assert any(
        d["discussion_id"] == "cdg_dual_fungal_strains_and_conditions" for d in doc["discussions"]
    )
    assert [f["name"] for f in doc["environmental_factors"]] == [
        "Chinese Distillers' grains solid substrate"
    ]


def test_hydrogen_keeps_pair_mutualism_and_condition_specific_arrows():
    output, pair, community = record("Chlamydomonas_Bacterial_H2_Consortium")[
        "ecological_interactions"
    ]
    assert "interaction_type" not in output and "interaction_type" not in community
    assert pair["interaction_type"] == "MUTUALISM"
    assert "did not support algal growth" in pair["description"]
    assert "non-H2-producing aerobiosis" in pair["description"]
    assert any("alga complemented" in e["snippet"] for e in pair["evidence"])
    assert pair["downstream"][0]["description"].startswith("HYPOTHESIZED")
    assert pair["downstream"][0]["target"] == output["name"]
    assert community["downstream"][0]["target"] == output["name"]
    assert (
        "does not establish the necessity of every member"
        in community["downstream"][0]["description"]
    )
    assert "CHEBI:15379" not in {m["term"]["id"] for m in output["metabolites"]}
    assert community["participating_taxa"][1]["term"] == {
        "id": "NCBITaxon:40323",
        "label": "Stenotrophomonas",
    }


def test_methylobacterium_corrects_iaa_source_and_preserves_real_mutualisms():
    carbon, degradation, phenotype = record("Chlamydomonas_Methylobacterium_Mutualism")[
        "ecological_interactions"
    ]
    assert carbon["interaction_type"] == degradation["interaction_type"] == "MUTUALISM"
    assert "interaction_type" not in phenotype
    assert carbon["metabolites"][0]["term"] == {"id": "CHEBI:17754", "label": "glycerol"}
    assert len(carbon["metabolites"]) == 1
    assert "CC-1690" in carbon["description"] and "CYB/proline" in carbon["description"]
    assert "CC-5325" in degradation["description"]
    assert "bacterial IAA production is not established" in degradation["description"]
    assert "Salkowski assay measures indoles" in degradation["description"]
    assert "GO:0009684" not in {p["term"]["id"] for p in degradation["biological_processes"]}
    assert all(e["reference"] == "PMID:38269098" for e in degradation["evidence"])
    assert all(e["reference"] == "PMID:38269098" for e in phenotype["evidence"])
    assert carbon["downstream"][0]["target"] == degradation["name"]
    assert carbon["downstream"][0]["description"].startswith("HYPOTHESIZED")
    assert "acetate-containing T-N" in carbon["downstream"][0]["description"]
    assert degradation["downstream"][0]["target"] == phenotype["name"]
    assert degradation["downstream"][0]["description"].startswith("PARTIAL")
    assert "chlorophyll degradation" in phenotype["description"]


def test_added_auxin_cache_has_provenance_license_and_explicit_excerpt_scope():
    text = (ROOT / "references_cache/PMID_38269098.md").read_text()
    metadata = yaml.safe_load(text.split("---", 2)[1])
    assert metadata["reference_id"] == "PMID:38269098"
    assert metadata["doi"] == "10.1016/j.isci.2023.108762"
    assert metadata["license"] == "CC BY 4.0"
    assert metadata["license_url"] == "https://creativecommons.org/licenses/by/4.0/"
    assert len(metadata["authors"]) == 6
    assert "not a complete article transcription" in text
    assert len(metadata["source_xml_sha256"]) == 64
    nodes = record("Chlamydomonas_Methylobacterium_Mutualism")["ecological_interactions"]
    for node in nodes:
        for evidence in node["evidence"]:
            if evidence["reference"] == "PMID:38269098":
                assert " ".join(evidence["snippet"].split()) in " ".join(text.split())


def test_batch11_hash_bound_decisions_cover_every_node_and_arrow():
    rows = yaml.safe_load(LEDGER.read_text())["records"]
    assert len(rows) == 4
    assert Counter(r["status"] for r in rows) == {"reviewed": 4}
    assert sum(len(r["node_decisions"]) for r in rows) == 9
    assert sum(len(r["retained_edge_decisions"]) for r in rows) == 4
    for row in rows:
        raw = (ROOT / row["path"]).read_bytes()
        assert hashlib.sha256(raw).hexdigest() == row["record_sha256"]
        doc = yaml.safe_load(raw)
        nodes = doc["ecological_interactions"]
        assert Counter(d["node"] for d in row["node_decisions"]) == Counter(
            n["name"] for n in nodes
        )
        edges = [{"source": n["name"], **e} for n in nodes for e in n.get("downstream", [])]
        assert row["edges_after"] == edges
        assert {(e["source"], e["target"]) for e in edges} == {
            (d["source"], d["target"]) for d in row["retained_edge_decisions"]
        }
        assert not row["removed_edge_decisions"]
        assert row["non_graph_followups"]["issue"].startswith("https://github.com/CultureBotAI/")
