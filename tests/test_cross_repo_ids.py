"""Tests for the cross-repo ID validator (related_media / CultureMech).

`related_ingredients` is no longer validated here — the `MediaIngredientMech:NNNNNN`
scheme is vestigial (MediaIngredientMech#119); ingredient linking joins on
`chebi_term`, covered by the id-label validator.
"""

from pathlib import Path

import pytest

from communitymech.validators.cross_repo_ids import (
    CrossRepoIssue,
    validate_cross_repo_ids,
)


@pytest.fixture
def community_with_ids(tmp_path: Path) -> Path:
    """A community YAML that references CultureMech media IDs."""
    path = tmp_path / "community.yaml"
    path.write_text("""
id: CommunityMech:000999
name: Test community
related_media:
- preferred_term: Acidic Peatland Medium
  culturemech_id: CultureMech:010001
- preferred_term: Iron Selective Medium
  culturemech_id: CultureMech:010002
""".strip())
    return path


@pytest.fixture
def culturemech_repo(tmp_path: Path) -> Path:
    """A sibling CultureMech kb/ dir with one of the two IDs above."""
    repo = tmp_path / "culturemech_kb"
    repo.mkdir()
    (repo / "medium_a.yaml").write_text("id: CultureMech:010001\nname: Acidic Peatland Medium\n")
    return repo


class TestPatternCheck:
    def test_well_formed_ids_pass_pattern_check(self, community_with_ids: Path) -> None:
        issues = validate_cross_repo_ids(community_with_ids)
        assert not any(i.severity == "error" for i in issues)

    def test_malformed_culturemech_id_reports_error(self, tmp_path: Path) -> None:
        path = tmp_path / "bad.yaml"
        path.write_text(
            "id: CommunityMech:000001\n"
            "related_media:\n"
            "- preferred_term: X\n"
            "  culturemech_id: NOT-A-CURIE\n"
        )
        issues = validate_cross_repo_ids(path)
        errors = [i for i in issues if i.severity == "error"]
        assert len(errors) == 1
        assert "does not match pattern" in errors[0].message


class TestExistenceCheck:
    def test_no_sibling_repo_emits_info_per_id(self, community_with_ids: Path) -> None:
        issues = validate_cross_repo_ids(community_with_ids, sibling_repos={})
        infos = [i for i in issues if i.severity == "info"]
        # 2 culturemech IDs = 2 info notices
        assert len(infos) == 2

    def test_sibling_repo_finds_missing_culturemech_id(
        self, community_with_ids: Path, culturemech_repo: Path
    ) -> None:
        issues = validate_cross_repo_ids(
            community_with_ids,
            sibling_repos={"CultureMech": culturemech_repo},
        )
        errors = [i for i in issues if i.severity == "error"]
        assert len(errors) == 1
        assert "CultureMech:010002" in errors[0].message
        assert "not found" in errors[0].message

    def test_configured_repo_leaves_only_real_errors(
        self, community_with_ids: Path, culturemech_repo: Path
    ) -> None:
        issues = validate_cross_repo_ids(
            community_with_ids,
            sibling_repos={"CultureMech": culturemech_repo},
        )
        infos = [i for i in issues if i.severity == "info"]
        errors = [i for i in issues if i.severity == "error"]
        assert not infos  # repo configured, no skip notices
        assert len(errors) == 1  # 010002 missing

    def test_related_ingredients_are_not_validated(self, tmp_path: Path) -> None:
        # a bogus mediaingredientmech_id (vestigial scheme) must NOT be flagged
        path = tmp_path / "ingredients.yaml"
        path.write_text(
            "id: CommunityMech:000001\n"
            "related_ingredients:\n"
            "- preferred_term: X\n"
            "  mediaingredientmech_id: bogus\n"
        )
        assert validate_cross_repo_ids(path) == []


class TestEdgeCases:
    def test_yaml_without_related_slots_is_clean(self, tmp_path: Path) -> None:
        path = tmp_path / "minimal.yaml"
        path.write_text("id: CommunityMech:000001\nname: minimal\n")
        assert validate_cross_repo_ids(path) == []

    def test_related_media_entry_without_id_is_ignored(self, tmp_path: Path) -> None:
        path = tmp_path / "no_id.yaml"
        path.write_text(
            "id: CommunityMech:000001\n"
            "related_media:\n"
            "- preferred_term: Some medium without a sibling-repo ID\n"
        )
        assert validate_cross_repo_ids(path) == []

    def test_issue_str_includes_severity_and_message(self) -> None:
        issue = CrossRepoIssue(severity="error", field_path="x.y", message="bad")
        s = str(issue)
        assert "[error]" in s
        assert "x.y" in s
        assert "bad" in s
