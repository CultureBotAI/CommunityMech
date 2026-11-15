-- Inspect exact JMP134 taxon labels/synonyms/rank/parent for #2848, 2026-11-15.
-- Input: existing NCBITaxon SQLite with sqlite3 -readonly; output JSON stdout.
SELECT subject, predicate, value, object
FROM statements
WHERE subject = 'NCBITaxon:264198'
  AND (predicate = 'rdfs:label' OR predicate LIKE '%Synonym%'
       OR predicate LIKE '%rank%' OR predicate = 'rdfs:subClassOf')
ORDER BY predicate, value, object;
