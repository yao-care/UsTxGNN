---
layout: default
title: Vincristine
parent: Model Prediction Only (L5)
nav_order: 1293
evidence_level: L5
indication_count: 3
---

# Vincristine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Vincristine: From Established Antineoplastic Use to Ganglioneuroblastoma

## One-Sentence Summary

Vincristine is a vinca alkaloid chemotherapy drug that is marketed in the US as an injectable (Hospira ANDA); the provided data does not include its approved indication text.
The TxGNN model predicts it may be effective for **ganglioneuroblastoma**, with **4 clinical trials** and **5 publications** pointing in this direction.
The evidence is indirect: the trials test other agents added to a chemotherapy backbone, and the publications are mostly case reports.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the approved-indication text provided |
| Predicted New Indication | Ganglioneuroblastoma |
| TxGNN Prediction Score | 99.31% |
| Evidence Level | L3 (see note below) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 1 (ANDA071484) |
| Recommended Decision | Proceed with Guardrails |

**Evidence level note:** The source pack assigned L2, but no Phase 2/3 trial in the pack is completed, and none tests vincristine as the randomized variable. Under the evidence rules, the supporting material is case reports, a small prospective trial and trials with an indirect link, so this report uses **L3**.

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the Evidence Pack. From general pharmacology, vincristine binds tubulin, blocks microtubule polymerization and arrests dividing cells in metaphase.

Ganglioneuroblastoma belongs to the neuroblastic tumor spectrum, which is generally chemosensitive. Vincristine is a common backbone drug in multi-agent neuroblastoma induction regimens, and the case reports below describe it used in combination chemotherapy for ganglioneuroblastoma. The mechanistic link is therefore plausible.

There are two limits on this reasoning:
- The Phase 2/3 trials test add-on agents (dinutuximab, 131I-MIBG, an ALK inhibitor), not vincristine itself. Vincristine's own contribution cannot be isolated, and the trial summaries do not confirm the exact chemotherapy composition.
- The trials enroll neuroblastoma broadly, so a ganglioneuroblastoma-specific subgroup is unconfirmed.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03786783](https://clinicaltrials.gov/study/NCT03786783) | Phase 2 | Active, not recruiting | 42 | Pilot of dinutuximab and sargramostim combined with induction chemotherapy in newly diagnosed high-risk neuroblastoma. Vincristine is probably in the chemotherapy but its effect is not separable. |
| [NCT03126916](https://clinicaltrials.gov/study/NCT03126916) | Phase 3 | Recruiting | 750 | 131I-MIBG or lorlatinib (ALK inhibitor) added to intensive therapy in newly diagnosed high-risk neuroblastoma or ganglioneuroblastoma. Vincristine is likely in the backbone, but this is not verified. |
| [NCT06172296](https://clinicaltrials.gov/study/NCT06172296) | Phase 3 | Recruiting | 478 | Dinutuximab added to induction chemotherapy and multimodal therapy in newly diagnosed high-risk neuroblastoma. Vincristine is at most a backbone component. |
| [NCT01798004](https://clinicaltrials.gov/study/NCT01798004) | Phase 1 | Completed | 150 | Busulfan/melphalan consolidation after induction chemotherapy in high-risk neuroblastoma. The link to vincristine is weak and only through prior induction. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31342649](https://pubmed.ncbi.nlm.nih.gov/31342649/) | 2019 | Prospective clinical trial | Pediatr Blood Cancer | JN-L-10 used image-defined risk factors to guide surgical timing in low-risk neuroblastoma. It concerns surgical decisions, not vincristine. |
| [8255850](https://pubmed.ncbi.nlm.nih.gov/8255850/) | 1993 | Case report | Postgrad Med J | A 21-year-old with unresectable spinal ganglioneuroblastoma achieved histologically proven complete remission with chemotherapy alone. The regimen included vincristine with doxorubicin, cyclophosphamide, etoposide, ifosfamide and cisplatin. |
| [15701990](https://pubmed.ncbi.nlm.nih.gov/15701990/) | 2005 | Case report | J Pediatr Hematol Oncol | Ganglioneuroblastoma presenting with obstructive jaundice was treated with a chemotherapy regimen that included vincristine, cisplatin, pirarubicin/doxorubicin and cyclophosphamide. |
| [7421294](https://pubmed.ncbi.nlm.nih.gov/7421294/) | 1980 | Small series | J Thorac Cardiovasc Surg | 31 patients with intrathoracic ganglioneuroblastoma; 27 survived, with follow-up up to 25 years. Treatment was resection, radiation or chemotherapy, and no vincristine-specific effect is described. |
| [8888754](https://pubmed.ncbi.nlm.nih.gov/8888754/) | 1996 | Case report | J Pediatr Hematol Oncol | An infant with stage 4 multifocal ganglioneuroblastoma and gastric involvement. It is background on the disease, not a vincristine efficacy signal. |

Pack entry PMID 3071124 (adult adrenal ganglioneuroblastoma, 1988, multimodality treatment case report) is not tabulated because its provided abstract does not mention vincristine.

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA071484 | VinCRIStine Sulfate | Injection, solution | Hospira, Inc. |

Approved indication text is not provided for this authorization. The only route is injectable.

---

## Cytotoxicity

The details below are from general pharmacology knowledge, not from the Evidence Pack. Please confirm against the package insert.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (vinca alkaloid, antimicrotubule agent) |
| Myelosuppression Risk | Low to moderate. Neurotoxicity is the dose-limiting concern, and myelosuppression is usually less prominent than with many other cytotoxics. |
| Emetogenicity Classification | Low |
| Monitoring Items | CBC with differential, liver function, neurological examination (peripheral neuropathy), bowel function (constipation/ileus) |
| Handling Protection | Must follow cytotoxic drug handling regulations. It is a vesicant, so avoid extravasation. Intravenous use only. |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Vincristine has a plausible mechanism and is a common component of neuroblastoma induction regimens, and case reports describe responses in ganglioneuroblastoma. However, the Phase 2/3 trials test add-on agents rather than vincristine, and the supporting literature is mostly case reports. The proceed decision depends on completing the safety review below.

**To proceed, the following is needed:**
- The FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Verification of the actual chemotherapy backbone in NCT03786783, NCT03126916 and NCT06172296, and whether vincristine is included
- Ganglioneuroblastoma-specific subgroup data, since the trials enroll neuroblastoma broadly
- The approved indication text for ANDA071484, to establish the original indication

**Other predicted indications in the pack (not evaluated in detail above):**
- *Retroperitoneal neoplasm* (score 99.23%): evidence is L3 and histology-specific (paraganglioma, sarcoma, seminoma, extrarenal Wilms' tumor and others), so it does not support a single class-level indication. It is a research question.
- *Vertebral anomalies and variable endocrine and T-cell dysfunction* (score 99.24%): no trials or literature and no plausible mechanistic link, so it is likely a knowledge-graph artifact. Hold.

*These results are for research reference only and do not constitute medical advice. Repurposing candidates require clinical validation before application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

