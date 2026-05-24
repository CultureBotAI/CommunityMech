"""LLM-assisted network repair orchestrator."""

import shutil
from datetime import datetime
from pathlib import Path
from typing import Any

import yaml

from communitymech.llm.anthropic_client import AnthropicClient
from communitymech.network.auditor import NetworkIntegrityAuditor
from communitymech.network.repair_strategies import StrategySelector
from communitymech.network.validators import SuggestionValidator


class LLMNetworkRepairer:
    """Main orchestrator for LLM-assisted network repair."""

    def __init__(
        self,
        llm_client: AnthropicClient | None = None,
        validator: SuggestionValidator | None = None,
        backup_dir: Path = Path(".backups"),
    ):
        """
        Initialize LLM network repairer.

        Args:
            llm_client: LLM client instance (if None, creates new AnthropicClient)
            validator: Suggestion validator (if None, creates new SuggestionValidator)
            backup_dir: Directory for backups
        """
        self.llm_client = llm_client or AnthropicClient()
        self.validator = validator or SuggestionValidator()
        self.backup_dir = Path(backup_dir)
        self.backup_dir.mkdir(exist_ok=True)

        # Track repair session
        self.repairs_attempted = 0
        self.repairs_succeeded = 0
        self.repairs_failed = 0

    def repair_community(
        self,
        yaml_path: Path,
        dry_run: bool = True,
        auto_approve: bool = False,
        max_repairs: int | None = None,
    ) -> dict[str, Any]:
        """
        Repair network integrity issues in a community file.

        Args:
            yaml_path: Path to community YAML file
            dry_run: If True, don't apply changes
            auto_approve: If True, auto-approve high-confidence suggestions
            max_repairs: Maximum number of repairs to attempt (None = unlimited)

        Returns:
            Summary dict with repair results
        """
        yaml_path = Path(yaml_path)

        # 1. Audit to find issues
        auditor = NetworkIntegrityAuditor()
        issues = auditor.audit_community(yaml_path)

        if not issues:
            return {
                "status": "success",
                "message": "No issues found",
                "issues": [],
                "repairs": [],
            }

        # 2. Load community data
        with open(yaml_path) as f:
            community_data = yaml.safe_load(f)

        # 3. Initialize strategy selector
        selector = StrategySelector(yaml_path, self.validator)

        # 4. Filter repairable issues
        repairable_issues = [i for i in issues if selector.can_repair(i)]

        if not repairable_issues:
            return {
                "status": "no_repairs",
                "message": f"Found {len(issues)} issues, but none are auto-repairable",
                "issues": issues,
                "repairs": [],
            }

        # 5. Apply repair limit if specified
        if max_repairs:
            repairable_issues = repairable_issues[:max_repairs]

        # 6. Generate and apply repairs
        repairs = []
        for issue in repairable_issues:
            repair_result = self._repair_single_issue(
                issue=issue,
                yaml_path=yaml_path,
                community_data=community_data,
                selector=selector,
                dry_run=dry_run,
                auto_approve=auto_approve,
            )
            repairs.append(repair_result)

        # 7. Build summary
        summary = {
            "status": "success" if repairs else "no_repairs",
            "file": str(yaml_path),
            "total_issues": len(issues),
            "repairable_issues": len(repairable_issues),
            "repairs_attempted": self.repairs_attempted,
            "repairs_succeeded": self.repairs_succeeded,
            "repairs_failed": self.repairs_failed,
            "dry_run": dry_run,
            "repairs": repairs,
            "cost": self.llm_client.get_cost_estimate() if self.llm_client else None,
        }

        return summary

    def _repair_single_issue(
        self,
        issue: dict[str, Any],
        yaml_path: Path,
        community_data: dict[str, Any],
        selector: StrategySelector,
        dry_run: bool,
        auto_approve: bool,
    ) -> dict[str, Any]:
        """
        Repair a single network integrity issue.

        Args:
            issue: Issue dict from auditor
            yaml_path: Path to community YAML
            community_data: Full community data
            selector: Strategy selector
            dry_run: If True, don't apply changes
            auto_approve: If True, auto-approve suggestions

        Returns:
            Repair result dict
        """
        self.repairs_attempted += 1

        try:
            # 1. Select strategy
            strategy = selector.select_strategy(issue)

            # 2. Build context
            context = strategy.build_context(issue)

            # 3. Generate suggestion with LLM
            prompt = strategy.get_prompt_template()
            suggestion = self.llm_client.generate_suggestion(
                prompt=prompt, context=context, temperature=0.1
            )

            # 4. Validate suggestion
            is_valid, errors = strategy.validate_suggestion(suggestion, community_data)

            # 5. Build repair result
            repair_result = {
                "issue": issue,
                "issue_summary": strategy.get_issue_summary(issue),
                "strategy": strategy.__class__.__name__,
                "suggestion": suggestion,
                "validation": {
                    "passed": is_valid,
                    "errors": [e.to_dict() for e in errors],
                },
                "applied": False,
            }

            # 6. Apply if valid and approved
            if is_valid:
                if auto_approve or not dry_run:
                    # Apply the suggestion
                    self._apply_suggestion(yaml_path, suggestion, community_data, dry_run)
                    repair_result["applied"] = not dry_run
                    self.repairs_succeeded += 1
                else:
                    repair_result["applied"] = False
                    repair_result["message"] = "Valid but requires manual approval"
            else:
                self.repairs_failed += 1
                repair_result["message"] = "Validation failed"

            return repair_result

        except Exception as e:
            self.repairs_failed += 1
            return {
                "issue": issue,
                "issue_summary": issue.get("message", "Unknown"),
                "error": str(e),
                "applied": False,
            }

    def _apply_suggestion(
        self,
        yaml_path: Path,
        suggestion: dict[str, Any],
        community_data: dict[str, Any],
        dry_run: bool,
    ):
        """
        Apply a validated suggestion to the community file.

        Args:
            yaml_path: Path to community YAML
            suggestion: Validated suggestion
            community_data: Current community data
            dry_run: If True, don't actually write
        """
        if dry_run:
            return  # Don't apply in dry run

        # Create backup
        backup_path = self._create_backup(yaml_path)

        try:
            # Add suggested interactions to community data
            suggested_interactions = suggestion.get("suggested_interactions", [])

            if "ecological_interactions" not in community_data:
                community_data["ecological_interactions"] = []

            community_data["ecological_interactions"].extend(suggested_interactions)

            # Write back
            with open(yaml_path, "w") as f:
                yaml.dump(
                    community_data, f, default_flow_style=False, sort_keys=False, allow_unicode=True
                )

        except Exception as e:
            # Restore from backup on failure
            if backup_path.exists():
                shutil.copy(backup_path, yaml_path)
            raise RuntimeError(f"Failed to apply suggestion: {e}") from e

    def _create_backup(self, yaml_path: Path) -> Path:
        """
        Create timestamped backup of community file.

        Args:
            yaml_path: Path to community YAML

        Returns:
            Path to backup file
        """
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_name = f"{yaml_path.stem}_{timestamp}.yaml"
        backup_path = self.backup_dir / backup_name

        shutil.copy(yaml_path, backup_path)
        return backup_path

    def list_backups(self, yaml_path: Path) -> list[Path]:
        """
        List available backups for a file.

        Args:
            yaml_path: Path to community YAML

        Returns:
            List of backup paths (newest first)
        """
        pattern = f"{yaml_path.stem}_*.yaml"
        backups = sorted(self.backup_dir.glob(pattern), reverse=True)
        return backups

    def restore_backup(self, backup_path: Path, target_path: Path):
        """
        Restore from a backup.

        Args:
            backup_path: Path to backup file
            target_path: Path to restore to
        """
        if not backup_path.exists():
            raise FileNotFoundError(f"Backup not found: {backup_path}")

        shutil.copy(backup_path, target_path)

    def get_repair_summary(self) -> dict[str, Any]:
        """
        Get summary of repair session.

        Returns:
            Summary dict with statistics and costs
        """
        cost = self.llm_client.get_cost_estimate() if self.llm_client else None

        return {
            "repairs_attempted": self.repairs_attempted,
            "repairs_succeeded": self.repairs_succeeded,
            "repairs_failed": self.repairs_failed,
            "success_rate": (
                self.repairs_succeeded / self.repairs_attempted
                if self.repairs_attempted > 0
                else 0.0
            ),
            "cost": cost,
        }

    def reset_session(self):
        """Reset repair session statistics."""
        self.repairs_attempted = 0
        self.repairs_succeeded = 0
        self.repairs_failed = 0
        if self.llm_client:
            self.llm_client.reset_cost_tracking()
