"""Verify bounded M5 successors without rewriting historical reviews (#2782)."""

import hashlib
import json
import subprocess

import yaml
from phase2_review_successor import TARGETS
from phase2_review_successor import current_record_sha256 as phase2_record_sha256

PROVENANCE = "reports/m5-completion-20261114/successor-provenance.yaml"
BASELINE = "76aa644cd6803ea2c9545d4c704276ede219d354"


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def load_provenance(root):
    result = yaml.safe_load((root / PROVENANCE).read_text())
    assert result["source_baseline"] == BASELINE
    assert result["independent_approval"] is False
    for group, key in (("records", "id"), ("cache_corrections", "path")):
        assert len({row[key] for row in result[group]}) == len(result[group])
    return result


def original(root, path):
    # This is the main-branch baseline, not an off-main review commit.
    return subprocess.check_output(["git", "show", f"{BASELINE}:{path}"], cwd=root)


def read_artifact(root, artifact):
    raw = (root / artifact["path"]).read_bytes()
    assert digest(raw) == artifact["sha256"], artifact["path"]
    return raw


def current_record_sha256(root, predecessor, row, *, provenance=None, current=None):
    provenance = load_provenance(root) if provenance is None else provenance
    matches = [candidate for candidate in provenance["records"] if candidate["id"] == row["id"]]
    if not matches:
        return row["record_sha256"]
    assert len(matches) == 1
    successor = matches[0]
    assert successor["path"] == row["path"]
    assert successor["supersedes_review"] == {
        "review_file": str(predecessor.relative_to(root)),
        "record_sha256": row["record_sha256"],
    }
    before = digest(original(root, row["path"]))
    assert before == row["record_sha256"] == successor["original_sha256"]
    read_artifact(root, successor["scientific_review"])
    assert successor["curation_receipts"]
    for artifact in successor["curation_receipts"]:
        receipt = json.loads(read_artifact(root, artifact))
        assert receipt["path"] == row["path"] and receipt["applied"] is True
        assert receipt["before_sha256"] == before
        before = receipt["after_sha256"]
    assert before == successor["record_sha256"]
    current = (root / row["path"]).read_bytes() if current is None else current
    if row["path"] in TARGETS:
        return phase2_record_sha256(root, row["path"], before, current=current)
    assert digest(current) == before
    return before


def assert_header_only_cache_change(previous, current):
    assert previous.startswith(b"---\n") and current.startswith(b"---\n")
    before_header, before_marker, before_body = previous.partition(b"\n---\n")
    after_header, after_marker, after_body = current.partition(b"\n---\n")
    assert before_marker and after_marker
    assert before_body == after_body, "article body changed"
    assert before_header.count(b"content_type: abstract_only") == 1
    assert after_header == before_header.replace(
        b"content_type: abstract_only", b"content_type: abstract_and_full_text", 1
    ), "cache identity or another header changed"
    return digest(before_body)


def assert_cache_successor(root, path, predecessor_digest, *, provenance=None, current=None):
    provenance = load_provenance(root) if provenance is None else provenance
    current = (root / path).read_bytes() if current is None else current
    matches = [row for row in provenance["cache_corrections"] if row["path"] == path]
    if not matches:
        assert digest(current) == predecessor_digest
        return
    assert len(matches) == 1
    correction = matches[0]
    previous = original(root, path)
    assert digest(previous) == predecessor_digest == correction["original_sha256"]
    assert assert_header_only_cache_change(previous, current) == correction["article_body_sha256"]
    assert digest(current) == correction["current_sha256"]
    receipt = json.loads(read_artifact(root, correction["receipt"]))
    assert receipt["path"] == path and receipt["applied"] is True
    assert receipt["before_sha256"] == predecessor_digest
    assert receipt["after_sha256"] == correction["current_sha256"]
