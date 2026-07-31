window.searchData = [
 {
  "discussion_id": "kg-dv-acetate-co2-to-mc-methanogenesis",
  "prompt": "Does D. vulgaris fermentation of lactate to acetate and CO2 causally enhance acetoclastic methanogenesis by M. concilii, i.e. is there a second (D. vulgaris-derived) carbon route to methane beyond the direct R. cellulolyticum \u2192 M. concilii hand-off?",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "Cellulose-to-Methane Quad-Culture SynCom",
  "source_id": "CommunityMech:000089",
  "source_file": "Cellulose_Methane_Quad_Culture_SynCom.yaml",
  "attaches_to": [
   "ecological_interactions#R. cellulolyticum acetate cross-feeding to M. concilii"
  ],
  "rationale": "If confirmed, D. vulgaris would be a secondary acetate/CO2 supplier to the acetoclastic methanogen, adding a parallel carbon route to methane and changing how the causal graph attributes methane output between the two carbon sources. The source paper proposes it mechanistically (\"it may be\") but does not demonstrate the D. vulgaris \u2192 M. concilii carbon edge directly, so it is recorded here as a knowledge gap rather than asserted as an ecological interaction.",
  "num_experiments": 0,
  "num_evidence": 1,
  "evidence_refs": [
   "PMID:36847519"
  ],
  "posed_by": "",
  "page_url": "../docs/communities/Cellulose_Methane_Quad_Culture_SynCom.html#kg-dv-acetate-co2-to-mc-methanogenesis"
 },
 {
  "discussion_id": "kg-dietsimp-proposed-diet-no-causal-edge",
  "prompt": "Are the S. globosa\u2192M. mazei and C. aceticum\u2192M. mazei DIET pathways experimentally validated (direct interspecies electron transfer vs H2/formate mediation), and is there any causal dependency between the two parallel donor\u2192methanogen relationships?\n",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "DIET-based Simplified Lignocellulose-to-Methane Consortia (DIETsimp)",
  "source_id": "CommunityMech:000297",
  "source_file": "DIETsimp_Lignocellulose_to_Methane_DIET_Consortia.yaml",
  "attaches_to": [
   "ecological_interactions#DIET syntrophy from S. globosa to M. mazei",
   "ecological_interactions#DIET syntrophy from C. aceticum to M. mazei"
  ],
  "rationale": "An Edison causal-graph pass (PMID:42229598) found no justifiable directed causal edge for this consortium: both interactions are recorded as \"Proposed DIET pathway\", the primary full text was inaccessible, and no perturbation (donor-removal, inhibitor, mono-/co-culture, or knockout) evidence was retrieved. The source supports two parallel donor\u2192methanogen proposals, not a causal dependency of one on the other, so no `downstream` edge was added. Neutral-red-mediated electron delivery to M. mazei reported in a different system must not be imported here without exact-system verification.\n",
  "num_experiments": 0,
  "num_evidence": 1,
  "evidence_refs": [
   "PMID:42229598"
  ],
  "posed_by": "",
  "page_url": "../docs/communities/DIETsimp_Lignocellulose_to_Methane_DIET_Consortia.html#kg-dietsimp-proposed-diet-no-causal-edge"
 },
 {
  "discussion_id": "kg-geobacter-clostridium-contact-dependence-contested",
  "prompt": "Is the G. sulfurreducens-induced metabolic shift in C. pasteurianum actually caused by contact-dependent direct interspecies electron transfer along conductive pili, or by a diffusible mediator (candidate: a cobamide) released by G. sulfurreducens?\n",
  "kind": "CONTROVERSY",
  "status": "OPEN",
  "is_gap": "Other discussion",
  "source_name": "Geobacter-Clostridium Interspecies Electron Transfer Coculture",
  "source_id": "CommunityMech:000031",
  "source_file": "Geobacter_Clostridium_Interspecies_Electron_Transfer_Coculture.yaml",
  "attaches_to": [
   "ecological_interactions#Acetate Oxidation and Interspecies Electron Transfer",
   "ecological_interactions#Glycerol Fermentation with Electron-Transfer-Induced Metabolic Shift"
  ],
  "rationale": "RE-SCOPED (was: this record asserted contact-dependent DIET as established). Caching the open-access full text of the discovery study (PMID:28287150, PMC5347079) showed the contact/nanowire mechanism was never supported by it. \"Pili\" and \"nanowires\" appear there only as general background about Geobacter species, and its own discussion states the opposite of what this record claimed: pre-cultures were \"constituted of both nanowire-rich aggregates and nanowire-poor planktonic cells\", and growing G. sulfurreducens on conductive material is offered as a future option \"to ensure electrical connections\" - i.e. electrical connection was NOT established in these experiments. Several evidence items had also cited that generic background sentence, or the unrelated \"sole electron acceptor\" sentence, as if they demonstrated contact-mediated transfer between these two organisms.\nAccordingly: `community_category` moved DIET -> SYNTROPHY (the schema defines DIET specifically as \"Direct interspecies electron transfer\", a mechanism claim no source supports here); pili/nanowire assertions were removed from the description, environment notes, taxon notes, and the interaction; the interactions were renamed to mechanism-neutral forms; and the \"Cell Contact and Nanowire Formation\" environmental factor became \"Electrical Connection Between Cells\", recording that connection was not established.\nThe competing mechanism is NOT asserted in its place. The follow-up (PMID:34939136) concludes the interaction \"is mediated\" and proposes a diffusible cobamide acting on glycerol dehydratase, with a transmembrane flavin-bound polyferredoxin / cytochrome b5-rubredoxin electron-entry route offered only as putative reinforcement - and that paper calls its own model \"putative\". It is not open access, so only its abstract is snippet-verifiable here; its reported 0.22-um-filtered cell-free spent-medium result, which would show Geobacter cells are unnecessary for the shift, remains unverified against full text. STILL OPEN: which route actually carries the electrons, and whether the record's `name` and filename (both still say \"DIET\") should be changed - those affect external references and were left to a curator.\n",
  "num_experiments": 0,
  "num_evidence": 3,
  "evidence_refs": [
   "PMID:34939136",
   "PMID:34939136",
   "PMID:34939136"
  ],
  "posed_by": "",
  "page_url": "../docs/communities/Geobacter_Clostridium_Interspecies_Electron_Transfer_Coculture.html#kg-geobacter-clostridium-contact-dependence-contested"
 },
 {
  "discussion_id": "kg-geobacter-methanosaeta-acetate-route-unresolved",
  "prompt": "Alongside DIET-driven CO2 reduction, does M. harundinacea also cross-feed on the acetate generated by G. metallireducens ethanol oxidation, and what fraction of methane comes from each route in this defined coculture?\n",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "Geobacter-Methanosaeta DIET Community",
  "source_id": "CommunityMech:000032",
  "source_file": "Geobacter_Methanosaeta_DIET.yaml",
  "attaches_to": [
   "ecological_interactions#Ethanol Oxidation and Direct Electron Transfer",
   "ecological_interactions#Direct Electron Acceptance and Methanogenesis"
  ],
  "rationale": "A causal-graph pass on this record proposed an additional acetate cross-feeding node and an acetate -> methanogenesis edge, on the reasoning that Methanosaeta is classically an acetoclastic genus and that ethanol oxidation by G. metallireducens yields acetate, giving an overall stoichiometry near 1.5 mol CH4 per mol ethanol. That claim is NOT curated here as an interaction: the primary source (doi:10.1039/C3EE42189A) is cached abstract-only and its full text was not retrievable, and the abstract states only that M. harundinacea \"accepted electrons via DIET for the reduction of carbon dioxide to methane\" - it does not report acetate cross-feeding, the acetate/DIET split, or the per-route methane stoichiometry. The supporting quotations offered for the acetate route came from secondary reviews attributing findings to this study, which per this repo's conservative-curation rule (see CommunityMech:000176) is not a sufficient basis for an exact-system causal edge. Resolving this needs the primary full text or a radiotracer/isotope partition experiment in this exact coculture.\n",
  "num_experiments": 0,
  "num_evidence": 1,
  "evidence_refs": [
   "doi:10.1039/C3EE42189A"
  ],
  "posed_by": "",
  "page_url": "../docs/communities/Geobacter_Methanosaeta_DIET.html#kg-geobacter-methanosaeta-acetate-route-unresolved"
 },
 {
  "discussion_id": "kg-ornl-exchanged-products-and-edge-strength",
  "prompt": "Which exact C. cellulolyticum fermentation products are transferred to D. vulgaris and G. sulfurreducens, and is the electron-acceptor to cross-feeding coupling perturbation-demonstrated rather than only abstract-level implied?\n",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "ORNL Clostridium-Desulfovibrio-Geobacter Trophic Model Community",
  "source_id": "CommunityMech:000176",
  "source_file": "ORNL_Clostridium_Desulfovibrio_Geobacter_Trophic_Model.yaml",
  "attaches_to": [
   "ecological_interactions#Sulfate-Linked Dependence of D. vulgaris",
   "ecological_interactions#Fumarate-Linked Dependence of G. sulfurreducens"
  ],
  "rationale": "The curated donor-to-partner causal edges rest on the abstract statement that the partners \"derived carbon and energy from the metabolic products\" of C. cellulolyticum; the primary full text (doi:10.1186/1471-2180-10-149) was not retrievable, so the exact exchanged metabolites and any sulfate/fumarate-removal or inhibitor perturbation evidence remain unresolved. Products reported for a related two-species C. cellulolyticum / G. sulfurreducens fuel-cell system (acetate, ethanol, H2) must NOT be imported here without exact-system verification.\n",
  "num_experiments": 0,
  "num_evidence": 1,
  "evidence_refs": [
   "doi:10.1186/1471-2180-10-149"
  ],
  "posed_by": "",
  "page_url": "../docs/communities/ORNL_Clostridium_Desulfovibrio_Geobacter_Trophic_Model.html#kg-ornl-exchanged-products-and-edge-strength"
 },
 {
  "discussion_id": "kg-syntrophobacter-methanobacterium-partner-attribution",
  "prompt": "Which curated claims about this consortium rest on exact-pair (S. fumaroxidans + M. formicicum) evidence, and which were imported from S. fumaroxidans + M. hungatei experiments?\n",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "Syntrophobacter-Methanobacterium Syntrophic Consortium",
  "source_id": "CommunityMech:000068",
  "source_file": "Syntrophobacter_Methanobacterium_Syntrophy.yaml",
  "attaches_to": [
   "ecological_interactions#Propionate Oxidation and H2/Formate Production",
   "ecological_interactions#Interspecies Electron Transfer and Methanogenesis"
  ],
  "rationale": "Several evidence items on this record quote doi:10.1099/00207713-48-4-1383 (Harmsen et al. 1998), whose syntrophic coculture passage names *Methanospirillum hungateii*, not this record's partner *Methanobacterium formicicum*. Two of those items previously carried explanations asserting that the passage established M. formicicum as the partner; they have been corrected and downgraded to PARTIAL, and exact-pair support has been added from PMID:29611893 (Sedano-Nunez et al. 2018), which explicitly grew S. fumaroxidans in syntrophy with M. formicicum. The residual gap: the frequently cited biochemical formate-transfer and FDH/hydrogenase transcription results for this system were obtained with M. hungatei, so carrier apportionment (\"formate is the dominant carrier\") must NOT be curated as an exact-pair finding.\nPARTLY RESOLVED: the 2024 exact-pair perturbation study (Li et al., Water 16:3551, doi:10.3390/w16243551) is now ingested - its full text was supplied by a curator from the publisher PDF, since the journal is absent from PubMed and Europe PMC and MDPI blocks programmatic download. Its graded-formate results for the exact S. fumaroxidans-M. formicicum coculture are curated under the Exogenous Formate Dosage environmental factor, and its FDH downregulation result on the Propionate Oxidation interaction. Two cautions came out of that ingestion: (a) the paper runs an anaerobic-sludge system ALONGSIDE the coculture, and sludge-only results (e.g. Acetobacterium homoacetogenesis rising with formate dose) must not be attributed to this two-member consortium; (b) the dose response is non-monotonic - 30 mM recovers in the later stage - so it is NOT a simple \">=30 mM inhibits\" threshold.\nStill open: carrier apportionment between H2 and formate for the M. formicicum pair specifically, which no retrieved study resolves with an isotope or selective-inhibition experiment.\n",
  "num_experiments": 0,
  "num_evidence": 2,
  "evidence_refs": [
   "PMID:29611893",
   "doi:10.1099/00207713-48-4-1383"
  ],
  "posed_by": "",
  "page_url": "../docs/communities/Syntrophobacter_Methanobacterium_Syntrophy.html#kg-syntrophobacter-methanobacterium-partner-attribution"
 },
 {
  "discussion_id": "kg-aggregation-and-diet-unverified",
  "prompt": "Does syntrophic aggregation / cell-to-cell attraction causally enhance butyrate oxidation or methanogenesis in this coculture, and is direct interspecies electron transfer (e.g. the reported carbon-nanotube methane stimulation) involved rather than only H2/formate transfer?\n",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "Syntrophomonas-Methanococcus Butyrate Growth Coordination Coculture",
  "source_id": "CommunityMech:000189",
  "source_file": "Syntrophomonas_Methanococcus_Butyrate_Growth_Coordination_Coculture.yaml",
  "attaches_to": [
   "ecological_interactions#Syntrophic Aggregation and Cell-to-Cell Attraction"
  ],
  "rationale": "Aggregation and disturbance-resistant cell-to-cell attraction are observed, but no experiment demonstrates that aggregation increases butyrate oxidation or methane production in this exact coculture, so no aggregation\u2192enhancement `downstream` edge was added. Likewise, carbon-nanotube acceleration of methane production is reported, but DIET \"does not always explain the enhancement of methane production\" and was not directly proven here, so a DIET mechanism is not asserted.\n",
  "num_experiments": 0,
  "num_evidence": 1,
  "evidence_refs": [
   "PMID:34603271"
  ],
  "posed_by": "",
  "page_url": "../docs/communities/Syntrophomonas_Methanococcus_Butyrate_Growth_Coordination_Coculture.html#kg-aggregation-and-diet-unverified"
 },
 {
  "discussion_id": "kg-es5-mediation-mechanism-unresolved",
  "prompt": "Does T. flocculiformis ES5 improve the S. wolfei / M. hungatei syntrophy via co-aggregation-based spatial bridging (possible DIET) or via the observed proteomic changes, and is either mechanism causal rather than correlative?\n",
  "kind": "KNOWLEDGE_GAP",
  "status": "OPEN",
  "is_gap": "Knowledge gap",
  "source_name": "Trichococcus-Syntrophomonas-Methanospirillum Butyrate Coculture",
  "source_id": "CommunityMech:000188",
  "source_file": "Trichococcus_Syntrophomonas_Methanospirillum_Butyrate_Coculture.yaml",
  "attaches_to": [
   "ecological_interactions#Aggregation With Syntrophic Partners",
   "ecological_interactions#Proteome Response in the Syntrophic Partners"
  ],
  "rationale": "The ES5-driven increase in butyrate consumption (120%) and methane (150%) is perturbation-supported, but the mediating mechanism is unresolved: aggregation and the partner proteome response are observed correlates, not demonstrated causal mediators (the two `downstream` edges here are flagged HYPOTHESIZED accordingly). Direct interspecies electron transfer was not experimentally demonstrated for this tri-culture, and the exact ES5 bridging role remains an open question per the source.\n",
  "num_experiments": 0,
  "num_evidence": 1,
  "evidence_refs": [
   "PMID:35699440"
  ],
  "posed_by": "",
  "page_url": "../docs/communities/Trichococcus_Syntrophomonas_Methanospirillum_Butyrate_Coculture.html#kg-es5-mediation-mechanism-unresolved"
 }
];
window.searchMetrics = {
 "total_discussions": 8,
 "total_knowledge_gaps": 7,
 "total_source_entries": 8,
 "kinds": [
  "CONTROVERSY",
  "KNOWLEDGE_GAP"
 ]
};
window.repoName = "CommunityMech";
