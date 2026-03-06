"""Tests for repair strategies."""

import tempfile
from pathlib import Path
from unittest.mock import MagicMock

import pytest
import yaml

from communitymech.network.auditor import IssueType
from communitymech.network.repair_strategies import (
    DisconnectedTaxonStrategy,
    MissingSourceStrategy,
    StrategySelector,
    UnknownSourceStrategy,
    UnknownTargetStrategy,
)
from communitymech.network.validators import SuggestionValidator


@pytest.fixture
def test_community():
    """Create a test community."""
    return {
        "name": "Test Community",
        "taxonomy": [
            {
                "taxon_term": {
                    "preferred_term": "Escherichia coli",
                    "term": {"id": "NCBITaxon:562", "label": "Escherichia coli"},
                }
            },
            {
                "taxon_term": {
                    "preferred_term": "Pseudomonas aeruginosa",
                    "term": {"id": "NCBITaxon:287", "label": "Pseudomonas aeruginosa"},
                }
            },
            {
                "taxon_term": {
                    "preferred_term": "Disconnected taxon",
                    "term": {"id": "NCBITaxon:999", "label": "Disconnected taxon"},
                }
            },
        ],
        "ecological_interactions": [
            {
                "name": "Test Interaction",
                "interaction_type": "MUTUALISM",
                "description": "Test",
                "source_taxon": {
                    "preferred_term": "Escherichia coli",
                    "term": {"id": "NCBITaxon:562", "label": "Escherichia coli"},
                },
                "target_taxon": {
                    "preferred_term": "Pseudomonas aeruginosa",
                    "term": {"id": "NCBITaxon:287", "label": "Pseudomonas aeruginosa"},
                },
            }
        ],
        "environmental_factors": {
            "habitat": [{"id": "ENVO:00002001", "label": "freshwater"}],
            "physical_parameters": [
                {"parameter_type": "temperature", "value": "25", "unit": "°C"}
            ],
        },
    }


@pytest.fixture
def temp_community_file(test_community):
    """Create temporary community file."""
    with tempfile.NamedTemporaryFile(mode="w", suffix=".yaml", delete=False) as f:
        yaml.dump(test_community, f)
        path = Path(f.name)

    yield path

    # Cleanup
    path.unlink()


@pytest.fixture
def validator():
    """Create mock validator."""
    return SuggestionValidator(
        validate_evidence=False, validate_ontology=False, check_plausibility=False
    )


def test_disconnected_taxon_strategy_can_handle(temp_community_file, validator):
    """Test DisconnectedTaxonStrategy handles DISCONNECTED issues."""
    strategy = DisconnectedTaxonStrategy(temp_community_file, validator)

    disconnected_issue = {
        "type": IssueType.DISCONNECTED,
        "taxon": "Disconnected taxon",
        "taxon_id": "NCBITaxon:999",
    }

    assert strategy.can_handle(disconnected_issue) is True

    other_issue = {"type": IssueType.MISSING_SOURCE}
    assert strategy.can_handle(other_issue) is False


def test_disconnected_taxon_strategy_build_context(temp_community_file, validator):
    """Test DisconnectedTaxonStrategy builds context."""
    strategy = DisconnectedTaxonStrategy(temp_community_file, validator)

    issue = {
        "type": IssueType.DISCONNECTED,
        "taxon": "Disconnected taxon",
        "taxon_id": "NCBITaxon:999",
    }

    context = strategy.build_context(issue)

    # Check required context fields
    assert "community_name" in context
    assert "taxon_name" in context
    assert "taxon_id" in context
    assert "environment" in context
    assert "connected_taxa" in context
    assert "interaction_summary" in context

    assert context["taxon_name"] == "Disconnected taxon"
    assert context["taxon_id"] == "NCBITaxon:999"


def test_disconnected_taxon_strategy_missing_fields(temp_community_file, validator):
    """Test DisconnectedTaxonStrategy raises on missing fields."""
    strategy = DisconnectedTaxonStrategy(temp_community_file, validator)

    invalid_issue = {"type": IssueType.DISCONNECTED}  # Missing taxon and taxon_id

    with pytest.raises(ValueError, match="missing required fields"):
        strategy.build_context(invalid_issue)


def test_missing_source_strategy_can_handle(temp_community_file, validator):
    """Test MissingSourceStrategy handles MISSING_SOURCE issues."""
    strategy = MissingSourceStrategy(temp_community_file, validator)

    missing_source_issue = {
        "type": IssueType.MISSING_SOURCE,
        "interaction": "Test Interaction",
        "interaction_index": 0,
    }

    assert strategy.can_handle(missing_source_issue) is True

    other_issue = {"type": IssueType.DISCONNECTED}
    assert strategy.can_handle(other_issue) is False


def test_missing_source_strategy_build_context(temp_community_file, validator):
    """Test MissingSourceStrategy builds context."""
    strategy = MissingSourceStrategy(temp_community_file, validator)

    issue = {
        "type": IssueType.MISSING_SOURCE,
        "interaction": "Test Interaction",
        "interaction_index": 0,
    }

    context = strategy.build_context(issue)

    # Check required context fields
    assert "community_name" in context
    assert "interaction_name" in context
    assert "interaction_description" in context
    assert "available_taxa" in context
    assert "interaction_details" in context

    assert context["interaction_name"] == "Test Interaction"


