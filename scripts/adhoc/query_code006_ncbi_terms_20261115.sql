-- Purpose: current local authority rows for the three #2849 source taxon IDs.
-- Input: existing NCBITaxon SQLite opened with sqlite3 -readonly.
-- Output: JSON stdout, no database or canonical writes. 2026-11-15.
SELECT subject, predicate, value, object
FROM statements
WHERE subject IN ('NCBITaxon:1070896', 'NCBITaxon:1472881', 'NCBITaxon:53633')
  AND (predicate = 'rdfs:label' OR predicate LIKE '%Synonym%' OR predicate LIKE '%rank%')
ORDER BY subject, predicate, value, object;
