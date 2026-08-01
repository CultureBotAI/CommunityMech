# Validation & Troubleshooting

*Reference for the **manage-identifiers** skill — see [`../SKILL.md`](../SKILL.md) for the CommunityMech overview and core workflow.*

---

## Validation and Troubleshooting

### Validating ID Format

**Python validator**:
```python
import re

def validate_id_format(id_string: str, prefix: str) -> bool:
    """Validate ID matches expected format.

    Args:
        id_string: ID to validate (e.g., "MediaIngredientMech:000001")
        prefix: Expected prefix (e.g., "MediaIngredientMech")

    Returns:
        True if valid, False otherwise

    Examples:
        >>> validate_id_format("MediaIngredientMech:000001", "MediaIngredientMech")
        True

        >>> validate_id_format("MediaIngredientMech:1", "MediaIngredientMech")
        False  # Not zero-padded

        >>> validate_id_format("CultureMech:000001", "MediaIngredientMech")
        False  # Wrong prefix
    """
    pattern = rf'^{re.escape(prefix)}:\d{{6}}$'
    return bool(re.match(pattern, id_string))

# Usage
is_valid = validate_id_format("MediaIngredientMech:000001", "MediaIngredientMech")
print(f"Valid: {is_valid}")  # True
```

### Finding Duplicate IDs

**Single-file collection**:
```python
from collections import Counter

def find_duplicate_ids(yaml_path: Path, collection_key: str = "ingredients") -> list[str]:
    """Find duplicate IDs in single-file collection."""
    with open(yaml_path) as f:
        data = yaml.safe_load(f)

    ids = [record.get('id') for record in data.get(collection_key, [])]
    counts = Counter(ids)

    duplicates = [id_str for id_str, count in counts.items() if count > 1]
    return duplicates

# Usage
yaml_path = Path('data/curated/unmapped_ingredients.yaml')
duplicates = find_duplicate_ids(yaml_path)
if duplicates:
    print(f"⚠️  Duplicate IDs found: {duplicates}")
else:
    print("✓ No duplicates")
```

**Multi-file collection**:
```python
from collections import defaultdict

def find_duplicate_ids_multi_file(directory: Path) -> dict[str, list[Path]]:
    """Find duplicate IDs across multiple files."""
    id_to_files = defaultdict(list)

    for yaml_file in directory.rglob('*.yaml'):
        try:
            with open(yaml_file) as f:
                data = yaml.safe_load(f)

            id_str = data.get('id')
            if id_str:
                id_to_files[id_str].append(yaml_file)
        except Exception:
            continue

    # Filter to only duplicates
    duplicates = {id_str: files for id_str, files in id_to_files.items() if len(files) > 1}
    return duplicates

# Usage
base_dir = Path('data/normalized_yaml')
duplicates = find_duplicate_ids_multi_file(base_dir)
if duplicates:
    for id_str, files in duplicates.items():
        print(f"⚠️  {id_str} found in {len(files)} files:")
        for file in files:
            print(f"   - {file}")
else:
    print("✓ No duplicates")
```

### Finding Gaps in Sequence

**Check for gaps**:
```python
def find_id_gaps(yaml_path: Path, prefix: str, collection_key: str = "ingredients") -> list[int]:
    """Find gaps in ID sequence for single-file collection."""
    with open(yaml_path) as f:
        data = yaml.safe_load(f)

    ids = []
    for record in data.get(collection_key, []):
        id_str = record.get('id', '')
        if match := re.match(rf'{prefix}:(\d+)', id_str):
            ids.append(int(match.group(1)))

    ids.sort()
    if not ids:
        return []

    # Find gaps
    expected = set(range(ids[0], ids[-1] + 1))
    actual = set(ids)
    gaps = sorted(expected - actual)

    return gaps

# Usage
yaml_path = Path('data/curated/unmapped_ingredients.yaml')
gaps = find_id_gaps(yaml_path, 'MediaIngredientMech')
if gaps:
    print(f"⚠️  Gaps found in sequence: {gaps}")
else:
    print("✓ No gaps (sequential)")
```

### Common Issues and Solutions

#### Issue 1: Duplicate IDs

**Symptom**: Same ID appears in multiple records

**Cause**: Manual editing, script error, or merge conflict

**Solution**:
```python
# Re-run batch assignment with force-overwrite
python scripts/add_mediaingredientmech_ids.py --force-overwrite

# Or manually fix in YAML and re-run without force
```

#### Issue 2: Incorrect Zero-Padding

**Symptom**: IDs like `MediaIngredientMech:1` instead of `MediaIngredientMech:000001`

**Cause**: Manual creation without using `f"{prefix}:{number:06d}"`

**Solution**:
```python
# Fix formatting
def fix_id_padding(id_string: str) -> str:
    """Fix ID zero-padding."""
    parts = id_string.split(':')
    if len(parts) == 2:
        prefix, number = parts
        return f"{prefix}:{int(number):06d}"
    return id_string

# Apply to all records
# (re-run batch script or manual fix)
```

#### Issue 3: Registry Out of Sync (CultureMech)

**Symptom**: Registry missing IDs or has wrong file paths

**Cause**: Manual file moves or registry not updated

**Solution**:
```python
# Rebuild registry from scratch
import pandas as pd
from pathlib import Path

def rebuild_registry(base_dir: Path, output_path: Path):
    """Rebuild CultureMech ID registry from YAML files."""
    records = []

    for yaml_file in base_dir.rglob('*.yaml'):
        try:
            with open(yaml_file) as f:
                data = yaml.safe_load(f)

            id_str = data.get('id')
            if id_str and id_str.startswith('CultureMech:'):
                records.append({
                    'culturemech_id': id_str,
                    'file_path': str(yaml_file)
                })
        except Exception:
            continue

    df = pd.DataFrame(records).sort_values('culturemech_id')
    df.to_csv(output_path, sep='\t', index=False)
    print(f"✓ Rebuilt registry with {len(df)} entries")

# Usage
rebuild_registry(
    Path('data/normalized_yaml'),
    Path('data/culturemech_id_registry.tsv')
)
```

#### Issue 4: Gaps in Sequence

**Symptom**: Missing IDs (e.g., 1, 2, 4, 5 - missing 3)

**Cause**: Deleted record, manual ID assignment, or migration

**Solution**:
```
This is usually fine! IDs are persistent - once assigned, they should never be reused.
If a record is deleted, its ID should remain unused (tombstone).

To fill gaps (NOT RECOMMENDED):
- Only if absolutely necessary for migration/cleanup
- Re-run batch assignment with sequential ordering
- Document the renumbering in changelog
```

