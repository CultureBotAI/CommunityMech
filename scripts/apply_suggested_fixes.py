#!/usr/bin/env python3
"""
Apply suggested snippet fixes from the evidence curation report to all YAML files.

Reads evidence_curation_report.txt, extracts SNIPPET_NOT_IN_SOURCE entries that have
a valid "Suggested fix:" line, skips wrong-paper entries (where the fetched abstract
is from a completely different paper), and applies the fixes to YAML files.

Usage:
    poetry run python scripts/apply_suggested_fixes.py
    poetry run python scripts/apply_suggested_fixes.py --report evidence_curation_report.txt
    poetry run python scripts/apply_suggested_fixes.py --dry-run
"""

import argparse
import re
import sys
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import yaml

# Add scripts to path for imports
sys.path.insert(0, str(Path(__file__).parent))

# Wrong-paper detection patterns: these phrases indicate the "Suggested fix" came
# from a completely different paper than the one referenced in the YAML.
WRONG_PAPER_PATTERNS = [
    # Ewaste_Bioleaching_Consortium.yaml — doi:10.3390/min11090932 → bentonite paper
    "Bentonite is currently proposed",
    # Mixed_Gallium_LED_Recovery_Consortium.yaml — doi:10.1016/j.jhazmat.2024.135891 → CW-MFC/PFOA paper
    "constructed wetland-microbial fuel cell",
    # Copper_Biomining_Heap_Leach.yaml — doi:10.1007/s00248-013-0274-4 → salt brines paper
    "The genetic diversity of a collection of 336 spore-forming isolates",
    # Ferroplasma_Leptospirillum_Syntrophy.yaml — doi:10.1016/j.chemosphere.2025.144565 → ZnO nanocomposite paper
    "This study addresses the treatment of polluted Yamuna river",
    # PGM_Spent_Catalyst_Bioleaching.yaml — doi:10.1016/j.wasman.2023.08.011 → plastic waste/landfill paper
    "Plastic wastes deposited in landfills",
    # Aspergillus_Indium_LED_Recovery.yaml — doi:10.1016/j.scitotenv.2021.147918 → Bisphenol AF paper
    "Bisphenol AF (BPAF)",
    # Bayan_Obo_REE_Tailings_Consortium.yaml — doi:10.1016/j.chemosphere.2024.143054 → environmental pollution paper
    "Contemporary global industrialization",
]


class SnippetFix:
    """Represents a suggested snippet fix from the curation report."""

    def __init__(self, yaml_file: str, organism: str, reference: str, current: str, suggested: str):
        self.yaml_file = yaml_file
        self.organism = organism
        self.reference = reference
        self.current = current
        self.suggested = suggested

    def __repr__(self):
        return f"SnippetFix(file={self.yaml_file}, organism={self.organism}, ref={self.reference})"


def is_wrong_paper_fix(suggested: str) -> bool:
    """Check if the suggested fix is from a wrong paper (should be skipped)."""
    for pattern in WRONG_PAPER_PATTERNS:
        if pattern.lower() in suggested.lower():
            return True
    return False


