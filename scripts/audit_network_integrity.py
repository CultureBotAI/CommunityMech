#!/usr/bin/env python3
"""
Audit all community YAML files for network data integrity issues.

Checks for:
1. NCBITaxon ID mismatches between taxonomy and interactions
2. Missing source_taxon or target_taxon in interactions
3. Interactions referencing taxa not in taxonomy section
4. Disconnected taxa (no interactions involving them)
"""

import yaml
from pathlib import Path
from collections import defaultdict
from typing import Dict, List, Set, Tuple


class NetworkIntegrityAuditor:
    def __init__(self, communities_dir: Path = Path("kb/communities")):
        self.communities_dir = communities_dir
        self.issues = defaultdict(list)

    def audit_all(self):
        """Audit all community YAML files."""
        yaml_files = sorted(self.communities_dir.glob("*.yaml"))

        print(f"\n🔍 Auditing {len(yaml_files)} communities for network integrity issues...\n")

        total_issues = 0
        communities_with_issues = 0

        for yaml_file in yaml_files:
            issues = self.audit_community(yaml_file)
            if issues:
                communities_with_issues += 1
                total_issues += len(issues)
                self.report_community_issues(yaml_file.stem, issues)

        print(f"\n{'='*80}")
        print(f"Summary: {communities_with_issues}/{len(yaml_files)} communities have issues")
        print(f"Total issues found: {total_issues}")
        print(f"{'='*80}\n")

        return self.issues

    def audit_community(self, yaml_path: Path) -> List[Dict]:
        """Audit a single community file."""
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
                issues.append({
                    "type": "MISSING_SOURCE",
                    "interaction": int_name,
                    "message": "Interaction has no source_taxon"
                })
            else:
                source_term = source.get("preferred_term") or source.get("term", {}).get("label")
                source_id = source.get("term", {}).get("id")

                if source_term not in taxonomy_by_term:
                    issues.append({
                        "type": "UNKNOWN_SOURCE",
                        "interaction": int_name,
                        "taxon": source_term,
                        "message": f"Source taxon '{source_term}' not found in taxonomy section"
                    })
                else:
                    connected_taxa.add(source_term)
                    # Check ID mismatch
                    expected_id = taxonomy_by_term[source_term]["id"]
                    if source_id != expected_id:
                        issues.append({
                            "type": "ID_MISMATCH",
                            "interaction": int_name,
                            "taxon": source_term,
                            "role": "source",
                            "expected_id": expected_id,
                            "actual_id": source_id,
                            "message": f"Source '{source_term}' has ID {source_id}, expected {expected_id}"
                        })

            # Check target_taxon (optional but if present should be valid)
            target = interaction.get("target_taxon")
            if target:
                target_term = target.get("preferred_term") or target.get("term", {}).get("label")
                target_id = target.get("term", {}).get("id")

                if target_term not in taxonomy_by_term:
                    issues.append({
                        "type": "UNKNOWN_TARGET",
                        "interaction": int_name,
                        "taxon": target_term,
                        "message": f"Target taxon '{target_term}' not found in taxonomy section"
                    })
                else:
                    connected_taxa.add(target_term)
                    # Check ID mismatch
                    expected_id = taxonomy_by_term[target_term]["id"]
                    if target_id != expected_id:
                        issues.append({
                            "type": "ID_MISMATCH",
                            "interaction": int_name,
                            "taxon": target_term,
                            "role": "target",
                            "expected_id": expected_id,
                            "actual_id": target_id,
                            "message": f"Target '{target_term}' has ID {target_id}, expected {expected_id}"
                        })

        # Check for disconnected taxa
        all_taxa = set(taxonomy_by_term.keys())
        disconnected = all_taxa - connected_taxa

        if disconnected and interactions:  # Only flag if there ARE interactions
            for taxon in sorted(disconnected):
                issues.append({
                    "type": "DISCONNECTED",
                    "taxon": taxon,
                    "message": f"Taxon '{taxon}' has no interactions"
                })

        return issues

    def report_community_issues(self, community_name: str, issues: List[Dict]):
        """Print issues for a community."""
        print(f"\n{'─'*80}")
        print(f"📋 {community_name}")
        print(f"{'─'*80}")

        # Group by type
        by_type = defaultdict(list)
        for issue in issues:
            by_type[issue["type"]].append(issue)

        # Report each type
        for issue_type in ["ID_MISMATCH", "MISSING_SOURCE", "UNKNOWN_SOURCE", "UNKNOWN_TARGET", "DISCONNECTED"]:
            if issue_type in by_type:
                print(f"\n  {issue_type}:")
                for issue in by_type[issue_type]:
                    if issue_type == "ID_MISMATCH":
                        print(f"    • [{issue['interaction']}] {issue['role']}: {issue['taxon']}")
                        print(f"      Expected: {issue['expected_id']}, Found: {issue['actual_id']}")
                    elif issue_type == "DISCONNECTED":
                        print(f"    • {issue['taxon']}")
                    else:
                        print(f"    • [{issue.get('interaction', 'N/A')}] {issue['message']}")

        print(f"\n  Total issues: {len(issues)}")


def main():
    auditor = NetworkIntegrityAuditor()
    issues = auditor.audit_all()

    # Write detailed report to file
    report_path = Path("network_integrity_audit.txt")
    with open(report_path, "w") as f:
        f.write("Network Integrity Audit Report\n")
        f.write("="*80 + "\n\n")

        for community, community_issues in sorted(issues.items()):
            f.write(f"\n{community}\n")
            f.write("-"*80 + "\n")
            for issue in community_issues:
                f.write(f"  {issue['type']}: {issue['message']}\n")
                if issue['type'] == 'ID_MISMATCH':
                    f.write(f"    Expected: {issue['expected_id']}, Found: {issue['actual_id']}\n")
            f.write(f"\nTotal: {len(community_issues)} issues\n")

    print(f"\n✅ Detailed report written to {report_path}\n")


if __name__ == "__main__":
    main()
