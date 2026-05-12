"""Tests for suggestion validators."""

from unittest.mock import MagicMock, patch

import pytest

from communitymech.network.validators import SuggestionValidator, ValidationError


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
        ],
        "ecological_interactions": [],
    }


@pytest.fixture
def valid_suggestion():
    """Create a valid suggestion."""
    return {
        "suggested_interactions": [
            {
                "name": "Test Interaction",
                "interaction_type": "MUTUALISM",
                "description": "Test description",
                "source_taxon": {
                    "preferred_term": "Escherichia coli",
                    "term": {"id": "NCBITaxon:562", "label": "Escherichia coli"},
                },
                "target_taxon": {
                    "preferred_term": "Pseudomonas aeruginosa",
                    "term": {"id": "NCBITaxon:287", "label": "Pseudomonas aeruginosa"},
                },
                "metabolites_exchanged": [
                    {
                        "metabolite_term": {
                            "id": "CHEBI:15377",
                            "label": "water",
                        },
                        "direction": "bidirectional",
                    }
                ],
                "biological_processes": [{"id": "GO:0008150", "label": "biological_process"}],
                "evidence": [
                    {
                        "reference": "PMID:12345678",
                        "supports": "SUPPORT",
                        "evidence_source": "LITERATURE",
                        "snippet": "Test snippet from abstract",
                    }
                ],
            }
        ]
    }


def test_validator_initialization():
    """Test validator initializes correctly."""
    validator = SuggestionValidator(
        validate_evidence=True, validate_ontology=True, check_plausibility=True
    )

    assert validator.validate_evidence_enabled is True
    assert validator.validate_ontology_enabled is True
    assert validator.check_plausibility_enabled is True
    assert validator.min_snippet_match_score == 0.95


def test_validation_error():
    """Test ValidationError class."""
    error = ValidationError(
        layer="schema", field="test_field", message="Test error", severity="error"
    )

    assert error.layer == "schema"
    assert error.field == "test_field"
    assert error.message == "Test error"
    assert error.severity == "error"

    error_dict = error.to_dict()
    assert error_dict["layer"] == "schema"
    assert error_dict["field"] == "test_field"


def test_schema_validation_valid(valid_suggestion, test_community):
    """Test schema validation with valid suggestion."""
    validator = SuggestionValidator(
        validate_evidence=False, validate_ontology=False, check_plausibility=False
    )

    is_valid, errors = validator.validate(valid_suggestion, test_community)

    assert is_valid is True
    assert len(errors) == 0


def test_schema_validation_missing_required_field(test_community):
    """Test schema validation catches missing fields."""
    invalid_suggestion = {
        "suggested_interactions": [
            {
                # Missing 'name'
                "interaction_type": "MUTUALISM",
                "description": "Test",
                "source_taxon": {
                    "preferred_term": "Escherichia coli",
                    "term": {"id": "NCBITaxon:562", "label": "Escherichia coli"},
                },
            }
        ]
    }

    validator = SuggestionValidator(
        validate_evidence=False, validate_ontology=False, check_plausibility=False
    )

    is_valid, errors = validator.validate(invalid_suggestion, test_community)

    assert is_valid is False
    assert any(e.field == "suggested_interactions[0].name" for e in errors)


def test_schema_validation_invalid_interaction_type(test_community):
    """Test schema validation catches invalid interaction types."""
    invalid_suggestion = {
        "suggested_interactions": [
            {
                "name": "Test",
                "interaction_type": "INVALID_TYPE",
                "description": "Test",
                "source_taxon": {
                    "preferred_term": "Escherichia coli",
                    "term": {"id": "NCBITaxon:562", "label": "Escherichia coli"},
                },
            }
        ]
    }

    validator = SuggestionValidator(
        validate_evidence=False, validate_ontology=False, check_plausibility=False
    )

    is_valid, errors = validator.validate(invalid_suggestion, test_community)

    assert is_valid is False
    assert any("interaction_type" in e.field for e in errors)


def test_ontology_validation_invalid_ncbitaxon(test_community):
    """Test ontology validation catches invalid NCBITaxon IDs."""
    invalid_suggestion = {
        "suggested_interactions": [
            {
                "name": "Test",
                "interaction_type": "MUTUALISM",
                "description": "Test",
                "source_taxon": {
                    "preferred_term": "Test",
                    "term": {"id": "INVALID:123", "label": "Test"},  # Invalid format
                },
            }
        ]
    }

    validator = SuggestionValidator(
        validate_evidence=False, validate_ontology=True, check_plausibility=False
    )

    is_valid, errors = validator.validate(invalid_suggestion, test_community)

    assert is_valid is False
    assert any("NCBITaxon" in e.message for e in errors)


def test_ontology_validation_invalid_chebi(test_community):
    """Test ontology validation catches invalid CHEBI IDs."""
    invalid_suggestion = {
        "suggested_interactions": [
            {
                "name": "Test",
                "interaction_type": "MUTUALISM",
                "description": "Test",
                "source_taxon": {
                    "preferred_term": "Escherichia coli",
                    "term": {"id": "NCBITaxon:562", "label": "Escherichia coli"},
                },
                "metabolites_exchanged": [
                    {
                        "metabolite_term": {
                            "id": "INVALID:123",  # Invalid format
                            "label": "test",
                        }
                    }
                ],
            }
        ]
    }

    validator = SuggestionValidator(
        validate_evidence=False, validate_ontology=True, check_plausibility=False
    )

    is_valid, errors = validator.validate(invalid_suggestion, test_community)

    # Should have warning (not error) for CHEBI
    assert any("CHEBI" in e.message for e in errors)


