"""The cleanup recipe must never target a tracked repository file (#663)."""

from __future__ import annotations

import glob
import shlex
import subprocess
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent


def _tracked_paths() -> set[Path]:
    result = subprocess.run(
        ["git", "ls-files", "-z"],
        cwd=REPO,
        check=True,
        capture_output=True,
    )
    return {
        (REPO / path.decode()).resolve()
        for path in result.stdout.split(b"\0")
        if path
    }


def _clean_commands() -> list[list[str]]:
    result = subprocess.run(
        ["just", "--dry-run", "clean"],
        cwd=REPO,
        check=True,
        capture_output=True,
        text=True,
    )
    return [shlex.split(line) for line in result.stdout.splitlines() if line.strip()]


def test_clean_targets_no_tracked_files():
    """Expand every cleanup target and compare it with the Git index.

    This catches both an explicit tracked path and a broad glob such as
    ``docs/*.md``. New cleanup commands must stay simple enough for this audit;
    dynamic shell expressions would make a destructive recipe harder to review.
    """
    tracked = _tracked_paths()
    offenders: set[Path] = set()

    for command in _clean_commands():
        assert command[:2] == ["rm", "-rf"], f"unaudited clean command: {command}"
        for target in command[2:]:
            assert not any(token in target for token in ("$", "`", "$(")), (
                f"clean target must be an explicit path or glob: {target}"
            )
            matches = glob.glob(str(REPO / target), recursive=True)
            offenders.update(Path(match).resolve() for match in matches if Path(match).is_file())

    assert not offenders & tracked, (
        "clean would delete tracked files:\n"
        + "\n".join(str(path.relative_to(REPO)) for path in sorted(offenders & tracked))
    )


def test_clean_keeps_tracked_datamodel_and_documentation_out_of_its_commands():
    rendered = "\n".join(" ".join(command) for command in _clean_commands())

    assert "src/communitymech/datamodel" not in rendered
    assert "docs/" not in rendered
