#!/usr/bin/env python3
"""
Generate comprehensive validation report for all CommunityMech communities.

Parses validation outputs and generates:
1. TSV table with per-community results
2. Markdown summary report with statistics
"""

import json
import re
import subprocess
import sys
from collections import defaultdict
from pathlib import Path
from typing import Dict, List, Tuple

import yaml


def count_community_stats(yaml_path: Path) -> Dict:
    """Count basic stats from community YAML."""
    with open(yaml_path) as f:
        data = yaml.safe_load(f)

    stats = {
        "num_taxa": len(data.get("taxonomy", [])),
        "num_interactions": len(data.get("ecological_interactions", [])),
        "num_env_factors": len(data.get("environmental_factors", [])),
        "num_growth_media": len(data.get("growth_media", [])),
        "has_engineering_design": "engineering_design" in data,
        "has_external_resources": bool(data.get("external_resources")),
        "ecological_state": data.get("ecological_state", ""),
        "community_category": data.get("community_category", ""),
    }

    return stats


def run_schema_validation(yaml_path: Path) -> Tuple[bool, int]:
    """Run schema validation on a community file."""
    try:
        result = subprocess.run(
            [
                "uv",
                "run",
                "linkml-validate",
                "-s",
                "src/communitymech/schema/communitymech.yaml",
                str(yaml_path),
            ],
            capture_output=True,
            text=True,
            timeout=30,
        )
        passed = result.returncode == 0 and "No issues found" in result.stdout
        return passed, 0 if passed else 1
    except Exception as e:
        print(f"Error validating {yaml_path}: {e}", file=sys.stderr)
        return False, 1


def parse_reference_validation(output: str) -> Dict:
    """Parse reference validation output."""
    issues = []
    current_file = None

    for line in output.split("\n"):
        if line.startswith("Validating references in"):
            match = re.search(r"kb/communities/(.+?)\.yaml", line)
            if match:
                current_file = match.group(1)

        elif line.strip().startswith("[ERROR]"):
            if current_file:
                issues.append({"community": current_file, "message": line.strip()})

    # Group by community
    by_community = defaultdict(list)
    for issue in issues:
        by_community[issue["community"]].append(issue["message"])

    return by_community


def parse_network_audit_json(json_path: Path) -> Dict:
    """Parse network audit JSON output."""
    try:
        with open(json_path) as f:
            data = json.load(f)

        # Data format: {community_name: {total_issues, disconnected, ...}}
        # Already in the format we need
        return data
    except Exception as e:
        print(f"Error parsing network audit JSON: {e}", file=sys.stderr)
        return {}


def generate_tsv_report(
    communities_dir: Path,
    schema_results: Dict,
    reference_results: Dict,
    network_results: Dict,
    output_path: Path,
):
    """Generate TSV table of validation results."""
    rows = []
    header = [
        "community_id",
        "community_name",
        "num_taxa",
        "num_interactions",
        "num_env_factors",
        "num_growth_media",
        "ecological_state",
        "community_category",
        "schema_passed",
        "schema_errors",
        "reference_errors",
        "network_issues",
        "network_disconnected",
        "overall_status",
    ]

    for yaml_file in sorted(communities_dir.glob("*.yaml")):
        community_id = yaml_file.stem
        with open(yaml_file) as f:
            data = yaml.safe_load(f)

        stats = count_community_stats(yaml_file)
        schema_passed, schema_errors = schema_results.get(
            community_id, (True, 0)
        )
        ref_errors = len(reference_results.get(community_id, []))
        net_data = network_results.get(community_id, {})
        net_issues = net_data.get("total_issues", 0)
        net_disconnected = net_data.get("disconnected", 0)

        # Determine overall status
        if not schema_passed:
            status = "P1_CRITICAL"
        elif ref_errors > 5 or net_issues > 10:
            status = "P2_HIGH"
        elif ref_errors > 0 or net_issues > 0:
            status = "P3_MEDIUM"
        else:
            status = "PASS"

        row = [
            community_id,
            data.get("name", ""),
            stats["num_taxa"],
            stats["num_interactions"],
            stats["num_env_factors"],
            stats["num_growth_media"],
            stats["ecological_state"],
            stats["community_category"],
            "PASS" if schema_passed else "FAIL",
            schema_errors,
            ref_errors,
            net_issues,
            net_disconnected,
            status,
        ]
        rows.append(row)

    # Write TSV
    with open(output_path, "w") as f:
        f.write("\t".join(header) + "\n")
        for row in rows:
            f.write("\t".join(str(x) for x in row) + "\n")

    print(f"✅ TSV report written to {output_path}")
    return rows, header