def parse_curation_report(report_path: Path) -> List[SnippetFix]:
    """
    Parse the evidence curation report and extract all SNIPPET_NOT_IN_SOURCE fixes.

    Uses a line-by-line state machine:
    - File header detected → set current_file
    - SNIPPET_NOT_IN_SOURCE section → start collecting entries
    - Each entry ends at a blank line

    Returns:
        List of SnippetFix objects for all files
    """
    fixes = []

    with open(report_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Split into file sections
    # Format: "FILENAME.yaml (N issues)\n---..."
    file_section_pattern = re.compile(
        r"^([A-Za-z0-9_\-]+\.yaml) \(\d+ issues\)\s*\n-+\s*\n",
        re.MULTILINE,
    )

    file_sections = []
    for match in file_section_pattern.finditer(content):
        file_sections.append((match.group(1), match.start()))

    for i, (filename, start_pos) in enumerate(file_sections):
        # Find end of this file's section
        end_pos = file_sections[i + 1][1] if i + 1 < len(file_sections) else len(content)
        section = content[start_pos:end_pos]

        # Find SNIPPET_NOT_IN_SOURCE subsection
        snip_match = re.search(
            r"SNIPPET_NOT_IN_SOURCE \(\d+ instances\)\s*~+\s*(.*?)(?:\n\n\n|\n\n[A-Z_]+\s*\(|\Z)",
            section,
            re.DOTALL,
        )
        if not snip_match:
            continue

        snippet_section = snip_match.group(1)

        # Parse individual entries
        # Format:
        # Organism/Item: X
        # Reference: Y
        # Current: Z...
        # Suggested fix: W...
        #
        # (blank line separates entries)
        entries = re.split(r"\n\n(?=Organism/Item:)", snippet_section.strip())

        for entry in entries:
            if not entry.strip():
                continue

            organism_match = re.search(r"^Organism/Item:\s*(.+)", entry, re.MULTILINE)
            reference_match = re.search(r"^Reference:\s*(.+)", entry, re.MULTILINE)
            current_match = re.search(r"^Current:\s*(.+)", entry, re.MULTILINE)
            suggested_match = re.search(r"^Suggested fix:\s*(.+)", entry, re.MULTILINE | re.DOTALL)

            if not all([organism_match, reference_match, current_match, suggested_match]):
                continue

            organism = organism_match.group(1).strip()
            reference = reference_match.group(1).strip()
            current = current_match.group(1).strip()
            suggested = suggested_match.group(1).strip()
            # Clean up suggested text (remove trailing newlines, extra spaces)
            suggested = " ".join(suggested.split())

            if not suggested:
                continue

            fixes.append(SnippetFix(
                yaml_file=filename,
                organism=organism,
                reference=reference,
                current=current,
                suggested=suggested,
            ))

    return fixes


def apply_snippet_fix_to_yaml_content(
    raw_content: str, current_snippet: str, new_snippet: str,
    allow_multi_match: bool = False,
) -> Tuple[str, bool]:
    """
    Apply a snippet replacement to raw YAML file content using string matching.

    Handles:
    - Truncated snippets in the curation report (report shows ~100 chars only)
    - Multi-line plain YAML scalars (continuation lines with leading whitespace)
    - Single/double quoted snippets

    Args:
        allow_multi_match: If True, replace ALL occurrences when multiple are found
                           (safe when the same current snippet appears in multiple
                           evidence items all needing the same fix).

    Returns:
        Tuple of (updated_content, success)
    """
    # Strip trailing '...' from truncated report snippets
    search_text = current_snippet
    if search_text.endswith("..."):
        search_text = search_text[:-3].rstrip()

    # Escape special regex chars in the snippet
    escaped = re.escape(search_text)

    # Pattern 1: simple single-line match
    # Matches: snippet: "...SNIPPET..." or snippet: '...SNIPPET...' or snippet: SNIPPET...
    # Allows the snippet to continue past the matched prefix (for truncated snippets)
    # and optionally have continuation lines (YAML plain scalar multi-line)
    pattern = (
        rf'snippet:\s*'          # "snippet:" with optional whitespace
        rf'["\']?'               # optional opening quote
        rf'{escaped}'            # the snippet text (prefix match)
        rf'[^\n]*'               # rest of first line
        rf'(?:\n[ \t]+[^\n]*)*'  # optional continuation lines (indented)
        rf'["\']?'               # optional closing quote
    )

    matches = list(re.finditer(pattern, raw_content))

    if not matches:
        return raw_content, False

    if len(matches) > 1 and not allow_multi_match:
        # Multiple matches - can't safely replace without ambiguity
        # unless all occurrences should get the same fix
        return raw_content, False

    # Replace all matches (in reverse order to preserve string positions)
    for match in reversed(matches):
        match_text = match.group(0)
        after_snippet = match_text[match_text.index("snippet:") + 8:].lstrip()
        if after_snippet.startswith('"'):
            new_snippet_yaml = f'snippet: "{new_snippet}"'
        elif after_snippet.startswith("'"):
            new_snippet_yaml = f"snippet: '{new_snippet}'"
        else:
            new_snippet_yaml = f'snippet: "{new_snippet}"'

        raw_content = raw_content[:match.start()] + new_snippet_yaml + raw_content[match.end():]

    return raw_content, True


def apply_fixes_to_file(
    yaml_path: Path,
    fixes: List[SnippetFix],
    dry_run: bool = False,
) -> Tuple[int, int, int]:
    """
    Apply all fixes for a file to its YAML content.

    Groups fixes by (current_snippet, suggested) so that when the same current
    snippet appears multiple times with the same suggested fix, all occurrences
    are replaced in one pass.

    Returns:
        Tuple of (applied, skipped_wrong_paper, failed)
    """
    with open(yaml_path, "r", encoding="utf-8") as f:
        raw_content = f.read()

    original_content = raw_content
    applied = 0
    skipped_wrong_paper = 0
    failed = 0

    # Deduplicate: group by (current, suggested) so we apply each unique
    # (current -> suggested) replacement once, using allow_multi_match.
    seen_replacements: Dict[Tuple[str, str], List[SnippetFix]] = {}
    ordered_keys: List[Tuple[str, str]] = []

    for fix in fixes:
        key = (fix.current, fix.suggested)
        if key not in seen_replacements:
            seen_replacements[key] = []
            ordered_keys.append(key)
        seen_replacements[key].append(fix)

    for key in ordered_keys:
        group = seen_replacements[key]
        fix = group[0]  # representative fix for logging

        # Skip wrong-paper suggested fixes
        if is_wrong_paper_fix(fix.suggested):
            for f in group:
                print(f"  ⚠️  SKIP (wrong paper): {f.organism[:50]} / {f.reference}")
                skipped_wrong_paper += 1
            continue

        # Always use allow_multi_match=True: the report may show only one entry
        # per file but the YAML may have multiple evidence items with the same
        # truncated snippet text (all need the same fix).
        raw_content, success = apply_snippet_fix_to_yaml_content(
            raw_content, fix.current, fix.suggested, allow_multi_match=True
        )

        if success:
            for f in group:
                print(f"  ✓  Applied: {f.organism[:50]} / {f.reference}")
            applied += len(group)
        else:
            for f in group:
                print(f"  ✗  Failed:  {f.organism[:50]} / {f.reference}")
            failed += len(group)

    if applied > 0 and not dry_run:
        # Make a backup before writing
        backup_path = yaml_path.with_suffix(".yaml.bak_apply_fixes")
        with open(backup_path, "w", encoding="utf-8") as f:
            f.write(original_content)

        with open(yaml_path, "w", encoding="utf-8") as f:
            f.write(raw_content)
        print(f"  💾 Saved (backup: {backup_path.name})")
    elif dry_run and applied > 0:
        print(f"  [DRY RUN] Would apply {applied} fix(es) to {yaml_path.name}")

    return applied, skipped_wrong_paper, failed


def main():
    parser = argparse.ArgumentParser(
        description="Apply suggested snippet fixes from evidence curation report to all YAML files"
    )
    parser.add_argument(
        "--report",
        default="evidence_curation_report.txt",
        help="Path to curation report (default: evidence_curation_report.txt)",
    )
    parser.add_argument(
        "--kb-dir",
        default="kb/communities",
        help="Path to YAML communities directory (default: kb/communities)",
    )
    parser.add_argument(
        "--files",
        nargs="*",
        help="Limit to specific YAML files (by filename, e.g. AMD_Nitrososphaerota_Archaeal.yaml)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be done without writing any files",
    )

    args = parser.parse_args()

    report_path = Path(args.report)
    kb_dir = Path(args.kb_dir)

    if not report_path.exists():
        print(f"ERROR: Report not found: {report_path}")
        print("Run: poetry run python scripts/curate_evidence_with_pdfs.py --quick")
        return 1

    if not kb_dir.exists():
        print(f"ERROR: YAML directory not found: {kb_dir}")
        return 1

    print(f"Parsing curation report: {report_path}")
    all_fixes = parse_curation_report(report_path)

    if not all_fixes:
        print("No SNIPPET_NOT_IN_SOURCE fixes found in report.")
        return 0

    # Group by file
    fixes_by_file: Dict[str, List[SnippetFix]] = {}
    for fix in all_fixes:
        fixes_by_file.setdefault(fix.yaml_file, []).append(fix)

    # Filter to specific files if requested
    if args.files:
        filter_set = set(args.files)
        fixes_by_file = {k: v for k, v in fixes_by_file.items() if k in filter_set}

    print(f"Found {len(all_fixes)} fixes across {len(fixes_by_file)} files\n")

    total_applied = 0
    total_skipped = 0
    total_failed = 0

    for filename, fixes in sorted(fixes_by_file.items()):
        yaml_path = kb_dir / filename

        if not yaml_path.exists():
            print(f"\n[{filename}] — FILE NOT FOUND, skipping")
            continue

        print(f"\n[{filename}] — {len(fixes)} suggested fix(es)")
        applied, skipped, failed = apply_fixes_to_file(yaml_path, fixes, dry_run=args.dry_run)
        total_applied += applied
        total_skipped += skipped
        total_failed += failed

    print(f"\n{'='*60}")
    print(f"SUMMARY")
    print(f"{'='*60}")
    print(f"  Applied:             {total_applied}")
    print(f"  Skipped (wrong paper): {total_skipped}")
    print(f"  Failed (no match):   {total_failed}")
    if args.dry_run:
        print(f"\n  [DRY RUN] No files were modified.")
    else:
        print(f"\n  Run validation: poetry run python scripts/curate_evidence_with_pdfs.py --quick")
    return 0


if __name__ == "__main__":
    exit(main())
