"""A local `just report-label-drift` run must not leave the checkout dirty (#1089).

The recipe writes its drift report into reports/. The label-correspondence CI
workflow regenerates that file and uploads it as an artifact; it is never
committed, so .gitignore names it. Unignored, one local run leaves an untracked
file, and claw's fleet pull skips any checkout whose `git status --porcelain` is
not empty (`skipped_dirty`), which is how the gap was found.

The rule is deliberately narrow. Five reports/*.tsv files are tracked (#391
weighed ignoring instance_validation_failures.tsv; #406 kept it tracked), so the
second test pins that no tracked report is ignored: widening the rule to
reports/*.tsv goes red instead of silently hiding the next TSV deliverable.

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

# Only committed ignore rules count. This switches off a contributor's global
# excludes file; .git/info/exclude cannot be switched off, so the first test also
# checks which file the matching rule came from.
_GIT = ["git", "-c", f"core.excludesFile={os.devnull}"]

# Tracked files that a .gitignore rule matches (info/exclude is not read).
_TRACKED_BUT_IGNORED = ("--cached", "--ignored", "--exclude-per-directory=.gitignore")


def _drift_report_path() -> str:
    """The --report argument of `just report-label-drift`, as just would run it."""
    # A contributor's JUST_* settings must not reach the echo: JUST_COLOR=always
    # appends an ANSI reset to the path and JUST_QUIET=true rejects --dry-run.
    env = {key: value for key, value in os.environ.items() if not key.startswith("JUST_")}
    result = subprocess.run(
        ["just", "--color", "never", "--dry-run", "report-label-drift"],
        cwd=REPO,
        env=env,
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
    # -z needs --stdin. With -v, git also reports a matching negated ("!") rule,
    # so both the rule's file and its pattern are checked.
    result = subprocess.run(
        [*_GIT, "check-ignore", "-v", "-z", "--stdin", "--no-index"],
        cwd=REPO,
        input=f"{path}\0",
        capture_output=True,
        text=True,
    )
    source, _line, pattern, _path = (result.stdout.split("\0") + ["", "", "", ""])[:4]
    assert Path(source).name == ".gitignore" and not pattern.startswith("!"), (
        f"`just report-label-drift` writes {path}, which no committed .gitignore rule "
        f"ignores (matched: {source or 'nothing'} {pattern!r}): a local run leaves an "
        "untracked file and claw's fleet pull skips the checkout"
    )


def _git_paths(*args: str, cwd: Path = REPO) -> list[str]:
    result = subprocess.run(
        [*_GIT, "ls-files", "-z", *args, "--", "reports/"],
        cwd=cwd,
        check=True,
        capture_output=True,
        text=True,
    )
    return [path for path in result.stdout.split("\0") if path]


def test_the_tracked_but_ignored_query_can_find_one(tmp_path: Path):
    """Positive control: an empty answer below must mean 'none', not 'unreadable'."""
    subprocess.run(["git", "init", "-q", str(tmp_path)], check=True)
    (tmp_path / ".gitignore").write_text("reports/*.tsv\n")
    (tmp_path / "reports").mkdir()
    (tmp_path / "reports" / "planted.tsv").write_text("x\n")
    subprocess.run(["git", "add", "-f", "reports/planted.tsv"], cwd=tmp_path, check=True)
    assert _git_paths(*_TRACKED_BUT_IGNORED, cwd=tmp_path) == ["reports/planted.tsv"]


def test_no_tracked_report_is_ignored():
    assert _git_paths(), "git lists no tracked file under reports/; nothing was checked"
    ignored = _git_paths(*_TRACKED_BUT_IGNORED)
    assert ignored == [], (
        "tracked reports match an ignore rule, so a new sibling matching it would be "
        "silently left out of a commit; keep report ignore rules per file:\n"
        + "\n".join(f"  {path}" for path in ignored)
    )