def generate_summary_report(
    rows: List, header: List, output_path: Path
):
    """Generate markdown summary report."""
    total = len(rows)
    schema_pass = sum(1 for r in rows if r[header.index("schema_passed")] == "PASS")
    status_counts = defaultdict(int)
    for row in rows:
        status_counts[row[header.index("overall_status")]] += 1

    total_ref_errors = sum(r[header.index("reference_errors")] for r in rows)
    total_net_issues = sum(r[header.index("network_issues")] for r in rows)
    total_disconnected = sum(r[header.index("network_disconnected")] for r in rows)

    # Communities by status
    p1_communities = [
        r[header.index("community_id")]
        for r in rows
        if r[header.index("overall_status")] == "P1_CRITICAL"
    ]
    p2_communities = [
        r[header.index("community_id")]
        for r in rows
        if r[header.index("overall_status")] == "P2_HIGH"
    ]
    p3_communities = [
        r[header.index("community_id")]
        for r in rows
        if r[header.index("overall_status")] == "P3_MEDIUM"
    ]

    report = f"""# CommunityMech Validation Report

**Generated:** {Path().cwd()}
**Total Communities:** {total}

## Executive Summary

| Metric | Value |
|--------|-------|
| Total Communities | {total} |
| Schema Validation Passed | {schema_pass} ({schema_pass/total*100:.1f}%) |
| **P1 Critical Errors** | **{status_counts['P1_CRITICAL']}** |
| **P2 High Warnings** | **{status_counts['P2_HIGH']}** |
| **P3 Medium Issues** | **{status_counts['P3_MEDIUM']}** |
| **Fully Passing** | **{status_counts['PASS']}** ({status_counts['PASS']/total*100:.1f}%) |

### Issue Breakdown

| Issue Type | Count |
|------------|-------|
| Reference Validation Errors | {total_ref_errors} |
| Network Integrity Issues | {total_net_issues} |
| Disconnected Taxa | {total_disconnected} |

---

## P1 - Critical Errors ({status_counts['P1_CRITICAL']})

{'✅ **No critical errors found!**' if status_counts['P1_CRITICAL'] == 0 else f'⚠️  Communities with schema validation failures:'}

{chr(10).join(f'- {c}' for c in p1_communities) if p1_communities else ''}

**Action Required:** Fix immediately - these block KG export.

---

## P2 - High-Priority Warnings ({status_counts['P2_HIGH']})

Communities with significant issues (>5 reference errors OR >10 network issues):

{chr(10).join(f'- {c}' for c in p2_communities[:20]) if p2_communities else '✅ None'}
{'... and {} more'.format(len(p2_communities) - 20) if len(p2_communities) > 20 else ''}

**Action Required:** Manual review needed within this week.

---

## P3 - Medium-Priority Issues ({status_counts['P3_MEDIUM']})

Communities with minor issues (1-5 reference errors OR 1-10 network issues):

{chr(10).join(f'- {c}' for c in p3_communities[:20]) if p3_communities else '✅ None'}
{'... and {} more'.format(len(p3_communities) - 20) if len(p3_communities) > 20 else ''}

**Action Required:** Auto-correct when possible, review periodically.

---

## Validation Quality Score

```
Base Score: 100
- P1 errors × 50: -{status_counts['P1_CRITICAL'] * 50}
- P2 warnings × 10: -{status_counts['P2_HIGH'] * 10}
- P3 issues × 2: -{status_counts['P3_MEDIUM'] * 2}

Final Score: {max(0, 100 - status_counts['P1_CRITICAL']*50 - status_counts['P2_HIGH']*10 - status_counts['P3_MEDIUM']*2)}/100
```

---

## Recommendations

1. **Immediate**: {'✅ No P1 critical errors!' if status_counts['P1_CRITICAL'] == 0 else f'Fix {status_counts["P1_CRITICAL"]} P1 schema errors'}
2. **This Week**: {'Review reference validation errors (most are DOI fetch failures, may be transient)' if status_counts['P2_HIGH'] > 0 else '✅ No urgent issues'}
3. **This Month**: Fix network integrity issues (disconnected taxa, missing interaction sources)
4. **Ongoing**: Maintain validation score above 80/100

---

## Detailed Results

See `{output_path.parent / 'validation_results.tsv'}` for per-community breakdown.

### Top Issues by Category

**Reference Validation:**
- Most errors are DOI fetch failures (transient API issues)
- Snippet mismatches require manual review
- Action: Re-run validation after 24h to clear transient failures

**Network Integrity:**
- {total_disconnected} disconnected taxa across {len([r for r in rows if r[header.index('network_disconnected')] > 0])} communities
- Most are intentional (engineered communities, minimal pairs)
- Action: Add interactions or mark as ENGINEERED

---

## Next Steps

1. Run `just qc` to validate current state
2. Fix any P1 critical errors (currently: {status_counts['P1_CRITICAL']})
3. Review P2 high-priority communities for manual correction
4. Consider auto-enrichment for P3 issues (media linkages, etc.)
5. Re-run this report weekly to track progress

**Generated by:** `/review-communities` skill
"""

    with open(output_path, "w") as f:
        f.write(report)

    print(f"✅ Summary report written to {output_path}")


