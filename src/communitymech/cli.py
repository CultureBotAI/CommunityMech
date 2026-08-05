"""CLI for CommunityMech: Microbial Community Knowledge Base Tools."""

import os
import sys
from pathlib import Path

import click
import yaml

from communitymech.network.auditor import (
    EXIT_CRASH,
    EXIT_ERRORS,
    EXIT_WARNINGS,
    NetworkIntegrityAuditor,
)
from communitymech.paths import DOCS, REPO_ROOT, REPORTS

# Try to import rich for beautiful output
try:
    from rich.console import Console
    from rich.panel import Panel
    from rich.prompt import Confirm
    from rich.syntax import Syntax
    from rich.table import Table

    RICH_AVAILABLE = True
except ImportError:
    RICH_AVAILABLE = False
    Console = None  # type: ignore[assignment,misc]


@click.group()
@click.version_option(version="0.1.0", prog_name="communitymech")
def cli():
    """CommunityMech: Microbial community knowledge base tools.

    Tools for auditing, validating, and maintaining microbial community
    interaction networks with evidence-based curation.
    """
    pass


@cli.command(name="audit-network")
@click.option(
    "--communities-dir",
    type=click.Path(exists=True, file_okay=False, dir_okay=True, path_type=Path),
    default="kb/communities",
    help="Directory containing community YAML files",
)
@click.option(
    "--check-only",
    is_flag=True,
    help="CI mode: no output; exit 3 on error-severity findings, 1 on warnings only",
)
@click.option(
    "--json",
    "output_json",
    is_flag=True,
    help="Output results as JSON",
)
@click.option(
    "--report",
    type=click.Path(dir_okay=False, path_type=Path),
    help="Write detailed report to file",
)
def audit_network(
    communities_dir: Path, check_only: bool, output_json: bool, report: Path | None = None
):
    """Audit network integrity for all community YAML files.

    Checks for:
    - NCBITaxon ID mismatches between taxonomy and interactions
    - Missing source_taxon or target_taxon in interactions
    - Interactions referencing taxa not in taxonomy section
    - Disconnected taxa (no interactions involving them)

    Examples:

        # Standard audit with human-readable output
        communitymech audit-network

        # CI mode - exit with error if issues found
        communitymech audit-network --check-only

        # JSON output for programmatic consumption
        communitymech audit-network --json

        # Write detailed report to file
        communitymech audit-network --report audit_results.txt
    """
    auditor = NetworkIntegrityAuditor(communities_dir=communities_dir)

    try:
        # `quiet` under --json: the human report and the JSON both went to
        # stdout, so `audit-network --json > out.json` wrote a file that was not
        # JSON, which is why the workflow's JSON artifact was dropped (#273).
        issues = auditor.audit_all(check_only=check_only, quiet=output_json)

        if output_json:
            print(auditor.to_json())

        if report:
            auditor.write_report(output_path=report)

        # Exit code carries *which kind* of finding, not merely whether there
        # were any: EXIT_ERRORS for a record that contradicts itself, which CI
        # gates on, versus EXIT_WARNINGS for one that is merely incomplete,
        # which it only reports. check_only has already exited by this point.
        if issues and not check_only:
            sys.exit(EXIT_ERRORS if auditor.count_by_severity()["error"] else EXIT_WARNINGS)

    except Exception as e:
        click.echo(f"❌ Error during audit: {e}", err=True)
        sys.exit(EXIT_CRASH)


