---
layout: default
title: Irinotecan
parent: High Evidence (L1-L2)
nav_order: 810
evidence_level: L2
indication_count: 1
---

# Irinotecan
{: .fs-9 }

Evidence Level: **L2** | Predicted Indications: **1** 
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

# Irinotecan: From Its Current US-Approved Use to Female Breast Carcinoma

## One-Sentence Summary

Irinotecan is an injectable topoisomerase I-inhibitor chemotherapy that is currently marketed in the US under 20 authorizations.
The TxGNN model predicts it may be effective for **female breast carcinoma**. Of the **20 clinical trials** and **20 publications** retrieved, only **3 trials** test irinotecan directly in breast cancer. Most of the supporting literature concerns sacituzumab govitecan, a drug that carries irinotecan's active metabolite SN-38.

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Female breast carcinoma |
| TxGNN Prediction Score | 99.08% |
| Evidence Level | L2 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the source record, and the approved indication text is also empty. Based on known pharmacology, irinotecan is a prodrug. Carboxylesterases convert it to SN-38, a topoisomerase I inhibitor that causes replication-dependent DNA double-strand breaks.

Breast tumors with high proliferation or DNA-repair deficiency, such as triple-negative or HRD-like tumors, are plausibly sensitive to this mechanism. Sacituzumab govitecan is an antibody-drug conjugate that delivers SN-38. It has Phase 3 benefit in metastatic breast cancer, which shows that SN-38 is an active payload in this disease.

This is indirect evidence. It does not show that systemic irinotecan itself works in breast cancer. The 1998 and 2003 reviews describe irinotecan's breast cancer activity as limited or "marginal", and the 2020 pilot study notes it is "rarely used" in metastatic breast cancer. The TxGNN score is very high, but it is a computational prediction only.

## Clinical Trial Evidence

