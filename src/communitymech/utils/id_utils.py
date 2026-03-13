"""Generic ID utilities for X-Mech repositories.

This module provides reusable functions for managing stable, sequential identifiers
across X-Mech repositories (MediaIngredientMech, CultureMech, CommunityMech, etc.).

Standard ID format: RepoName:NNNNNN (e.g., MediaIngredientMech:000001)

Usage:
    from communitymech.utils.id_utils import mint_next_id, generate_xmech_id

    # Mint next ID for multi-file collection (CommunityMech)
    next_id = mint_next_id(
        Path('kb/communities'),
        'CommunityMech',
        'multi_file'
    )

    # Mint next ID for single-file collection (MediaIngredientMech example)
    next_id = mint_next_id(
        Path('data/curated/unmapped_ingredients.yaml'),
        'MediaIngredientMech',
        'single_file',
        'ingredients'
    )

This module can be copied to other X-Mech repositories with minimal modifications.
"""

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

    Examples:
        >>> parse_xmech_id("MediaIngredientMech:000001", "MediaIngredientMech")
        1

        >>> parse_xmech_id("CultureMech:015431", "CultureMech")
        15431

        >>> parse_xmech_id("InvalidID", "MediaIngredientMech")
        None

        >>> parse_xmech_id("MediaIngredientMech:000001", "CultureMech")
        None
    """
    if not id_string or not id_string.startswith(f"{expected_prefix}:"):
        return None

    try:
        return int(id_string.split(':', 1)[1])
    except (IndexError, ValueError):
        return None


def generate_xmech_id(prefix: str, number: int) -> str:
    """Generate formatted X-Mech ID with zero-padding.

    Args:
        prefix: Repository name (e.g., "MediaIngredientMech")
        number: Sequential number (1-999999)

    Returns:
        Formatted ID (e.g., "MediaIngredientMech:000001")

    Examples:
        >>> generate_xmech_id("MediaIngredientMech", 1)
        'MediaIngredientMech:000001'

        >>> generate_xmech_id("CultureMech", 15431)
        'CultureMech:015431'

        >>> generate_xmech_id("CommunityMech", 78)
        'CommunityMech:000078'
    """
    return f"{prefix}:{number:06d}"


def validate_id_format(id_string: str, prefix: str) -> bool:
    """Validate ID matches expected format.

    Args:
        id_string: ID to validate
        prefix: Expected prefix

    Returns:
        True if valid, False otherwise

    Examples:
        >>> validate_id_format("MediaIngredientMech:000001", "MediaIngredientMech")
        True

        >>> validate_id_format("MediaIngredientMech:1", "MediaIngredientMech")
        False  # Not zero-padded

        >>> validate_id_format("CultureMech:000001", "MediaIngredientMech")
        False  # Wrong prefix

        >>> validate_id_format("Invalid:ID", "Invalid")
        False  # Wrong format
    """
    pattern = rf'^{re.escape(prefix)}:\d{{6}}$'
    return bool(re.match(pattern, id_string))


def find_highest_id_single_file(
    yaml_path: Path,
    prefix: str,
    collection_key: str = "ingredients"
) -> int:
    """Find highest ID in single-file YAML collection.

    For repositories that store all records in a single YAML file with a
    collection key (e.g., MediaIngredientMech).

    Args:
        yaml_path: Path to YAML file
        prefix: ID prefix (e.g., "MediaIngredientMech")
        collection_key: YAML key for collection (e.g., "ingredients")

    Returns:
        Highest ID number (0 if none found)

    Examples:
        >>> # For MediaIngredientMech
        >>> find_highest_id_single_file(
        ...     Path('data/curated/unmapped_ingredients.yaml'),
        ...     'MediaIngredientMech',
        ...     'ingredients'
        ... )
        112
    """
    try:
        with open(yaml_path) as f:
            data = yaml.safe_load(f)
    except FileNotFoundError:
        return 0

    if not data:
        return 0

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

    For repositories that store each record in a separate YAML file
    (e.g., CultureMech, CommunityMech).

    Args:
        directory: Directory to search (recursive)
        prefix: ID prefix (e.g., "CultureMech")
        pattern: Glob pattern for files (default: "*.yaml")

    Returns:
        Highest ID number (0 if none found)

    Examples:
        >>> # For CommunityMech
        >>> find_highest_id_multi_file(
        ...     Path('kb/communities'),
        ...     'CommunityMech'
        ... )
        78

        >>> # For CultureMech with nested directories
        >>> find_highest_id_multi_file(
        ...     Path('data/normalized_yaml'),
        ...     'CultureMech'
        ... )
        15431
    """
    if not directory.exists():
        return 0

    max_id = 0

    for yaml_file in directory.rglob(pattern):
        try:
            with open(yaml_file) as f:
                data = yaml.safe_load(f)

            if not data:
                continue

            id_str = data.get('id', '')
            if id_num := parse_xmech_id(id_str, prefix):
                max_id = max(max_id, id_num)
        except Exception:
            # Skip files that can't be parsed
            continue

    return max_id