@cli.command(name="repair-network")
@click.argument("file", type=click.Path(exists=True, dir_okay=False, path_type=Path))
@click.option(
    "--auto-approve",
    is_flag=True,
    help="Automatically approve high-confidence suggestions",
)
@click.option(
    "--dry-run",
    is_flag=True,
    help="Show suggestions without applying changes",
)
@click.option(
    "--max-repairs",
    type=int,
    default=None,
    help="Maximum number of repairs to attempt",
)
def repair_network(file: Path, auto_approve: bool, dry_run: bool, max_repairs: int):
    """LLM-assisted network repair for a single community file.

    Uses large language models to suggest biologically plausible repairs
    for network integrity issues with interactive human-in-the-loop approval.

    Examples:

        # Interactive repair with human approval
        communitymech repair-network kb/communities/Richmond_Mine_AMD_Biofilm.yaml

        # Dry run - show suggestions only
        communitymech repair-network kb/communities/Test.yaml --dry-run

        # Auto-approve high-confidence suggestions
        communitymech repair-network kb/communities/Test.yaml --auto-approve

    Note: Requires ANTHROPIC_API_KEY environment variable to be set.
    """
    # Check for API key
    if not os.getenv("ANTHROPIC_API_KEY"):
        click.echo("❌ Error: ANTHROPIC_API_KEY environment variable not set", err=True)
        click.echo("\n💡 Set your API key:")
        click.echo("   export ANTHROPIC_API_KEY=sk-ant-your-key")
        click.echo("\n   Get your key from: https://console.anthropic.com/")
        sys.exit(1)

    # Import repair components (lazy import to avoid errors if anthropic not installed)
    try:
        from communitymech.network.llm_repair import LLMNetworkRepairer
    except ImportError as e:
        click.echo(f"❌ Error: Missing dependencies: {e}", err=True)
        click.echo("\n💡 Install LLM dependencies:")
        click.echo("   uv sync --all-extras")
        sys.exit(1)

    # Initialize console
    console = Console() if RICH_AVAILABLE else None

    try:
        # Initialize repairer
        repairer = LLMNetworkRepairer()

        # Run repair with interactive UI
        if RICH_AVAILABLE and console is not None and not auto_approve and not dry_run:
            result = _interactive_repair(console, repairer, file, max_repairs)
        else:
            result = _non_interactive_repair(repairer, file, auto_approve, dry_run, max_repairs)

        # Display summary
        if RICH_AVAILABLE and console is not None:
            _display_repair_summary(console, result)
        else:
            _display_repair_summary_plain(result)

    except Exception as e:
        click.echo(f"❌ Error during repair: {e}", err=True)
        if "--verbose" in sys.argv:
            import traceback

            traceback.print_exc()
        sys.exit(1)


