"""Where the count-coherence constraint actually lives, and where it does not (#387).

`support_genomes` and `total_genomes` are typed and bounded individually, but
nothing in the schema relates them to each other or to `majority_fraction`. #387
asked whether that could be fixed in LinkML. The spike says no, for two
independent reasons:

* `equals_expression` — the obvious candidate, e.g.
  ``{support_genomes} / {total_genomes}`` — is LinkML's **inference** machinery,
  not a constraint. A block declaring 99/3 with a ratio of 0.1 validates clean.
* `rules` compile to JSON Schema, which can compare a property to a *literal*
  and never to another property.

So the constraint lives in `communitymech.validators.gtdb_coherence`, and the
guarantee is: **an incoherent block cannot reach `main`**, because
`validate-strict` is a CI gate and rejects it. What it is not: `just validate`
alone will pass one.

These tests pin both halves. The negative ones matter as much as the positive:
if LinkML ever gains the ability, `test_linkml_validate_still_cannot_catch_it`
starts failing, which is the signal to move the constraint into the schema where
it belongs and delete this file's reason for existing.
"""

from __future__ import annotations

import os
import subprocess
import tempfile
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).parent.parent
SCHEMA = REPO / "src/communitymech/schema/communitymech.yaml"
FIXTURE = REPO / "kb/communities/Lake_Washington_Methane_Oxygen_Methylotroph_Community.yaml"

# Two of the three instances #387 probed — the ones needing cross-field
# arithmetic. The third, `total_genomes: 0`, is a bound on a *single* value, so
# the schema can express it and `minimum_value: 1` now does; it gets its own test
# below precisely because it is the case that behaves differently.
INCOHERENT = {
    "support exceeds total": {"support_genomes": 99, "total_genomes": 3, "majority_fraction": 0.1},
    "fraction contradicts the counts": {
        "support_genomes": 2,
        "total_genomes": 9999,
        "majority_fraction": 1.0,
    },
}
COHERENT = {"support_genomes": 15, "total_genomes": 15, "majority_fraction": 1.0}


def _record_with(mutation: dict, drop: tuple[str, ...] = ()) -> str:
    """The fixture record with its first grounding block mutated. Returns YAML.

    `drop` removes keys, which matters for isolating a single constraint: to
    test that `total_genomes: 0` is rejected *for being zero*, the block must not
    also carry a `support_genomes` that violates its own bound.
    """
    document = yaml.safe_load(FIXTURE.read_text())
    for entry in document["taxonomy"]:
        block = (entry.get("taxon_term") or {}).get("gtdb_classification")
        if block:
            for key in drop:
                block.pop(key, None)
            block.update(mutation)
            return yaml.dump(document, sort_keys=False, allow_unicode=True)
    raise AssertionError("fixture has no gtdb_classification; this test is stale")


def _run(command: list[str], path: Path) -> int:
    return subprocess.run(
        command + [str(path)],
        capture_output=True,
        cwd=REPO,
        env={**os.environ, "PYTHONPATH": "src"},
        timeout=900,
    ).returncode


@pytest.mark.parametrize("label", sorted(INCOHERENT))
def test_linkml_validate_still_cannot_catch_it(label):
    """The gap #387 records — asserted for years, now actually probed.

    If this starts *failing*, LinkML gained cross-field constraints and the
    check should move into the schema.
    """
    with tempfile.TemporaryDirectory() as directory:
        path = Path(directory) / "probe.yaml"
        path.write_text(_record_with(INCOHERENT[label]))
        assert _run(["uv", "run", "linkml-validate", "-s", str(SCHEMA)], path) == 0, (
            f"linkml-validate now rejects {label!r} — move the constraint into "
            f"the schema and simplify this test (#387)"
        )


@pytest.mark.parametrize("label", sorted(INCOHERENT))
def test_the_coherence_validator_catches_it(label):
    with tempfile.TemporaryDirectory() as directory:
        path = Path(directory) / "probe.yaml"
        path.write_text(_record_with(INCOHERENT[label]))
        assert (
            _run(["uv", "run", "python", "scripts/validate_gtdb_coherence.py"], path) != 0
        ), f"validate-gtdb passed {label!r}"


