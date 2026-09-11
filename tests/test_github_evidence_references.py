"""GITHUB evidence references must name immutable repository objects."""

from __future__ import annotations

import re
from pathlib import Path

import pytest
import yaml

SCHEMA = Path("src/communitymech/schema/communitymech.yaml")
SHA = "693011e69d83bf23f02f144d506df5b8ee17a8dd"


@pytest.fixture(scope="module")
def reference_patterns() -> dict[str, str]:
    schema = yaml.safe_load(SCHEMA.read_text())
    return {
        "EvidenceItem.reference": schema["classes"]["EvidenceItem"]["attributes"]["reference"][
            "pattern"
        ],
        "ComputationalTool.tool_reference": schema["classes"]["ComputationalTool"]["attributes"][
            "tool_reference"
        ]["pattern"],
    }


def test_tool_reference_mirrors_evidence_reference_pattern(
    reference_patterns: dict[str, str],
) -> None:
    assert (
        reference_patterns["ComputationalTool.tool_reference"]
        == reference_patterns["EvidenceItem.reference"]
    )


@pytest.mark.parametrize(
    "value",
    [
        "PMID:42454401",
        "doi:10.1111/nph.71425",
        "bioproject:PRJNA1404338",
        f"GITHUB:deanpettinga/src2_paper/tree/{SHA}",
        f"GITHUB:deanpettinga/src2_paper/tree/{SHA}/data",
        f"GITHUB:deanpettinga/src2_paper/blob/{SHA}/SRC2_formulations.tsv",
        f"GITHUB:deanpettinga/src2_paper/commit/{SHA}",
    ],
)
def test_stable_references_match(value: str, reference_patterns: dict[str, str]) -> None:
    pattern = re.compile(reference_patterns["EvidenceItem.reference"])

    assert pattern.fullmatch(value)


@pytest.mark.parametrize(
    "value",
    [
        "GITHUB:deanpettinga/src2_paper",
        "GITHUB:deanpettinga/src2_paper/tree/main",
        "GITHUB:deanpettinga/src2_paper/blob/main/SRC2_formulations.tsv",
        "GITHUB:deanpettinga/src2_paper/tree/693011e",
    ],
)
def test_mutable_or_short_github_references_do_not_match(
    value: str,
    reference_patterns: dict[str, str],
) -> None:
    pattern = re.compile(reference_patterns["EvidenceItem.reference"])

    assert not pattern.fullmatch(value)
