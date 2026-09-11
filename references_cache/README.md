# references_cache

Source text for evidence verification. `linkml-reference-validator` matches each
record's `EvidenceItem.snippet` against the file here for the reference it cites,
so a curated claim can be shown to come from the source it names.

## What may be kept here

- **Abstracts.** Retrieved from PubMed or Europe PMC for any cited reference.
- **Open-access full text.** Only where Europe PMC reports the record as open
  access. `scripts/cache_fulltext.py` enforces this and refuses anything else:
  `[skip] <id>: not open-access in Europe PMC`.
- **Supplementary text**, in a separate `<stem>.supplement.md` — never merged
  into the article cache, because a snippet must not validate against text that
  is not the article.

## What may not

- **Publication PDFs.** Not here, not in `references_pdfs/`, not anywhere in the
  repository. Cite the DOI.
- **Paywalled or otherwise non-open-access article bodies**, however obtained.
  The curator-supplied-file path in `cache_fulltext.py` exists for open-access
  papers that no API will serve; it is not a way around the open-access check.

`tests/test_no_paywalled_text_in_repo.py` enforces both, by looking for PDFs
anywhere in the tree and for a publisher rights assertion beside a body-sized
cache file. A Creative Commons marker exempts a file, since the text is then
redistributable whatever boilerplate sits next to it.

## Why the line is drawn there

This repository is **public**, and its `LICENSE` (BSD 3-Clause) covers the code
in it, not third-party article text stored beside that code. Abstracts and
open-access full text carry terms that permit what this cache does with them;
subscription article bodies do not.

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
