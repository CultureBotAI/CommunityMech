"""Exercise the real CLI, not only the plugin's private excerpt method."""

import importlib.util
import tempfile
from pathlib import Path

import pytest


@pytest.mark.parametrize(
    "stem,count,discussions",
    [
        ("Phormidium_Alkaline_Consortium", 23, 2),
        ("Alseth_FourSpecies_Pathogen_Phage_Community", 28, 1),
        ("PHA_MixedCulture_Phage_Succession_Community", 24, 0),
    ],
)
def test_native_cli_counts_issues_not_checked_excerpts(stem, count, discussions):
    root = Path(__file__).resolve().parents[1]
    path = root / "scripts/adhoc/probe_reference_cli_successor_20261115.py"
    spec = importlib.util.spec_from_file_location("reference_cli_probe", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    (root / ".temp").mkdir(exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="reference-cli-test-", dir=root / ".temp") as scratch:
        result = module.run_probe(stem, Path(scratch) / "probe")
    assert result["controls_passed"], result
    cases = result["cases"]
    assert [case["native_exit_code"] for case in cases] == [0, 1, 0] + (
        [1, 0] if discussions else []
    )
    assert all(case["counts"]["snippet_occurrences_compared"] == count for case in cases)
    assert all(case["counts"]["snippet_surfaces"] == count for case in cases)
    assert all(case["assertion_coverage_complete"] for case in cases)
    assert len(result["discussion_fields"]) == discussions
