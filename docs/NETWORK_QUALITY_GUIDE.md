# Network Quality Check Guide

## Quick Start

### Check Network Integrity

```bash
# Audit all communities
just audit-network

# CI mode (exit 1 if issues)
just check-network-quality

# Generate JSON report
just audit-network-json > report.json

# Write detailed report to file
just audit-network-report audit.txt
```

### Understanding Issues

The auditor checks for 5 types of network integrity issues:

1. **ID_MISMATCH** - NCBITaxon IDs don't match between taxonomy and interactions
   ```yaml
   # taxonomy section has:
   NCBITaxon:562  # Escherichia coli

   # but interaction references:
   NCBITaxon:9999  # Wrong ID!
   ```

2. **MISSING_SOURCE** - Interaction has no `source_taxon` field
   ```yaml
   ecological_interactions:
     - name: "Some interaction"
       # source_taxon: MISSING!
       target_taxon: ...
   ```

3. **UNKNOWN_SOURCE** - Source taxon not found in taxonomy section
   ```yaml
   ecological_interactions:
     - source_taxon:
         preferred_term: "Mystery bacterium"  # Not in taxonomy!
   ```

4. **UNKNOWN_TARGET** - Target taxon not found in taxonomy section
   ```yaml
   ecological_interactions:
     - target_taxon:
         preferred_term: "Unknown archaea"  # Not in taxonomy!
   ```

5. **DISCONNECTED** - Taxon in taxonomy but not involved in any interactions
   ```yaml
   taxonomy:
     - taxon_term:
         preferred_term: "Lonely bacterium"  # No interactions!
   ```

## Interpreting Output

### Standard Output

```
🔍 Auditing 76 communities for network integrity issues...

────────────────────────────────────────────────────────────────────────────────
📋 Richmond_Mine_AMD_Biofilm
────────────────────────────────────────────────────────────────────────────────

  ID_MISMATCH:
    • [Iron Oxidation] source: Leptospirillum group II
      Expected: NCBITaxon:1228, Found: NCBITaxon:9999

  DISCONNECTED:
    • ARMAN (NCBITaxon:123456)
    • Thermoplasmatales archaeon (NCBITaxon:234567)

  Total issues: 3

================================================================================
Summary: 1/76 communities have issues
Total issues found: 3
================================================================================
```

### JSON Output

```json
{
  "Richmond_Mine_AMD_Biofilm": [
    {
      "type": "ID_MISMATCH",
      "interaction": "Iron Oxidation",
      "taxon": "Leptospirillum group II",
      "role": "source",
      "expected_id": "NCBITaxon:1228",
      "actual_id": "NCBITaxon:9999"
    },
    {
      "type": "DISCONNECTED",
      "taxon": "ARMAN",
      "taxon_id": "NCBITaxon:123456"
    }
  ]
}
```

## Fixing Issues

### Automated Fixes (ID_MISMATCH only)

For simple ID mismatches, the old `scripts/fix_network_integrity.py` can automatically fix:

```bash
# Dry run
python scripts/fix_network_integrity.py

# Apply fixes
python scripts/fix_network_integrity.py --apply
```

### Manual Fixes Required

For **DISCONNECTED**, **UNKNOWN_SOURCE**, **UNKNOWN_TARGET**, and **MISSING_SOURCE** issues, manual curation is required:

**Example: Fixing a disconnected taxon**

```yaml
# Before: Taxon exists but has no interactions
taxonomy:
  - taxon_term:
      preferred_term: "Ferroplasma acidarmanus"
      term:
        id: "NCBITaxon:55206"
        label: "Ferroplasma acidarmanus"

ecological_interactions: []  # Empty!

# After: Add biologically plausible interaction
ecological_interactions:
  - name: "Iron Cycling Partnership"
    interaction_type: "MUTUALISM"
    description: "F. acidarmanus reduces Fe(III) to Fe(II), which is then oxidized by Leptospirillum"
    source_taxon:
      preferred_term: "Ferroplasma acidarmanus"
      term:
        id: "NCBITaxon:55206"
        label: "Ferroplasma acidarmanus"
    target_taxon:
      preferred_term: "Leptospirillum group II"
      term:
        id: "NCBITaxon:1228"
        label: "Leptospirillum group II"
    metabolites_exchanged:
      - metabolite_term:
          id: "CHEBI:29033"
          label: "iron(2+)"
        direction: "source_to_target"
    evidence:
      - reference: "PMID:15066799"
        supports: "SUPPORT"
        evidence_source: "LITERATURE"
        snippet: "Ferroplasma acidarmanus was capable of growing by reduction of Fe(III)..."
```

