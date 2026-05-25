#!/usr/bin/env python3
"""Audit YAML-writing scripts in CommunityMech.

For every Python module under ``scripts/`` and the central
``src/communitymech/`` package that writes a YAML (looks for
``yaml.dump``, ``yaml.safe_dump``, ``write_validated_community``, or a
``path.write_text(yaml.safe_dump(...))`` flow), record:

- ``appends_curation_history``: does the script append a CurationEvent
  to ``community['curation_history']``?
- ``has_write_safeguard``: a ``--dry-run`` opt-out OR ``--apply``/``--write``
  opt-in flag.
- ``validates_before_write``: does it route through
  ``write_validated_community`` or call ``validate_community`` /
  ``linkml-validate`` first?
- ``wired_into_just``: is the script invoked from a justfile recipe?

TSV columns: path, writes_yaml, appends_curation_history,
has_write_safeguard, validates_before_write, wired_into_just.

Output: TSV to stdout (and via ``--out`` to a file).

Ported from CultureMech / MediaIngredientMech / TraitMech.
"""

from __future__ import annotations

import argparse
import csv
import re
import sys
from pathlib import Path

SEARCH_DIRS = [
    Path("scripts"),
    Path("src/communitymech"),
]

# Patterns
_WRITE_TEXT_OF_YAML = re.compile(r"\.write_text\s*\(\s*yaml\.(?:safe_)?dump")
_CURATION_APPEND = re.compile(
    r"curation_history.*?(append|\+=|\.insert)"
    r"|['\"]curator['\"]\s*:"
    r"|append_curation_event"
    r"|record_curation_event"
)
_WRITE_SAFEGUARD = re.compile(
    r"--dry[-_]run|dry_run\s*[:=]"
    r"|--apply\b|args\.apply\b"
    r"|--write\b|args\.write\b"
)
_VALIDATE_BEFORE_WRITE = re.compile(
    r"linkml[._-]?validate"
    r"|validate_community\("
    r"|validator\.validate\("
    r"|write_validated_community\("
)


def script_paths() -> list[Path]:
    out: list[Path] = []
    for d in SEARCH_DIRS:
        if not d.exists():
            continue
        out.extend(sorted(p for p in d.rglob("*.py") if "__pycache__" not in str(p)))
    return out


def looks_like_yaml_writer(text: str) -> bool:
    if "yaml.safe_dump(" in text or "yaml.dump(" in text:
        return True
    if _WRITE_TEXT_OF_YAML.search(text):
        return True
    # write_validated_community is the closed-schema-gated wrapper that
    # callers route through instead of yaml.dump directly.
    return "write_validated_community(" in text


def audit(path: Path, justfile_text: str) -> dict | None:
    # Suppress self-match: this module's regex source contains
    # `yaml.safe_dump` etc., so it would otherwise appear in its own output.
    if path.resolve() == Path(__file__).resolve():
        return None
    try:
        text = path.read_text()
    except (UnicodeDecodeError, OSError):
        return None
    if not looks_like_yaml_writer(text):
        return None
    return {
        "path": str(path),
        "writes_yaml": "yes",
        "appends_curation_history": "yes" if _CURATION_APPEND.search(text) else "no",
        "has_write_safeguard": "yes" if _WRITE_SAFEGUARD.search(text) else "no",
        "validates_before_write": "yes" if _VALIDATE_BEFORE_WRITE.search(text) else "no",
        "wired_into_just": "yes" if _is_wired_into_just(path, justfile_text) else "no",
    }


def _is_wired_into_just(path: Path, justfile_text: str) -> bool:
    """Detect whether a justfile recipe actually invokes this script.

    The earlier substring check (``path.stem in justfile_text``) had false
    positives — e.g. ``write_validated.py`` matched a justfile comment
    referencing ``write_validated_community``. Require the filename to
    appear as an explicit ``python ... <name>.py`` invocation, which is
    how every justfile recipe actually runs a script.
    """
    needle = re.compile(rf"\b{re.escape(path.name)}\b")
    for line in justfile_text.splitlines():
        stripped = line.strip()
        # Ignore comment-only lines so a mention in docs doesn't count.
        if stripped.startswith("#"):
            continue
        if needle.search(stripped):
            return True
    return False


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--out", type=Path, default=None, help="TSV output path (default stdout)")
    args = ap.parse_args()

    justfile_path = Path("justfile")
    justfile_text = justfile_path.read_text() if justfile_path.exists() else ""

    rows: list[dict] = []
    for p in script_paths():
        row = audit(p, justfile_text)
        if row is not None:
            rows.append(row)

    fields = [
        "path",
        "writes_yaml",
        "appends_curation_history",
        "has_write_safeguard",
        "validates_before_write",
        "wired_into_just",
    ]

    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        with args.out.open("w", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=fields, delimiter="\t", lineterminator="\n")
            w.writeheader()
            for row in rows:
                w.writerow(row)
        print(f"Wrote {len(rows)} rows to {args.out}", file=sys.stderr)
    else:
        w = csv.DictWriter(sys.stdout, fieldnames=fields, delimiter="\t")
        w.writeheader()
        for row in rows:
            w.writerow(row)

    def count(field: str, val: str) -> int:
        return sum(1 for r in rows if r[field] == val)

    print("", file=sys.stderr)
    print(f"=== writers audit summary ({len(rows)} writers) ===", file=sys.stderr)
    print(f"  appends curation_history:   {count('appends_curation_history', 'yes')} / {len(rows)}",
          file=sys.stderr)
    print(f"  has write safeguard:        {count('has_write_safeguard', 'yes')} / {len(rows)}",
          file=sys.stderr)
    print(f"  validates before write:     {count('validates_before_write', 'yes')} / {len(rows)}",
          file=sys.stderr)
    print(f"  wired into justfile:        {count('wired_into_just', 'yes')} / {len(rows)}",
          file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