No efficacy results were included in the source record, so the findings below describe study design only. Only the first three trials test irinotecan directly in breast cancer.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00072852](https://clinicaltrials.gov/study/NCT00072852) | Phase 2 | Completed | 134 | Single-agent oral irinotecan on two schedules (5-day vs 14-day, 3-week cycles) in metastatic breast cancer after anthracycline, taxane and capecitabine failure. Direct evidence. |
| [NCT03562390](https://clinicaltrials.gov/study/NCT03562390) | Phase 2 | Unknown | 124 | Single-arm, third-line or later irinotecan in Chinese patients with recurrent or metastatic breast cancer previously treated with anthracyclines and taxanes. |
| [NCT00083148](https://clinicaltrials.gov/study/NCT00083148) | Phase 1 | Completed | 12 | Irinotecan followed by capecitabine in advanced breast carcinoma. Dose and safety study. |
| [NCT00031681](https://clinicaltrials.gov/study/NCT00031681) | Phase 1 | Completed | 41 | UCN-01 plus irinotecan in resistant solid tumors, with a triple-negative breast cancer part. |
| [NCT05453825](https://clinicaltrials.gov/study/NCT05453825) | Phase 2 | Unknown | 180 | Basket study of navicixizumab alone or with paclitaxel or irinotecan, including a triple-negative breast cancer cohort. |
| [NCT01770353](https://clinicaltrials.gov/study/NCT01770353) | Phase 1 | Completed | 45 | Nanoliposomal irinotecan (MM-398): tumor drug levels and ferumoxytol MRI in solid tumors. Different formulation. |
| [NCT01631552](https://clinicaltrials.gov/study/NCT01631552) | Phase 1/2 | Completed | 515 | Sacituzumab govitecan (SN-38 antibody-drug conjugate) in epithelial cancers including breast. Indirect evidence. |
| [NCT00004095](https://clinicaltrials.gov/study/NCT00004095) | Phase 1 | Completed | 38 | Irinotecan plus gemcitabine in unresectable or metastatic solid tumors. |
| [NCT02033551](https://clinicaltrials.gov/study/NCT02033551) | Phase 1 | Completed | 47 | Veliparib extension study, alone or with chemotherapy including FOLFIRI, in solid tumors. |
| [NCT04640480](https://clinicaltrials.gov/study/NCT04640480) | Phase 1 | Completed | 21 | SNB-101 (nano-particle SN-38) dose-finding in advanced solid tumors. Link to breast cancer is unclear. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36027558](https://pubmed.ncbi.nlm.nih.gov/36027558/) | 2022 | RCT (Phase 3) | J Clin Oncol | Sacituzumab govitecan (SN-38 payload) in HR+/HER2- metastatic breast cancer. Indirect evidence. |
| [30786188](https://pubmed.ncbi.nlm.nih.gov/30786188/) | 2019 | Phase 1/2 single-arm | N Engl J Med | Sacituzumab govitecan in refractory metastatic triple-negative breast cancer. |
| [28291390](https://pubmed.ncbi.nlm.nih.gov/28291390/) | 2017 | Single-arm trial | J Clin Oncol | Sacituzumab govitecan in heavily pretreated metastatic triple-negative breast cancer. |
| [32727805](https://pubmed.ncbi.nlm.nih.gov/32727805/) | 2020 | Pilot study | Anticancer Res | Irinotecan plus S-1 (IRIS) in advanced and metastatic breast cancer. The paper notes irinotecan is rarely used in this setting. |
| [12800602](https://pubmed.ncbi.nlm.nih.gov/12800602/) | 2003 | Review | Oncology (Williston Park) | Rationale for mitomycin plus irinotecan. Each has marginal single-agent activity, and preclinical data suggest synergy. |
| [9726101](https://pubmed.ncbi.nlm.nih.gov/9726101/) | 1998 | Review | Oncology (Williston Park) | Irinotecan's broad antitumor activity across tumor types, including breast cancer. |
| [36302269](https://pubmed.ncbi.nlm.nih.gov/36302269/) | 2022 | Review | Breast | Clinical development of TROP-2 antibody-drug conjugates in metastatic breast cancer. |
| [39768216](https://pubmed.ncbi.nlm.nih.gov/39768216/) | 2024 | Review | Cells | Sacituzumab govitecan in refractory triple-negative breast cancer. |
| [32223649](https://pubmed.ncbi.nlm.nih.gov/32223649/) | 2020 | Trial design paper | Future Oncol | Design of TROPiCS-02, a Phase 3 trial of sacituzumab govitecan in HR+/HER2- metastatic breast cancer. |
| [10472342](https://pubmed.ncbi.nlm.nih.gov/10472342/) | 1999 | Preclinical | Anticancer Res | In nude-mouse xenografts, irinotecan and doxorubicin halted or caused significant regression of the breast cancer lines tested (MCF7, MDA-MB-231, T47D). |

## US Market Information

The source record lists no approved indication text for these authorizations. Five of the 20 are shown.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| NDA020571 | Camptosar | Injection, solution | Pharmacia & Upjohn Company LLC |
| ANDA208718 | Irinotecan Hydrochloride | Injection | Armas Pharmaceuticals Inc. |
| ANDA203380 | Irinotecan Hydrochloride | Injection, solution | Apotex Corp. |
| ANDA203380 | Irinotecan Hydrochloride | Injection, solution | Qilu Pharmaceutical Co., Ltd. |
| ANDA091032 | Irinotecan Hydrochloride | Injection | Hikma Pharmaceuticals USA Inc. |

All products are injectables (injection, injection solution, and powder for solution).

## Cytotoxicity

The Evidence Pack contains no toxicity data. The entries below reflect general class knowledge and must be confirmed against the current package insert.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (topoisomerase I inhibitor) |
| Myelosuppression Risk | High (severe myelosuppression is a recognized class concern) |
| Emetogenicity Classification | Moderate |
| Monitoring Items | CBC with differential, liver and renal function, electrolytes, and hydration status |
| Handling Protection | Must follow cytotoxic drug handling regulations |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
One completed Phase 2 trial (NCT00072852) and one unresolved Phase 2 (NCT03562390) directly test irinotecan in metastatic breast cancer, which supports evidence level L2. However, no efficacy results are in the record, the literature describes single-agent activity as marginal, and most supporting publications concern sacituzumab govitecan rather than irinotecan itself. Package insert safety information is also missing. The candidate stays at the research-question stage.

**To proceed, the following is needed:**
- Package insert warnings and contraindications, which block safety screening
- Mechanism of action data from DrugBank
- Published results and response rates from NCT00072852 and NCT03562390, including whether the schedules were randomized
- Breast cancer subtype analysis (triple-negative, HR+/HER2-, HRD-like) to define a target population
- A comparison against current standard options, including sacituzumab govitecan
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

