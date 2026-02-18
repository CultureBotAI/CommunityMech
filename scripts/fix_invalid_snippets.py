#!/usr/bin/env python3
"""
Fix Invalid Evidence Snippets

Identifies snippets that don't match abstracts and helps replace them with valid quotes.
"""

import yaml
import sys
import re
from pathlib import Path
from typing import Dict, List, Tuple, Optional
from collections import defaultdict

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from communitymech.literature_enhanced import EnhancedLiteratureFetcher


class SnippetFixer:
    """Fix invalid evidence snippets"""

    def __init__(self):
        self.fetcher = EnhancedLiteratureFetcher(
            cache_dir=".literature_cache",
            use_fallback_pdf=False
        )
        self.invalid_snippets = []

    def find_invalid_snippets(self, yaml_path: Path) -> List[Dict]:
        """Find all invalid snippets in a YAML file"""

        with open(yaml_path, 'r') as f:
            data = yaml.safe_load(f)

        invalid = []

        # Check taxonomy
        if 'taxonomy' in data:
            for taxon_idx, taxon_entry in enumerate(data['taxonomy']):
                if 'evidence' not in taxon_entry:
                    continue

                organism = taxon_entry.get('taxon_term', {}).get('preferred_term', 'Unknown')

                for ev_idx, ev in enumerate(taxon_entry['evidence']):
                    snippet = ev.get('snippet')
                    reference = ev.get('reference', '')

                    if not snippet or not reference:
                        continue

                    # Fetch abstract
                    try:
                        paper = self.fetcher.fetch_paper(reference, download_pdf=False)
                        if paper['abstract']:
                            valid = self.fetcher.validate_evidence_snippet(snippet, paper['abstract'])

                            if not valid:
                                invalid.append({
                                    'file': yaml_path.name,
                                    'context': 'taxonomy',
                                    'organism': organism,
                                    'reference': reference,
                                    'snippet': snippet,
                                    'abstract': paper['abstract'],
                                    'taxon_idx': taxon_idx,
                                    'ev_idx': ev_idx
                                })
                    except:
                        pass

        # Check interactions
        if 'ecological_interactions' in data:
            for int_idx, interaction in enumerate(data['ecological_interactions']):
                if 'evidence' not in interaction:
                    continue

                int_name = interaction.get('name', 'Unknown')

                for ev_idx, ev in enumerate(interaction['evidence']):
                    snippet = ev.get('snippet')
                    reference = ev.get('reference', '')

                    if not snippet or not reference:
                        continue

                    # Fetch abstract
                    try:
                        paper = self.fetcher.fetch_paper(reference, download_pdf=False)
                        if paper['abstract']:
                            valid = self.fetcher.validate_evidence_snippet(snippet, paper['abstract'])

                            if not valid:
                                invalid.append({
                                    'file': yaml_path.name,
                                    'context': 'interaction',
                                    'organism': int_name,
                                    'reference': reference,
                                    'snippet': snippet,
                                    'abstract': paper['abstract'],
                                    'int_idx': int_idx,
                                    'ev_idx': ev_idx
                                })
                    except:
                        pass

        return invalid

    def extract_best_snippet(self, abstract: str, organism: str, keywords: List[str] = None) -> Optional[str]:
        """Extract best matching snippet from abstract"""

        # Split into sentences
        sentences = self._split_sentences(abstract)

        if not sentences:
            return None

        # If keywords provided, find sentence with most keywords
        if keywords:
            best_sentence = None
            best_score = 0

            for sentence in sentences:
                score = sum(1 for kw in keywords if kw.lower() in sentence.lower())
                if score > best_score:
                    best_score = score
                    best_sentence = sentence

            if best_sentence and best_score > 0:
                return self._clean_sentence(best_sentence)

        # Otherwise, find sentence mentioning organism
        for sentence in sentences:
            if organism and organism.lower() in sentence.lower():
                return self._clean_sentence(sentence)

        # Fallback: return first substantive sentence
        for sentence in sentences:
            if len(sentence) > 50:
                return self._clean_sentence(sentence)

        return None

    def _split_sentences(self, text: str) -> List[str]:
        """Split text into sentences"""
        # Simple sentence splitter
        sentences = re.split(r'(?<=[.!?])\s+(?=[A-Z])', text)
        return [s.strip() for s in sentences if s.strip()]

    def _clean_sentence(self, sentence: str) -> str:
        """Clean up sentence for use as snippet"""
        # Remove reference citations
        sentence = re.sub(r'\[\d+\]', '', sentence)
        sentence = re.sub(r'\([A-Za-z\s,]+\d{4}\)', '', sentence)
        # Remove excess whitespace
        sentence = ' '.join(sentence.split())
        return sentence


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Fix invalid evidence snippets")
    parser.add_argument('--file', help="Specific YAML file to check")
    parser.add_argument('--interactive', action='store_true', help="Interactive mode to review each snippet")
    parser.add_argument('--auto-fix', action='store_true', help="Automatically extract better snippets")
    args = parser.parse_args()

    fixer = SnippetFixer()
    kb_dir = Path('kb/communities')

    if args.file:
        yaml_files = [kb_dir / args.file]
    else:
        yaml_files = sorted(kb_dir.glob('*.yaml'))

    print("Invalid Snippet Analyzer")
    print("=" * 80)
    print()

    all_invalid = []

    for yaml_path in yaml_files:
        print(f"Checking {yaml_path.name}...")
        invalid = fixer.find_invalid_snippets(yaml_path)

        if invalid:
            print(f"  Found {len(invalid)} invalid snippets")
            all_invalid.extend(invalid)

    print()
    print("=" * 80)
    print(f"Total invalid snippets: {len(all_invalid)}")
    print()

    # Generate report
    with open('invalid_snippets_report.txt', 'w') as f:
        f.write("INVALID SNIPPETS REPORT\n")
        f.write("=" * 80 + "\n\n")
        f.write(f"Total: {len(all_invalid)}\n\n")

        # Group by file
        by_file = defaultdict(list)
        for item in all_invalid:
            by_file[item['file']].append(item)

        for file, items in sorted(by_file.items()):
            f.write(f"\n{file} ({len(items)} invalid)\n")
            f.write("-" * 80 + "\n\n")

            for item in items[:5]:  # Show first 5
                f.write(f"Organism: {item['organism']}\n")
                f.write(f"Reference: {item['reference']}\n")
                f.write(f"\nCurrent snippet (INVALID):\n")
                f.write(f"  \"{item['snippet'][:200]}...\"\n\n")

                # Suggest better snippet
                better = fixer.extract_best_snippet(
                    item['abstract'],
                    item['organism']
                )
                if better:
                    f.write(f"Suggested replacement:\n")
                    f.write(f"  \"{better[:200]}...\"\n\n")

                f.write("-" * 40 + "\n\n")

            if len(items) > 5:
                f.write(f"... and {len(items)-5} more\n\n")

    print("✓ Report written: invalid_snippets_report.txt")
    print()

    # Show top files needing fixes
    by_file_count = [(f, len(items)) for f, items in by_file.items()]
    by_file_count.sort(key=lambda x: x[1], reverse=True)

    print("Files with most invalid snippets:")
    for file, count in by_file_count[:10]:
        print(f"  {file}: {count}")

    print()
    print("Next steps:")
    print("  1. Review invalid_snippets_report.txt")
    print("  2. Use suggested replacements or extract better ones")
    print("  3. Manually update YAML files with valid snippets")


if __name__ == '__main__':
    main()
