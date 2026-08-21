"""Tests for CommunityMech deep research command wiring."""

from __future__ import annotations

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from research_community import (  # noqa: E402
    build_command,
    load_community,
    provider_args,
    research_env,
    resolve_community_file,
    template_vars,
)


def test_resolve_community_file_finds_slug_record():
    path = resolve_community_file("Yogurt_TwoSpecies_Starter_Culture")
    assert path == REPO_ROOT / "kb" / "communities" / "Yogurt_TwoSpecies_Starter_Culture.yaml"


def test_resolve_community_file_finds_id_record():
    path = resolve_community_file("CommunityMech:000164")
    assert path.name == "Yogurt_TwoSpecies_Starter_Culture.yaml"


def test_template_vars_include_community_context():
    path = resolve_community_file("Yogurt_TwoSpecies_Starter_Culture")
    variables = template_vars(load_community(path), path)
    assert variables["community_name"] == "Yogurt Two-Species Starter Culture"
    assert variables["community_id"] == "CommunityMech:000164"
    assert variables["community_category"] == "BIOTECHNOLOGY"
    assert "Streptococcus thermophilus" in variables["taxonomy_summary"]
    assert "Lactobacillus delbrueckii subsp. bulgaricus" in variables["taxonomy_summary"]
    assert "formate" in variables["interaction_summary"]


def test_provider_args_mirror_dismech_cborg_shortcut():
    assert provider_args("falcon") == ["--provider", "falcon"]
    assert provider_args("cborg") == ["--use-cborg"]


def test_build_command_for_falcon_research():
    command = build_command(
        provider="falcon",
        template=Path("templates/community_mechanism_research.md"),
        output_file=Path(
            "research/communities/Yogurt_TwoSpecies_Starter_Culture-deep-research-falcon.md"
        ),
        variables={
            "community_name": "Yogurt Two-Species Starter Culture",
            "community_id": "CommunityMech:000164",
        },
        passthrough_args=["--max-cost", "1"],
    )
    assert command[:4] == [
        "deep-research-client",
        "research",
        "--template",
        "templates/community_mechanism_research.md",
    ]
    assert "--provider" in command
    assert "falcon" in command
    # NO --separate-citations: the client's regex-based sidecar is malformed
    # (see build_command's docstring comment / CultureMech's
    # docs/RESEARCH_ARTIFACT_CONTRACT.md). The report's own References
    # section is the trustworthy artifact.
    assert "--separate-citations" not in command
    assert command[-2:] == ["--max-cost", "1"]
    assert not any("test-key" in arg for arg in command)


def test_research_env_maps_futurehouse_key_to_edison(monkeypatch):
    monkeypatch.delenv("EDISON_API_KEY", raising=False)
    monkeypatch.setenv("FUTUREHOUSE_API_KEY", "test-key")
    env = research_env("falcon")
    assert env["EDISON_API_KEY"] == "test-key"


def test_research_env_preserves_existing_edison_key(monkeypatch):
    monkeypatch.setenv("EDISON_API_KEY", "edison-key")
    monkeypatch.setenv("FUTUREHOUSE_API_KEY", "futurehouse-key")
    env = research_env("falcon")
    assert env["EDISON_API_KEY"] == "edison-key"
