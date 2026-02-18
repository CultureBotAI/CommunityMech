#!/usr/bin/env python3
"""
Literature Review & Update Tool for CommunityMech

Comprehensively reviews and validates literature evidence in community YAML files.

Features:
1. Validate evidence snippets against abstracts
2. Identify missing references
3. Download full PDFs (with scihub fallback)
4. Extract additional evidence from full papers
5. Generate literature quality report
6. Suggest evidence improvements

Usage:
    python scripts/review_literature.py                  # Review all communities
    python scripts/review_literature.py --community AMD  # Review specific community
    python scripts/review_literature.py --download-pdfs  # Download full PDFs
    python scripts/review_literature.py --update         # Auto-update valid evidence
"""

import yaml
import sys
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Set
from collections import defaultdict
from dataclasses import dataclass, field
import argparse

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from communitymech.literature_enhanced import EnhancedLiteratureFetcher

# Color codes
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    RESET = '\033[0m'


@dataclass
class EvidenceItem:
    """Represents a single evidence item from YAML"""
    file: str
    context: str  # taxonomy/interaction/environmental_factor
    organism: Optional[str]
    reference: str
    snippet: Optional[str]
    supports: str
    evidence_source: Optional[str]
    explanation: Optional[str]


@dataclass
class ValidationResult:
    """Results of validating an evidence item"""
    evidence: EvidenceItem
    abstract_fetched: bool = False
    abstract_text: Optional[str] = None
    snippet_valid: bool = False
    pdf_available: bool = False
    pdf_url: Optional[str] = None
    pdf_source: Optional[str] = None
    issues: List[str] = field(default_factory=list)
    suggestions: List[str] = field(default_factory=list)


