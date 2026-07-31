---
name: review-communities
description: Use this skill to quality-check ontology-mapped CommunityMech microbial-community records — verify NCBITaxon/ENVO/GO/CHEBI terms (OAK), PMID/DOI evidence citations and snippet matching, ecological-interaction network integrity, and CultureMech/MediaIngredientMech growth-media linkages. Use after curating a community, before a KG export, or for periodic maintenance. Issues are graded P1 (blocking) → P4 (optional).
version: 1.1.0
tags: [validation, quality-assurance, ontology, oak, ncbitaxon, envo, go, chebi, references, evidence]
author: CommunityMech Team
created: 2026-03-16
---

# Review Communities Skill

## Overview

The **Review Communities** skill provides quality assurance for ontology-mapped microbial
communities in CommunityMech. It verifies that:

1. **Taxonomy is correctly mapped** — NCBITaxon IDs exist, labels match, roles appropriate
2. **Evidence is properly cited** — PMID/DOI references valid, snippets match abstracts
3. **Ontology terms are valid** — ENVO (environment), GO (processes), CHEBI (metabolites)
4. **Network integrity maintained** — interaction partners exist, directions valid
5. **Growth media linked** — CultureMech/MediaIngredientMech IDs valid
6. **Metadata is complete** — required fields populated, enums valid

**Technology stack:** LinkML schema, OAK (NCBITaxon/ENVO/GO/CHEBI term existence), a
reference validator (PubMed/CrossRef citations + snippet matching), a network auditor
(ecological-interaction integrity), and a media linker (CultureMech/MIM cross-references).

**Dataset:** 78 communities (60 curated + 18 BioModels synthetic); 100% schema-validated,
~95% with validated ontology terms.

---

## When to Use This Skill

| Scenario | Workflow | Priority |
|----------|----------|----------|
| **Post-curation QA** | Validate a newly curated community before committing | High |
| **Batch validation** | Review all 78 communities | High |
| **Pre-export check** | Ensure KG export quality before KG-Microbe ingestion | Critical |
| **Periodic maintenance** | Monthly validation after ontology updates | Medium |
| **Evidence verification** | Cross-check snippets with PubMed abstracts | High |
| **Network validation** | Check interaction partner references | High |
| **Media linkage check** | Validate CultureMech/MediaIngredientMech IDs | Medium |

```
IF newly curated community → interactive review
IF full dataset check      → batch validation (just qc)
IF evidence issues         → validate-references
IF network issues          → audit-network
IF media linkage           → link-media-dry
IF ontology terms          → validate-terms
```

---

## Review Workflows

All workflows run via `just`. `FILE` is a path like `kb/communities/Richmond_Mine_AMD_Biofilm.yaml`.

### 1. Schema Validation
```bash
just validate FILE        # single
just validate-all         # all communities
```
Checks required fields, types, enum values (`ecological_state`, `community_category`), and nested structure.

### 2. Ontology Term Validation
```bash
just validate-terms FILE  # single
just validate-terms-all   # all
just validate-schema-terms # schema-level term meanings
```
Checks NCBITaxon/ENVO/GO/CHEBI IDs exist and labels match; OAK adapters configured.

### 3. Evidence Reference Validation
```bash
just validate-references FILE      # single
just validate-references-all       # all
just repair-references FILE        # suggest fixes (dry-run)
```
Checks PMID/DOI validity, snippet fuzzy-match to abstracts (≥70%), required evidence fields,
support level (SUPPORT/REFUTE/NEUTRAL), and evidence source (EXPERIMENTAL/COMPUTATIONAL/REVIEW).

### 4. Network Integrity Audit
```bash
just audit-network                 # all communities
just audit-network-json            # JSON output
just check-network-quality         # CI mode (exits on error)
just audit-network-report FILE     # write report
```
Checks interaction partners reference existing taxa, valid directionality, no orphaned taxa
(in STABLE communities), no self-loops, and role/interaction consistency.

### 5. Growth Media Linkage Validation
```bash
just link-media-dry                # dry-run
just link-media-report             # mapping reports
```
Checks CultureMech/MediaIngredientMech IDs exist, URL formatting, composition mappings, and
source attribution (CultureMech vs community_curated).

### 6. Full Quality Control
```bash
just qc   # validate-all + validate-terms-all + validate-references-all + lint + test
```

### Claude Code-Assisted Review
```bash
/review-communities                # interactive
/review-communities "Richmond Mine AMD Biofilm"
```
Claude runs the validation suite, categorizes issues by priority, proposes fixes, applies on
approval, and documents changes in curation history. The full 7-step execution protocol
(identify → validate → categorize → report → propose → apply → document) is in
[`reference/execution-protocol.md`](reference/execution-protocol.md).

---

## Validation Rules

Issues are graded by priority. Full definitions (checks, impact, fixes) are in
[`reference/validation-rules.md`](reference/validation-rules.md).

| Level | Meaning | Action | Target |
|-------|---------|--------|--------|
| **P1** | Critical errors blocking KG export | Fix immediately | 0 |
| **P2** | High-priority warnings needing review | Manual review | < 5% |
| **P3** | Medium-priority enrichment opportunities | Auto-correct when possible | < 20% |
| **P4** | Low-priority info/suggestions | Optional | Any |

| Rule | Summary |
|------|---------|
| **P1.1** | Ontology term does not exist |
| **P1.2** | Invalid CURIE format |
| **P1.3** | Schema validation failure |
| **P1.4** | Evidence reference invalid (PMID/DOI) |
| **P1.5** | Network integrity violation |
| **P2.1** | Ontology label mismatch |
| **P2.2** | Snippet fuzzy-match below threshold |
| **P2.3** | Missing required metadata |
| **P2.4** | Functional role mismatch |
| **P3.1** | Growth media not linked |
| **P3.2** | Limited evidence |
| **P3.3** | Synonyms missing |
| **P3.4** | Environmental factors sparse |
| **P4.1** | External resources missing |
| **P4.2** | Metabolic pathways not detailed |
| **P4.3** | Temporal dynamics missing |

---

## Justfile Integration

The skill drives existing `just` recipes:

```
qc: validate-all validate-terms-all validate-references-all lint test
validate[-all] / validate-terms[-all] / validate-references[-all]   # validation
audit-network / check-network-quality                               # network integrity
link-media-dry / link-media / link-media-report                     # growth media
```

---

## Reference Files

| File | Contents |
|------|----------|
| [`reference/validation-rules.md`](reference/validation-rules.md) | Full definitions for all 16 P1–P4 rules: checks, impact, fixes |
| [`reference/execution-protocol.md`](reference/execution-protocol.md) | The Claude Code-assisted review and the 7-step execution protocol (identify → validate → categorize → report → propose → apply → document), with the report template and commit/curation-history steps |
| [`reference/metrics-and-reports.md`](reference/metrics-and-reports.md) | Completeness and validation-quality score formulas, and the text + JSON validation-report formats |
| [`reference/advanced-features.md`](reference/advanced-features.md) | Automated evidence repair, cross-community consistency checks, interaction-type inference, and literature mining for evidence |