def _interactive_repair(console: Console, repairer, file: Path, max_repairs: int):
    """Interactive repair with rich UI."""
    console.print(f"\n[bold blue]🔧 Repairing:[/bold blue] {file}\n")

    # Audit first
    with console.status("[bold yellow]Auditing network integrity...", spinner="dots"):
        auditor = NetworkIntegrityAuditor()
        issues = auditor.audit_community(file)

    if not issues:
        console.print("[green]✅ No issues found![/green]\n")
        return {"status": "success", "message": "No issues found", "repairs": []}

    # Display issues
    console.print(f"[yellow]Found {len(issues)} issues[/yellow]\n")

    # Show issues table
    table = Table(title="Network Integrity Issues")
    table.add_column("Type", style="cyan")
    table.add_column("Details", style="magenta")

    for issue in issues[:10]:  # Show first 10
        table.add_row(issue.get("type"), issue.get("message", ""))

    console.print(table)

    if len(issues) > 10:
        console.print(f"\n[dim]... and {len(issues) - 10} more issues[/dim]")

    # Load community data
    with open(file) as f:
        community_data = yaml.safe_load(f)

    # Process each issue
    from communitymech.network.repair_strategies import StrategySelector

    selector = StrategySelector(file, repairer.validator)
    repairable_issues = [i for i in issues if selector.can_repair(i)]

    if not repairable_issues:
        console.print(
            f"\n[yellow]⚠️  None of the {len(issues)} issues are auto-repairable[/yellow]"
        )
        return {"status": "no_repairs", "repairs": []}

    console.print(
        f"\n[green]{len(repairable_issues)} issues can be repaired with LLM assistance[/green]\n"
    )

    if max_repairs:
        repairable_issues = repairable_issues[:max_repairs]

    repairs = []
    for idx, issue in enumerate(repairable_issues):
        console.print(f"\n[bold]Issue {idx+1}/{len(repairable_issues)}[/bold]")
        console.print(f"[yellow]{issue.get('type')}:[/yellow] {issue.get('message')}")

        # Generate suggestion
        strategy = selector.select_strategy(issue)
        context = strategy.build_context(issue)
        prompt = strategy.get_prompt_template()

        with console.status("[bold yellow]Generating LLM suggestion...", spinner="dots"):
            suggestion = repairer.llm_client.generate_suggestion(prompt, context, temperature=0.1)

        # Display suggestion
        if "suggested_interactions" in suggestion:
            for int_suggestion in suggestion["suggested_interactions"]:
                console.print("\n[bold green]💡 Suggested Repair:[/bold green]")

                yaml_str = yaml.dump(int_suggestion, default_flow_style=False, sort_keys=False)
                syntax = Syntax(yaml_str, "yaml", theme="monokai", line_numbers=False)
                console.print(Panel(syntax, title="Suggested Interaction", border_style="green"))

        # Validate
        is_valid, errors = strategy.validate_suggestion(suggestion, community_data)

        if is_valid:
            console.print("[green]✅ Validation: PASSED[/green]")
        else:
            console.print("[red]❌ Validation: FAILED[/red]")
            for error in errors:
                if error.severity == "error":
                    console.print(f"  [red]✗[/red] {error.message}")
                else:
                    console.print(f"  [yellow]⚠[/yellow] {error.message}")

        # Ask for approval
        if is_valid:
            if Confirm.ask("\n[bold]Apply this repair?[/bold]", default=False):
                # Apply
                if "ecological_interactions" not in community_data:
                    community_data["ecological_interactions"] = []
                community_data["ecological_interactions"].extend(
                    suggestion.get("suggested_interactions", [])
                )

                # Create backup and write
                backup_path = repairer._create_backup(file)
                with open(file, "w") as f:
                    yaml.dump(
                        community_data,
                        f,
                        default_flow_style=False,
                        sort_keys=False,
                        allow_unicode=True,
                    )

                console.print(f"[green]✓ Applied[/green] (backup: {backup_path.name})")
                repairs.append({"issue": issue, "applied": True, "valid": True})
            else:
                console.print("[dim]⊘ Skipped[/dim]")
                repairs.append({"issue": issue, "applied": False, "valid": True})
        else:
            console.print("[red]⊘ Skipped (validation failed)[/red]")
            repairs.append({"issue": issue, "applied": False, "valid": False})

    return {
        "status": "success",
        "repairs": repairs,
        "cost": repairer.llm_client.get_cost_estimate(),
    }


def _non_interactive_repair(
    repairer, file: Path, auto_approve: bool, dry_run: bool, max_repairs: int
):
    """Non-interactive repair (batch mode or auto-approve)."""
    return repairer.repair_community(
        yaml_path=file, dry_run=dry_run, auto_approve=auto_approve, max_repairs=max_repairs
    )


def _display_repair_summary(console: Console, result: dict):
    """Display repair summary with rich formatting."""
    console.print("\n[bold]📊 Repair Summary[/bold]\n")

    repairs = result.get("repairs", [])
    applied = sum(1 for r in repairs if r.get("applied"))
    valid = sum(1 for r in repairs if r.get("valid"))

    table = Table()
    table.add_column("Metric", style="cyan")
    table.add_column("Value", style="magenta")

    table.add_row("Total Repairs", str(len(repairs)))
    table.add_row("Applied", str(applied))
    table.add_row("Valid", str(valid))

    if "cost" in result and result["cost"]:
        cost = result["cost"]
        table.add_row("API Calls", str(cost.get("api_calls", 0)))
        table.add_row("Total Cost", f"${cost.get('total_cost_usd', 0):.4f}")

    console.print(table)
    console.print()


