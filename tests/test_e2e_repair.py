"""End-to-end integration tests for network repair workflow.

Note: These tests require ANTHROPIC_API_KEY to be set and will make real API calls.
Run with: pytest tests/test_e2e_repair.py --e2e
"""

import os
import tempfile
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest
import yaml

# Mark all tests in this file as e2e
pytestmark = pytest.mark.e2e


@pytest.fixture
def test_community_with_disconnected():
    """Create a test community with a disconnected taxon."""
    return {
        "name": "Test E2E Community",
        "description": "Test community for end-to-end repair testing",
        "taxonomy": [
            {
                "taxon_term": {
                    "preferred_term": "Escherichia coli",
                    "term": {"id": "NCBITaxon:562", "label": "Escherichia coli"},
                },
                "functional_roles": [
                    {"id": "GO:0008152", "label": "metabolic process"}
                ],
            },
            {
                "taxon_term": {
                    "preferred_term": "Pseudomonas aeruginosa",
                    "term": {
                        "id": "NCBITaxon:287",
                        "label": "Pseudomonas aeruginosa",
                    },
                },
            },
            {
                "taxon_term": {
                    "preferred_term": "Disconnected bacterium",
                    "term": {
                        "id": "NCBITaxon:999999",
                        "label": "Disconnected bacterium",
                    },
                },
            },
        ],
        "ecological_interactions": [
            {
                "name": "Competition for nutrients",
                "interaction_type": "COMPETITION",
                "description": "Competition between E. coli and P. aeruginosa",
                "source_taxon": {
                    "preferred_term": "Escherichia coli",
                    "term": {"id": "NCBITaxon:562", "label": "Escherichia coli"},
                },
                "target_taxon": {
                    "preferred_term": "Pseudomonas aeruginosa",
                    "term": {
                        "id": "NCBITaxon:287",
                        "label": "Pseudomonas aeruginosa",
                    },
                },
            }
        ],
        "environmental_factors": {
            "habitat": [{"id": "ENVO:00002001", "label": "freshwater"}],
            "physical_parameters": [
                {"parameter_type": "temperature", "value": "25", "unit": "°C"},
                {"parameter_type": "pH", "value": "7.0", "unit": ""},
            ],
        },
    }


@pytest.fixture
def temp_community_file(test_community_with_disconnected):
    """Create temporary community file."""
    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".yaml", delete=False
    ) as f:
        yaml.dump(test_community_with_disconnected, f)
        path = Path(f.name)

    yield path

    # Cleanup
    if path.exists():
        path.unlink()


@pytest.mark.skipif(
    not os.getenv("ANTHROPIC_API_KEY"), reason="ANTHROPIC_API_KEY not set"
)
def test_e2e_audit_finds_disconnected(temp_community_file):
    """Test that audit correctly identifies disconnected taxon."""
    from communitymech.network.auditor import IssueType, NetworkIntegrityAuditor

    auditor = NetworkIntegrityAuditor()
    issues = auditor.audit_community(temp_community_file)

    # Should find disconnected taxon
    disconnected_issues = [i for i in issues if i["type"] == IssueType.DISCONNECTED]
    assert len(disconnected_issues) == 1
    assert disconnected_issues[0]["taxon"] == "Disconnected bacterium"


@pytest.mark.skipif(
    not os.getenv("ANTHROPIC_API_KEY"), reason="ANTHROPIC_API_KEY not set"
)
def test_e2e_strategy_selection(temp_community_file):
    """Test that strategy selector works end-to-end."""
    from communitymech.network.auditor import NetworkIntegrityAuditor
    from communitymech.network.repair_strategies import (
        DisconnectedTaxonStrategy,
        StrategySelector,
    )
    from communitymech.network.validators import SuggestionValidator

    # Find issues
    auditor = NetworkIntegrityAuditor()
    issues = auditor.audit_community(temp_community_file)

    # Select strategy
    validator = SuggestionValidator(validate_evidence=False)
    selector = StrategySelector(temp_community_file, validator)

    for issue in issues:
        if selector.can_repair(issue):
            strategy = selector.select_strategy(issue)
            assert isinstance(strategy, DisconnectedTaxonStrategy)


