"""Verify a private Phase2 checkpoint on M5 using only stdlib, 2026-11-15.

Inputs: explicit snapshot directory and expected manifest SHA. Output: stdout
JSON of actual persisted file/hash/byte checks. No writes, source discovery or
network. The calling transfer helper retains this script and its exact hash.
"""

import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath


def verify(directory, expected_manifest_sha256):
    directory = directory.resolve()
    raw = (directory / "manifest.json").read_bytes()
    actual_manifest_sha256 = hashlib.sha256(raw).hexdigest()
    if actual_manifest_sha256 != expected_manifest_sha256:
        raise ValueError("manifest hash differs from accepted local snapshot")
    manifest = json.loads(raw)
    if manifest["status"] != "complete":
        raise ValueError("snapshot was not completed")
    expected = {"manifest.json"}
    total = 0
    for row in manifest["files"]:
        name = row["path"]
        relative = PurePosixPath(name)
        if relative.is_absolute() or any(part in {"", ".", ".."} for part in name.split("/")):
            raise ValueError("unsafe artifact path")
        if name in expected:
            raise ValueError("duplicate artifact")
        expected.add(name)
        path = directory / name
        if path.is_symlink() or not path.resolve().is_relative_to(directory):
            raise ValueError("artifact escapes snapshot")
        content = path.read_bytes()
        if hashlib.sha256(content).hexdigest() != row["sha256"] or len(content) != row["bytes"]:
            raise ValueError("artifact hash/bytes differ: " + name)
        total += len(content)
    discovered = list(directory.rglob("*"))
    if any(path.is_symlink() for path in discovered):
        raise ValueError("snapshot contains a symlink")
    actual = {str(path.relative_to(directory)) for path in discovered if path.is_file()}
    if actual != expected:
        raise ValueError("snapshot membership differs")
    if len(manifest["files"]) != manifest["file_count"] or total != manifest["total_bytes"]:
        raise ValueError("snapshot counts differ")
    return {
        "manifest_sha256": actual_manifest_sha256,
        "files_verified": len(manifest["files"]),
        "bytes_verified": total,
        "review_ids": manifest["review_ids"],
        "status": "verified",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("snapshot", type=Path)
    parser.add_argument("--expected-manifest-sha256", required=True)
    args = parser.parse_args()
    print(json.dumps(verify(args.snapshot, args.expected_manifest_sha256)))


if __name__ == "__main__":
    main()
