#!/usr/bin/env python3
"""
Analyze REVIEW cases from ncbitaxon_corrections.tsv and categorize them.

This script reads the corrections file, filters for REVIEW action cases,
and categorizes them into different issue types with recommendations.
"""

import csv
import re
from collections import defaultdict
from pathlib import Path


def load_review_cases(filepath):
    """Load all REVIEW cases from the TSV file."""
    review_cases = []
    with open(filepath, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f, delimiter='\t')
        for row in reader:
            if row['action'] == 'REVIEW':
                review_cases.append(row)
    return review_cases


def categorize_case(case):
    """
    Categorize a REVIEW case based on the issue type.

    Returns: (category_name, priority, details)
    """
    preferred_term = case['preferred_term']
    current_id = case['current_id']
    current_label = case['current_label']
    recommended_id = case['recommended_id']
    recommended_label = case['recommended_label']
    notes = case['notes']
    strain = case['strain']

    # Category 1: Taxonomy Renames (NCBI updated the official name)
    # ID is same, but labels differ significantly
    if current_id == recommended_id and current_label != recommended_label:
        # Check if it's a phylum-level rename (common in recent NCBI updates)
        phylum_renames = {
            'Proteobacteria': 'Pseudomonadota',
            'Acidobacteria': 'Acidobacteriota',
            'Actinobacteria': 'Actinomycetota',
            'Firmicutes': 'Bacillota',
            'Bacteroidetes': 'Bacteroidota',
        }

        if preferred_term in phylum_renames:
            return ('taxonomy_rename_phylum', 'MEDIUM', {
                'old_name': preferred_term,
                'new_name': recommended_label,
                'rename_type': 'Major phylum nomenclature update (2021 ICNP)',
            })
        else:
            return ('taxonomy_rename_species', 'MEDIUM', {
                'old_name': preferred_term,
                'new_name': recommended_label,
                'rename_type': 'Species name update in NCBI Taxonomy',
            })

    # Category 2: Wrong IDs (Completely incorrect - ID points to different organism)
    if current_label != 'NOT_FOUND' and not any([
        current_label.lower() in preferred_term.lower(),
        preferred_term.lower() in current_label.lower(),
        # Check if they share genus
        current_label.split()[0] == preferred_term.split()[0]
    ]):
        # Completely different organism
        return ('wrong_id', 'HIGH', {
            'expected': preferred_term,
            'got': current_label,
            'problem': 'ID points to completely different organism',
        })

    # Category 3: Strain-specific names (No strain ID available)
    if strain and 'Strain' in notes:
        return ('strain_not_found', 'MEDIUM', {
            'strain_name': strain,
            'species_level': recommended_label,
            'problem': 'Strain-specific entry not available in NCBITaxon',
        })

    # Category 4: Generic names (sp., bacterium, species, members, etc.)
    generic_patterns = [
        r'\bsp\b',
        r'\bbacterium\b',
        r'\bspecies\b',
        r'\bmembers\b',
        r'\bclone\b',
        r'\benvironmental\b',
        r'\blineage\b',
    ]

    if any(re.search(pattern, preferred_term, re.IGNORECASE) for pattern in generic_patterns):
        return ('generic_name', 'LOW', {
            'term': preferred_term,
            'genus_level': current_label,
            'problem': 'Generic designation cannot be precisely identified',
        })

    # Category 5: Ambiguous genus-level assignments
    # When current and recommended are the same but at genus level
    if current_id == recommended_id and current_label == recommended_label:
        # Check if it's just genus level
        if len(current_label.split()) == 1 and not current_label.endswith('aceae'):
            return ('ambiguous_genus', 'LOW', {
                'term': preferred_term,
                'genus': current_label,
                'problem': 'Multiple strains map to same genus-level ID',
            })

    # Category 6: Candidate/Provisional taxa
    if preferred_term.startswith('Candidatus') or preferred_term.startswith('Candidate'):
        return ('candidate_taxon', 'MEDIUM', {
            'term': preferred_term,
            'current': current_label,
            'problem': 'Provisional/uncultured taxon with uncertain classification',
        })

    # Category 7: Complex cases needing manual investigation
    return ('needs_investigation', 'HIGH', {
        'term': preferred_term,
        'current_id': current_id,
        'current_label': current_label,
        'recommended_id': recommended_id,
        'recommended_label': recommended_label,
        'notes': notes,
        'problem': 'Complex case requiring manual literature review',
    })


def analyze_reviews(filepath):
    """Main analysis function."""
    review_cases = load_review_cases(filepath)

    # Categorize all cases
    categorized = defaultdict(list)
    for case in review_cases:
        category, priority, details = categorize_case(case)
        categorized[category].append({
            'case': case,
            'priority': priority,
            'details': details,
        })

    return categorized, len(review_cases)


