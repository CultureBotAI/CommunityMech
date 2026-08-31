"""A workflow that runs `just X` must trigger when `just X` changes (#717).

`label-correspondence.yaml` runs five recipes -- `kgx-export`,
`report-label-drift`, `validate-products`, `validate-terms-taxa`,
`validate-terms-all` -- and every one of them is DEFINED in the justfile. Its
paths filter listed `scripts/validate_id_label_correspondence.py` and
`conf/id_label_targets.yaml`, but not `justfile`.

So a PR that changes what those gates DO does not run them. Found the direct
way: the #708 PR rewired three of those recipes and `label-correspondence` did
not fire on it. Measured across the tree by parsing `run:` blocks rather than
whole files -- a first pass regexed the text and counted two workflows that only
MENTION just in a comment -- **three of the four** path-filtered workflows that
actually invoke a recipe had the hole: `curation-history`, `docs-current` and
`label-correspondence`. Only `validate-strict.yaml` already listed it.

This is the family the filter's own comments already describe one level down --
`data/isolates` outside every glob (#350), `kb/taxa` outside every trigger
(#471), `.claude/` outside every filter (#687). Those were about the DATA a gate
reads. This is about the gate's own definition, which is a shorter path to a
false green: the data can only make a gate miss a defect, the recipe can stop it
checking at all.

Deliberately not asserted here: that a workflow lists every file its recipes
transitively read. That is #636, it is not decidable by parsing, and conflating
the two would make this test unfalsifiable.
"""

from __future__ import annotations

import pathlib
import re

import pytest
import yaml

REPO = pathlib.Path(__file__).parent.parent
WORKFLOWS = REPO / ".github" / "workflows"

# `just <recipe>` in a run: block. Requires a recipe name so that prose using
# the word "just" cannot match -- the difference between a mention and a call
# (#700).
_JUST_CALL = re.compile(r"\bjust\s+(?:--[\w-]+\s+)*[a-z][\w-]*")


def _workflows() -> list[pathlib.Path]:
    return sorted(p for p in WORKFLOWS.glob("*.y*ml"))


def _run_blocks(document) -> list[str]:
    """Every `run:` script in a workflow, so prose and comments cannot match."""
    blocks: list[str] = []

    def walk(node):
        if isinstance(node, dict):
            for key, value in node.items():
                if key == "run" and isinstance(value, str):
                    blocks.append(value)
                else:
                    walk(value)
        elif isinstance(node, list):
            for item in node:
                walk(item)

    walk(document)
    return blocks


def _paths(document) -> set[str]:
    found: set[str] = set()

    def walk(node):
        if isinstance(node, dict):
            for key, value in node.items():
                if key == "paths" and isinstance(value, list):
                    found.update(str(item) for item in value)
                else:
                    walk(value)
        elif isinstance(node, list):
            for item in node:
                walk(item)

    walk(document)
    return found


def _invokes_just(document) -> bool:
    return any(_JUST_CALL.search(block) for block in _run_blocks(document))


def test_there_are_filtered_workflows_invoking_just():
    """Guard on the guard: if nothing matches, the test below proves nothing."""
    matching = [
        path.name
        for path in _workflows()
        if (doc := yaml.safe_load(path.read_text(encoding="utf-8")))
        and _paths(doc)
        and _invokes_just(doc)
    ]
    assert (
        len(matching) >= 3
    ), f"expected several path-filtered workflows invoking just; found {matching}"


@pytest.mark.parametrize("workflow", _workflows(), ids=lambda p: p.name)
def test_a_workflow_running_a_recipe_triggers_on_the_justfile(workflow: pathlib.Path):
    """If it runs `just X` and it filters by path, `justfile` is one of them."""
    document = yaml.safe_load(workflow.read_text(encoding="utf-8"))
    if not document:
        pytest.skip(f"{workflow.name} did not parse as a mapping")

    paths = _paths(document)
    if not paths:
        # An unfiltered workflow runs on everything, so it cannot have this hole.
        pytest.skip(f"{workflow.name} has no paths filter, so it always runs")
    if not _invokes_just(document):
        pytest.skip(f"{workflow.name} invokes no just recipe")

    assert any(entry.strip("\"'").startswith("justfile") for entry in paths), (
        f"{workflow.name} runs a just recipe but does not list `justfile` in its "
        f"paths filter, so editing that recipe does not run this gate (#717). "
        f"Current filter: {sorted(paths)}"
    )
