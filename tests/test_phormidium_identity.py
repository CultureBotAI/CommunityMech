"""Keep the cyanobacterial member distinct from the unrelated legacy taxon (#2009)."""

from pathlib import Path
import xml.etree.ElementTree as ET

import yaml

ROOT = Path(__file__).resolve().parents[1]
SPECIES = {"id": "NCBITaxon:3723519", "label": "Candidatus Sodalinema alkaliphilum"}
SOURCE_NAME = "Candidatus Phormidium alkaliphilum"


def test_phormidium_member_and_graph_references_share_the_correct_species():
    doc = yaml.safe_load((ROOT / "kb/communities/Phormidium_Alkaline_Consortium.yaml").read_text())
    nodes = doc["ecological_interactions"]
    descriptors = [doc["taxonomy"][0]["taxon_term"], nodes[1]["participating_taxa"][0]]
    descriptors.extend(nodes[i]["source_taxon"] for i in (0, 2, 3))
    assert doc["id"] == "CommunityMech:000054"
    assert len(descriptors) == 5
    assert all(d["term"] == SPECIES and d["preferred_term"] == SOURCE_NAME for d in descriptors)
    assert "strain_designation" not in doc["taxonomy"][0]
    assert "species-level" in descriptors[0]["notes"]
    assert "2839084" in descriptors[0]["notes"]
    assert any("only cyanobacterium" in e["snippet"] for e in doc["taxonomy"][0]["evidence"])


def test_wrong_organism_is_not_waived_on_canonical_or_export_surfaces():
    config = yaml.safe_load((ROOT / "conf/id_label_targets.yaml").read_text())
    targets = {t["name"]: t for t in config["targets"]}
    for name in ("communities_yaml", "kgx_nodes"):
        assert all(e["id"] != "NCBITaxon:1807132" for e in targets[name]["exceptions"])


def test_archived_taxonomy_distinguishes_species_strain_and_wrong_legacy_id():
    path = (
        ROOT
        / "reports/causal_graph_review/sources/20261015-phormidium-identity-batch132/ncbi-taxonomy.xml"
    )
    taxa = {t.findtext("TaxId"): t for t in ET.parse(path).getroot().findall("Taxon")}
    species, strain, unrelated = (taxa[n] for n in ("3723519", "2839084", "2293317"))
    assert species.findtext("ScientificName") == SPECIES["label"]
    assert species.findtext("Rank") == "species"
    assert SOURCE_NAME in [n.text for n in species.findall("OtherNames/Synonym")]
    assert strain.findtext("ParentTaxId") == "3723519" and strain.findtext("Rank") == "strain"
    assert unrelated.findtext("ScientificName") == "Candidatus Syntrophocurvum alkaliphilum"
    assert "1807132" in [n.text for n in unrelated.findall("AkaTaxIds/TaxId")]
