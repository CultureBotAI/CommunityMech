"""
Determine community strain coverage in UniProt reference proteomes.

This module reads community YAML files, extracts taxonomy entries, and checks
whether each strain-like taxon is represented in UniProt reference proteomes.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import time
import urllib.parse
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

import requests
import yaml

TRANSIENT_STATUS_CODES = {429, 500, 502, 503, 504}
STRAIN_STOPWORDS = {
    "strain",
    "str",
    "subsp",
    "serovar",
    "pv",
    "pathovar",
    "biovar",
    "group",
}
QUALIFIER_PREFIXES = ("subsp", "serovar", "pv.", "pathovar", "biovar", "group")
COARSE_NCBI_TAXON_IDS = {
    1,  # root
    2,  # Bacteria
    2157,  # Archaea
    2759,  # Eukaryota
    10239,  # Viruses
    131567,  # cellular organisms
}


@dataclass(frozen=True)
class CommunityTaxon:
    """Taxon entry extracted from a community YAML file."""

    community_file: str
    community_name: str
    preferred_term: str
    taxon_label: str
    taxon_id: str
    ncbi_taxonomy_id: int | None
    inferred_strain_name: str | None
    has_explicit_strain_designation: bool
    is_strain_taxon: bool


@dataclass(frozen=True)
class ProteomeSummary:
    """Minimal UniProt proteome metadata used for matching."""

    upid: str
    proteome_type: str
    strain: str
    taxonomy_id: int | None
    scientific_name: str


@dataclass(frozen=True)
class StrainCoverageResult:
    """Coverage result for a single taxon."""

    community_file: str
    community_name: str
    preferred_term: str
    taxon_label: str
    taxon_id: str
    ncbi_taxonomy_id: int | None
    inferred_strain_name: str | None
    is_strain_taxon: bool
    represented: bool
    reason: str
    reference_proteomes: list[ProteomeSummary]
    matched_proteomes: list[ProteomeSummary]

    def to_dict(self) -> dict[str, Any]:
        """Serialize the result for JSON output."""
        data = asdict(self)
        data["reference_proteomes"] = [asdict(item) for item in self.reference_proteomes]
        data["matched_proteomes"] = [asdict(item) for item in self.matched_proteomes]
        return data


class UniProtProteomeClient:
    """Thin client for UniProt proteomes REST API."""

    BASE_URL = "https://rest.uniprot.org/proteomes/search"

    def __init__(
        self,
        timeout_s: float = 30.0,
        max_retries: int = 3,
        request_delay_s: float = 0.0,
        user_agent: str = "CommunityMech/0.1.0 (UniProt strain coverage checker)",
    ) -> None:
        self.timeout_s = timeout_s
        self.max_retries = max_retries
        self.request_delay_s = request_delay_s
        self._cache: dict[int, list[ProteomeSummary]] = {}
        self.session = requests.Session()
        self.session.headers.update({"User-Agent": user_agent, "Accept": "application/json"})

    def search_reference_proteomes(self, taxonomy_id: int) -> list[ProteomeSummary]:
        """
        Fetch all reference proteomes matching a taxonomy ID.

        UniProt query:
            taxonomy_id:<id> AND reference:true
        """
        if taxonomy_id in self._cache:
            return self._cache[taxonomy_id]

        query = f"taxonomy_id:{taxonomy_id} AND reference:true"
        params = {"query": query, "format": "json", "size": "500"}
        url = f"{self.BASE_URL}?{urllib.parse.urlencode(params)}"
        results: list[ProteomeSummary] = []

        while url:
            payload, headers = self._get_json_with_retries(url)
            for raw_result in payload.get("results", []):
                taxonomy = raw_result.get("taxonomy", {})
                results.append(
                    ProteomeSummary(
                        upid=raw_result.get("id", ""),
                        proteome_type=raw_result.get("proteomeType", ""),
                        strain=raw_result.get("strain", ""),
                        taxonomy_id=taxonomy.get("taxonId"),
                        scientific_name=taxonomy.get("scientificName", ""),
                    )
                )

            url = _extract_next_link(headers.get("Link"))
            if self.request_delay_s and url:
                time.sleep(self.request_delay_s)

        self._cache[taxonomy_id] = results
        return results

    def _get_json_with_retries(
        self, url: str
    ) -> tuple[dict[str, Any], requests.structures.CaseInsensitiveDict[str]]:
        """GET JSON with retry on transient failures."""
        last_error: Exception | None = None
        for attempt in range(self.max_retries):
            try:
                response = self.session.get(url, timeout=self.timeout_s)
                if (
                    response.status_code in TRANSIENT_STATUS_CODES
                    and attempt < self.max_retries - 1
                ):
                    time.sleep(1.0 * (attempt + 1))
                    continue
                response.raise_for_status()
                return response.json(), response.headers
            except requests.RequestException as exc:
                last_error = exc
                if attempt < self.max_retries - 1:
                    time.sleep(1.0 * (attempt + 1))
                    continue
                break
            except ValueError as exc:
                last_error = exc
                break

        raise RuntimeError(f"UniProt request failed: {url}") from last_error


def extract_ncbi_taxonomy_id(term_id: str) -> int | None:
    """Parse NCBITaxon CURIE into integer taxonomy ID."""
    if not term_id or not term_id.startswith("NCBITaxon:"):
        return None
    raw_id = term_id.split(":", maxsplit=1)[1].strip()
    return int(raw_id) if raw_id.isdigit() else None


def infer_strain_name(
    strain_designation: dict[str, Any] | None,
    preferred_term: str,
    taxon_label: str,
) -> str | None:
    """Infer a strain name from explicit data or taxon label text."""
    if isinstance(strain_designation, dict):
        strain_name = str(strain_designation.get("strain_name", "")).strip()
        if strain_name:
            return strain_name

        culture_collections = strain_designation.get("culture_collections", [])
        if isinstance(culture_collections, list):
            for collection_entry in culture_collections:
                if not isinstance(collection_entry, dict):
                    continue
                collection = str(collection_entry.get("collection", "")).strip()
                accession = str(collection_entry.get("accession", "")).strip()
                if collection and accession:
                    return f"{collection} {accession}"

    for text in (preferred_term, taxon_label):
        if not text:
            continue

        strain_marker_match = re.search(r"\b(?:str\.?|strain)\s+(.+)$", text, flags=re.IGNORECASE)
        if strain_marker_match:
            return strain_marker_match.group(1).strip()

        species_open_match = re.match(
            r"^[A-Z][a-z]+\s+sp\.\s+([A-Za-z0-9._+-]+)$",
            text,
        )
        if species_open_match:
            return species_open_match.group(1).strip()

        collection_match = re.search(
            r"\b(ATCC|DSM|PCC|JCM|LMG|NCTC|NBRC|CCUG|CIP|KCTC|NCIMB)\s*-?\s*([A-Za-z0-9.-]+)\b",
            text,
            flags=re.IGNORECASE,
        )
        if collection_match:
            return f"{collection_match.group(1).upper()} {collection_match.group(2)}"

        binomial_tail = re.match(
            r"^([A-Z][a-z]+)\s+([a-z][a-z-]+)\s+([A-Za-z0-9._+-]+)$",
            text,
        )
        if binomial_tail:
            species_epithet = (binomial_tail.group(2) or "").strip().lower()
            if species_epithet in {
                "group",
                "lineage",
                "community",
                "bacterium",
                "bacteria",
                "species",
            }:
                continue
            tail = (binomial_tail.group(3) or "").strip()
            if tail and not tail.lower().startswith(QUALIFIER_PREFIXES):
                return tail

    return None


def load_community_taxa(community_yaml: Path) -> list[CommunityTaxon]:
    """Load taxon entries from a community YAML file."""
    with community_yaml.open() as handle:
        data = yaml.safe_load(handle) or {}

    community_name = str(data.get("name", community_yaml.stem))
    taxa: list[CommunityTaxon] = []

    for taxonomy_entry in data.get("taxonomy", []):
        if not isinstance(taxonomy_entry, dict):
            continue
        taxon_term = taxonomy_entry.get("taxon_term", {})
        if not isinstance(taxon_term, dict):
            continue
        term = taxon_term.get("term", {})
        if not isinstance(term, dict):
            term = {}

        preferred_term = str(taxon_term.get("preferred_term", "")).strip()
        taxon_label = str(term.get("label", "")).strip()
        taxon_id = str(term.get("id", "")).strip()
        strain_designation = taxonomy_entry.get("strain_designation")
        inferred_strain_name = infer_strain_name(strain_designation, preferred_term, taxon_label)
        has_explicit_strain = isinstance(strain_designation, dict) and bool(strain_designation)
        is_strain_taxon = has_explicit_strain or bool(inferred_strain_name)

        taxa.append(
            CommunityTaxon(
                community_file=community_yaml.name,
                community_name=community_name,
                preferred_term=preferred_term,
                taxon_label=taxon_label,
                taxon_id=taxon_id,
                ncbi_taxonomy_id=extract_ncbi_taxonomy_id(taxon_id),
                inferred_strain_name=inferred_strain_name,
                has_explicit_strain_designation=has_explicit_strain,
                is_strain_taxon=is_strain_taxon,
            )
        )

    return taxa


def strain_matches_proteome(local_strain_name: str, proteome: ProteomeSummary) -> bool:
    """Check whether a local strain string matches UniProt strain metadata."""
    if not local_strain_name:
        return True

    candidate_text = f"{proteome.strain} {proteome.scientific_name}".strip()
    if not candidate_text:
        return False

    local_normalized = _normalize_text(local_strain_name)
    candidate_normalized = _normalize_text(candidate_text)
    local_compact = re.sub(r"[^a-z0-9]+", "", local_strain_name.lower())
    candidate_compact = re.sub(r"[^a-z0-9]+", "", candidate_text.lower())
    if local_normalized and (
        local_normalized in candidate_normalized or candidate_normalized in local_normalized
    ):
        return True
    if local_compact and (local_compact in candidate_compact or candidate_compact in local_compact):
        return True

    local_tokens = _informative_tokens(local_strain_name)
    candidate_tokens = _informative_tokens(candidate_text)
    if not local_tokens or not candidate_tokens:
        return False

    overlap = local_tokens & candidate_tokens
    if not overlap:
        return False

    return (len(overlap) / len(local_tokens)) >= 0.5


def assess_taxon_coverage(
    taxon: CommunityTaxon,
    client: UniProtProteomeClient,
) -> StrainCoverageResult:
    """Assess whether a taxon is represented in UniProt reference proteomes."""
    if taxon.ncbi_taxonomy_id is None:
        return StrainCoverageResult(
            community_file=taxon.community_file,
            community_name=taxon.community_name,
            preferred_term=taxon.preferred_term,
            taxon_label=taxon.taxon_label,
            taxon_id=taxon.taxon_id,
            ncbi_taxonomy_id=None,
            inferred_strain_name=taxon.inferred_strain_name,
            is_strain_taxon=taxon.is_strain_taxon,
            represented=False,
            reason="Missing or invalid NCBITaxon identifier.",
            reference_proteomes=[],
            matched_proteomes=[],
        )

    reference_proteomes = client.search_reference_proteomes(taxon.ncbi_taxonomy_id)
    if not reference_proteomes:
        return StrainCoverageResult(
            community_file=taxon.community_file,
            community_name=taxon.community_name,
            preferred_term=taxon.preferred_term,
            taxon_label=taxon.taxon_label,
            taxon_id=taxon.taxon_id,
            ncbi_taxonomy_id=taxon.ncbi_taxonomy_id,
            inferred_strain_name=taxon.inferred_strain_name,
            is_strain_taxon=taxon.is_strain_taxon,
            represented=False,
            reason="No UniProt reference proteomes found for this taxonomy_id query.",
            reference_proteomes=[],
            matched_proteomes=[],
        )

    if taxon.inferred_strain_name:
        matched = [
            proteome
            for proteome in reference_proteomes
            if strain_matches_proteome(taxon.inferred_strain_name, proteome)
        ]
        represented = bool(matched)
        reason = (
            f"Matched {len(matched)} of {len(reference_proteomes)} reference proteomes to "
            f"strain '{taxon.inferred_strain_name}'."
        )
        return StrainCoverageResult(
            community_file=taxon.community_file,
            community_name=taxon.community_name,
            preferred_term=taxon.preferred_term,
            taxon_label=taxon.taxon_label,
            taxon_id=taxon.taxon_id,
            ncbi_taxonomy_id=taxon.ncbi_taxonomy_id,
            inferred_strain_name=taxon.inferred_strain_name,
            is_strain_taxon=taxon.is_strain_taxon,
            represented=represented,
            reason=reason,
            reference_proteomes=reference_proteomes,
            matched_proteomes=matched,
        )

    return StrainCoverageResult(
        community_file=taxon.community_file,
        community_name=taxon.community_name,
        preferred_term=taxon.preferred_term,
        taxon_label=taxon.taxon_label,
        taxon_id=taxon.taxon_id,
        ncbi_taxonomy_id=taxon.ncbi_taxonomy_id,
        inferred_strain_name=None,
        is_strain_taxon=taxon.is_strain_taxon,
        represented=True,
        reason=f"Found {len(reference_proteomes)} reference proteomes for taxonomy_id query.",
        reference_proteomes=reference_proteomes,
        matched_proteomes=reference_proteomes,
    )


def is_coarse_ncbi_taxonomy_id(taxonomy_id: int | None) -> bool:
    """Return True for coarse/root taxonomy assignments not suitable for strain mapping."""
    return taxonomy_id in COARSE_NCBI_TAXON_IDS if taxonomy_id is not None else False


def determine_strain_reference_proteome_coverage(
    community_path: Path,
    include_non_strains: bool = False,
    include_coarse_taxa: bool = False,
    client: UniProtProteomeClient | None = None,
) -> list[StrainCoverageResult]:
    """
    Determine UniProt reference proteome coverage for taxa in a community file/dir.

    Args:
        community_path: A single YAML file or a directory containing `*.yaml`.
        include_non_strains: Include entries without strain-like cues.
        include_coarse_taxa: Include coarse taxonomy IDs (e.g., NCBITaxon:2).
        client: Optional injected client for testing.
    """
    resolved_paths = _resolve_community_paths(community_path)
    if client is None:
        client = UniProtProteomeClient()

    results: list[StrainCoverageResult] = []
    for yaml_path in resolved_paths:
        for taxon in load_community_taxa(yaml_path):
            if not include_non_strains and not taxon.is_strain_taxon:
                continue
            if not include_coarse_taxa and is_coarse_ncbi_taxonomy_id(taxon.ncbi_taxonomy_id):
                continue
            results.append(assess_taxon_coverage(taxon, client))
    return results


def _resolve_community_paths(community_path: Path) -> list[Path]:
    """Resolve a file or directory into a sorted list of YAML files."""
    if community_path.is_file():
        return [community_path]
    if community_path.is_dir():
        return sorted(community_path.glob("*.yaml"))
    raise FileNotFoundError(f"Community path does not exist: {community_path}")


def _extract_next_link(link_header: str | None) -> str | None:
    """Extract the `next` pagination URL from HTTP Link header."""
    if not link_header:
        return None

    for link_part in link_header.split(","):
        section = link_part.strip()
        if 'rel="next"' not in section:
            continue
        if not section.startswith("<"):
            continue
        end_idx = section.find(">")
        if end_idx == -1:
            continue
        return section[1:end_idx]
    return None


def _normalize_text(value: str) -> str:
    """Normalize free text for robust matching."""
    return re.sub(r"[^a-z0-9]+", " ", value.lower()).strip()


def _informative_tokens(value: str) -> set[str]:
    """Tokenize text and drop generic strain words."""
    raw_tokens = re.findall(r"[a-z0-9]+", value.lower())
    fused_tokens: list[str] = []

    for left, right in zip(raw_tokens, raw_tokens[1:]):
        if (left.isalpha() and right.isdigit()) or (left.isdigit() and right.isalpha()):
            fused_tokens.append(f"{left}{right}")

    all_tokens = raw_tokens + fused_tokens
    return {token for token in all_tokens if len(token) >= 2 and token not in STRAIN_STOPWORDS}


def _print_console_report(results: list[StrainCoverageResult]) -> None:
    """Print a concise tab-separated report."""
    print(
        "represented\tcommunity_file\tpreferred_term\tinferred_strain\t"
        "ncbi_taxonomy_id\treference_proteomes\tmatched_proteomes\tmatched_upids"
    )
    for result in results:
        upids = [proteome.upid for proteome in result.matched_proteomes]
        print(
            "\t".join(
                [
                    "YES" if result.represented else "NO",
                    result.community_file,
                    result.preferred_term,
                    result.inferred_strain_name or "-",
                    str(result.ncbi_taxonomy_id or "-"),
                    str(len(result.reference_proteomes)),
                    str(len(result.matched_proteomes)),
                    ",".join(upids) if upids else "-",
                ]
            )
        )

    represented_count = sum(1 for result in results if result.represented)
    print("")
    print(f"Total entries checked: {len(results)}")
    print(f"Represented in UniProt reference proteomes: {represented_count}")
    print(f"Not represented: {len(results) - represented_count}")


def _write_json_output(results: list[StrainCoverageResult], output_path: Path) -> None:
    """Write JSON output file."""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w") as handle:
        json.dump([result.to_dict() for result in results], handle, indent=2)


def _write_tsv_output(results: list[StrainCoverageResult], output_path: Path) -> None:
    """Write TSV output file."""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = [
        "represented",
        "community_file",
        "community_name",
        "preferred_term",
        "taxon_label",
        "taxon_id",
        "ncbi_taxonomy_id",
        "inferred_strain_name",
        "reference_proteomes",
        "matched_proteomes",
        "matched_upids",
        "reason",
    ]
    with output_path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, delimiter="\t")
        writer.writeheader()
        for result in results:
            writer.writerow(
                {
                    "represented": result.represented,
                    "community_file": result.community_file,
                    "community_name": result.community_name,
                    "preferred_term": result.preferred_term,
                    "taxon_label": result.taxon_label,
                    "taxon_id": result.taxon_id,
                    "ncbi_taxonomy_id": result.ncbi_taxonomy_id or "",
                    "inferred_strain_name": result.inferred_strain_name or "",
                    "reference_proteomes": len(result.reference_proteomes),
                    "matched_proteomes": len(result.matched_proteomes),
                    "matched_upids": ",".join(p.upid for p in result.matched_proteomes),
                    "reason": result.reason,
                }
            )


def _extract_gtdb_id_from_result(result: StrainCoverageResult) -> str:
    """Extract GTDB identifier from available result fields if present."""
    if result.taxon_id.startswith("GTDB:"):
        return result.taxon_id

    gtdb_pattern = re.compile(r"\b(GTDB:[A-Za-z0-9_.-]+)\b", flags=re.IGNORECASE)
    for text in (result.preferred_term, result.taxon_label, result.reason):
        match = gtdb_pattern.search(text)
        if match:
            return match.group(1).upper()
    return ""


def _write_proteome_csv_output(results: list[StrainCoverageResult], output_path: Path) -> None:
    """
    Write a proteome-oriented CSV.

    Columns:
    - uniprot_proteome_id
    - taxon_id
    - gtdb_id
    - is_reference
    - proteome_type
    - communities_found_in
    """
    output_path.parent.mkdir(parents=True, exist_ok=True)

    aggregated: dict[tuple[str, str, str, str, str], set[str]] = {}

    for result in results:
        if not result.represented:
            continue
        gtdb_id = _extract_gtdb_id_from_result(result)
        for proteome in result.matched_proteomes:
            is_reference = str("reference" in proteome.proteome_type.lower()).lower()
            key = (
                proteome.upid,
                result.taxon_id,
                gtdb_id,
                is_reference,
                proteome.proteome_type,
            )
            aggregated.setdefault(key, set()).add(result.community_name)

    with output_path.open("w", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=[
                "uniprot_proteome_id",
                "taxon_id",
                "gtdb_id",
                "is_reference",
                "proteome_type",
                "communities_found_in",
            ],
        )
        writer.writeheader()
        for uniprot_proteome_id, taxon_id, gtdb_id, is_reference, proteome_type in sorted(
            aggregated
        ):
            communities = sorted(
                aggregated[(uniprot_proteome_id, taxon_id, gtdb_id, is_reference, proteome_type)]
            )
            writer.writerow(
                {
                    "uniprot_proteome_id": uniprot_proteome_id,
                    "taxon_id": taxon_id,
                    "gtdb_id": gtdb_id,
                    "is_reference": is_reference,
                    "proteome_type": proteome_type,
                    "communities_found_in": "; ".join(communities),
                }
            )


def _build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Determine which community strains are represented in UniProt " "reference proteomes."
        )
    )
    parser.add_argument(
        "community_path",
        nargs="?",
        default=Path("kb/communities"),
        type=Path,
        help="Community YAML file or directory (default: kb/communities).",
    )
    parser.add_argument(
        "--include-non-strains",
        action="store_true",
        help="Include taxonomy entries without strain-like cues.",
    )
    parser.add_argument(
        "--include-coarse-taxa",
        action="store_true",
        help="Include coarse taxonomy IDs (e.g., NCBITaxon:2) in checks.",
    )
    parser.add_argument(
        "--json-out",
        type=Path,
        help="Optional JSON output path.",
    )
    parser.add_argument(
        "--tsv-out",
        type=Path,
        help="Optional TSV output path.",
    )
    parser.add_argument(
        "--proteome-csv-out",
        type=Path,
        help="Optional proteome-oriented CSV output path.",
    )
    parser.add_argument(
        "--fail-on-missing",
        action="store_true",
        help="Exit with code 1 if any checked entry is not represented.",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    """CLI entrypoint."""
    args = _build_arg_parser().parse_args(argv)
    results = determine_strain_reference_proteome_coverage(
        community_path=args.community_path,
        include_non_strains=args.include_non_strains,
        include_coarse_taxa=args.include_coarse_taxa,
    )
    _print_console_report(results)

    if args.json_out:
        _write_json_output(results, args.json_out)
    if args.tsv_out:
        _write_tsv_output(results, args.tsv_out)
    if args.proteome_csv_out:
        _write_proteome_csv_output(results, args.proteome_csv_out)

    has_missing = any(not result.represented for result in results)
    if args.fail_on_missing and has_missing:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