### LLM-Assisted Repair (Coming in Phase 2-4)

Future versions will support LLM-assisted suggestions:

```bash
# Interactive repair with human approval
communitymech repair-network kb/communities/Richmond_Mine_AMD_Biofilm.yaml

# Generate suggestions report for batch review
communitymech repair-network-batch --report-only

# Apply pre-approved repairs
communitymech repair-network-batch --apply-from reports/approved_repairs.yaml
```

## CI/CD Integration

### GitHub Actions

The `.github/workflows/network-quality.yml` workflow automatically:

1. Runs on PR changes to `kb/communities/*.yaml`
2. Audits network integrity
3. Fails PR if issues detected
4. Uploads detailed reports as artifacts
5. Comments on PR with issue summary

### Pre-commit Hook (Optional)

Add to `.git/hooks/pre-commit`:

```bash
#!/bin/bash
just check-network-quality
```

## Best Practices

### 1. Check Before Committing

```bash
# Always audit before committing
just audit-network

# Or use CI mode to fail on issues
just check-network-quality
```

### 2. Fix Issues Promptly

- **ID mismatches**: Run automated fix script
- **Disconnected taxa**: Add biologically plausible interactions with evidence
- **Unknown taxa**: Add missing taxa to taxonomy or fix typos

### 3. Document Rationale

When adding interactions to fix disconnected taxa, always:
- Use peer-reviewed literature (PMID preferred)
- Include metabolites with CHEBI IDs
- Include processes with GO IDs
- Extract exact snippets from abstracts

### 4. Validate After Fixes

```bash
# After manual fixes
just validate kb/communities/YourCommunity.yaml
just validate-references kb/communities/YourCommunity.yaml
just audit-network
```

## Python API

```python
from pathlib import Path
from communitymech.network.auditor import NetworkIntegrityAuditor

# Create auditor
auditor = NetworkIntegrityAuditor(communities_dir=Path("kb/communities"))

# Audit all communities
issues = auditor.audit_all()

# Audit single community
issues = auditor.audit_community(Path("kb/communities/Test.yaml"))

# Check specific issue types
for issue in issues:
    if issue["type"] == "DISCONNECTED":
        taxon = issue["taxon"]
        taxon_id = issue["taxon_id"]
        print(f"Disconnected: {taxon} ({taxon_id})")

# Export as JSON
import json
with open("audit.json", "w") as f:
    f.write(auditor.to_json())

# Get community data and taxonomy lookup (for context building)
data = auditor.get_community_data(Path("kb/communities/Test.yaml"))
taxonomy = auditor.get_taxonomy_lookup(data)
```

## Troubleshooting

### Issue: "No module named communitymech.network"

**Solution**: Reinstall package
```bash
uv sync --all-extras
```

### Issue: "Exit code 1" in CI

**Meaning**: Network integrity issues detected

**Solution**:
1. Check CI logs or PR comment for issue details
2. Download artifact reports for full details
3. Fix issues manually or with scripts
4. Re-run CI

### Issue: Tests failing

**Solution**:
```bash
uv run pytest tests/test_network_auditor.py -v
# Fix any failures
uv sync --all-extras  # Reinstall if needed
```

## Advanced Usage

### Custom Communities Directory

```bash
communitymech audit-network --communities-dir /path/to/communities
```

### Filtering JSON Output with jq

```bash
# Get all disconnected taxa
just audit-network-json | jq '.[] | .[] | select(.type=="DISCONNECTED") | .taxon'

# Count issues by type
just audit-network-json | jq '[.[] | .[] | .type] | group_by(.) | map({type: .[0], count: length})'

# Find communities with ID mismatches
just audit-network-json | jq 'to_entries | map(select(.value | any(.type=="ID_MISMATCH"))) | map(.key)'
```

### Programmatic Validation

```python
from communitymech.network.auditor import NetworkIntegrityAuditor
import sys

auditor = NetworkIntegrityAuditor()
issues = auditor.audit_all(check_only=True)

# Exits with code 1 if issues found
# Use for custom validation pipelines
```

## See Also

- [Phase 1 Completion Report](../PHASE_1_COMPLETION.md)
- [LLM Configuration](../conf/llm_config.yaml)
- [CI/CD Workflow](../.github/workflows/network-quality.yml)
- [Main README](../README.md)
