"""`--emit-yaml` output must be pasteable, i.e. identical to what `--apply` writes (#380).

`apply_to_community` dumped blocks at `width=4096`, one key per line.
`--emit-yaml` used PyYAML's default, so `gtdb_lineage` and `mapping_source` —
the two long scalars — wrapped onto continuation lines indented deeper than the
block keys. `--emit-yaml` exists to be **pasted into a record**, so the two
paths disagreeing is how wrapped blocks got into the KB.

That is not cosmetic. It is the root cause of the corruption #378 had to fix:
a line-level editor then has to handle both shapes, and the first version
matched exactly six spaces and orphaned the continuations into duplicate keys.

The fix is one constant, `DUMP_WIDTH`, used by both. What keeps it fixed is
this test: render the same grounding down each path and compare.

Also covered: `--refresh` only modifies how `--apply` treats existing blocks, so
on its own — or with `--ncbi-id`/`--name`, where there is no stored block —
it did nothing and exited 0, leaving the caller believing a re-ground had
happened. Argparse enforced neither.
"""

from __future__ import annotations

import importlib.util
import subprocess
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).parent.parent


@pytest.fixture(scope="module")
def gtdb():
    spec = importlib.util.spec_from_file_location("gtdb_ground", REPO / "scripts/gtdb_ground.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _grounding(gtdb) -> dict:
    """A grounding whose long scalars are long enough to wrap at any sane width."""
    return {
        "gtdb_id": "GTDB:g__Bosea",
        "gtdb_taxon": "Bosea",
        "gtdb_lineage": (
            "d__Bacteria;p__Pseudomonadota;c__Alphaproteobacteria;o__Rhizobiales;"
            "f__Beijerinckiaceae;g__Bosea"
        ),
        "ncbi_source_id": "NCBITaxon:85413",
        "majority_fraction": 1.0,
        "support_genomes": 34,
        "total_genomes": 34,
        "is_reclassified": False,
        "n_alt": 1,
        "via": "ncbi_rank_g",
    }


MAPPING_SOURCE = "kg-microbe NCBI2GTDB.tsv.gz; GTDB release latest (built 2026-07-25)"


def test_no_line_of_an_emitted_block_wraps(gtdb):
    """The property that matters: every key is one line, so a paste is safe."""
    emitted = gtdb.emit_block(_grounding(gtdb), MAPPING_SOURCE)

    orphans = [
        line for line in emitted.split("\n")[1:] if line.strip() and ":" not in line.split("#")[0]
    ]
    assert orphans == [], (
        "these lines carry no key, so they are continuations of a wrapped "
        f"scalar and a paste would indent them under the wrong parent: {orphans}"
    )


def test_both_render_paths_agree(gtdb):
    """`--emit-yaml` and `--apply` must produce the same bytes for one grounding.

    Rendering through each path separately and comparing is the point: a future
    change to one dump call — a width, a flow style, a sort — silently
    reintroduces #380 unless something notices the two diverging.
    """
    emitted = gtdb.emit_block(_grounding(gtdb), MAPPING_SOURCE)
    applied = yaml.dump(
        {"gtdb_classification": gtdb._block(_grounding(gtdb), MAPPING_SOURCE)},
        default_flow_style=False,
        sort_keys=False,
        allow_unicode=True,
        width=gtdb.DUMP_WIDTH,
    )
    assert emitted == applied


def test_an_emitted_block_round_trips(gtdb):
    """It parses back to the block it came from, indentation and all."""
    emitted = gtdb.emit_block(_grounding(gtdb), MAPPING_SOURCE)
    parsed = yaml.safe_load(emitted)["gtdb_classification"]
    assert parsed == gtdb._block(_grounding(gtdb), MAPPING_SOURCE)


def _run(*args):
    return subprocess.run(
        ["uv", "run", "python", "scripts/gtdb_ground.py", *args],
        capture_output=True,
        text=True,
        cwd=REPO,
        timeout=900,
    )


@pytest.mark.parametrize(
    ("label", "argv"),
    [
        (
            "--refresh without --apply",
            ["--community", "kb/communities/Richmond_Mine_AMD_Biofilm.yaml", "--refresh"],
        ),
        ("--refresh on a bare name lookup", ["--name", "Bosea", "--refresh"]),
    ],
)
def test_a_refresh_that_would_do_nothing_is_refused(label, argv):
    """Silently exiting 0 let a caller believe a re-ground had happened."""
    result = _run(*argv)
    assert result.returncode != 0, f"{label} should be refused, not silently ignored"
    assert "--refresh" in result.stderr


def test_refresh_with_apply_is_still_allowed(tmp_path):
    """The guard must not block the one combination that does work."""
    record = REPO / "kb/communities/Richmond_Mine_AMD_Biofilm.yaml"
    probe = tmp_path / record.name
    probe.write_text(record.read_text())

    result = _run("--community", str(probe), "--refresh", "--apply")
    assert result.returncode == 0, result.stderr[-400:]
