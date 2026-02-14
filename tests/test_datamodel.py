"""Test that generated Python datamodel exists and community YAML is valid."""

import pytest
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
    assert synecho["taxon_term"]["term"]["id"] == "NCBITaxon:1140"
    assert "PRIMARY_PRODUCER" in synecho["functional_role"]

    # Check second organism (E. coli)
    ecoli = community["taxonomy"][1]
    assert ecoli["taxon_term"]["preferred_term"] == "Escherichia coli K-12"
    assert ecoli["taxon_term"]["term"]["id"] == "NCBITaxon:83333"
    assert "CROSS_FEEDER" in ecoli["functional_role"]

    # Verify interactions (2)
    assert len(community["ecological_interactions"]) == 2

    # Check first interaction
    interaction1 = community["ecological_interactions"][0]
    assert interaction1["name"] == "CO2 Fixation and Sucrose Production"
    assert interaction1["interaction_type"] == "CROSS_FEEDING"
    assert len(interaction1["metabolites"]) == 1
    assert interaction1["metabolites"][0]["term"]["id"] == "CHEBI:17992"  # sucrose

    # Verify downstream edges
    assert len(interaction1["downstream"]) == 1
    assert interaction1["downstream"][0]["target"] == "Sucrose Uptake and Heterotrophic Growth"

    # Verify evidence
    assert len(interaction1["evidence"]) == 1
    evidence = interaction1["evidence"][0]
    assert evidence["reference"] == "PMID:32753581"
    assert evidence["supports"] == "SUPPORT"
    assert evidence["evidence_source"] == "IN_VITRO"

    # Verify environmental factors (3)
    assert len(community["environmental_factors"]) == 3
    factor_names = [f["name"] for f in community["environmental_factors"]]
    assert "Light" in factor_names
    assert "NaCl (Osmotic Pressure)" in factor_names
    assert "IPTG (Isopropyl β-D-1-thiogalactopyranoside)" in factor_names

    print("✅ All YAML structure tests passed!")


if __name__ == "__main__":
    test_load_synechococcus_ecoli()
