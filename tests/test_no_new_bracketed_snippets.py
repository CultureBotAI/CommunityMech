"""Preserve and validate literal scientific bracket content (CommunityMech #622).

The former guard prohibited adding brackets because validator 0.1.7 deleted
their contents from queries. Upstream 0.2.1 supports literal bracket patterns.
Our quotes must preserve source text, so the native recipe configuration keeps
every bracket's contents. These tests exercise the configured real matcher,
including the unchanged Asgard quote and a mutated cofactor that must fail.
"""

from __future__ import annotations

import pathlib
import re

import pytest
import yaml
from linkml_reference_validator.models import ReferenceContent, ReferenceValidationConfig
from linkml_reference_validator.validation.supporting_text_validator import SupportingTextValidator

REPO = pathlib.Path(__file__).parent.parent


def _record_dirs() -> list[str]:
    """Derive the record surfaces from the existing id/label gate configuration."""
    config = yaml.safe_load((REPO / "conf/id_label_targets.yaml").read_text(encoding="utf-8"))
    globs = [t["glob"] for t in config["targets"] if t.get("glob", "").endswith(".yaml")]
    return sorted({glob.rsplit("/", 1)[0] for glob in globs})


def _snippets() -> list[tuple[str, str]]:
    found = []
    for directory in _record_dirs():
        for path in sorted((REPO / directory).glob("*.yaml")):
            stack = [yaml.safe_load(path.read_text(encoding="utf-8")) or {}]
            while stack:
                node = stack.pop()
                if isinstance(node, dict):
                    if isinstance(node.get("snippet"), str):
                        found.append((path.name, node["snippet"]))
                    stack.extend(node.values())
                elif isinstance(node, list):
                    stack.extend(node)
    return found


@pytest.fixture(scope="module")
def validator():
    # Use the native recipe's configuration, not a test-only literal setting.
    config = yaml.safe_load((REPO / "conf/reference_validator.yaml").read_text(encoding="utf-8"))
    config["cache_dir"] = REPO / config["cache_dir"]
    return SupportingTextValidator(ReferenceValidationConfig(**config))


def test_the_scan_finds_snippets_at_all():
    snippets = _snippets()
    assert len(snippets) > 5000, f"only {len(snippets)} snippets found; the walk is broken"


def test_every_curated_bracket_content_survives_query_splitting(validator):
    checked = 0
    for record, snippet in _snippets():
        parts = " ".join(validator._split_query(snippet))
        for fragment in re.findall(r"\[[^\]]*\]", snippet):
            checked += 1
            assert fragment in parts, f"{record}: literal source content was removed: {fragment}"
    assert checked >= 2, "the known scientific bracket cases were not exercised"


def test_unchanged_asgard_nife_quote_matches_its_committed_article(validator):
    path = REPO / "kb/communities/Asgard_Wetland_Soil_Methanogenesis_Substrate_Community.yaml"
    record = yaml.safe_load(path.read_text(encoding="utf-8"))
    evidence = record["related_ingredients"][2]["evidence"][0]
    assert "[NiFe]" in evidence["snippet"]
    content = (REPO / "references_cache/PMID_39085194.md").read_text(encoding="utf-8")
    reference = ReferenceContent(reference_id=evidence["reference"], content=content)
    assert validator.find_text_in_reference(evidence["snippet"], reference).found
    mutation = evidence["snippet"].replace("[NiFe]", "[FeFe]")
    assert not validator.find_text_in_reference(mutation, reference).found


@pytest.mark.parametrize("literal", ["[v/v]", "[co]", "[35S]", "[Fe-S]", "[before rewetting]"])
def test_bracket_contents_are_evidence_not_discardable_editorial_notes(validator, literal):
    quote = f"The source reports {literal} in this condition."
    reference = ReferenceContent(reference_id="PMID:1", content=quote)
    assert validator.find_text_in_reference(quote, reference).found
    mutation = quote.replace(literal, "[ZZQQ fabricated content]")
    assert not validator.find_text_in_reference(mutation, reference).found


def test_the_record_directories_come_from_config_and_are_real():
    directories = _record_dirs()
    assert set(directories) == {"kb/communities", "kb/taxa", "data/isolates"}, directories
    for directory in directories:
        path = REPO / directory
        assert path.is_dir(), f"{directory} is configured but does not exist"
        assert list(path.glob("*.yaml")), f"{directory} holds no YAML records"
