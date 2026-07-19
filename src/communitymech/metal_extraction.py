"""Metal and rare earth element extraction utilities for CommunityMech.

This module provides functions to extract metal and REE data from community YAML files
using a three-tiered approach:
1. CHEBI ID matching in metabolites
2. Environmental factor quantification
3. Description keyword matching with context validation
"""

import re
from pathlib import Path

import yaml

# Mapping from CHEBI IDs to MetalElementEnum values
METAL_CHEBI_MAP = {
    "CHEBI:29036": "COPPER",
    "CHEBI:29033": "IRON",
    "CHEBI:27363": "ZINC",
    "CHEBI:49786": "NICKEL",
    "CHEBI:48828": "COBALT",
    "CHEBI:27698": "VANADIUM",
    "CHEBI:27214": "URANIUM",
    "CHEBI:28073": "CHROMIUM",
    "CHEBI:25016": "LEAD",
    "CHEBI:49713": "LITHIUM",
    "CHEBI:29287": "GOLD",
    "CHEBI:30512": "SILVER",
    "CHEBI:33363": "PALLADIUM",
    "CHEBI:49631": "GALLIUM",
    "CHEBI:49464": "INDIUM",
    "CHEBI:33341": "TITANIUM",
}

# Mapping from CHEBI IDs to RareEarthElementEnum values
REE_CHEBI_MAP = {
    "CHEBI:32359": "LANTHANUM",
    "CHEBI:32998": "CERIUM",
    "CHEBI:49648": "PRASEODYMIUM",
    "CHEBI:33372": "NEODYMIUM",
    "CHEBI:33376": "SAMARIUM",
    "CHEBI:30688": "EUROPIUM",
    "CHEBI:33375": "GADOLINIUM",
    "CHEBI:33374": "TERBIUM",
    "CHEBI:49782": "DYSPROSIUM",
    "CHEBI:49649": "HOLMIUM",
    "CHEBI:49650": "ERBIUM",
    "CHEBI:33377": "THULIUM",
    "CHEBI:33378": "YTTERBIUM",
    "CHEBI:33382": "LUTETIUM",
    "CHEBI:49976": "YTTRIUM",
    "CHEBI:33330": "SCANDIUM",
}

# Keywords for metal detection in environmental factors and descriptions
METAL_KEYWORDS: dict[str, list[str]] = {
    "COPPER": ["copper", "cu2+", "cu(ii)", "cupric"],
    "IRON": ["iron", "fe2+", "fe3+", "fe(ii)", "fe(iii)", "ferrous", "ferric"],
    "ZINC": ["zinc", "zn2+", "zn(ii)"],
    "NICKEL": ["nickel", "ni2+", "ni(ii)"],
    "COBALT": ["cobalt", "co2+", "co(ii)"],
    "VANADIUM": ["vanadium", "v5+", "v(v)", "vanadate"],
    "URANIUM": ["uranium", "u6+", "u(vi)", "uranyl"],
    "CHROMIUM": ["chromium", "cr6+", "cr(vi)", "chromate"],
    "LEAD": ["lead", "pb2+", "pb(ii)"],
    "LITHIUM": ["lithium", "li+"],
    "GOLD": ["gold", "au", "au3+"],
    "SILVER": ["silver", "ag+", "ag(i)"],
    "PALLADIUM": ["palladium", "pd", "pd2+"],
    "GALLIUM": ["gallium", "ga3+"],
    "INDIUM": ["indium", "in3+"],
    "TITANIUM": ["titanium", "ti", "ti4+"],
}

# REE keywords
REE_KEYWORDS: dict[str, list[str]] = {
    "LANTHANUM": ["lanthanum", "la3+", "la(iii)"],
    "CERIUM": ["cerium", "ce3+", "ce4+", "ce(iii)", "ce(iv)"],
    "PRASEODYMIUM": ["praseodymium", "pr3+", "pr(iii)"],
    "NEODYMIUM": ["neodymium", "nd3+", "nd(iii)"],
    "SAMARIUM": ["samarium", "sm3+", "sm(iii)"],
    "EUROPIUM": ["europium", "eu3+", "eu(iii)"],
    "GADOLINIUM": ["gadolinium", "gd3+", "gd(iii)"],
    "TERBIUM": ["terbium", "tb3+", "tb(iii)"],
    "DYSPROSIUM": ["dysprosium", "dy3+", "dy(iii)"],
    "HOLMIUM": ["holmium", "ho3+", "ho(iii)"],
    "ERBIUM": ["erbium", "er3+", "er(iii)"],
    "THULIUM": ["thulium", "tm3+", "tm(iii)"],
    "YTTERBIUM": ["ytterbium", "yb3+", "yb(iii)"],
    "LUTETIUM": ["lutetium", "lu3+", "lu(iii)"],
    "YTTRIUM": ["yttrium", "y3+", "y(iii)"],
    "SCANDIUM": ["scandium", "sc3+", "sc(iii)"],
}