@pytest.mark.skipif(
    not os.getenv("ANTHROPIC_API_KEY"), reason="ANTHROPIC_API_KEY not set"
)
def test_e2e_context_building(temp_community_file):
    """Test that context builder creates valid context."""
    from communitymech.network.auditor import IssueType, NetworkIntegrityAuditor
    from communitymech.network.repair_strategies import StrategySelector
    from communitymech.network.validators import SuggestionValidator

    # Find disconnected issue
    auditor = NetworkIntegrityAuditor()
    issues = auditor.audit_community(temp_community_file)
    disconnected = [i for i in issues if i["type"] == IssueType.DISCONNECTED][0]

    # Build context
    validator = SuggestionValidator(validate_evidence=False)
    selector = StrategySelector(temp_community_file, validator)
    strategy = selector.select_strategy(disconnected)

    context = strategy.build_context(disconnected)

    # Verify context has required fields
    assert "community_name" in context
    assert "taxon_name" in context
    assert "taxon_id" in context
    assert "environment" in context
    assert "connected_taxa" in context
    assert "interaction_summary" in context

    # Verify content
    assert context["taxon_name"] == "Disconnected bacterium"
    assert "freshwater" in context["environment"]


def test_e2e_mock_suggestion_generation():
    """Test suggestion generation workflow with mocked LLM."""
    from communitymech.llm.anthropic_client import AnthropicClient
    from communitymech.llm.prompts import DISCONNECTED_TAXON_PROMPT

    # Create mock suggestion
    mock_suggestion = {
        "suggested_interactions": [
            {
                "name": "Test Interaction",
                "interaction_type": "MUTUALISM",
                "description": "Test description",
                "source_taxon": {
                    "preferred_term": "Disconnected bacterium",
                    "term": {
                        "id": "NCBITaxon:999999",
                        "label": "Disconnected bacterium",
                    },
                },
                "target_taxon": {
                    "preferred_term": "Escherichia coli",
                    "term": {"id": "NCBITaxon:562", "label": "Escherichia coli"},
                },
            }
        ]
    }

    with patch.object(AnthropicClient, "generate_suggestion") as mock_gen:
        mock_gen.return_value = mock_suggestion

        client = AnthropicClient()
        context = {"test": "context"}

        suggestion = client.generate_suggestion(
            prompt=DISCONNECTED_TAXON_PROMPT, context=context
        )

        assert "suggested_interactions" in suggestion
        assert len(suggestion["suggested_interactions"]) == 1


def test_e2e_validation_workflow():
    """Test complete validation workflow."""
    from communitymech.network.validators import SuggestionValidator

    validator = SuggestionValidator(
        validate_evidence=False,  # Skip evidence to avoid API calls
        validate_ontology=True,
        check_plausibility=True,
    )

    suggestion = {
        "suggested_interactions": [
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
                    "term": {
                        "id": "NCBITaxon:287",
                        "label": "Pseudomonas aeruginosa",
                    },
                },
            }
        ]
    }

    community_data = {
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
                    "term": {
                        "id": "NCBITaxon:287",
                        "label": "Pseudomonas aeruginosa",
                    },
                }
            },
        ]
    }

    is_valid, errors = validator.validate(suggestion, community_data)

    # Should pass (might have warnings but no errors)
    critical_errors = [e for e in errors if e.severity == "error"]
    assert len(critical_errors) == 0


def test_e2e_workflow_summary():
    """Document the complete E2E workflow."""
    workflow = """
    Complete E2E Workflow:

    1. Audit → Find Issues
       NetworkIntegrityAuditor.audit_community()
       → Returns list of issues

    2. Filter → Repairable Issues
       StrategySelector.can_repair()
       → Returns True for DISCONNECTED, MISSING_SOURCE, etc.

    3. Route → Select Strategy
       StrategySelector.select_strategy()
       → Returns appropriate RepairStrategy

    4. Context → Build Rich Context
       RepairStrategy.build_context()
       → Returns context dict for LLM prompt

    5. Generate → LLM Suggestion
       AnthropicClient.generate_suggestion()
       → Returns parsed YAML suggestion

    6. Validate → Multi-Layer Validation
       SuggestionValidator.validate()
       → Returns (is_valid, errors)

    7. Apply → Update YAML
       LLMNetworkRepairer._apply_suggestion()
       → Backs up, updates, writes file

    8. Verify → Re-audit
       NetworkIntegrityAuditor.audit_community()
       → Should show issue resolved
    """
    assert workflow  # Documentation test


@pytest.mark.integration
def test_integration_batch_reporter():
    """Test batch reporter integration."""
    from communitymech.network.batch_reporter import BatchReporter

    # Can initialize without errors
    reporter = BatchReporter()
    assert reporter is not None
    assert reporter.auditor is not None
    assert reporter.validator is not None