def generate_report(categorized, total_count, output_path):
    """Generate comprehensive human-readable report."""

    category_info = {
        'taxonomy_rename_phylum': {
            'title': 'Taxonomy Renames - Phylum Level (NCBI 2021+ Updates)',
            'recommendation': 'Update preferred_term to use new NCBI name, or add old name as synonym with note about literature usage.',
            'description': 'These IDs are correct but NCBI updated official phylum names in 2021 following ICNP rules.',
        },
        'taxonomy_rename_species': {
            'title': 'Taxonomy Renames - Species Level',
            'recommendation': 'Update preferred_term to current NCBI name, or document historical name usage.',
            'description': 'These IDs are correct but the official species name changed in NCBI Taxonomy.',
        },
        'wrong_id': {
            'title': 'Wrong IDs (Completely Incorrect)',
            'recommendation': 'URGENT: Find correct NCBITaxon ID using OAK search or manual NCBI lookup.',
            'description': 'These IDs point to the wrong organism entirely. Data is currently INCORRECT.',
        },
        'strain_not_found': {
            'title': 'Strain-Specific Names (No Strain-Level ID Available)',
            'recommendation': 'Use species-level ID + document specific strain in notes/description field.',
            'description': 'Literature specifies a strain but NCBITaxon lacks strain-level entry.',
        },
        'generic_name': {
            'title': 'Generic Names (sp., bacterium, species, etc.)',
            'recommendation': 'Use genus-level or family-level ID + add descriptive notes about strain/isolation.',
            'description': 'Organisms with generic designations that cannot be precisely identified.',
        },
        'ambiguous_genus': {
            'title': 'Ambiguous Genus-Level Assignments',
            'recommendation': 'Multiple strains map to same genus - acceptable if no species-level data available.',
            'description': 'Cases where multiple distinct strains/species map to the same genus-level ID.',
        },
        'candidate_taxon': {
            'title': 'Candidate/Provisional Taxa',
            'recommendation': 'Verify Candidatus name is in NCBI, otherwise use higher taxonomic level.',
            'description': 'Uncultured or provisional taxa with "Candidatus" or similar designations.',
        },
        'needs_investigation': {
            'title': 'Needs Manual Investigation',
            'recommendation': 'Review literature and perform detailed NCBI searches to resolve.',
            'description': 'Complex cases requiring careful manual review and literature consultation.',
        },
    }

    with open(output_path, 'w', encoding='utf-8') as f:
        # Header
        f.write("=" * 80 + "\n")
        f.write(f"REVIEW CASES ANALYSIS ({total_count} total)\n")
        f.write("=" * 80 + "\n\n")
        f.write("Generated from: ncbitaxon_corrections.tsv\n")
        f.write("Purpose: Categorize and prioritize taxonomy correction review cases\n\n")

        # Summary by category
        f.write("SUMMARY BY CATEGORY\n")
        f.write("-" * 80 + "\n")
        for cat_key in category_info.keys():
            count = len(categorized.get(cat_key, []))
            if count > 0:
                f.write(f"  {category_info[cat_key]['title']}: {count} cases\n")
        f.write("\n\n")

        # Detailed breakdown by category
        for cat_key, cat_info in category_info.items():
            cases = categorized.get(cat_key, [])
            if not cases:
                continue

            f.write("=" * 80 + "\n")
            f.write(f"Category: {cat_info['title']}\n")
            f.write("=" * 80 + "\n")
            f.write(f"Count: {len(cases)} cases\n")
            f.write(f"Priority: {cases[0]['priority']}\n\n")
            f.write(f"Description:\n{cat_info['description']}\n\n")
            f.write(f"Recommendation:\n{cat_info['recommendation']}\n\n")

            # List cases
            f.write("Cases:\n")
            f.write("-" * 80 + "\n")

            for i, item in enumerate(cases, 1):
                case = item['case']
                details = item['details']

                f.write(f"\n{i}. {case['preferred_term']}\n")
                f.write(f"   File: {case['file']}\n")
                f.write(f"   Current ID: NCBITaxon:{case['current_id']} ({case['current_label']})\n")
                f.write(f"   Recommended ID: NCBITaxon:{case['recommended_id']} ({case['recommended_label']})\n")

                if case['strain']:
                    f.write(f"   Strain: {case['strain']}\n")

                # Category-specific details
                if cat_key == 'taxonomy_rename_phylum':
                    f.write(f"   Old name: {details['old_name']} → New name: {details['new_name']}\n")
                    f.write(f"   Type: {details['rename_type']}\n")
                    f.write(f"   Action: Literature may use '{details['old_name']}' - document this\n")

                elif cat_key == 'taxonomy_rename_species':
                    f.write(f"   Old name: {details['old_name']} → New name: {details['new_name']}\n")
                    f.write(f"   Type: {details['rename_type']}\n")

                elif cat_key == 'wrong_id':
                    f.write(f"   PROBLEM: Expected '{details['expected']}' but ID points to '{details['got']}'\n")
                    f.write(f"   Action: URGENT - Search NCBI for correct ID\n")

                elif cat_key == 'strain_not_found':
                    f.write(f"   Strain requested: {details['strain_name']}\n")
                    f.write(f"   Available: {details['species_level']} (species level only)\n")
                    f.write(f"   Action: Use species-level ID, document strain in notes\n")

                elif cat_key == 'generic_name':
                    f.write(f"   Term: {details['term']}\n")
                    f.write(f"   Genus: {details['genus_level']}\n")
                    f.write(f"   Action: Use genus-level ID with descriptive notes\n")

                elif cat_key == 'candidate_taxon':
                    f.write(f"   Candidate taxon: {details['term']}\n")
                    f.write(f"   Current mapping: {details['current']}\n")
                    f.write(f"   Action: Verify in NCBI or use higher taxonomic rank\n")

                if case['notes']:
                    f.write(f"   Notes: {case['notes']}\n")

            f.write("\n\n")

    print(f"Report written to: {output_path}")


