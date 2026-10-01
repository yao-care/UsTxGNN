---
layout: default
title: Docetaxel
parent: Model Prediction Only (L5)
nav_order: 617
evidence_level: L5
indication_count: 10
---

# Docetaxel
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

# Docetaxel: From Cytotoxic Chemotherapy to Female Breast Carcinoma

## One-Sentence Summary

Docetaxel is a taxane-class chemotherapy injection. The retrieved US license records do not list its approved indications.
The TxGNN model predicts it may be effective for **female breast carcinoma**, with **50 clinical trials** and **20 publications** retrieved for this direction, including 3 completed Phase 3 trials.
Docetaxel is widely known to be used in breast cancer already, so this may be an existing indication rather than a true repurposing. This should be confirmed against the current US label.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not captured in the retrieved license records |
| Predicted New Indication | Female breast carcinoma |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L2 (see note below) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 |
| Recommended Decision | Proceed with Guardrails |

Note: at least two completed Phase 3 trials involve docetaxel-containing regimens (NCT00003519, NCT00017095), and a randomized adjuvant series (PMID 28398846) is also present. A manual review could justify upgrading the level to L1.

---

## Why is This Prediction Reasonable?

Docetaxel stabilizes microtubules. This causes mitotic arrest and apoptosis in rapidly dividing tumor cells. Detailed mechanism-of-action data is not available in the record. However, this microtubule-stabilizing mechanism is well established in breast cancer.

The clinical literature is extensive, and the model's very high score is consistent with it. Docetaxel has been studied in neoadjuvant, adjuvant and metastatic breast cancer. It has been tested alone and in combination with anthracyclines, cyclophosphamide, carboplatin, gemcitabine, capecitabine and HER2-targeted agents.

Because the original indication text is empty in the pack, the "new" indication status cannot be verified from the pack alone. The label status should be checked against the FDA record.

---

## Clinical Trial Evidence