def mint_next_id(
    source: Path,
    prefix: str,
    collection_type: str = "single_file",
    collection_key: str = "ingredients"
) -> str:
    """Mint next available ID for a collection.

    This is the main function for generating new IDs. It automatically
    finds the highest existing ID and returns the next sequential ID.

    Args:
        source: Path to YAML file (single_file) or directory (multi_file)
        prefix: ID prefix / repository name
        collection_type: "single_file" or "multi_file"
        collection_key: Collection key name (for single_file type only)

    Returns:
        Next available ID string

    Raises:
        ValueError: If collection_type is invalid

    Examples:
        >>> # MediaIngredientMech (single-file)
        >>> mint_next_id(
        ...     Path('data/curated/unmapped_ingredients.yaml'),
        ...     'MediaIngredientMech',
        ...     'single_file',
        ...     'ingredients'
        ... )
        'MediaIngredientMech:000113'

        >>> # CommunityMech (multi-file)
        >>> mint_next_id(
        ...     Path('kb/communities'),
        ...     'CommunityMech',
        ...     'multi_file'
        ... )
        'CommunityMech:000079'

        >>> # CultureMech (multi-file with nested dirs)
        >>> mint_next_id(
        ...     Path('data/normalized_yaml'),
        ...     'CultureMech',
        ...     'multi_file'
        ... )
        'CultureMech:015432'
    """
    if collection_type == "single_file":
        highest = find_highest_id_single_file(source, prefix, collection_key)
    elif collection_type == "multi_file":
        highest = find_highest_id_multi_file(source, prefix)
    else:
        raise ValueError(
            f"Unknown collection_type: {collection_type}. "
            f"Must be 'single_file' or 'multi_file'"
        )

    return generate_xmech_id(prefix, highest + 1)


def find_duplicate_ids_single_file(
    yaml_path: Path,
    collection_key: str = "ingredients"
) -> list[str]:
    """Find duplicate IDs in single-file collection.

    Args:
        yaml_path: Path to YAML file
        collection_key: Collection key name

    Returns:
        List of duplicate IDs (empty if none found)

    Examples:
        >>> find_duplicate_ids_single_file(
        ...     Path('data/curated/unmapped_ingredients.yaml')
        ... )
        []  # No duplicates
    """
    from collections import Counter

    try:
        with open(yaml_path) as f:
            data = yaml.safe_load(f)
    except FileNotFoundError:
        return []

    if not data:
        return []

    ids = [record.get('id') for record in data.get(collection_key, [])]
    counts = Counter(ids)

    duplicates = [id_str for id_str, count in counts.items() if count > 1 and id_str is not None]
    return duplicates


def find_id_gaps(
    yaml_path: Path,
    prefix: str,
    collection_key: str = "ingredients"
) -> list[int]:
    """Find gaps in ID sequence for single-file collection.

    Args:
        yaml_path: Path to YAML file
        prefix: ID prefix
        collection_key: Collection key name

    Returns:
        List of missing ID numbers in sequence

    Examples:
        >>> # If IDs are 1, 2, 4, 5 (missing 3)
        >>> find_id_gaps(
        ...     Path('data/curated/unmapped_ingredients.yaml'),
        ...     'MediaIngredientMech'
        ... )
        [3]
    """
    try:
        with open(yaml_path) as f:
            data = yaml.safe_load(f)
    except FileNotFoundError:
        return []

    if not data:
        return []

    ids = []
    for record in data.get(collection_key, []):
        id_str = record.get('id', '')
        if id_num := parse_xmech_id(id_str, prefix):
            ids.append(id_num)

    if not ids:
        return []

    ids.sort()

    # Find gaps
    expected = set(range(ids[0], ids[-1] + 1))
    actual = set(ids)
    gaps = sorted(expected - actual)

    return gaps


# Example usage and tests
if __name__ == "__main__":
    """Example usage for different X-Mech repositories."""

    print("=== X-Mech ID Utilities Example Usage ===\n")

    # Example 1: MediaIngredientMech (single-file)
    print("1. MediaIngredientMech (single-file collection)")
    yaml_path = Path('data/curated/unmapped_ingredients.yaml')
    if yaml_path.exists():
        highest = find_highest_id_single_file(yaml_path, 'MediaIngredientMech', 'ingredients')
        next_id = generate_xmech_id('MediaIngredientMech', highest + 1)
        print(f"   Highest ID: {highest}")
        print(f"   Next ID: {next_id}")

        duplicates = find_duplicate_ids_single_file(yaml_path)
        print(f"   Duplicates: {duplicates if duplicates else 'None'}")

        gaps = find_id_gaps(yaml_path, 'MediaIngredientMech')
        print(f"   Gaps: {gaps if gaps else 'None'}")
    else:
        print(f"   File not found: {yaml_path}")

    print()

    # Example 2: Validation
    print("2. ID Validation Examples")
    test_ids = [
        ("MediaIngredientMech:000001", "MediaIngredientMech"),
        ("MediaIngredientMech:1", "MediaIngredientMech"),  # Invalid (no padding)
        ("CultureMech:015431", "CultureMech"),
        ("Invalid:ID", "Invalid"),  # Invalid format
    ]

    for id_str, prefix in test_ids:
        is_valid = validate_id_format(id_str, prefix)
        status = "✓" if is_valid else "✗"
        print(f"   {status} {id_str} (prefix: {prefix})")

    print()

    # Example 3: Parsing IDs
    print("3. ID Parsing Examples")
    test_parse = [
        ("MediaIngredientMech:000001", "MediaIngredientMech"),
        ("CultureMech:015431", "CultureMech"),
        ("CommunityMech:000078", "CommunityMech"),
    ]

    for id_str, prefix in test_parse:
        number = parse_xmech_id(id_str, prefix)
        print(f"   {id_str} → {number}")

    print()

    # Example 4: Minting function
    print("4. Complete Minting Workflow")
    print("   # Single-file collection")
    print("   next_id = mint_next_id(")
    print("       Path('data/curated/unmapped_ingredients.yaml'),")
    print("       'MediaIngredientMech',")
    print("       'single_file',")
    print("       'ingredients'")
    print("   )")
    print()
    print("   # Multi-file collection")
    print("   next_id = mint_next_id(")
    print("       Path('kb/communities'),")
    print("       'CommunityMech',")
    print("       'multi_file'")
    print("   )")