@patch("communitymech.network.validators.LiteratureFetcher")
def test_evidence_validation_snippet_match(mock_fetcher_class, test_community):
    """Test evidence validation with matching snippet."""
    # Setup mock
    mock_fetcher = MagicMock()
    mock_fetcher_class.return_value = mock_fetcher
    mock_fetcher.fetch_paper.return_value = (
        "This is a test abstract with the exact snippet: Test snippet from abstract",
        None,
    )

    suggestion = {
        "suggested_interactions": [
            {
                "name": "Test",
                "interaction_type": "MUTUALISM",
                "description": "Test",
                "source_taxon": {
                    "preferred_term": "Escherichia coli",
                    "term": {"id": "NCBITaxon:562", "label": "Escherichia coli"},
                },
                "evidence": [
                    {
                        "reference": "PMID:12345678",
                        "supports": "SUPPORT",
                        "evidence_source": "LITERATURE",
                        "snippet": "Test snippet from abstract",
                    }
                ],
            }
        ]
    }

    validator = SuggestionValidator(
        validate_evidence=True, validate_ontology=False, check_plausibility=False
    )

    is_valid, errors = validator.validate(suggestion, test_community)

    # Should validate successfully
    assert is_valid is True
    # Should have called fetch_paper
    mock_fetcher.fetch_paper.assert_called_once_with("PMID:12345678")


@patch("communitymech.network.validators.LiteratureFetcher")
def test_evidence_validation_snippet_mismatch(mock_fetcher_class, test_community):
    """Test evidence validation with non-matching snippet."""
    # Setup mock
    mock_fetcher = MagicMock()
    mock_fetcher_class.return_value = mock_fetcher
    mock_fetcher.fetch_paper.return_value = (
        "This abstract does not contain the snippet at all",
        None,
    )

    suggestion = {
        "suggested_interactions": [
            {
                "name": "Test",
                "interaction_type": "MUTUALISM",
                "description": "Test",
                "source_taxon": {
                    "preferred_term": "Escherichia coli",
                    "term": {"id": "NCBITaxon:562", "label": "Escherichia coli"},
                },
                "evidence": [
                    {
                        "reference": "PMID:12345678",
                        "supports": "SUPPORT",
                        "evidence_source": "LITERATURE",
                        "snippet": "Completely different snippet",
                    }
                ],
            }
        ]
    }

    validator = SuggestionValidator(
        validate_evidence=True, validate_ontology=False, check_plausibility=False
    )

    is_valid, errors = validator.validate(suggestion, test_community)

    # Should fail validation
    assert is_valid is False
    assert any("snippet" in e.field.lower() for e in errors)


def test_plausibility_check_taxon_not_in_taxonomy(test_community):
    """Test plausibility check catches taxa not in taxonomy."""
    suggestion = {
        "suggested_interactions": [
            {
                "name": "Test",
                "interaction_type": "MUTUALISM",
                "description": "Test",
                "source_taxon": {
                    "preferred_term": "Unknown bacterium",  # Not in taxonomy
                    "term": {"id": "NCBITaxon:999999", "label": "Unknown bacterium"},
                },
            }
        ]
    }

    validator = SuggestionValidator(
        validate_evidence=False, validate_ontology=False, check_plausibility=True
    )

    is_valid, errors = validator.validate(suggestion, test_community)

    assert is_valid is False
    assert any("not found in community taxonomy" in e.message for e in errors)


def test_plausibility_check_mutualism_without_metabolites(test_community):
    """Test plausibility check warns about mutualism without metabolites."""
    suggestion = {
        "suggested_interactions": [
            {
                "name": "Test",
                "interaction_type": "MUTUALISM",
                "description": "Test",
                "source_taxon": {
                    "preferred_term": "Escherichia coli",
                    "term": {"id": "NCBITaxon:562", "label": "Escherichia coli"},
                },
                # No metabolites_exchanged
            }
        ]
    }

    validator = SuggestionValidator(
        validate_evidence=False, validate_ontology=False, check_plausibility=True
    )

    is_valid, errors = validator.validate(suggestion, test_community)

    # Should pass but with warnings
    warnings = [e for e in errors if e.severity == "warning"]
    assert len(warnings) > 0
    assert any("metabolite" in e.message.lower() for e in warnings)


def test_plausibility_check_no_evidence_warning(test_community):
    """Test plausibility check warns about missing evidence."""
    suggestion = {
        "suggested_interactions": [
            {
                "name": "Test",
                "interaction_type": "MUTUALISM",
                "description": "Test",
                "source_taxon": {
                    "preferred_term": "Escherichia coli",
                    "term": {"id": "NCBITaxon:562", "label": "Escherichia coli"},
                },
                # No evidence
            }
        ]
    }

    validator = SuggestionValidator(
        validate_evidence=False, validate_ontology=False, check_plausibility=True
    )

    is_valid, errors = validator.validate(suggestion, test_community)

    # Should have warning about missing evidence
    warnings = [e for e in errors if e.severity == "warning"]
    assert any("evidence" in e.message.lower() for e in warnings)
