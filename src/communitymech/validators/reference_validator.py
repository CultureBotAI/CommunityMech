"""
Reference validation for CommunityMech.

Validates that evidence snippets match their cited sources.
"""

import yaml
from pathlib import Path
from typing import List, Tuple, Dict, Any
from difflib import SequenceMatcher

from communitymech.literature import LiteratureFetcher


class ReferenceValidator:
    """Validate evidence references in community YAML files."""

    def __init__(self, cache_dir: str = "references_cache"):
        self.fetcher = LiteratureFetcher(cache_dir=cache_dir)
        self.errors: List[str] = []
        self.warnings: List[str] = []

    def validate_yaml_file(self, yaml_path: Path) -> bool:
        """
        Validate all evidence references in a community YAML file.

        Args:
            yaml_path: Path to community YAML file

        Returns:
            True if all validations pass, False otherwise
        """
        self.errors = []
        self.warnings = []

        with open(yaml_path) as f:
            data = yaml.safe_load(f)

        # Collect all evidence items from the YAML
        evidence_items = self._collect_evidence(data)

        print(f"\nValidating {len(evidence_items)} evidence items from {yaml_path.name}...")

        for item in evidence_items:
            self._validate_evidence_item(item)

        # Report results
        if self.errors:
            print(f"\n❌ {len(self.errors)} validation errors:")
            for error in self.errors:
                print(f"  - {error}")

        if self.warnings:
            print(f"\n⚠️  {len(self.warnings)} warnings:")
            for warning in self.warnings:
                print(f"  - {warning}")

        if not self.errors and not self.warnings:
            print("✅ All references validated successfully!")

        return len(self.errors) == 0

    def _collect_evidence(self, data: dict) -> List[Dict[str, Any]]:
        """Recursively collect all evidence items from YAML data."""
        evidence_items = []

        def recurse(obj, path=""):
            if isinstance(obj, dict):
                if "evidence" in obj and isinstance(obj["evidence"], list):
                    for i, evidence in enumerate(obj["evidence"]):
                        evidence_items.append({
                            "path": f"{path}.evidence[{i}]",
                            "data": evidence
                        })
                for key, value in obj.items():
                    recurse(value, f"{path}.{key}" if path else key)
            elif isinstance(obj, list):
                for i, item in enumerate(obj):
                    recurse(item, f"{path}[{i}]")

        recurse(data)
        return evidence_items

    def _validate_evidence_item(self, item: Dict[str, Any]) -> None:
        """Validate a single evidence item."""
        evidence = item["data"]
        path = item["path"]

        reference = evidence.get("reference")
        snippet = evidence.get("snippet")

        if not reference:
            self.warnings.append(f"{path}: No reference provided")
            return

        if not snippet:
            self.warnings.append(f"{path}: No snippet provided for {reference}")
            return

        # Fetch the source
        abstract, pdf_url = self.fetcher.fetch_paper(reference)

        if not abstract:
            self.warnings.append(f"{path}: Could not fetch abstract for {reference}")
            return

        # Validate snippet appears in abstract
        is_valid = self.fetcher.validate_evidence_snippet(snippet, abstract)

        if not is_valid:
            # Calculate similarity for debugging
            snippet_normalized = " ".join(snippet.split())
            abstract_normalized = " ".join(abstract.split())
            ratio = SequenceMatcher(None, snippet_normalized.lower(), abstract_normalized.lower()).ratio()

            self.errors.append(
                f"{path}: Snippet not found in {reference} "
                f"(similarity: {ratio:.2%})\n"
                f"  Snippet: {snippet[:100]}..."
            )
        else:
            print(f"  ✓ {reference}: snippet validated")

    def get_cached_abstracts(self) -> Dict[str, str]:
        """Get all cached abstracts."""
        abstracts = {}
        for cache_file in self.fetcher.cache_dir.glob("pmid_*.txt"):
            pmid = cache_file.stem.replace("pmid_", "")
            abstracts[f"PMID:{pmid}"] = cache_file.read_text()
        return abstracts


def main():
    """CLI for reference validation."""
    import sys
    import argparse

    parser = argparse.ArgumentParser(description="Validate evidence references in community YAML files")
    parser.add_argument("yaml_file", help="Path to community YAML file")
    parser.add_argument("--cache-dir", default="references_cache", help="Directory for caching abstracts")

    args = parser.parse_args()

    validator = ReferenceValidator(cache_dir=args.cache_dir)
    yaml_path = Path(args.yaml_file)

    if not yaml_path.exists():
        print(f"Error: File not found: {yaml_path}")
        sys.exit(1)

    success = validator.validate_yaml_file(yaml_path)
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
