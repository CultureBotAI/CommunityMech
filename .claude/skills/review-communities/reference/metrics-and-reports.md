# Quality Metrics & Validation Reports

*Reference for the **review-communities** skill — see [`../skill.md`](../skill.md) for the overview, workflows, and rule summary.*

---

## Quality Metrics

### Completeness Score

```python
def calculate_completeness(community_data):
    """
    Calculate completeness score (0-100)

    Required fields (50 points):
    - id, name, description
    - taxonomy with roles
    - ecological_state, community_category

    Recommended fields (30 points):
    - environment_term
    - environmental_factors (≥3)
    - ecological_interactions (≥3)
    - external_resources (≥1)

    Enrichment fields (20 points):
    - growth_media with linkages
    - associated_datasets
    - metabolic_pathways
    - temporal_dynamics
    """
    score = 0

    # Required fields
    if all_required_fields_present(community_data):
        score += 50

    # Recommended fields
    if community_data.get('environment_term'):
        score += 5
    if len(community_data.get('environmental_factors', [])) >= 3:
        score += 10
    if len(community_data.get('ecological_interactions', [])) >= 3:
        score += 10
    if community_data.get('external_resources'):
        score += 5

    # Enrichment
    if community_data.get('growth_media'):
        score += 10
    if community_data.get('associated_datasets'):
        score += 5
    if any('metabolites' in i for i in community_data.get('ecological_interactions', [])):
        score += 5

    return min(100, score)
```

### Validation Quality Score

```python
def calculate_validation_score(validation_summary):
    """
    Calculate validation quality score (0-100)

    Weights:
      - P1 errors: -50 points each (blocking)
      - P2 warnings: -10 points each
      - P3 warnings: -2 points each
      - Evidence coverage: +20 points
      - Network completeness: +15 points
    """
    base_score = 100

    base_score -= validation_summary['P1'] * 50
    base_score -= validation_summary['P2'] * 10
    base_score -= validation_summary['P3'] * 2

    # Evidence coverage bonus
    avg_evidence_per_interaction = validation_summary.get('avg_evidence', 0)
    base_score += min(avg_evidence_per_interaction / 2, 1.0) * 20

    # Network completeness bonus
    if validation_summary.get('network_integrity') == 'COMPLETE':
        base_score += 15

    return max(0, min(100, base_score))
```

---

## Validation Reports

### Text Report Format

```markdown
# CommunityMech Validation Report
**Generated:** 2026-03-16 14:23:45
**Communities Validated:** 78

## Summary

| Metric | Value |
|--------|-------|
| Total Communities | 78 |
| Passed All Checks | 72 (92.3%) |
| P1 Critical Errors | 0 |
| P2 High Warnings | 12 |
| P3 Medium Warnings | 45 |
| P4 Low Suggestions | 89 |
| Avg Completeness Score | 87.3 |
| Avg Validation Score | 92.1 |

## P1 Critical Errors (0)

✅ No critical errors found!

## P2 High-Priority Warnings (12)

### Ontology Label Mismatches (8)
- `Richmond_Mine_AMD_Biofilm.yaml`: "Leptospirillum ferriphilum" → "Leptospirillum ferrooxidans" (NCBITaxon:178)
- `Geobacter_Methanosarcina_DIET.yaml`: "Methanosarcina barkeri" label mismatch
- ...

### Evidence Snippet Mismatches (4)
- `Dangl_SynComm_35.yaml`: interaction[2].evidence[0] snippet similarity 65%
- ...

## P3 Medium-Priority Enrichment (45)

### Growth Media Not Linked (21)
- Communities missing CultureMech linkages
- Run: `just link-media` to auto-link

### Limited Evidence (15)
- Communities with < 3 evidence items
- Recommend adding citations

...

## Recommendations

1. **Immediate**: Fix 0 P1 errors (none found!)
2. **This Week**: Review 12 P2 warnings, prioritize label mismatches
3. **This Month**: Auto-enrich 21 communities with media linkages
4. **Ongoing**: Add evidence to 15 under-cited communities
```

### JSON Report Format

```json
{
  "metadata": {
    "generated_at": "2026-03-16T14:23:45Z",
    "generator": "CommunityMech Review Skill v1.0.0",
    "communities_validated": 78
  },
  "summary": {
    "total_communities": 78,
    "passed_all_checks": 72,
    "P1_critical": 0,
    "P2_high": 12,
    "P3_medium": 45,
    "P4_low": 89,
    "avg_completeness_score": 87.3,
    "avg_validation_score": 92.1
  },
  "issues_by_priority": {
    "P1": [],
    "P2": [
      {
        "rule_id": "P2.1",
        "community": "Richmond_Mine_AMD_Biofilm",
        "description": "Ontology label mismatch",
        "location": "taxonomy[1].taxon_term.term.label",
        "current": "Leptospirillum ferriphilum",
        "expected": "Leptospirillum ferrooxidans",
        "ontology_id": "NCBITaxon:178",
        "suggested_fix": "Update label to match NCBITaxon preferred term",
        "auto_correctable": true
      }
    ],
    "P3": [...],
    "P4": [...]
  },
  "communities": [
    {
      "id": "CommunityMech:000001",
      "file": "Richmond_Mine_AMD_Biofilm.yaml",
      "name": "Richmond Mine Acid Mine Drainage Biofilm",
      "completeness_score": 95,
      "validation_score": 88,
      "issues": {
        "P1": 0,
        "P2": 1,
        "P3": 2,
        "P4": 5
      }
    }
  ]
}
```

---

