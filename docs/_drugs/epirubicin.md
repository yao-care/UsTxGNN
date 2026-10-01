---
layout: default
title: Epirubicin
parent: Moderate Evidence (L3-L4)
nav_order: 661
evidence_level: L4
indication_count: 7
---

# Epirubicin
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **7** 
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

# Epirubicin: From Anthracycline Cancer Chemotherapy to Primary Pulmonary Lymphoma

## One-Sentence Summary

Epirubicin is an anthracycline chemotherapy drug used in a range of cancers, marketed in the US as Ellence injection.
The TxGNN model predicts it may be effective for **primary pulmonary lymphoma**, but there are **0 clinical trials** and only **9 publications** (case reports, retrospective series and reviews, none testing epirubicin for this disease).
The prediction is therefore mainly model-based and not yet supported by direct evidence.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | The US label indication text is not included in the data provided. Literature describes epirubicin as an anthracycline used in cancer chemotherapy. |
| Predicted New Indication | Primary pulmonary lymphoma |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L4 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 2 records (both NDA050778, Ellence) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the Evidence Pack. Epirubicin is an anthracycline that inhibits topoisomerase II and damages DNA in dividing tumor cells. Anthracyclines are core components of CHOP-like regimens for aggressive B-cell lymphoma, so the link to a lymphoma of the lung is biologically plausible.

However, no epirubicin-specific data exist for primary pulmonary lymphoma. The retrieved literature consists of case reports, retrospective series, and Hodgkin or DLBCL regimens that mostly use doxorubicin. The very high score (0.997) is a model prediction only and should not be read as evidence of efficacy.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [7686469](https://pubmed.ncbi.nlm.nih.gov/7686469/) | 1993 | Review | Drugs | Epirubicin is the 4' epimer of doxorubicin. In breast and lung cancers, trials showed response and survival equivalent to doxorubicin regimens. Lymphoma is not the focus. |
| [36237246](https://pubmed.ncbi.nlm.nih.gov/36237246/) | 2022 | Case report | Translational Cancer Research | Primary MALT lymphoma of the pleura, misdiagnosed, first such case in China. No epirubicin data. |
| [1866500](https://pubmed.ncbi.nlm.nih.gov/1866500/) | 1991 | Case report | Revista de Investigacion Clinica | Non-Hodgkin lymphoma presenting in the lung with pleural effusion. Background on the disease, not on epirubicin efficacy. |
| [40728626](https://pubmed.ncbi.nlm.nih.gov/40728626/) | 2025 | Cohort | Annals of Hematology | Retrospective study of 117 DLBCL patients on Pola-R-CHP first-line. The regimen contains doxorubicin, not epirubicin. |
| [39192408](https://pubmed.ncbi.nlm.nih.gov/39192408/) | 2024 | Cohort | Zhongguo Shi Yan Xue Ye Xue Za Zhi | Single-center retrospective analysis of primary extranodal DLBCL in the rituximab era. Prognostic factors only. |
| [16428496](https://pubmed.ncbi.nlm.nih.gov/16428496/) | 2006 | Cohort | Clinical Cancer Research | 10-year results of the MOPPEBVCAD regimen (which includes epidoxorubicin, i.e. epirubicin) plus limited radiotherapy in advanced Hodgkin lymphoma. Reports late toxicity and second tumors. |
| [10526668](https://pubmed.ncbi.nlm.nih.gov/10526668/) | 1999 | Cohort | Cancer Journal | Pilot study of the intensive VEBEP regimen plus involved-field radiotherapy in advanced Hodgkin disease. Hodgkin lymphoma, not pulmonary lymphoma. |
| [7525516](https://pubmed.ncbi.nlm.nih.gov/7525516/) | 1994 | Cohort | Int J Radiat Oncol Biol Phys | Extended-field radiotherapy alone in early-stage Hodgkin disease. No relevance to epirubicin. |
| [8386780](https://pubmed.ncbi.nlm.nih.gov/8386780/) | 1993 | Case report | Rinsho Ketsueki | Lymphoblastic lymphoma developing after small cell lung cancer therapy. Resistant to combination chemotherapy. |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA050778 | Ellence (Pharmacia & Upjohn Company LLC) | Injection, solution | Not listed in the data provided |

The pack lists this NDA twice with identical details; it is shown once here. The only route of administration is injectable.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (anthracycline, topoisomerase II inhibitor) |
| Myelosuppression Risk | High (neutropenia is the main dose-limiting effect) |
| Emetogenicity Classification | Moderate to high, depending on dose and combination |
| Monitoring Items | CBC with differential, liver and renal function, cardiac function (LVEF, cumulative anthracycline dose) |
| Handling Protection | Must follow cytotoxic drug handling regulations. Extravasation is a serious risk. |

Please also refer to the package insert warnings and precautions. The retrieved literature further links epirubicin-based chemotherapy to secondary AML/MDS and to anthracycline cardiotoxicity.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a mechanistic argument and a model score, with no trials and no epirubicin-specific publications for primary pulmonary lymphoma. Standard lymphoma regimens use doxorubicin, so there is no clear reason to switch to epirubicin.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (blocking gap for safety screening)
- The US label indication text and detailed mechanism of action data
- Any epirubicin-specific clinical or preclinical data in pulmonary or B-cell lymphoma
- Comparison against standard anthracycline regimens (for example doxorubicin-based R-CHOP), including a cardiotoxicity assessment

**Other predictions in this pack:** Small cell lung carcinoma (rank 3) has much stronger support. It has a completed Phase 3 RCT of epirubicin plus cyclophosphamide added to cisplatin/etoposide (NCT00003606), but the trial outcome is not shown in the data. The evidence level there is L1, with a recommendation of Proceed with Guardrails. Upper aerodigestive tract neoplasm (rank 7) is also L1, but the literature mostly covers gastroesophageal cancer, where epirubicin is already established. Consider evaluating small cell lung carcinoma as the lead candidate.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

