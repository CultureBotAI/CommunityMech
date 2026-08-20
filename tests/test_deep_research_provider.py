from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
MODULE_PATH = REPO_ROOT / "scripts" / "deep_research_provider.py"
CONFIG_PATH = REPO_ROOT / "conf" / "deep_research_provider.yaml"
SPEC = importlib.util.spec_from_file_location("deep_research_provider", MODULE_PATH)
assert SPEC and SPEC.loader
drp = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = drp
SPEC.loader.exec_module(drp)


def test_profile_has_domain_specific_default_and_three_stage_triage():
    config = drp.load_config(CONFIG_PATH)
    focus = config["focuses"][config["default_focus"]]

    assert config["mech"].endswith("Mech")
    assert config["target"]
    assert set(focus["stages"]) == {"discovery", "synthesis", "verification"}
    assert focus["source_priorities"]


@pytest.mark.parametrize("alias", ["edison", "futurehouse", "Falcon"])
def test_edison_aliases_resolve_to_falcon(alias):
    assert drp.canonical_provider(alias) == "falcon"


def test_falcon_platform_key_is_recognized_without_exposing_it():
    status, reason = drp.provider_status("falcon", {"EDISON_PLATFORM_API_KEY": "secret"})
    assert status == "available"
    assert reason == "credential configured"
    assert "secret" not in reason


def test_explicit_empty_environment_does_not_fall_back_to_process_credentials():
    status, reason = drp.provider_status("asta", {})
    assert status == "unavailable"
    assert reason == "set ASTA_API_KEY"


def test_every_focus_ranks_all_real_and_stub_providers(monkeypatch):
    monkeypatch.setenv("ASTA_API_KEY", "test-only")
    config = drp.load_config(CONFIG_PATH)

    for focus_name in config["focuses"]:
        report = drp.build_report(config, focus_name)
        for stage in report["stages"]:
            names = {row["provider"] for row in stage["ranking"]}
            assert names == set(drp.PROVIDERS)
            assert stage["recommended_available"] is not None
            assert stage["recommended_available"]["status"] == "available"


def test_unknown_default_focus_is_rejected(tmp_path):
    profile = tmp_path / "bad.yaml"
    profile.write_text("default_focus: absent\nfocuses:\n  present:\n    stages: {}\n")
    with pytest.raises(ValueError, match="default_focus"):
        drp.load_config(profile)


def test_provider_adjustments_alias_key_is_canonicalized(tmp_path):
    profile = tmp_path / "aliased.yaml"
    profile.write_text(
        "default_focus: f\n"
        "focuses:\n"
        "  f:\n"
        "    stages:\n"
        "      discovery: {}\n"
        "    provider_adjustments:\n"
        "      edison: 3\n"
        "      Claude Code: 2\n"
    )
    config = drp.load_config(profile)
    adjustments = config["focuses"]["f"]["provider_adjustments"]
    assert adjustments == {"falcon": 3, "claude_code": 2}


def test_provider_adjustments_unknown_key_is_rejected(tmp_path):
    profile = tmp_path / "typo.yaml"
    profile.write_text(
        "default_focus: f\n"
        "focuses:\n"
        "  f:\n"
        "    stages:\n"
        "      discovery: {}\n"
        "    provider_adjustments:\n"
        "      flacon: 3\n"  # typo of "falcon"
    )
    with pytest.raises(ValueError, match="unknown provider"):
        drp.load_config(profile)


def test_provider_adjustments_colliding_aliases_are_rejected(tmp_path):
    """Two raw keys that canonicalize to the same provider (edison/falcon)
    must not silently let the second overwrite the first."""
    profile = tmp_path / "collision.yaml"
    profile.write_text(
        "default_focus: f\n"
        "focuses:\n"
        "  f:\n"
        "    stages:\n"
        "      discovery: {}\n"
        "    provider_adjustments:\n"
        "      edison: 3\n"
        "      falcon: 5\n"
    )
    with pytest.raises(ValueError, match="multiple"):
        drp.load_config(profile)


def test_main_rejects_unknown_provider_argument():
    focus = next(iter(drp.load_config(CONFIG_PATH)["focuses"]))
    with pytest.raises(ValueError, match="Unknown provider"):
        drp.main(
            ["--config", str(CONFIG_PATH), "--focus", focus, "--provider", "not-a-real-provider"]
        )


def test_main_rejects_unknown_focus_argument():
    with pytest.raises(ValueError, match="Unknown focus"):
        drp.main(["--config", str(CONFIG_PATH), "--focus", "not-a-real-focus"])


def test_provider_adjustment_actually_changes_rank_order(monkeypatch):
    """The canonicalization test above only checks the config-loading side;
    this proves the bonus actually reaches the score — the exact silent-no-op
    failure mode #487's review found."""
    monkeypatch.setenv("ASTA_API_KEY", "test-only")
    monkeypatch.setenv("CONSENSUS_API_KEY", "test-only")
    config = drp.load_config(CONFIG_PATH)
    focus_name = config["default_focus"]
    stage_name = next(iter(config["focuses"][focus_name]["stages"]))

    baseline = drp.rank_stage(config, focus_name, stage_name)
    # Boost whichever provider ranks last, not a hardcoded name — a provider
    # already at fit=100 (the ceiling) can't visibly increase, so the choice
    # has to guarantee headroom regardless of this repo's specific weights.
    target = min(baseline, key=lambda row: row["fit"])["provider"]
    baseline_fit = {row["provider"]: row["fit"] for row in baseline}

    config["focuses"][focus_name]["provider_adjustments"] = {target: 1000}
    boosted = drp.rank_stage(config, focus_name, stage_name)
    boosted_fit = {row["provider"]: row["fit"] for row in boosted}

    assert boosted_fit[target] > baseline_fit[target]
    assert boosted[0]["provider"] == target


def test_json_provider_filter_keeps_recommended_and_fallback_consistent(capsys, monkeypatch):
    """--json --provider must not leave recommended_available/fallback_available
    naming a provider that isn't in the filtered ranking (#412 review)."""
    monkeypatch.setenv("CONSENSUS_API_KEY", "test-only")
    rc = drp.main(
        [
            "--config",
            str(CONFIG_PATH),
            "--focus",
            next(iter(drp.load_config(CONFIG_PATH)["focuses"])),
            "--provider",
            "consensus",
            "--json",
        ]
    )
    assert rc == 0
    import json

    payload = json.loads(capsys.readouterr().out)
    for stage in payload["stages"]:
        ranking_providers = {row["provider"] for row in stage["ranking"]}
        assert ranking_providers <= {"consensus"}
        for key in ("recommended_available", "fallback_available"):
            entry = stage[key]
            if entry is not None:
                assert entry["provider"] in ranking_providers
