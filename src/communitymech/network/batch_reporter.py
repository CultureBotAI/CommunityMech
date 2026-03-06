"""Batch report generation for network repair suggestions."""

from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional

import yaml

from communitymech.llm.anthropic_client import AnthropicClient
from communitymech.network.auditor import NetworkIntegrityAuditor
from communitymech.network.repair_strategies import StrategySelector
from communitymech.network.validators import SuggestionValidator


class BatchReporter:
    """Generate repair suggestion reports for offline review."""

    def __init__(
        self,
        llm_client: Optional[AnthropicClient] = None,
        validator: Optional[SuggestionValidator] = None,
        communities_dir: Path = Path("kb/communities"),
        parallel: bool = True,
        max_workers: int = 4,
    ):
        """
        Initialize batch reporter.

        Args:
            llm_client: LLM client instance
            validator: Suggestion validator instance
            communities_dir: Directory containing community YAML files
            parallel: Enable parallel processing of communities
            max_workers: Max parallel workers (default: 4)
        """
        self.llm_client = llm_client or AnthropicClient()
        self.validator = validator or SuggestionValidator()
        self.communities_dir = Path(communities_dir)
        self.auditor = NetworkIntegrityAuditor(communities_dir=communities_dir)
        self.parallel = parallel
        self.max_workers = max_workers

    def generate_report(
        self,
        output_path: Path = Path("reports/network_repair_suggestions.yaml"),
        max_communities: Optional[int] = None,
        max_issues_per_community: Optional[int] = None,
    ) -> Dict[str, Any]:
        """
        Generate repair suggestions report for all communities.

        Args:
            output_path: Path to write report YAML file
            max_communities: Limit number of communities to process
            max_issues_per_community: Limit issues per community

        Returns:
            Summary dict with report metadata
        """
        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)

        report = {
            "generated_at": datetime.now().isoformat(),
            "generator": "CommunityMech Batch Reporter",
            "total_communities": 0,
            "communities_with_issues": 0,
            "total_suggestions": 0,
            "communities": [],
        }

        # Get all community files
        yaml_files = sorted(self.communities_dir.glob("*.yaml"))

        if max_communities:
            yaml_files = yaml_files[:max_communities]

        report["total_communities"] = len(yaml_files)

        # Process communities (parallel or sequential)
        if self.parallel and len(yaml_files) > 1:
            community_reports = self._process_communities_parallel(
                yaml_files, max_issues_per_community
            )
        else:
            community_reports = [
                self._process_community(f, max_issues_per_community) for f in yaml_files
            ]

        # Aggregate results
        for community_report in community_reports:
            if community_report["suggestions"]:
                report["communities_with_issues"] += 1
                report["total_suggestions"] += len(community_report["suggestions"])
                report["communities"].append(community_report)

        # Add cost estimate
        report["cost_estimate"] = self.llm_client.get_cost_estimate()

        # Write report
        with open(output_path, "w") as f:
            yaml.dump(report, f, default_flow_style=False, sort_keys=False, allow_unicode=True)

        return {
            "report_path": str(output_path),
            "communities_processed": len(yaml_files),
            "communities_with_issues": report["communities_with_issues"],
            "total_suggestions": report["total_suggestions"],
            "cost": report["cost_estimate"],
        }

    def _process_communities_parallel(
        self, yaml_files: List[Path], max_issues: Optional[int] = None
    ) -> List[Dict[str, Any]]:
        """
        Process multiple communities in parallel.

        Args:
            yaml_files: List of community YAML files
            max_issues: Max issues per community

        Returns:
            List of community reports
        """
        reports = []

        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            # Submit all tasks
            future_to_file = {
                executor.submit(self._process_community, yaml_file, max_issues): yaml_file
                for yaml_file in yaml_files
            }

            # Collect results as they complete
            for future in as_completed(future_to_file):
                try:
                    report = future.result()
                    reports.append(report)
                except Exception as e:
                    yaml_file = future_to_file[future]
                    # Return error report
                    reports.append(
                        {
                            "file": str(yaml_file),
                            "name": yaml_file.stem,
                            "error": str(e),
                            "issues_count": 0,
                            "suggestions": [],
                        }
                    )

        return reports

    def _process_community(
        self, yaml_path: Path, max_issues: Optional[int] = None
    ) -> Dict[str, Any]:
        """
        Process a single community and generate repair suggestions.

        Args:
            yaml_path: Path to community YAML file
            max_issues: Maximum issues to process

        Returns:
            Community report dict
        """
        # Audit for issues
        issues = self.auditor.audit_community(yaml_path)

        if not issues:
            return {
                "file": str(yaml_path),
                "name": yaml_path.stem,
                "issues_count": 0,
                "suggestions": [],
            }

        # Load community data
        with open(yaml_path) as f:
            community_data = yaml.safe_load(f)

        # Initialize strategy selector
        selector = StrategySelector(yaml_path, self.validator)

        # Filter repairable issues
        repairable_issues = [i for i in issues if selector.can_repair(i)]

        if max_issues:
            repairable_issues = repairable_issues[:max_issues]

        # Generate suggestions
        suggestions = []
        for issue in repairable_issues:
            suggestion_entry = self._generate_suggestion(
                issue, yaml_path, community_data, selector
            )
            suggestions.append(suggestion_entry)

        return {
            "file": str(yaml_path),
            "name": yaml_path.stem,
            "issues_count": len(issues),
            "repairable_count": len(repairable_issues),
            "suggestions": suggestions,
        }

    def _generate_suggestion(
        self,
        issue: Dict[str, Any],
        yaml_path: Path,
        community_data: Dict[str, Any],
        selector: StrategySelector,
    ) -> Dict[str, Any]:
        """
        Generate a single repair suggestion.

        Args:
            issue: Issue dict from auditor
            yaml_path: Path to community file
            community_data: Community data
            selector: Strategy selector

        Returns:
            Suggestion entry for report
        """
        try:
            # Select strategy
            strategy = selector.select_strategy(issue)

            # Build context
            context = strategy.build_context(issue)

            # Generate suggestion
            prompt = strategy.get_prompt_template()
            suggestion = self.llm_client.generate_suggestion(
                prompt=prompt, context=context, temperature=0.1
            )

            # Validate
            is_valid, errors = strategy.validate_suggestion(suggestion, community_data)

            return {
                "issue": {
                    "type": issue.get("type"),
                    "summary": strategy.get_issue_summary(issue),
                    "details": issue,
                },
                "suggestion": suggestion,
                "validation": {
                    "passed": is_valid,
                    "errors": [
                        {
                            "layer": e.layer,
                            "field": e.field,
                            "message": e.message,
                            "severity": e.severity,
                        }
                        for e in errors
                    ],
                },
                "strategy": strategy.__class__.__name__,
                "approved": False,  # User must set to true to approve
                "notes": "",  # User can add notes
            }

        except Exception as e:
            return {
                "issue": {
                    "type": issue.get("type"),
                    "summary": issue.get("message", "Unknown"),
                    "details": issue,
                },
                "error": str(e),
                "approved": False,
            }

    def apply_approved_suggestions(
        self, report_path: Path, backup_dir: Path = Path(".backups")
    ) -> Dict[str, Any]:
        """
        Apply suggestions from a report that have been approved.

        Args:
            report_path: Path to report YAML file
            backup_dir: Directory for backups

        Returns:
            Summary of applied suggestions
        """
        backup_dir = Path(backup_dir)
        backup_dir.mkdir(exist_ok=True)

        # Load report
        with open(report_path) as f:
            report = yaml.safe_load(f)

        applied_count = 0
        skipped_count = 0
        error_count = 0

        # Process each community
        for community in report.get("communities", []):
            yaml_path = Path(community["file"])

            if not yaml_path.exists():
                error_count += 1
                continue

            # Load community data
            with open(yaml_path) as f:
                community_data = yaml.safe_load(f)

            # Apply approved suggestions
            for suggestion_entry in community["suggestions"]:
                if not suggestion_entry.get("approved", False):
                    skipped_count += 1
                    continue

                if "error" in suggestion_entry:
                    error_count += 1
                    continue

                if not suggestion_entry["validation"]["passed"]:
                    skipped_count += 1
                    continue

                try:
                    # Create backup
                    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                    backup_path = backup_dir / f"{yaml_path.stem}_{timestamp}.yaml"
                    import shutil
                    shutil.copy(yaml_path, backup_path)

                    # Apply suggestion
                    suggestion = suggestion_entry["suggestion"]
                    if "ecological_interactions" not in community_data:
                        community_data["ecological_interactions"] = []

                    community_data["ecological_interactions"].extend(
                        suggestion.get("suggested_interactions", [])
                    )

                    # Write back
                    with open(yaml_path, "w") as f:
                        yaml.dump(
                            community_data,
                            f,
                            default_flow_style=False,
                            sort_keys=False,
                            allow_unicode=True,
                        )

                    applied_count += 1

                except Exception as e:
                    error_count += 1

        return {
            "applied": applied_count,
            "skipped": skipped_count,
            "errors": error_count,
        }
