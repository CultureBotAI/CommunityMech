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
import sys
from pathlib import Path
from typing import List, Dict
import re
import subprocess

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


def parse_curation_report(report_path: Path) -> List[Dict[str, int]]:
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

    with open(report_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Parse file entries: "FILENAME.yaml (X issues)"
    pattern = r'([A-Za-z_]+\.yaml) \((\d+) issues\)'
    matches = re.findall(pattern, content)

    files_with_issues = [
        {"file": filename, "issues": int(count)}
        for filename, count in matches
    ]

    # Sort by issue count (descending)
    files_with_issues.sort(key=lambda x: x["issues"], reverse=True)

    return files_with_issues


def validate_file(yaml_path: Path) -> Dict[str, int]:
    """
    Run validation on a file and return issue counts.

    Args:
        yaml_path: Path to YAML file

    Returns:
        Dict with issue type counts
    """
    try:
        result = subprocess.run(
            ["poetry", "run", "python", "scripts/curate_evidence_with_pdfs.py",
             "--file", yaml_path.name, "--quick"],
            cwd=yaml_path.parent.parent,
            capture_output=True,
            text=True,
            timeout=300
        )

        # Parse output for issue counts
        output = result.stdout + result.stderr
        issues = {
            "total": 0,
            "errors": 0,
            "warnings": 0
        }

        # Look for issue counts in output
        error_match = re.search(r'ERROR:\s*(\d+)', output)
        warning_match = re.search(r'WARNING:\s*(\d+)', output)

        if error_match:
            issues["errors"] = int(error_match.group(1))
        if warning_match:
            issues["warnings"] = int(warning_match.group(1))

        issues["total"] = issues["errors"] + issues["warnings"]

        return issues

    except Exception as e:
        print(f"  ⚠️  Validation failed: {e}")
        return {"total": -1, "errors": -1, "warnings": -1}


def process_files_batch(
    file_list: List[str],
    auto_approve: bool = False,
    only_invalid: bool = True,
    validate_after: bool = True,
    relaxed: bool = False
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
    print(f"BATCH SNIPPET FIXER")
    print(f"{'='*80}")
    print(f"Files to process: {len(file_list)}")
    print(f"Mode: {'Auto-approve' if auto_approve else 'Interactive'}")
    print(f"{'='*80}\n")

    results = []

    for i, filename in enumerate(file_list, 1):
        print(f"\n{'#'*80}")
        print(f"# PROCESSING FILE {i}/{len(file_list)}: {filename}")
        print(f"{'#'*80}\n")

        yaml_path = Path('kb/communities') / filename

        if not yaml_path.exists():
            print(f"❌ File not found: {yaml_path}")
            results.append({
                "file": filename,
                "status": "not_found",
                "applied": 0
            })
            continue

        # Get initial issue count
        print(f"📊 Pre-processing validation...")
        initial_issues = validate_file(yaml_path) if validate_after else {"total": 0}

        # Process with intelligent fixer
        try:
            interactive_fix_workflow(
                yaml_path,
                only_invalid=only_invalid,
                auto_approve=auto_approve,
                verbose=False,
                relaxed=relaxed
            )

            # Validate after processing
            if validate_after:
                print(f"\n📊 Post-processing validation...")
                final_issues = validate_file(yaml_path)

                print(f"\n📈 IMPROVEMENT:")
                print(f"   Issues before: {initial_issues['total']}")
                print(f"   Issues after:  {final_issues['total']}")
                print(f"   Issues fixed:  {initial_issues['total'] - final_issues['total']}")

                results.append({
                    "file": filename,
                    "status": "processed",
                    "issues_before": initial_issues['total'],
                    "issues_after": final_issues['total'],
                    "issues_fixed": initial_issues['total'] - final_issues['total']
                })
            else:
                results.append({
                    "file": filename,
                    "status": "processed"
                })

        except Exception as e:
            print(f"❌ Error processing {filename}: {e}")
            results.append({
                "file": filename,
                "status": "error",
                "error": str(e)
            })

        # Pause between files (unless auto-approve)
        if not auto_approve and i < len(file_list):
            print(f"\n{'='*80}")
            input(f"Press Enter to continue to next file ({i+1}/{len(file_list)})...")

    # Print final summary
    print(f"\n{'='*80}")
    print(f"BATCH PROCESSING SUMMARY")
    print(f"{'='*80}")
    print(f"Total files processed: {len(file_list)}\n")

    for result in results:
        status_icon = "✅" if result["status"] == "processed" else "❌"
        print(f"{status_icon} {result['file']}")
        if result["status"] == "processed" and "issues_fixed" in result:
            print(f"   Issues: {result['issues_before']} → {result['issues_after']} "
                  f"(fixed {result['issues_fixed']})")
        elif result["status"] == "error":
            print(f"   Error: {result.get('error', 'Unknown')}")
        print()

    if validate_after and any(r["status"] == "processed" for r in results):
        total_fixed = sum(r.get("issues_fixed", 0) for r in results if r["status"] == "processed")
        print(f"🎉 Total issues fixed across all files: {total_fixed}")


def main():
    parser = argparse.ArgumentParser(
        description='Batch evidence snippet fixer for multiple community files'
    )

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        '--phase',
        type=int,
        choices=[1, 2, 3],
        help='Process files from a specific phase (1=top 10, 2=medium priority, 3=all)'
    )
    group.add_argument(
        '--files',
        nargs='+',
        help='Specific YAML files to process'
    )
    group.add_argument(
        '--from-report',
        action='store_true',
        help='Process all files from curation report, sorted by issue count'
    )
    group.add_argument(
        '--all',
        action='store_true',
        help='Process all YAML files in kb/communities/'
    )

    parser.add_argument(
        '--auto-approve',
        action='store_true',
        help='Automatically apply top suggestion without prompting'
    )
    parser.add_argument(
        '--only-short',
        action='store_true',
        default=False,
        help='Only process evidence items with short snippets (<50 chars). Default: process all.'
    )
    parser.add_argument(
        '--no-validate',
        action='store_false',
        dest='validate',
        help='Skip validation before and after processing each file (much faster)'
    )
    parser.set_defaults(validate=False)  # Off by default; too slow for batch runs
    parser.add_argument(
        '--relaxed',
        action='store_true',
        help='Apply low-confidence suggestions too (use after fixing wrong references)'
    )
    parser.add_argument(
        '--limit',
        type=int,
        help='Limit number of files to process'
    )

    args = parser.parse_args()

    # Determine file list
    if args.phase:
        if args.phase == 1:
            file_list = PHASE_1_FILES
            print(f"📋 Phase 1: Top 10 priority files")
        elif args.phase == 2:
            file_list = PHASE_2_FILES
            print(f"📋 Phase 2: Medium priority files")
        else:
            # Phase 3: All remaining files
            print(f"📋 Phase 3: All remaining files")
            report_path = Path("evidence_curation_report.txt")
            files_from_report = parse_curation_report(report_path)
            processed_files = set(PHASE_1_FILES + PHASE_2_FILES)
            file_list = [
                f["file"] for f in files_from_report
                if f["file"] not in processed_files
            ]

    elif args.from_report:
        report_path = Path("evidence_curation_report.txt")
        files_from_report = parse_curation_report(report_path)
        file_list = [f["file"] for f in files_from_report]
        print(f"📋 Processing files from curation report (sorted by issue count)")

    elif getattr(args, 'all', False):
        communities_dir = Path("kb/communities")
        file_list = sorted(p.name for p in communities_dir.glob("*.yaml")
                           if not any(x in p.name for x in ['.bak', '.backup']))
        print(f"📋 Processing all {len(file_list)} YAML files in kb/communities/")

    else:
        file_list = args.files
        print(f"📋 Processing specified files")

    # Apply limit if specified
    if args.limit:
        file_list = file_list[:args.limit]
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
        relaxed=args.relaxed
    )

    return 0


if __name__ == '__main__':
    exit(main())
