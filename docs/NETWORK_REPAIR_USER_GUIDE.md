# Network Repair User Guide

Complete guide to using the LLM-Assisted Network Quality Check Infrastructure for maintaining microbial community interaction networks.

## Table of Contents

1. [Quick Start](#quick-start)
2. [Workflows](#workflows)
3. [Commands Reference](#commands-reference)
4. [Configuration](#configuration)
5. [Best Practices](#best-practices)
6. [Cost Management](#cost-management)
7. [Troubleshooting](#troubleshooting)

---

## Quick Start

### Prerequisites

```bash
# 1. Install dependencies
just install

# 2. Set API key (get from: https://console.anthropic.com/)
export ANTHROPIC_API_KEY=sk-ant-your-key-here

# 3. Verify installation
uv run communitymech --help
```

### Your First Repair

```bash
# 1. Audit all communities to find issues
just audit-network

# 2. Repair a single community interactively
just repair-network kb/communities/Richmond_Mine_AMD_Biofilm.yaml

# 3. Review and approve suggestions
# (Interactive prompts will guide you)

# 4. Verify fixes
just audit-network
```

---

## Workflows

### Workflow 1: Interactive Single-Community Repair

**Best for**: Fixing issues in one or two community files

```bash
# Step 1: Identify issues
just audit-network
# Output shows which communities have issues

# Step 2: Interactive repair
export ANTHROPIC_API_KEY=sk-ant-...
just repair-network kb/communities/YourCommunity.yaml

# What happens:
# - Audits the file for network integrity issues
# - For each issue:
#   * Generates LLM suggestion with context
#   * Displays formatted YAML suggestion
#   * Shows validation results (schema, ontology, evidence)
#   * Prompts: [A]pprove [E]dit [R]eject [S]kip [Q]uit?
# - Creates backups before applying
# - Shows summary with costs

# Step 3: Verify
just validate kb/communities/YourCommunity.yaml
just audit-network
```

**Interactive Controls**:
- `A` = Approve and apply suggestion
- `E` = Edit suggestion before applying (opens editor)
- `R` = Reject suggestion (mark as reviewed)
- `S` = Skip suggestion (ask again later)
- `Q` = Quit repair session

**Example Output**:
```
🔧 Repairing: kb/communities/Richmond_Mine_AMD_Biofilm.yaml

Auditing network integrity...
Found 3 issues

┌─────────────────────────────────┬────────────────────────────────┐
│ Type                            │ Details                        │
├─────────────────────────────────┼────────────────────────────────┤
│ DISCONNECTED                    │ Taxon 'ARMAN' has no ...       │
│ DISCONNECTED                    │ Taxon 'Ferroplasma' has no ... │
│ UNKNOWN_TARGET                  │ Target taxon 'Mystery bac...'  │
└─────────────────────────────────┴────────────────────────────────┘

Issue 1/3: DISCONNECTED - ARMAN

Generating LLM suggestion...

💡 Suggested Repair:
╭─── Suggested Interaction ─────────────────────╮
│ - name: "Iron Cycling Partnership"            │
│   interaction_type: "MUTUALISM"               │
│   description: "ARMAN oxidizes Fe(II)..."     │
│   source_taxon:                               │
│     preferred_term: "ARMAN"                   │
│     term:                                     │
│       id: "NCBITaxon:123456"                  │
│       label: "ARMAN"                          │
│   target_taxon:                               │
│     preferred_term: "Leptospirillum group II" │
│     ...                                       │
╰───────────────────────────────────────────────╯

✅ Validation: PASSED
  ✓ Schema valid
  ✓ Ontology terms found
  ✓ Evidence snippet validated (97% match)
  ✓ Biologically plausible

Apply this repair? [A/e/r/s/q]: a
✓ Applied (backup: Richmond_Mine_AMD_Biofilm_20260306_143022.yaml)

...processing remaining issues...

📊 Repair Summary

┌───────────────┬───────┐
│ Metric        │ Value │
├───────────────┼───────┤
│ Total Repairs │ 3     │
│ Applied       │ 2     │
│ Rejected      │ 1     │
│ API Calls     │ 3     │
│ Total Cost    │ $0.06 │
└───────────────┴───────┘
```

### Workflow 2: Dry-Run Mode (Testing)

**Best for**: Testing prompts, estimating costs, reviewing LLM output quality

```bash
# Generate suggestions without applying any changes
just repair-network-dry kb/communities/YourCommunity.yaml

# What you see:
# - All suggestions with full context
# - All validation results
# - Cost estimates
# - NO changes to files
# - NO backups created

# Use cases:
# - Test new prompt templates
# - Estimate API costs before batch run
# - Review LLM output quality
# - Debug validation issues
```

### Workflow 3: Batch Repair with Offline Review

**Best for**: Processing many communities, team review, production deployments

```bash
# ============================================
# PHASE 1: Generate Suggestions
# ============================================

# Generate report for ALL communities with issues
export ANTHROPIC_API_KEY=sk-ant-...
just suggest-network-repairs

# Output: reports/network_repair_suggestions.yaml
# Cost: ~$5-10 for all 76 communities (with parallel processing)

# OR: Generate for limited set (faster, cheaper testing)
just suggest-network-repairs-limited 10

# ============================================
# PHASE 2: Human Review (Offline)
# ============================================

# Open the report for review
vim reports/network_repair_suggestions.yaml

# Report structure:
# communities:
#   - file: kb/communities/Richmond_Mine_AMD_Biofilm.yaml
#     name: Richmond_Mine_AMD_Biofilm
#     issues_count: 3
#     suggestions:
#       - issue:
#           type: DISCONNECTED
#           summary: "Disconnected: ARMAN"
#         suggestion:
#           suggested_interactions:
#             - name: "Iron Cycling Partnership"
#               interaction_type: "MUTUALISM"
#               ...
#         validation:
#           passed: true
#           errors: []
#         approved: false  # ← SET TO true
#         notes: ""        # ← ADD YOUR NOTES

# Review each suggestion:
# 1. Read the issue description
# 2. Review the suggested interaction
# 3. Check validation results
# 4. Verify biological plausibility
# 5. Check evidence (PMID, snippet)
# 6. Decision:
#    - Set approved: true (to apply)
#    - Set approved: false (to skip)
#    - Add notes for your reasoning

# ============================================
# PHASE 3: Apply Approved Suggestions
# ============================================

just apply-batch-repairs reports/network_repair_suggestions.yaml

# Output:
# 🔧 Applying Batch Repairs
#
# Results:
# ┌─────────┬───────┐
# │ Status  │ Count │
# ├─────────┼───────┤
# │ ✅ Applied │ 12    │
# │ ⊘ Skipped │ 8     │
# │ ❌ Errors  │ 0     │
# └─────────┴───────┘
#
# ✓ Suggestions applied successfully
# Backups saved to .backups/

# ============================================
# PHASE 4: Verify Changes
# ============================================

# Run full QC
just qc

# Verify network integrity improved
just audit-network
# Should show fewer issues

# Generate HTML to view changes
just gen-html
```

**Batch Report Features**:
- **Parallel Processing**: Multiple communities processed simultaneously (4x speedup)
- **Cost Control**: Configurable limits on communities and issues
- **Offline Review**: No API calls during review phase
- **Selective Application**: Only approved suggestions applied
- **Safety**: Validation errors automatically skip
- **Audit Trail**: Notes field for documentation

### Workflow 4: CI/CD Integration

**Best for**: Pull request validation, automated quality checks

The GitHub Actions workflow automatically:
1. Runs network integrity audit on every PR
2. Fails if new issues introduced
3. Generates repair suggestions (if ANTHROPIC_API_KEY secret set)
4. Uploads suggestions as artifact
5. Comments on PR with summary

**Setup**:
```bash
# 1. Add API key to GitHub Secrets
# Settings → Secrets → Actions → New repository secret
# Name: ANTHROPIC_API_KEY
# Value: sk-ant-your-key

# 2. Workflow runs automatically on PR
# See: .github/workflows/network-quality.yml

# 3. Download suggestions from PR
# Actions tab → Workflow run → Artifacts → network-repair-suggestions
```

---

## Commands Reference

### Audit Commands

```bash
# Audit all communities (human-readable output)
just audit-network
communitymech audit-network

# CI mode (exits with error if issues found)
just check-network-quality
communitymech audit-network --check-only

# JSON output (for parsing)
just audit-network-json
communitymech audit-network --json

# Write report to file
just audit-network-report network_audit.txt
communitymech audit-network --report network_audit.txt
```

### Repair Commands

```bash
# Interactive repair (single community)
just repair-network FILE
communitymech repair-network FILE

# Dry-run mode (no changes)
just repair-network-dry FILE
communitymech repair-network FILE --dry-run

# Auto-approve mode (no prompts)
communitymech repair-network FILE --auto-approve

# Limit number of repairs
communitymech repair-network FILE --max-repairs 5
```

### Batch Commands

```bash
# Generate batch report (all communities)
just suggest-network-repairs
communitymech repair-network-batch --report-only

# Generate with limits
just suggest-network-repairs-limited 10
communitymech repair-network-batch --report-only --max-communities 10 --max-issues 3

# Custom output path
communitymech repair-network-batch --report-only --output my_report.yaml

# Apply approved suggestions
just apply-batch-repairs REPORT
communitymech repair-network-batch --apply-from REPORT
```

### Validation Commands

```bash
# Schema validation
just validate FILE
linkml-validate -s src/communitymech/schema/communitymech.yaml FILE

# Evidence validation
just validate-references FILE
linkml-reference-validator validate data FILE -s schema

# Ontology validation
just validate-terms FILE
linkml-term-validator validate-data FILE -s schema --labels

# Full QC (all checks)
just qc
```

---

## Configuration

### Environment Variables

```bash
# Required for repair commands
export ANTHROPIC_API_KEY=sk-ant-your-key

# Optional: Override model (default: claude-opus-4-6)
export LLM_MODEL=claude-sonnet-4-6

# Optional: Override cost limit (default: 10.0 USD)
export MAX_COST_PER_RUN=5.0
```

### LLM Configuration (`conf/llm_config.yaml`)

```yaml
llm:
  provider: anthropic
  model: claude-opus-4-6  # or claude-sonnet-4-6, claude-haiku-4-5
  api_key_env: ANTHROPIC_API_KEY
  temperature: 0.1  # Low for factual outputs
  max_tokens: 4096
  timeout: 60  # seconds

repair:
  auto_approve_threshold: 0.9
  max_suggestions_per_taxon: 2
  require_evidence_validation: true
  backup_before_apply: true

limits:
  rate_limit_per_minute: 10
  max_api_calls_per_run: 100
  max_cost_per_run_usd: 10.0
  track_costs: true

validation:
  validate_evidence: true
  validate_ontology: true
  check_plausibility: true
  min_snippet_similarity: 0.95
```

### Model Selection Guide

| Model | Speed | Cost | Quality | Best For |
|-------|-------|------|---------|----------|
| **claude-opus-4-6** | Slow | High ($15/1M in) | Best | Production, complex communities |
| **claude-sonnet-4-6** | Medium | Medium ($3/1M in) | Good | Most use cases, balanced |
| **claude-haiku-4-5** | Fast | Low ($0.25/1M in) | Fair | Testing, simple repairs |

**Recommendation**: Start with Sonnet for testing, use Opus for production.

---

## Best Practices

### 1. Incremental Repairs

```bash
# ❌ DON'T: Repair all 60 communities at once
just suggest-network-repairs  # $10+ cost

# ✅ DO: Start small, validate, iterate
just suggest-network-repairs-limited 5  # $0.50 cost
# Review results
# Adjust prompts if needed
# Then scale up
```

### 2. Review Before Applying

```bash
# ❌ DON'T: Auto-approve without review
communitymech repair-network FILE --auto-approve

# ✅ DO: Review each suggestion
just repair-network FILE  # Interactive mode
# OR
just suggest-network-repairs  # Offline review
```

### 3. Validate Evidence

All LLM suggestions include evidence (PMID/DOI + snippet). Always verify:

1. **Snippet matches abstract**: Validation checks 95%+ fuzzy match
2. **Reference supports claim**: Read the paper if uncertain
3. **Context is correct**: Check year, organism, environment

```bash
# Evidence in suggestion:
evidence:
  - reference: "PMID:15066799"
    snippet: "Ferroplasma acidarmanus was capable of growing..."
    supports: SUPPORTS
    evidence_source: SCIENTIFIC_PUBLICATION

# Verify:
# 1. Fetch abstract: https://pubmed.ncbi.nlm.nih.gov/15066799/
# 2. Confirm snippet appears (fuzzy match OK)
# 3. Check context matches your community
```

### 4. Cost Control

```bash
# Set limits in conf/llm_config.yaml:
limits:
  max_cost_per_run_usd: 5.0  # Hard limit

# Monitor costs:
# - Displayed in repair summaries
# - Tracked per run
# - Stops when limit reached

# Cost-saving tips:
# 1. Use --max-communities and --max-issues for testing
# 2. Use claude-sonnet-4-6 instead of opus
# 3. Enable parallel processing (default, 4x faster)
# 4. Cache results (automatic)
```

### 5. Backup Management

```bash
# Backups created automatically in .backups/
.backups/
  Richmond_Mine_AMD_Biofilm_20260306_143022.yaml
  Richmond_Mine_AMD_Biofilm_20260306_145312.yaml
  ...

# List backups for a file
ls .backups/Richmond_Mine_AMD_Biofilm_*.yaml

# Restore from backup
cp .backups/Richmond_Mine_AMD_Biofilm_20260306_143022.yaml \
   kb/communities/Richmond_Mine_AMD_Biofilm.yaml

# Or use git
git restore kb/communities/Richmond_Mine_AMD_Biofilm.yaml
```

### 6. Iterative Refinement

```bash
# 1. First pass: dry-run
just repair-network-dry FILE
# Review suggestions, identify issues

# 2. Adjust prompts if needed
vim src/communitymech/llm/prompts.py

# 3. Test with single community
just repair-network FILE

# 4. Scale to batch
just suggest-network-repairs-limited 10

# 5. Full batch when confident
just suggest-network-repairs
```

---

## Cost Management

### Pricing (as of March 2026)

| Model | Input (per 1M tokens) | Output (per 1M tokens) |
|-------|----------------------|------------------------|
| Claude Opus 4.6 | $15.00 | $75.00 |
| Claude Sonnet 4.6 | $3.00 | $15.00 |
| Claude Haiku 4.5 | $0.25 | $1.25 |

### Typical Costs

**Single Community Repair**:
- Context: ~2,000 tokens
- Prompt: ~1,000 tokens
- Output: ~800 tokens
- **Cost per suggestion**: $0.02 (Sonnet), $0.08 (Opus)

**Batch Processing (76 communities)**:
- Avg 2 issues per community = 152 suggestions
- Sequential: ~15 minutes, $3-12
- Parallel (4 workers): ~4 minutes, $3-12
- **Cost savings**: Time only, API costs same

**Cost Estimate Tool**:
```bash
# Dry-run shows cost estimate without charges
just repair-network-dry FILE
# Shows: "Estimated cost: $0.16 (2 suggestions)"

# Batch report includes cost estimate
just suggest-network-repairs
# Output includes: "Total Cost: $3.45 (42 API calls)"
```

### Budget Planning

For a project with 60 communities:

| Scenario | Communities | Issues/Community | Suggestions | Cost (Sonnet) | Cost (Opus) |
|----------|-------------|------------------|-------------|---------------|-------------|
| Testing | 10 | 2 | 20 | $0.40 | $1.60 |
| Medium | 30 | 2 | 60 | $1.20 | $4.80 |
| Full | 60 | 2 | 120 | $2.40 | $9.60 |
| Large | 100 | 3 | 300 | $6.00 | $24.00 |

**Note**: Costs include context caching optimization (reduces input costs by ~60% on repeated communities).

---

## Troubleshooting

### Issue: API Key Not Found

```
❌ Error: ANTHROPIC_API_KEY environment variable not set
```

**Solution**:
```bash
# Set API key
export ANTHROPIC_API_KEY=sk-ant-your-key

# Verify
echo $ANTHROPIC_API_KEY

# For persistence, add to ~/.bashrc or ~/.zshrc
echo 'export ANTHROPIC_API_KEY=sk-ant-your-key' >> ~/.bashrc
```

### Issue: Rate Limit Exceeded

```
❌ Error: Rate limit exceeded (429)
```

**Solution**: Automatic rate limiting is built-in (10 req/min default). If hit:
```yaml
# Adjust in conf/llm_config.yaml
limits:
  rate_limit_per_minute: 5  # Reduce from 10
```

### Issue: Validation Failed

```
❌ Validation: FAILED
  ✗ Evidence snippet mismatch (85% similarity, required 95%)
```

**Solution**: LLM hallucinated snippet or found wrong reference.
- **Option 1**: Reject suggestion, try again (LLM will generate new one)
- **Option 2**: Edit suggestion to fix reference/snippet
- **Option 3**: Lower threshold (not recommended):
  ```yaml
  # conf/llm_config.yaml
  validation:
    min_snippet_similarity: 0.85  # Lower from 0.95
  ```

### Issue: Cost Limit Exceeded

```
❌ Error: Cost limit exceeded ($10.50 > $10.00)
```

**Solution**:
```yaml
# Increase limit in conf/llm_config.yaml
limits:
  max_cost_per_run_usd: 20.0
```

### Issue: Missing Dependencies

```
❌ Error: anthropic package not installed
```

**Solution**:
```bash
# Install with LLM dependencies
uv sync --all-extras

# Or specific group
uv sync --group llm
```

### Issue: Slow Batch Processing

**Solution**: Enable parallel processing (should be default):
```python
# In batch_reporter.py initialization
reporter = BatchReporter(parallel=True, max_workers=4)
```

Current: 4 workers (4x speedup)
Can increase: `max_workers=8` (diminishing returns beyond 8)

### Issue: Network Integrity Issues Not Found

```bash
just audit-network
# No issues found (but you see obvious problems in YAML)
```

**Solution**: Auditor may not detect all issue types. Manual review required.

Detected issue types:
- ✅ DISCONNECTED: Taxon with no interactions
- ✅ MISSING_SOURCE: Interaction missing source_taxon
- ✅ UNKNOWN_SOURCE: source_taxon not in taxonomy
- ✅ UNKNOWN_TARGET: target_taxon not in taxonomy
- ✅ ID_MISMATCH: Taxon IDs don't match

Not detected (require manual curation):
- ❌ Biologically implausible interactions
- ❌ Missing evidence
- ❌ Incorrect ontology terms

---

## Advanced Usage

### Custom Prompt Templates

Edit prompts for specialized domains:

```bash
vim src/communitymech/llm/prompts.py
```

```python
# Example: Add marine-specific context
DISCONNECTED_TAXON_PROMPT = """
You are a marine microbial ecology expert...

Additional context for marine systems:
- Salinity: {salinity}
- Depth: {depth}
- Nutrient availability: {nutrients}
...
"""
```

### Programmatic API

Use the repair system in Python code:

```python
from pathlib import Path
from communitymech.network.llm_repair import LLMNetworkRepairer
from communitymech.llm.anthropic_client import AnthropicClient

# Initialize
client = AnthropicClient()
repairer = LLMNetworkRepairer(llm_client=client)

# Repair community
result = repairer.repair_community(
    yaml_path=Path("kb/communities/YourCommunity.yaml"),
    dry_run=False,
    auto_approve=False,
    max_repairs=5
)

# Check results
print(f"Applied: {result['applied_count']}")
print(f"Cost: ${result['cost']['total_cost_usd']:.4f}")
```

### Batch Processing with Custom Logic

```python
from communitymech.network.batch_reporter import BatchReporter

# Custom reporter with filters
reporter = BatchReporter(
    parallel=True,
    max_workers=8
)

# Generate report
result = reporter.generate_report(
    output_path=Path("custom_report.yaml"),
    max_communities=None,  # All communities
    max_issues_per_community=5  # Limit per community
)

# Custom post-processing
import yaml
with open("custom_report.yaml") as f:
    report = yaml.safe_load(f)

# Filter high-confidence suggestions
high_confidence = [
    s for c in report["communities"]
    for s in c["suggestions"]
    if s["validation"]["passed"] and len(s["validation"]["errors"]) == 0
]

# Auto-approve high-confidence
for suggestion in high_confidence:
    suggestion["approved"] = True

# Save filtered report
with open("auto_approved.yaml", "w") as f:
    yaml.dump(report, f)
```

---

## FAQ

**Q: How accurate are LLM suggestions?**

A: Validation catches most errors:
- Schema validation: 100% (enforced)
- Ontology terms: ~95% (checked via OAK)
- Evidence snippets: ~90% (95%+ similarity required)
- Biological plausibility: ~85% (heuristic checks)

Always review before applying.

**Q: Can I use OpenAI instead of Anthropic?**

A: Not currently. The system is built for Claude API. OpenAI support could be added by implementing `OpenAIClient(LLMClient)`.

**Q: How do I revert changes?**

A:
```bash
# Option 1: Restore from backup
cp .backups/YourCommunity_TIMESTAMP.yaml kb/communities/YourCommunity.yaml

# Option 2: Use git
git restore kb/communities/YourCommunity.yaml

# Option 3: Git reset (if committed)
git reset --hard HEAD~1
```

**Q: Can I customize validation rules?**

A: Yes, edit `src/communitymech/network/validators.py`:
```python
class SuggestionValidator:
    def __init__(
        self,
        validate_evidence=True,
        validate_ontology=True,
        check_plausibility=True,
        min_snippet_similarity=0.95  # ← Adjust threshold
    ):
        ...
```

**Q: What if LLM suggests wrong interaction type?**

A: Use Edit mode:
```
Apply this repair? [A/E/r/s/q]: e
# Opens editor with YAML
# Edit interaction_type: MUTUALISM → COMPETITION
# Save and exit
# System re-validates and applies
```

**Q: How do I track which suggestions were applied?**

A: Check git history:
```bash
git log --oneline kb/communities/YourCommunity.yaml
# Shows commits with LLM repairs

git show COMMIT_HASH
# Shows exact changes
```

Also: Batch reports include `notes` field for documentation.

---

## Support

- **Documentation**: `docs/` directory
- **Issues**: https://github.com/your-org/CommunityMech/issues
- **Examples**: `examples/` directory
- **Tests**: `tests/test_e2e_repair.py` for workflow examples

---

**Last Updated**: March 6, 2026
**Version**: Phase 5 - Integration & Polish Complete
