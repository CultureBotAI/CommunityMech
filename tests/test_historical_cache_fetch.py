"""Exercise the actual CI prerequisite without relying on retained local objects."""

import hashlib
import shlex
import subprocess
from pathlib import Path

import pytest
import yaml
from historical_cache import assert_historical_cache_hash

ROOT = Path(__file__).resolve().parents[1]
LEDGERS = [
    "20261005-three-records-batch15.yaml",
    "20261006-ginseng-s11-batch48.yaml",
    "20261006-assay-boundaries-batch64.yaml",
    "20261007-four-records-batch88.yaml",
    "20261007-four-records-batch92.yaml",
]


def workflow_command():
    workflow = yaml.safe_load((ROOT / ".github/workflows/validate-strict.yaml").read_text())
    steps = workflow["jobs"]["validate-strict"]["steps"]
    index = next(
        i for i, s in enumerate(steps) if s.get("name") == "Fetch historical cache review bases"
    )
    assert index < next(i for i, s in enumerate(steps) if s.get("name") == "Run tests")
    step = steps[index]
    assert not any(key in step for key in ("if", "continue-on-error"))
    command = shlex.split(step["run"].replace("\\\n", ""))
    assert command[:4] == ["git", "fetch", "--no-tags", "origin"]
    expected = [
        yaml.safe_load((ROOT / "reports/causal_graph_review/decisions" / name).read_text())[
            "base_commit"
        ]
        for name in LEDGERS
    ]
    assert command[4:] == expected
    return command


def git(root, *args):
    return subprocess.check_output(["git", "-C", str(root), *args], text=True).strip()


def test_workflow_fetches_exact_ledger_bases_before_all_test_events():
    workflow_command()


def test_actual_fetch_control_mutation_and_restoration_in_fresh_clones(tmp_path):
    remote = tmp_path / "remote"
    remote.mkdir()
    git(remote, "init", "-q", "-b", "main")
    git(remote, "config", "user.name", "Provenance fixture")
    git(remote, "config", "user.email", "fixture@example.invalid")
    git(remote, "commit", "--allow-empty", "-qm", "Main")
    git(remote, "switch", "-qc", "historical")
    path = "references_cache/fixture.txt"
    (remote / path).parent.mkdir()
    inputs = []
    for i in range(5):
        content = f"Historical evidence {i}.\n".encode()
        (remote / path).write_bytes(content)
        git(remote, "add", path)
        git(remote, "commit", "-qm", "Historical source")
        inputs.append(
            (
                {
                    "base_commit": git(remote, "rev-parse", "HEAD"),
                    "base_tree": git(remote, "rev-parse", "HEAD^{tree}"),
                },
                hashlib.sha256(content).hexdigest(),
            )
        )
    git(remote, "switch", "-q", "main")
    git(remote, "branch", "-D", "historical")
    command = workflow_command()[:4] + [ledger["base_commit"] for ledger, _ in inputs]
    for arm in ("control", "mutation", "restoration"):
        clone = tmp_path / arm
        git(tmp_path, "clone", "-q", "--no-local", "--single-branch", str(remote), str(clone))
        for ledger, digest in inputs:
            with pytest.raises(subprocess.CalledProcessError):
                assert_historical_cache_hash(clone, ledger, path, digest)
        run = command.copy()
        if arm == "mutation":
            run[-1] = "0" * 40
            assert run != command and run.count("0" * 40) == 1
        else:
            assert run == command
        result = subprocess.run(run, cwd=clone, capture_output=True)
        if arm == "mutation":
            assert result.returncode != 0
        else:
            assert result.returncode == 0, result.stderr
            for ledger, digest in inputs:
                assert_historical_cache_hash(clone, ledger, path, digest)