class LiteratureReviewer:
    """Reviews and validates literature evidence in community YAMLs"""

    def __init__(
        self,
        kb_dir: Path,
        download_pdfs: bool = False,
        use_fallback: bool = True
    ):
        self.kb_dir = kb_dir
        self.download_pdfs = download_pdfs
        self.fetcher = EnhancedLiteratureFetcher(
            cache_dir=".literature_cache",
            pdf_cache_dir=".pdf_cache",
            email="noreply@communitymech.org",
            use_fallback_pdf=use_fallback
        )
        self.stats = defaultdict(int)
        self.evidence_items: List[EvidenceItem] = []
        self.validation_results: List[ValidationResult] = []

    def extract_evidence_from_yaml(self, yaml_path: Path) -> List[EvidenceItem]:
        """Extract all evidence items from a YAML file"""
        with open(yaml_path, 'r') as f:
            data = yaml.safe_load(f)

        evidence_items = []

        # Extract from taxonomy
        if 'taxonomy' in data:
            for taxon_entry in data['taxonomy']:
                organism = taxon_entry.get('taxon_term', {}).get('preferred_term', 'Unknown')

                if 'evidence' in taxon_entry:
                    for ev in taxon_entry['evidence']:
                        evidence_items.append(EvidenceItem(
                            file=yaml_path.name,
                            context='taxonomy',
                            organism=organism,
                            reference=ev.get('reference', ''),
                            snippet=ev.get('snippet'),
                            supports=ev.get('supports', ''),
                            evidence_source=ev.get('evidence_source'),
                            explanation=ev.get('explanation')
                        ))

        # Extract from ecological_interactions
        if 'ecological_interactions' in data:
            for interaction in data['ecological_interactions']:
                interaction_name = interaction.get('name', 'Unknown')

                if 'evidence' in interaction:
                    for ev in interaction['evidence']:
                        evidence_items.append(EvidenceItem(
                            file=yaml_path.name,
                            context='interaction',
                            organism=interaction_name,
                            reference=ev.get('reference', ''),
                            snippet=ev.get('snippet'),
                            supports=ev.get('supports', ''),
                            evidence_source=ev.get('evidence_source'),
                            explanation=ev.get('explanation')
                        ))

        # Extract from environmental_factors
        if 'environmental_factors' in data:
            for factor in data['environmental_factors']:
                factor_name = factor.get('name', 'Unknown')

                if 'evidence' in factor:
                    for ev in factor['evidence']:
                        evidence_items.append(EvidenceItem(
                            file=yaml_path.name,
                            context='environmental',
                            organism=factor_name,
                            reference=ev.get('reference', ''),
                            snippet=ev.get('snippet'),
                            supports=ev.get('supports', ''),
                            evidence_source=ev.get('evidence_source'),
                            explanation=ev.get('explanation')
                        ))

        return evidence_items

    def scan_all_communities(self) -> None:
        """Scan all community YAML files for evidence"""
        print(f"{Colors.CYAN}Scanning community YAML files...{Colors.RESET}\n")

        yaml_files = sorted(self.kb_dir.glob('*.yaml'))

        for yaml_path in yaml_files:
            evidence = self.extract_evidence_from_yaml(yaml_path)
            self.evidence_items.extend(evidence)

            if evidence:
                print(f"  {Colors.GREEN}✓{Colors.RESET} {yaml_path.name}: {len(evidence)} evidence items")

        print(f"\n{Colors.BOLD}Total evidence items: {len(self.evidence_items)}{Colors.RESET}\n")

    def validate_evidence_item(self, evidence: EvidenceItem) -> ValidationResult:
        """Validate a single evidence item"""
        result = ValidationResult(evidence=evidence)

        # Fetch paper
        paper = self.fetcher.fetch_paper(
            evidence.reference,
            download_pdf=self.download_pdfs
        )

        # Check if abstract was fetched
        if paper["abstract"]:
            result.abstract_fetched = True
            result.abstract_text = paper["abstract"]
            self.stats['abstracts_fetched'] += 1

            # Validate snippet against abstract
            if evidence.snippet:
                is_valid = self.fetcher.validate_evidence_snippet(
                    evidence.snippet,
                    paper["abstract"]
                )
                result.snippet_valid = is_valid

                if is_valid:
                    self.stats['snippets_valid'] += 1
                else:
                    result.issues.append("Snippet not found in abstract")
                    self.stats['snippets_invalid'] += 1
            else:
                result.issues.append("No snippet provided")
                self.stats['missing_snippets'] += 1

        else:
            result.issues.append("Could not fetch abstract")
            self.stats['abstracts_failed'] += 1

        # Check PDF availability
        if paper["pdf_url"]:
            result.pdf_available = True
            result.pdf_url = paper["pdf_url"]
            result.pdf_source = paper["source"]
            self.stats['pdfs_available'] += 1

        # Generate suggestions
        if not evidence.snippet and result.abstract_text:
            result.suggestions.append("Could extract snippet from abstract")

        if not evidence.explanation:
            result.suggestions.append("Missing explanation field")

        if not evidence.evidence_source:
            result.suggestions.append("Missing evidence_source field")

        return result

    def validate_all_evidence(self) -> None:
        """Validate all evidence items"""
        print(f"{Colors.CYAN}Validating evidence items...{Colors.RESET}\n")

        total = len(self.evidence_items)

        for i, evidence in enumerate(self.evidence_items, 1):
            if i % 10 == 0 or i == 1:
                print(f"  Progress: {i}/{total}")

            result = self.validate_evidence_item(evidence)
            self.validation_results.append(result)

        print(f"\n{Colors.GREEN}✓{Colors.RESET} Validation complete\n")

    def generate_report(self, output_path: Path) -> None:
        """Generate comprehensive literature quality report"""
        print(f"{Colors.CYAN}Generating literature quality report...{Colors.RESET}")

        with open(output_path, 'w') as f:
            f.write("=" * 80 + "\n")
            f.write("COMMUNITYMECH LITERATURE QUALITY REPORT\n")
            f.write("=" * 80 + "\n\n")

            # Summary statistics
            f.write("SUMMARY STATISTICS\n")
            f.write("-" * 80 + "\n\n")
            f.write(f"Total evidence items: {len(self.evidence_items)}\n")
            f.write(f"Abstracts fetched: {self.stats['abstracts_fetched']}\n")
            f.write(f"Abstracts failed: {self.stats['abstracts_failed']}\n")
            f.write(f"Snippets valid: {self.stats['snippets_valid']}\n")
            f.write(f"Snippets invalid: {self.stats['snippets_invalid']}\n")
            f.write(f"Missing snippets: {self.stats['missing_snippets']}\n")
            f.write(f"PDFs available: {self.stats['pdfs_available']}\n\n")

            # Calculate quality metrics
            if len(self.evidence_items) > 0:
                abstract_rate = (self.stats['abstracts_fetched'] / len(self.evidence_items)) * 100
                snippet_rate = (self.stats['snippets_valid'] / (self.stats['snippets_valid'] + self.stats['snippets_invalid'])) * 100 if (self.stats['snippets_valid'] + self.stats['snippets_invalid']) > 0 else 0
                pdf_rate = (self.stats['pdfs_available'] / len(self.evidence_items)) * 100

                f.write("QUALITY METRICS\n")
                f.write("-" * 80 + "\n\n")
                f.write(f"Abstract fetch rate: {abstract_rate:.1f}%\n")
                f.write(f"Snippet validation rate: {snippet_rate:.1f}%\n")
                f.write(f"PDF availability rate: {pdf_rate:.1f}%\n\n")

            # Issues by file
            f.write("\n" + "=" * 80 + "\n")
            f.write("ISSUES BY FILE\n")
            f.write("=" * 80 + "\n\n")

            issues_by_file = defaultdict(list)
            for result in self.validation_results:
                if result.issues:
                    issues_by_file[result.evidence.file].append(result)

            for file, results in sorted(issues_by_file.items()):
                f.write(f"\n{file}\n")
                f.write("-" * 80 + "\n")

                for result in results:
                    f.write(f"\nReference: {result.evidence.reference}\n")
                    f.write(f"Context: {result.evidence.context}\n")
                    if result.evidence.organism:
                        f.write(f"Organism/Factor: {result.evidence.organism}\n")

                    f.write(f"Issues:\n")
                    for issue in result.issues:
                        f.write(f"  - {issue}\n")

                    if result.suggestions:
                        f.write(f"Suggestions:\n")
                        for suggestion in result.suggestions:
                            f.write(f"  - {suggestion}\n")

                    if result.snippet_valid:
                        f.write(f"  ✓ Snippet valid\n")

                    if result.pdf_available:
                        f.write(f"  ✓ PDF available: {result.pdf_url}\n")

            # Valid evidence (for reference)
            f.write("\n\n" + "=" * 80 + "\n")
            f.write("VALID EVIDENCE (No Issues)\n")
            f.write("=" * 80 + "\n\n")

            valid_by_file = defaultdict(list)
            for result in self.validation_results:
                if not result.issues:
                    valid_by_file[result.evidence.file].append(result)

            for file, results in sorted(valid_by_file.items()):
                f.write(f"\n{file}: {len(results)} valid evidence items\n")

            # References with PDFs available
            f.write("\n\n" + "=" * 80 + "\n")
            f.write("REFERENCES WITH FULL PDF ACCESS\n")
            f.write("=" * 80 + "\n\n")

            pdf_refs = {}
            for result in self.validation_results:
                if result.pdf_available:
                    ref = result.evidence.reference
                    if ref not in pdf_refs:
                        pdf_refs[ref] = {
                            'url': result.pdf_url,
                            'source': result.pdf_source,
                            'files': []
                        }
                    pdf_refs[ref]['files'].append(result.evidence.file)

            for ref, info in sorted(pdf_refs.items()):
                f.write(f"\n{ref}\n")
                f.write(f"  URL: {info['url']}\n")
                f.write(f"  Source: {info['source']}\n")
                f.write(f"  Used in: {', '.join(set(info['files']))}\n")

        print(f"{Colors.GREEN}✓{Colors.RESET} Report written: {output_path}\n")

    def generate_priority_update_list(self, output_path: Path) -> None:
        """Generate prioritized list of evidence needing updates"""
        print(f"{Colors.CYAN}Generating priority update list...{Colors.RESET}")

        # Categorize issues by priority
        critical = []  # Invalid snippets, missing abstracts
        high = []      # Missing snippets
        medium = []    # Missing explanations/evidence_source

        for result in self.validation_results:
            if not result.abstract_fetched:
                critical.append(result)
            elif result.evidence.snippet and not result.snippet_valid:
                critical.append(result)
            elif not result.evidence.snippet and result.abstract_text:
                high.append(result)
            elif not result.evidence.explanation or not result.evidence.evidence_source:
                medium.append(result)

        with open(output_path, 'w') as f:
            f.write("PRIORITY LITERATURE UPDATES\n")
            f.write("=" * 80 + "\n\n")

            f.write(f"CRITICAL ({len(critical)} items): Invalid/missing evidence\n")
            f.write("-" * 80 + "\n\n")
            for result in critical[:20]:  # Top 20
                f.write(f"File: {result.evidence.file}\n")
                f.write(f"Reference: {result.evidence.reference}\n")
                f.write(f"Context: {result.evidence.context} - {result.evidence.organism}\n")
                f.write(f"Issues: {', '.join(result.issues)}\n\n")

            f.write(f"\nHIGH ({len(high)} items): Missing snippets (abstract available)\n")
            f.write("-" * 80 + "\n\n")
            for result in high[:20]:  # Top 20
                f.write(f"File: {result.evidence.file}\n")
                f.write(f"Reference: {result.evidence.reference}\n")
                f.write(f"Context: {result.evidence.context} - {result.evidence.organism}\n")
                f.write(f"Abstract available: {len(result.abstract_text)} chars\n\n")

            f.write(f"\nMEDIUM ({len(medium)} items): Missing metadata\n")
            f.write("-" * 80 + "\n\n")
            for result in medium[:20]:  # Top 20
                f.write(f"File: {result.evidence.file}\n")
                f.write(f"Reference: {result.evidence.reference}\n")
                f.write(f"Missing: ")
                if not result.evidence.explanation:
                    f.write("explanation ")
                if not result.evidence.evidence_source:
                    f.write("evidence_source")
                f.write("\n\n")

        print(f"{Colors.GREEN}✓{Colors.RESET} Priority list written: {output_path}\n")

    def print_summary(self) -> None:
        """Print summary statistics"""
        print(f"{Colors.BOLD}{Colors.CYAN}LITERATURE REVIEW SUMMARY{Colors.RESET}")
        print("=" * 80)
        print(f"Total evidence items: {len(self.evidence_items)}")
        print(f"Abstracts fetched: {self.stats['abstracts_fetched']} ({self.stats['abstracts_fetched']/len(self.evidence_items)*100:.1f}%)")
        print(f"Abstracts failed: {self.stats['abstracts_failed']} ({self.stats['abstracts_failed']/len(self.evidence_items)*100:.1f}%)")
        print()
        print(f"Snippets valid: {self.stats['snippets_valid']}")
        print(f"Snippets invalid: {self.stats['snippets_invalid']}")
        print(f"Missing snippets: {self.stats['missing_snippets']}")
        print()
        print(f"PDFs available: {self.stats['pdfs_available']} ({self.stats['pdfs_available']/len(self.evidence_items)*100:.1f}%)")
        print("=" * 80)


