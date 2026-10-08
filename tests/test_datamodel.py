"""Test that generated Python datamodel exists and community YAML is valid."""

from pathlib import Path

import yaml

# from linkml_runtime.loaders import yaml_loader
# from communitymech.datamodel.communitymech import MicrobialCommunity


def test_load_synechococcus_ecoli():
    """Test loading Synechococcus-E.coli SPC community with basic YAML."""
    yaml_file = Path("kb/communities/Synechococcus_Ecoli_SPC.yaml")
    assert yaml_file.exists(), f"Community file not found: {yaml_file}"

    # Load with plain YAML for now (LinkML runtime has issues with inlined objects)
    with open(yaml_file) as f:
        community = yaml.safe_load(f)

    # Verify basic fields
    assert community["name"] == "Synechococcus-E.coli Synthetic Photosynthetic Consortium"
    assert community["ecological_state"] == "ENGINEERED"

    # Verify taxonomy (2 organisms)
    assert len(community["taxonomy"]) == 2

    # Check first organism (Synechococcus)
    synecho = community["taxonomy"][0]
    assert synecho["taxon_term"]["preferred_term"] == "Synechococcus elongatus PCC 7942 cscB+"
    assert synecho["taxon_term"]["term"]["id"] == "NCBITaxon:32046"
    assert "PRIMARY_PRODUCER" in synecho["functional_role"]

    # Check second organism (E. coli)
    ecoli = community["taxonomy"][1]
    assert ecoli["taxon_term"]["preferred_term"] == "Escherichia coli W delta-cscR"
    assert ecoli["taxon_term"]["term"]["id"] == "NCBITaxon:562"
    assert "CROSS_FEEDER" in ecoli["functional_role"]

    # Verify interactions (3)
    assert len(community["ecological_interactions"]) == 3

    # Check first interaction
    interaction1 = community["ecological_interactions"][0]
    assert interaction1["name"] == "Photosynthetic carbon supply to E. coli"
    assert interaction1["interaction_type"] == "CROSS_FEEDING"
    assert interaction1["scope"] == "PAIRWISE"
    assert interaction1["source_taxon"]["term"]["id"] == "NCBITaxon:32046"
    assert interaction1["target_taxon"]["term"]["id"] == "NCBITaxon:562"
    assert len(interaction1["metabolites"]) == 1
    assert interaction1["metabolites"][0]["term"]["id"] == "CHEBI:17992"  # sucrose

    # Verify downstream edges
    assert len(interaction1["downstream"]) == 1
    target = interaction1["downstream"][0]["target"]
    assert target == "E. coli growth on cyanobacterial photosynthate"
    assert sum(n["name"] == target for n in community["ecological_interactions"]) == 1
    assert "PARTIAL for sucrose-specific mediation" in interaction1["downstream"][0]["description"]

    # Export capacity does not establish sucrose as the sole early-growth substrate.
    assert len(interaction1["evidence"]) == 2
    assert [e["supports"] for e in interaction1["evidence"]] == ["SUPPORT", "PARTIAL"]
    for evidence in interaction1["evidence"]:
        assert evidence["reference"] == "PMID:28127397"
        assert evidence["evidence_source"] == "IN_VITRO"
    assert "other metabolites" in interaction1["evidence"][1]["snippet"]

    # Verify environmental factors (3)
    assert len(community["environmental_factors"]) == 3
    factor_names = [f["name"] for f in community["environmental_factors"]]
    assert "Light" in factor_names
    assert "NaCl (Osmotic Pressure)" in factor_names
    assert "IPTG (Isopropyl β-D-1-thiogalactopyranoside)" in factor_names

    print("✅ All YAML structure tests passed!")


if __name__ == "__main__":
    test_load_synechococcus_ecoli()
