---
layout: default
title: Lomustine
parent: Model Prediction Only (L5)
nav_order: 867
evidence_level: L5
indication_count: 10
---

# Lomustine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Lomustine: From Hodgkin Lymphoma to Lymphosarcoma (Non-Hodgkin Lymphoma)

## One-Sentence Summary

Lomustine is an oral nitrosourea alkylating chemotherapy that the evidence pack describes as already labeled for Hodgkin lymphoma. The TxGNN model predicts it may be effective for **lymphosarcoma** (an older term for non-Hodgkin lymphoma, including primary CNS lymphoma), with **17 clinical trials** and **20 publications** retrieved, of which 9 trials and 10 publications are summarized below. Nearly all of that evidence comes from multi-drug regimens, so lomustine's individual contribution cannot be isolated.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the US license records; Hodgkin lymphoma is noted as a labeled use in the evidence pack |
| Predicted New Indication | Lymphosarcoma |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L2 (per pack scoring; see the note under Clinical Trial Evidence) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 9 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data are not available in the pack. Lomustine belongs to the nitrosourea class of alkylating agents. It is lipophilic, crosslinks DNA, and crosses the blood-brain barrier. Its efficacy in Hodgkin lymphoma is established, and mechanistically it may apply to other lymphoid malignancies.

Lymphosarcoma maps to non-Hodgkin lymphoma (NHL). Lomustine appears in several NHL combination regimens:
- MPL/R-MPL (methotrexate, procarbazine, lomustine ± rituximab) for primary CNS lymphoma.
- LEMP, CAMP, PACET and CIBO-P for relapsed or refractory NHL.
- Oral lomustine, etoposide, cyclophosphamide and procarbazine for AIDS-related lymphoma.

Its ability to reach the CNS is a plausible advantage in CNS lymphoma.