def main():
    parser = argparse.ArgumentParser(description="Review and validate literature evidence in CommunityMech")
    parser.add_argument('--community', help="Review specific community file")
    parser.add_argument('--download-pdfs', action='store_true', help="Download full PDFs")
    parser.add_argument('--no-fallback', action='store_true', help="Disable scihub fallback")
    parser.add_argument('--output', default='literature_review_report.txt', help="Output report file")

    args = parser.parse_args()

    # Paths
    kb_dir = Path('kb/communities')

    # Initialize reviewer
    reviewer = LiteratureReviewer(
        kb_dir=kb_dir,
        download_pdfs=args.download_pdfs,
        use_fallback=not args.no_fallback
    )

    print(f"{Colors.BOLD}{Colors.CYAN}CommunityMech Literature Review Tool{Colors.RESET}")
    print(f"{Colors.CYAN}Download PDFs: {args.download_pdfs}{Colors.RESET}")
    print(f"{Colors.CYAN}Use fallback (scihub): {not args.no_fallback}{Colors.RESET}\n")

    # Scan communities
    reviewer.scan_all_communities()

    # Validate evidence
    reviewer.validate_all_evidence()

    # Generate reports
    reviewer.generate_report(Path(args.output))
    reviewer.generate_priority_update_list(Path('priority_literature_updates.txt'))

    # Print summary
    print()
    reviewer.print_summary()

    print(f"\n{Colors.GREEN}{Colors.BOLD}✓ Literature review complete!{Colors.RESET}")
    print(f"\nReports generated:")
    print(f"  - {args.output}")
    print(f"  - priority_literature_updates.txt")


if __name__ == '__main__':
    main()
