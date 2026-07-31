# Cross-Repository Reference (collection types, other repos, integration, roadmap)

*Reference for the **manage-identifiers** skill — see [`../SKILL.md`](../SKILL.md) for the CommunityMech overview and core workflow.*

---

## Collection Types

X-Mech repositories use two main patterns for organizing records:

### Type 1: Single-File Collection

**Pattern**: All records stored in one YAML file with a collection key

**Example Repository**: MediaIngredientMech

**Structure**:
```yaml
generation_date: '2026-03-09T06:54:18.022301+00:00'
total_count: 112
mapped_count: 65
unmapped_count: 47
ingredients:  # <-- Collection key
  - id: MediaIngredientMech:000001
    preferred_term: Sodium chloride
    mapping_status: MAPPED
    # ... other fields

  - id: MediaIngredientMech:000002
    preferred_term: Glucose
    mapping_status: MAPPED
    # ... other fields
```

**Characteristics**:
- ✓ Simple to manage (one file)
- ✓ Easy to see all records at once
- ✓ Good for <1000 records
- ✗ Large files can be slow to load/edit
- ✗ Git merge conflicts more likely

**Files**:
- Data: `data/curated/unmapped_ingredients.yaml`
- ID script: `scripts/add_mediaingredientmech_ids.py`

### Type 2: Multi-File Collection

**Pattern**: Each record is a separate YAML file in a directory hierarchy

**Example Repositories**: CultureMech, CommunityMech

**Structure**:
```
data/normalized_yaml/
├── bacterial/
│   ├── LB_Medium.yaml        # id: CultureMech:000001
│   ├── TSA_Medium.yaml       # id: CultureMech:000002
│   └── ...
├── algae/
│   ├── BG11_Medium.yaml      # id: CultureMech:000500
│   └── ...
└── fungi/
    └── PDA_Medium.yaml       # id: CultureMech:001000
```

**Each file contains**:
```yaml
id: CultureMech:000001
name: LB Medium
category: bacterial
# ... other fields
```

**Characteristics**:
- ✓ Scales well (1000s of records)
- ✓ Smaller git diffs (one file per change)
- ✓ Parallel editing easier
- ✗ More complex to manage
- ✗ Need to scan all files to find highest ID

**CultureMech adds**: ID registry file (`data/culturemech_id_registry.tsv`)
```tsv
culturemech_id	file_path
CultureMech:000001	data/normalized_yaml/bacterial/LB_Medium.yaml
CultureMech:000002	data/normalized_yaml/bacterial/TSA_Medium.yaml
```

**Files**:
- Data: `data/normalized_yaml/**/*.yaml`
- ID script: `scripts/assign_culturemech_ids.py` (with registry)
- Registry: `data/culturemech_id_registry.tsv` (CultureMech only)

### Comparison Table

| Feature | Single-File | Multi-File | Multi-File + Registry |
|---------|-------------|------------|----------------------|
| **Repo Example** | MediaIngredientMech | CommunityMech | CultureMech |
| **Record Count** | 112 | 78 | 15,431 |
| **Find Highest ID** | Parse YAML once | Scan all files | Read registry file |
| **Add New Record** | Append to list | Create new file | Create file + update registry |
| **Git Conflicts** | More likely | Rare | Rare |
| **Scalability** | <1000 records | <10,000 records | 10,000+ records |
| **Complexity** | Low | Medium | Medium-High |


---

## Repository-Specific Workflows

### MediaIngredientMech Quick Reference

**Current state**: 112 ingredients (`MediaIngredientMech:000001` to `MediaIngredientMech:000112`)

**Add single ingredient**:
```python
# 1. Find next ID
yaml_path = Path('data/curated/unmapped_ingredients.yaml')
highest = find_highest_id_single_file(yaml_path, 'MediaIngredientMech', 'ingredients')
next_id = generate_xmech_id('MediaIngredientMech', highest + 1)

# 2. Create record (see Workflow 1 above)
# 3. Append to data['ingredients']
# 4. Update data['total_count']
# 5. Save YAML
```

**Batch operation**:
```bash
python scripts/add_mediaingredientmech_ids.py --dry-run
python scripts/add_mediaingredientmech_ids.py
```

### CultureMech Quick Reference

**Current state**: 15,431 media (`CultureMech:000001` to `CultureMech:015431`)

**Add single medium**:
```python
# 1. Find next ID from registry
registry_path = Path('data/culturemech_id_registry.tsv')
highest = find_highest_id_from_registry(registry_path, 'CultureMech')
next_id = generate_xmech_id('CultureMech', highest + 1)

# 2. Create record (see Workflow 3 above)
# 3. Save to category directory
# 4. Update registry
```

