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


def test_missing_source_skipped_for_community_level_scope(temp_communities_dir, valid_community):
    """COMMUNITY_LEVEL interactions describe emergent/community-wide phenomena
    and need not have source_taxon set."""
    del valid_community["ecological_interactions"][0]["source_taxon"]
    valid_community["ecological_interactions"][0]["scope"] = "COMMUNITY_LEVEL"

    test_file = temp_communities_dir / "test_community_level.yaml"
    with open(test_file, "w") as f:
        yaml.dump(valid_community, f)

    auditor = NetworkIntegrityAuditor(communities_dir=temp_communities_dir)
    issues = auditor.audit_community(test_file)

    missing_source = [i for i in issues if i["type"] == IssueType.MISSING_SOURCE]
    assert missing_source == []


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


def test_unknown_source_skipped_for_community_level_scope(temp_communities_dir, valid_community):
    """COMMUNITY_LEVEL interactions can use aggregate source descriptors that
    don't appear in the taxonomy section without raising UNKNOWN_SOURCE."""
    valid_community["ecological_interactions"][0]["source_taxon"] = {
        "preferred_term": "aggregate community descriptor",
        "term": {"id": "NCBITaxon:2", "label": "Bacteria"},
    }
    valid_community["ecological_interactions"][0]["scope"] = "COMMUNITY_LEVEL"
    # Mark the formerly-source taxon as a community member so it doesn't
    # become DISCONNECTED and confound the test.
    valid_community["taxonomy"][0]["functional_role"] = ["PRIMARY_DEGRADER"]

    test_file = temp_communities_dir / "test_unknown_source_community.yaml"
    with open(test_file, "w") as f:
        yaml.dump(valid_community, f)

    auditor = NetworkIntegrityAuditor(communities_dir=temp_communities_dir)
    issues = auditor.audit_community(test_file)

    assert issues == []


def test_unknown_target_skipped_for_community_level_scope(temp_communities_dir, valid_community):
    """COMMUNITY_LEVEL interactions can use aggregate target descriptors that
    don't appear in the taxonomy section without raising UNKNOWN_TARGET."""
    valid_community["ecological_interactions"][0]["target_taxon"] = {
        "preferred_term": "external host or aggregate community",
        "term": {"id": "NCBITaxon:2", "label": "Bacteria"},
    }
    valid_community["ecological_interactions"][0]["scope"] = "COMMUNITY_LEVEL"
    # Mark the formerly-target taxon as a community member so it doesn't
    # become DISCONNECTED and confound the test.
    valid_community["taxonomy"][1]["functional_role"] = ["PRIMARY_DEGRADER"]

    test_file = temp_communities_dir / "test_unknown_target_community.yaml"
    with open(test_file, "w") as f:
        yaml.dump(valid_community, f)

    auditor = NetworkIntegrityAuditor(communities_dir=temp_communities_dir)
    issues = auditor.audit_community(test_file)

    assert issues == []


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


def test_membership_metadata_no_longer_exempts_from_disconnected(
    temp_communities_dir, valid_community
):
    """abundance_level / functional_role do not exempt a taxon (#304).

    They used to. That proxy stood in for "described as a member even without an
    edge", but it exempted 931 of 1007 taxa, so DISCONNECTED effectively reported
    "lacks metadata" rather than "lacks interactions" — and it rewarded filling
    those slots, since removing a fabricated abundance_level created findings.
    Membership without an edge is now expressed by a COMMUNITY_LEVEL interaction,
    which credits its members (see the test below).
    """
    for pref, tid, extra in [
        ("Membership-only taxon", "NCBITaxon:99999", {"abundance_level": "ABUNDANT"}),
        ("Role-only taxon", "NCBITaxon:88888", {"functional_role": ["PRIMARY_DEGRADER"]}),
    ]:
        valid_community["taxonomy"].append(
            {"taxon_term": {"preferred_term": pref, "term": {"id": tid, "label": pref}}, **extra}
        )

    test_file = temp_communities_dir / "test_membership.yaml"
    test_file.write_text(yaml.dump(valid_community))

    issues = NetworkIntegrityAuditor(communities_dir=temp_communities_dir).audit_community(
        test_file
    )
    flagged = {i["taxon"] for i in issues if i["type"] == IssueType.DISCONNECTED}

    assert flagged == {"Membership-only taxon", "Role-only taxon"}, (
        "carrying abundance_level or functional_role must no longer suppress a "
        "DISCONNECTED finding; the rule reports connectivity, not slot completeness"
    )


def test_community_level_interaction_connects_every_member(temp_communities_dir, valid_community):
    """A COMMUNITY_LEVEL interaction credits all members (#304).

    Such an interaction has no source_taxon or target_taxon by design, so it
    previously contributed no connections and every taxon in a record using them
    exclusively was disconnected by construction — 107 of 302 records with
    interactions.
    """
    valid_community["taxonomy"].append(
        {
            "taxon_term": {
                "preferred_term": "Edgeless member",
                "term": {"id": "NCBITaxon:77777", "label": "Edgeless member"},
            }
        }
    )
    valid_community["ecological_interactions"] = [
        {
            "name": "Community-wide effect",
            "interaction_type": "NICHE_PARTITIONING",
            "scope": "COMMUNITY_LEVEL",
        }
    ]

    test_file = temp_communities_dir / "test_community_level.yaml"
    test_file.write_text(yaml.dump(valid_community))

    issues = NetworkIntegrityAuditor(communities_dir=temp_communities_dir).audit_community(
        test_file
    )

    assert [i for i in issues if i["type"] == IssueType.DISCONNECTED] == [], (
        "a COMMUNITY_LEVEL interaction asserts a relationship across the whole "
        "community, so no member should count as disconnected"
    )


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


