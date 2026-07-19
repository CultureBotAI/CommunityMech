"""Tests for the DRAFT CHEBI-route ingredient suggester (issue #30, pending MIM#119).

Loads the script module directly and exercises its pure helpers with fake OAK
adapters. No sibling repos, no network.
"""

import importlib.util
from pathlib import Path

from communitymech.cross_repo_environment import IngredientHit

_spec = importlib.util.spec_from_file_location(
    "suggest_related_ingredients",
    Path(__file__).parent.parent / "scripts" / "suggest_related_ingredients.py",
)
sug = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(sug)


class _FakeEnvoAdapter:
    def descendants(self, envo_id, predicates=None):
        return {"ENVO:00002007", "ENVO:03000033"} if envo_id == "ENVO:00002007" else {envo_id}


class _FakeChebiAdapter:
    _L = {"CHEBI:26833": "sulfur atom", "CHEBI:16136": "hydrogen sulfide"}

    def label(self, cid):
        return self._L.get(cid)


def _ing(chebi_id, env_id, env_label="e", name="n"):
    return IngredientHit(name, chebi_id, env_id, env_label, chebi_id or "kgmicrobe.ingredient:x")


def test_linked_chebi_ids():
    data = {"related_ingredients": [{"chebi_term": {"id": "CHEBI:1"}}, {"preferred_term": "x"}]}
    assert sug._linked_chebi_ids(data) == {"CHEBI:1"}


def test_community_env():
    assert sug._community_env(
        {"environment_term": {"term": {"id": "ENVO:00000051", "label": "hot spring"}}}
    ) == ("ENVO:00000051", "hot spring")
    assert sug._community_env({}) is None


def test_ingredient_matches_chebi_only_exact():
    ing = {
        "ENVO:00000051": [
            _ing("CHEBI:26833", "ENVO:00000051"),
            _ing(None, "ENVO:00000051"),  # non-CHEBI ingredient must be dropped
        ]
    }
    matches = sug._ingredient_matches("ENVO:00000051", ing, envo_adapter=None)
    assert [(h.chebi_id, rel) for h, rel in matches] == [("CHEBI:26833", "exact")]


def test_ingredient_matches_subtype_and_generic_exclusion():
    ing = {
        "ENVO:00002007": [_ing("CHEBI:1", "ENVO:00002007")],
        "ENVO:03000033": [_ing("CHEBI:2", "ENVO:03000033")],
    }
    matches = sug._ingredient_matches("ENVO:00002007", ing, _FakeEnvoAdapter())
    assert {h.chebi_id: rel for h, rel in matches} == {"CHEBI:1": "exact", "CHEBI:2": "subtype"}


def test_blocks_uses_canonical_label_and_skips_unresolved():
    matches = [
        (_ing("CHEBI:26833", "ENVO:00000051", "hot spring", "Sulfur"), "exact"),
        (
            _ing("CHEBI:99999", "ENVO:00000051", "hot spring", "Mystery"),
            "exact",
        ),  # no canonical label
    ]
    blocks, unresolved = sug._blocks(matches, "ENVO:00000051", "hot spring", _FakeChebiAdapter())
    assert unresolved == ["CHEBI:99999"]
    assert len(blocks) == 1
    b = blocks[0]
    assert b["preferred_term"] == "Sulfur"
    # canonical ChEBI label, NOT the MIM free-text name -> keeps id-label gate green
    assert b["chebi_term"] == {"id": "CHEBI:26833", "label": "sulfur atom"}
    assert b["shared_environment_term"] == {"id": "ENVO:00000051", "label": "hot spring"}
