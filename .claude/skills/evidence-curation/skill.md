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

## Overview

CommunityMech community records require evidence-backed claims: each interaction,
taxonomic assignment, or environmental property should cite a PMID or DOI with an
exact text snippet from the publication.

This skill covers the full evidence lifecycle:
- **Extract** — pull snippets from PDFs or PubMed abstracts
- **Repair** — fix malformed, missing, or mismatched snippets
- **Review** — manual literature review and snippet approval
- **Validate** — confirm evidence passes schema and reference checks

**Run from `CommunityMech/CommunityMech/` directory.**

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

# 6. Run review-communities to check remaining issues
communitymech audit-network
```

---

## Manual Curation Workflow (Adding New Evidence)

```bash
# Extract snippets from a PDF
python scripts/curate_evidence_with_pdfs.py --pdf path/to/paper.pdf

# Quick literature review for a specific community
python scripts/quick_literature_review.py --community CommunityMech:000042

# Full literature review with scoring
python scripts/review_literature.py --community CommunityMech:000042

# Apply suggested fixes after review
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
| `scripts/quick_literature_review.py` | Fast per-community literature scan |
| `scripts/review_literature.py` | Full literature review with scoring |
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
# Full schema + reference validation
communitymech audit-network

# Or use review-communities skill
# (checks evidence references as part of full QA)
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
- Run `quick_literature_review.py` to find candidate papers
- Or use LLM: `communitymech repair-network --community CommunityMech:XXXXXX`

---

## Related Skills

- `review-communities` — validates evidence as part of full QA
- `manage-identifiers` — if adding new community records that need evidence
