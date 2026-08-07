#!/usr/bin/env python3
"""
Batch evidence snippet fixer for processing multiple community files.

Processes multiple YAML files in sequence, applying intelligent snippet
fixes based on direct abstract fetching.

Usage:
    # Process Phase 1 top 10 files
    python scripts/batch_snippet_fixer.py --phase 1

    # Process specific files
    python scripts/batch_snippet_fixer.py --files Australian_Lead_Zinc_Polymetallic.yaml AMD_Acidophile_Heterotroph_Network.yaml

    # Process all files with issues (from report)
    python scripts/batch_snippet_fixer.py --from-report
"""

import argparse
import re
import subprocess
import sys
from pathlib import Path

# Add scripts to path for imports
sys.path.insert(0, str(Path(__file__).parent))

from intelligent_snippet_fixer import interactive_fix_workflow

# Priority file lists from the systematic evidence curation plan
PHASE_1_FILES = [
    "Australian_Lead_Zinc_Polymetallic.yaml",
    "AMD_Acidophile_Heterotroph_Network.yaml",
    "Chromium_Sulfur_Reduction_Enrichment.yaml",
    "Ewaste_Bioleaching_Consortium.yaml",
    "Copper_Biomining_Heap_Leach.yaml",
    "Aspergillus_Indium_LED_Recovery.yaml",
    "Chromobacterium_Gold_Biocyanidation.yaml",
    "Bayan_Obo_REE_Tailings_Consortium.yaml",
    "AMD_Nitrososphaerota_Archaeal.yaml",
    "Dangl_SynComm_35.yaml",
]

PHASE_2_FILES = [
    "Coscinodiscus_Synthetic_Community.yaml",
    "DVM_Triculture.yaml",
    "Ferroplasma_Leptospirillum_Syntrophy.yaml",
    "Desulfovibrio_Methanococcus_Syntrophy.yaml",
    # Add more Phase 2 files as needed
]


def parse_curation_report(report_path: Path) -> list[dict[str, int]]:
    """
    Parse the evidence curation report to get files sorted by issue count.

    Args:
        report_path: Path to evidence_curation_report.txt

    Returns:
        List of dicts with file name and issue count, sorted by count (descending)
    """
    if not report_path.exists():
        print(f"⚠️  Report not found: {report_path}")
        return []

    with open(report_path, encoding="utf-8") as f:
        content = f.read()

    # Parse file entries: "FILENAME.yaml (X issues)"
    pattern = r"([A-Za-z_]+\.yaml) \((\d+) issues\)"
    matches = re.findall(pattern, content)

    files_with_issues = [{"file": filename, "issues": int(count)} for filename, count in matches]

    # Sort by issue count (descending)
    files_with_issues.sort(key=lambda x: x["issues"], reverse=True)

    return files_with_issues


REPO_ROOT = Path(__file__).resolve().parent.parent


def _count(value: int) -> str:
    """Render an issue count, never letting the -1 sentinel read as a number."""
    return "could not validate" if value == -1 else str(value)


def validate_file(yaml_path: Path) -> dict[str, int]:
    """
    Run snippet validation on a file and return issue counts.

    Returns ``{"total": -1, ...}`` when validation could not be run. A caller
    must distinguish that from a clean file, which is exactly what this used to
    make impossible (#410).

    It shelled out to ``poetry run python scripts/curate_evidence_with_pdfs.py``.
    Three things were wrong at once, and together they were silent:

    * that script imports ``communitymech.literature_enhanced``, which has never
      existed in any commit, so it cannot start;
    * ``poetry`` is not this repo's runner — it uses ``uv``;
    * ``cwd`` was ``yaml_path.parent.parent``, i.e. ``kb/``, not the repo root.

    ``returncode`` was never checked. The subprocess failed, stdout and stderr
    carried no ``ERROR: N`` for the regex to match, and the function returned
    ``{"total": 0, "errors": 0, "warnings": 0}`` — reported to the caller as
    *validated, no issues*. A validation step that reports success because it
    never ran is worse than one that is simply missing.

    It now calls ``linkml-reference-validator``, which is what
    ``just validate-references`` runs and which does check snippets against
    ``references_cache/``. It exits 0 when clean and 1 when it finds issues, and
    prints ``Issues found: N`` only in the latter case — which is the line
    parsed below. (Its ``Total checks`` line also counts issues rather than
    checks, per #257 and #466, but nothing here reads it.)
    """
    try:
        result = subprocess.run(
            [
                "uv",
                "run",
                "linkml-reference-validator",
                "validate",
                "data",
                str(yaml_path.resolve()),
                "-s",
                "src/communitymech/schema/communitymech.yaml",
                "--config",
                "conf/reference_validator.yaml",
            ],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            timeout=600,
        )
    except Exception as exc:  # noqa: BLE001 — reported, not swallowed
        print(f"  ⚠️  Validation could not run: {exc}")
        return {"total": -1, "errors": -1, "warnings": -1}

    output = result.stdout + result.stderr
    if result.returncode not in (0, 1):
        # Anything else means the validator itself failed to run. Say so
        # instead of reporting a clean file.
        print(f"  ⚠️  Validator exited {result.returncode}: {output.strip()[-200:]}")
        return {"total": -1, "errors": -1, "warnings": -1}

    found = re.search(r"Issues found:\s*(\d+)", output)
    errors = int(found.group(1)) if found else 0
    if errors == 0 and result.returncode == 1:
        # Non-zero without a parseable count: do not round down to clean.
        print(f"  ⚠️  Validator reported failure with no issue count: {output.strip()[-200:]}")
        return {"total": -1, "errors": -1, "warnings": -1}

    # Everything under `total`. The old code split errors from warnings, but
    # linkml-reference-validator reports one issue count, so filing all of it
    # under `errors` and hardcoding `warnings: 0` stated something untrue —
    # a cache miss prints [WARN] and would still have landed in `errors`
    # (#487 review). The keys stay for callers; they now agree with the source.
    return {"total": errors, "errors": errors, "warnings": 0}


