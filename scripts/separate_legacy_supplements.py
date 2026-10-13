#!/usr/bin/env python3
"""Apply a reviewed, hash-bound article/supplement separation manifest (#1994)."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

MARKER = b"===== SUPPLEMENTARY FILE TEXT"
REPO = Path(__file__).resolve().parents[1]


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def split_article(data: bytes) -> tuple[bytes, bytes]:
    if data.count(MARKER) != 1:
        raise ValueError("expected exactly one supplementary boundary")
    offset = data.index(MARKER)
    if not data[:offset].strip() or data[offset - 1 : offset] != b"\n":
        raise ValueError("supplement boundary must follow a nonempty article on a new line")
    head = data[:offset]
    if not head.endswith(b"\n\n"):
        raise ValueError("expected the reviewed blank-line append separator")
    return head[:-1], data[offset:]


def cache_path(root: Path, name: str) -> Path:
    path = root / name
    if Path(name).parts[:1] != ("references_cache",) or len(Path(name).parts) != 2:
        raise ValueError(f"not a flat reference-cache path: {name}")
    if path.is_symlink() or path.parent.resolve() != (root / "references_cache").resolve():
        raise ValueError(f"unsafe cache path: {name}")
    return path


def prepare(root: Path, entries: list[dict]) -> list[tuple[Path, bytes, Path, bytes | None]]:
    """Validate the whole batch before any write; never replace an existing sidecar."""
    plan = []
    used: set[str] = set()
    for entry in entries:
        article = cache_path(root, entry["article"])
        sidecar = cache_path(root, entry["supplement"])
        if article == sidecar or not sidecar.name.endswith(".supplement.md"):
            raise ValueError("article and separate supplement paths are required")
        if {str(article), str(sidecar)} & used:
            raise ValueError("duplicate cache path in separation manifest")
        used.update((str(article), str(sidecar)))
        raw = article.read_bytes()
        if digest(raw) != entry["article_before_sha256"]:
            raise ValueError(f"article input changed: {article.name}")
        head, tail = split_article(raw)
        if digest(head) != entry["article_after_sha256"]:
            raise ValueError(f"article boundary changed: {article.name}")
        if digest(tail) != entry["appended_sha256"]:
            raise ValueError(f"supplement input changed: {article.name}")
        expected = entry["supplement_before_sha256"]
        addition = None
        if expected is None:
            if sidecar.exists():
                raise ValueError(f"unreviewed supplement already exists: {sidecar.name}")
            addition = tail
        else:
            saved = sidecar.read_bytes()
            if digest(saved) != expected:
                raise ValueError(f"existing supplement changed: {sidecar.name}")
            # A reviewed offset excludes only retrieval furniture, never source text.
            payload = tail[entry["preserved_payload_offset"] :]
            if not payload.strip() or payload not in saved:
                raise ValueError(f"supplement does not preserve the appended text: {sidecar.name}")
        plan.append((article, head, sidecar, addition))
    return plan


def apply_plan(plan: list[tuple[Path, bytes, Path, bytes | None]]) -> None:
    for _, _, sidecar, addition in plan:
        if addition is not None:
            with sidecar.open("xb") as handle:
                handle.write(addition)
    for article, head, _, _ in plan:
        article.write_bytes(head)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("manifest", type=Path)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    entries = json.loads(args.manifest.read_text(encoding="utf-8"))["entries"]
    plan = prepare(REPO, entries)
    for article, head, sidecar, addition in plan:
        action = "extract" if addition is not None else "retain existing"
        print(f"{article.name}: retain {len(head)} article bytes; {action} {sidecar.name}")
    if args.apply:
        apply_plan(plan)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
