---
layout: default
title: Doxorubicin
parent: High Evidence (L1-L2)
nav_order: 626
evidence_level: L1
indication_count: 10
---

# Doxorubicin
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **10** 
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

# Doxorubicin: From Established Cancer Chemotherapy to Ewing Sarcoma

## One-Sentence Summary

Doxorubicin is an anthracycline chemotherapy drug. The Evidence Pack lists no approved indication text for it, so the original indication is not documented here.
The TxGNN model predicts it is effective for **Ewing sarcoma**. Retrieval found **48 clinical trials** (3 completed Phase 3) and **20 publications** on this disease, including several randomized trials.
This is most likely an existing standard-of-care use (doxorubicin is a backbone drug in the vincristine/doxorubicin/cyclophosphamide regimen) rather than true repurposing.

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Ewing sarcoma |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L1 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Doxorubicin is a topoisomerase II poison and DNA intercalator. Detailed mechanism-of-action data from DrugBank is not available in this pack, so the mechanism above comes from the pack's repurposing rationale.

Ewing sarcoma is treated with multi-agent chemotherapy. The standard backbone alternates vincristine/doxorubicin/cyclophosphamide (VDC) with ifosfamide/etoposide (IE). The trial and literature records repeatedly name this doxorubicin-containing backbone, for example NCT01231906 and NCT06820957 and the COG interval-compressed chemotherapy RCTs. The very high TxGNN score is consistent with this established use.

The evidence has limits. Many retrieved trials test an add-on agent (ganitumab, regorafenib, dinutuximab beta) on top of the backbone, so they do not isolate doxorubicin's own contribution. Some trial records do not state the regimen composition.

## Clinical Trial Evidence

