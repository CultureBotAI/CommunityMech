"""
Literature fetching utilities for CommunityMech.

Fetches papers from PubMed, DOI, and other sources with caching.
"""

import re
from pathlib import Path

import requests

# ---------------------------------------------------------------------------
# Citation / first-author derivation
# ---------------------------------------------------------------------------
#
# Background: the related_ingredients backfill writes `relevance` prose that
# ends with a short citation of the form "(Surname et al. Year)". When that
# string is composed by hand (or from an LLM's memory of the paper) the
# first-author surname is frequently WRONG — it names a non-first or
# non-present author. The functions below derive the citation
# DETERMINISTICALLY from the authoritative metadata that the fetcher already
# caches, so the cited surname is always the paper's real first author.
#
# Two metadata shapes are supported:
#   1. NCBI efetch `rettype=abstract&retmode=text` (MEDLINE-ish plain text),
#      which is what fetch_pubmed_abstract caches as PMID_<id>.txt.
#   2. A free-form author string ("Surname AB, Other CD, ...") such as the
#      Europe PMC `authorString` field or a CrossRef author list joined into
#      one line — see parse_first_author_from_author_string.

# A MEDLINE author line looks like:
#   "Luo DL(1), Huang SY(1), Ma CY(1), ..., Dai CC(1)."
# i.e. "Surname INITIALS" tokens (initials are 1-3 uppercase letters,
# optionally with parenthetical affiliation markers) separated by commas. A
# single-author paper has no comma. Collective/consortium authors appear as a
# capitalized phrase ending in a keyword like "Group"/"Consortium" and have
# no initials token.
_AUTHOR_TOKEN_RE = re.compile(
    r"^([A-Z][\w'\-]+(?:\s+[A-Z][\w'\-]+)*)"  # surname (may be multi-word, e.g. "Van Dyk")
    r"\s+([A-Z][A-Za-z]{0,2}(?:\s+[A-Z][A-Za-z]{0,2})*)"  # given-name initials
    r"(?:\([\d,\s]+\))*$"  # optional affiliation markers like "(1)(2)"
)
_COLLECTIVE_KEYWORDS = (
    "group",
    "consortium",
    "collaboration",
    "network",
    "team",
    "study",
    "investigators",
)


def _strip_affiliation_markers(token: str) -> str:
    """Remove trailing "(1)(2)" affiliation superscripts from a name token."""
    return re.sub(r"\([\d,\s]+\)", "", token).strip()


def parse_first_author_from_author_string(author_string: str) -> str | None:
    """Return the first author's surname from a comma-separated author string.

    Handles the Europe PMC ``authorString`` shape ("Luo DL, Huang SY, ...")
    and a CrossRef author list joined as "Surname GivenInitials, ...".
    Returns the surname only (no initials). Returns ``None`` when no author
    can be parsed.
    """
    if not author_string:
        return None
    first = author_string.split(",")[0].strip().rstrip(".")
    first = _strip_affiliation_markers(first)
    if not first:
        return None

    # Collective/consortium author (e.g. "The Human Microbiome Consortium"):
    # keep the whole phrase, it has no surname/initials split.
    if any(kw in first.lower() for kw in _COLLECTIVE_KEYWORDS):
        return first

    m = _AUTHOR_TOKEN_RE.match(first)
    if m:
        return m.group(1)
    # Fallback: first whitespace-delimited token is the surname for most
    # "Surname Initials" forms even if initials look unusual.
    return first.split()[0] if first.split() else None


def parse_first_author_from_medline(text: str) -> str | None:
    """Extract the first author's surname from MEDLINE-format abstract text.

    The NCBI efetch text layout is:

        <ordinal>. <Journal>. <Year> ... doi: ...
        <Title spanning one or more lines>
        <Author line: "Surname AB(1), Other CD(2), ...">
        Author information:
        ...

    The author line is the first non-empty line *after* the title that parses
    as a list of "Surname Initials" tokens. We find it by scanning for the
    first line whose leading comma-separated token matches an author token (or
    is a collective author). This is robust to multi-line titles and to the
    leading "N." reference ordinal that efetch prepends in batch mode.
    """
    if not text:
        return None
    lines = text.splitlines()
    # Skip the journal/citation line(s) and title; find the author line.
    for raw in lines:
        line = raw.strip()
        if not line:
            continue
        # The author line ends with a period and its first token parses as an
        # author. Reject the journal line (contains "doi:" / volume colons)
        # and "Author information:" / "PMID:" administrative lines.
        low = line.lower()
        if low.startswith(("author information", "pmid", "doi", "©", "free", "copyright")):
            continue
        first_token = line.split(",")[0].strip().rstrip(".")
        first_token_clean = _strip_affiliation_markers(first_token)
        if not first_token_clean:
            continue
        if any(kw in first_token_clean.lower() for kw in _COLLECTIVE_KEYWORDS):
            # Only treat as a collective author if it sits where the author
            # line is expected (not the title). Require it to be followed by
            # "Author information:" within the next few lines, or be the last
            # name-like line — heuristic, but collective-only papers are rare.
            return first_token_clean
        if _AUTHOR_TOKEN_RE.match(first_token_clean):
            return _AUTHOR_TOKEN_RE.match(first_token_clean).group(1)
    return None


