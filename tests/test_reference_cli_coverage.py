"""Exercise the real CLI, not only the plugin's private excerpt method."""

import importlib.util
from pathlib import Path

import pytest


@pytest.mark.parametrize(
    "stem,count,omitted",
    [
        ("Phormidium_Alkaline_Consortium", 21, 2),
        ("Alseth_FourSpecies_Pathogen_Phage_Community", 27, 1),
        ("PHA_MixedCulture_Phage_Succession_Community", 24, 0),
    ],
)
def test_native_cli_counts_issues_not_checked_excerpts(stem, count, omitted):
    path = Path(__file__).resolve().parents[1] / "reports/reference_cli_coverage/probe.py"
    spec = importlib.util.spec_from_file_location("reference_cli_probe", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    result = module.run_probe(stem)
    assert [case["exit_code"] for case in result["cases"]] == [0, 1, 0] + ([0] if omitted else [])
    assert all(case["excerpt_count"] == count for case in result["cases"])
    assert len(result["omitted_discussion_fields"]) == omitted
