#!/usr/bin/env python3
"""
Quick analysis of literature review report

Extracts key statistics and prioritizes issues for immediate action.
"""

import re
from pathlib import Path
from collections import defaultdict


def analyze_report(report_path: Path):
    """Parse and analyze the literature review report"""

    if not report_path.exists():
        print(f"Report not found: {report_path}")
        return

    with open(report_path, 'r') as f:
        content = f.read()

    # Extract summary statistics
    stats = {}

    total_match = re.search(r'Total evidence items:\s*(\d+)', content)
    if total_match:
        stats['total_items'] = int(total_match.group(1))

    abstracts_fetched = re.search(r'Abstracts fetched:\s*(\d+)', content)
    if abstracts_fetched:
        stats['abstracts_fetched'] = int(abstracts_fetched.group(1))

    abstracts_failed = re.search(r'Abstracts failed:\s*(\d+)', content)
    if abstracts_failed:
        stats['abstracts_failed'] = int(abstracts_failed.group(1))

    snippets_valid = re.search(r'Snippets valid:\s*(\d+)', content)
    if snippets_valid:
        stats['snippets_valid'] = int(snippets_valid.group(1))

    snippets_invalid = re.search(r'Snippets invalid:\s*(\d+)', content)
    if snippets_invalid:
        stats['snippets_invalid'] = int(snippets_invalid.group(1))

    missing_snippets = re.search(r'Missing snippets:\s*(\d+)', content)
    if missing_snippets:
        stats['missing_snippets'] = int(missing_snippets.group(1))

    pdfs_available = re.search(r'PDFs available:\s*(\d+)', content)
    if pdfs_available:
        stats['pdfs_available'] = int(pdfs_available.group(1))

    # Print summary
    print("=" * 80)
    print("LITERATURE REVIEW SUMMARY")
    print("=" * 80)
    print()

    if 'total_items' in stats:
        print(f"Total evidence items: {stats['total_items']}")
        print()

        if 'abstracts_fetched' in stats:
            rate = (stats['abstracts_fetched'] / stats['total_items']) * 100
            print(f"Abstracts fetched: {stats['abstracts_fetched']} ({rate:.1f}%)")

        if 'abstracts_failed' in stats:
            rate = (stats['abstracts_failed'] / stats['total_items']) * 100
            print(f"Abstracts failed: {stats['abstracts_failed']} ({rate:.1f}%)")

        print()

        if 'snippets_valid' in stats:
            print(f"Snippets valid: {stats['snippets_valid']}")

        if 'snippets_invalid' in stats:
            print(f"Snippets invalid: {stats['snippets_invalid']}")

        if 'missing_snippets' in stats:
            print(f"Missing snippets: {stats['missing_snippets']}")

        print()

        if 'pdfs_available' in stats:
            rate = (stats['pdfs_available'] / stats['total_items']) * 100
            print(f"PDFs available: {stats['pdfs_available']} ({rate:.1f}%)")

    print()
    print("=" * 80)

    # Extract files with most issues
    print("\nFILES WITH MOST ISSUES:")
    print("-" * 80)

    issues_section = re.search(r'ISSUES BY FILE\n={80}\n\n(.+?)\n\n={80}', content, re.DOTALL)
    if issues_section:
        files = re.findall(r'\n([A-Za-z_]+\.yaml)\n-{80}', issues_section.group(1))
        issue_counts = defaultdict(int)

        current_file = None
        for line in issues_section.group(1).split('\n'):
            if line.endswith('.yaml'):
                current_file = line.strip()
            elif line.startswith('Issues:') and current_file:
                issue_counts[current_file] += 1

        # Sort by issue count
        sorted_files = sorted(issue_counts.items(), key=lambda x: x[1], reverse=True)

        for file, count in sorted_files[:10]:
            print(f"  {file}: {count} issues")

    print()
    print("=" * 80)


def analyze_priority_updates(priority_path: Path):
    """Analyze priority updates file"""

    if not priority_path.exists():
        print(f"Priority file not found: {priority_path}")
        return

    with open(priority_path, 'r') as f:
        content = f.read()

    print("\nPRIORITY UPDATES NEEDED:")
    print("=" * 80)

    # Extract counts
    critical_match = re.search(r'CRITICAL \((\d+) items\)', content)
    high_match = re.search(r'HIGH \((\d+) items\)', content)
    medium_match = re.search(r'MEDIUM \((\d+) items\)', content)

    if critical_match:
        print(f"CRITICAL: {critical_match.group(1)} items (invalid/missing evidence)")
    if high_match:
        print(f"HIGH: {high_match.group(1)} items (missing snippets, abstract available)")
    if medium_match:
        print(f"MEDIUM: {medium_match.group(1)} items (missing metadata)")

    print()
    print("=" * 80)


def main():
    """Main analysis"""
    report_path = Path('literature_review_report.txt')
    priority_path = Path('priority_literature_updates.txt')

    print("\nLiterature Review Analysis")
    print("=" * 80)
    print()

    analyze_report(report_path)
    analyze_priority_updates(priority_path)

    print("\nDetailed reports available:")
    print(f"  - {report_path}")
    print(f"  - {priority_path}")
    print()


if __name__ == '__main__':
    main()