def parse_year_from_medline(text: str) -> str | None:
    """Extract the 4-digit publication year from MEDLINE-format text.

    The year follows the journal name in the first citation line, e.g.
    "J Appl Microbiol. 2024 Apr 1;135(4)..." -> "2024".
    """
    if not text:
        return None
    m = re.search(r"\b(19|20)\d{2}\b", text)
    return m.group(0) if m else None


def _author_count_medline(text: str) -> int:
    """Best-effort count of authors on the MEDLINE author line.

    Used to decide whether "et al." is warranted (>1 author).
    """
    if not text:
        return 0
    for raw in text.splitlines():
        line = raw.strip()
        if not line:
            continue
        low = line.lower()
        if low.startswith(("author information", "pmid", "doi", "©", "free", "copyright")):
            continue
        first_token = _strip_affiliation_markers(line.split(",")[0].strip().rstrip("."))
        if not first_token:
            continue
        if any(kw in first_token.lower() for kw in _COLLECTIVE_KEYWORDS):
            return 1
        if _AUTHOR_TOKEN_RE.match(first_token):
            # Author line may wrap across lines; collect until a blank line or
            # an "Author information:" sentinel.
            buf = [line]
            return buf[0].count(",") + 1 if buf[0].endswith(".") else max(1, buf[0].count(",") + 1)
    return 0


def format_citation(text: str, *, author_string: str | None = None) -> str | None:
    """Build the canonical "(Surname et al. Year)" citation deterministically.

    Args:
        text: MEDLINE-format abstract text (as cached in PMID_<id>.txt). May
            be empty if only an author_string is available.
        author_string: Optional explicit author list (Europe PMC
            ``authorString`` / CrossRef joined list). Preferred over parsing
            the MEDLINE text when supplied.

    Returns:
        A citation string like "(Luo et al. 2024)", or "(Luo 2024)" for a
        single-author paper, or just "(Luo)" when no year is parseable.
        Returns ``None`` when no first author can be derived.
    """
    surname = (
        parse_first_author_from_author_string(author_string)
        if author_string
        else parse_first_author_from_medline(text)
    )
    if not surname:
        return None

    year = parse_year_from_medline(text) if text else None

    # Decide "et al." — only for multi-author papers.
    if author_string:
        n_authors = len([p for p in author_string.split(",") if p.strip()])
    else:
        n_authors = _author_count_medline(text)
    is_collective = any(kw in surname.lower() for kw in _COLLECTIVE_KEYWORDS)
    etal = " et al." if (n_authors > 1 and not is_collective) else ""

    if year:
        return f"({surname}{etal} {year})"
    return f"({surname}{etal})"


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

        # Check cache first.
        #
        # Use the uppercase `PMID_<id>.txt` convention so the cached abstract is
        # ALSO discoverable by the external linkml-reference-validator, whose
        # ReferenceFetcher.get_cache_path() normalizes "PMID:<id>" to
        # `PMID_<id>.md` (primary) with a legacy fallback to `PMID_<id>.txt`.
        # The old lowercase `pmid_<id>.txt` name was invisible to the validator
        # on case-sensitive filesystems (Linux/CI), forcing a network re-fetch
        # and "Could not fetch" warnings every run.
        cache_file = self.cache_dir / f"PMID_{pmid}.txt"
        if cache_file.exists():
            return cache_file.read_text()
        # Legacy lowercase fallback (pre-rename caches); read-only.
        legacy_cache_file = self.cache_dir / f"pmid_{pmid}.txt"
        if legacy_cache_file.exists():
            return legacy_cache_file.read_text()

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

    def citation_for_pmid(self, pmid: str) -> str | None:
        """Return the canonical "(Surname et al. Year)" citation for a PMID.

        Fetches (or reads from cache) the PubMed abstract text and derives the
        citation DETERMINISTICALLY from the paper's real first author. This is
        the function backfill tooling should call to produce the relevance
        citation, instead of composing the author name by hand.

        Returns ``None`` when the abstract cannot be fetched or no author can
        be parsed.
        """
        abstract = self.fetch_pubmed_abstract(pmid)
        if not abstract:
            return None
        return format_citation(abstract)

    def first_author_for_pmid(self, pmid: str) -> str | None:
        """Return just the first-author surname for a PMID (from cached text)."""
        abstract = self.fetch_pubmed_abstract(pmid)
        if not abstract:
            return None
        return parse_first_author_from_medline(abstract)

    def validate_citation_author(self, pmid: str, cited_surname: str) -> bool:
        """Check a hand-written cited surname against the paper's real first author.

        Returns ``True`` when ``cited_surname`` matches the first author parsed
        from the cached PubMed metadata (case-insensitive). Use this as an
        anti-hallucination gate before committing relevance prose.
        Returns ``False`` when they differ OR when the author cannot be parsed
        (fail-closed: an unverifiable citation should not silently pass).
        """
        actual = self.first_author_for_pmid(pmid)
        if not actual or not cited_surname:
            return False
        return actual.strip().lower() == cited_surname.strip().lower()


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