The 10 trials below were selected from 48 retrieved.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00006734](https://clinicaltrials.gov/study/NCT00006734) | Phase 3 | Completed | 587 | Randomized comparison of chemotherapy intensification through interval compression in Ewing sarcoma and related tumors. Doxorubicin's role is not stated in the record. |
| [NCT01231906](https://clinicaltrials.gov/study/NCT00334867) | Phase 3 | Completed | 642 | Adds vincristine-topotecan-cyclophosphamide to standard therapy in non-metastatic Ewing sarcoma. The standard 5-drug arm explicitly includes doxorubicin. |
| [NCT02063022](https://clinicaltrials.gov/study/NCT02063022) | Phase 3 | Completed | 278 | Standard versus intensive treatment in non-metastatic Ewing sarcoma. Doxorubicin is not confirmed in the record. |
| [NCT02306161](https://clinicaltrials.gov/study/NCT02306161) | Phase 3 | Active, not recruiting | 312 | Ganitumab (IGF-1R antibody) added to interval-compressed chemotherapy in newly diagnosed metastatic Ewing sarcoma. Doxorubicin is named among the chemotherapy drugs. |
| [NCT06820957](https://clinicaltrials.gov/study/NCT06820957) | Phase 2/3 | Active, not recruiting | 437 | Vincristine-irinotecan-regorafenib added to VDC/IE versus VDC/IE alone in newly diagnosed metastatic Ewing sarcoma. |
| [NCT00020566](https://clinicaltrials.gov/study/NCT00020566) | Phase 3 | Unknown | 1200 | EURO-E.W.I.N.G.99: randomized trial of combination chemotherapy with or without radiotherapy or surgery. |
| [NCT00002516](https://clinicaltrials.gov/study/NCT00002516) | Phase 3 | Unknown | Not reported | EICESS 92: randomized comparison of combination chemotherapy regimens plus surgery and radiotherapy. |
| [NCT00003667](https://clinicaltrials.gov/study/NCT00003667) | Phase 2 | Completed | Not reported | Vincristine/doxorubicin/cyclophosphamide with dexrazoxane, with or without ImmTher, in high-risk Ewing sarcoma. Doxorubicin is explicit. |
| [NCT01313884](https://clinicaltrials.gov/study/NCT01313884) | Phase 2 | Terminated | 3 | Cyclophosphamide/doxorubicin/vincristine alternating with irinotecan/temozolomide in metastatic Ewing sarcoma. Terminated after only 3 patients. |
| [NCT00002466](https://clinicaltrials.gov/study/NCT00002466) | Phase 2 | Completed | Not reported | Cyclophosphamide, doxorubicin, vincristine, etoposide and ifosfamide, followed by resection and radiotherapy, in peripheral PNET or Ewing sarcoma. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12594313](https://pubmed.ncbi.nlm.nih.gov/12594313/) | 2003 | RCT | N Engl J Med | Tested adding ifosfamide and etoposide to standard chemotherapy in newly diagnosed Ewing sarcoma and PNET of bone. |
| [36522207](https://pubmed.ncbi.nlm.nih.gov/36522207/) | 2022 | RCT | Lancet | EE2012 Phase 3: compares the two standard European and US chemotherapy strategies in newly diagnosed Ewing sarcoma. |
| [23091096](https://pubmed.ncbi.nlm.nih.gov/23091096/) | 2012 | RCT | J Clin Oncol | COG trial of interval-compressed chemotherapy, using alternating VDC/IE cycles, in localized Ewing sarcoma. |
| [36669140](https://pubmed.ncbi.nlm.nih.gov/36669140/) | 2023 | RCT | J Clin Oncol | COG Phase 3: ganitumab added to interval-compressed chemotherapy in newly diagnosed metastatic Ewing sarcoma. |
| [31952545](https://pubmed.ncbi.nlm.nih.gov/31952545/) | 2020 | RCT protocol | Trials | EURO EWING 2012 protocol comparing two induction/consolidation chemotherapy regimens. |
| [37403815](https://pubmed.ncbi.nlm.nih.gov/37403815/) | 2023 | Consensus guideline | Cancer | National Ewing Sarcoma Tumor Board recommendations on standard-of-care nuances and debates. |
| [20152770](https://pubmed.ncbi.nlm.nih.gov/20152770/) | 2010 | Review | Lancet Oncol | Chemotherapy raised survival from about 10% to about 75% in localized disease. Patients with metastases still fare badly, and toxicity is a concern. |
| [26304893](https://pubmed.ncbi.nlm.nih.gov/26304893/) | 2015 | Review | J Clin Oncol | Current management relies on risk-adapted intensive chemotherapy plus surgery and/or radiotherapy. |
| [28710342](https://pubmed.ncbi.nlm.nih.gov/28710342/) | 2017 | Retrospective study | Oncologist | Institutional results of vincristine, ifosfamide and doxorubicin (VID) for initial treatment of Ewing sarcoma in adults. |
| [1833556](https://pubmed.ncbi.nlm.nih.gov/1833556/) | 1991 | Cohort/dose-intensity analysis | J Natl Cancer Inst | Dose-intensity analysis of published trials for doxorubicin in osteosarcoma and Ewing sarcoma. |

## US Market Information

The Evidence Pack lists 20 authorizations. The pack contains no approved-indication text for them, so that column is omitted. Dosage forms seen include solution injection, liposomal injection and lyophilized powder for injection.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA209825 | Doxorubicin Hydrochloride | Injection, solution | Gland Pharma Limited |
| NDA050629 | Doxorubicin Hydrochloride | Injection, solution | Pfizer Laboratories Div Pfizer Inc |
| ANDA208657 | Doxorubicin Hydrochloride | Injectable, liposomal | BluePoint Laboratories |
| ANDA062975 | Doxorubicin Hydrochloride | Injection, solution | Hikma Pharmaceuticals USA Inc. |

## Cytotoxicity

The Evidence Pack has no DrugBank toxicity data for this drug. The entries below reflect general knowledge of the anthracycline class and should be confirmed against the package insert.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (anthracycline; topoisomerase II poison and DNA intercalator) |
| Myelosuppression Risk | High. Ewing sarcoma trials in the pack test supportive agents against VDC/IE myelosuppression (trilaciclib, NCT06699472) and thrombocytopenia (romiplostim, NCT07048249). |
| Emetogenicity Classification | Moderate to high, particularly when combined with cyclophosphamide |
| Monitoring Items | CBC with differential, liver and renal function, cardiac function (echocardiography) and cumulative anthracycline dose |
| Handling Protection | Must follow cytotoxic drug handling regulations |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Three completed Phase 3 trials (NCT00006734, NCT01231906, NCT02063022), several randomized trials in the literature, and consensus guidance support a doxorubicin-containing multi-agent regimen in Ewing sarcoma (Evidence Level L1). This appears to be an established standard-of-care use rather than a new repurposing finding, and doxorubicin's own contribution is not isolated in the retrieved evidence.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications, which are missing from the pack and block safety screening.
- Detailed mechanism-of-action data from DrugBank.
- Confirmation of the regimen composition, including doxorubicin, in the trials where it is not stated (for example NCT00006734, NCT02063022, NCT00020566).
- Guardrails: cumulative anthracycline dose limits, cardiac monitoring, and use only within multimodal protocols.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

