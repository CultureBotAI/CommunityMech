"""
Network integrity auditor for microbial community YAML files.

Checks for:
1. NCBITaxon ID mismatches between taxonomy and interactions
2. Missing source_taxon or target_taxon in interactions
3. Interactions referencing taxa not in taxonomy section
4. Disconnected taxa (no interactions involving them)
"""

import json
import sys
from collections import defaultdict
from enum import Enum
from pathlib import Path
from typing import Dict, List, Optional, Set

import yaml


class IssueType(str, Enum):
    """Types of network integrity issues."""

    ID_MISMATCH = "ID_MISMATCH"
    MISSING_SOURCE = "MISSING_SOURCE"
    UNKNOWN_SOURCE = "UNKNOWN_SOURCE"
    UNKNOWN_TARGET = "UNKNOWN_TARGET"
    DISCONNECTED = "DISCONNECTED"


class NetworkIntegrityAuditor:
    """Audit community YAML files for network data integrity issues."""

    def __init__(self, communities_dir: Path = Path("kb/communities")):
        self.communities_dir = Path(communities_dir)
        self.issues: Dict[str, List[Dict]] = defaultdict(list)

    def audit_all(self, check_only: bool = False) -> Dict[str, List[Dict]]:
        """
        Audit all community YAML files.

        Args:
            check_only: If True, exit with code 1 if issues found (CI mode)

        Returns:
            Dictionary mapping community names to their issues
        """
        yaml_files = sorted(self.communities_dir.glob("*.yaml"))

        if not check_only:
            print(
                f"\n🔍 Auditing {len(yaml_files)} communities for network integrity issues...\n"
            )

        total_issues = 0
        communities_with_issues = 0

        for yaml_file in yaml_files:
            issues = self.audit_community(yaml_file)
            if issues:
                self.issues[yaml_file.stem] = issues
                communities_with_issues += 1
                total_issues += len(issues)
                if not check_only:
                    self.report_community_issues(yaml_file.stem, issues)

        if not check_only:
            print(f"\n{'='*80}")
            print(
                f"Summary: {communities_with_issues}/{len(yaml_files)} communities have issues"
            )
            print(f"Total issues found: {total_issues}")
            print(f"{'='*80}\n")

        # In check-only mode, exit with code 1 if issues found
        if check_only and total_issues > 0:
            print(f"❌ Found {total_issues} network integrity issues", file=sys.stderr)
            sys.exit(1)

        return self.issues

    def audit_community(self, yaml_path: Path) -> List[Dict]:
        """
        Audit a single community file.

        Args:
            yaml_path: Path to community YAML file

        Returns:
            List of issue dictionaries
        """
        with open(yaml_path) as f:
            data = yaml.safe_load(f)

        issues = []

        # Build taxonomy lookup by preferred_term
        taxonomy_by_term = {}
        for taxon in data.get("taxonomy", []):
            term = taxon.get("taxon_term", {})
            preferred = term.get("preferred_term") or term.get("term", {}).get("label")
            taxon_id = term.get("term", {}).get("id")

            if preferred:
                taxonomy_by_term[preferred] = {
                    "id": taxon_id,
                    "label": term.get("term", {}).get("label"),
                    "taxon_data": taxon,  # Store full taxon data for context
                }

        # Check each interaction
        interactions = data.get("ecological_interactions", [])

        # Track which taxa are connected
        connected_taxa = set()

        for idx, interaction in enumerate(interactions):
            int_name = interaction.get("name", f"Interaction {idx+1}")

            # Check source_taxon
            source = interaction.get("source_taxon")
            if not source:
                issues.append(
                    {
                        "type": IssueType.MISSING_SOURCE,
                        "interaction": int_name,
                        "interaction_index": idx,
                        "message": "Interaction has no source_taxon",
                    }
                )
            else:
                source_term = source.get("preferred_term") or source.get("term", {}).get(
                    "label"
                )
                source_id = source.get("term", {}).get("id")

                if source_term not in taxonomy_by_term:
                    issues.append(
                        {
                            "type": IssueType.UNKNOWN_SOURCE,
                            "interaction": int_name,
                            "interaction_index": idx,
                            "taxon": source_term,
                            "message": f"Source taxon '{source_term}' not found in taxonomy section",
                        }
                    )
                else:
                    connected_taxa.add(source_term)
                    # Check ID mismatch
                    expected_id = taxonomy_by_term[source_term]["id"]
                    if source_id != expected_id:
                        issues.append(
                            {
                                "type": IssueType.ID_MISMATCH,
                                "interaction": int_name,
                                "interaction_index": idx,
                                "taxon": source_term,
                                "role": "source",
                                "expected_id": expected_id,
                                "actual_id": source_id,
                                "message": f"Source '{source_term}' has ID {source_id}, expected {expected_id}",
                            }
                        )

            # Check target_taxon (optional but if present should be valid)
            target = interaction.get("target_taxon")
            if target:
                target_term = target.get("preferred_term") or target.get("term", {}).get(
                    "label"
                )
                target_id = target.get("term", {}).get("id")

                if target_term not in taxonomy_by_term:
                    issues.append(
                        {
                            "type": IssueType.UNKNOWN_TARGET,
                            "interaction": int_name,
                            "interaction_index": idx,
                            "taxon": target_term,
                            "message": f"Target taxon '{target_term}' not found in taxonomy section",
                        }
                    )
                else:
                    connected_taxa.add(target_term)
                    # Check ID mismatch
                    expected_id = taxonomy_by_term[target_term]["id"]
                    if target_id != expected_id:
                        issues.append(
                            {
                                "type": IssueType.ID_MISMATCH,
                                "interaction": int_name,
                                "interaction_index": idx,
                                "taxon": target_term,
                                "role": "target",
                                "expected_id": expected_id,
                                "actual_id": target_id,
                                "message": f"Target '{target_term}' has ID {target_id}, expected {expected_id}",
                            }
                        )

        # Check for disconnected taxa
        all_taxa = set(taxonomy_by_term.keys())
        disconnected = all_taxa - connected_taxa

        if disconnected and interactions:  # Only flag if there ARE interactions
            for taxon in sorted(disconnected):
                taxon_data = taxonomy_by_term[taxon]["taxon_data"]
                issues.append(
                    {
                        "type": IssueType.DISCONNECTED,
                        "taxon": taxon,
                        "taxon_id": taxonomy_by_term[taxon]["id"],
                        "taxon_data": taxon_data,  # Include for context building
                        "message": f"Taxon '{taxon}' has no interactions",
                    }
                )

        return issues

    def report_community_issues(self, community_name: str, issues: List[Dict]):
        """
        Print issues for a community.

        Args:
            community_name: Name of the community
            issues: List of issue dictionaries
        """
        print(f"\n{'─'*80}")
        print(f"📋 {community_name}")
        print(f"{'─'*80}")

        # Group by type
        by_type = defaultdict(list)
        for issue in issues:
            by_type[issue["type"]].append(issue)

        # Report each type
        for issue_type in [
            IssueType.ID_MISMATCH,
            IssueType.MISSING_SOURCE,
            IssueType.UNKNOWN_SOURCE,
            IssueType.UNKNOWN_TARGET,
            IssueType.DISCONNECTED,
        ]:
            if issue_type in by_type:
                print(f"\n  {issue_type.value}:")
                for issue in by_type[issue_type]:
                    if issue_type == IssueType.ID_MISMATCH:
                        print(f"    • [{issue['interaction']}] {issue['role']}: {issue['taxon']}")
                        print(
                            f"      Expected: {issue['expected_id']}, Found: {issue['actual_id']}"
                        )
                    elif issue_type == IssueType.DISCONNECTED:
                        print(f"    • {issue['taxon']} ({issue['taxon_id']})")
                    else:
                        print(f"    • [{issue.get('interaction', 'N/A')}] {issue['message']}")

        print(f"\n  Total issues: {len(issues)}")

    def to_json(self) -> str:
        """
        Export issues as JSON for programmatic consumption.

        Returns:
            JSON string of all issues
        """
        return json.dumps(self.issues, indent=2, default=str)

    def write_report(self, output_path: Path = Path("network_integrity_audit.txt")):
        """
        Write detailed report to file.

        Args:
            output_path: Path to write report
        """
        with open(output_path, "w") as f:
            f.write("Network Integrity Audit Report\n")
            f.write("=" * 80 + "\n\n")

            for community, community_issues in sorted(self.issues.items()):
                f.write(f"\n{community}\n")
                f.write("-" * 80 + "\n")
                for issue in community_issues:
                    f.write(f"  {issue['type']}: {issue['message']}\n")
                    if issue["type"] == "ID_MISMATCH":
                        f.write(
                            f"    Expected: {issue['expected_id']}, Found: {issue['actual_id']}\n"
                        )
                f.write(f"\nTotal: {len(community_issues)} issues\n")

        print(f"\n✅ Detailed report written to {output_path}\n")

    def get_community_data(self, community_path: Path) -> Dict:
        """
        Load community data from YAML file.

        Args:
            community_path: Path to community YAML file

        Returns:
            Community data dictionary
        """
        with open(community_path) as f:
            return yaml.safe_load(f)

    def get_taxonomy_lookup(self, community_data: Dict) -> Dict[str, Dict]:
        """
        Build taxonomy lookup from community data.

        Args:
            community_data: Community data dictionary

        Returns:
            Dictionary mapping taxon names to their data
        """
        taxonomy_by_term = {}
        for taxon in community_data.get("taxonomy", []):
            term = taxon.get("taxon_term", {})
            preferred = term.get("preferred_term") or term.get("term", {}).get("label")

            if preferred:
                taxonomy_by_term[preferred] = {
                    "id": term.get("term", {}).get("id"),
                    "label": term.get("term", {}).get("label"),
                    "taxon_data": taxon,
                }

        return taxonomy_by_term
