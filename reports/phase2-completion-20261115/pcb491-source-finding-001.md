# PCB491: second-stage organism scope and interaction labels

Tracked in [issue2876](https://github.com/CultureBotAI/CommunityMech/issues/2876).

The source-context pass at `0f2c4915` identified a bounded scientific finding in
`kb/communities/TwoStep_PCB_Copper_Gold_Bioleaching_Consortium.yaml`
(CommunityMech:000491). Its description and final interaction attribute the
44.0% gold result to lixiviants from both Pseudomonas putida and P. fluorescens,
and its latter two nodes are labelled MUTUALISM. The retained primary abstract
instead identifies a pure P. putida WCS361 culture as the producer of the measured
cyanide preparation used for the subsequent gold result. It reports no reciprocal
microbial fitness observation supporting those interaction labels.

This establishes a mismatch between the encoded certainty/scope and the evidence
currently cited in the record. It does not establish that unread full-text or
supplementary material contains no additional experiment. The current DOI open
failed after redirecting to the publisher; only the retained abstract at
`references_cache/PMID_26704063.md`, lines55–70, was inspected directly here.
The native species-reference correction is separate and cannot resolve this
scientific finding.

Source: [Işıldar et al., Two-step bioleaching of copper and gold from discarded
printed circuit boards](https://doi.org/10.1016/j.wasman.2015.11.033), PMID26704063.

Follow-up should verify each organism and treatment in the main article, separate
the acidophile mixture from the pure-culture cyanide preparation and the subsequent
material-transfer step, and qualify interaction/role labels to the demonstrated
observations. Preserve the positive copper/gold outcomes, literal source text and
historical review bytes. Do not invent four-member simultaneous coculture or infer
benefit to one organism from recovery of a metal.

All-state GitHub issue searches for000491 and PCB found no matching owner for this
specific finding. Closed2079 concerns the batch report narrative; open1448 and
2173–2175 concern other e-waste records. This is a bounded source comparison, not
a full scientific assessment or permission to rewrite the canonical record.
