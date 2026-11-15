"""Exercise the actual additive jq selector, including #2873's missing-ID defect.

2026-11-15: synthetic stdin only; no native source reads, transfers or writes.
The jq executable is the same required tool used by the transfer-path command.
"""

import json
import subprocess
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
SELECTOR = ROOT / "scripts/adhoc/gtdb_source_unit_transfer_paths_v2_20261115.jq"


def run_selector(requested, rows):
    return subprocess.run(
        ["jq", "-r", "--argjson", "record_ids", json.dumps(requested), "-f", str(SELECTOR)],
        input=json.dumps({"records": rows}),
        capture_output=True,
        text=True,
        check=False,
    )


def row(identifier, *paths):
    return {"record_id": identifier, "input_paths": list(paths)}


@pytest.mark.parametrize(
    "requested,rows",
    [
        (["A", "B"], [row("A", "first"), row("A", "second")]),
        (["A"], [row("A", "first"), row("A", "second")]),
        (["A", "B"], [row("A", "first")]),
        (["A"], []),
        (["A", "A"], [row("A", "first")]),
        ([], [row("A", "first")]),
        ([str(i) for i in range(11)], [row(str(i), "path") for i in range(11)]),
        ([""], [row("", "first")]),
        ([1], [row(1, "first")]),
    ],
)
def test_invalid_selection_refuses_before_any_output(requested, rows):
    result = run_selector(requested, rows)
    assert result.returncode != 0
    assert result.stdout == ""


def test_unique_two_unit_selection_restores_the_missing_id_case():
    result = run_selector(["B", "A"], [row("A", "first", "common"), row("B", "second", "common")])
    assert result.returncode == 0, result.stderr
    assert result.stdout.splitlines() == ["common", "first", "second"]


def test_one_unit_selects_only_its_paths_from_a_larger_proof():
    result = run_selector(["A"], [row("B", "excluded"), row("A", "first", "first")])
    assert result.returncode == 0, result.stderr
    assert result.stdout.splitlines() == ["first"]