def _display_repair_summary_plain(result: dict):
    """Display repair summary without rich formatting."""
    click.echo("\n📊 Repair Summary\n")

    repairs = result.get("repairs", [])
    applied = sum(1 for r in repairs if r.get("applied"))

    click.echo(f"Total Repairs: {len(repairs)}")
    click.echo(f"Applied: {applied}")

    if "cost" in result and result["cost"]:
        cost = result["cost"]
        click.echo(f"API Calls: {cost.get('api_calls', 0)}")
        click.echo(f"Total Cost: ${cost.get('total_cost_usd', 0):.4f}")

    click.echo()


@cli.command(name="repair-network-batch")
@click.option(
    "--report-only",
    is_flag=True,
    help="Generate repair suggestions report without applying",
)
@click.option(
    "--apply-from",
    type=click.Path(exists=True, dir_okay=False, path_type=Path),
    help="Apply repairs from a previously generated report",
)
@click.option(
    "--output",
    type=click.Path(dir_okay=False, path_type=Path),
    default=str(REPORTS / "network_repair_suggestions.yaml"),
    help="Output path for report",
)
@click.option(
    "--max-communities",
    type=int,
    default=None,
    help="Maximum number of communities to process",
)
@click.option(
    "--max-issues",
    type=int,
    default=None,
    help="Maximum issues per community",
)
def repair_network_batch(
    report_only: bool,
    apply_from: Path,
    output: Path,
    max_communities: int,
    max_issues: int,
):
    """Batch repair with review mode for multiple communities.

    Generate repair suggestions for all communities with issues,
    allowing for offline review before application.

    Examples:

        # Generate repair suggestions report
        communitymech repair-network-batch --report-only

        # Generate with limits
        communitymech repair-network-batch --report-only --max-communities 10

        # Apply repairs from previously reviewed report
        communitymech repair-network-batch --apply-from reports/repairs.yaml

    Note: Requires ANTHROPIC_API_KEY environment variable to be set for --report-only.
    """
    if apply_from:
        # Apply mode - no API key needed
        _apply_batch_report(apply_from)
    elif report_only:
        # Generate mode - needs API key
        if not os.getenv("ANTHROPIC_API_KEY"):
            click.echo("❌ Error: ANTHROPIC_API_KEY environment variable not set", err=True)
            click.echo("\n💡 Set your API key:")
            click.echo("   export ANTHROPIC_API_KEY=sk-ant-your-key")
            sys.exit(1)

        _generate_batch_report(output, max_communities, max_issues)
    else:
        click.echo("❌ Error: Must specify either --report-only or --apply-from", err=True)
        click.echo("\n💡 Usage:")
        click.echo("   communitymech repair-network-batch --report-only")
        click.echo("   communitymech repair-network-batch --apply-from report.yaml")
        sys.exit(1)


