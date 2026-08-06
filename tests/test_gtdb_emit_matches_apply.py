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
        "gtdb_id": "GTDB:s__Bosea_lathyri",
        "gtdb_taxon": "Bosea lathyri",
        # A species lineage on purpose: its final segment carries a space, so
        # `gtdb_lineage` can actually wrap. The genus lineage this fixture used
        # first has none, so it could not — leaving the scalar the module
        # comment names as a wrapping risk untested.
        "gtdb_lineage": (
            "d__Bacteria;p__Pseudomonadota;c__Alphaproteobacteria;o__Rhizobiales;"
            "f__Beijerinckiaceae;g__Bosea;s__Bosea lathyri"
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

    # Detect by indentation, not by looking for a colon: a wrapped scalar can
    # carry one (`mapping_source` splits after "release latest:"-shaped text),
    # and the earlier heuristic would have called that line a key.
    body = [line for line in emitted.split("\n")[1:] if line.strip()]
    orphans = [line for line in body if len(line) - len(line.lstrip()) != 2]
    assert orphans == [], (
        "these lines carry no key, so they are continuations of a wrapped "
        f"scalar and a paste would indent them under the wrong parent: {orphans}"
    )


def test_both_render_paths_agree(gtdb, tmp_path):
    """What `--emit-yaml` prints must be what `--apply` writes, modulo indent.

    Comparing `emit_block` against a locally rebuilt `yaml.dump` was a
    tautology: it restated `emit_block`'s own body, so it passed for any
    `DUMP_WIDTH` and never touched `apply_to_community` — whose dump is a
    *different* call, on the inner block, with its own flow-style and
    hand-prefixed indent. Changing the apply side left it green, which is
    exactly the regression this file exists to catch.

    So run the real thing: apply a block to a record and read back what landed.
    """
    record = tmp_path / "Probe.yaml"
    record.write_text(
        "id: CommunityMech:TEST\n"
        "name: probe\n"
        "taxonomy:\n"
        "- taxon_term:\n"
        "    preferred_term: Bosea\n"
        "    term:\n"
        "      id: NCBITaxon:85413\n"
        "      label: Bosea\n"
    )
    result = subprocess.run(
        ["uv", "run", "python", "scripts/gtdb_ground.py", "--community", str(record), "--apply"],
        capture_output=True,
        text=True,
        cwd=REPO,
        timeout=900,
    )
    assert result.returncode == 0, result.stderr[-400:]

    written = record.read_text().split("\n")
    start = next(i for i, line in enumerate(written) if line.strip() == "gtdb_classification:")
    applied = [written[start]]
    for line in written[start + 1 :]:
        if line.strip() and len(line) - len(line.lstrip()) <= len(applied[0]) - len(
            applied[0].lstrip()
        ):
            break
        applied.append(line)

    def _dedent(lines):
        pad = len(lines[0]) - len(lines[0].lstrip())
        return [line[pad:].rstrip() for line in lines if line.strip()]

    emitted = gtdb.emit_block(_grounding(gtdb), MAPPING_SOURCE).split("\n")
    # Same shape, key for key — the values differ only where the fixture does.
    assert [line.split(":")[0] for line in _dedent(applied)] == [
        line.split(":")[0] for line in _dedent(emitted)
    ]
    for line in _dedent(applied)[1:]:
        assert len(line) - len(line.lstrip()) == 2, f"apply wrapped a scalar: {line!r}"


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
