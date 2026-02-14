"""
Literature fetching utilities for CommunityMech.

Fetches papers from PubMed, DOI, and other sources with caching.
"""

import re
import requests
from pathlib import Path
from typing import Optional, Tuple
import time


class LiteratureFetcher:
    """Fetch and cache scientific literature."""

    def __init__(self, cache_dir: str = "references_cache"):
        self.cache_dir = Path(cache_dir)
        self.cache_dir.mkdir(exist_ok=True)
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": "CommunityMech/0.1.0 (https://github.com/CultureBotAI/CommunityMech)"
        })

    def fetch_pubmed_abstract(self, pmid: str) -> Optional[str]:
        """
        Fetch abstract from PubMed for a given PMID.

        Args:
            pmid: PubMed ID (e.g., "32753581")

        Returns:
            Abstract text or None if not found
        """
        # Clean PMID
        pmid = pmid.replace("PMID:", "").strip()

        # Check cache first
        cache_file = self.cache_dir / f"pmid_{pmid}.txt"
        if cache_file.exists():
            return cache_file.read_text()

        # Fetch from PubMed E-utilities
        url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
        params = {
            "db": "pubmed",
            "id": pmid,
            "rettype": "abstract",
            "retmode": "text",
        }

        try:
            response = self.session.get(url, params=params, timeout=30)
            response.raise_for_status()

            abstract = response.text

            # Cache the result
            cache_file.write_text(abstract)

            return abstract

        except requests.exceptions.RequestException as e:
            print(f"Error fetching PMID {pmid}: {e}")
            return None

    def fetch_doi_metadata(self, doi: str) -> Optional[dict]:
        """
        Fetch metadata for a DOI from CrossRef.

        Args:
            doi: DOI (e.g., "10.1038/s41467-020-17612-8")

        Returns:
            Metadata dict or None
        """
        # Clean DOI
        doi = doi.replace("doi:", "").replace("https://doi.org/", "").strip()

        # Check cache
        cache_file = self.cache_dir / f"doi_{doi.replace('/', '_')}.json"
        if cache_file.exists():
            import json
            return json.loads(cache_file.read_text())

        # Fetch from CrossRef
        url = f"https://api.crossref.org/works/{doi}"

        try:
            response = self.session.get(url, timeout=30)
            response.raise_for_status()

            metadata = response.json()

            # Cache the result
            import json
            cache_file.write_text(json.dumps(metadata, indent=2))

            return metadata

        except requests.exceptions.RequestException as e:
            print(f"Error fetching DOI {doi}: {e}")
            return None

    def fetch_unpaywall(self, doi: str, email: str = "noreply@example.com") -> Optional[str]:
        """
        Try to fetch open access PDF URL from Unpaywall.

        Args:
            doi: DOI string
            email: Email for Unpaywall API (required)

        Returns:
            PDF URL or None
        """
        doi = doi.replace("doi:", "").replace("https://doi.org/", "").strip()

        url = f"https://api.unpaywall.org/v2/{doi}"
        params = {"email": email}

        try:
            response = self.session.get(url, params=params, timeout=30)
            response.raise_for_status()

            data = response.json()

            # Check for OA location
            if data.get("is_oa") and data.get("best_oa_location"):
                pdf_url = data["best_oa_location"].get("url_for_pdf")
                return pdf_url

            return None

        except requests.exceptions.RequestException as e:
            print(f"Error checking Unpaywall for {doi}: {e}")
            return None

    def fetch_paper(self, reference: str, email: str = "noreply@example.com") -> Tuple[Optional[str], Optional[str]]:
        """
        Fetch a paper's abstract and metadata from various sources.

        Args:
            reference: PMID (e.g., "PMID:12345") or DOI (e.g., "doi:10.1234/...")
            email: Email for APIs

        Returns:
            Tuple of (abstract_text, pdf_url)
        """
        # Determine reference type
        if reference.startswith("PMID:") or reference.isdigit():
            pmid = reference.replace("PMID:", "").strip()
            abstract = self.fetch_pubmed_abstract(pmid)

            # Try to get DOI from PubMed record for PDF access
            # For now, just return abstract
            return (abstract, None)

        elif "doi" in reference.lower() or reference.startswith("10."):
            doi = reference.replace("doi:", "").replace("https://doi.org/", "").strip()

            # Try Unpaywall for OA PDF
            pdf_url = self.fetch_unpaywall(doi, email=email)

            # Get metadata (may contain abstract)
            metadata = self.fetch_doi_metadata(doi)
            abstract = metadata.get("abstract") if metadata else None

            return (abstract, pdf_url)

        else:
            print(f"Unknown reference format: {reference}")
            return (None, None)

    def validate_evidence_snippet(self, snippet: str, abstract: str) -> bool:
        """
        Check if a snippet appears in the abstract (fuzzy match).

        Args:
            snippet: Quoted text from YAML
            abstract: Full abstract text

        Returns:
            True if snippet found in abstract
        """
        if not abstract or not snippet:
            return False

        # Normalize whitespace
        snippet_normalized = " ".join(snippet.split())
        abstract_normalized = " ".join(abstract.split())

        # Check for exact match
        if snippet_normalized.lower() in abstract_normalized.lower():
            return True

        # Check for fuzzy match (allow minor differences)
        from difflib import SequenceMatcher
        ratio = SequenceMatcher(None, snippet_normalized.lower(), abstract_normalized.lower()).ratio()
        if ratio > 0.95:
            return True

        return False


def main():
    """CLI for testing literature fetching."""
    import sys

    if len(sys.argv) < 2:
        print("Usage: python -m communitymech.literature <PMID|DOI>")
        sys.exit(1)

    fetcher = LiteratureFetcher()
    reference = sys.argv[1]

    print(f"Fetching: {reference}")
    abstract, pdf_url = fetcher.fetch_paper(reference)

    if abstract:
        print(f"\n{'='*80}")
        print("ABSTRACT:")
        print(f"{'='*80}")
        print(abstract[:500] + "..." if len(abstract) > 500 else abstract)

    if pdf_url:
        print(f"\n{'='*80}")
        print(f"PDF URL: {pdf_url}")

    if not abstract and not pdf_url:
        print("Could not fetch paper.")


if __name__ == "__main__":
    main()
