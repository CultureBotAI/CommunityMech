"""Tests for LLM context builder."""

import tempfile
from pathlib import Path

import pytest
import yaml

from communitymech.llm.context_builder import ContextBuilder


@pytest.fixture
def test_community():
    """Create a test community YAML structure."""
    return {
        "name": "Test AMD Community",
        "taxonomy": [
            {
                "taxon_term": {
                    "preferred_term": "Ferroplasma acidarmanus",
                    "term": {
                        "id": "NCBITaxon:55206",
                        "label": "Ferroplasma acidarmanus",
                    },
                },
                "functional_roles": [{"id": "GO:0055114", "label": "oxidation-reduction process"}],
                "abundance": {
                    "relative_abundance": 0.25,
                    "abundance_category": "dominant",
                },
            },
            {
                "taxon_term": {
                    "preferred_term": "Leptospirillum group II",
                    "term": {
                        "id": "NCBITaxon:1228",
                        "label": "Leptospirillum group II",
                    },
                },
                "functional_roles": [{"id": "GO:0019740", "label": "nitrogen fixation"}],
            },
            {
                "taxon_term": {
                    "preferred_term": "ARMAN",
                    "term": {"id": "NCBITaxon:123456", "label": "ARMAN"},
                },
            },
        ],
        "ecological_interactions": [
            {
                "name": "Iron Oxidation",
                "interaction_type": "MUTUALISM",
                "description": "Iron cycling",
                "source_taxon": {
                    "preferred_term": "Ferroplasma acidarmanus",
                    "term": {
                        "id": "NCBITaxon:55206",
                        "label": "Ferroplasma acidarmanus",
                    },
                },
                "target_taxon": {
                    "preferred_term": "Leptospirillum group II",
                    "term": {
                        "id": "NCBITaxon:1228",
                        "label": "Leptospirillum group II",
                    },
                },
                "metabolites_exchanged": [
                    {
                        "metabolite_term": {
                            "id": "CHEBI:29033",
                            "label": "iron(2+)",
                        },
                        "direction": "source_to_target",
                    }
                ],
                "biological_processes": [
                    {"id": "GO:0055114", "label": "oxidation-reduction process"}
                ],
            }
        ],
        "environmental_factors": {
            "habitat": [{"id": "ENVO:00002058", "label": "acid mine drainage"}],
            "physical_parameters": [
                {"parameter_type": "temperature", "value": "40", "unit": "°C"},
                {"parameter_type": "pH", "value": "2.0", "unit": ""},
            ],
            "chemical_parameters": [
                {
                    "parameter_type": "iron concentration",
                    "value": "500",
                    "unit": "mg/L",
                }
            ],
        },
    }


@pytest.fixture
def temp_community_file(test_community):
    """Create a temporary community YAML file."""
    with tempfile.NamedTemporaryFile(mode="w", suffix=".yaml", delete=False) as f:
        yaml.dump(test_community, f)
        path = Path(f.name)

    yield path

    # Cleanup
    path.unlink()


def test_context_builder_initialization(temp_community_file):
    """Test context builder initializes correctly."""
    builder = ContextBuilder(temp_community_file)

    assert builder.community_path == temp_community_file
    assert builder.data is not None
    assert builder.data["name"] == "Test AMD Community"


def test_build_disconnected_taxon_context(temp_community_file):
    """Test building context for disconnected taxon."""
    builder = ContextBuilder(temp_community_file)

    context = builder.build_disconnected_taxon_context(
        taxon_name="ARMAN", taxon_id="NCBITaxon:123456"
    )

    # Check basic fields
    assert context["community_name"] == "Test AMD Community"
    assert context["taxon_name"] == "ARMAN"
    assert context["taxon_id"] == "NCBITaxon:123456"

    # Check environmental context
    assert context["environment"] == "acid mine drainage"
    assert "temperature: 40 °C" in context["environmental_context"]
    assert "pH: 2.0" in context["environmental_context"]

    # Check connected taxa list
    assert "Ferroplasma acidarmanus" in context["connected_taxa"]
    assert "Leptospirillum group II" in context["connected_taxa"]
    assert "NCBITaxon:55206" in context["connected_taxa"]
    assert "NCBITaxon:1228" in context["connected_taxa"]

    # Check interaction summary
    assert "Total interactions: 1" in context["interaction_summary"]
    assert "MUTUALISM" in context["interaction_summary"]
    assert "iron(2+)" in context["interaction_summary"]


def test_build_environmental_context(temp_community_file):
    """Test building environmental context."""
    builder = ContextBuilder(temp_community_file)

    env_context = builder._build_environmental_context()

    assert env_context["environment"] == "acid mine drainage"
    assert "temperature: 40 °C" in env_context["environmental_context"]
    assert "pH: 2.0" in env_context["environmental_context"]
    assert "iron concentration: 500 mg/L" in env_context["environmental_context"]


