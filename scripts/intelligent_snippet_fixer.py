#!/usr/bin/env python3
"""
Intelligent evidence snippet fixer with direct abstract fetching.

This tool directly fetches abstracts from PMID/DOI references and uses
context (organism name, functional role) to intelligently suggest the
best snippet from the abstract.

Usage:
    python scripts/intelligent_snippet_fixer.py --file FILENAME.yaml
    python scripts/intelligent_snippet_fixer.py --file FILENAME.yaml --auto-approve
    python scripts/intelligent_snippet_fixer.py --file FILENAME.yaml --only-invalid
"""

import argparse
import re
import shutil
import sys
from pathlib import Path
from typing import Dict, List, Tuple, Optional
import yaml

# Add src to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from communitymech.literature_enhanced import EnhancedLiteratureFetcher


class SnippetSuggestion:
    """Represents a suggested snippet fix with supporting data."""

    def __init__(
        self,
        organism: str,
        reference: str,
        current_snippet: str,
        suggested_snippets: List[str],
        abstract: str,
        confidence: str = "medium"
    ):
        self.organism = organism
        self.reference = reference
        self.current_snippet = current_snippet
        self.suggested_snippets = suggested_snippets
        self.abstract = abstract
        self.confidence = confidence

    def __repr__(self):
        return f"SnippetSuggestion(organism={self.organism}, ref={self.reference}, suggestions={len(self.suggested_snippets)})"


