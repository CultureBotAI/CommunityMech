"""A typo'd CURIE in data/isolates passed every gate in the repo (#471).

Two engines check (id, label) pairs. Engine A, `linkml-term-validator --labels`,
runs on isolates but **does not fail on an id it cannot resolve** — its
`--no-lenient` default catches a wrong label and silently skips a nonexistent
id. Engine B, `scripts/validate_id_label_correspondence.py`, does report
`ID_NOT_FOUND`, but its targets in `conf/id_label_targets.yaml` were
`kb/communities`, `kb/taxa`, and `output/kgx/nodes.tsv` — isolates were in
none. The CI step name said it gated `data/isolates`; for this defect class it
did not.

What was hiding there: `CHEBI:49782 "dysprosium(3+)"`, an id in no CHEBI
release. Its correction was *already decided* — recorded in NEXT_TASKS.md's
rare-earth table and in `chebi_fix_apply.py`'s REPOINT map — but that script
globbed `kb/communities` alone, so the fix never reached the record. A decision
that cannot reach every record is not yet applied.

These tests pin both halves: the config covers isolates, and the sweep script
does too.
"""

from __future__ import annotations

import ast
import pathlib

import pytest
import yaml

REPO = pathlib.Path(__file__).parent.parent
CONFIG = REPO / "conf/id_label_targets.yaml"
ISOLATES = REPO / "data/isolates"


def _targets() -> list[dict]:
    return yaml.safe_load(CONFIG.read_text())["targets"]


def test_engine_b_has_a_target_covering_the_isolates():
    """Without this, ID_NOT_FOUND is unreachable for every isolate record."""
    globs = [t.get("glob", "") for t in _targets()]
    assert any(g.startswith("data/isolates/") for g in globs), (
        "conf/id_label_targets.yaml has no data/isolates target, so Engine B "
        f"never reads those records and nothing else reports ID_NOT_FOUND for "
        f"them (#471). Current globs: {globs}"
    )


def test_that_target_checks_the_id_label_pair_canonically():
    """A target that checked some other pair, or leniently, would not close this."""
    target = next(t for t in _targets() if t.get("glob", "").startswith("data/isolates/"))
    assert target["policy"] == "canonical"
    assert ["id", "label"] in [list(p) for p in target["pairs"]]


def test_the_isolate_records_are_actually_matched_by_that_glob():
    """A target whose glob matches nothing passes vacuously."""
    target = next(t for t in _targets() if t.get("glob", "").startswith("data/isolates/"))
    # Glob from the repo root, which is what the validator does — resolving it
    # against data/isolates/ instead silently looked for data/isolates/isolates/
    # and matched nothing, so this test failed while the config was correct.
    matched = list(REPO.glob(target["glob"]))
    assert len(matched) >= 4, (
        f"{target['glob']!r} matches {len(matched)} files; the isolate records "
        f"are {sorted(p.name for p in ISOLATES.glob('*.yaml'))}"
    )


def _sweep_ast() -> tuple[set[str], ast.For]:
    """(directories in RECORD_DIRS, the loop that walks the records).

    Parsed rather than imported: the script does its OAK lookups at module
    scope, so importing it shells out to `runoak` for ~100 ids. Parsed rather
    than regexed because both regexes tried here were wrong in opposite
    directions — `([^)]*)` stopped inside the first `Path("...")`, and the
    `.*` that replaced it stops at the newline, so `black` splitting the tuple
    across lines (which a 4th directory would trigger — it is at 76 of 100
    columns now) would report an empty sweep set. An AST has neither failure
    mode.
    """
    tree = ast.parse((REPO / "scripts/chebi_fix_apply.py").read_text())

    dirs: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign) and any(
            isinstance(t, ast.Name) and t.id == "RECORD_DIRS" for t in node.targets
        ):
            for call in ast.walk(node.value):
                if (
                    isinstance(call, ast.Call)
                    and isinstance(call.func, ast.Name)
                    and call.func.id == "Path"
                    and call.args
                    and isinstance(call.args[0], ast.Constant)
                ):
                    dirs.add(call.args[0].value)

    loops = [
        node
        for node in ast.walk(tree)
        if isinstance(node, ast.For) and "glob" in ast.dump(node.iter)
    ]
    assert len(loops) == 1, f"expected one record-globbing loop, found {len(loops)}"
    return dirs, loops[0]


def test_the_chebi_sweep_reaches_every_record_directory():
    """The repoint table was right and unapplied because this globbed one dir."""
    dirs, _ = _sweep_ast()
    assert "data/isolates" in dirs, (
        "chebi_fix_apply.py does not sweep data/isolates, which is how the "
        "dysprosium repoint stayed unapplied while sitting in its own REPOINT "
        f"table (#471). It sweeps: {sorted(dirs)}"
    )
    assert "kb/communities" in dirs


def test_the_sweep_loop_actually_reads_that_constant():
    """Naming the directories is not sweeping them.

    The first version of this file asserted only on the value of RECORD_DIRS,
    which the review broke in one line: leave the constant exactly as written
    and revert the loop to `Path("kb/communities").glob("*.yaml")`. The whole
    suite stayed green while the precise regression this PR exists to prevent —
    a correction sitting in REPOINT that never reaches data/isolates — was
    fully reintroduced. A constant nothing reads is a comment.
    """
    _, loop = _sweep_ast()
    assert "RECORD_DIRS" in ast.dump(loop.iter), (
        "the record loop in chebi_fix_apply.py does not iterate RECORD_DIRS, so "
        "the directories declared there are decorative and the sweep can still "
        "miss data/isolates (#471)"
    )


def test_no_isolate_carries_the_nonexistent_dysprosium_id():
    """CHEBI:49782 is in no CHEBI release — not obsolete, absent.

    Pinned by id rather than by validator run so it fails in the fast test
    suite, with no ontology download.

    Checks parsed `id` values, not raw text: the record's curation note names
    the retired id in prose to explain the change, and a substring scan cannot
    tell that apart from the grounding itself — it flagged the very note that
    documents the fix.
    """
    offenders = []
    for path in sorted(ISOLATES.glob("*.yaml")):
        stack = [yaml.safe_load(path.read_text()) or {}]
        while stack:
            node = stack.pop()
            if isinstance(node, dict):
                if node.get("id") == "CHEBI:49782":
                    offenders.append(path.name)
                    break
                stack.extend(node.values())
            elif isinstance(node, list):
                stack.extend(node)
    assert offenders == [], (
        "CHEBI:49782 does not resolve in the OAK snapshot or at EBI; the "
        f"decided replacement is CHEBI:33377 'dysprosium atom' (#471): {offenders}"
    )


@pytest.mark.parametrize("record", sorted(p.name for p in ISOLATES.glob("*.yaml")))
def test_every_isolate_ontology_label_is_a_string_pair(record: str):
    """Guard for the sweep above: the pairs it checks must actually be there.

    If `term` blocks were restructured, the glob could keep matching while the
    (id, label) pairs it looks for no longer exist — passing for the wrong
    reason.
    """
    document = yaml.safe_load((ISOLATES / record).read_text()) or {}
    pairs, stack = 0, [document]
    while stack:
        node = stack.pop()
        if isinstance(node, dict):
            if isinstance(node.get("id"), str) and isinstance(node.get("label"), str):
                pairs += 1
            stack.extend(node.values())
        elif isinstance(node, list):
            stack.extend(node)
    assert pairs > 0, f"{record} carries no (id, label) pair for the gate to check"
