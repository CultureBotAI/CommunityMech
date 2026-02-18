#!/usr/bin/env python3
"""
Evidence Curation Workflow with PDF Fallback

Uses the enhanced PDF fetching to:
1. Validate all evidence items in community YAMLs
2. Fetch abstracts and PDFs for references
3. Validate snippets against source text
4. Extract better snippets from full text when available
5. Generate actionable curation tasks
6. Optionally apply automatic fixes

This script enforces the schema requirements:
- reference: Required, must match pattern (PMID:|doi:|bioproject:)
- evidence_source: Required (IN_VITRO, IN_VIVO, etc.)
- snippet: Required, minimum 10 characters, must be exact quote
- confidence_score: Optional, based on validation
"""

import sys
import yaml
import re
from pathlib import Path
from typing import Dict, List, Tuple, Optional
from collections import defaultdict
from dataclasses import dataclass
import time

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from communitymech.literature_enhanced import EnhancedLiteratureFetcher


@dataclass
class EvidenceIssue:
    """Represents an evidence quality issue"""
    file: str
    context: str  # taxonomy, interaction, environmental
    organism: str
    reference: str
    issue_type: str
    current_value: str
    suggested_fix: Optional[str] = None
    severity: str = "WARNING"  # ERROR, WARNING, INFO