def process_files_batch(
    file_list: list[str],
    auto_approve: bool = False,
    only_invalid: bool = True,
    validate_after: bool = True,
    relaxed: bool = False,
):
    """
    Process a batch of files in sequence.

    Args:
        file_list: List of YAML filenames
        auto_approve: Auto-approve suggestions
        only_invalid: Only process invalid snippets
        validate_after: Run validation after processing each file
    """
    print(f"\n{'='*80}")
    print("BATCH SNIPPET FIXER")
    print(f"{'='*80}")
    print(f"Files to process: {len(file_list)}")
    print(f"Mode: {'Auto-approve' if auto_approve else 'Interactive'}")
    print(f"{'='*80}\n")

    results = []

    for i, filename in enumerate(file_list, 1):
        print(f"\n{'#'*80}")
        print(f"# PROCESSING FILE {i}/{len(file_list)}: {filename}")
        print(f"{'#'*80}\n")

        yaml_path = Path("kb/communities") / filename

        if not yaml_path.exists():
            print(f"❌ File not found: {yaml_path}")
            results.append({"file": filename, "status": "not_found", "applied": 0})
            continue

        # Get initial issue count
        print("📊 Pre-processing validation...")
        initial_issues = validate_file(yaml_path) if validate_after else {"total": 0}

        # Process with intelligent fixer
        try:
            interactive_fix_workflow(
                yaml_path,
                only_invalid=only_invalid,
                auto_approve=auto_approve,
                verbose=False,
                relaxed=relaxed,
            )

            # Validate after processing
            if validate_after:
                print("\n📊 Post-processing validation...")
                final_issues = validate_file(yaml_path)

                # -1 means the validator could not run. Subtracting it
                # reported `0 -> -1` as "fixed 1", with a green tick, and summed
                # that fabricated 1 into the batch total — the same
                # never-ran-but-looks-clean defect this function was fixed for,
                # one frame up (#487 review).
                unknown = -1 in (initial_issues["total"], final_issues["total"])
                fixed = None if unknown else initial_issues["total"] - final_issues["total"]

                print("\n📈 IMPROVEMENT:")
                print(f"   Issues before: {_count(initial_issues['total'])}")
                print(f"   Issues after:  {_count(final_issues['total'])}")
                print(f"   Issues fixed:  {'unknown' if unknown else fixed}")

                results.append(
                    {
                        "file": filename,
                        "status": "validation_failed" if unknown else "processed",
                        "issues_before": initial_issues["total"],
                        "issues_after": final_issues["total"],
                        "issues_fixed": fixed,
                    }
                )
            else:
                results.append({"file": filename, "status": "processed"})

        except Exception as e:
            print(f"❌ Error processing {filename}: {e}")
            results.append({"file": filename, "status": "error", "error": str(e)})

        # Pause between files (unless auto-approve)
        if not auto_approve and i < len(file_list):
            print(f"\n{'='*80}")
            input(f"Press Enter to continue to next file ({i+1}/{len(file_list)})...")

    # Print final summary
    print(f"\n{'='*80}")
    print("BATCH PROCESSING SUMMARY")
    print(f"{'='*80}")
    print(f"Total files processed: {len(file_list)}\n")

    for result in results:
        # `validation_failed` is its own icon: it is neither a clean pass nor a
        # processing error, and a ✅ beside a file whose validation never ran is
        # the whole defect (#487 review).
        status_icon = {"processed": "✅", "validation_failed": "⚠️"}.get(result["status"], "❌")
        print(f"{status_icon} {result['file']}")
        if result["status"] == "validation_failed":
            print(
                f"   Issues: {_count(result['issues_before'])} → "
                f"{_count(result['issues_after'])} (fixed: unknown — the "
                f"validator could not run, so this file is unverified)"
            )
        elif result["status"] == "processed" and result.get("issues_fixed") is not None:
            print(
                f"   Issues: {result['issues_before']} → {result['issues_after']} "
                f"(fixed {result['issues_fixed']})"
            )
        elif result["status"] == "error":
            print(f"   Error: {result.get('error', 'Unknown')}")
        print()

    if validate_after and any(r["status"] == "processed" for r in results):
        total_fixed = sum(
            r["issues_fixed"]
            for r in results
            if r["status"] == "processed" and r.get("issues_fixed") is not None
        )
        print(f"🎉 Total issues fixed across all files: {total_fixed}")
        unverified = [r["file"] for r in results if r["status"] == "validation_failed"]
        if unverified:
            # Said out loud, not left to be inferred from a smaller total.
            print(
                f"⚠️  {len(unverified)} file(s) could not be validated and are "
                f"NOT counted above: {', '.join(unverified)}"
            )


