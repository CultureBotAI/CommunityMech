#!/usr/bin/env python3
"""
Evidence Snippet Extraction Tool

Extracts relevant snippets from abstracts/PDFs for evidence items missing snippets.

Usage:
    python scripts/extract_evidence_snippets.py <reference> <search_terms>

Example:
    python scripts/extract_evidence_snippets.py "PMID:28287150" "DIET" "electron transfer"
"""

import sys
import re
from pathlib import Path
from typing import List, Optional

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from communitymech.literature_enhanced import EnhancedLiteratureFetcher


class SnippetExtractor:
    """Extract relevant snippets from papers based on search terms"""

    def __init__(self):
        self.fetcher = EnhancedLiteratureFetcher(
            cache_dir=".literature_cache",
            use_fallback_pdf=True
        )

    def extract_snippets(
        self,
        reference: str,
        search_terms: List[str],
        use_pdf: bool = False
    ) -> List[str]:
        """
        Extract relevant snippets containing search terms.

        Args:
            reference: PMID or DOI
            search_terms: List of keywords to search for
            use_pdf: Whether to download and search full PDF

        Returns:
            List of relevant snippets
        """
        # Fetch paper
        paper = self.fetcher.fetch_paper(reference, download_pdf=use_pdf)

        snippets = []

        # Search in abstract
        if paper["abstract"]:
            abstract_snippets = self._find_snippets_in_text(
                paper["abstract"],
                search_terms
            )
            snippets.extend(abstract_snippets)

        # Search in PDF text
        if use_pdf and paper["pdf_text"]:
            pdf_snippets = self._find_snippets_in_text(
                paper["pdf_text"],
                search_terms,
                max_snippets=5  # Limit PDF snippets
            )
            snippets.extend(pdf_snippets)

        return snippets

    def _find_snippets_in_text(
        self,
        text: str,
        search_terms: List[str],
        max_snippets: int = 10,
        context_chars: int = 200
    ) -> List[str]:
        """
        Find snippets containing search terms with surrounding context.

        Args:
            text: Full text to search
            search_terms: Keywords to find
            max_snippets: Maximum number of snippets to return
            context_chars: Characters of context around each match

        Returns:
            List of snippets
        """
        snippets = []

        # Normalize text
        text_normalized = " ".join(text.split())

        # Find sentences containing any search term
        sentences = self._split_into_sentences(text_normalized)

        for sentence in sentences:
            # Check if sentence contains any search term (case-insensitive)
            if any(term.lower() in sentence.lower() for term in search_terms):
                # Clean up sentence
                snippet = sentence.strip()

                # Remove references like [1], (Smith et al., 2020)
                snippet = re.sub(r'\[\d+\]', '', snippet)
                snippet = re.sub(r'\([A-Za-z\s,]+\d{4}\)', '', snippet)

                # Remove excessive whitespace
                snippet = " ".join(snippet.split())

                if len(snippet) > 50:  # Minimum snippet length
                    snippets.append(snippet)

            if len(snippets) >= max_snippets:
                break

        return snippets

    def _split_into_sentences(self, text: str) -> List[str]:
        """
        Split text into sentences.

        Args:
            text: Text to split

        Returns:
            List of sentences
        """
        # Simple sentence splitter (could be improved with nltk)
        # Split on period followed by space and capital letter
        sentences = re.split(r'(?<=[.!?])\s+(?=[A-Z])', text)

        # Also split on newlines (for abstracts with line breaks)
        result = []
        for s in sentences:
            result.extend(s.split('\n'))

        return [s.strip() for s in result if s.strip()]


def main():
    """CLI for extracting evidence snippets"""
    if len(sys.argv) < 3:
        print("Usage: python scripts/extract_evidence_snippets.py <reference> <search_term1> [search_term2] ...")
        print("\nExample:")
        print('  python scripts/extract_evidence_snippets.py "PMID:28287150" "DIET" "electron transfer"')
        sys.exit(1)

    reference = sys.argv[1]
    search_terms = sys.argv[2:]
    use_pdf = "--pdf" in sys.argv

    print(f"Reference: {reference}")
    print(f"Search terms: {', '.join(search_terms)}")
    print(f"Use PDF: {use_pdf}")
    print("=" * 80)

    extractor = SnippetExtractor()

    print(f"\nFetching paper and extracting snippets...")
    snippets = extractor.extract_snippets(reference, search_terms, use_pdf=use_pdf)

    if not snippets:
        print("\n✗ No relevant snippets found")
        sys.exit(1)

    print(f"\n✓ Found {len(snippets)} relevant snippets:\n")
    print("=" * 80)

    for i, snippet in enumerate(snippets, 1):
        print(f"\n{i}. {snippet}")
        print()

    print("=" * 80)
    print("\nCopy the most relevant snippet into your YAML evidence item.")


if __name__ == '__main__':
    main()
