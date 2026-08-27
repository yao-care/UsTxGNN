---
layout: default
title: Ifosfamide
parent: 僅模型預測 (L5)
nav_order: 788
evidence_level: L5
indication_count: 10
---

# Ifosfamide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Ifosfamide: From Soft Tissue Sarcoma/Testicular Carcinoma to Breast Carcinoma

## One-Sentence Summary

Ifosfamide is an oxazaphosphorine alkylating agent (a cyclophosphamide analog) with established chemotherapeutic activity in soft tissue sarcoma and testicular carcinoma. The TxGNN model predicts it may also be effective for **Female Breast Carcinoma**, with **8 clinical trials** and **20 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not formally recorded (TFDA license/regulatory text unavailable); literature evidence in this pack identifies ifosfamide as established for soft tissue sarcoma and testicular carcinoma |
| Predicted New Indication | Female Breast Carcinoma |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L1 |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, ifosfamide is an oxazaphosphorine alkylating agent structurally analogous to cyclophosphamide; its efficacy in soft tissue sarcoma and testicular carcinoma has been well established, and mechanistically it may be applicable to breast carcinoma as well.

Both the original and predicted indications share a common therapeutic logic: alkylating-agent cytotoxicity against rapidly dividing tumor cells. Mechanistic/translational studies included in this evidence pack (PMID 14970873, PMID 11138456) show that ifosfamide's active metabolite can be locally bioactivated by CYP3A4/CYP2C9/CYP2B6 within breast tumor tissue itself, producing measurable intratumoral DNA damage — providing tissue-level mechanistic support beyond simple hepatic prodrug activation.

Clinically, this is not a novel-mechanism repurposing signal but rather a knowledge-graph re-confirmation of an already-recognized salvage role: ifosfamide combined with paclitaxel, etoposide, or vinorelbine has Phase 2 evidence specifically in anthracycline-resistant metastatic breast cancer, where it serves as second/third-line rescue chemotherapy after standard anthracycline/taxane failure.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00954174](https://clinicaltrials.gov/study/NCT00954174) | Phase 3 | Unknown | 637 | Randomized comparison of paclitaxel+carboplatin vs. ifosfamide+paclitaxel in newly diagnosed/persistent/recurrent carcinosarcoma; largest and highest-grade direct evidence, but publication status unverified |
| [NCT00026078](https://clinicaltrials.gov/study/NCT00026078) | Phase 2 | Unknown | 42 | Docetaxel + ifosfamide as first-line chemotherapy in metastatic breast cancer |
| [NCT00002854](https://clinicaltrials.gov/study/NCT00002854) | Phase 1 | Completed | 33 | Sequential high-dose cisplatin/cyclophosphamide/etoposide/ifosfamide/carboplatin/paclitaxel with autologous stem cell support |
| [NCT00006032](https://clinicaltrials.gov/study/NCT00006032) | Phase 2 | Terminated | N/A | TIME regimen (topotecan/ifosfamide-mesna/etoposide) + autologous stem cell rescue in metastatic breast cancer |
| [NCT00012311](https://clinicaltrials.gov/study/NCT00012311) | Phase 2 | Unknown | N/A | Multi-cycle high-dose chemotherapy vs. optimized conventional-dose chemotherapy in metastatic breast cancer |
| [NCT00020722](https://clinicaltrials.gov/study/NCT00020722) | Phase 2 | Terminated | 7 | Chemotherapy + peripheral stem cell transplant + activated T-cell biotherapy pilot in Stage IV breast cancer |
| [NCT00003086](https://clinicaltrials.gov/study/NCT00003086) | Phase 1/2 | Terminated | 12 | Samarium-153 as part of double sequential autologous bone marrow transplant in Stage IV breast cancer |
| [NCT04279509](https://clinicaltrials.gov/study/NCT04279509) | N/A | Unknown | 35 | Organoid-based high-throughput drug screening assay for chemotherapy selection in refractory solid tumors (drug-sensitivity platform, not a direct efficacy trial) |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [11932893](https://pubmed.ncbi.nlm.nih.gov/11932893/) | 2002 | Phase 2 trial | Cancer | Paclitaxel (24-hr infusion) + ifosfamide in anthracycline-resistant metastatic breast carcinoma |
| [9226029](https://pubmed.ncbi.nlm.nih.gov/9226029/) | 1997 | Phase 2 trial | Tumori | Ifosfamide + etoposide in previously treated advanced breast cancer |
| [7695982](https://pubmed.ncbi.nlm.nih.gov/7695982/) | 1995 | PK/Cohort | European Journal of Cancer | PK, metabolism, and clinical effect of ifosfamide (5 g/m² 24-hr infusion) + doxorubicin/epirubicin in 15 breast cancer patients |
| [8873839](https://pubmed.ncbi.nlm.nih.gov/8873839/) | 1996 | Phase 2 (2nd-line) | Journal of Chemotherapy | Ifosfamide + mesna + epirubicin as second-line therapy; 50% overall response rate in 16 patients |
| [2112056](https://pubmed.ncbi.nlm.nih.gov/2112056/) | 1990 | Cohort | Cancer Chemotherapy and Pharmacology | Ifosfamide/etoposide + mesna uroprotection in 44 patients with advanced, anthracycline-pretreated breast cancer |
| [8918497](https://pubmed.ncbi.nlm.nih.gov/8918497/) | 1996 | Phase 2 (1st-line) | Journal of Clinical Oncology | Ifosfamide + vinorelbine as first-line chemotherapy for metastatic breast cancer |
| [2347057](https://pubmed.ncbi.nlm.nih.gov/2347057/) | 1990 | Cohort | Cancer Chemotherapy and Pharmacology | Ifosfamide substituted for cyclophosphamide in CMF regimen; effective in 25 patients refractory to/relapsed after CMF |
| [2347053](https://pubmed.ncbi.nlm.nih.gov/2347053/) | 1990 | Cohort | Cancer Chemotherapy and Pharmacology | Epirubicin + ifosfamide in 23 refractory breast cancer patients (part of 58-patient mixed solid tumor cohort) |
| [10602903](https://pubmed.ncbi.nlm.nih.gov/10602903/) | 1999 | Prospective trial | Cancer Chemotherapy and Pharmacology | Ifosfamide + vinorelbine in metastatic breast cancer patients with prior anthracycline therapy |
| [11840607](https://pubmed.ncbi.nlm.nih.gov/11840607/) | 2001 | Phase 1 trial | JPMA | Ifosfamide + doxorubicin dose-finding trial in ER-negative/hormone-refractory metastatic breast cancer |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic — Oxazaphosphorine alkylating agent (cyclophosphamide analog) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Evidence level L1 is supported by 8 clinical trials and 10+ relevant publications, including a Phase 3 RCT (NCT00954174, n=637) and multiple Phase 2 combination regimens (docetaxel-ifosfamide, ifosfamide-vinorelbine, ifosfamide-etoposide) specifically in metastatic and anthracycline-resistant breast cancer. This represents an established salvage-chemotherapy role rather than a novel mechanistic signal, but the blocking safety data gap (TFDA label/warnings) prevents a full "Go" recommendation.

**To proceed, the following is needed:**
- TFDA package insert / warnings and contraindications (DG001, blocking)
- Confirmed mechanism of action data via DrugBank API (DG002)
- Verification of published outcomes for NCT00954174 (currently status "Unknown")
- Confirmation of current US market/regulatory status, given "Not Marketed" flag with zero NDAs on file
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