# ---------------------------------------------------------------------------
# Regressions: an unreadable file must not abort the sweep (#281), and report
# labels must not depend on the Python version (#282).
# ---------------------------------------------------------------------------


def _write_malformed(directory: Path, stem: str = "broken") -> Path:
    """Write a YAML file that `yaml.safe_load` cannot parse."""
    path = directory / f"{stem}.yaml"
    path.write_text("name: broken\ntaxonomy: [\n  - bad: {\n")
    return path


def test_unreadable_file_is_recorded_instead_of_raising(temp_communities_dir):
    """A malformed YAML becomes a finding rather than an exception.

    It used to propagate out of ``audit_all``'s loop into the CLI's blanket
    handler, which exited 2 without writing a report.
    """
    _write_malformed(temp_communities_dir)

    auditor = NetworkIntegrityAuditor(communities_dir=temp_communities_dir)
    all_issues = auditor.audit_all()

    assert "broken" in all_issues
    assert [i["type"] for i in all_issues["broken"]] == [IssueType.UNREADABLE]
    assert "Could not audit this file" in all_issues["broken"][0]["message"]


def test_one_unreadable_file_does_not_hide_the_others(temp_communities_dir, valid_community):
    """The rest of the sweep still runs — the actual regression behind #281.

    A single bad record used to take the audit down with it, so the other files'
    findings were never computed and the report was never written.
    """
    valid_community["taxonomy"].append(
        {
            "taxon_term": {
                "preferred_term": "Disconnected",
                "term": {"id": "NCBITaxon:999", "label": "Disconnected"},
            }
        }
    )
    (temp_communities_dir / "has_findings.yaml").write_text(yaml.dump(valid_community))
    _write_malformed(temp_communities_dir)

    auditor = NetworkIntegrityAuditor(communities_dir=temp_communities_dir)
    all_issues = auditor.audit_all()

    assert "broken" in all_issues
    assert [i["type"] for i in all_issues["has_findings"]] == [IssueType.DISCONNECTED]


def test_unreadable_file_still_writes_a_report(temp_communities_dir, tmp_path):
    """`--report` must produce a file even when a record cannot be parsed."""
    _write_malformed(temp_communities_dir)
    report = tmp_path / "audit.txt"

    auditor = NetworkIntegrityAuditor(communities_dir=temp_communities_dir)
    auditor.audit_all()
    auditor.write_report(output_path=report)

    assert report.exists()
    assert "UNREADABLE:" in report.read_text()


def test_unreadable_is_listed_in_the_console_report_order():
    """Guards against adding an IssueType that `report_community_issues` drops.

    That function iterates a hard-coded list of types; anything missing from it
    is silently absent from console output while still counting in the total.
    """
    import inspect

    source = inspect.getsource(NetworkIntegrityAuditor.report_community_issues)
    for member in IssueType:
        assert f"IssueType.{member.name}" in source, (
            f"{member.name} is not handled by report_community_issues, so it "
            f"would count toward the total but never be printed."
        )


def test_report_labels_are_bare_enum_values(temp_communities_dir, valid_community, tmp_path):
    """Report labels are the enum *value*, on every Python (#282).

    ``IssueType`` is a ``str``-mixin enum, and that mixin's ``__format__``
    switched in 3.11 from the value to the qualified ``IssueType.NAME``. The
    report interpolated a member directly, so CI (3.10) and a dev venv (3.14)
    produced different text for identical input.
    """
    valid_community["taxonomy"].append(
        {
            "taxon_term": {
                "preferred_term": "Disconnected",
                "term": {"id": "NCBITaxon:999", "label": "Disconnected"},
            }
        }
    )
    (temp_communities_dir / "test.yaml").write_text(yaml.dump(valid_community))
    report = tmp_path / "audit.txt"

    auditor = NetworkIntegrityAuditor(communities_dir=temp_communities_dir)
    auditor.audit_all()
    auditor.write_report(output_path=report)

    text = report.read_text()
    assert "IssueType." not in text, "report leaked the qualified enum name"
    assert "DISCONNECTED: Taxon 'Disconnected' has no interactions" in text


def test_type_label_is_version_independent():
    """The helper returns the value for members and passes strings through."""
    from communitymech.network.auditor import _type_label

    assert _type_label(IssueType.UNKNOWN_SOURCE) == "UNKNOWN_SOURCE"
    assert _type_label(IssueType.UNREADABLE) == "UNREADABLE"
    # Some call sites hold plain strings rather than members.
    assert _type_label("ID_MISMATCH") == "ID_MISMATCH"


def test_all_files_unreadable_is_treated_as_a_tool_failure(temp_communities_dir):
    """Catching per file must not turn an auditor bug into "all data is bad".

    Nothing legitimate makes every record unreadable at once, so that case is
    raised rather than reported as findings — the CLI turns it into exit 2 with
    no report, which the network-quality workflow surfaces as a crash.
    """
    _write_malformed(temp_communities_dir, "broken_one")
    _write_malformed(temp_communities_dir, "broken_two")

    auditor = NetworkIntegrityAuditor(communities_dir=temp_communities_dir)
    with pytest.raises(RuntimeError, match="failure of the auditor, not of the data"):
        auditor.audit_all()


def test_a_lone_unreadable_file_is_still_a_finding(temp_communities_dir):
    """The all-failed guard must not fire on a single-file directory.

    One bad file out of one is an ordinary data finding, not evidence that the
    auditor is broken.
    """
    _write_malformed(temp_communities_dir)

    auditor = NetworkIntegrityAuditor(communities_dir=temp_communities_dir)
    all_issues = auditor.audit_all()

    assert [i["type"] for i in all_issues["broken"]] == [IssueType.UNREADABLE]