class IntelligentSnippetFixer:
    """Intelligent snippet fixer with context-aware abstract analysis."""

    def __init__(self, verbose: bool = False):
        self.fetcher = EnhancedLiteratureFetcher()
        self.verbose = verbose

    def extract_relevant_sentences(
        self,
        abstract: str,
        organism: str,
        context_keywords: Optional[List[str]] = None
    ) -> List[Tuple[str, float]]:
        """
        Extract relevant sentences from abstract based on organism and context.

        Args:
            abstract: Full abstract text
            organism: Organism name (e.g., "Acidithiobacillus ferrooxidans")
            context_keywords: Additional keywords to boost relevance (e.g., ["iron", "oxidation"])

        Returns:
            List of (sentence, score) tuples, sorted by relevance
        """
        if not abstract:
            return []

        # Split into sentences (simple approach)
        # Handle common abbreviations
        abstract = abstract.replace("sp.", "sp__")
        abstract = abstract.replace("nov.", "nov__")
        abstract = abstract.replace("et al.", "et al__")

        sentences = re.split(r'[.!?]\s+', abstract)

        # Restore abbreviations
        sentences = [s.replace("sp__", "sp.").replace("nov__", "nov__").replace("et al__", "et al.").strip() for s in sentences]

        # Filter out non-scientific content (author info, copyright, etc.)
        exclude_patterns = [
            r'^author information:',
            r'^copyright',
            r'^\(\d+\)',  # Author affiliations like (1), (2)
            r'^[A-Z][a-z]+ [A-Z]{1,3}\(\d+\)',  # Author names like "Smith AB(1)"
            r'[A-Z][a-z]+\s+[A-Z]{2,4}\(\d+\)',  # Author names anywhere: "Smith AB(1)"
            r'^[A-Z][a-z]+\s+[A-Z][A-Z]',  # Names like "Wakelin SA"
            r'@',  # Email addresses
            r'^\d{4}',  # Years at start (copyright years)
            r'^doi:',
            r'^pmid:',
            r'^published by',
            r'^all rights reserved',
            r'et al',  # Author lists
        ]

        filtered_sentences = []
        for s in sentences:
            s_lower = s.lower()
            # Skip if matches any exclude pattern
            if any(re.search(pattern, s_lower) for pattern in exclude_patterns):
                continue
            # Skip if very short or very long
            if not (50 <= len(s) <= 500):
                continue
            filtered_sentences.append(s)

        sentences = filtered_sentences

        if not sentences:
            return []

        # Score each sentence
        scored_sentences = []
        organism_parts = organism.lower().split()

        for sentence in sentences:
            sentence_lower = sentence.lower()
            score = 0.0

            # Check for organism name (full or partial)
            if organism.lower() in sentence_lower:
                score += 5.0
            else:
                # Check for genus name
                if organism_parts[0] in sentence_lower:
                    score += 2.0
                # Check for species epithet
                if len(organism_parts) > 1 and organism_parts[1] in sentence_lower:
                    score += 1.0

            # Check for context keywords
            if context_keywords:
                for keyword in context_keywords:
                    if keyword.lower() in sentence_lower:
                        score += 1.0

            # Prefer sentences with numerical data
            if re.search(r'\d+\.?\d*\s*%', sentence):
                score += 0.5
            if re.search(r'\d+\.?\d*\s*(mM|µM|mg/L|g/L|pH)', sentence):
                score += 0.5

            # Prefer sentences that are not the first (title) or last (generic)
            sentence_idx = sentences.index(sentence)
            if 0 < sentence_idx < len(sentences) - 1:
                score += 0.3

            # Penalty for very generic sentences
            generic_terms = ["paper", "study", "review", "article", "here we", "in this"]
            if any(term in sentence_lower for term in generic_terms):
                score -= 1.0

            # Bonus for sentences with scientific verbs (results/findings)
            scientific_verbs = [
                "showed", "demonstrated", "observed", "found", "indicated",
                "revealed", "exhibited", "contained", "produced", "reduced",
                "oxidized", "catalyzed", "dominated", "enriched"
            ]
            if any(verb in sentence_lower for verb in scientific_verbs):
                score += 0.5

            if score > 0:
                scored_sentences.append((sentence, score))

        # Sort by score (highest first)
        scored_sentences.sort(key=lambda x: x[1], reverse=True)

        return scored_sentences

    def suggest_snippets_for_evidence(
        self,
        organism: str,
        reference: str,
        current_snippet: str,
        context_keywords: Optional[List[str]] = None
    ) -> Optional[SnippetSuggestion]:
        """
        Fetch abstract and suggest better snippets for an evidence item.

        Args:
            organism: Organism name
            reference: Reference (PMID:xxx or doi:xxx)
            current_snippet: Current snippet (possibly invalid)
            context_keywords: Additional context keywords

        Returns:
            SnippetSuggestion object or None if abstract can't be fetched
        """
        if self.verbose:
            print(f"  Fetching abstract for {reference}...")

        # Route to optimized fetcher based on reference type
        if reference.upper().startswith("PMID:"):
            pmid = reference.replace("PMID:", "").replace("pmid:", "").strip()
            abstract = self.fetcher.fetch_pubmed_abstract(pmid)
        elif "doi" in reference.lower() or reference.startswith("10."):
            doi = reference.replace("doi:", "").replace("https://doi.org/", "").strip()
            abstract = self.fetcher.fetch_abstract_for_doi(doi)
        else:
            paper = self.fetcher.fetch_paper(reference, download_pdf=False)
            abstract = paper.get("abstract")

        if not abstract:
            if self.verbose:
                print(f"  ⚠️  Could not fetch abstract for {reference}")
            return None

        # Extract relevant sentences
        scored_sentences = self.extract_relevant_sentences(
            abstract, organism, context_keywords
        )

        if not scored_sentences:
            if self.verbose:
                print(f"  ⚠️  No relevant sentences found in abstract")
            return None

        # Take top 3 suggestions
        suggested_snippets = [sentence for sentence, score in scored_sentences[:3]]

        # Determine confidence based on top score
        top_score = scored_sentences[0][1]
        if top_score >= 5.0:
            confidence = "high"
        elif top_score >= 2.0:
            confidence = "medium"
        else:
            confidence = "low"

        return SnippetSuggestion(
            organism=organism,
            reference=reference,
            current_snippet=current_snippet,
            suggested_snippets=suggested_snippets,
            abstract=abstract,
            confidence=confidence
        )

    def extract_context_keywords(self, organism_notes: str, functional_roles: List[str]) -> List[str]:
        """
        Extract context keywords from organism notes and functional roles.

        Args:
            organism_notes: Full notes field for organism
            functional_roles: List of functional roles

        Returns:
            List of keywords
        """
        keywords = []

        # Extract from functional roles
        role_mapping = {
            "PRIMARY_DEGRADER": ["degradation", "degrader", "breakdown"],
            "PRODUCER": ["production", "produces", "synthesis"],
            "CONSUMER": ["consumption", "utilizes", "uptake"],
            "CROSS_FEEDER": ["cross-feeding", "exchange", "transfer"],
        }

        for role in functional_roles:
            if role in role_mapping:
                keywords.extend(role_mapping[role])

        # Extract key terms from notes (simple approach)
        # Look for metabolic terms
        metabolic_terms = [
            "oxidation", "reduction", "fermentation", "respiration",
            "fixation", "assimilation", "metabolism", "pathway",
            "iron", "sulfur", "nitrogen", "carbon", "hydrogen",
            "pH", "acid", "metal", "mineral"
        ]

        notes_lower = organism_notes.lower()
        for term in metabolic_terms:
            if term in notes_lower:
                keywords.append(term)

        return list(set(keywords))  # Remove duplicates


