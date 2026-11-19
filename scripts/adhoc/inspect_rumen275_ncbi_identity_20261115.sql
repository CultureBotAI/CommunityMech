-- Purpose: inspect the local authority row that refused the rumen275 source binding.
-- Input: existing NCBITaxon SQLite, opened read-only; output: label/rank/synonym rows.
-- Serves #2888 source-canary diagnosis; 2026-11-15. No writes or external acquisition.
SELECT subject, predicate, value, object
FROM statements
WHERE subject = 'NCBITaxon:971'
  AND (predicate = 'rdfs:label' OR predicate LIKE '%Synonym%'
       OR predicate LIKE '%rank%' OR predicate = 'rdfs:subClassOf')
ORDER BY predicate, value, object;