# Generic REE terms
GENERIC_REE_KEYWORDS = ["rare earth", "ree", "lanthanide"]

# Flatten keyword lists for easier searching
METAL_KEYWORDS_FLAT = [kw for keywords in METAL_KEYWORDS.values() for kw in keywords]
REE_KEYWORDS_FLAT = [kw for keywords in REE_KEYWORDS.values() for kw in keywords]


def keyword_in_text(keyword: str, text: str) -> bool:
    """Return True if keyword occurs in text as a standalone token.

    Plain substring matching falsely fires when short element symbols like
    'ti' or 'au' appear inside unrelated words ('characteristic',
    'Australia'). Anchor on non-alphanumeric boundaries (so 'au3+' still
    matches; '+' is non-alphanumeric). Case-insensitive.
    """
    pattern = rf"(?<![A-Za-z0-9]){re.escape(keyword)}(?![A-Za-z0-9])"
    return re.search(pattern, text, re.IGNORECASE) is not None


# Strong evidence context keywords for tier 3 extraction
STRONG_CONTEXT_KEYWORDS = [
    "bioleaching",
    "biomining",
    "reduction",
    "oxidation",
    "precipitation",
    "solubilization",
    "extraction",
    "recovery",
    "biosorption",
    "bioaccumulation",
    "bioremediation",
]


def extract_metals_from_community(yaml_path: Path) -> tuple[list[str], list[str], str, str]:
    """Extract metal/REE presence and relevance from community YAML.

    Uses a three-tiered extraction approach:
    1. CHEBI ID matching in metabolites (highest confidence)
    2. Environmental factor quantification (medium confidence)
    3. Description keyword matching with context validation (lower confidence)

    Args:
        yaml_path: Path to community YAML file

    Returns:
        Tuple of (metals_list, ree_list, relevance_enum, notes)
    """
    with open(yaml_path) as f:
        data = yaml.safe_load(f)

    metals: set[str] = set()
    ree: set[str] = set()
    notes_parts: list[str] = []

    # Tier 1: CHEBI ID matching in metabolites
    tier1_metals, tier1_ree = _extract_from_chebi_terms(data)
    metals.update(tier1_metals)
    ree.update(tier1_ree)

    if tier1_metals or tier1_ree:
        notes_parts.append("Metal/REE detected via CHEBI terms in metabolites")

    # Tier 2: Environmental factor quantification
    tier2_metals, tier2_ree = _extract_from_environmental_factors(data)
    metals.update(tier2_metals)
    ree.update(tier2_ree)

    if tier2_metals or tier2_ree:
        notes_parts.append("Metal/REE detected via environmental factor measurements")

    # Tier 3: Description keyword matching with context validation
    tier3_metals, tier3_ree, tier3_notes = _extract_from_description(data)
    metals.update(tier3_metals)
    ree.update(tier3_ree)

    if tier3_notes:
        notes_parts.append(tier3_notes)

    # Compute relevance based on category and evidence
    relevance = _compute_relevance(data, metals, ree)

    # Combine notes
    notes = "; ".join(notes_parts) if notes_parts else ""

    return sorted(metals), sorted(ree), relevance, notes


def _extract_from_chebi_terms(data: dict) -> tuple[set[str], set[str]]:
    """Extract metals/REE from CHEBI terms in metabolites (Tier 1)."""
    metals: set[str] = set()
    ree: set[str] = set()

    for interaction in data.get("ecological_interactions", []):
        for metabolite in interaction.get("metabolites", []):
            term = metabolite.get("term", {})
            chebi_id = term.get("id", "")

            if chebi_id in METAL_CHEBI_MAP:
                metals.add(METAL_CHEBI_MAP[chebi_id])
            elif chebi_id in REE_CHEBI_MAP:
                ree.add(REE_CHEBI_MAP[chebi_id])

    return metals, ree