def _generate_batch_report(output_path: Path, max_communities: int, max_issues: int):
    """Generate batch repair report."""
    try:
        from communitymech.network.batch_reporter import BatchReporter
    except ImportError as e:
        click.echo(f"❌ Error: Missing dependencies: {e}", err=True)
        sys.exit(1)

    if RICH_AVAILABLE:
        console = Console()
        console.print("\n[bold blue]📋 Generating Batch Repair Report[/bold blue]\n")

        with console.status("[bold yellow]Processing communities...", spinner="dots"):
            reporter = BatchReporter()
            result = reporter.generate_report(
                output_path=output_path,
                max_communities=max_communities,
                max_issues_per_community=max_issues,
            )

        console.print(f"[green]✅ Report generated:[/green] {result['report_path']}\n")

        # Display summary table
        table = Table(title="Batch Report Summary")
        table.add_column("Metric", style="cyan")
        table.add_column("Value", style="magenta")

        table.add_row("Communities Processed", str(result["communities_processed"]))
        table.add_row("Communities with Issues", str(result["communities_with_issues"]))
        table.add_row("Total Suggestions", str(result["total_suggestions"]))

        if result["cost"]:
            cost = result["cost"]
            table.add_row("API Calls", str(cost.get("api_calls", 0)))
            table.add_row("Total Cost", f"${cost.get('total_cost_usd', 0):.4f}")

        console.print(table)

        console.print("\n[bold]Next Steps:[/bold]")
        console.print(f"1. Review the report: {result['report_path']}")
        console.print("2. Set 'approved: true' for suggestions you want to apply")
        console.print(
            "3. Apply approved: communitymech repair-network-batch "
            f"--apply-from {result['report_path']}"
        )
        console.print()

    else:
        click.echo("\n📋 Generating Batch Repair Report\n")
        reporter = BatchReporter()
        result = reporter.generate_report(
            output_path=output_path,
            max_communities=max_communities,
            max_issues_per_community=max_issues,
        )

        click.echo(f"✅ Report generated: {result['report_path']}")
        click.echo(f"\nCommunities Processed: {result['communities_processed']}")
        click.echo(f"Communities with Issues: {result['communities_with_issues']}")
        click.echo(f"Total Suggestions: {result['total_suggestions']}")

        if result["cost"]:
            cost = result["cost"]
            click.echo(f"API Calls: {cost.get('api_calls', 0)}")
            click.echo(f"Total Cost: ${cost.get('total_cost_usd', 0):.4f}")

        click.echo("\nNext Steps:")
        click.echo(f"1. Review: {result['report_path']}")
        click.echo("2. Set 'approved: true' for suggestions to apply")
        click.echo(
            f"3. Apply: communitymech repair-network-batch --apply-from {result['report_path']}\n"
        )


def _apply_batch_report(report_path: Path):
    """Apply approved suggestions from batch report."""
    try:
        from communitymech.network.batch_reporter import BatchReporter
    except ImportError as e:
        click.echo(f"❌ Error: Missing dependencies: {e}", err=True)
        sys.exit(1)

    if RICH_AVAILABLE:
        console = Console()
        console.print("\n[bold blue]🔧 Applying Batch Repairs[/bold blue]")
        console.print(f"[dim]From: {report_path}[/dim]\n")

        with console.status("[bold yellow]Applying approved suggestions...", spinner="dots"):
            reporter = BatchReporter()
            result = reporter.apply_approved_suggestions(report_path)

        console.print("[bold]Results:[/bold]\n")

        table = Table()
        table.add_column("Status", style="cyan")
        table.add_column("Count", style="magenta")

        table.add_row("✅ Applied", str(result["applied"]))
        table.add_row("⊘ Skipped", str(result["skipped"]))
        table.add_row("❌ Errors", str(result["errors"]))

        console.print(table)
        console.print()

        if result["applied"] > 0:
            console.print("[green]✓ Suggestions applied successfully[/green]")
            console.print("[dim]Backups saved to .backups/[/dim]\n")

    else:
        click.echo(f"\n🔧 Applying Batch Repairs from: {report_path}\n")

        reporter = BatchReporter()
        result = reporter.apply_approved_suggestions(report_path)

        click.echo("Results:")
        click.echo(f"  Applied: {result['applied']}")
        click.echo(f"  Skipped: {result['skipped']}")
        click.echo(f"  Errors: {result['errors']}")

        if result["applied"] > 0:
            click.echo("\n✓ Suggestions applied successfully")
            click.echo("Backups saved to .backups/\n")