def analyze_yaml_file(
    yaml_path: Path,
    only_invalid: bool = False,
    verbose: bool = False
) -> List[Dict]:
    """
    Analyze a YAML file and identify evidence items needing snippet fixes.

    Covers all three sections: taxonomy, ecological_interactions, and
    environmental_factors.

    Args:
        yaml_path: Path to YAML file
        only_invalid: Only analyze items flagged as invalid by validation
        verbose: Print progress

    Returns:
        List of dicts with organism info and evidence needing fixes
    """
    with open(yaml_path, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)

    items_needing_fixes = []

    # --- taxonomy section ---
    taxonomy = data.get("taxonomy", [])
    for taxon_entry in taxonomy:
        taxon_term = taxon_entry.get("taxon_term", {})
        organism = taxon_term.get("preferred_term", "Unknown")
        notes = taxon_entry.get("notes", "")
        functional_roles = taxon_entry.get("functional_role", [])

        evidence_list = taxon_entry.get("evidence", [])
        for evidence in evidence_list:
            reference = evidence.get("reference", "")
            snippet = evidence.get("snippet", "")

            if not only_invalid or len(snippet) < 50:
                items_needing_fixes.append({
                    "organism": organism,
                    "reference": reference,
                    "current_snippet": snippet,
                    "notes": notes,
                    "functional_roles": functional_roles,
                    "section": "taxonomy"
                })

    # --- ecological_interactions section ---
    ecological_interactions = data.get("ecological_interactions", [])
    for interaction in ecological_interactions:
        name = interaction.get("name", "Unknown interaction")
        description = interaction.get("description", "")

        evidence_list = interaction.get("evidence", [])
        for evidence in evidence_list:
            reference = evidence.get("reference", "")
            snippet = evidence.get("snippet", "")

            if not only_invalid or len(snippet) < 50:
                items_needing_fixes.append({
                    "organism": name,
                    "reference": reference,
                    "current_snippet": snippet,
                    "notes": description,
                    "functional_roles": [],
                    "section": "ecological_interactions"
                })

    # --- environmental_factors section ---
    environmental_factors = data.get("environmental_factors", [])
    for factor in environmental_factors:
        name = factor.get("name", "Unknown factor")
        description = factor.get("description", "")

        evidence_list = factor.get("evidence", [])
        for evidence in evidence_list:
            reference = evidence.get("reference", "")
            snippet = evidence.get("snippet", "")

            if not only_invalid or len(snippet) < 50:
                items_needing_fixes.append({
                    "organism": name,
                    "reference": reference,
                    "current_snippet": snippet,
                    "notes": description,
                    "functional_roles": [],
                    "section": "environmental_factors"
                })

    if verbose:
        print(f"Found {len(items_needing_fixes)} evidence items to analyze")

    return items_needing_fixes