def generate_structured_tsv(categorized, output_path):
    """Generate structured TSV with categorized data."""

    rows = []
    for category, cases in categorized.items():
        for item in cases:
            case = item['case']
            rows.append({
                'category': category,
                'priority': item['priority'],
                'file': case['file'],
                'preferred_term': case['preferred_term'],
                'strain': case['strain'],
                'current_id': case['current_id'],
                'current_label': case['current_label'],
                'recommended_id': case['recommended_id'],
                'recommended_label': case['recommended_label'],
                'notes': case['notes'],
            })

    # Sort by priority then category
    priority_order = {'HIGH': 0, 'MEDIUM': 1, 'LOW': 2}
    rows.sort(key=lambda x: (priority_order[x['priority']], x['category'], x['file']))

    with open(output_path, 'w', encoding='utf-8', newline='') as f:
        fieldnames = ['category', 'priority', 'file', 'preferred_term', 'strain',
                     'current_id', 'current_label', 'recommended_id',
                     'recommended_label', 'notes']
        writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter='\t')
        writer.writeheader()
        writer.writerows(rows)

    print(f"Structured TSV written to: {output_path}")


def generate_high_priority_report(categorized, output_path):
    """Generate report of high-priority cases needing immediate attention."""

    high_priority_cases = []
    for category, cases in categorized.items():
        for item in cases:
            if item['priority'] == 'HIGH':
                high_priority_cases.append((category, item))

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("=" * 80 + "\n")
        f.write(f"HIGH PRIORITY REVIEW CASES ({len(high_priority_cases)} total)\n")
        f.write("=" * 80 + "\n\n")
        f.write("These cases require immediate attention as they represent incorrect or\n")
        f.write("ambiguous taxonomic assignments that could affect data integrity.\n\n")

        for i, (category, item) in enumerate(high_priority_cases, 1):
            case = item['case']
            details = item['details']

            f.write(f"\n{i}. {case['preferred_term']}\n")
            f.write(f"   Category: {category}\n")
            f.write(f"   File: {case['file']}\n")
            f.write(f"   Current: NCBITaxon:{case['current_id']} ({case['current_label']})\n")
            f.write(f"   Recommended: NCBITaxon:{case['recommended_id']} ({case['recommended_label']})\n")

            if category == 'wrong_id':
                f.write(f"\n   ⚠️  CRITICAL: This ID points to the WRONG organism!\n")
                f.write(f"   Expected: {details['expected']}\n")
                f.write(f"   Got: {details['got']}\n")
                f.write(f"   Action: Search NCBI Taxonomy database for correct ID\n")
                f.write(f"   Search query: \"{details['expected']}\"\n")

            elif category == 'needs_investigation':
                f.write(f"\n   ⚠️  COMPLEX: Requires manual investigation\n")
                f.write(f"   Problem: {details['problem']}\n")
                if details.get('notes'):
                    f.write(f"   Notes: {details['notes']}\n")

            f.write(f"\n" + "-" * 80 + "\n")

    print(f"High priority report written to: {output_path}")


def main():
    """Main execution function."""
    # File paths
    base_dir = Path(__file__).parent.parent
    corrections_file = base_dir / "ncbitaxon_corrections.tsv"
    output_dir = base_dir

    # Output files
    report_file = output_dir / "review_cases_analysis.txt"
    structured_file = output_dir / "review_cases_by_category.tsv"
    high_priority_file = output_dir / "high_priority_reviews.txt"

    print(f"Analyzing REVIEW cases from: {corrections_file}")
    print()

    # Analyze
    categorized, total_count = analyze_reviews(corrections_file)

    print(f"Found {total_count} REVIEW cases")
    print()

    # Generate outputs
    print("Generating reports...")
    generate_report(categorized, total_count, report_file)
    generate_structured_tsv(categorized, structured_file)
    generate_high_priority_report(categorized, high_priority_file)

    print()
    print("Analysis complete!")
    print()
    print("Generated files:")
    print(f"  1. {report_file} - Comprehensive human-readable report")
    print(f"  2. {structured_file} - Structured data for further analysis")
    print(f"  3. {high_priority_file} - High-priority cases requiring immediate attention")

    # Summary statistics
    print()
    print("Summary by priority:")
    priority_counts = defaultdict(int)
    for category, cases in categorized.items():
        for item in cases:
            priority_counts[item['priority']] += 1

    for priority in ['HIGH', 'MEDIUM', 'LOW']:
        count = priority_counts.get(priority, 0)
        if count > 0:
            print(f"  {priority}: {count} cases")


if __name__ == '__main__':
    main()
