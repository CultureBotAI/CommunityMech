# Undefined communities — tracking log (not in the resource)

CommunityMech records **defined** microbial communities (known, enumerable member
set). Some curated sources also describe **undefined** communities — donor-derived
faecal/environmental inocula, enrichment cultures, complex consortia with no
resolved membership. By policy these are **not** added to `kb/communities/`, but we
log them here so the observation (and its cultivation conditions) is not lost and a
later decision to include them is informed.

Each entry: the source, the defined-community record it was found alongside (if
any), a one-line description, the cultivation conditions reported, and why it is
excluded.

---

## Infant faecal fermentation (donor-derived)

- **Source:** Schwalbe et al., *Feeding-mode-defined microbial communities modulate
  prebiotic responses and alters colonic motility in early life*, bioRxiv 2026 —
  `doi:10.64898/2026.05.29.728681`
- **Found alongside:** `CommunityMech:000281` (Infant-gut Prebiotic-response SynCom
  — the *defined* six-member community from the same paper, which **is** in the KB)
- **Description:** In vitro fermentations of faecal samples from five exclusively
  breast-fed (BF) and five exclusively formula-fed (FF) infants; complex,
  donor-defined communities dominated by *Bifidobacterium* and *Bacteroides* with
  *Escherichia coli*, used as the physiological-relevance backdrop for the SynCom.
- **Cultivation conditions reported:**
  - Individual bioreactors (Cryptobiotix, Ghent) with 5 mL nutritional medium
    (M0017, Cryptobiotix)
  - Inoculated with faecal samples; supplemented with 5 g/L 2'-fucosyllactose,
    5 g/L galactooligosaccharides, 5 g/L lacto-N-tetraose, or a 5 g/L 1:4 mixture of
    2'FL and GOS, or plain medium (non-substrate control)
  - 37 °C, 24 h, anaerobic; sampling at 0 h (NSC only), 6 h, 24 h
  - Readouts: pH, gas production, flow-cytometry cell counts, SCFAs (GC-FID),
    lactate (spectrophotometric)
- **Excluded because:** membership is donor-defined and not enumerable — an
  undefined faecal community, not a defined consortium.
