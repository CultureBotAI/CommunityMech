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

    hit = MediaHit("CultureMech:000009", "peat_medium", "ENVO:00000044", "peatland")
    blocks = sug._suggestion_block([(hit, "exact")], "ENVO:00000044", "peatland")
    assert len(blocks) == 1
    b = blocks[0]
    assert b["preferred_term"] == "peat_medium"
    assert b["culturemech_id"] == "CultureMech:000009"
    assert b["relationship_type"] == "ENVIRONMENT_ANALOG"
    assert b["shared_environment_term"] == {"id": "ENVO:00000044", "label": "peatland"}
    assert "peatland" in b["relevance_notes"]


def test_suggestion_block_subtype_note_mentions_subtype():
    from communitymech.cross_repo_environment import MediaHit

    hit = MediaHit("CultureMech:000002", "marine_sed_medium", "ENVO:03000033", "marine sediment")
    blocks = sug._suggestion_block([(hit, "subtype")], "ENVO:00002007", "sediment")
    note = blocks[0]["relevance_notes"]
    assert "subtype" in note and "marine sediment" in note
    # join key is the community's (broader) term
    assert blocks[0]["shared_environment_term"] == {"id": "ENVO:00002007", "label": "sediment"}


def test_laboratory_environment_is_generic():
    # the over-generic lab environment is excluded by default (noise guard)
    assert "ENVO:01001405" in sug.GENERIC_ENVIRONMENTS


class _FakeEnvoAdapter:
    """sediment (ENVO:00002007) has one subtype: marine sediment (ENVO:03000033)."""

    def descendants(self, envo_id, predicates=None):
        return {"ENVO:00002007", "ENVO:03000033"} if envo_id == "ENVO:00002007" else {envo_id}


def _hit(cid, env_id, env_label):
    from communitymech.cross_repo_environment import MediaHit

    return MediaHit(cid, f"{cid}_medium", env_id, env_label)


def test_matches_for_exact_only_without_adapter():
    media = {"ENVO:00002007": [_hit("CultureMech:000001", "ENVO:00002007", "sediment")]}
    matches = sug._matches_for("ENVO:00002007", media, envo_adapter=None)
    assert matches == [(media["ENVO:00002007"][0], "exact")]


def test_matches_for_includes_subtype_media_with_adapter():
    media = {
        "ENVO:00002007": [_hit("CultureMech:000001", "ENVO:00002007", "sediment")],
        "ENVO:03000033": [_hit("CultureMech:000002", "ENVO:03000033", "marine sediment")],
    }
    matches = sug._matches_for("ENVO:00002007", media, _FakeEnvoAdapter())
    by_id = {h.culturemech_id: rel for h, rel in matches}
    assert by_id == {"CultureMech:000001": "exact", "CultureMech:000002": "subtype"}


def test_matches_for_excludes_generic_subtype_env():
    # a generic subtype env (e.g. laboratory environment) must not leak in via subsumption
    class _AdapterWithGenericSub:
        def descendants(self, envo_id, predicates=None):
            return {envo_id, "ENVO:01001405"}

    media = {
        "ENVO:01000313": [_hit("CultureMech:000001", "ENVO:01000313", "anthropogenic")],
        "ENVO:01001405": [_hit("CultureMech:000009", "ENVO:01001405", "laboratory environment")],
    }
    matches = sug._matches_for(
        "ENVO:01000313",
        media,
        _AdapterWithGenericSub(),
        exclude_subtype_envs=sug.GENERIC_ENVIRONMENTS,
    )
    assert {h.culturemech_id for h, _ in matches} == {"CultureMech:000001"}


def test_matches_for_prefers_exact_over_subtype_on_dupe():
    hit = _hit("CultureMech:000001", "ENVO:00002007", "sediment")
    # same medium reachable both exactly and as a subtype -> exact wins
    media = {"ENVO:00002007": [hit], "ENVO:03000033": [hit]}
    matches = sug._matches_for("ENVO:00002007", media, _FakeEnvoAdapter())
    assert matches == [(hit, "exact")]
