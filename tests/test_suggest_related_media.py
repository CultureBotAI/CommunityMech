"""Tests for the environment-based related_media suggester (issue #30, Use Case 1).

Loads the script module directly (it lives under scripts/, not the package) and
exercises its pure helpers plus the generic-environment guard. No sibling repos,
no network.
"""

import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location(
    "suggest_related_media",
    Path(__file__).parent.parent / "scripts" / "suggest_related_media.py",
)
sug = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(sug)


def test_community_env_extracts_envo():
    data = {"environment_term": {"term": {"id": "ENVO:00000044", "label": "peatland"}}}
    assert sug._community_env(data) == ("ENVO:00000044", "peatland")


def test_community_env_ignores_non_envo_and_missing():
    assert sug._community_env({"environment_term": {"term": {"id": "UBERON:1"}}}) is None
    assert sug._community_env({}) is None


def test_linked_culturemech_ids_spans_related_and_growth_media():
    data = {
        "related_media": [{"culturemech_id": "CultureMech:000001"}, {"preferred_term": "x"}],
        "growth_media": [{"culturemech_id": "CultureMech:000002"}],
    }
    assert sug._linked_culturemech_ids(data) == {"CultureMech:000001", "CultureMech:000002"}


def test_suggestion_block_shape():
    from communitymech.cross_repo_environment import MediaHit

    hits = [MediaHit("CultureMech:000009", "peat_medium", "ENVO:00000044", "peatland")]
    blocks = sug._suggestion_block(hits, "ENVO:00000044", "peatland")
    assert len(blocks) == 1
    b = blocks[0]
    assert b["preferred_term"] == "peat_medium"
    assert b["culturemech_id"] == "CultureMech:000009"
    assert b["relationship_type"] == "ENVIRONMENT_ANALOG"
    assert b["shared_environment_term"] == {"id": "ENVO:00000044", "label": "peatland"}
    assert "peatland" in b["relevance_notes"]


def test_laboratory_environment_is_generic():
    # the over-generic lab environment is excluded by default (noise guard)
    assert "ENVO:01001405" in sug.GENERIC_ENVIRONMENTS