**Batch operation**:
```bash
python scripts/assign_culturemech_ids.py --dry-run
python scripts/assign_culturemech_ids.py
```

**Rebuild registry**:
```python
rebuild_registry(
    Path('data/normalized_yaml'),
    Path('data/culturemech_id_registry.tsv')
)
```

### CommunityMech Quick Reference

**Current state**: 78 communities (`CommunityMech:000001` to `CommunityMech:000078`)

**Add single community**:
```python
# 1. Find next ID
communities_dir = Path('kb/communities')
highest = find_highest_id_multi_file(communities_dir, 'CommunityMech')
next_id = generate_xmech_id('CommunityMech', highest + 1)

# 2. Create record (see Workflow 2 above)
# 3. Save to communities directory
```

**Batch operation**:
```bash
python scripts/add_community_ids.py
```

## Integration with Other Tools

### Using with IngredientCurator

The `IngredientCurator` class in MediaIngredientMech handles ID preservation automatically:

```python
from mediaingredientmech.curation.ingredient_curator import IngredientCurator

curator = IngredientCurator(yaml_path='data/curated/unmapped_ingredients.yaml')

# IDs are preserved when loading
curator.load()

# When adding new ingredients manually, mint ID first
next_id = mint_next_id(
    Path('data/curated/unmapped_ingredients.yaml'),
    'MediaIngredientMech',
    'single_file',
    'ingredients'
)

# Then create record with ID
new_record = {
    'id': next_id,
    'preferred_term': 'New Ingredient',
    # ... other fields
}

# Curator preserves IDs when saving
curator.save()
```

### Using in Knowledge Graph Export

IDs serve as RDF subjects in KG exports:

```python
# Example KGX export
from kgx import Transformer

# MediaIngredientMech:000001 becomes RDF subject
subject = "MediaIngredientMech:000001"
predicate = "biolink:has_chemical_role"
object = "CHEBI:32599"

# Can be referenced from other entities
edge = {
    "subject": "CultureMech:000001",  # LB Medium
    "predicate": "biolink:has_part",
    "object": "MediaIngredientMech:000001"  # Sodium chloride
}
```

## Future Enhancements

**Not in current scope, but documented for future consideration**:

1. **Centralized xmech-common Package**
   - Shared ID utilities across all X-Mech repos
   - Consistent validation and minting logic
   - Cross-repo reference checking

2. **CLI Tool for ID Management**
   ```bash
   xmech-id mint MediaIngredientMech
   xmech-id validate data/curated/unmapped_ingredients.yaml
   xmech-id check-duplicates data/normalized_yaml/
   ```

3. **Automated CI/CD Validation**
   - Pre-commit hooks to validate IDs
   - GitHub Actions to check for duplicates
   - Automatic registry rebuilding

4. **ID Migration Utilities**
   - Safe renumbering with tombstone tracking
   - Cross-reference preservation
   - Migration audit trails

5. **Web UI for ID Management**
   - Visual gap detection
   - Duplicate resolution interface
   - Batch assignment dashboard


---

## Summary Decision Tree

```
┌─────────────────────────────────────┐
│ Need to add a new record?           │
└─────────────┬───────────────────────┘
              │
              ▼
    ┌─────────────────────┐
    │ What collection type?│
    └──────┬────────┬──────┘
           │        │
    Single │        │ Multi
    File   │        │ File
           ▼        ▼
    ┌──────────┐  ┌──────────┐
    │Find max  │  │Find max  │
    │in YAML   │  │across    │
    │array     │  │files     │
    └─────┬────┘  └─────┬────┘
          │             │
          │             ▼
          │      ┌──────────────┐
          │      │Has registry? │
          │      └───┬──────┬───┘
          │          │Yes   │No
          │          ▼      │
          │      ┌───────┐  │
          │      │Read   │  │
          │      │registry│ │
          │      └───┬───┘  │
          │          │      │
          └──────────┴──────┘
                     │
                     ▼
            ┌────────────────┐
            │Mint next ID:   │
            │max + 1         │
            └────────┬───────┘
                     │
                     ▼
            ┌────────────────┐
            │Create record   │
            │with ID first   │
            └────────┬───────┘
                     │
          ┌──────────┴────────────┐
          │                       │
    Single│                       │Multi
    File  ▼                       ▼
    ┌──────────┐          ┌──────────────┐
    │Append to │          │Create new    │
    │array     │          │YAML file     │
    │          │          │              │
    │Update    │          │Update        │
    │metadata  │          │registry?     │
    └─────┬────┘          └──────┬───────┘
          │                      │
          │                      │
          └──────────┬───────────┘
                     │
                     ▼
            ┌────────────────┐
            │Save changes    │
            └────────────────┘
```

