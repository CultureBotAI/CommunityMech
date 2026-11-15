"""Run serial final M5 QC and focused gates on frozen code (2026-11-14).

Inputs: explicit final revision, frozen installed environment, three reviewed records.
Outputs: native logs/exits, input hashes, strict artifacts and stage checkpoints.
An aggregate failure remains a failure; subsequent gates are independent diagnostics.
Use the same new --attempt ID for plan, canary and completion on a later revision.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.metadata
import json
import re

from m5_completion_checks import ROOT, STATE, git, now, run_check, write_json

RECORDS = {
    "000025": "EcoFAB_Ring_Trial_SynCom17",
    "000515": "Yolo_Silt_Loam_Soil_Dopamine_Amendment_Microcosm",
    "000516": "Brachypodium_Natural_Variation_Dopamine_SynCom16",
}
CANARY_TEST = "tests/test_no_new_bracketed_snippets.py::test_unchanged_asgard_nife_quote_matches_its_committed_article"
CACHE_TESTS = (
    "tests/test_reference_cache_names_are_case_exact.py",
    "tests/test_no_case_conflicting_cache_pairs.py",
    "tests/test_cache_is_source_text_not_notes.py",
    "tests/test_cache_supplements.py",
)


def stage_outputs(prefix, stage):
    """Enumerate all names a stage could write before starting any part of it."""
    if stage == "plan":
        runs = [f"{prefix}-plan-qc-references"]
        controls = []
    elif stage == "canary":
        runs = [f"{prefix}-environment-canary"]
        controls = []
    else:
        runs = [
            f"{prefix}-{suffix}"
            for suffix in (
                "qc-references",
                "check-docs-current",
                "validate-products",
                "cache-tests-diagnostic",
                "reference-diagnostic",
            )
        ]
        controls = [STATE / f"{prefix}-checks-progress.json"]
        for identifier in RECORDS:
            runs.extend(
                f"{prefix}-{identifier}-{gate}"
                for gate in ("schema", "strict", "terms", "references", "gtdb", "domain", "history")
            )
            controls.extend(
                STATE / f"{prefix}-{identifier}-{suffix}"
                for suffix in ("inputs.json", "strict.tsv", "strict-artifact.json")
            )
    paths = [STATE / f"{name}.{suffix}" for name in runs for suffix in ("json", "log", "exit")]
    paths.extend(controls)
    return paths + [
        path.with_suffix(path.suffix + ".writing") for path in paths if path.suffix == ".json"
    ]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("stage", choices=("plan", "canary", "completion"))
    parser.add_argument("--expected-revision", required=True)
    parser.add_argument("--attempt", help="new attempt ID; omitted preserves first-run names")
    args = parser.parse_args()
    if args.attempt is not None and not re.fullmatch(r"[a-z0-9][a-z0-9_-]{0,31}", args.attempt):
        parser.error("--attempt requires 1–32 lowercase letters, digits, underscores or hyphens")
    prefix = "final" + ("-" + args.attempt if args.attempt else "")
    if any(path.exists() or path.is_symlink() for path in stage_outputs(prefix, args.stage)):
        raise ValueError("retained stage outputs already exist; use a new --attempt")
    if git("rev-parse", "HEAD") != args.expected_revision:
        raise ValueError("unexpected final revision")
    if importlib.metadata.version("linkml-reference-validator") != "0.2.1":
        raise ValueError("the frozen final reference validator is not installed")
    if git("diff", "--name-only", "HEAD", "--"):
        raise ValueError("tracked final checkout files have changed")
    extra_files = git("ls-files", "--others", "--exclude-standard").splitlines()
    extra_hashes = {
        path: hashlib.sha256((ROOT / path).read_bytes()).hexdigest()
        for path in extra_files
        if path.startswith("scripts/") and (ROOT / path).is_file()
    }
    startup = {
        "head": args.expected_revision,
        "tracked_files_clean": True,
        "untracked_orchestration_files": extra_hashes,
        "reference_validator_version": importlib.metadata.version("linkml-reference-validator"),
    }
    startup_path = STATE / f"{prefix}-orchestration-inputs.json"
    if startup_path.is_symlink():
        raise ValueError("retained startup receipt must be a regular file")
    if startup_path.exists():
        if json.loads(startup_path.read_text()) != startup:
            raise ValueError("orchestration files changed since the final canary")
    else:
        write_json(startup_path, startup)
    if args.stage == "plan":
        return run_check(
            f"{prefix}-plan-qc-references",
            ["qc-references"],
            dry_run=True,
            expected_revision=args.expected_revision,
        )
    if args.stage == "canary":
        return run_check(
            f"{prefix}-environment-canary",
            [],
            native_command=["uv", "run", "pytest", CANARY_TEST, "-q"],
            expected_revision=args.expected_revision,
        )
    canary = json.loads((STATE / f"{prefix}-environment-canary.json").read_text())
    if canary.get("exit_code") != 0 or canary["head"] != args.expected_revision:
        raise ValueError("a passed final-revision canary is required")
    canary_log = (ROOT / canary["log"]).read_bytes()
    if not canary_log or hashlib.sha256(canary_log).hexdigest() != canary["log_sha256"]:
        raise ValueError("the canary artifact is missing or changed")
    completed = []

    def check(name, recipe, **kwargs):
        code = run_check(name, recipe, expected_revision=args.expected_revision, **kwargs)
        completed.append({"name": name, "exit_code": code})
        write_json(
            STATE / f"{prefix}-checks-progress.json",
            {"head": args.expected_revision, "updated_at": now(), "checks": completed},
        )
        return code

    check(f"{prefix}-qc-references", ["qc-references"])
    aggregate = json.loads((STATE / f"{prefix}-qc-references.json").read_text())
    stages = {row["recipe"]: row["status"] for row in aggregate["stages"]}
    for identifier, stem in RECORDS.items():
        path = f"kb/communities/{stem}.yaml"
        write_json(
            STATE / f"{prefix}-{identifier}-inputs.json",
            {
                "head": args.expected_revision,
                "path": path,
                "sha256": hashlib.sha256((ROOT / path).read_bytes()).hexdigest(),
                "git_blob": git("hash-object", path),
            },
        )
        strict = str((STATE / f"{prefix}-{identifier}-strict.tsv").relative_to(ROOT))
        recipes = (
            ("schema", ["validate", path]),
            ("strict", ["validate-strict", path, "--out", strict]),
            ("terms", ["validate-terms", path]),
            ("references", ["validate-references-explained", path]),
            ("gtdb", ["validate-gtdb", path]),
            ("domain", ["validate-gtdb-domain", path]),
            ("history", ["validate-history", f"history/records/{stem}"]),
        )
        for label, recipe in recipes:
            check(f"{prefix}-{identifier}-{label}", recipe)
        strict_path = ROOT / strict
        if strict_path.exists():
            write_json(
                STATE / f"{prefix}-{identifier}-strict-artifact.json",
                {
                    "path": strict,
                    "sha256": hashlib.sha256(strict_path.read_bytes()).hexdigest(),
                    "bytes": strict_path.stat().st_size,
                },
            )
    check(f"{prefix}-check-docs-current", ["check-docs-current"])
    check(f"{prefix}-validate-products", ["validate-products"])
    if stages.get("test") != "PASSED":
        check(
            f"{prefix}-cache-tests-diagnostic",
            [],
            native_command=["uv", "run", "pytest", *CACHE_TESTS, "-q"],
        )
    if stages.get("validate-references-all") == "NOT RUN":
        check(f"{prefix}-reference-diagnostic", ["validate-references-all"], no_deps=True)
    return int(any(row["exit_code"] for row in completed))


if __name__ == "__main__":
    raise SystemExit(main())