def apply_snippet_fix_to_yaml(
    yaml_path: Path,
    organism: str,
    reference: str,
    new_snippet: str,
    section: str = "taxonomy"
) -> bool:
    """
    Apply a snippet fix to the YAML file using proper YAML parsing.

    Supports all three sections: taxonomy, ecological_interactions, and
    environmental_factors.

    Args:
        yaml_path: Path to YAML file
        organism: Organism/interaction/factor name (for finding the right evidence item)
        reference: Reference (for finding the right evidence item)
        new_snippet: New snippet text
        section: YAML section to search ('taxonomy', 'ecological_interactions',
                 'environmental_factors')

    Returns:
        True if successful
    """
    # Load YAML
    with open(yaml_path, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)

    # Find and update the evidence item
    updated = False

    if section == "taxonomy":
        for taxon_entry in data.get("taxonomy", []):
            taxon_term = taxon_entry.get("taxon_term", {})
            current_organism = taxon_term.get("preferred_term", "")

            # Match organism (case-insensitive partial match)
            if organism.lower() not in current_organism.lower():
                continue

            for evidence in taxon_entry.get("evidence", []):
                if evidence.get("reference", "") == reference:
                    evidence["snippet"] = new_snippet
                    updated = True
                    break

            if updated:
                break

    elif section == "ecological_interactions":
        for interaction in data.get("ecological_interactions", []):
            current_name = interaction.get("name", "")
            if organism.lower() not in current_name.lower():
                continue

            for evidence in interaction.get("evidence", []):
                if evidence.get("reference", "") == reference:
                    evidence["snippet"] = new_snippet
                    updated = True
                    break

            if updated:
                break

    elif section == "environmental_factors":
        for factor in data.get("environmental_factors", []):
            current_name = factor.get("name", "")
            if organism.lower() not in current_name.lower():
                continue

            for evidence in factor.get("evidence", []):
                if evidence.get("reference", "") == reference:
                    evidence["snippet"] = new_snippet
                    updated = True
                    break

            if updated:
                break

    else:
        print(f"  ❌ Unknown section: '{section}'")
        return False

    if not updated:
        print(f"  ❌ Could not find evidence item with name='{organism}' and reference='{reference}' in section='{section}'")
        return False

    # Write back to YAML with nice formatting
    with open(yaml_path, 'w', encoding='utf-8') as f:
        yaml.dump(data, f, default_flow_style=False, allow_unicode=True, sort_keys=False, width=120)

    return True


