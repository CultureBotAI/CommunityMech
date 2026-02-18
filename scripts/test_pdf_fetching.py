#!/usr/bin/env python3
"""
Test PDF Fetching Core Capability

Tests all 6 tiers of the PDF cascade:
1. Publisher direct
2. PubMed Central
3. Unpaywall API
4. Semantic Scholar
5. Scihub fallback mirrors
6. Web search

Validates configuration, success rates, and fallback behavior.
"""

import sys
import yaml
from pathlib import Path
from typing import Dict, List, Tuple, Optional
from collections import defaultdict
import time

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from communitymech.literature_enhanced import EnhancedLiteratureFetcher


class PDFFetchingTester:
    """Comprehensive PDF fetching test suite"""

    def __init__(self):
        # Test with fallback enabled
        self.fetcher_with_fallback = EnhancedLiteratureFetcher(
            cache_dir=".literature_cache",
            use_fallback_pdf=True
        )

        # Test without fallback
        self.fetcher_no_fallback = EnhancedLiteratureFetcher(
            cache_dir=".literature_cache",
            use_fallback_pdf=False
        )

        self.results = {
            'publisher': [],
            'pmc': [],
            'unpaywall': [],
            'semantic_scholar': [],
            'fallback_mirror': [],
            'web_search': [],
            'failed': []
        }

    def extract_dois_from_kb(self, max_dois: int = 20) -> List[str]:
        """Extract sample DOIs from knowledge base"""

        kb_dir = Path('kb/communities')
        yaml_files = sorted(kb_dir.glob('*.yaml'))

        dois = []
        seen = set()

        for yaml_path in yaml_files:
            if len(dois) >= max_dois:
                break

            with open(yaml_path, 'r') as f:
                data = yaml.safe_load(f)

            # Check all evidence
            for section in ['taxonomy', 'ecological_interactions', 'environmental_factors']:
                if section not in data:
                    continue

                items = data[section]
                for item in items:
                    if 'evidence' not in item:
                        continue

                    for ev in item['evidence']:
                        ref = ev.get('reference', '')

                        if ref.startswith('doi:'):
                            doi = ref[4:]
                            if doi not in seen:
                                dois.append(doi)
                                seen.add(doi)

                                if len(dois) >= max_dois:
                                    return dois

        return dois

    def test_single_doi(self, doi: str, use_fallback: bool = False) -> Tuple[Optional[str], Optional[str]]:
        """
        Test PDF fetching for a single DOI.

        Returns: (pdf_url, source_tier)
        """

        fetcher = self.fetcher_with_fallback if use_fallback else self.fetcher_no_fallback

        try:
            result = fetcher.fetch_pdf_url(doi)
            if result:
                pdf_url, source = result
                return (pdf_url, source)
            return (None, None)
        except Exception as e:
            print(f"  Error: {e}")
            return (None, None)

    def test_cascade(self, dois: List[str], use_fallback: bool = True):
        """Test PDF cascade for multiple DOIs"""

        print(f"\nTesting {'WITH' if use_fallback else 'WITHOUT'} fallback mirrors...")
        print("=" * 80)

        for i, doi in enumerate(dois, 1):
            print(f"\n[{i}/{len(dois)}] Testing {doi}")
            print("-" * 80)

            pdf_url, source = self.test_single_doi(doi, use_fallback)

            if source:
                self.results[source].append({
                    'doi': doi,
                    'pdf_url': pdf_url
                })
                print(f"✓ SUCCESS via {source}")
            else:
                self.results['failed'].append(doi)
                print(f"✗ FAILED - No PDF found")

            # Rate limit
            time.sleep(1)

    def test_scihub_config(self):
        """Test scihub fallback configuration"""

        print("\n" + "=" * 80)
        print("SCIHUB FALLBACK CONFIGURATION")
        print("=" * 80)

        print(f"\nFallback enabled: {self.fetcher_with_fallback.use_fallback_pdf}")
        print(f"Fallback mirrors configured: {len(self.fetcher_with_fallback.fallback_pdf_urls)}")

        if self.fetcher_with_fallback.fallback_pdf_urls:
            print("\nConfigured mirrors:")
            for mirror in self.fetcher_with_fallback.fallback_pdf_urls:
                print(f"  - {mirror}")
        else:
            print("\n⚠ WARNING: No fallback mirrors configured!")
            print("Set FALLBACK_PDF_MIRRORS environment variable")

        print()

    def test_html_parsing(self):
        """Test scihub HTML parsing with sample HTML"""

        print("\n" + "=" * 80)
        print("SCIHUB HTML PARSING TEST")
        print("=" * 80)

        # Sample scihub HTML patterns
        test_cases = [
            # Pattern 1: <object> tag
            '''<html><body>
            <object id="pdf" data="https://twin.sci-hub.se/12345/article.pdf"
                    type="application/pdf" width="100%" height="100%">
            </object>
            </body></html>''',

            # Pattern 2: <a> tag
            '''<html><body>
            <a href="//sci-hub.se/downloads/2023-01-15/abc/article.pdf">Download PDF</a>
            </body></html>''',

            # Pattern 3: <embed> tag
            '''<html><body>
            <embed src="/downloads/article.pdf" type="application/pdf">
            </body></html>''',

            # Pattern 4: <iframe>
            '''<html><body>
            <iframe src="https://sci-hub.st/pdf/article.pdf"></iframe>
            </body></html>''',
        ]

        base_url = "https://sci-hub.se"

        for i, html in enumerate(test_cases, 1):
            print(f"\nTest case {i}:")
            pdf_url = self.fetcher_with_fallback._extract_pdf_from_fallback_html(html, base_url)
            if pdf_url:
                print(f"  ✓ Extracted: {pdf_url}")
            else:
                print(f"  ✗ Failed to extract PDF URL")

    def generate_report(self):
        """Generate comprehensive test report"""

        print("\n" + "=" * 80)
        print("PDF FETCHING TEST RESULTS")
        print("=" * 80)

        total = sum(len(items) for source, items in self.results.items() if source != 'failed')
        total_tested = total + len(self.results['failed'])

        print(f"\nTotal DOIs tested: {total_tested}")
        print(f"Successful: {total} ({100*total/total_tested if total_tested > 0 else 0:.1f}%)")
        print(f"Failed: {len(self.results['failed'])} ({100*len(self.results['failed'])/total_tested if total_tested > 0 else 0:.1f}%)")

        print("\n" + "-" * 80)
        print("SUCCESS BY TIER")
        print("-" * 80)

        tier_order = ['publisher', 'pmc', 'unpaywall', 'semantic_scholar', 'fallback_mirror', 'web_search']

        for tier in tier_order:
            count = len(self.results[tier])
            pct = 100 * count / total_tested if total_tested > 0 else 0

            status = "✓" if count > 0 else "✗"
            print(f"{status} Tier {tier_order.index(tier)+1} ({tier:20s}): {count:3d} ({pct:5.1f}%)")

        # Show examples
        print("\n" + "-" * 80)
        print("EXAMPLES")
        print("-" * 80)

        for tier in tier_order:
            if self.results[tier]:
                print(f"\n{tier.upper()} (showing 3 examples):")
                for item in self.results[tier][:3]:
                    print(f"  {item['doi']}")
                    print(f"    → {item['pdf_url'][:80]}...")
                if len(self.results[tier]) > 3:
                    print(f"  ... and {len(self.results[tier])-3} more")

        # Show failures
        if self.results['failed']:
            print(f"\nFAILED (showing 5 examples):")
            for doi in self.results['failed'][:5]:
                print(f"  {doi}")
            if len(self.results['failed']) > 5:
                print(f"  ... and {len(self.results['failed'])-5} more")

    def test_specific_publishers(self):
        """Test publisher-specific PDF patterns"""

        print("\n" + "=" * 80)
        print("PUBLISHER-SPECIFIC PATTERN TEST")
        print("=" * 80)

        test_dois = {
            'ASM (American Society for Microbiology)': '10.1128/AEM.00001-20',
            'PLOS': '10.1371/journal.pone.0123456',
            'Frontiers': '10.3389/fmicb.2020.00001',
            'MDPI': '10.3390/microorganisms8010001',
            'Nature': '10.1038/s41586-020-0001-0',
            'Science': '10.1126/science.aaa0001',
            'Elsevier': '10.1016/j.cell.2020.01.001'
        }

        print("\nPublisher pattern coverage:")
        for publisher, doi_prefix in test_dois.items():
            # Check if pattern exists in code
            has_pattern = self.fetcher_with_fallback._get_pdf_url_from_publisher(doi_prefix) is not None
            status = "✓" if has_pattern else "✗"
            print(f"  {status} {publisher}: {doi_prefix}")


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Test PDF fetching capabilities")
    parser.add_argument('--quick', action='store_true', help="Quick test with 5 DOIs")
    parser.add_argument('--full', action='store_true', help="Full test with 20 DOIs")
    parser.add_argument('--no-fallback', action='store_true', help="Test without scihub fallback")
    parser.add_argument('--config-only', action='store_true', help="Only test configuration")
    args = parser.parse_args()

    tester = PDFFetchingTester()

    print("PDF FETCHING CORE CAPABILITY TEST")
    print("=" * 80)

    # Always test configuration
    tester.test_scihub_config()
    tester.test_html_parsing()

    if args.config_only:
        print("\n✓ Configuration test complete")
        return

    # Determine test size
    if args.quick:
        max_dois = 5
    elif args.full:
        max_dois = 20
    else:
        max_dois = 10  # default

    # Extract DOIs from KB
    print(f"\nExtracting {max_dois} DOIs from knowledge base...")
    dois = tester.extract_dois_from_kb(max_dois)
    print(f"Found {len(dois)} DOIs to test")

    if not dois:
        print("⚠ No DOIs found in knowledge base")
        return

    # Test with/without fallback
    use_fallback = not args.no_fallback
    tester.test_cascade(dois, use_fallback=use_fallback)

    # Test publisher patterns
    tester.test_specific_publishers()

    # Generate report
    tester.generate_report()

    print("\n" + "=" * 80)
    print("RECOMMENDATIONS")
    print("=" * 80)

    if len(tester.results['fallback_mirror']) == 0 and use_fallback:
        print("\n⚠ No PDFs found via fallback mirrors")
        print("  Possible reasons:")
        print("  1. Scihub mirrors may be blocked/unavailable")
        print("  2. HTML parsing patterns may need update")
        print("  3. Mirrors may have changed URLs")
        print("\n  Try:")
        print("  - Check FALLBACK_PDF_MIRRORS environment variable")
        print("  - Test individual mirrors manually")
        print("  - Update HTML parsing patterns if needed")

    success_rate = 100 * sum(len(items) for source, items in tester.results.items() if source != 'failed') / len(dois)

    if success_rate < 50:
        print("\n⚠ Low success rate detected")
        print("  Suggestions:")
        print("  1. Enable scihub fallback (if disabled)")
        print("  2. Add more publisher-specific patterns")
        print("  3. Check network connectivity")
    elif success_rate > 80:
        print("\n✓ Good PDF discovery rate!")
        print("  Core capability is working well")

    print()


if __name__ == '__main__':
    main()