def test_build_taxon_context(temp_community_file):
    """Test building taxon-specific context."""
    builder = ContextBuilder(temp_community_file)

    taxon_context = builder._build_taxon_context("Ferroplasma acidarmanus")

    assert "Functional Roles" in taxon_context
    assert "oxidation-reduction process" in taxon_context
    assert "Relative Abundance: 0.25" in taxon_context
    assert "Abundance Category: dominant" in taxon_context


def test_build_taxon_context_no_data(temp_community_file):
    """Test building context for taxon with minimal data."""
    builder = ContextBuilder(temp_community_file)

    taxon_context = builder._build_taxon_context("ARMAN")

    assert "No additional information available" in taxon_context


def test_build_connected_taxa_list(temp_community_file):
    """Test building list of connected taxa."""
    builder = ContextBuilder(temp_community_file)

    connected_list = builder._build_connected_taxa_list()

    assert "Ferroplasma acidarmanus (NCBITaxon:55206)" in connected_list
    assert "Leptospirillum group II (NCBITaxon:1228)" in connected_list
    assert "ARMAN" not in connected_list  # Not connected


def test_build_interaction_summary(temp_community_file):
    """Test building interaction summary."""
    builder = ContextBuilder(temp_community_file)

    summary = builder._build_interaction_summary()

    assert "Total interactions: 1" in summary
    assert "MUTUALISM: 1" in summary
    assert "iron(2+)" in summary
    assert "oxidation-reduction process" in summary


def test_build_missing_source_context(temp_community_file):
    """Test building context for missing source."""
    builder = ContextBuilder(temp_community_file)

    context = builder.build_missing_source_context(
        interaction_name="Iron Oxidation", interaction_index=0
    )

    assert context["community_name"] == "Test AMD Community"
    assert context["interaction_name"] == "Iron Oxidation"
    assert context["interaction_description"] == "Iron cycling"

    # Check available taxa
    assert "Ferroplasma acidarmanus (NCBITaxon:55206)" in context["available_taxa"]
    assert "Leptospirillum group II (NCBITaxon:1228)" in context["available_taxa"]
    assert "ARMAN (NCBITaxon:123456)" in context["available_taxa"]

    # Check interaction details
    assert "Type: MUTUALISM" in context["interaction_details"]
    assert "Target: Leptospirillum group II" in context["interaction_details"]


def test_build_unknown_target_context(temp_community_file):
    """Test building context for unknown target."""
    builder = ContextBuilder(temp_community_file)

    context = builder.build_unknown_target_context(
        interaction_name="Iron Oxidation", unknown_target="Mystery Bacterium"
    )

    assert context["community_name"] == "Test AMD Community"
    assert context["interaction_name"] == "Iron Oxidation"
    assert context["unknown_target"] == "Mystery Bacterium"
    assert "Ferroplasma acidarmanus (NCBITaxon:55206)" in context["available_taxa"]


def test_get_all_taxa(temp_community_file):
    """Test getting all taxa."""
    builder = ContextBuilder(temp_community_file)

    taxa = builder.get_all_taxa()

    assert len(taxa) == 3
    assert {"name": "Ferroplasma acidarmanus", "id": "NCBITaxon:55206"} in taxa
    assert {"name": "Leptospirillum group II", "id": "NCBITaxon:1228"} in taxa
    assert {"name": "ARMAN", "id": "NCBITaxon:123456"} in taxa


def test_get_connected_taxa(temp_community_file):
    """Test getting connected taxa."""
    builder = ContextBuilder(temp_community_file)

    connected = builder.get_connected_taxa()

    assert "Ferroplasma acidarmanus" in connected
    assert "Leptospirillum group II" in connected
    assert "ARMAN" not in connected  # Not in any interactions


def test_no_interactions(temp_community_file, test_community):
    """Test context building with no interactions."""
    # Modify community to have no interactions
    test_community["ecological_interactions"] = []

    with tempfile.NamedTemporaryFile(mode="w", suffix=".yaml", delete=False) as f:
        yaml.dump(test_community, f)
        path = Path(f.name)

    try:
        builder = ContextBuilder(path)

        connected = builder._build_connected_taxa_list()
        assert "No connected taxa" in connected

        summary = builder._build_interaction_summary()
        assert "No interactions yet" in summary

    finally:
        path.unlink()


def test_missing_environmental_factors(temp_community_file, test_community):
    """Test context building with missing environmental factors."""
    # Remove environmental factors
    del test_community["environmental_factors"]

    with tempfile.NamedTemporaryFile(mode="w", suffix=".yaml", delete=False) as f:
        yaml.dump(test_community, f)
        path = Path(f.name)

    try:
        builder = ContextBuilder(path)

        env_context = builder._build_environmental_context()
        assert env_context["environment"] == "Unknown environment"
        assert "No specific parameters" in env_context["environmental_context"]

    finally:
        path.unlink()
