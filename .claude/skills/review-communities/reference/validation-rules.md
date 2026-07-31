# Validation Rule Definitions

*Reference for the **review-communities** skill — see [`../SKILL.md`](../SKILL.md) for the overview, workflows, and rule summary.*

---

### Rule Definitions

#### P1 - Critical Errors

**Rule P1.1: Ontology Term Existence**
```yaml
id: P1.1
description: Ontology term does not exist (404 from OAK)
check: OAK lookup returns None for term ID
impact: Broken link in knowledge graph
fix: Re-map to correct term or update to current ID
tools: just validate-terms FILE
```

**Rule P1.2: Invalid CURIE Format**
```yaml
id: P1.2
description: Ontology ID not valid CURIE (e.g., "NCBITaxon:562" vs "562")
check: Regex ^[A-Z]+:\d+$ for ontology IDs
impact: Parser failures in downstream systems
fix: Correct to valid CURIE format
tools: Schema validation catches this
```

**Rule P1.3: Schema Validation Failure**
```yaml
id: P1.3
description: YAML does not validate against LinkML schema
check: linkml-validate returns errors
impact: Cannot load community into datamodel
fix: Correct YAML structure to match schema
tools: just validate FILE
```

**Rule P1.4: Evidence Reference Invalid**
```yaml
id: P1.4
description: PMID/DOI reference does not exist or is inaccessible
check: PubMed/CrossRef API returns 404
impact: Citation cannot be verified
fix: Correct reference ID or remove if invalid
tools: just validate-references FILE
```

**Rule P1.5: Network Integrity Violation**
```yaml
id: P1.5
description: Interaction references non-existent taxon
check: Partner taxon ID not in community taxonomy
impact: Orphaned network edges in KG
fix: Add missing taxon or correct partner reference
tools: just audit-network
```

#### P2 - High-Priority Warnings

**Rule P2.1: Ontology Label Mismatch**
```yaml
id: P2.1
description: Term label doesn't match ontology (e.g., "E. coli" vs "Escherichia coli")
check: Compare label to OAK-fetched preferred label
impact: Confusing discrepancies, potential wrong mapping
fix: Update label to match ontology or verify mapping
tools: just validate-terms FILE
```

**Rule P2.2: Snippet Fuzzy Match Low**
```yaml
id: P2.2
description: Evidence snippet similarity < 70% with abstract
check: Fuzzy match score below threshold
impact: Citation may not support claim
fix: Update snippet or verify correct reference
tools: just validate-references FILE
```

**Rule P2.3: Missing Required Metadata**
```yaml
id: P2.3
description: Optional but important fields missing (e.g., description, environment_term)
check: Field is None or empty string
impact: Reduced discoverability and context
fix: Populate from literature or domain knowledge
tools: Manual curation
```

**Rule P2.4: Functional Role Mismatch**
```yaml
id: P2.4
description: Taxon's functional role inconsistent with interactions
check: E.g., PRIMARY_PRODUCER with no cross-feeding interactions
impact: Metadata doesn't reflect actual ecology
fix: Correct role or add missing interactions
tools: just audit-network
```

#### P3 - Medium-Priority Enrichment

**Rule P3.1: Growth Media Not Linked**
```yaml
id: P3.1
description: Growth media lacks CultureMech/MediaIngredientMech IDs
check: culturemech_id or media_ingredient_mech_id missing
impact: Reduced linkage to external resources
fix: Run media linking script
tools: just link-media
```

**Rule P3.2: Limited Evidence**
```yaml
id: P3.2
description: Community has < 3 evidence items
check: Count evidence items across all fields
impact: Less robust support for claims
fix: Add citations from literature
tools: Manual curation + literature search
```

**Rule P3.3: Synonyms Missing**
```yaml
id: P3.3
description: Taxon has no synonyms (common names, strains)
check: taxon_term.synonyms empty or None
impact: Reduced search/discovery
fix: Add from NCBI Taxonomy or literature
tools: Manual enrichment
```

**Rule P3.4: Environmental Factors Sparse**
```yaml
id: P3.4
description: < 3 environmental factors for non-minimal communities
check: Count environmental_factors list
impact: Incomplete environmental context
fix: Add pH, temperature, salinity from literature
tools: Manual curation
```

#### P4 - Low-Priority Suggestions

**Rule P4.1: External Resources Missing**
```yaml
id: P4.1
description: No external_resources links (GenBank, NCBI BioProject, etc.)
check: external_resources empty
impact: Less connected to external databases
fix: Add dataset links opportunistically
tools: Manual enrichment
```

**Rule P4.2: Metabolic Pathways Not Detailed**
```yaml
id: P4.2
description: Interactions lack detailed metabolite exchange info
check: Metabolites field empty in interaction
impact: Less mechanistic detail
fix: Add CHEBI-mapped metabolites from literature
tools: Manual curation
```

**Rule P4.3: Temporal Dynamics Missing**
```yaml
id: P4.3
description: No temporal information for dynamic communities
check: No time-series or succession data
impact: Static view of potentially dynamic system
fix: Add temporal metadata if available
tools: Future enhancement
```

---

