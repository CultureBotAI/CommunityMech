# EcoFAB source correction checkpoint

The final EcoFAB correction separates the four ring-trial treatments, the stock-preparation protocol and the reporter assay. It preserves the five graph nodes and four qualified arrows while removing unsupported member roles and member-specific causal claims. Four relative 16S read observations now name their treatment and harvest time. Seventeen source-reported IMG/GOLD pairs replace the invalid identifier range.

The primary evidence is the ring-trial article, Methods 4.1–4.2/4.8–4.9, Results 2.4, and S2 rows 2–18. Earlier independent source and guard review accepted the bounded correction. The five mutation controls passed again after the canonical write, using the frozen public predecessor fixture from commit `17616c9cad16a1b62cd6e9b39d82af4276e5188a`.

| Record | Current SHA256 | Generation 003 focused native gates |
| --- | --- | --- |
| 000025 EcoFAB | `7f5b0122647382d048e0b750d1c5f324b32f74868685d111db39d588c735b339` | 9 passed |
| 000516 dopamine | `304702c684faedb244d678e628ec174851dbdcafe46128eab86d824798e0482a` | 9 passed |
| 000087 Methods-defined LBNL | `bb31b1df4a9be2241453528101fc5d55657c23eccf1d58ce1cc9639e5912b368` | 8 passed; references failed on two Table S1 cells |

All gates executed at Git base `17616c9cad16a1b62cd6e9b39d82af4276e5188a` with the exact working-input hashes above. Persisted raw triplets are `.temp/phase2-science-20261115/linked-{ecofab,dopamine,lbnl}-{gate}-003.{json,log,exit}`. The LBNL failures are `discussions[4].evidence[2].snippet` (OAE516) and `discussions[4].evidence[4].snippet` (OAE603), retained under [issue 1996](https://github.com/CultureBotAI/CommunityMech/issues/1996). Actual assertion-comparison coverage will be measured after this source checkpoint is committed; no coverage count is inferred from the native issue counter.

The [six-step applied chain](applied-chain-ecofab-final-002/chain.json) preserves all actual before/after receipts and seven native sidecars. The earlier five-step checkpoint remains unchanged. The rejected sixth-step export with stale descriptive scope is retained privately; [issue 2824](https://github.com/CultureBotAI/CommunityMech/issues/2824) records the correction. [Issue 2823](https://github.com/CultureBotAI/CommunityMech/issues/2823) records the frozen-fixture correction, and [issue 2821](https://github.com/CultureBotAI/CommunityMech/issues/2821) records the new-prose spacing correction.

Native HTML generation completed for the changed record and derived indexes. This checkpoint is an applied source correction with focused technical evidence. The new full current scientific review, combined QC, release status and merge status are separate subsequent results; this report does not claim their completion.
