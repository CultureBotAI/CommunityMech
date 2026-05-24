"""
Literature fetching utilities for CommunityMech.

Fetches papers from PubMed, DOI, and other sources with caching.
"""

import re
from pathlib import Path

import requests


class LiteratureFetcher:
    """Fetch and cache scientific literature."""

    def __init__(self, cache_dir: str = "references_cache"):
        self.cache_dir = Path(cache_dir)
        self.cache_dir.mkdir(exist_ok=True)
        self.session = requests.Session()
        self.session.headers.update(
            {"User-Agent": "CommunityMech/0.1.0 (https://github.com/CultureBotAI/CommunityMech)"}
        )

    def fetch_pubmed_abstract(self, pmid: str) -> str | None:
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
        url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
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

    def fetch_doi_metadata(self, doi: str) -> dict | None:
        """
        Fetch metadata for a DOI from CrossRef.

        Args:
            doi: DOI (e.g., "10.1038/s41467-020-17612-8")

        Returns:
            Metadata dict or None
        """
        # Clean DOI
        doi = re.sub(r"^(?i:doi:)", "", doi).replace("https://doi.org/", "").strip()

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

    def fetch_pmid_for_doi(self, doi: str) -> str | None:
        """
        Resolve a DOI to its corresponding PubMed ID via NCBI esearch.

        Many DOIs that are paywalled on the publisher side and lack a
        CrossRef abstract still have a PubMed record with a free abstract.
        This helper looks up the PMID so the caller can fall back to
        fetch_pubmed_abstract for the abstract text.

        Args:
            doi: DOI string (with or without "doi:" prefix)

        Returns:
            PMID string (no prefix) or None
        """
        doi = re.sub(r"^(?i:doi:)", "", doi).replace("https://doi.org/", "").strip()

        url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
        params = {
            "db": "pubmed",
            "term": f"{doi}[doi]",
            "retmode": "json",
            "retmax": "1",
        }

        try:
            response = self.session.get(url, params=params, timeout=30)
            response.raise_for_status()
            data = response.json()
            id_list = data.get("esearchresult", {}).get("idlist", [])
            return id_list[0] if id_list else None
        except (requests.exceptions.RequestException, ValueError) as e:
            print(f"Error mapping DOI {doi} to PMID: {e}")
            return None

    def fetch_pmcid_for_doi(self, doi: str) -> str | None:
        """
        Resolve a DOI to its PubMed Central (PMC) ID via the PMC ID
        Converter API.

        Some DOIs that don't have a PubMed record do have a PMC record
        (for example, non-MEDLINE-indexed OA preprints). PMC content is
        free full-text XML, which contains an extractable abstract.

        The ID converter API performs an exact DOI lookup and returns an
        explicit `errmsg: "Identifier not found in PMC"` for DOIs that
        aren't in PMC. This avoids the silent fuzzy fallback that NCBI
        esearch performs on `[DOI]`-tagged terms (which strips DOI
        punctuation and re-runs as an `[All Fields]` token search,
        producing wrong-paper matches).

        Args:
            doi: DOI string (with or without "doi:" prefix)

        Returns:
            PMC ID (no prefix; numeric) or None
        """
        doi = re.sub(r"^(?i:doi:)", "", doi).replace("https://doi.org/", "").strip()

        url = "https://pmc.ncbi.nlm.nih.gov/tools/idconv/api/v1/articles/"
        params = {"ids": doi, "format": "json", "idtype": "doi"}

        try:
            response = self.session.get(url, params=params, timeout=30)
            response.raise_for_status()
            data = response.json()
            records = data.get("records", [])
            if not records:
                return None
            record = records[0]
            if record.get("status") == "error":
                return None
            pmcid = record.get("pmcid")
            if not pmcid:
                return None
            # Strip "PMC" prefix to return the numeric id
            return pmcid.replace("PMC", "").strip() or None
        except (requests.exceptions.RequestException, ValueError) as e:
            print(f"Error mapping DOI {doi} to PMCID: {e}")
            return None

    def fetch_pmc_abstract(self, pmcid: str) -> str | None:
        """
        Fetch the abstract portion of a PMC full-text XML record.

        PMC stores OA articles as JATS XML; the <abstract> element holds
        the abstract. This is a lighter-weight alternative to parsing the
        whole full-text body when only the abstract is needed for
        downstream snippet validation.

        Args:
            pmcid: PMC ID (with or without "PMC" prefix)

        Returns:
            Abstract text or None
        """
        # Normalize: strip the "PMCID:" prefix first, then the bare "PMC"
        # prefix. The reverse order would mangle "PMCID:3035377" into
        # "ID:3035377" since the inner "PMC" would be removed first.
        pmcid = pmcid.replace("PMCID:", "").replace("PMC", "").strip()

        cache_file = self.cache_dir / f"pmc_{pmcid}.txt"
        if cache_file.exists():
            return cache_file.read_text()

        url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
        params = {
            "db": "pmc",
            "id": pmcid,
            "rettype": "xml",
            "retmode": "xml",
        }

        try:
            response = self.session.get(url, params=params, timeout=30)
            response.raise_for_status()
            xml_text = response.text

            # Extract the <abstract>...</abstract> element. The JATS schema
            # nests text inside <p>, <sec>, etc.; strip XML tags for a
            # plain-text representation.
            abs_match = re.search(r"<abstract\b[^>]*>(.*?)</abstract>", xml_text, re.DOTALL)
            if not abs_match:
                return None
            inner = abs_match.group(1)
            # Strip tags
            plain = re.sub(r"<[^>]+>", " ", inner)
            # Collapse whitespace
            plain = re.sub(r"\s+", " ", plain).strip()
            if not plain:
                return None

            cache_file.write_text(plain)
            return plain
        except (requests.exceptions.RequestException, ValueError) as e:
            print(f"Error fetching PMC {pmcid} XML: {e}")
            return None

    def _abstract_cache_path(self, source: str, doi: str) -> Path:
        """
        Filesystem path for a per-source abstract cache file.

        Mirrors the on-disk caching pattern used by fetch_pubmed_abstract
        and fetch_pmc_abstract so repeated runs (validator, refresh
        scripts, smoke tests) do not re-hit rate-limited external APIs.
        """
        safe_doi = doi.replace("/", "_")
        return self.cache_dir / f"{source}_{safe_doi}.txt"

    def fetch_openalex_abstract(self, doi: str) -> str | None:
        """
        Fetch abstract from OpenAlex by DOI.

        OpenAlex stores abstracts as an inverted index (term -> [positions])
        for licensing reasons; we reconstruct the linear text by sorting on
        positions. Covers many older non-OA papers that Crossref/DataCite
        do not have abstracts for (e.g., legacy IJSEM, Springer, Elsevier
        titles indexed pre-1995).

        Args:
            doi: DOI string (with or without "doi:" prefix)

        Returns:
            Abstract text or None
        """
        doi = re.sub(r"^(?i:doi:)", "", doi).replace("https://doi.org/", "").strip()
        cache_file = self._abstract_cache_path("openalex", doi)
        if cache_file.exists():
            return cache_file.read_text() or None

        url = f"https://api.openalex.org/works/doi:{doi}"
        try:
            response = self.session.get(url, timeout=30)
            response.raise_for_status()
            data = response.json()
            inv = data.get("abstract_inverted_index")
            if not inv:
                return None
            # Reconstruct linear text from inverted index
            words = {pos: w for w, positions in inv.items() for pos in positions}
            text = " ".join(words[i] for i in sorted(words))
            if not text:
                return None
            cache_file.write_text(text)
            return text
        except (requests.exceptions.RequestException, ValueError) as e:
            print(f"Error fetching OpenAlex for {doi}: {e}")
            return None

    def fetch_semantic_scholar_abstract(self, doi: str) -> str | None:
        """
        Fetch abstract from Semantic Scholar by DOI.

        Semantic Scholar's coverage overlaps with Crossref+OpenAlex but
        sometimes carries an abstract when those do not (recent Elsevier
        titles where the publisher disclosed the abstract to Semantic
        Scholar but not Crossref).

        Args:
            doi: DOI string

        Returns:
            Abstract text or None
        """
        doi = re.sub(r"^(?i:doi:)", "", doi).replace("https://doi.org/", "").strip()
        cache_file = self._abstract_cache_path("semanticscholar", doi)
        if cache_file.exists():
            return cache_file.read_text() or None

        url = f"https://api.semanticscholar.org/graph/v1/paper/DOI:{doi}"
        try:
            response = self.session.get(url, params={"fields": "abstract"}, timeout=30)
            response.raise_for_status()
            data = response.json()
            abstract = data.get("abstract")
            if not abstract:
                return None
            cache_file.write_text(abstract)
            return abstract
        except (requests.exceptions.RequestException, ValueError) as e:
            print(f"Error fetching Semantic Scholar for {doi}: {e}")
            return None

    def fetch_europepmc_abstract(self, doi: str) -> str | None:
        """
        Fetch abstract from Europe PMC by DOI.

        Europe PMC indexes a broader set of life-science abstracts than
        US PMC, including some Springer/Wiley records where the abstract
        is mirrored to Europe PMC but the paper itself is not OA.

        Args:
            doi: DOI string

        Returns:
            Abstract text or None
        """
        doi = re.sub(r"^(?i:doi:)", "", doi).replace("https://doi.org/", "").strip()
        cache_file = self._abstract_cache_path("europepmc", doi)
        if cache_file.exists():
            return cache_file.read_text() or None

        url = "https://www.ebi.ac.uk/europepmc/webservices/rest/search"
        params = {
            "query": f"DOI:{doi}",
            "format": "json",
            "resultType": "core",
            "pageSize": "1",
        }
        try:
            response = self.session.get(url, params=params, timeout=30)
            response.raise_for_status()
            data = response.json()
            results = data.get("resultList", {}).get("result", [])
            if not results:
                return None
            abstract = results[0].get("abstractText")
            if not abstract:
                return None
            cache_file.write_text(abstract)
            return abstract
        except (requests.exceptions.RequestException, ValueError) as e:
            print(f"Error fetching Europe PMC for {doi}: {e}")
            return None

    def fetch_publisher_meta_abstract(self, doi: str) -> str | None:
        """
        Last-resort scrape of the DOI landing page for an abstract excerpt.

        Most publishers expose the abstract (or its first ~200 chars) in
        page-level meta tags - typically `twitter:description`,
        `og:description`, or the standard `<meta name="description">` -
        even when the article itself is paywalled and Crossref / OpenAlex /
        Semantic Scholar / Europe PMC carry no abstract. Springer/Nature
        is the most reliable source for this pattern; Elsevier
        ScienceDirect serves a bot-detection page and yields nothing.

        Args:
            doi: DOI string (with or without "doi:" prefix)

        Returns:
            Abstract excerpt (may be truncated to ~200 chars by the
            publisher) or None.
        """
        doi = re.sub(r"^(?i:doi:)", "", doi).replace("https://doi.org/", "").strip()
        cache_file = self._abstract_cache_path("publisher", doi)
        if cache_file.exists():
            return cache_file.read_text() or None

        try:
            response = self.session.get(
                f"https://doi.org/{doi}",
                headers={"User-Agent": "Mozilla/5.0 (Macintosh)"},
                allow_redirects=True,
                timeout=30,
            )
            response.raise_for_status()
            html = response.text
        except requests.exceptions.RequestException as e:
            print(f"Error scraping publisher page for {doi}: {e}")
            return None

        for tag in ("twitter:description", "og:description", "description"):
            match = re.search(
                rf'<meta\s+[^>]*name=["\']?{tag}["\']?\s+content=["\']([^"\']+)["\']',
                html,
                re.IGNORECASE,
            )
            if not match:
                match = re.search(
                    rf'<meta\s+[^>]*property=["\']?{tag}["\']?\s+content=["\']([^"\']+)["\']',
                    html,
                    re.IGNORECASE,
                )
            if match:
                text = match.group(1)
                # Decode common HTML entities
                text = (
                    text.replace("&amp;", "&")
                    .replace("&quot;", '"')
                    .replace("&#x27;", "'")
                    .replace("&lt;", "<")
                    .replace("&gt;", ">")
                )
                # Strip Springer's "Journal Name - " prefix and trailing ellipsis
                text = re.sub(r"^[^-]+-\s*", "", text).rstrip(" .")
                if len(text) > 80:  # skip nav-text and similar short snippets
                    cache_file.write_text(text)
                    return text
        return None

    def fetch_unpaywall(self, doi: str, email: str = "noreply@example.com") -> str | None:
        """
        Try to fetch open access PDF URL from Unpaywall.

        Args:
            doi: DOI string
            email: Email for Unpaywall API (required)

        Returns:
            PDF URL or None
        """
        doi = re.sub(r"^(?i:doi:)", "", doi).replace("https://doi.org/", "").strip()

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

    def fetch_paper(
        self, reference: str, email: str = "noreply@example.com"
    ) -> tuple[str | None, str | None]:
        """
        Fetch a paper's abstract and metadata from various sources.

        Args:
            reference: PMID (e.g., "PMID:12345") or DOI (e.g., "doi:10.1234/...")
            email: Email for APIs

        Returns:
            Tuple of (abstract_text, pdf_url)
        """
        # Determine reference type
        pmid: str | None
        if reference.startswith("PMID:") or reference.isdigit():
            pmid = reference.replace("PMID:", "").strip()
            abstract = self.fetch_pubmed_abstract(pmid)

            # Try to get DOI from PubMed record for PDF access
            # For now, just return abstract
            return (abstract, None)

        elif "doi" in reference.lower() or reference.startswith("10."):
            doi = re.sub(r"^(?i:doi:)", "", reference).replace("https://doi.org/", "").strip()

            # Try Unpaywall for OA PDF
            pdf_url = self.fetch_unpaywall(doi, email=email)

            # Get metadata (may contain abstract)
            metadata = self.fetch_doi_metadata(doi)
            abstract = metadata.get("abstract") if metadata else None

            # Fallback chain for paywalled DOIs with no CrossRef abstract:
            # (a) Try DOI -> PMID -> PubMed abstract.
            # (b) Try DOI -> PMCID -> PMC OA full-text XML and extract the
            #     <abstract> element. Covers OA papers (preprints, BMC, PLoS,
            #     Frontiers, etc.) in PMC but missing from CrossRef.
            # (c) Try OpenAlex (broad coverage of legacy non-OA titles
            #     including pre-1995 IJSEM, Springer, Elsevier).
            # (d) Try Semantic Scholar (sometimes carries abstracts for
            #     recent Elsevier titles when Crossref does not).
            # (e) Try Europe PMC (broader life-science coverage than US PMC,
            #     mirrors abstracts for some Springer/Wiley records).
            if not abstract:
                pmid = self.fetch_pmid_for_doi(doi)
                if pmid:
                    abstract = self.fetch_pubmed_abstract(pmid)
            if not abstract:
                pmcid = self.fetch_pmcid_for_doi(doi)
                if pmcid:
                    abstract = self.fetch_pmc_abstract(pmcid)
            if not abstract:
                abstract = self.fetch_openalex_abstract(doi)
            if not abstract:
                abstract = self.fetch_semantic_scholar_abstract(doi)
            if not abstract:
                abstract = self.fetch_europepmc_abstract(doi)
            if not abstract:
                abstract = self.fetch_publisher_meta_abstract(doi)

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

        ratio = SequenceMatcher(
            None, snippet_normalized.lower(), abstract_normalized.lower()
        ).ratio()
        return ratio > 0.95


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