The link is only partly a repurposing signal, since Hodgkin lymphoma is already a labeled use. All lymphoma evidence comes from single-arm Phase 2 trials and retrospective series of multi-drug regimens. Lomustine's presence in each regimen is inferred from titles and summaries, and the provided records were truncated.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00049439](https://clinicaltrials.gov/study/NCT00049439) | Phase 2 | Completed | 54 | Dose-modified oral lomustine + etoposide + cyclophosphamide + procarbazine in AIDS-related NHL (US and Africa). Largest lymphoma dataset, but single-arm and multi-drug |
| [NCT00989352](https://clinicaltrials.gov/study/NCT00989352) | Phase 2 | Unknown | 56 | Rituximab + high-dose methotrexate, lomustine and procarbazine, then procarbazine maintenance, in primary CNS lymphoma over age 65 |
| [NCT00074191](https://clinicaltrials.gov/study/NCT00074191) | Phase 2 | Completed | 1 | Methotrexate, procarbazine and CCNU with intraventricular chemotherapy in primary CNS lymphoma. Only 1 patient, so essentially uninformative |
| [NCT00003114](https://clinicaltrials.gov/study/NCT00003114) | Phase 2 | Completed | 5 | Oral lomustine, etoposide, cyclophosphamide and procarbazine in AIDS-associated Hodgkin's disease. Very small sample |
| [NCT00003113](https://clinicaltrials.gov/study/NCT00003113) | Phase 2 | Terminated | 6 | Oral combination chemotherapy + G-CSF in elderly intermediate- and high-grade NHL. Small, terminated early |
| [NCT01775475](https://clinicaltrials.gov/study/NCT01775475) | Phase 2 | Completed | 7 | Randomized CHOP vs oral chemotherapy (including lomustine, etoposide, procarbazine) in HIV-associated lymphoma in sub-Saharan Africa. Very small |
| [NCT00003929](https://clinicaltrials.gov/study/NCT00003929) | Phase 2 | Withdrawn | 0 | Lomustine, procarbazine, filgrastim and radiation in primary CNS lymphoma. No patients enrolled, so no data |
| [NCT05518383](https://clinicaltrials.gov/study/NCT05518383) | Phase 4 | Recruiting | 300 | Pediatric mature B-cell NHL protocol (B-NHL-M-2021). Disease matches, but lomustine's role is not evident |
| [NCT00317408](https://clinicaltrials.gov/study/NCT00317408) | N/A | Unknown | 96 | Relapsed pediatric anaplastic large cell lymphoma with chemotherapy, total-body irradiation and stem cell transplant. Lomustine's role is not confirmed |

The pack scores this indication L2 (a completed Phase 2 trial). Strictly, none of these is a randomized Phase 2/3 trial with lomustine-specific data, so treat the level as generous. No Phase 3 RCT exists for this indication.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [348294](https://pubmed.ncbi.nlm.nih.gov/348294/) | 1978 | Randomized comparison | Cancer | CALGB study of CCNU vs methyl-CCNU in advanced Hodgkin's disease, lymphosarcoma and reticulum cell sarcoma |
| [21303800](https://pubmed.ncbi.nlm.nih.gov/21303800/) | 2011 | Phase 2 pilot | Ann Oncol | Adding rituximab to methotrexate, procarbazine and lomustine in elderly primary CNS lymphoma |
| [8436213](https://pubmed.ncbi.nlm.nih.gov/8436213/) | 1993 | Clinical trial | Eur J Haematol | LEMP regimen (lomustine, etoposide, methotrexate, prednisone) in 22 patients with relapsed or refractory NHL |
| [2259920](https://pubmed.ncbi.nlm.nih.gov/2259920/) | 1990 | Phase 2 | Semin Oncol | CAMP regimen in 30 patients with doxorubicin-resistant NHL: 27% complete and 20% partial remission |
| [8422281](https://pubmed.ncbi.nlm.nih.gov/8422281/) | 1993 | Phase 2 | Eur J Cancer | PACET regimen in relapsed or refractory NHL: 26% complete response, median survival 6 months, intensely myelosuppressive |
| [10711848](https://pubmed.ncbi.nlm.nih.gov/10711848/) | 1999 | Review | Drugs | Oral lomustine, etoposide, cyclophosphamide and procarbazine in 38 patients with AIDS-related NHL |
| [15803492](https://pubmed.ncbi.nlm.nih.gov/15803492/) | 2005 | Clinical study | Cancer | CIBO-P regimen (lomustine, ifosfamide, bleomycin, vincristine, cisplatin) for refractory or recurrent aggressive NHL |
| [33336792](https://pubmed.ncbi.nlm.nih.gov/33336792/) | 2021 | Clinical study | Br J Haematol | DECC oral regimen (dexamethasone, etoposide, chlorambucil, lomustine) in relapsed or refractory DLBCL. No abstract available |
| [30197327](https://pubmed.ncbi.nlm.nih.gov/30197327/) | 2018 | Retrospective | J Cancer Res Ther | LACE conditioning before autologous transplant in relapsed or refractory lymphoma: toxicity and long-term outcomes |
| [22888657](https://pubmed.ncbi.nlm.nih.gov/22888657/) | 2012 | Preclinical (mouse) | Vopr Onkol | Gemcitabine + lomustine in mice with intracranial lymphosarcoma LIO-1: median lifespan increased 3.3-fold vs control |

The pack also returned several veterinary series of lomustine-based canine lymphoma protocols (LOPP, LPP). They are omitted here because they are not human evidence.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| NDA017588 | Gleostine | Capsule, gelatin coated | Azurity Pharmaceuticals, Inc. |
| NDA017588 | Gleostine | Capsule, gelatin coated | NextSource Biotechnology, LLC |
| ANDA219265 | Lomustine | Capsule | Carnegie Pharmaceuticals LLC |

The record shows 9 licenses in total, but only these 3 distinct authorizations appeared in the extract. All are oral capsules. Approved-indication text was not included in the records.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (nitrosourea alkylating agent) |
| Myelosuppression Risk | High (delayed and cumulative; the PACET series was described as intensely myelosuppressive) |
| Emetogenicity Classification | Moderate to high |
| Monitoring Items | CBC with differential and platelets, liver and renal function; pulmonary status (nitrosourea lung toxicity is described in the retrieved literature) |
| Handling Protection | Must follow cytotoxic drug handling regulations |

The classification is based on drug class. Please refer to the package insert warnings and precautions for product-specific details.

## Safety Considerations

Package insert warnings and contraindications were not available in the pack, and no drug-interaction records were found. Please refer to the package insert for safety information.

The retrieved literature signals two class-related concerns:
- Nitrosourea-induced pulmonary toxicity (PMID 1470749).
- A case of myelodysplastic syndrome progressing to AML after a CCNU-containing regimen (PMID 9673540).

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is high and lomustine is used in NHL and CNS lymphoma regimens. However, the evidence consists of small, mostly single-arm Phase 2 trials and older or retrospective multi-drug series. There is no Phase 3 RCT, and Hodgkin lymphoma is already a labeled use. The blocking gap in package insert safety data also prevents progression past the S1 screening stage. At best this is a research question at present.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (blocking data gap), plus the approved indication text.
- Full trial records to confirm lomustine's role in each regimen, and the remaining publications not summarized here.
- Comparative or randomized evidence isolating lomustine's contribution.
- Mechanism-of-action data from DrugBank.
- A defined target population, for example relapsed or refractory primary CNS lymphoma, with a safety monitoring plan for myelosuppression.

Nine other indications were also predicted: malignant tumor of meninges, spinal cord cancer, cerebral neuroblastoma, pediatric cerebral ependymoblastoma, pediatric infratentorial ependymoblastoma, childhood brain germinoma, cerebellopontine angle embryonal tumor, lymph node cancer and cerebral sarcoma. They are outside this report's scope. Their evidence is generally weaker, and several have no trial or literature support.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

