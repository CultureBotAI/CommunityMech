#!/usr/bin/env python3
"""
Add Evidence Source to YAML Files

Automatically adds evidence_source field to evidence items based on:
1. Paper keywords (field study, culture, metagenome, etc.)
2. Community origin (natural=IN_VIVO, engineered=IN_VITRO)
3. Manual review mode for uncertain cases

Usage:
  # Automatic mode (uses heuristics)
  python scripts/add_evidence_source.py --auto

  # Interactive mode (ask for each item)
  python scripts/add_evidence_source.py --interactive

  # Single file
  python scripts/add_evidence_source.py --file FILE.yaml --auto
"""

import sys
import yaml
from pathlib import Path
from typing import Dict, List, Optional
import re

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from communitymech.literature_enhanced import EnhancedLiteratureFetcher


class EvidenceSourceAdder:
    """Add evidence_source to evidence items"""

    def __init__(self):
        self.fetcher = EnhancedLiteratureFetcher(
            cache_dir=".literature_cache",
            use_fallback_pdf=False
        )
        self.stats = {
            'total_evidence': 0,
            'already_has_source': 0,
            'auto_added': 0,
            'manual_added': 0,
            'skipped': 0
        }

        # Keywords for automatic classification
        self.in_vitro_keywords = [
            'culture', 'batch', 'bioreactor', 'enrichment', 'laboratory',
            'pure culture', 'co-culture', 'synthetic', 'engineered',
            'flask', 'medium', 'cultivation', 'isolated', 'strain'
        ]

        self.in_vivo_keywords = [
            'field', 'environmental', 'sample', 'site', 'natural',
            'sediment', 'soil', 'water', 'community', 'microbiome',
            '16s rrna', 'metagenome', 'metatranscriptome', 'amplicon'
        ]

        self.computational_keywords = [
            'genome', 'model', 'simulation', 'bioinformatic', 'in silico',
            'reconstruction', 'prediction', 'annotation', 'assembly',
            'metabolic network', 'flux balance'
        ]

        self.review_keywords = [
            'review', 'meta-analysis', 'survey'
        ]

    def guess_evidence_source(
        self,
        snippet: str,
        abstract: str = None,
        title: str = None,
        community_origin: str = None
    ) -> Optional[str]:
        """Guess evidence source using heuristics"""

        # Combine text for keyword matching
        text = ' '.join(filter(None, [snippet, abstract, title])).lower()

        # Check for review first (highest specificity)
        if any(kw in text for kw in self.review_keywords):
            return 'REVIEW'

        # Check computational
        computational_count = sum(1 for kw in self.computational_keywords if kw in text)
        if computational_count >= 2:
            return 'COMPUTATIONAL'

        # Check in vitro
        in_vitro_count = sum(1 for kw in self.in_vitro_keywords if kw in text)

        # Check in vivo
        in_vivo_count = sum(1 for kw in self.in_vivo_keywords if kw in text)

        # Use community origin as tiebreaker
        if in_vitro_count > in_vivo_count:
            return 'IN_VITRO'
        elif in_vivo_count > in_vitro_count:
            return 'IN_VIVO'
        elif community_origin == 'ENGINEERED' or community_origin == 'SYNTHETIC':
            return 'IN_VITRO'
        elif community_origin == 'NATURAL':
            return 'IN_VIVO'

        return None  # Can't determine

    def process_yaml(
        self,
        yaml_path: Path,
        auto_mode: bool = False,
        interactive: bool = False
    ) -> Dict:
        """Process a YAML file and add evidence_source"""

        with open(yaml_path, 'r') as f:
            data = yaml.safe_load(f)

        changes = []
        community_origin = data.get('origin')

        # Process taxonomy
        if 'taxonomy' in data:
            for taxon_idx, taxon_entry in enumerate(data['taxonomy']):
                if 'evidence' not in taxon_entry:
                    continue

                organism = taxon_entry.get('taxon_term', {}).get('preferred_term', 'Unknown')

                for ev_idx, ev in enumerate(taxon_entry['evidence']):
                    if 'evidence_source' in ev and ev['evidence_source']:
                        self.stats['already_has_source'] += 1
                        continue

                    self.stats['total_evidence'] += 1

                    # Get snippet and reference
                    snippet = ev.get('snippet', '')
                    reference = ev.get('reference', '')

                    # Try to fetch abstract for better classification
                    abstract = None
                    title = None
                    try:
                        paper = self.fetcher.fetch_paper(reference, download_pdf=False)
                        abstract = paper.get('abstract')
                        title = paper.get('title')
                    except:
                        pass

                    # Guess evidence source
                    guessed_source = self.guess_evidence_source(
                        snippet, abstract, title, community_origin
                    )

                    if auto_mode and guessed_source:
                        ev['evidence_source'] = guessed_source
                        changes.append({
                            'context': 'taxonomy',
                            'organism': organism,
                            'reference': reference,
                            'source': guessed_source,
                            'confidence': 'auto'
                        })
                        self.stats['auto_added'] += 1

                    elif interactive:
                        # Show evidence and ask user
                        print(f"\nOrganism: {organism}")
                        print(f"Reference: {reference}")
                        print(f"Snippet: {snippet[:150]}...")
                        if guessed_source:
                            print(f"Suggested: {guessed_source}")

                        choice = input("Source [I=IN_VITRO, V=IN_VIVO, C=COMPUTATIONAL, R=REVIEW, S=skip]: ").upper()

                        source_map = {
                            'I': 'IN_VITRO',
                            'V': 'IN_VIVO',
                            'C': 'COMPUTATIONAL',
                            'R': 'REVIEW'
                        }

                        if choice in source_map:
                            ev['evidence_source'] = source_map[choice]
                            changes.append({
                                'context': 'taxonomy',
                                'organism': organism,
                                'reference': reference,
                                'source': source_map[choice],
                                'confidence': 'manual'
                            })
                            self.stats['manual_added'] += 1
                        else:
                            self.stats['skipped'] += 1

        # Process interactions (similar logic)
        if 'ecological_interactions' in data:
            for int_idx, interaction in enumerate(data['ecological_interactions']):
                if 'evidence' not in interaction:
                    continue

                int_name = interaction.get('name', 'Unknown')

                for ev_idx, ev in enumerate(interaction['evidence']):
                    if 'evidence_source' in ev and ev['evidence_source']:
                        self.stats['already_has_source'] += 1
                        continue

                    self.stats['total_evidence'] += 1

                    snippet = ev.get('snippet', '')
                    reference = ev.get('reference', '')

                    abstract = None
                    title = None
                    try:
                        paper = self.fetcher.fetch_paper(reference, download_pdf=False)
                        abstract = paper.get('abstract')
                        title = paper.get('title')
                    except:
                        pass

                    guessed_source = self.guess_evidence_source(
                        snippet, abstract, title, community_origin
                    )

                    if auto_mode and guessed_source:
                        ev['evidence_source'] = guessed_source
                        changes.append({
                            'context': 'interaction',
                            'organism': int_name,
                            'reference': reference,
                            'source': guessed_source,
                            'confidence': 'auto'
                        })
                        self.stats['auto_added'] += 1

                    elif interactive:
                        print(f"\nInteraction: {int_name}")
                        print(f"Reference: {reference}")
                        print(f"Snippet: {snippet[:150]}...")
                        if guessed_source:
                            print(f"Suggested: {guessed_source}")

                        choice = input("Source [I/V/C/R/S]: ").upper()

                        source_map = {
                            'I': 'IN_VITRO',
                            'V': 'IN_VIVO',
                            'C': 'COMPUTATIONAL',
                            'R': 'REVIEW'
                        }

                        if choice in source_map:
                            ev['evidence_source'] = source_map[choice]
                            changes.append({
                                'context': 'interaction',
                                'organism': int_name,
                                'reference': reference,
                                'source': source_map[choice],
                                'confidence': 'manual'
                            })
                            self.stats['manual_added'] += 1
                        else:
                            self.stats['skipped'] += 1

        # Write back if changes made
        if changes:
            # Backup
            backup_path = yaml_path.with_suffix('.yaml.bak_source')
            yaml_path.rename(backup_path)

            # Write updated
            with open(yaml_path, 'w') as f:
                yaml.dump(data, f,
                         default_flow_style=False,
                         sort_keys=False,
                         allow_unicode=True,
                         width=120,
                         indent=2)

        return {
            'file': yaml_path.name,
            'changes': changes,
            'count': len(changes)
        }


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Add evidence_source to YAML files")
    parser.add_argument('--file', help="Specific YAML file to process")
    parser.add_argument('--auto', action='store_true', help="Auto-add using heuristics")
    parser.add_argument('--interactive', action='store_true', help="Interactive mode")
    parser.add_argument('--dry-run', action='store_true', help="Don't write changes")
    args = parser.parse_args()

    if not args.auto and not args.interactive:
        print("Error: Must specify --auto or --interactive mode")
        sys.exit(1)

    adder = EvidenceSourceAdder()
    kb_dir = Path('kb/communities')

    if args.file:
        yaml_files = [kb_dir / args.file]
    else:
        yaml_files = sorted(kb_dir.glob('*.yaml'))

    print("Evidence Source Adder")
    print("=" * 80)
    print(f"Mode: {'AUTO' if args.auto else 'INTERACTIVE'}")
    print()

    results = []

    for yaml_path in yaml_files:
        print(f"Processing {yaml_path.name}...")

        if not args.dry_run:
            result = adder.process_yaml(yaml_path, auto_mode=args.auto, interactive=args.interactive)

            if result['count'] > 0:
                print(f"  Added {result['count']} evidence_source fields")
                results.append(result)
        else:
            print("  (dry run - no changes)")

    print()
    print("=" * 80)
    print("Statistics:")
    print(f"  Total evidence items: {adder.stats['total_evidence']}")
    print(f"  Already had source: {adder.stats['already_has_source']}")
    print(f"  Auto-added: {adder.stats['auto_added']}")
    print(f"  Manual-added: {adder.stats['manual_added']}")
    print(f"  Skipped: {adder.stats['skipped']}")
    print()

    if results:
        print(f"Modified {len(results)} files")
        print("Backups saved as .yaml.bak_source")


if __name__ == '__main__':
    main()