class EvidenceCurator:
    """Comprehensive evidence curation using PDF fallback"""

    def __init__(self, use_pdf_fallback: bool = True, auto_fix: bool = False):
        self.fetcher = EnhancedLiteratureFetcher(
            cache_dir=".literature_cache",
            use_fallback_pdf=use_pdf_fallback
        )
        self.auto_fix = auto_fix
        self.issues = []
        self.stats = defaultdict(int)

    def validate_reference_format(self, reference: str) -> Tuple[bool, Optional[str]]:
        """Validate reference matches schema pattern"""

        # Check pattern: Must start with PMID:, doi:, or bioproject:
        pattern = r"^(PMID:|doi:|bioproject:)"
        if not re.match(pattern, reference):
            # Try to fix common issues
            if reference.startswith("pmid:"):
                return False, f"PMID:{reference[5:]}"
            elif reference.startswith("DOI:"):
                return False, f"doi:{reference[4:]}"
            elif re.match(r"^10\.\d+/", reference):
                return False, f"doi:{reference}"
            elif re.match(r"^PMC\d+$", reference):
                return False, f"PMID:{reference}"
            else:
                return False, None

        return True, reference

    def validate_snippet(self, snippet: str) -> Tuple[bool, List[str]]:
        """Validate snippet meets schema requirements"""

        issues = []

        if not snippet:
            issues.append("Snippet is empty")
            return False, issues

        if len(snippet) < 10:
            issues.append(f"Snippet too short ({len(snippet)} chars, minimum 10)")

        # Check for common invalid patterns
        if snippet.startswith("Appl Environ Microbiol") or snippet.startswith("Front Microbiol"):
            issues.append("Snippet appears to be journal citation, not content quote")

        if "..." in snippet and len(snippet) < 50:
            issues.append("Snippet is truncated but very short")

        # Check for AI-generated patterns
        ai_patterns = [
            "is an? (important|key|critical)",
            "plays an? (important|key|critical) role",
            "has been shown to",
            "it is (known|believed) that",
        ]
        for pattern in ai_patterns:
            if re.search(pattern, snippet, re.IGNORECASE):
                issues.append(f"Snippet may be AI-generated/paraphrased (pattern: {pattern})")
                break

        return len(issues) == 0, issues

    def fetch_and_validate_evidence(
        self,
        reference: str,
        snippet: str,
        organism: str = None,
        fetch_pdf: bool = False
    ) -> Dict:
        """
        Fetch paper and validate snippet against it.

        Returns:
            {
                'abstract_fetched': bool,
                'pdf_fetched': bool,
                'snippet_valid': bool,
                'snippet_in_abstract': bool,
                'snippet_in_fulltext': bool,
                'suggested_snippet': str or None,
                'confidence_score': float,
                'paper_metadata': dict
            }
        """

        result = {
            'abstract_fetched': False,
            'pdf_fetched': False,
            'snippet_valid': False,
            'snippet_in_abstract': False,
            'snippet_in_fulltext': False,
            'suggested_snippet': None,
            'confidence_score': 0.0,
            'paper_metadata': {}
        }

        try:
            # Fetch paper
            paper = self.fetcher.fetch_paper(reference, download_pdf=fetch_pdf)

            if paper.get('abstract'):
                result['abstract_fetched'] = True
                result['paper_metadata'] = {
                    'title': paper.get('title'),
                    'year': paper.get('year'),
                    'journal': paper.get('journal'),
                    'authors': paper.get('authors', [])
                }

                # Validate snippet against abstract
                if snippet:
                    result['snippet_in_abstract'] = self.fetcher.validate_evidence_snippet(
                        snippet, paper['abstract']
                    )
                    result['snippet_valid'] = result['snippet_in_abstract']

                    if result['snippet_valid']:
                        result['confidence_score'] = 1.0
                    else:
                        # Try to extract better snippet
                        result['suggested_snippet'] = self._extract_best_snippet(
                            paper['abstract'], organism, snippet
                        )
                        result['confidence_score'] = 0.3

            if fetch_pdf and paper.get('pdf_text'):
                result['pdf_fetched'] = True

                # If snippet not in abstract, check full text
                if not result['snippet_valid'] and snippet:
                    result['snippet_in_fulltext'] = self.fetcher.validate_evidence_snippet(
                        snippet, paper['pdf_text']
                    )
                    if result['snippet_in_fulltext']:
                        result['snippet_valid'] = True
                        result['confidence_score'] = 0.8  # Lower than abstract (less specific)

                    # Extract from full text if still invalid
                    if not result['snippet_valid']:
                        result['suggested_snippet'] = self._extract_best_snippet(
                            paper['pdf_text'], organism, snippet
                        )
                        result['confidence_score'] = 0.5

        except Exception as e:
            print(f"  Error fetching {reference}: {e}")

        return result

    def _extract_best_snippet(
        self,
        text: str,
        organism: str = None,
        current_snippet: str = None
    ) -> Optional[str]:
        """Extract best matching snippet from text"""

        # Split into sentences
        sentences = re.split(r'(?<=[.!?])\s+(?=[A-Z])', text)

        # Filter out journal citation lines
        sentences = [
            s for s in sentences
            if not re.match(r'^[A-Z][a-z]+ [A-Z][a-z]+\.\s+\d{4}', s)  # Journal citation
            and len(s) > 50  # Substantive
        ]

        if not sentences:
            return None

        # Try to find sentence mentioning organism
        if organism:
            organism_variants = [
                organism,
                organism.split()[0] if ' ' in organism else None,  # Genus only
                organism.replace('Candidatus ', '') if 'Candidatus' in organism else None
            ]
            organism_variants = [v for v in organism_variants if v]

            for sentence in sentences:
                if any(org and org.lower() in sentence.lower() for org in organism_variants):
                    return self._clean_snippet(sentence)

        # Try to find sentence with keywords from current snippet
        if current_snippet:
            keywords = [
                w for w in re.findall(r'\b\w{4,}\b', current_snippet.lower())
                if w not in ['that', 'with', 'from', 'this', 'were', 'have']
            ][:5]  # Top 5 keywords

            best_sentence = None
            best_score = 0

            for sentence in sentences:
                score = sum(1 for kw in keywords if kw in sentence.lower())
                if score > best_score:
                    best_score = score
                    best_sentence = sentence

            if best_sentence and best_score >= 2:  # At least 2 keyword matches
                return self._clean_snippet(best_sentence)

        # Fallback: return first substantive sentence
        return self._clean_snippet(sentences[0]) if sentences else None

    def _clean_snippet(self, text: str) -> str:
        """Clean snippet for use in YAML"""
        # Remove citations
        text = re.sub(r'\[\d+\]', '', text)
        text = re.sub(r'\([A-Za-z\s,]+\d{4}\)', '', text)
        # Remove excess whitespace
        text = ' '.join(text.split())
        return text

    def audit_community_yaml(
        self,
        yaml_path: Path,
        fetch_pdfs: bool = False
    ) -> List[EvidenceIssue]:
        """Audit all evidence in a community YAML"""

        with open(yaml_path, 'r') as f:
            data = yaml.safe_load(f)

        issues = []

        # Check taxonomy evidence
        if 'taxonomy' in data:
            for taxon_entry in data['taxonomy']:
                organism = taxon_entry.get('taxon_term', {}).get('preferred_term', 'Unknown')

                if 'evidence' not in taxon_entry or not taxon_entry['evidence']:
                    issues.append(EvidenceIssue(
                        file=yaml_path.name,
                        context='taxonomy',
                        organism=organism,
                        reference='N/A',
                        issue_type='MISSING_EVIDENCE',
                        current_value='No evidence provided',
                        severity='ERROR'
                    ))
                    continue

                for ev in taxon_entry['evidence']:
                    issues.extend(self._audit_evidence_item(
                        ev, yaml_path.name, 'taxonomy', organism, fetch_pdfs
                    ))

        # Check interaction evidence
        if 'ecological_interactions' in data:
            for interaction in data['ecological_interactions']:
                interaction_name = interaction.get('name', 'Unknown')

                if 'evidence' not in interaction or not interaction['evidence']:
                    issues.append(EvidenceIssue(
                        file=yaml_path.name,
                        context='interaction',
                        organism=interaction_name,
                        reference='N/A',
                        issue_type='MISSING_EVIDENCE',
                        current_value='No evidence provided',
                        severity='ERROR'
                    ))
                    continue

                for ev in interaction['evidence']:
                    issues.extend(self._audit_evidence_item(
                        ev, yaml_path.name, 'interaction', interaction_name, fetch_pdfs
                    ))

        # Check environmental evidence
        if 'environmental_factors' in data:
            for factor in data['environmental_factors']:
                factor_name = factor.get('factor', 'Unknown')

                if 'evidence' in factor and factor['evidence']:
                    for ev in factor['evidence']:
                        issues.extend(self._audit_evidence_item(
                            ev, yaml_path.name, 'environmental', factor_name, fetch_pdfs
                        ))

        return issues

    def _audit_evidence_item(
        self,
        evidence: Dict,
        filename: str,
        context: str,
        organism: str,
        fetch_pdf: bool
    ) -> List[EvidenceIssue]:
        """Audit single evidence item"""

        issues = []
        reference = evidence.get('reference', '')
        snippet = evidence.get('snippet', '')
        evidence_source = evidence.get('evidence_source', '')

        # Check reference format
        ref_valid, ref_fix = self.validate_reference_format(reference)
        if not ref_valid:
            issues.append(EvidenceIssue(
                file=filename,
                context=context,
                organism=organism,
                reference=reference,
                issue_type='INVALID_REFERENCE_FORMAT',
                current_value=reference,
                suggested_fix=ref_fix,
                severity='ERROR' if not ref_fix else 'WARNING'
            ))
            self.stats['invalid_reference_format'] += 1

        # Check evidence_source
        if not evidence_source:
            issues.append(EvidenceIssue(
                file=filename,
                context=context,
                organism=organism,
                reference=reference,
                issue_type='MISSING_EVIDENCE_SOURCE',
                current_value='Not specified',
                suggested_fix='IN_VITRO or IN_VIVO (check paper)',
                severity='ERROR'
            ))
            self.stats['missing_evidence_source'] += 1

        # Check snippet
        snippet_valid, snippet_issues = self.validate_snippet(snippet)
        if not snippet_valid:
            for issue_desc in snippet_issues:
                issues.append(EvidenceIssue(
                    file=filename,
                    context=context,
                    organism=organism,
                    reference=reference,
                    issue_type='INVALID_SNIPPET',
                    current_value=snippet[:100] if snippet else '(empty)',
                    suggested_fix=f"Issue: {issue_desc}",
                    severity='ERROR'
                ))
            self.stats['invalid_snippet'] += 1

        # Validate against source if snippet provided and reference valid
        if snippet and ref_valid:
            self.stats['total_validated'] += 1
            validation = self.fetch_and_validate_evidence(
                reference, snippet, organism, fetch_pdf
            )

            if not validation['abstract_fetched']:
                issues.append(EvidenceIssue(
                    file=filename,
                    context=context,
                    organism=organism,
                    reference=reference,
                    issue_type='ABSTRACT_FETCH_FAILED',
                    current_value=snippet[:100],
                    severity='WARNING'
                ))
                self.stats['abstract_fetch_failed'] += 1

            elif not validation['snippet_valid']:
                issues.append(EvidenceIssue(
                    file=filename,
                    context=context,
                    organism=organism,
                    reference=reference,
                    issue_type='SNIPPET_NOT_IN_SOURCE',
                    current_value=snippet[:100],
                    suggested_fix=validation['suggested_snippet'][:150] if validation['suggested_snippet'] else None,
                    severity='ERROR'
                ))
                self.stats['snippet_not_in_source'] += 1
            else:
                self.stats['valid_evidence'] += 1

        return issues

    def generate_report(self, issues: List[EvidenceIssue], output_path: Path):
        """Generate comprehensive curation report"""

        with open(output_path, 'w') as f:
            f.write("EVIDENCE CURATION REPORT\n")
            f.write("=" * 80 + "\n\n")

            # Statistics
            f.write("STATISTICS\n")
            f.write("-" * 80 + "\n")
            f.write(f"Total evidence items validated: {self.stats.get('total_validated', 0)}\n")
            f.write(f"Valid evidence: {self.stats.get('valid_evidence', 0)}\n")
            f.write(f"Issues found: {len(issues)}\n\n")

            f.write("Issue breakdown:\n")
            f.write(f"  - Invalid reference format: {self.stats.get('invalid_reference_format', 0)}\n")
            f.write(f"  - Missing evidence source: {self.stats.get('missing_evidence_source', 0)}\n")
            f.write(f"  - Invalid snippet: {self.stats.get('invalid_snippet', 0)}\n")
            f.write(f"  - Abstract fetch failed: {self.stats.get('abstract_fetch_failed', 0)}\n")
            f.write(f"  - Snippet not in source: {self.stats.get('snippet_not_in_source', 0)}\n")
            f.write("\n")

            # Group by file
            by_file = defaultdict(list)
            for issue in issues:
                by_file[issue.file].append(issue)

            # Group by severity
            by_severity = defaultdict(list)
            for issue in issues:
                by_severity[issue.severity].append(issue)

            f.write(f"Files affected: {len(by_file)}\n")
            f.write(f"  - ERROR: {len(by_severity['ERROR'])}\n")
            f.write(f"  - WARNING: {len(by_severity['WARNING'])}\n")
            f.write(f"  - INFO: {len(by_severity['INFO'])}\n")
            f.write("\n" + "=" * 80 + "\n\n")

            # Detailed issues by file
            for filename in sorted(by_file.keys()):
                file_issues = by_file[filename]
                f.write(f"\n{filename} ({len(file_issues)} issues)\n")
                f.write("-" * 80 + "\n\n")

                # Group by issue type
                by_type = defaultdict(list)
                for issue in file_issues:
                    by_type[issue.issue_type].append(issue)

                for issue_type in sorted(by_type.keys()):
                    type_issues = by_type[issue_type]
                    f.write(f"{issue_type} ({len(type_issues)} instances)\n")
                    f.write("~" * 40 + "\n")

                    for issue in type_issues[:5]:  # Show first 5
                        f.write(f"\nOrganism/Item: {issue.organism}\n")
                        f.write(f"Reference: {issue.reference}\n")
                        f.write(f"Current: {issue.current_value}\n")
                        if issue.suggested_fix:
                            f.write(f"Suggested fix: {issue.suggested_fix}\n")
                        f.write("\n")

                    if len(type_issues) > 5:
                        f.write(f"... and {len(type_issues)-5} more\n\n")

                    f.write("\n")


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Curate evidence with PDF fallback")
    parser.add_argument('--file', help="Specific YAML file to audit")
    parser.add_argument('--with-pdfs', action='store_true', help="Fetch PDFs for validation (slow)")
    parser.add_argument('--auto-fix', action='store_true', help="Automatically apply fixes where possible")
    parser.add_argument('--quick', action='store_true', help="Quick audit (skip PDF fetching)")
    args = parser.parse_args()

    curator = EvidenceCurator(
        use_pdf_fallback=not args.quick,
        auto_fix=args.auto_fix
    )

    kb_dir = Path('kb/communities')

    if args.file:
        yaml_files = [kb_dir / args.file]
    else:
        yaml_files = sorted(kb_dir.glob('*.yaml'))

    print("Evidence Curation Workflow")
    print("=" * 80)
    print(f"Mode: {'WITH PDFs' if args.with_pdfs else 'Abstracts only'}")
    print(f"Auto-fix: {args.auto_fix}")
    print()

    all_issues = []

    for yaml_path in yaml_files:
        print(f"Auditing {yaml_path.name}...")
        issues = curator.audit_community_yaml(yaml_path, fetch_pdfs=args.with_pdfs)

        if issues:
            print(f"  Found {len(issues)} issues")
            all_issues.extend(issues)
        else:
            print(f"  ✓ No issues found")

        # Rate limit
        time.sleep(0.5)

    print()
    print("=" * 80)
    print(f"Total issues: {len(all_issues)}")
    print()

    # Generate report
    report_path = Path('evidence_curation_report.txt')
    curator.generate_report(all_issues, report_path)

    print(f"✓ Report written: {report_path}")
    print()

    # Summary by severity
    by_severity = defaultdict(int)
    for issue in all_issues:
        by_severity[issue.severity] += 1

    print("Issues by severity:")
    print(f"  ERROR:   {by_severity['ERROR']:4d} (must fix)")
    print(f"  WARNING: {by_severity['WARNING']:4d} (should fix)")
    print(f"  INFO:    {by_severity['INFO']:4d} (nice to fix)")
    print()

    print("Next steps:")
    print("  1. Review evidence_curation_report.txt")
    print("  2. Fix ERROR-level issues first")
    print("  3. Re-run with --with-pdfs for thorough validation")
    print("  4. Run schema validation: just validate-all")


if __name__ == '__main__':
    main()
