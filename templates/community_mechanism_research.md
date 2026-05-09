# Microbial Community Mechanism Research Template

## Target Community
- **Community name:** {community_name}
- **Community id:** {community_id}
- **Community file:** {community_file}
- **Community category:** {community_category}
- **Ecological state:** {ecological_state}
- **Community origin:** {community_origin}
- **Environment:** {environment_summary}
- **Description:** {description}

## Existing Record Context
- **Taxa:** {taxonomy_summary}
- **Known ecological interactions:** {interaction_summary}
- **Environmental factors:** {environmental_factor_summary}
- **Growth media / culture conditions:** {growth_media_summary}
- **Associated datasets / resources:** {dataset_summary}
- **Existing evidence:** {evidence_summary}

## Research Objective

Research the microbial community **{community_name}** as a candidate CommunityMech
mechanism record. Focus on source-backed community composition, ecological
interactions, mechanisms, environmental controls, cultivation conditions, and
datasets that can improve `kb/communities/{community_file}`.

## Required Findings

### 1. Community Scope
- Confirm the exact community composition and identify strain-level designations when available.
- If multiple publications report the same exact species composition, list them explicitly.
- Distinguish this community from related communities with overlapping taxa or environments.

### 2. Mechanistic Interactions
- Identify cross-feeding, syntrophy, mutualism, competition, detoxification, niche partitioning,
  colonization facilitation, and other mechanisms.
- For every proposed interaction, name the source taxon, target taxon, exchanged metabolite or
  process, and experimental evidence.

### 3. Environment and Conditions
- Identify ENVO-grounded environments where possible.
- Report growth media, temperature, atmosphere, substrates, electron donors/acceptors,
  perturbations, and measurement endpoints when available.

### 4. Evidence and Grounding
- Prefer primary literature, PubMed/PMC, DOI landing pages, NCBI, BioProject/SRA,
  KBase, BioModels, JGI/IMG/GOLD, NMDC, MGnify, and government/lab reports.
- Provide short verbatim snippets for every biological claim.
- Suggest CURIEs where available: NCBITaxon, ENVO, CHEBI, GO, PMID, DOI, BioProject,
  BioSample, SRA, BioModels, or KBase.
- Do not invent taxa, ontology ids, snippets, accession ids, or citations.

## Output Format

Return a curation-focused report with:
- A short scope summary.
- Confirmed taxa and strain designations.
- Candidate interaction updates in a table with reference, snippet, and explanation.
- Candidate environmental factor and growth-media updates.
- Dataset and external-resource links.
- DOI/PMID-first bibliography.
- Warnings for uncertain or weakly supported claims that should not yet be curated.
