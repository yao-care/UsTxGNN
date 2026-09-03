---
layout: default
title: Mitoxantrone
parent: 僅模型預測 (L5)
nav_order: 937
evidence_level: L5
indication_count: 8
---

# Mitoxantrone
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Mitoxantrone: From Established Antineoplastic Chemotherapy to Upper Aerodigestive Tract Neoplasm

## One-Sentence Summary

Mitoxantrone is an anthraquinone antineoplastic agent, structurally related to the anthracyclines, historically used against metastatic breast cancer, acute leukemias, and non-Hodgkin lymphoma. The TxGNN model predicts it may also be effective for **Upper Aerodigestive Tract Neoplasm**, a prediction supported by **1 registered clinical trial** and **20 publications**, including several Phase II trials in head-and-neck-region cancers. No Taiwan/US marketing or formal safety-label data are currently available for this drug.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available from TFDA/US license records (0 licenses on file); per literature, mitoxantrone is historically used for metastatic breast cancer, acute leukemias, and non-Hodgkin lymphoma |
| Predicted New Indication | Upper Aerodigestive Tract Neoplasm |
| TxGNN Prediction Score | 99.78% |
| Evidence Level | L3 (single-arm Phase II trials + 1 systematic review; no completed RCT) |
| US Market Status | 未上市 (Not Marketed) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed, structured mechanism-of-action data is not currently available for mitoxantrone in this evidence pack (flagged as a High-severity data gap). Based on the literature returned by the same evidence collection, mitoxantrone is described as an anthraquinone antineoplastic agent "with structural similarities to doxorubicin" and "a mechanism of action similar to the anthracyclines" (PMID 3512224) — i.e., a DNA-intercalating topoisomerase II inhibitor. This class of drugs is broadly cytotoxic across proliferating tumor cells and is not tissue-restricted, which mechanistically supports testing in additional solid-tumor indications.

"Upper aerodigestive tract neoplasm" is an umbrella term covering cancers of the oral cavity, pharynx, larynx, and related structures (head and neck, nasopharyngeal, salivary gland, and adenoid cystic carcinomas). The evidence pack shows that this overlaps substantially with the independently-ranked "head and neck cancer" indication (rank 7 in this same evidence pack), which has stronger and more recent trial support (6 registered trials, including ongoing Phase II/III studies of liposomal mitoxantrone in nasopharyngeal carcinoma). This convergence across two independently scored TxGNN predictions strengthens biological plausibility.

