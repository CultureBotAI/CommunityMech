# references_cache

Source text for evidence verification. `linkml-reference-validator` matches each
record's `EvidenceItem.snippet` against the file here for the reference it cites,
so a curated claim can be shown to come from the source it names.

## What may be kept here

- **Abstracts.** Retain PubMed or Europe PMC abstracts subject to the applicable
  source terms.
- **Full text with verified permission.** Check the actual license and terms for
  the particular version being cached. `scripts/cache_fulltext.py` filters on
  Europe PMC's open-access flag and refuses other records, but that flag alone
  does not verify redistribution permission for a curator-supplied copy.
- **Supplementary text**, in a separate `<stem>.supplement.md` — never merged
  into the article cache, because a snippet must not validate against text that
  is not the article.

## What may not

- **Publication PDFs.** Not here, not in `references_pdfs/`, not anywhere in the
  repository. Cite the DOI.
- **Paywalled or otherwise non-open-access article bodies**, however obtained.
  The curator-supplied-file path in `cache_fulltext.py` exists for open-access
  papers that no API will serve; it is not a way around the open-access check.

`tests/test_no_paywalled_text_in_repo.py` rejects PDFs and flags a publisher
rights assertion beside a body-sized cache file. Its size, rights-text and
Creative Commons marker checks are heuristics, not a license audit. A marker
exempts a file from this heuristic; it does not establish that its actual terms
permit the cached version or every intended use. Check those terms separately.

## Why the line is drawn there

This repository is **public**, and its `LICENSE` (BSD 3-Clause) covers the code
in it, not third-party article text stored beside that code. Third-party source
terms still apply. Neither an abstract, a freely readable article, an open-access
flag nor a license marker alone establishes permission for a particular use or
publication version. The cache policy requires checking those terms before
retaining full text.

## When removing text breaks a snippet

It will, and that is the correct outcome rather than a problem to route around.
A snippet taken from a paywalled Methods section is a claim this repository
cannot substantiate from anything it holds. Delete the evidence item. If that
leaves the claim with none, the evidence policy applies as written: omit the
claim or record uncertainty — **do not** restore the text to keep the validator
green.

#754 did exactly this: one 14 MB Elsevier PDF and five non-open-access bodies
were removed, 78 evidence items stopped verifying and were deleted, and 63
claims across 5 records were left needing re-evidencing from citable sources.

## Current-main refresh (2026-09-13, PR #766)

The same gate caught four later local-file article bodies. The refresh retains
their existing PubMed abstracts and removes 12 newly unverifiable evidence items
from the Drosophila five-species, altered Schaedler flora, and Trichodesmium
records. The combined PR removes 90 evidence items across eight records and
trims nine caches; scientific claims and interaction topology are preserved,
with re-evidencing still required where support was removed.

Europe PMC reports PMID:24242251, PMID:26323627, and PMID:28440800 as not open
access. PMID:25692519 has an open-access flag for an NIH author manuscript,
but the cached extraction was the publisher version with a rights assertion.
An open redistribution license for that version was not verified; the flag
alone does not establish permission for this particular cached copy. The
append-only publication-text-removal history records the public metadata URLs
and the version/license uncertainty. No copyright or gate exception was added.
