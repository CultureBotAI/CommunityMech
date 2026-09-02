"""A gate that reads a generated artifact must build it first (#686).

`conf/id_label_targets.yaml` carries a `kgx_nodes` target globbing
`output/kgx/nodes.tsv`. `output/kgx/` is gitignored and holds zero tracked
files, and no CI job built the export before `just validate-products` ran. So
on every CI run the glob matched nothing, the target skipped, and the gate
printed::

    - kgx_nodes: no files match ['output/kgx/nodes.tsv']
    ✅ All id↔label pairs correspond.

Reproduced by moving the local artifact aside: exit 0, target skipped, gate
green. It was green by blindness, and three genuine CHEBI MISMATCHes
(europium/holmium/lutetium, all the `+ cation` typo already waived once for
mercury) were sitting behind the skip.

`output/kgx/**` in the workflow's own `paths:` filter was inert for the same
reason: no file under a gitignored directory can appear in a pull request.

Two conditions have to hold together, which is why this is one module rather
than a note in a comment:

* the workflow builds the artifact before the step that validates it, and
* the target is `required: true`, so an artifact that stops being produced is a
  MISSING_GLOB error rather than a silent skip.

Either alone restores the hole. A `required` target with nothing building it
fails every run; a build step with an optional target goes quiet again the day
the build breaks.
"""

from __future__ import annotations

import pathlib

import pytest
import yaml

REPO = pathlib.Path(__file__).parent.parent
CONFIG = REPO / "conf/id_label_targets.yaml"
WORKFLOW = REPO / ".github/workflows/label-correspondence.yaml"

# Directories whose contents are produced by a build rather than committed. A
# target globbing into one of these cannot rely on the checkout providing it.
_GENERATED_ROOTS = ("output/",)


def _targets() -> list[dict]:
    return (yaml.safe_load(CONFIG.read_text(encoding="utf-8")) or {}).get("targets") or []


def _globs(target: dict) -> list[str]:
    glob = target.get("glob")
    return glob if isinstance(glob, list) else [glob] if glob else []


def _generated_targets() -> list[dict]:
    return [
        target
        for target in _targets()
        if any(g.startswith(_GENERATED_ROOTS) for g in _globs(target))
    ]


def _steps() -> list[dict]:
    document = yaml.safe_load(WORKFLOW.read_text(encoding="utf-8")) or {}
    return [
        step for job in (document.get("jobs") or {}).values() for step in (job.get("steps") or [])
    ]


def test_there_is_a_generated_target_to_check():
    """Guard: with no such target every assertion below passes vacuously."""
    generated = _generated_targets()
    assert generated, (
        "no id↔label target globs into a generated directory any more. If that "
        "is deliberate, delete this module; if a target was renamed, update "
        "_GENERATED_ROOTS (#686)."
    )


@pytest.mark.parametrize("target", _generated_targets(), ids=lambda t: t["name"])
def test_a_generated_target_is_required(target):
    """Optional + generated = the exact combination that skipped silently."""
    assert target.get("required") is True, (
        f"target {target['name']!r} globs a generated path {_globs(target)} but is "
        f"not `required: true`. Without it a missing artifact is a skip, not an "
        f"error, and the gate reports success having read nothing (#686)."
    )


def _job_inputs() -> dict[str, str]:
    """The `with:` inputs of every job, flattened.

    The gate moved to a reusable workflow in claw (#731): a job that is `uses:`
    plus `with:` has no `steps:`, so the recipes are inputs now rather than
    `run:` lines. The local workflow names them explicitly instead of relying on
    claw's defaults, so what this repository runs stays readable here.
    """
    document = yaml.safe_load(WORKFLOW.read_text(encoding="utf-8")) or {}
    inputs: dict[str, str] = {}
    for job in (document.get("jobs") or {}).values():
        if isinstance(job, dict):
            for key, value in (job.get("with") or {}).items():
                inputs[key] = str(value)
    return inputs


def test_the_workflow_builds_the_export_before_it_validates():
    """Order matters: building after the check is the same as not building."""
    steps = _steps()
    runs = [(index, str(step.get("run") or "")) for index, step in enumerate(steps)]
    build = [index for index, run in runs if "kgx-export" in run]
    validate = [index for index, run in runs if "validate-products" in run]

    if not (build or validate):
        # The reusable-workflow form. Order is claw's to guarantee -- it runs
        # `prepare-recipe` before `enforce-recipe` -- so what this repository
        # can still assert is that the export IS named as the preparation for
        # the gate it feeds, and that both are named here rather than inherited
        # from a default in another repo.
        inputs = _job_inputs()
        assert inputs.get("enforce-recipe") == "validate-products", (
            "label-correspondence no longer names `validate-products` as its "
            f"enforce-recipe: {inputs.get('enforce-recipe')!r}"
        )
        assert "kgx-export" in inputs.get("prepare-recipe", ""), (
            "label-correspondence runs `validate-products`, whose kgx_nodes "
            "target reads output/kgx/ — gitignored and absent from a fresh "
            "checkout — but no prepare-recipe builds it (#686)."
        )
        return

    assert validate, "label-correspondence no longer runs `just validate-products`"
    assert build, (
        "label-correspondence runs `just validate-products`, whose kgx_nodes "
        "target reads output/kgx/ — a gitignored directory absent from a fresh "
        "checkout — but no step builds it. Add a `just kgx-export` step before "
        "the enforce step (#686)."
    )
    assert min(build) < min(validate), (
        f"`just kgx-export` runs at step {min(build)}, after `just "
        f"validate-products` at step {min(validate)}. Building the artifact "
        f"after the gate reads it leaves the gate reading nothing (#686)."
    )


def test_no_other_workflow_runs_the_gate_without_building():
    """This module names one workflow; a second one running the gate is a hole.

    The checks above read `label-correspondence.yaml` because that is where the
    gate lives today. If another workflow starts running `just
    validate-products` without a `just kgx-export` before it, the target skips
    there exactly as it did here — and every assertion above would still pass,
    because they are looking at a different file.
    """
    offenders = []
    for path in sorted(WORKFLOW.parent.glob("*.y*ml")):
        document = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        runs = [
            str(step.get("run") or "")
            for job in (document.get("jobs") or {}).values()
            for step in (job.get("steps") or [])
        ]
        validates = [index for index, run in enumerate(runs) if "validate-products" in run]
        builds = [index for index, run in enumerate(runs) if "kgx-export" in run]
        if validates and (not builds or min(builds) > min(validates)):
            offenders.append(path.name)

    assert offenders == [], (
        "these workflows run `just validate-products` without building "
        "output/kgx first, so its kgx_nodes target skips and the gate passes "
        f"having read nothing (#686): {offenders}"
    )


def test_the_report_step_also_gets_the_artifact():
    """The drift report reads the same targets; it must not run before the build.

    It is the triage artifact people read when the gate fails, so a report
    generated without the export would quietly under-report exactly when it
    matters most.
    """
    runs = [(index, str(step.get("run") or "")) for index, step in enumerate(_steps())]
    build = [index for index, run in runs if "kgx-export" in run]
    report = [index for index, run in runs if "report-label-drift" in run]
    if not report:
        pytest.skip("workflow no longer generates the drift report")
    assert build and min(build) < min(report), (
        "`just report-label-drift` reads the same config as the gate, so it "
        "must run after `just kgx-export` too (#686)."
    )