def interactive_fix_workflow(
    yaml_path: Path,
    only_invalid: bool = False,
    auto_approve: bool = False,
    verbose: bool = False,
    relaxed: bool = False
):
    """
    Interactive workflow for fixing snippets in a YAML file.

    Args:
        yaml_path: Path to YAML file
        only_invalid: Only process items flagged as invalid
        auto_approve: Auto-approve all suggestions
        verbose: Print detailed progress
    """
    print(f"\n{'='*80}")
    print(f"INTELLIGENT SNIPPET FIXER")
    print(f"{'='*80}")
    print(f"File: {yaml_path.name}")
    mode_label = 'Auto-approve (relaxed)' if auto_approve and relaxed else ('Auto-approve' if auto_approve else 'Interactive review')
    print(f"Mode: {mode_label}")
    print(f"{'='*80}\n")

    # Analyze file
    items = analyze_yaml_file(yaml_path, only_invalid=only_invalid, verbose=verbose)

    if not items:
        print("✅ No evidence items need fixing")
        return

    print(f"📋 Found {len(items)} evidence items to process\n")

    # Create backup
    backup_path = yaml_path.with_suffix('.yaml.bak_intelligent')
    shutil.copy2(yaml_path, backup_path)
    print(f"💾 Created backup: {backup_path}\n")

    # Initialize fixer
    fixer = IntelligentSnippetFixer(verbose=verbose)

    applied_count = 0
    skipped_count = 0
    failed_count = 0

    for i, item in enumerate(items, 1):
        print(f"\n{'='*80}")
        print(f"Item {i}/{len(items)}")
        print(f"{'='*80}")
        print(f"Section:   {item.get('section', 'taxonomy')}")
        print(f"Organism:  {item['organism']}")
        print(f"Reference: {item['reference']}")
        print(f"\n❌ CURRENT snippet:")
        print(f"   {item['current_snippet'][:200]}{'...' if len(item['current_snippet']) > 200 else ''}")
        print()

        # Extract context keywords (notes, roles, and key words from current snippet)
        context_keywords = fixer.extract_context_keywords(
            item['notes'],
            item['functional_roles']
        )
        # Add significant words from current snippet as context hints
        current_words = [w.lower() for w in re.findall(r'[A-Za-z]{5,}', item['current_snippet'])]
        context_keywords = list(set(context_keywords + current_words[:8]))

        if verbose and context_keywords:
            print(f"🔍 Context keywords: {', '.join(context_keywords[:5])}")

        # Get suggestions
        suggestion = fixer.suggest_snippets_for_evidence(
            organism=item['organism'],
            reference=item['reference'],
            current_snippet=item['current_snippet'],
            context_keywords=context_keywords
        )

        if not suggestion:
            print(f"❌ Could not fetch abstract or find relevant snippets")
            failed_count += 1
            if not auto_approve:
                input("Press Enter to continue...")
            continue

        # Display suggestions
        print(f"✅ SUGGESTED snippets (confidence: {suggestion.confidence}):\n")
        for j, snippet in enumerate(suggestion.suggested_snippets, 1):
            print(f"  [{j}] {snippet}\n")

        if auto_approve:
            # In relaxed mode, apply all confidence levels (for verified-correct papers after reference fixes)
            # In normal mode, skip low confidence to avoid wrong-paper replacements
            if suggestion.confidence == "low" and not relaxed:
                print(f"⏭️  Auto-skipped (low confidence — review manually)")
                skipped_count += 1
                continue
            choice = '1'
        else:
            print("👉 Enter number to apply, [S]kip, [V]iew abstract, [Q]uit: ", end='')
            choice = input().strip().lower()

        if choice == 'q':
            print("\n🛑 Quitting")
            break
        elif choice == 's' or choice == '':
            print("⏭️  Skipped")
            skipped_count += 1
            continue
        elif choice == 'v':
            print(f"\n📄 FULL ABSTRACT:\n{suggestion.abstract}\n")
            print("👉 Enter number to apply, [S]kip, [Q]uit: ", end='')
            choice = input().strip().lower()
            if choice == 'q':
                break
            elif choice == 's' or choice == '':
                print("⏭️  Skipped")
                skipped_count += 1
                continue

        # Apply the selected snippet
        try:
            snippet_idx = int(choice) - 1
            if 0 <= snippet_idx < len(suggestion.suggested_snippets):
                selected_snippet = suggestion.suggested_snippets[snippet_idx]

                success = apply_snippet_fix_to_yaml(
                    yaml_path,
                    item['organism'],
                    item['reference'],
                    selected_snippet,
                    section=item.get('section', 'taxonomy')
                )

                if success:
                    print(f"✅ Applied snippet #{choice}")
                    applied_count += 1
                else:
                    print(f"❌ Failed to apply snippet")
                    failed_count += 1
            else:
                print(f"❌ Invalid choice: {choice}")
                skipped_count += 1
        except ValueError:
            print(f"❌ Invalid input: {choice}")
            skipped_count += 1

    # Summary
    print(f"\n{'='*80}")
    print(f"📊 SUMMARY")
    print(f"{'='*80}")
    print(f"✅ Applied:  {applied_count}")
    print(f"⏭️  Skipped:  {skipped_count}")
    print(f"❌ Failed:   {failed_count}")

    if applied_count > 0:
        print(f"\n💾 Updated file: {yaml_path}")
        print(f"💾 Backup saved: {backup_path}")
        print(f"\n🔍 Next: Validate with curate_evidence_with_pdfs.py")
    else:
        print("\n⚠️  No fixes were applied")
        if backup_path.exists():
            backup_path.unlink()


def main():
    parser = argparse.ArgumentParser(
        description='Intelligent evidence snippet fixer with direct abstract fetching'
    )
    parser.add_argument(
        '--file',
        required=True,
        help='YAML file to process (e.g., Australian_Lead_Zinc_Polymetallic.yaml)'
    )
    parser.add_argument(
        '--only-invalid',
        action='store_true',
        help='Only process evidence items with short snippets (likely invalid)'
    )
    parser.add_argument(
        '--auto-approve',
        action='store_true',
        help='Automatically apply top suggestion without prompting'
    )
    parser.add_argument(
        '--verbose',
        action='store_true',
        help='Print detailed progress'
    )
    parser.add_argument(
        '--relaxed',
        action='store_true',
        help='Apply low-confidence suggestions too (use after fixing wrong references)'
    )

    args = parser.parse_args()

    # Resolve path
    yaml_filename = args.file
    if not yaml_filename.endswith('.yaml'):
        yaml_filename += '.yaml'

    yaml_path = Path('kb/communities') / yaml_filename

    if not yaml_path.exists():
        print(f"❌ File not found: {yaml_path}")
        return 1

    # Run interactive workflow
    interactive_fix_workflow(
        yaml_path,
        only_invalid=args.only_invalid,
        auto_approve=args.auto_approve,
        verbose=args.verbose,
        relaxed=args.relaxed
    )

    return 0


if __name__ == '__main__':
    exit(main())
