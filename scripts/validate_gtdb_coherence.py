#!/usr/bin/env python3
"""Report `gtdb_classification` blocks whose evidence counts contradict each other.

The schema types and bounds the counts individually but cannot relate two slots
to each other — the JSON-Schema backend has no cross-field arithmetic — so
`linkml-validate` accepts a block claiming 99 supporting genomes out of 3, and
accepts `total_genomes: null` because a null satisfies `required` (#387).

The same checks run inside `just validate-strict`, which is the CI gate. This
script exists for the single-file case, where booting the full closed-schema
validator to ask one question is slow and its output buries the answer.

    just validate-gtdb kb/communities/Foo.yaml
    just validate-gtdb-all

Exits 1 if any issue is found, so it can be used as a gate on its own.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "src"))

from communitymech.validators.gtdb_coherence import validate_gtdb_coherence  # noqa: E402


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("files", nargs="+", type=Path, help="community YAML file(s)")
    args = parser.parse_args(argv)

    issues = []
    for path in args.files:
        if not path.exists():
            print(f"[gtdb-coherence] no such file: {path}", file=sys.stderr)
            return 2
        issues.extend(validate_gtdb_coherence(path))

    by_category: dict[str, int] = {}
    for issue in issues:
        by_category[issue.category] = by_category.get(issue.category, 0) + 1
        print(f"{issue.file}: {issue.taxon}\n  [{issue.category}] {issue.message}")

    print(f"\nfiles checked: {len(args.files)}", file=sys.stderr)
    print(f"incoherent blocks: {len(issues)}", file=sys.stderr)
    for category, count in sorted(by_category.items(), key=lambda kv: -kv[1]):
        print(f"  {category:34s} {count:>6d}", file=sys.stderr)
    return 1 if issues else 0


if __name__ == "__main__":
    raise SystemExit(main())
