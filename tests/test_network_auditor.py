"""Tests for network integrity auditor."""

import tempfile
from pathlib import Path

import pytest
import yaml

from communitymech.network.auditor import IssueType, NetworkIntegrityAuditor


@pytest.fixture
def temp_communities_dir():
    """Create a temporary directory for test community files."""
    with tempfile.TemporaryDirectory() as tmpdir:
        yield Path(tmpdir)


@pytest.fixture
def valid_community():
    """Create a valid community YAML structure."""
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
        "ecological_interactions": [
            {
                "name": "Competition for nutrients",
                "interaction_type": "COMPETITION",
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
    }


def test_valid_community_no_issues(temp_communities_dir, valid_community):
    """Test that a valid community has no issues."""
    # Write test file
    test_file = temp_communities_dir / "test_valid.yaml"
    with open(test_file, "w") as f:
        yaml.dump(valid_community, f)

    # Audit
    auditor = NetworkIntegrityAuditor(communities_dir=temp_communities_dir)
    issues = auditor.audit_community(test_file)

    assert len(issues) == 0, "Valid community should have no issues"


def test_id_mismatch_detected(temp_communities_dir, valid_community):
    """Test that ID mismatches are detected."""
    # Create mismatch
    valid_community["ecological_interactions"][0]["source_taxon"]["term"]["id"] = "NCBITaxon:9999"

    test_file = temp_communities_dir / "test_mismatch.yaml"
    with open(test_file, "w") as f:
        yaml.dump(valid_community, f)

    auditor = NetworkIntegrityAuditor(communities_dir=temp_communities_dir)
    issues = auditor.audit_community(test_file)

    assert len(issues) == 1
    assert issues[0]["type"] == IssueType.ID_MISMATCH
    assert issues[0]["taxon"] == "Escherichia coli"
    assert issues[0]["expected_id"] == "NCBITaxon:562"
    assert issues[0]["actual_id"] == "NCBITaxon:9999"


def test_missing_source_detected(temp_communities_dir, valid_community):
    """Test that missing source_taxon is detected."""
    # Remove source_taxon
    del valid_community["ecological_interactions"][0]["source_taxon"]

    test_file = temp_communities_dir / "test_missing_source.yaml"
    with open(test_file, "w") as f:
        yaml.dump(valid_community, f)

    auditor = NetworkIntegrityAuditor(communities_dir=temp_communities_dir)
    issues = auditor.audit_community(test_file)

    assert len(issues) >= 1
    source_issues = [i for i in issues if i["type"] == IssueType.MISSING_SOURCE]
    assert len(source_issues) == 1


def test_unknown_source_detected(temp_communities_dir, valid_community):
    """Test that unknown source taxon is detected."""
    # Add interaction with unknown source
    valid_community["ecological_interactions"][0]["source_taxon"] = {
        "preferred_term": "Unknown bacterium",
        "term": {"id": "NCBITaxon:99999", "label": "Unknown bacterium"},
    }

    test_file = temp_communities_dir / "test_unknown_source.yaml"
    with open(test_file, "w") as f:
        yaml.dump(valid_community, f)

    auditor = NetworkIntegrityAuditor(communities_dir=temp_communities_dir)
    issues = auditor.audit_community(test_file)

    unknown_issues = [i for i in issues if i["type"] == IssueType.UNKNOWN_SOURCE]
    assert len(unknown_issues) == 1
    assert unknown_issues[0]["taxon"] == "Unknown bacterium"


def test_disconnected_taxon_detected(temp_communities_dir, valid_community):
    """Test that disconnected taxa are detected."""
    # Add a taxon that's not in any interactions
    valid_community["taxonomy"].append(
        {
            "taxon_term": {
                "preferred_term": "Disconnected taxon",
                "term": {"id": "NCBITaxon:12345", "label": "Disconnected taxon"},
            }
        }
    )

    test_file = temp_communities_dir / "test_disconnected.yaml"
    with open(test_file, "w") as f:
        yaml.dump(valid_community, f)

    auditor = NetworkIntegrityAuditor(communities_dir=temp_communities_dir)
    issues = auditor.audit_community(test_file)

    disconnected_issues = [i for i in issues if i["type"] == IssueType.DISCONNECTED]
    assert len(disconnected_issues) == 1
    assert disconnected_issues[0]["taxon"] == "Disconnected taxon"


def test_no_disconnected_if_no_interactions(temp_communities_dir, valid_community):
    """Test that disconnected taxa are not flagged if there are no interactions."""
    # Remove all interactions
    valid_community["ecological_interactions"] = []

    test_file = temp_communities_dir / "test_no_interactions.yaml"
    with open(test_file, "w") as f:
        yaml.dump(valid_community, f)

    auditor = NetworkIntegrityAuditor(communities_dir=temp_communities_dir)
    issues = auditor.audit_community(test_file)

    disconnected_issues = [i for i in issues if i["type"] == IssueType.DISCONNECTED]
    assert len(disconnected_issues) == 0, "Should not flag disconnected if no interactions"


def test_audit_all_communities(temp_communities_dir, valid_community):
    """Test auditing multiple community files."""
    # Create two files - one valid, one with issues
    valid_file = temp_communities_dir / "valid.yaml"
    with open(valid_file, "w") as f:
        yaml.dump(valid_community, f)

    # Create file with issues
    invalid_community = valid_community.copy()
    invalid_community["taxonomy"].append(
        {
            "taxon_term": {
                "preferred_term": "Disconnected",
                "term": {"id": "NCBITaxon:999", "label": "Disconnected"},
            }
        }
    )
    invalid_file = temp_communities_dir / "invalid.yaml"
    with open(invalid_file, "w") as f:
        yaml.dump(invalid_community, f)

    auditor = NetworkIntegrityAuditor(communities_dir=temp_communities_dir)
    all_issues = auditor.audit_all()

    assert "valid" not in all_issues or len(all_issues["valid"]) == 0
    assert "invalid" in all_issues
    assert len(all_issues["invalid"]) == 1  # One disconnected taxon


def test_json_export(temp_communities_dir, valid_community):
    """Test JSON export of issues."""
    # Add disconnected taxon
    valid_community["taxonomy"].append(
        {
            "taxon_term": {
                "preferred_term": "Disconnected",
                "term": {"id": "NCBITaxon:999", "label": "Disconnected"},
            }
        }
    )

    test_file = temp_communities_dir / "test.yaml"
    with open(test_file, "w") as f:
        yaml.dump(valid_community, f)

    auditor = NetworkIntegrityAuditor(communities_dir=temp_communities_dir)
    auditor.audit_all()

    json_output = auditor.to_json()
    assert isinstance(json_output, str)
    assert "Disconnected" in json_output
    assert "DISCONNECTED" in json_output


def test_taxonomy_lookup(temp_communities_dir, valid_community):
    """Test taxonomy lookup helper method."""
    test_file = temp_communities_dir / "test.yaml"
    with open(test_file, "w") as f:
        yaml.dump(valid_community, f)

    auditor = NetworkIntegrityAuditor(communities_dir=temp_communities_dir)
    data = auditor.get_community_data(test_file)
    lookup = auditor.get_taxonomy_lookup(data)

    assert "Escherichia coli" in lookup
    assert lookup["Escherichia coli"]["id"] == "NCBITaxon:562"
    assert "Pseudomonas aeruginosa" in lookup
    assert lookup["Pseudomonas aeruginosa"]["id"] == "NCBITaxon:287"