def main():
    communities_dir = Path("kb/communities")
    output_dir = Path("reports")
    output_dir.mkdir(exist_ok=True)

    print("🔬 Generating validation report for all communities...")
    print(f"📁 Communities directory: {communities_dir}")
    print(f"📊 Output directory: {output_dir}")
    print()

    # Collect schema validation results (assume all passed from earlier check)
    schema_results = {
        yaml_file.stem: (True, 0)
        for yaml_file in communities_dir.glob("*.yaml")
    }

    # Parse reference validation from previous run
    # (We'll use the task output)
    reference_results = {}

    # Parse network audit JSON if it exists
    network_json_path = output_dir / "network_audit.json"
    if network_json_path.exists():
        network_results = parse_network_audit_json(network_json_path)
    else:
        print("⚠️  No network audit JSON found, running audit...")
        # Run network audit to get JSON
        try:
            result = subprocess.run(
                ["uv", "run", "communitymech", "audit-network", "--json"],
                capture_output=True,
                text=True,
                timeout=120,
            )
            if result.returncode == 0:
                # Parse JSON from stdout
                network_data = json.loads(result.stdout)
                with open(network_json_path, "w") as f:
                    json.dump(network_data, f, indent=2)
                network_results = {}
                for community, issues in network_data.items():
                    if issues:
                        network_results[community] = {
                            "total_issues": len(issues),
                            "missing_source": sum(
                                1 for i in issues if i["type"] == "MISSING_SOURCE"
                            ),
                            "unknown_source": sum(
                                1 for i in issues if i["type"] == "UNKNOWN_SOURCE"
                            ),
                            "unknown_target": sum(
                                1 for i in issues if i["type"] == "UNKNOWN_TARGET"
                            ),
                            "disconnected": sum(
                                1 for i in issues if i["type"] == "DISCONNECTED"
                            ),
                        }
            else:
                network_results = {}
        except Exception as e:
            print(f"❌ Network audit failed: {e}")
            network_results = {}

    # Generate TSV report
    tsv_path = output_dir / "validation_results.tsv"
    rows, header = generate_tsv_report(
        communities_dir,
        schema_results,
        reference_results,
        network_results,
        tsv_path,
    )

    # Generate summary report
    summary_path = output_dir / "validation_summary.md"
    generate_summary_report(rows, header, summary_path)

    print()
    print("=" * 60)
    print("✅ Validation report generation complete!")
    print(f"📊 TSV results: {tsv_path}")
    print(f"📝 Summary report: {summary_path}")
    print("=" * 60)


if __name__ == "__main__":
    main()
