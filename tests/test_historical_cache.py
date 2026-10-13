"""Control, mutation and restoration checks for historical evidence provenance."""

import hashlib
import subprocess
from copy import deepcopy

import pytest
from historical_cache import assert_historical_cache_hash

PATH = "references_cache/fixture.txt"
ORIGINAL = b"Original article and supplementary evidence.\n"


@pytest.fixture
def repository(tmp_path):
    target = tmp_path / PATH
    target.parent.mkdir()
    target.write_bytes(ORIGINAL)
    for args in (
        ["init"],
        ["config", "user.name", "Provenance fixture"],
        ["config", "user.email", "fixture@example.invalid"],
        ["add", PATH],
        ["commit", "-m", "Historical evidence"],
    ):
        subprocess.run(["git", "-C", str(tmp_path), *args], check=True, capture_output=True)
    ledger = {
        key: subprocess.check_output(
            ["git", "-C", str(tmp_path), "rev-parse", revision], text=True
        ).strip()
        for key, revision in [("base_commit", "HEAD"), ("base_tree", "HEAD^{tree}")]
    }
    return tmp_path, ledger, hashlib.sha256(ORIGINAL).hexdigest()


def test_current_source_may_evolve_but_historical_hash_stays_enforced(repository):
    root, ledger, digest = repository
    assert_historical_cache_hash(root, ledger, PATH, digest)
    current = root / PATH
    current.write_bytes(b"Article only.\n")
    assert current.read_bytes() != ORIGINAL
    assert_historical_cache_hash(root, ledger, PATH, digest)
    changed_digest = hashlib.sha256(current.read_bytes()).hexdigest()
    assert changed_digest != digest
    with pytest.raises(AssertionError, match=PATH):
        assert_historical_cache_hash(root, ledger, PATH, changed_digest)
    current.unlink()
    assert_historical_cache_hash(root, ledger, PATH, digest)
    current.write_bytes(ORIGINAL)
    assert current.read_bytes() == ORIGINAL
    assert_historical_cache_hash(root, ledger, PATH, digest)


@pytest.mark.parametrize("field", ["base_commit", "base_tree"])
@pytest.mark.parametrize("mutation", ["missing", "unknown", "mutable"])
def test_missing_or_invalid_provenance_fails_closed(repository, field, mutation):
    root, ledger, digest = repository
    assert_historical_cache_hash(root, ledger, PATH, digest)
    altered = deepcopy(ledger)
    if mutation == "missing":
        del altered[field]
    else:
        altered[field] = "0" * 40 if mutation == "unknown" else "HEAD"
    assert altered != ledger
    with pytest.raises((AssertionError, KeyError, subprocess.CalledProcessError)):
        assert_historical_cache_hash(root, altered, PATH, digest)
    assert_historical_cache_hash(root, ledger, PATH, digest)


def test_missing_historical_path_cannot_fall_back_to_current_bytes(repository):
    root, ledger, digest = repository
    assert_historical_cache_hash(root, ledger, PATH, digest)
    missing = "references_cache/new.txt"
    (root / missing).write_bytes(ORIGINAL)
    assert (root / missing).read_bytes() == ORIGINAL
    with pytest.raises(subprocess.CalledProcessError):
        assert_historical_cache_hash(root, ledger, missing, digest)
    assert_historical_cache_hash(root, ledger, PATH, digest)


def test_legacy_commit_only_exception_is_explicit_and_never_ignores_present_tree(repository):
    root, ledger, digest = repository
    assert_historical_cache_hash(root, ledger, PATH, digest)
    legacy = deepcopy(ledger)
    del legacy["base_tree"]
    with pytest.raises(KeyError):
        assert_historical_cache_hash(root, legacy, PATH, digest)
    assert_historical_cache_hash(root, legacy, PATH, digest, allow_missing_tree=True)
    legacy["base_tree"] = "0" * 40
    assert legacy["base_tree"] != ledger["base_tree"]
    with pytest.raises(AssertionError, match="tree mismatch"):
        assert_historical_cache_hash(root, legacy, PATH, digest, allow_missing_tree=True)
    assert_historical_cache_hash(root, ledger, PATH, digest)


@pytest.mark.parametrize(
    "path", ["/references_cache/fixture.txt", "../fixture.txt", "kb/file.yaml"]
)
def test_only_cache_paths_are_historical_inputs(repository, path):
    root, ledger, digest = repository
    assert_historical_cache_hash(root, ledger, PATH, digest)
    with pytest.raises(AssertionError):
        assert_historical_cache_hash(root, ledger, path, digest)
    assert_historical_cache_hash(root, ledger, PATH, digest)
