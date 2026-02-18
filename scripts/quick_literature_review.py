#!/usr/bin/env python3
"""
Quick Literature Review - Fast validation without PDF fetching

Validates abstracts and snippets only, skipping PDF discovery.
Much faster for initial assessment (~5-10 minutes vs 60-90 minutes).
"""

import yaml
import sys
from pathlib import Path
from typing import Dict, List, Optional
from collections import defaultdict
from dataclasses import dataclass

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from communitymech.literature_enhanced import EnhancedLiteratureFetcher

# Disable PDF fetching for speed
class FastFetcher(EnhancedLiteratureFetcher):
    """Override to skip PDF fetching"""

    def fetch_pdf_url(self, doi: str):
        """Skip PDF fetching for speed"""
        return None

@dataclass
class QuickResult:
    reference: str
    file: str
    context: str
    has_abstract: bool
    snippet_valid: bool = False
    has_snippet: bool = False
    issue: Optional[str] = None


def main():
    print("QUICK LITERATURE REVIEW (Abstract validation only)")
    print("=" * 80)
    print()

    kb_dir = Path('kb/communities')
    fetcher = FastFetcher(cache_dir=".literature_cache", use_fallback_pdf=False)

    # Scan all YAMLs
    print("Scanning YAMLs...")
    yaml_files = sorted(kb_dir.glob('*.yaml'))
    all_evidence = []

    for yaml_path in yaml_files:
        with open(yaml_path, 'r') as f:
            data = yaml.safe_load(f)

        # Extract evidence
        if 'taxonomy' in data:
            for taxon in data['taxonomy']:
                if 'evidence' in taxon:
                    for ev in taxon['evidence']:
                        all_evidence.append({
                            'file': yaml_path.name,
                            'context': 'taxonomy',
                            'ref': ev.get('reference', ''),
                            'snippet': ev.get('snippet')
                        })

        if 'ecological_interactions' in data:
            for interaction in data['ecological_interactions']:
                if 'evidence' in interaction:
                    for ev in interaction['evidence']:
                        all_evidence.append({
                            'file': yaml_path.name,
                            'context': 'interaction',
                            'ref': ev.get('reference', ''),
                            'snippet': ev.get('snippet')
                        })

    print(f"Found {len(all_evidence)} evidence items")
    print()

    # Quick validation
    print("Validating (abstracts only, no PDFs)...")
    results = []
    stats = defaultdict(int)

    for i, ev in enumerate(all_evidence, 1):
        if i % 50 == 0:
            print(f"  Progress: {i}/{len(all_evidence)}")

        result = QuickResult(
            reference=ev['ref'],
            file=ev['file'],
            context=ev['context'],
            has_abstract=False,
            has_snippet=bool(ev['snippet'])
        )

        # Fetch abstract only
        try:
            paper = fetcher.fetch_paper(ev['ref'], download_pdf=False)

            if paper['abstract']:
                result.has_abstract = True
                stats['abstracts_ok'] += 1

                # Validate snippet if present
                if ev['snippet']:
                    valid = fetcher.validate_evidence_snippet(ev['snippet'], paper['abstract'])
                    result.snippet_valid = valid
                    if valid:
                        stats['snippets_valid'] += 1
                    else:
                        stats['snippets_invalid'] += 1
                        result.issue = "Snippet not in abstract"
                else:
                    stats['missing_snippet'] += 1
                    result.issue = "Missing snippet"
            else:
                stats['abstracts_failed'] += 1
                result.issue = "Abstract not found"

        except Exception as e:
            stats['errors'] += 1
            result.issue = f"Error: {str(e)[:50]}"

        results.append(result)

    # Summary
    print()
    print("=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print(f"Total evidence: {len(all_evidence)}")
    print(f"Abstracts fetched: {stats['abstracts_ok']}")
    print(f"Abstracts failed: {stats['abstracts_failed']}")
    print(f"Snippets valid: {stats['snippets_valid']}")
    print(f"Snippets invalid: {stats['snippets_invalid']}")
    print(f"Missing snippets: {stats['missing_snippet']}")
    print(f"Errors: {stats['errors']}")
    print()

    # Quality metrics
    if len(all_evidence) > 0:
        abstract_rate = (stats['abstracts_ok'] / len(all_evidence)) * 100
        print(f"Abstract fetch rate: {abstract_rate:.1f}%")

        if stats['snippets_valid'] + stats['snippets_invalid'] > 0:
            snippet_rate = (stats['snippets_valid'] / (stats['snippets_valid'] + stats['snippets_invalid'])) * 100
            print(f"Snippet validation rate: {snippet_rate:.1f}%")

    # Write quick report
    with open('quick_literature_report.txt', 'w') as f:
        f.write("QUICK LITERATURE REVIEW\n")
        f.write("=" * 80 + "\n\n")
        f.write(f"Total: {len(all_evidence)}\n")
        f.write(f"Abstracts OK: {stats['abstracts_ok']}\n")
        f.write(f"Abstracts failed: {stats['abstracts_failed']}\n")
        f.write(f"Snippets valid: {stats['snippets_valid']}\n")
        f.write(f"Snippets invalid: {stats['snippets_invalid']}\n")
        f.write(f"Missing snippets: {stats['missing_snippet']}\n\n")

        # Issues
        f.write("ISSUES:\n" + "-" * 80 + "\n\n")
        for result in results:
            if result.issue:
                f.write(f"{result.file} - {result.reference}\n")
                f.write(f"  Issue: {result.issue}\n\n")

    print()
    print("✓ Report: quick_literature_report.txt")


if __name__ == '__main__':
    main()