def _extract_from_environmental_factors(data: dict) -> tuple[set[str], set[str]]:
    """Extract metals/REE from environmental factors with quantification (Tier 2)."""
    metals: set[str] = set()
    ree: set[str] = set()

    for factor in data.get("environmental_factors", []):
        name = factor.get("name", "").lower()
        value = factor.get("value")

        # Only add if quantified (has a value)
        if not value:
            continue

        # Check for metal keywords
        for metal, keywords in METAL_KEYWORDS.items():
            if any(keyword_in_text(kw, name) for kw in keywords):
                metals.add(metal)

        # Check for REE keywords
        for element, keywords in REE_KEYWORDS.items():
            if any(keyword_in_text(kw, name) for kw in keywords):
                ree.add(element)

    return metals, ree


def _extract_from_description(data: dict) -> tuple[set[str], set[str], str]:
    """Extract metals/REE from description with context validation (Tier 3)."""
    metals: set[str] = set()
    ree: set[str] = set()
    notes = ""

    # Combine description, name, and environment notes for searching
    text_parts = [
        data.get("description", ""),
        data.get("name", ""),
    ]

    env_term = data.get("environment_term", {})
    if env_term:
        text_parts.append(env_term.get("notes", ""))

    search_text = " ".join(text_parts).lower()

    # Check for strong evidence context
    has_strong_context = any(keyword_in_text(kw, search_text) for kw in STRONG_CONTEXT_KEYWORDS)

    if not has_strong_context:
        return metals, ree, notes

    # Only extract if strong context is present
    for metal, keywords in METAL_KEYWORDS.items():
        if any(keyword_in_text(kw, search_text) for kw in keywords):
            metals.add(metal)

    for element, keywords in REE_KEYWORDS.items():
        if any(keyword_in_text(kw, search_text) for kw in keywords):
            ree.add(element)

    # Check for generic REE mentions
    if any(keyword_in_text(kw, search_text) for kw in GENERIC_REE_KEYWORDS):
        notes = "Generic REE mention detected in description - manual curation recommended"

    if metals or ree:
        notes = "Metal/REE detected via keyword matching in description (context-validated)"

    return metals, ree, notes


def _compute_relevance(data: dict, metals: set[str], ree: set[str]) -> str:
    """Compute metal relevance based on category and evidence."""
    category = data.get("community_category", "")
    description = data.get("description", "").lower()

    # PRIMARY: Metal/REE is the main focus
    primary_categories = ["BIOMINING", "AMD", "METAL_REDUCTION"]
    if category in primary_categories and (metals or ree):
        return "PRIMARY"

    # Check for explicit biomining/bioleaching mentions
    if (metals or ree) and any(
        kw in description for kw in ["biomining", "bioleaching", "metal extraction"]
    ):
        return "PRIMARY"

    # SIGNIFICANT: Metal/REE plays an important but not primary role
    if (metals or ree) and category not in ["RHIZOSPHERE", "LIGNOCELLULOSE", "OTHER"]:
        # Has metals but not in categories where they're typically incidental
        return "SIGNIFICANT"

    # INCIDENTAL: Metal/REE mentioned but not central to function
    if metals or ree:
        return "INCIDENTAL"

    # NOT_APPLICABLE: No metal/REE relevance
    return "NOT_APPLICABLE"


def extract_all_metals_summary() -> dict[str, dict[str, int]]:
    """Generate a summary of all metals/REE across all communities.

    Returns:
        Dict with two keys ("metals", "ree") each mapping element name
        to its occurrence count across the community corpus.
    """
    community_dir = Path("kb/communities")
    metal_counts: dict[str, int] = {}
    ree_counts: dict[str, int] = {}

    for yaml_file in sorted(community_dir.glob("*.yaml")):
        metals, ree, _, _ = extract_metals_from_community(yaml_file)

        for metal in metals:
            metal_counts[metal] = metal_counts.get(metal, 0) + 1

        for element in ree:
            ree_counts[element] = ree_counts.get(element, 0) + 1

    return {"metals": metal_counts, "ree": ree_counts}
