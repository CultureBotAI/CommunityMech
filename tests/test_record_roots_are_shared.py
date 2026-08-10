"""Every gate looks at the same record directories (#350).

`data/isolates/**` was added to the network-quality workflow's trigger paths,
and separately to `validate_strict`, `validate-all`, `validate-terms-all` and
`validate-references-all`. The network auditor was not: it kept
`communities_dir: Path = Path("kb/communities")`. So editing an isolate re-ran a
suite whose only isolate coverage was schema validation, and the interactions in
`data/isolates` — 12 of them across 3 records — were never audited at all.

Nothing was wrong with any of them, which is the point. The gap was invisible
because it produced no findings either way, and would have stayed invisible
until an isolate gained a dangling reference.

`default_record_roots()` is now the single source, in `communitymech.paths`, and
this file checks the places that must agree with it. Two of those checks are
about *shape* rather than content, because the failure mode was never a wrong
list — it was a second list nobody remembered existed:

* the CLI's `--communities-dir` must default to `None`. It defaulted to the
  string `"kb/communities"`, which silently overrode the auditor's own default:
  after the auditor was fixed, `audit-network` still reported 312 records. The
  fix looked wired and was not, and only running it and reading the count found
  that.
* the workflow's trigger paths must mention every root. A gate that covers a
  directory but never fires on changes to it is covered only by accident.
"""

from __future__ import annotations

import ast
import pathlib

import pytest
import yaml

from communitymech.paths import default_record_roots

REPO = pathlib.Path(__file__).parent.parent
WORKFLOW = REPO / ".github/workflows/network-quality.yml"


@pytest.fixture(scope="module")
def roots() -> list[pathlib.Path]:
    return default_record_roots()


def test_the_roots_exist_and_hold_records(roots):
    """Guard: a root that does not exist makes every sweep below vacuous."""
    assert len(roots) >= 2
    for root in roots:
        assert root.is_dir(), f"{root} is not a directory"
        assert list(root.glob("*.yaml")), f"{root} holds no records"


def test_the_auditor_defaults_to_all_of_them(roots):
    """The defect itself: the audit saw one root while the validators saw two."""
    from communitymech.network.auditor import NetworkIntegrityAuditor

    assert NetworkIntegrityAuditor().record_dirs == roots


def test_a_single_directory_is_still_accepted():
    """`NetworkIntegrityAuditor(tmp_path)` must keep meaning what it did.

    Widening the default would be a poor trade if it broke every caller and
    test that audits one directory deliberately.
    """
    from communitymech.network.auditor import NetworkIntegrityAuditor

    only = REPO / "kb/communities"
    assert NetworkIntegrityAuditor(only).record_dirs == [only]
    assert NetworkIntegrityAuditor([only]).record_dirs == [only]


def test_validate_strict_uses_the_shared_list():
    """Parsed, not imported: importing the script pulls in linkml and forks.

    Asserted positively — that `DEFAULT_ROOTS` is assigned from a call to
    `default_record_roots` — rather than by checking the old literals are
    absent, which would also pass on a file that stopped defining roots.
    """
    tree = ast.parse((REPO / "scripts/validate_strict.py").read_text(encoding="utf-8"))
    assignments = [
        node
        for node in ast.walk(tree)
        if isinstance(node, ast.Assign)
        and any(isinstance(t, ast.Name) and t.id == "DEFAULT_ROOTS" for t in node.targets)
    ]
    assert len(assignments) == 1, "DEFAULT_ROOTS is gone or defined more than once"
    value = assignments[0].value
    assert isinstance(value, ast.Call), "DEFAULT_ROOTS is a literal again, not the shared list"
    assert getattr(value.func, "id", None) == "default_record_roots"


def test_the_cli_does_not_override_the_default():
    """A literal default here silently defeats the auditor's own (#350).

    This is the check that would have caught the half-fix: the auditor was
    already correct while `audit-network` still reported 312 records, because
    click passed `"kb/communities"` explicitly on every invocation.
    """
    tree = ast.parse((REPO / "src/communitymech/cli.py").read_text(encoding="utf-8"))
    # Scoped to `audit_network`'s own decorators. A module-wide sweep also flags
    # `generate-umap`, which takes the same option name but is a visualisation
    # rather than a gate — whether isolates belong in the UMAP is a separate
    # question (#519), not something to settle by widening this test.
    command = next(
        node
        for node in ast.walk(tree)
        if isinstance(node, ast.FunctionDef) and node.name == "audit_network"
    )
    offenders = []
    for node in command.decorator_list:
        if not isinstance(node, ast.Call):
            continue
        if getattr(node.func, "attr", None) != "option":
            continue
        names = [a.value for a in node.args if isinstance(a, ast.Constant)]
        if "--communities-dir" not in names:
            continue
        for keyword in node.keywords:
            if keyword.arg == "default" and not (
                isinstance(keyword.value, ast.Constant) and keyword.value.value is None
            ):
                offenders.append(ast.unparse(keyword.value))
    assert offenders == [], (
        "`--communities-dir` has a non-None default "
        f"({offenders}), which overrides `default_record_roots()` and drops "
        "`data/isolates` from the audit without changing anything visible (#350)"
    )


def test_the_workflow_fires_on_every_root(roots):
    """A gate that covers a directory but never triggers on it is luck."""
    workflow = yaml.safe_load(WORKFLOW.read_text(encoding="utf-8"))
    # `on` is parsed as the boolean True by YAML 1.1, which is why this reads
    # the key rather than the attribute.
    triggers = workflow.get("on") or workflow.get(True)
    patterns = triggers["pull_request"]["paths"]
    missing = [
        str(root.relative_to(REPO))
        for root in roots
        if not any(str(root.relative_to(REPO)) in pattern for pattern in patterns)
    ]
    assert missing == [], (
        "the network-quality workflow audits these directories but does not "
        f"trigger on changes to them: {missing}. Add them to `paths:` (#350)."
    )
