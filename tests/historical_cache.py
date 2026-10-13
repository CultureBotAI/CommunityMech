"""Verify immutable review inputs without freezing today's evidence cache (#1998)."""

import hashlib
import re
import subprocess
from pathlib import PurePosixPath


def assert_historical_cache_hash(root, ledger, path, digest, *, allow_missing_tree=False):
    base = ledger["base_commit"]
    assert re.fullmatch(r"[0-9a-f]{40}", base), "Expected an immutable review commit"
    commit = subprocess.check_output(
        ["git", "-C", str(root), "rev-parse", f"{base}^{{commit}}"], text=True
    ).strip()
    assert commit == base, "Historical review base must identify a commit"
    if not allow_missing_tree or "base_tree" in ledger:
        tree = subprocess.check_output(
            ["git", "-C", str(root), "rev-parse", f"{base}^{{tree}}"], text=True
        ).strip()
        assert tree == ledger["base_tree"], "Historical review tree mismatch"
    parts = PurePosixPath(path).parts
    assert len(parts) > 1 and parts[0] == "references_cache" and ".." not in parts, path
    content = subprocess.check_output(["git", "-C", str(root), "show", f"{base}:{path}"])
    assert hashlib.sha256(content).hexdigest() == digest, path
