"""A local `just report-label-drift` run must not leave the checkout dirty (#1089).

The recipe writes its drift report into reports/. The label-correspondence CI
workflow regenerates that file and uploads it as an artifact; it is never
committed, so .gitignore names it. Unignored, one local run leaves an untracked
file, and claw's fleet pull skips any checkout whose `git status --porcelain` is
not empty (`skipped_dirty`), which is how the gap was found.

The rule is deliberately narrow. Five reports/*.tsv files are tracked on purpose
(#391/#406), so the second test pins that no tracked report is ignored: widening
the rule to reports/*.tsv goes red instead of silently hiding the next TSV
deliverable.

Both tests read what decides the answer -- the recipe's own --report argument
and git's index -- rather than restating the .gitignore line, and neither can
pass by finding nothing to check.
"""

from __future__ import annotations

import os
import shlex
import subprocess
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent

# Only the repository's ignore rules count: a contributor's global excludes file
# must not decide whether this passes.
_GIT = ["git", "-c", f"core.excludesFile={os.devnull}"]


def _drift_report_path() -> str:
    """The --report argument of `just report-label-drift`, as just would run it."""
    result = subprocess.run(
        ["just", "--dry-run", "report-label-drift"],
        cwd=REPO,
        check=True,
        capture_output=True,
        text=True,
    )
    # `just --dry-run` echoes the recipe on stderr; stdout is empty.
    paths = []
    for line in result.stderr.splitlines():
        words = shlex.split(line, comments=True)
        paths += [words[i + 1] for i, word in enumerate(words[:-1]) if word == "--report"]
    assert len(paths) == 1, f"expected one --report argument in the recipe, found {paths}"
    return paths[0]


def test_the_drift_report_the_recipe_writes_is_ignored():
    path = _drift_report_path()
    assert path.startswith("reports/"), path
    result = subprocess.run([*_GIT, "check-ignore", "-q", "--no-index", path], cwd=REPO)
    assert result.returncode == 0, (
        f"`just report-label-drift` writes {path}, which .gitignore does not ignore: "
        "a local run leaves an untracked file and claw's fleet pull skips the checkout"
    )


def _git_paths(*args: str) -> list[str]:
    result = subprocess.run(
        [*_GIT, "ls-files", "-z", *args, "--", "reports/"],
        cwd=REPO,
        check=True,
        capture_output=True,
        text=True,
    )
    return [path for path in result.stdout.split("\0") if path]


def test_no_tracked_report_is_ignored():
    assert _git_paths(), "git lists no tracked file under reports/; nothing was checked"
    ignored = _git_paths("--cached", "--ignored", "--exclude-per-directory=.gitignore")
    assert ignored == [], (
        "tracked reports match an ignore rule, so a regenerated sibling would be "
        "silently left out of a commit; keep report ignore rules per file:\n"
        + "\n".join(f"  {path}" for path in ignored)
    )