def test_unknown_target_strategy_can_handle(temp_community_file, validator):
    """Test UnknownTargetStrategy handles UNKNOWN_TARGET issues."""
    strategy = UnknownTargetStrategy(temp_community_file, validator)

    unknown_target_issue = {
        "type": IssueType.UNKNOWN_TARGET,
        "interaction": "Test Interaction",
        "taxon": "Unknown bacterium",
    }

    assert strategy.can_handle(unknown_target_issue) is True

    other_issue = {"type": IssueType.MISSING_SOURCE}
    assert strategy.can_handle(other_issue) is False


def test_unknown_target_strategy_build_context(temp_community_file, validator):
    """Test UnknownTargetStrategy builds context."""
    strategy = UnknownTargetStrategy(temp_community_file, validator)

    issue = {
        "type": IssueType.UNKNOWN_TARGET,
        "interaction": "Test Interaction",
        "taxon": "Unknown bacterium",
    }

    context = strategy.build_context(issue)

    # Check required context fields
    assert "community_name" in context
    assert "interaction_name" in context
    assert "unknown_target" in context
    assert "available_taxa" in context

    assert context["unknown_target"] == "Unknown bacterium"


def test_unknown_source_strategy_can_handle(temp_community_file, validator):
    """Test UnknownSourceStrategy handles UNKNOWN_SOURCE issues."""
    strategy = UnknownSourceStrategy(temp_community_file, validator)

    unknown_source_issue = {
        "type": IssueType.UNKNOWN_SOURCE,
        "interaction": "Test Interaction",
        "taxon": "Unknown bacterium",
    }

    assert strategy.can_handle(unknown_source_issue) is True


def test_strategy_selector_select_strategy(temp_community_file, validator):
    """Test StrategySelector selects correct strategy."""
    selector = StrategySelector(temp_community_file, validator)

    # Test DISCONNECTED
    disconnected_issue = {
        "type": IssueType.DISCONNECTED,
        "taxon": "Test",
        "taxon_id": "NCBITaxon:123",
    }
    strategy = selector.select_strategy(disconnected_issue)
    assert isinstance(strategy, DisconnectedTaxonStrategy)

    # Test MISSING_SOURCE
    missing_source_issue = {
        "type": IssueType.MISSING_SOURCE,
        "interaction": "Test",
        "interaction_index": 0,
    }
    strategy = selector.select_strategy(missing_source_issue)
    assert isinstance(strategy, MissingSourceStrategy)

    # Test UNKNOWN_TARGET
    unknown_target_issue = {
        "type": IssueType.UNKNOWN_TARGET,
        "interaction": "Test",
        "taxon": "Unknown",
    }
    strategy = selector.select_strategy(unknown_target_issue)
    assert isinstance(strategy, UnknownTargetStrategy)

    # Test UNKNOWN_SOURCE
    unknown_source_issue = {
        "type": IssueType.UNKNOWN_SOURCE,
        "interaction": "Test",
        "taxon": "Unknown",
    }
    strategy = selector.select_strategy(unknown_source_issue)
    assert isinstance(strategy, UnknownSourceStrategy)


def test_strategy_selector_unknown_issue_type(temp_community_file, validator):
    """Test StrategySelector raises on unknown issue type."""
    selector = StrategySelector(temp_community_file, validator)

    unknown_issue = {"type": IssueType.ID_MISMATCH}  # Not supported

    with pytest.raises(ValueError, match="No strategy found"):
        selector.select_strategy(unknown_issue)


def test_strategy_selector_can_repair(temp_community_file, validator):
    """Test StrategySelector can_repair method."""
    selector = StrategySelector(temp_community_file, validator)

    # Can repair
    repairable = {"type": IssueType.DISCONNECTED, "taxon": "Test", "taxon_id": "NCBITaxon:123"}
    assert selector.can_repair(repairable) is True

    # Cannot repair
    non_repairable = {"type": IssueType.ID_MISMATCH}
    assert selector.can_repair(non_repairable) is False


def test_strategy_selector_get_repairable_issue_types(temp_community_file, validator):
    """Test StrategySelector lists repairable issue types."""
    selector = StrategySelector(temp_community_file, validator)

    repairable_types = selector.get_repairable_issue_types()

    assert IssueType.DISCONNECTED in repairable_types
    assert IssueType.MISSING_SOURCE in repairable_types
    assert IssueType.UNKNOWN_TARGET in repairable_types
    assert IssueType.UNKNOWN_SOURCE in repairable_types
    assert IssueType.ID_MISMATCH not in repairable_types


def test_strategy_validate_suggestion(temp_community_file, validator):
    """Test strategy validates suggestions."""
    strategy = DisconnectedTaxonStrategy(temp_community_file, validator)

    valid_suggestion = {
        "suggested_interactions": [
            {
                "name": "Test",
                "interaction_type": "MUTUALISM",
                "description": "Test",
                "source_taxon": {
                    "preferred_term": "Escherichia coli",
                    "term": {"id": "NCBITaxon:562", "label": "Escherichia coli"},
                },
            }
        ]
    }

    # Read community data
    with open(temp_community_file) as f:
        community_data = yaml.safe_load(f)

    is_valid, errors = strategy.validate_suggestion(valid_suggestion, community_data)

    # Should validate (with minimal validator)
    assert is_valid is True


def test_strategy_get_issue_summary(temp_community_file, validator):
    """Test strategy generates issue summary."""
    strategy = DisconnectedTaxonStrategy(temp_community_file, validator)

    issue = {
        "type": IssueType.DISCONNECTED,
        "taxon": "Test Taxon",
        "taxon_id": "NCBITaxon:123",
    }

    summary = strategy.get_issue_summary(issue)

    assert "Test Taxon" in summary
    assert "NCBITaxon:123" in summary