@pytest.mark.parametrize("label", sorted(INCOHERENT))
def test_the_ci_gate_catches_it(label):
    """The guarantee that actually matters: this cannot reach `main`.

    `validate-strict` runs in CI on every PR touching the record trees, so it is
    the reason #387 is a documentation gap rather than a correctness hole.
    """
    with tempfile.TemporaryDirectory() as directory:
        path = Path(directory) / "Bad_Record.yaml"
        path.write_text(_record_with(INCOHERENT[label]))
        result = subprocess.run(
            [
                "uv",
                "run",
                "python",
                "scripts/validate_strict.py",
                str(path),
                "--out",
                str(Path(directory) / "report.tsv"),
            ],
            capture_output=True,
            text=True,
            cwd=REPO,
            timeout=900,
        )
        assert result.returncode != 0, f"validate-strict passed {label!r}"
        assert "gtdb_" in (result.stdout + result.stderr), "failed for an unrelated reason"


def test_a_zero_denominator_is_the_one_the_schema_can_express():
    """`minimum_value` bounds one value, which is exactly why this one works.

    `support_genomes` is dropped rather than set to 0. Setting it to 0 violates
    *its own* `minimum_value: 1`, so the record would be rejected whatever
    `total_genomes` did — the test passed while proving nothing, and survived a
    mutation that set `total_genomes`'s bound to 0.
    """
    with tempfile.TemporaryDirectory() as directory:
        good, bad = Path(directory) / "good.yaml", Path(directory) / "bad.yaml"
        bad.write_text(_record_with({"total_genomes": 0}, drop=("support_genomes",)))
        good.write_text(_record_with({"total_genomes": 1}, drop=("support_genomes",)))

        assert _run(["uv", "run", "linkml-validate", "-s", str(SCHEMA)], bad) != 0
        # The control: without it, any unrelated breakage in the probe record
        # would make the assertion above pass.
        assert _run(["uv", "run", "linkml-validate", "-s", str(SCHEMA)], good) == 0


def test_a_coherent_block_passes_everything():
    """Two-sided: a gate that rejects the good case is worse than none."""
    with tempfile.TemporaryDirectory() as directory:
        path = Path(directory) / "probe.yaml"
        path.write_text(_record_with(COHERENT))
        assert _run(["uv", "run", "linkml-validate", "-s", str(SCHEMA)], path) == 0
        assert _run(["uv", "run", "python", "scripts/validate_gtdb_coherence.py"], path) == 0


def test_equals_expression_is_inference_not_validation(tmp_path):
    """Why the obvious LinkML answer does not work — demonstrated, not asserted.

    This is the spike #387 asked for, kept as a test so the claim in the schema
    stays honest. `equals_expression` populates a value; it never rejects one.
    """
    schema = tmp_path / "spike.yaml"
    schema.write_text(
        "id: https://example.org/spike\n"
        "name: spike\n"
        "prefixes: {linkml: https://w3id.org/linkml/, ex: 'https://example.org/spike/'}\n"
        "default_prefix: ex\n"
        "imports: [linkml:types]\n"
        "classes:\n"
        "  Block:\n"
        "    tree_root: true\n"
        "    attributes:\n"
        "      support_genomes: {range: integer}\n"
        "      total_genomes: {range: integer}\n"
        "      ratio:\n"
        "        range: float\n"
        '        equals_expression: "{support_genomes} / {total_genomes}"\n'
    )
    instance = tmp_path / "bad.yaml"
    instance.write_text("support_genomes: 99\ntotal_genomes: 3\nratio: 0.1\n")

    accepted = (
        subprocess.run(
            ["uv", "run", "linkml-validate", "-s", str(schema), str(instance)],
            capture_output=True,
            cwd=REPO,
            timeout=900,
        ).returncode
        == 0
    )

    assert accepted, (
        "equals_expression now constrains rather than infers — LinkML gained "
        "cross-field validation and #387 can be solved in the schema"
    )