@cli.command(name="generate-umap")
@click.option(
    "--communities-dir",
    type=click.Path(exists=True, file_okay=False, dir_okay=True, path_type=Path),
    default="kb/communities",
    help="Directory containing community YAML files",
)
@click.option(
    "--embeddings-path",
    type=click.Path(exists=True, file_okay=True, dir_okay=False, path_type=Path),
    default="data/embeddings/DeepWalkSkipGramEnsmallen_degreenorm_embedding_512_v3_2026-06-26_12_55_27.tsv.gz",
    help="Path to KG-Microbe embeddings TSV.gz file",
)
@click.option(
    "--output",
    type=click.Path(dir_okay=False, path_type=Path),
    # Repo-anchored so the default lands in one predictable place. The target is
    # git-tracked, so this makes a run from elsewhere rewrite the committed file
    # rather than leave a stray one — deliberate for a committed artifact (#407).
    default=str(DOCS / "community_umap.html"),
    help="Output HTML path",
)
@click.option(
    "--cache-dir",
    type=click.Path(file_okay=False, dir_okay=True, path_type=Path),
    default=str(REPO_ROOT / ".umap_cache"),
    help="Directory for embedding cache",
)
@click.option(
    "--force-reload",
    is_flag=True,
    help="Force reload embeddings (ignore cache)",
)
@click.option(
    "--method",
    type=click.Choice(["pacmap", "umap", "sfdp"]),
    default="pacmap",
    help="2D reduction method (pacmap default; umap; or sfdp graph layout)",
)
@click.option(
    "--n-neighbors",
    type=int,
    default=15,
    help="UMAP n_neighbors parameter (controls local vs global structure)",
)
@click.option(
    "--min-dist",
    type=float,
    default=0.1,
    help="UMAP min_dist parameter (minimum distance between points)",
)
@click.option(
    "--min-coverage",
    type=float,
    default=0.5,
    help="Minimum fraction of taxa that must have embeddings (0.0-1.0)",
)
@click.option(
    "--include-hosts/--exclude-hosts",
    default=False,
    help="Include non-microbial host taxa in representations (default: exclude)",
)
def generate_umap(
    communities_dir: Path,
    embeddings_path: Path,
    output: Path,
    cache_dir: Path,
    force_reload: bool,
    method: str,
    n_neighbors: int,
    min_dist: float,
    min_coverage: float,
    include_hosts: bool,
):
    """Generate interactive UMAP visualization of community embedding space.

    Creates a 2D UMAP projection of all communities based on their taxonomic
    composition embeddings from KG-Microbe. The visualization is an interactive
    HTML scatterplot published to docs/ for GitHub Pages.

    Examples:

        # Generate with default settings
        communitymech generate-umap

        # Custom UMAP parameters
        communitymech generate-umap --n-neighbors 20 --min-dist 0.05

        # Force reload embeddings (ignore cache)
        communitymech generate-umap --force-reload

        # Custom output location
        communitymech generate-umap --output docs/custom_umap.html
    """
    try:
        from communitymech.visualization.umap_generator import UMAPVisualizationGenerator
    except ImportError as e:
        click.echo(f"❌ Error: Missing dependencies: {e}", err=True)
        click.echo("\n💡 Install required dependencies:")
        click.echo("   uv sync")
        sys.exit(1)

    try:
        generator = UMAPVisualizationGenerator()
        generator.generate(
            communities_dir=str(communities_dir),
            embeddings_path=str(embeddings_path),
            output_path=str(output),
            cache_dir=str(cache_dir),
            force_reload=force_reload,
            method=method,
            n_neighbors=n_neighbors,
            min_dist=min_dist,
            min_coverage=min_coverage,
            exclude_hosts=not include_hosts,
        )

    except Exception as e:
        click.echo(f"❌ Error during UMAP generation: {e}", err=True)
        if "--verbose" in sys.argv or "-v" in sys.argv:
            import traceback

            traceback.print_exc()
        sys.exit(1)


def main():
    """Entry point for CLI."""
    cli()


if __name__ == "__main__":
    main()
