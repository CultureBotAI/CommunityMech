"""Tests for the environment-grounding quality report (issue #30 follow-up).

Loads the script module directly and exercises its pure flagging helper plus the
shared generic-term set. No sibling repos, no network.
"""

import importlib.util
from pathlib import Path

from communitymech.cross_repo_environment import GENERIC_ENVIRONMENT_TERMS

_spec = importlib.util.spec_from_file_location(
    "env_grounding_quality",
    Path(__file__).parent.parent / "scripts" / "env_grounding_quality.py",
)
egq = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(egq)


def test_generic_term_flagged_regardless_of_count():
    # ENVO:01001405 is generic; flagged even below the over-applied threshold
    assert egq.flags_for("ENVO:01001405", count=1, threshold=15) == ["GENERIC"]


def test_generic_and_over_applied_both_flagged():
    assert egq.flags_for("ENVO:01001405", count=110, threshold=15) == ["GENERIC", "over-applied"]


def test_specific_term_over_applied_only_at_threshold():
    # a legit specific env (rhizosphere) is only flagged when over-applied
    assert egq.flags_for("ENVO:00005801", count=42, threshold=15) == ["over-applied"]
    assert egq.flags_for("ENVO:00005801", count=14, threshold=15) == []


def test_shared_generic_set_matches_suggester():
    # both tools must key off the same generic-environment set
    _sug_spec = importlib.util.spec_from_file_location(
        "suggest_related_media",
        Path(__file__).parent.parent / "scripts" / "suggest_related_media.py",
    )
    sug = importlib.util.module_from_spec(_sug_spec)
    _sug_spec.loader.exec_module(sug)
    assert sug.GENERIC_ENVIRONMENTS is GENERIC_ENVIRONMENT_TERMS
    assert "ENVO:01001405" in GENERIC_ENVIRONMENT_TERMS
