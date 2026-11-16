-- Purpose: observe the eight unique NCBI identities in ten accepted occurrences.
-- Input: existing M5 NCBITaxon SQLite opened with sqlite3 -readonly.
-- Output: ordered identity rows only; no writes, source transfer or acquisition.
-- Serves the resident-input alternative for #2848; 2026-11-16.
SELECT subject, predicate, value, object
FROM statements
WHERE subject IN (
  'NCBITaxon:1148', 'NCBITaxon:470150', 'NCBITaxon:1390', 'NCBITaxon:86265',
  'NCBITaxon:89584', 'NCBITaxon:293', 'NCBITaxon:292', 'NCBITaxon:72361'
)
  AND (predicate = 'rdfs:label' OR predicate LIKE '%Synonym%'
       OR predicate LIKE '%rank%' OR predicate = 'rdfs:subClassOf')
ORDER BY subject, predicate, value, object;
