"""Record the bounded dependency update for CommunityMech #622 (2026-11-14).

Inputs: branch pyproject.toml, uv.lock, installed local Python 3.13 environment.
Outputs: updated lock/environment and durable logs through the completion runner.
Run only in an idle checkout; never updates a running M5 validator environment.
"""

from __future__ import annotations

import argparse

from m5_completion_checks import PIN, ROOT, run_check


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=("lock", "install"))
    parser.add_argument("--name", required=True)
    parser.add_argument("--expected-revision", default=PIN)
    args = parser.parse_args()
    command = ["uv"]
    if args.mode == "lock":
        command.extend(["lock", "--upgrade-package", "linkml-reference-validator==0.2.1"])
    else:
        command.extend(["sync", "--frozen", "--extra", "dev"])
    command.extend(["--python", str(ROOT / ".venv/bin/python")])
    return run_check(
        args.name, [], native_command=command, expected_revision=args.expected_revision
    )


if __name__ == "__main__":
    raise SystemExit(main())
