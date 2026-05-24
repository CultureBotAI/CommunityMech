#!/usr/bin/env python3
"""Non-destructive cleanup of metals_present / rare_earth_elements_present blocks.

Runs `extract_metals_from_community` against every community YAML and, when
the extracted lists differ from what's written on disk, rewrites only the
relevant blocks via line-based regex substitution. Comments, blank lines,
key order, and unrelated whitespace are preserved (unlike pyyaml's
dump-and-rewrite path used by `backfill_metals.py`).

Usage:
    PYTHONPATH=src uv run python scripts/clean_metals_inplace.py --dry-run
    PYTHONPATH=src uv run python scripts/clean_metals_inplace.py
"""

import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from communitymech.metal_extraction import extract_metals_from_community


def _read_block(text: str, key: str) -> tuple[int, int, list[str]]:
    """Locate `{key}:` block and return (start_line, end_line, current_values).

    Returns (-1, -1, []) if the key is not present.
    """
    lines = text.splitlines(keepends=True)
    start = None
    for i, line in enumerate(lines):
        if line.rstrip("\n") == f"{key}:" or line.startswith(f"{key}: "):
            start = i
            break
    if start is None:
        return -1, -1, []
    inline = lines[start].rstrip("\n").removeprefix(f"{key}:").strip()
    if inline and inline != "":
        return start, start + 1, [v.strip() for v in inline.strip("[]").split(",") if v.strip()]
    end = start + 1
    values: list[str] = []
    while end < len(lines):
        if lines[end].startswith("- "):
            values.append(lines[end][2:].strip())
            end += 1
        elif lines[end].strip() == "":
            end += 1
        else:
            break
    return start, end, values


def _format_list_block(key: str, values: list[str]) -> str:
    if not values:
        return f"{key}: []\n"
    body = "\n".join(f"- {v}" for v in values)
    return f"{key}:\n{body}\n"


def _replace_block(text: str, key: str, values: list[str]) -> str:
    start, end, _ = _read_block(text, key)
    if start == -1:
        return text
    lines = text.splitlines(keepends=True)
    new_block = _format_list_block(key, values)
    return "".join(lines[:start]) + new_block + "".join(lines[end:])


def _replace_scalar(text: str, key: str, value: str) -> str:
    pattern = re.compile(rf"^{re.escape(key)}:.*$", re.MULTILINE)
    if pattern.search(text):
        return pattern.sub(f"{key}: {value}", text, count=1)
    return text + f"{key}: {value}\n"


def clean_file(path: Path, dry_run: bool) -> tuple[bool, str]:
    metals, ree, relevance, notes = extract_metals_from_community(path)
    text = path.read_text()

    _, _, current_metals = _read_block(text, "metals_present")
    _, _, current_ree = _read_block(text, "rare_earth_elements_present")

    diff_metals = sorted(current_metals) != sorted(metals)
    diff_ree = sorted(current_ree) != sorted(ree)
    if not (diff_metals or diff_ree):
        return False, ""

    new_text = text
    new_text = _replace_block(new_text, "metals_present", sorted(metals))
    new_text = _replace_block(new_text, "rare_earth_elements_present", sorted(ree))
    new_text = _replace_scalar(new_text, "metal_relevance", relevance)
    if notes:
        new_text = _replace_scalar(new_text, "metal_notes", notes)

    summary = (
        f"  metals: {sorted(current_metals)} -> {sorted(metals)}\n"
        f"  ree:    {sorted(current_ree)} -> {sorted(ree)}"
    )
    if not dry_run:
        path.write_text(new_text)
    return True, summary


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    community_dir = Path("kb/communities")
    files = sorted(community_dir.glob("*.yaml"))
    changed = 0
    for f in files:
        did_change, summary = clean_file(f, dry_run=args.dry_run)
        if did_change:
            changed += 1
            print(f"{f.name}")
            print(summary)
    verb = "would change" if args.dry_run else "changed"
    print(f"\n{verb} {changed}/{len(files)} files")


if __name__ == "__main__":
    main()
