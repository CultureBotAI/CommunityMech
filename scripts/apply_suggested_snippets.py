#!/usr/bin/env python3
"""
Semi-automated evidence snippet replacement tool.

Parses evidence_curation_report.txt to extract suggested snippet fixes
and provides an interactive interface to review and apply them to YAML files.

Usage:
    python scripts/apply_suggested_snippets.py --file FILENAME.yaml
    python scripts/apply_suggested_snippets.py --file FILENAME.yaml --auto-approve
"""

import argparse
import re
import shutil
from pathlib import Path
from typing import Dict, List, Tuple, Optional
import yaml


class SnippetFix:
    """Represents a suggested snippet fix from the curation report."""

    def __init__(self, organism: str, reference: str, current: str, suggested: str):
        self.organism = organism
        self.reference = reference
        self.current = current
        self.suggested = suggested

    def __repr__(self):
        return f"SnippetFix(organism={self.organism}, ref={self.reference})"


def parse_curation_report(report_path: Path, target_file: str) -> List[SnippetFix]:
    """
    Parse the evidence curation report and extract suggested fixes for a specific file.

    Args:
        report_path: Path to evidence_curation_report.txt
        target_file: Name of the YAML file to extract fixes for (e.g., "Australian_Lead_Zinc_Polymetallic.yaml")

    Returns:
        List of SnippetFix objects with suggested replacements
    """
    fixes = []

    with open(report_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the section for this file
    file_pattern = re.escape(target_file) + r' \(\d+ issues\)'
    file_match = re.search(file_pattern, content)

    if not file_match:
        print(f"⚠️  File {target_file} not found in curation report")
        return fixes

    # Extract the section for this file (until next file or end)
    start_pos = file_match.start()
    next_file_match = re.search(r'\n\n[A-Z].*\.yaml \(\d+ issues\)', content[start_pos + len(target_file):])

    if next_file_match:
        end_pos = start_pos + len(target_file) + next_file_match.start()
        section = content[start_pos:end_pos]
    else:
        section = content[start_pos:]

    # Parse SNIPPET_NOT_IN_SOURCE entries
    snippet_section_match = re.search(r'SNIPPET_NOT_IN_SOURCE \(\d+ instances\)\s*~+\s*(.+?)(?:\n\n\n|\Z)', section, re.DOTALL)

    if not snippet_section_match:
        print(f"ℹ️  No SNIPPET_NOT_IN_SOURCE issues found for {target_file}")
        return fixes

    snippet_section = snippet_section_match.group(1)

    # Parse individual fix entries
    # Pattern: Organism/Item: ... Reference: ... Current: ... Suggested fix: ...
    entries = re.split(r'\n\nOrganism/Item: ', snippet_section)

    for entry in entries:
        if not entry.strip():
            continue

        # Add back the "Organism/Item: " prefix if needed
        if not entry.startswith('Organism/Item:'):
            entry = 'Organism/Item: ' + entry

        # Extract fields
        organism_match = re.search(r'Organism/Item: (.+)', entry)
        reference_match = re.search(r'Reference: (.+)', entry)
        current_match = re.search(r'Current: (.+)', entry)
        suggested_match = re.search(r'Suggested fix: (.+)', entry, re.DOTALL)

        if all([organism_match, reference_match, current_match, suggested_match]):
            organism = organism_match.group(1).strip()
            reference = reference_match.group(1).strip()
            current = current_match.group(1).strip()
            suggested = suggested_match.group(1).strip()

            # Clean up suggested text (remove trailing newlines, extra spaces)
            suggested = ' '.join(suggested.split())

            fixes.append(SnippetFix(organism, reference, current, suggested))

    return fixes


def load_yaml_file(yaml_path: Path) -> Tuple[dict, str]:
    """
    Load YAML file while preserving formatting.

    Returns:
        Tuple of (parsed_data, raw_content)
    """
    with open(yaml_path, 'r', encoding='utf-8') as f:
        raw_content = f.read()

    with open(yaml_path, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)

    return data, raw_content


def apply_snippet_fix(raw_content: str, fix: SnippetFix, max_matches: int = 1) -> Tuple[str, bool]:
    """
    Apply a snippet fix to the raw YAML content.

    Args:
        raw_content: Raw YAML file content as string
        fix: SnippetFix object with current and suggested snippets
        max_matches: Maximum number of replacements to make

    Returns:
        Tuple of (updated_content, success)
    """
    # Escape special regex characters in the current snippet
    # But we need to handle potential truncation (snippets ending with "...")
    current_pattern = re.escape(fix.current)

    # If the current snippet appears truncated, make the pattern more flexible
    if fix.current.endswith('...') or len(fix.current) < 50:
        # Remove trailing "..." from pattern and make it match more flexibly
        current_pattern = current_pattern.replace(r'\.\.\.', r'.*?')
        current_pattern = current_pattern.rstrip()
        # Match the snippet allowing for continuation
        pattern = rf'snippet:\s*["\']?{current_pattern}[^"\']*["\']?'
    else:
        # Exact match for full snippets
        pattern = rf'snippet:\s*["\']?{current_pattern}["\']?'

    # Try to find and replace
    matches = list(re.finditer(pattern, raw_content, re.DOTALL))

    if not matches:
        return raw_content, False

    if len(matches) > max_matches:
        print(f"⚠️  Found {len(matches)} matches for snippet, expected {max_matches}")
        return raw_content, False

    # Replace the snippet content
    # We need to preserve the YAML formatting (indentation, quotes, etc.)
    for match in matches[:max_matches]:
        match_text = match.group(0)

        # Determine quote style from original
        if match_text.startswith('snippet: "'):
            new_snippet = f'snippet: "{fix.suggested}"'
        elif match_text.startswith("snippet: '"):
            new_snippet = f"snippet: '{fix.suggested}'"
        else:
            # No quotes, add them for safety
            new_snippet = f'snippet: "{fix.suggested}"'

        raw_content = raw_content[:match.start()] + new_snippet + raw_content[match.end():]

    return raw_content, True


def interactive_review(fixes: List[SnippetFix], yaml_path: Path, auto_approve: bool = False) -> int:
    """
    Interactively review and apply snippet fixes.

    Args:
        fixes: List of SnippetFix objects
        yaml_path: Path to the YAML file to update
        auto_approve: If True, automatically apply all fixes without prompting

    Returns:
        Number of fixes applied
    """
    if not fixes:
        print("✅ No snippet fixes found to apply")
        return 0

    print(f"\n📋 Found {len(fixes)} suggested snippet fixes for {yaml_path.name}\n")

    # Load YAML file
    data, raw_content = load_yaml_file(yaml_path)

    # Create backup
    backup_path = yaml_path.with_suffix('.yaml.bak_snippets')
    shutil.copy2(yaml_path, backup_path)
    print(f"💾 Created backup: {backup_path}\n")

    applied_count = 0
    skipped_count = 0
    failed_count = 0

    for i, fix in enumerate(fixes, 1):
        print(f"{'='*80}")
        print(f"Fix {i}/{len(fixes)}")
        print(f"{'='*80}")
        print(f"Organism/Item: {fix.organism}")
        print(f"Reference:     {fix.reference}")
        print(f"\n❌ CURRENT (invalid):")
        print(f"   {fix.current[:200]}{'...' if len(fix.current) > 200 else ''}")
        print(f"\n✅ SUGGESTED (from abstract):")
        print(f"   {fix.suggested[:200]}{'...' if len(fix.suggested) > 200 else ''}")
        print()

        if auto_approve:
            choice = 'a'
        else:
            choice = input("👉 [A]pply, [E]dit, [S]kip, [Q]uit? ").lower().strip()

        if choice == 'q':
            print("\n🛑 Quitting without applying remaining fixes")
            break
        elif choice == 's':
            print("⏭️  Skipped")
            skipped_count += 1
            continue
        elif choice == 'e':
            print("\nEnter new snippet (or press Enter to skip):")
            custom_snippet = input().strip()
            if custom_snippet:
                fix.suggested = custom_snippet
                print(f"✏️  Using custom snippet")
            else:
                print("⏭️  Skipped")
                skipped_count += 1
                continue

        # Apply the fix
        raw_content, success = apply_snippet_fix(raw_content, fix)

        if success:
            print("✅ Applied")
            applied_count += 1
        else:
            print("❌ Failed to find snippet in file (may already be fixed or snippet doesn't match)")
            failed_count += 1

        print()

    # Save updated content if any fixes were applied
    if applied_count > 0:
        with open(yaml_path, 'w', encoding='utf-8') as f:
            f.write(raw_content)

        print(f"\n{'='*80}")
        print(f"📊 SUMMARY")
        print(f"{'='*80}")
        print(f"✅ Applied:  {applied_count}")
        print(f"⏭️  Skipped:  {skipped_count}")
        print(f"❌ Failed:   {failed_count}")
        print(f"\n💾 Updated file: {yaml_path}")
        print(f"💾 Backup saved: {backup_path}")
        print(f"\n🔍 Next: Validate with curate_evidence_with_pdfs.py")
    else:
        print("\n⚠️  No fixes were applied")
        backup_path.unlink()  # Remove backup if no changes

    return applied_count


def main():
    parser = argparse.ArgumentParser(
        description='Semi-automated evidence snippet replacement tool'
    )
    parser.add_argument(
        '--file',
        required=True,
        help='YAML file to process (e.g., Australian_Lead_Zinc_Polymetallic.yaml)'
    )
    parser.add_argument(
        '--report',
        default='evidence_curation_report.txt',
        help='Path to curation report (default: evidence_curation_report.txt)'
    )
    parser.add_argument(
        '--auto-approve',
        action='store_true',
        help='Automatically apply all suggested fixes without prompting'
    )

    args = parser.parse_args()

    # Resolve paths
    yaml_filename = args.file
    if not yaml_filename.endswith('.yaml'):
        yaml_filename += '.yaml'

    yaml_path = Path('kb/communities') / yaml_filename
    report_path = Path(args.report)

    if not yaml_path.exists():
        print(f"❌ File not found: {yaml_path}")
        return 1

    if not report_path.exists():
        print(f"❌ Report not found: {report_path}")
        print(f"   Run: poetry run python scripts/curate_evidence_with_pdfs.py --quick")
        return 1

    # Parse report
    print(f"📖 Parsing curation report: {report_path}")
    fixes = parse_curation_report(report_path, yaml_filename)

    if not fixes:
        print(f"\n✅ No snippet fixes needed for {yaml_filename}")
        return 0

    # Interactive review and application
    applied = interactive_review(fixes, yaml_path, args.auto_approve)

    if applied > 0:
        print(f"\n✅ Successfully applied {applied} snippet fixes")
        print(f"\n📋 Next steps:")
        print(f"   1. Validate: poetry run python scripts/curate_evidence_with_pdfs.py --file {yaml_filename}")
        print(f"   2. Schema check: just validate {yaml_path}")
        print(f"   3. Review changes: git diff {yaml_path}")
        return 0
    else:
        return 1


if __name__ == '__main__':
    exit(main())