def main():
    parser = argparse.ArgumentParser(
        description="Batch evidence snippet fixer for multiple community files"
    )

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "--phase",
        type=int,
        choices=[1, 2, 3],
        help="Process files from a specific phase (1=top 10, 2=medium priority, 3=all)",
    )
    group.add_argument("--files", nargs="+", help="Specific YAML files to process")
    group.add_argument(
        "--from-report",
        action="store_true",
        help="Process all files from curation report, sorted by issue count",
    )
    group.add_argument(
        "--all", action="store_true", help="Process all YAML files in kb/communities/"
    )

    parser.add_argument(
        "--auto-approve",
        action="store_true",
        help="Automatically apply top suggestion without prompting",
    )
    parser.add_argument(
        "--only-short",
        action="store_true",
        default=False,
        help="Only process evidence items with short snippets (<50 chars). Default: process all.",
    )
    # `--no-validate` existed with no `--validate` beside it, and
    # `set_defaults(validate=False)` then pinned it False whatever was passed —
    # so `validate_file` was unreachable from the CLI, and had been since the
    # commit that introduced both (7c658e6). The flag advertised a choice the
    # parser did not offer (#487 review).
    validation = parser.add_mutually_exclusive_group()
    validation.add_argument(
        "--validate",
        action="store_true",
        dest="validate",
        help=(
            "Validate snippets before and after each file. Off by default: it "
            "runs linkml-reference-validator twice per file (~1.3s each), so a "
            "full 312-file sweep adds roughly 13 minutes."
        ),
    )
    validation.add_argument(
        "--no-validate",
        action="store_false",
        dest="validate",
        help="Skip validation before and after processing each file (the default)",
    )
    parser.set_defaults(validate=False)
    parser.add_argument(
        "--relaxed",
        action="store_true",
        help="Apply low-confidence suggestions too (use after fixing wrong references)",
    )
    parser.add_argument("--limit", type=int, help="Limit number of files to process")

    args = parser.parse_args()

    # Determine file list
    if args.phase:
        if args.phase == 1:
            file_list = PHASE_1_FILES
            print("📋 Phase 1: Top 10 priority files")
        elif args.phase == 2:
            file_list = PHASE_2_FILES
            print("📋 Phase 2: Medium priority files")
        else:
            # Phase 3: All remaining files
            print("📋 Phase 3: All remaining files")
            report_path = Path("evidence_curation_report.txt")
            files_from_report = parse_curation_report(report_path)
            processed_files = set(PHASE_1_FILES + PHASE_2_FILES)
            file_list = [f["file"] for f in files_from_report if f["file"] not in processed_files]

    elif args.from_report:
        report_path = Path("evidence_curation_report.txt")
        files_from_report = parse_curation_report(report_path)
        file_list = [f["file"] for f in files_from_report]
        print("📋 Processing files from curation report (sorted by issue count)")

    elif getattr(args, "all", False):
        communities_dir = Path("kb/communities")
        file_list = sorted(
            p.name
            for p in communities_dir.glob("*.yaml")
            if not any(x in p.name for x in [".bak", ".backup"])
        )
        print(f"📋 Processing all {len(file_list)} YAML files in kb/communities/")

    else:
        file_list = args.files
        print("📋 Processing specified files")

    # Apply limit if specified
    if args.limit:
        file_list = file_list[: args.limit]
        print(f"   Limited to first {args.limit} files")

    if not file_list:
        print("❌ No files to process")
        return 1

    print(f"   Total files: {len(file_list)}\n")

    # Process batch
    process_files_batch(
        file_list,
        auto_approve=args.auto_approve,
        only_invalid=args.only_short,
        validate_after=args.validate,
        relaxed=args.relaxed,
    )

    return 0


if __name__ == "__main__":
    exit(main())
