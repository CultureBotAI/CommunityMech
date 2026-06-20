# Copy-Paste Utility Module

*Reference for the **manage-identifiers** skill — see [`../skill.md`](../skill.md) for the CommunityMech overview and core workflow.*

---

## Complete Code Examples

### Utility Module (Copy-Paste Ready)

Save this as `src/mediaingredientmech/utils/id_utils.py` (or equivalent in other repos):

```python
"""Generic ID utilities for X-Mech repositories."""

import re
import yaml
from pathlib import Path
from typing import Optional


def parse_xmech_id(id_string: str, expected_prefix: str) -> Optional[int]:
    """Parse X-Mech ID and return number part.

    Args:
        id_string: ID to parse (e.g., "MediaIngredientMech:000001")
        expected_prefix: Expected prefix (e.g., "MediaIngredientMech")

    Returns:
        ID number (e.g., 1) or None if invalid
    """
    if not id_string or not id_string.startswith(f"{expected_prefix}:"):
        return None

    try:
        return int(id_string.split(':', 1)[1])
    except (IndexError, ValueError):
        return None


def generate_xmech_id(prefix: str, number: int) -> str:
    """Generate formatted X-Mech ID.

    Args:
        prefix: Repository name
        number: Sequential number (1-999999)

    Returns:
        Formatted ID (e.g., "MediaIngredientMech:000001")
    """
    return f"{prefix}:{number:06d}"


def validate_id_format(id_string: str, prefix: str) -> bool:
    """Validate ID matches expected format.

    Args:
        id_string: ID to validate
        prefix: Expected prefix

    Returns:
        True if valid, False otherwise
    """
    pattern = rf'^{re.escape(prefix)}:\d{{6}}$'
    return bool(re.match(pattern, id_string))


def find_highest_id_single_file(
    yaml_path: Path,
    prefix: str,
    collection_key: str = "ingredients"
) -> int:
    """Find highest ID in single-file YAML collection.

    Args:
        yaml_path: Path to YAML file
        prefix: ID prefix
        collection_key: YAML key for collection

    Returns:
        Highest ID number (0 if none found)
    """
    with open(yaml_path) as f:
        data = yaml.safe_load(f)

    max_id = 0
    for record in data.get(collection_key, []):
        id_str = record.get('id', '')
        if id_num := parse_xmech_id(id_str, prefix):
            max_id = max(max_id, id_num)

    return max_id


def find_highest_id_multi_file(
    directory: Path,
    prefix: str,
    pattern: str = "*.yaml"
) -> int:
    """Find highest ID across multiple YAML files.

    Args:
        directory: Directory to search (recursive)
        prefix: ID prefix
        pattern: Glob pattern for files

    Returns:
        Highest ID number (0 if none found)
    """
    max_id = 0

    for yaml_file in directory.rglob(pattern):
        try:
            with open(yaml_file) as f:
                data = yaml.safe_load(f)

            id_str = data.get('id', '')
            if id_num := parse_xmech_id(id_str, prefix):
                max_id = max(max_id, id_num)
        except Exception:
            continue

    return max_id


def mint_next_id(
    source: Path,
    prefix: str,
    collection_type: str = "single_file",
    collection_key: str = "ingredients"
) -> str:
    """Mint next available ID for a collection.

    Args:
        source: Path to YAML file or directory
        prefix: ID prefix (repo name)
        collection_type: "single_file" or "multi_file"
        collection_key: Collection key name (for single_file type)

    Returns:
        Next available ID string

    Raises:
        ValueError: If collection_type is invalid
    """
    if collection_type == "single_file":
        highest = find_highest_id_single_file(source, prefix, collection_key)
    elif collection_type == "multi_file":
        highest = find_highest_id_multi_file(source, prefix)
    else:
        raise ValueError(f"Unknown collection_type: {collection_type}")

    return generate_xmech_id(prefix, highest + 1)


# Example usage
if __name__ == "__main__":
    # MediaIngredientMech
    next_id = mint_next_id(
        Path('data/curated/unmapped_ingredients.yaml'),
        'MediaIngredientMech',
        'single_file',
        'ingredients'
    )
    print(f"Next MediaIngredientMech ID: {next_id}")

    # CommunityMech
    next_id = mint_next_id(
        Path('kb/communities'),
        'CommunityMech',
        'multi_file'
    )
    print(f"Next CommunityMech ID: {next_id}")
```

