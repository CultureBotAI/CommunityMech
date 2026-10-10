---
name: evidence-curation
description: Curate, validate, and repair evidence snippets and literature references for CommunityMech microbial community records
category: workflow
requires_database: false
requires_internet: true
version: 1.0.0
tags: [evidence, snippets, literature, pmid, doi, references, repair, curation]
---

# Evidence Curation Skill

## Assessed Review Handoff

For an evidence review or audit, delegate the final assessment to
[review-communities](../review-communities/SKILL.md), following
[docs/record-reviews.md](../../../docs/record-reviews.md) and
[the local profile](../../../docs/record-review-profile.md).
Use the registered review-communities route as the saved `skill`; preserve
per-record P1-P4 findings, both native scores, and assertion-level evidence.
For each interaction or causal edge keep participants, direction, mechanism,
experimental context, exact source locator and inspected verbatim snippet.
Distinguish abstract, full text and supplementary evidence.

Extraction, network checks and repair suggestions are diagnostic inputs, not
completed scientific review or snippet approval. A deterministic-only
assessment uses `scientific_review: false`. No producer draft may be promoted
without actual source assessment. Missing evidence remains a scoped gap.
Save final assessed YAML plus derived Markdown under
`reviews/structured/<timestamp>-<slug>/` and link both:

```bash
uv run python scripts/record_review.py inspect --targets /tmp/evidence-targets.yaml
uv run python scripts/record_review.py validate /tmp/completed-evidence-review.yaml
uv run python scripts/record_review.py save --content /tmp/completed-evidence-review.yaml
```

Use session-unique temporary paths. Audit-only requests run no repair/apply
commands and change no scientific records, status or history. The repair
workflows below require explicit curation intent and the native guarded writer.
Paid/LLM research or repair additionally requires explicit authorization;
the assessment handoff does not invoke or recreate a research producer.

## Overview

CommunityMech community records require evidence-backed claims: each interaction,
taxonomic assignment, or environmental property should cite a PMID or DOI with an
exact text snippet from the publication.

This skill covers the full evidence lifecycle:
- **Extract** — pull snippets from PDFs or PubMed abstracts
- **Repair** — fix malformed, missing, or mismatched snippets
- **Review** — manual literature review and snippet approval
- **Validate** — confirm evidence passes schema and reference checks

**Run from the repository root.**

---

## Evidence Schema

Each evidence entry in a community YAML requires:

```yaml
evidence:
  - pmid: "12345678"          # or doi: "10.1038/..."
    snippet: "exact text from the abstract or paper"
    snippet_start: 42         # character offset (optional but preferred)
    snippet_end: 95
    accessed: "2026-01-15"
```

Common failures caught by `review-communities`:
- Snippet text not found in the referenced abstract
- PMID does not exist or is retracted
- Missing `snippet` field (bare reference)
- PMC ID used instead of PMID

---

## Repair Workflow (Most Common Path)

```bash
# 1. Find all snippets that don't match their referenced abstracts
python scripts/batch_snippet_fixer.py

# 2. Intelligent repair — tries to find the correct passage automatically
python scripts/intelligent_snippet_fixer.py

# 3. Remove still-invalid snippets (marks as needs_review)
python scripts/fix_invalid_snippets.py

# 4. Convert PMC IDs to PMIDs
python scripts/apply_pmc_conversions.py

# 5. Normalize reference formats (PMID: prefix, DOI capitalization)
python scripts/fix_reference_formats.py

# 6. Network diagnostics only; then hand off to review-communities above
communitymech audit-network
```

---

## Manual Curation Workflow (Adding New Evidence)

```bash
# Extract snippets from a PDF
python scripts/curate_evidence_with_pdfs.py --pdf path/to/paper.pdf

# Assess extracted evidence through review-communities and the common saver.
# Apply suggested fixes only after separately authorized curation review.
python scripts/apply_suggested_snippets.py
python scripts/apply_suggested_fixes.py
```

---

## Scripts

| Script | Purpose |
|--------|---------|
| `scripts/extract_evidence_snippets.py` | Extract snippets from PDFs/PubMed |
| `scripts/batch_snippet_fixer.py` | Batch repair of mismatched snippets |
| `scripts/intelligent_snippet_fixer.py` | AI-assisted snippet correction |
| `scripts/fix_invalid_snippets.py` | Remove or flag unfixable snippets |
| `scripts/fix_reference_formats.py` | Normalize PMID/DOI format |
| `scripts/apply_pmc_conversions.py` | PMC ID → PMID conversion |
| `scripts/handle_special_references.py` | Edge cases (preprints, books, datasets) |
| `scripts/curate_evidence_with_pdfs.py` | PDF-backed snippet extraction |
| `scripts/analyze_literature_report.py` | Analyze review results |
| `scripts/analyze_review_cases.py` | Categorize review case types |
| `scripts/apply_suggested_snippets.py` | Apply auto-suggested snippet text |
| `scripts/apply_suggested_fixes.py` | Apply batch-suggested fixes |

---

## LLM-Assisted Repair

The `communitymech repair-network` CLI uses an LLM to suggest fixes:

```bash
# Repair network issues including evidence (requires Anthropic API key)
communitymech repair-network --community CommunityMech:000042

# Or batch repair all communities with issues
communitymech repair-network --all --dry-run
communitymech repair-network --all
```

---

## Internet Requirements

- **PubMed API** — abstract fetching for snippet validation (`extract_evidence_snippets.py`)
- **PubMed Central** — PMC ID conversion (`apply_pmc_conversions.py`)
- **CrossRef** — DOI resolution and metadata

All API calls respect rate limits; no API key required for PubMed.

---

## Validation After Changes

Always run validation after evidence changes:

```bash
# Network diagnostics; this is not full schema + reference validation
communitymech audit-network

# Separate schema and reference checks for the actual reviewed record:
just validate-strict <record-path>
just validate-references-explained <record-path>
# Then use review-communities for the assessed review and shared persistence.
```

---

## Common Patterns

**"Snippet not found in abstract":**
- Use `batch_snippet_fixer.py` to auto-search for the passage
- If not found, snippet may be from full text (not abstract) — mark with `full_text: true`
- If PMC: use `apply_pmc_conversions.py` to get correct PMID

**"PMID does not exist":**
- Check for typo; use `https://pubmed.ncbi.nlm.nih.gov/{pmid}/`
- May be PMC ID (`PMC1234567`) — run `apply_pmc_conversions.py`
- May be preprint DOI — use `handle_special_references.py`

**"Missing evidence entirely":**
- Hand off to `review-communities` to assess inspected sources or record a gap.
- Do not run paid/LLM producers without explicit authorization. Suggestions
  remain unassessed leads until the source and exact assertion are checked.

---

## Related Skills

- `review-communities` — validates evidence as part of full QA
- `manage-identifiers` — if adding new community records that need evidence