50 trials were retrieved. The 10 most relevant are listed below.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00003519](https://clinicaltrials.gov/study/NCT00003519) | Phase 3 | Completed | 2778 | Adjuvant doxorubicin/docetaxel vs doxorubicin/cyclophosphamide in node-positive or high-risk node-negative breast cancer |
| [NCT00017095](https://clinicaltrials.gov/study/NCT00017095) | Phase 3 | Completed | 1856 | Taxane vs non-taxane regimen in locally advanced or large operable breast cancer, with p53 as a predictive marker |
| [NCT00408408](https://clinicaltrials.gov/study/NCT00408408) | Phase 3 | Unknown | 1206 | Neoadjuvant trial adding capecitabine or gemcitabine to docetaxel before AC, with or without bevacizumab |
| [NCT00629278](https://clinicaltrials.gov/study/NCT00629278) | Phase 3 | Unknown | 2500 | SHORT-HER: two adjuvant chemotherapy regimens plus 3 vs 12 months of trastuzumab in HER2-positive disease |
| [NCT00841828](https://clinicaltrials.gov/study/NCT00841828) | Phase 2 | Completed | 102 | Epirubicin/cyclophosphamide then docetaxel with trastuzumab vs lapatinib in HER2+ breast cancer |
| [NCT02413320](https://clinicaltrials.gov/study/NCT02413320) | Phase 2 | Completed | 101 | Neoadjuvant carboplatin plus docetaxel vs carboplatin plus paclitaxel, then AC, in triple-negative breast cancer |
| [NCT00545688](https://clinicaltrials.gov/study/NCT00545688) | Phase 2 | Completed | 417 | Four neoadjuvant combinations of trastuzumab, docetaxel and pertuzumab in HER2+ disease, measuring pathologic complete response |
| [NCT00941330](https://clinicaltrials.gov/study/NCT00941330) | Phase 2 | Completed | 31 | Pre-operative docetaxel-cyclophosphamide vs exemestane in HR+ disease. Small sample |
| [NCT05189067](https://clinicaltrials.gov/study/NCT05189067) | Phase 2/3 | Unknown | 190 | Adjuvant docetaxel plus trastuzumab vs paclitaxel plus trastuzumab in stage I HER2+ disease |
| [NCT00343512](https://clinicaltrials.gov/study/NCT00343512) | Phase 2 | Terminated | 34 | Pilot of neoadjuvant dose-dense docetaxel with molecular correlates. Exploratory and underpowered |

Several other retrieved trials are supportive-care studies rather than docetaxel efficacy studies. Examples are NCT03252431 (pegfilgrastim) and NCT01298193 (chemotherapy-induced nausea and vomiting).

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28398846](https://pubmed.ncbi.nlm.nih.gov/28398846/) | 2017 | RCT (series of 3 adjuvant trials) | J Clin Oncol | Compared docetaxel-cyclophosphamide (TC) with taxane-anthracycline regimens in early breast cancer (ABC trials) |
| [11481357](https://pubmed.ncbi.nlm.nih.gov/11481357/) | 2001 | Randomized phase IIb | J Clin Oncol | Dose-dense doxorubicin/docetaxel with or without tamoxifen as pre-operative therapy in operable breast cancer |
| [15161988](https://pubmed.ncbi.nlm.nih.gov/15161988/) | 2004 | Review | Oncologist | Docetaxel and paclitaxel are fundamental drugs in metastatic, adjuvant and neoadjuvant breast cancer therapy |
| [9282422](https://pubmed.ncbi.nlm.nih.gov/9282422/) | 1997 | Review | Drug Ther Bull | Review of paclitaxel and docetaxel in breast and ovarian cancer |
| [7595719](https://pubmed.ncbi.nlm.nih.gov/7595719/) | 1995 | Review | J Clin Oncol | Preclinical and clinical profile of docetaxel |
| [26874836](https://pubmed.ncbi.nlm.nih.gov/26874836/) | 2017 | Single-arm study | Breast Cancer | Neoadjuvant docetaxel, cyclophosphamide and trastuzumab in HER2-positive primary breast cancer |
| [15858439](https://pubmed.ncbi.nlm.nih.gov/15858439/) | 2005 | Phase II interim analysis | Breast Cancer | CEF followed by docetaxel as preoperative chemotherapy in early breast cancer (79 patients) |
| [12599222](https://pubmed.ncbi.nlm.nih.gov/12599222/) | 2003 | Phase II | Cancer | Capecitabine plus docetaxel and epirubicin as first-line therapy for advanced breast cancer |
| [15585076](https://pubmed.ncbi.nlm.nih.gov/15585076/) | 2004 | Phase II | Clin Breast Cancer | Docetaxel/cisplatin as primary chemotherapy for locally advanced breast cancer |
| [27997437](https://pubmed.ncbi.nlm.nih.gov/27997437/) | 2017 | Retrospective cohort | Anti-Cancer Drugs | Association between adjuvant docetaxel-based chemotherapy and breast cancer-related lymphedema |

---

## US Market Information

The record shows 20 licenses. The 5 main ones are listed below. Approved-indication text was not captured for any of them.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| NDA022234 | Docetaxel | Injection, solution | Hospira, Inc. |
| NDA022534 | Docetaxel | Injection, solution | Sun Pharmaceutical Industries, Inc. |
| ANDA213510 | Docetaxel | Injection | Sagent Pharmaceuticals |
| ANDA207252 | Docetaxel | Injection, solution, concentrate | Jiangsu Hengrui Pharmaceuticals Co., Ltd. |
| ANDA210072 | Docetaxel | Injection, solution | Mylan Institutional LLC |

All forms are injectable.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (taxane, microtubule stabilizer) |
| Myelosuppression Risk | High. Neutropenia is the expected dose-limiting toxicity. Several retrieved trials use G-CSF support alongside docetaxel |
| Emetogenicity Classification | Low to moderate. Antiemetic prophylaxis is studied in docetaxel-cyclophosphamide regimens (NCT01298193) |
| Monitoring Items | CBC with differential, liver function, signs of fluid retention and peripheral neuropathy |
| Handling Protection | Must follow cytotoxic drug handling regulations |

These entries reflect the taxane class and the retrieved trials, not label data. Please refer to the package insert warnings and precautions.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Breast carcinoma has by far the strongest evidence of the ten predictions. It has multiple completed Phase 2 and Phase 3 trials, plus randomized adjuvant data and reviews. The main uncertainty is administrative: the pack shows no recorded original indication, so it is unclear whether this is a new indication or an existing labeled one.

**To proceed, the following is needed:**
- Confirm the approved indications from the current US package insert or Drugs@FDA. This is also the blocking gap for safety screening.
- Obtain the package insert's warnings and contraindications. The safety fields in the pack are empty.
- Obtain mechanism-of-action data from DrugBank to complete the mechanistic analysis.
- Manually review the Phase 3 trials to decide whether the evidence level should be upgraded from L2 to L1.

Only the top-ranked prediction (breast carcinoma) is evaluated here. The lung and sarcoma-related predictions show weaker or purely computational support (Hold or Research Question in the pack). Several of the lung-related trials are NSCLC studies, and the other predictions have no direct trials or literature.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

