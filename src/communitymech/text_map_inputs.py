"""Versioned semantic YAML text for the common fleet map; no model calls.

Includes canonical community records and separately stored isolate records in
the text map; the graph community projection keeps its own population policy.
Stable CommunityMech IDs link to existing community pages. Text includes names,
descriptions, ecological class/state, environments, named taxa/roles,
interactions and measured environmental factors. Citations, evidence snippets,
history, grounding annotations and identifiers are excluded.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
import tempfile
from collections.abc import Iterator
from contextlib import nullcontext
from pathlib import Path
from urllib.parse import quote

import yaml

REPO_ROOT = Path(__file__).resolve().parents[2]
ADAPTER_VERSION = "communitymech-semantic-v1"
RECORD_ROOTS = ("kb/communities", "data/isolates")


def clean(value: object) -> str:
    return " ".join(str(value).split()) if value is not None else ""


def enum_text(value: object) -> str:
    return clean(value).lower().replace("_", " ")


def label_of(value: object) -> str:
    if isinstance(value, str):
        return clean(value)
    if not isinstance(value, dict):
        return ""
    return clean(
        value.get("preferred_term")
        or value.get("label")
        or value.get("name")
        or (value.get("term") or {}).get("label")
    )


def add(lines: list[str], label: str, value: object) -> None:
    text = clean(value)
    if text:
        lines.append(f"{label}: {text}")


def _load(path: Path) -> dict:
    with path.open(encoding="utf-8") as stream:
        record = yaml.safe_load(stream)
    if not isinstance(record, dict):
        raise TypeError(f"record is not a YAML mapping: {path}")
    return record


def _discover(directory: Path) -> Iterator[Path]:
    with os.scandir(directory) as entries:
        for entry in entries:
            if entry.is_symlink():
                raise ValueError(f"symlink in corpus: {entry.path}")
            if entry.is_dir(follow_symlinks=False):
                yield from _discover(Path(entry.path))
            elif entry.name.endswith(".yaml") and entry.is_file(follow_symlinks=False):
                yield Path(entry.path)


def _record_path(root: Path, relative: str) -> Path:
    path = Path(relative)
    if path.is_absolute() or ".." in path.parts or path.suffix != ".yaml":
        raise ValueError(f"not a repository-relative corpus YAML path: {relative}")
    source = root / path
    if not any(source.is_relative_to(root / directory) for directory in RECORD_ROOTS):
        raise ValueError(f"record leaves the corpus: {relative}")
    if any(
        (root / Path(*path.parts[:length])).is_symlink() for length in range(1, len(path.parts) + 1)
    ):
        raise ValueError(f"symlink in corpus path: {relative}")
    if not source.is_file():
        raise ValueError(f"missing corpus record: {relative}")
    return source


def include_record(record: dict) -> bool:
    return True


def build_context(paths: list[Path]) -> dict:
    return {}


def record_details(record: dict, path: Path) -> tuple[str, str, str, str]:
    return (
        record.get("id"),
        clean(record.get("name")),
        clean(record.get("community_category")) or "UNKNOWN",
        ("isolates/" if path.parent.name == "isolates" else "communities/")
        + quote(path.stem, safe="-._")
        + ".html",
    )


def semantic_text(record: dict, context: dict | None = None) -> str:
    lines = []
    add(lines, "name", record.get("name"))
    add(lines, "description", record.get("description"))
    for field in ("community_category", "ecological_state", "community_origin"):
        add(lines, field.replace("_", " "), enum_text(record.get(field)))
    add(lines, "environment", label_of(record.get("environment_term")))
    for taxon in record.get("taxonomy") or []:
        add(lines, "taxon", label_of(taxon.get("taxon_term")))
        for field in ("functional_role", "abundance_level"):
            add(lines, field.replace("_", " "), enum_text(taxon.get(field)))
    for interaction in record.get("ecological_interactions") or []:
        add(lines, "interaction", interaction.get("name"))
        add(lines, "interaction type", enum_text(interaction.get("interaction_type")))
        add(lines, "interaction description", interaction.get("description"))
        for field in ("metabolites", "biological_processes"):
            for value in interaction.get(field) or []:
                add(lines, field.replace("_", " "), label_of(value))
    for factor in record.get("environmental_factors") or []:
        add(lines, "environmental factor", factor.get("name"))
        add(lines, "value", factor.get("value"))
        add(lines, "factor description", factor.get("description"))
    return "\n".join(lines) + "\n"


def iter_inputs(
    root: Path = REPO_ROOT, *, records: list[str] | None = None, limit: int | None = None
) -> Iterator[dict]:
    root = root.resolve()
    if limit is not None and limit < 1:
        raise ValueError("limit must be a positive integer")
    paths = []
    for directory in RECORD_ROOTS:
        corpus = root / directory
        if not corpus.is_dir() or any(
            (root / Path(*Path(directory).parts[:length])).is_symlink()
            for length in range(1, len(Path(directory).parts) + 1)
        ):
            raise ValueError(f"missing real corpus directory: {corpus}")
        paths.extend(_discover(corpus))
    context = build_context(paths)
    selected = [_record_path(root, relative) for relative in records] if records else paths
    if len(set(selected)) != len(selected):
        raise ValueError("duplicate selected record path")
    selected = sorted(selected)
    identifiers = set()
    count = 0
    for path in selected:
        record = _load(path)
        if not include_record(record):
            continue
        identifier, label, category, page = record_details(record, path)
        if not all(
            isinstance(value, str) and value.strip()
            for value in (identifier, label, category, page)
        ):
            raise ValueError(f"missing record identity, label, category or page: {path}")
        if identifier in identifiers:
            raise ValueError(f"duplicate record identifier: {identifier}")
        identifiers.add(identifier)
        text = semantic_text(record, context)
        yield {
            "identifier": identifier,
            "label": label,
            "category": category,
            "page": page,
            "source_path": path.relative_to(root).as_posix(),
            "text": text,
            "text_sha256": hashlib.sha256(text.encode("utf-8")).hexdigest(),
            "adapter_version": ADAPTER_VERSION,
        }
        count += 1
        if limit is not None and count >= limit:
            break


def export_inputs(
    root: Path, output: Path | None, *, records: list[str] | None = None, limit: int | None = None
) -> dict:
    destination = output.resolve() if output is not None else None
    if destination is not None and destination.suffix != ".jsonl":
        raise ValueError("output must have a .jsonl suffix")
    temporary = None
    digest = hashlib.sha256()
    count = 0
    try:
        if destination is not None:
            destination.parent.mkdir(parents=True, exist_ok=True)
        with (
            tempfile.NamedTemporaryFile(
                mode="wb", prefix=".text-map-", dir=destination.parent, delete=False
            )
            if destination is not None
            else nullcontext()
        ) as handle:
            if handle is not None:
                temporary = Path(handle.name)
            for record in iter_inputs(root, records=records, limit=limit):
                data = (json.dumps(record, sort_keys=True, ensure_ascii=False) + "\n").encode(
                    "utf-8"
                )
                digest.update(data)
                count += 1
                if handle is not None:
                    handle.write(data)
        if not count:
            raise ValueError("selection contains no eligible corpus records")
        if temporary is not None:
            temporary.replace(destination)
        return {
            "mode": "export" if destination else "preview",
            "scope": "subset" if records or limit is not None else "full",
            "records": count,
            "adapter_version": ADAPTER_VERSION,
            "jsonl_sha256": digest.hexdigest(),
            "output": str(destination) if destination else None,
        }
    finally:
        if temporary is not None:
            temporary.unlink(missing_ok=True)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=REPO_ROOT)
    parser.add_argument(
        "--output", type=Path, help="write JSONL atomically; otherwise validate a preview"
    )
    parser.add_argument(
        "--record", action="append", help="repeat a repo-relative path for an explicit canary"
    )
    parser.add_argument(
        "--limit", type=int, help="explicit canary limit; normal exports cover the full corpus"
    )
    args = parser.parse_args(argv)
    try:
        result = export_inputs(args.root, args.output, records=args.record, limit=args.limit)
    except (OSError, ValueError, TypeError, yaml.YAMLError) as error:
        print(f"text-map inputs refused: {error}", file=sys.stderr)
        return 2
    print(json.dumps(result, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