Historically, mitoxantrone has already been studied as monotherapy and in combination regimens (with cisplatin, ifosfamide, raltitrexed/5-FU) specifically in head-and-neck-region cancers dating back to the 1980s–2000s, with modest single-agent response rates reported. This existing investigational track record in an anatomically overlapping tumor group is the most direct evidence supporting the TxGNN prediction, rather than a purely novel mechanistic hypothesis.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06953739](https://clinicaltrials.gov/study/NCT06953739) | Phase 3 | Not Yet Recruiting | 60 | Multicenter RCT comparing pegaspargase-based P-GEMD vs. P-Gemox regimens in untreated early-stage non-upper-aerodigestive-tract or advanced-stage extranodal NK/T-cell lymphoma; the exact composition of P-GEMD (whether it includes mitoxantrone) is not specified in the evidence pack. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31324333](https://pubmed.ncbi.nlm.nih.gov/31324333/) | 2019 | Systematic Review | Bulletin du Cancer | Systematic review of systemic treatments (chemotherapy, targeted therapy, immunotherapy) for recurrent/metastatic adenoid cystic carcinoma of the head and neck. |
| [8922205](https://pubmed.ncbi.nlm.nih.gov/8922205/) | 1996 | Phase II Trial | Annals of Oncology | EORTC Head and Neck Cancer Cooperative Group Phase II study of mitoxantrone monotherapy in adenoid cystic carcinoma. |
| [1650529](https://pubmed.ncbi.nlm.nih.gov/1650529/) | 1991 | Phase II Trial | American Journal of Clinical Oncology | Phase II trial of single-agent mitoxantrone (14 mg/m² q3w) in 19 patients with incurable head and neck carcinoma; toxicity mainly mild-to-moderate leukopenia. |
| [11290867](https://pubmed.ncbi.nlm.nih.gov/11290867/) | 2001 | Phase II Trial | Anti-Cancer Drugs | Ifosfamide + mitoxantrone combination in recurrent/metastatic squamous cell carcinoma of the head and neck. |
| [12045460](https://pubmed.ncbi.nlm.nih.gov/12045460/) | 2002 | Phase II Trial | Anti-Cancer Drugs | Mitoxantrone + cisplatin in recurrent/metastatic salivary gland malignancies (14 patients). |
| [1735075](https://pubmed.ncbi.nlm.nih.gov/1735075/) | 1992 | PK/PD Study | Cancer | Pharmacokinetic/pharmacodynamic study of IV mitoxantrone (12–14 mg/m²) in 15 patients with advanced nasopharyngeal carcinoma. |
| [11269736](https://pubmed.ncbi.nlm.nih.gov/11269736/) | 2001 | Phase I Trial | Cancer Chemotherapy and Pharmacology | Phase I study of mitoxantrone + raltitrexed + levofolinic acid + 5-FU in advanced solid tumors, building on prior activity in head and neck/colorectal cancer. |
| [3512224](https://pubmed.ncbi.nlm.nih.gov/3512224/) | 1986 | Review | Drug Intelligence & Clinical Pharmacy | General pharmacology review; notes reported activity of mitoxantrone in head and neck cancer among other tumor types. |
| [39472118](https://pubmed.ncbi.nlm.nih.gov/39472118/) | 2024 | Clinical Study | Chinese Journal of Otorhinolaryngology Head and Neck Surgery | Application of mitoxantrone hydrochloride as a tracer for cervical lymph node/parathyroid identification during thyroid cancer surgery (n=180). |
| [38514342](https://pubmed.ncbi.nlm.nih.gov/38514342/) | 2024 | Clinical Study | Zhonghua Yi Xue Za Zhi | Dual fluorescence imaging (including mitoxantrone tracing) for central lymph node/parathyroid identification in thyroid cancer surgery. |

---

## US Market Information

Currently no marketing authorization records are on file — `taiwan_regulatory.total_licenses = 0` and market status is "未上市" (Not Marketed).

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (anthracenedione/anthraquinone class, topoisomerase II inhibitor structurally related to anthracyclines) |
| Myelosuppression Risk | High — multiple trial reports across indications describe leukopenia and thrombocytopenia as the major dose-limiting toxicities (e.g., PMID 1650529: "leukopenia was mild, moderate, sev[ere]"; other trials in this evidence pack cite leukopenia/thrombocytopenia as major toxicities) |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions (not reported in this evidence pack) |
| Monitoring Items | CBC with differential; liver and renal function; cardiac monitoring (ECG/LVEF) given known anthracenedione-class cardiotoxicity |
| Handling Protection | Requires cytotoxic drug handling precautions per standard chemotherapy handling regulations |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The literature base (L3: systematic review plus multiple single-arm Phase II trials) shows modest but real single-agent/combination activity of mitoxantrone in head-and-neck-region tumors, and the only registered trial for this specific indication is not yet recruiting. Critically, TFDA warning/contraindication data is a **Blocking** gap that prevents any S1 safety pre-assessment, and the drug currently has no Taiwan or US marketing authorization.

**To proceed, the following is needed:**
- TFDA (or equivalent international) package insert data — warnings, contraindications, precautions
- Confirmed mechanism-of-action data from DrugBank
- Drug-drug interaction (DDI) data (current query returned "not_found")
- Monitoring of NCT06953739 as it advances past "Not Yet Recruiting"
- Clarification of regimen composition (does P-GEMD include mitoxantrone?) before citing that trial as direct supporting evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

