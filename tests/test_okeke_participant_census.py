"""Keep the explicit participant population synchronized without relaxing its gate."""

import importlib.util
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
TARGET = "Okeke_Lu_Cellulolytic_Consortium.yaml"


def test_the_census_rejects_an_omitted_okeke_entry(monkeypatch):
    spec = importlib.util.spec_from_file_location(
        "okeke_participant_census_guard", ROOT / "tests/test_participating_taxa.py"
    )
    guard = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(guard)
    original = guard.USERS.copy()
    assert TARGET in original
    guard.test_the_corpus_is_unchanged_by_this_feature()
    with monkeypatch.context() as mutation:
        mutation.setattr(guard, "USERS", original - {TARGET})
        assert original - guard.USERS == {TARGET}
        assert not guard.USERS - original
        with pytest.raises(AssertionError, match="Added:.*Okeke_Lu_Cellulolytic_Consortium"):
            guard.test_the_corpus_is_unchanged_by_this_feature()
    assert original == guard.USERS
    guard.test_the_corpus_is_unchanged_by_this_feature()
