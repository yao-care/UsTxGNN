---
layout: default
title: Epirubicin
parent: 僅模型預測 (L5)
nav_order: 661
evidence_level: L5
indication_count: 7
---

# Epirubicin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Epirubicin: From Anthracycline Chemotherapy to Primary Pulmonary Lymphoma

## One-Sentence Summary

Epirubicin is the 4'-epimer of doxorubicin, an anthracycline antineoplastic already used across breast, gastric, and lymphoma chemotherapy regimens, though this evidence pack does not carry a confirmed formal original indication record. The TxGNN model predicts it may be effective for **Primary Pulmonary Lymphoma**, but this direction is currently supported by **0 clinical trials** and **9 publications**, most of which are indirect (general anthracycline pharmacology reviews, Hodgkin's lymphoma regimens, and a lung-lymphoma misdiagnosis case report) rather than lung-lymphoma–specific trial data.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not established in this evidence pack — no `taiwan_regulatory.licenses` records exist (drug not marketed; see Data Gap DG001) |
| Predicted New Indication | Primary Pulmonary Lymphoma |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L4 |
| US Market Status | 未上市 (Not Marketed) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (Data Gap DG002). Based on the literature captured in this evidence pack, epirubicin is described as "the 4' epimer of the anthracycline antibiotic doxorubicin" (PMID 7686469), acting as a topoisomerase II inhibitor that intercalates DNA and induces double-strand breaks — the same class mechanism as doxorubicin, a core component of CHOP-based lymphoma chemotherapy.

Epirubicin has an established history of substituting for doxorubicin in lymphoma regimens specifically to reduce cardiotoxicity: it was used in MOPPEBVCAD and VEBEP protocols for advanced Hodgkin's lymphoma (PMID 16428496, 10526668, 7525516). This provides a plausible mechanistic bridge from lymphoma treatment in general to the rarer subtype "primary pulmonary lymphoma," but none of the retrieved literature directly studies epirubicin in this specific lung-confined lymphoma presentation.

The strongest caveat is evidentiary gap rather than mechanistic implausibility: the only literature item actually describing primary pulmonary/pleural lymphoma (PMID 36237246, a MALT lymphoma of the pleura misdiagnosis case) does not evaluate epirubicin at all, and the DLBCL/Hodgkin's citations are drawn from systemic (nodal) lymphoma populations, not the primary pulmonary subtype. This is why the mechanism is rated plausible (anthracycline class effect) but the direct evidence level remains low (L4).

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40728626](https://pubmed.ncbi.nlm.nih.gov/40728626/) | 2025 | RCT | Annals of Hematology | Pola-R-CHP (doxorubicin-based) first-line therapy performed well in 117 lower-risk/IPI 0-1 DLBCL patients; not epirubicin-specific but establishes anthracycline-regimen efficacy in DLBCL. |
| [7686469](https://pubmed.ncbi.nlm.nih.gov/7686469/) | 1993 | Review | Drugs | Foundational epirubicin pharmacology review; established efficacy in breast cancer, NSCLC and other malignancies as a doxorubicin analog. |
| [39192408](https://pubmed.ncbi.nlm.nih.gov/39192408/) | 2024 | Retrospective Cohort | Zhongguo Shi Yan Xue Ye Xue Za Zhi | Single-center analysis of primary extranodal DLBCL clinical features/prognosis in the rituximab era; no epirubicin-specific data. |
| [16428496](https://pubmed.ncbi.nlm.nih.gov/16428496/) | 2006 | Cohort | Clinical Cancer Research | 10-year results of MOPPEBVCAD regimen (includes epidoxirubicin) with limited radiotherapy in advanced Hodgkin's lymphoma; supports anthracycline-lymphoma class use. |
| [7525516](https://pubmed.ncbi.nlm.nih.gov/7525516/) | 1994 | Cohort | Int J Radiat Oncol Biol Phys | Extended-field radiotherapy outcomes in favorable stage IA-IIA Hodgkin's disease; anthracycline regimen background only. |
| [10526668](https://pubmed.ncbi.nlm.nih.gov/10526668/) | 1999 | Cohort | The Cancer Journal | VEBEP intensive regimen plus radiotherapy in advanced Hodgkin's disease; epirubicin-class anthracycline component. |
| [36237246](https://pubmed.ncbi.nlm.nih.gov/36237246/) | 2022 | Case Report | Translational Cancer Research | First reported Chinese case of pleural MALT lymphoma, easily misdiagnosed; does not evaluate epirubicin treatment. |
| [1866500](https://pubmed.ncbi.nlm.nih.gov/1866500/) | 1991 | Case Report | Rev Invest Clin | Case of primary non-Hodgkin's lymphoma of the lung with pleural effusion; no epirubicin treatment data. |
| [8386780](https://pubmed.ncbi.nlm.nih.gov/8386780/) | 1993 | Case Report | Rinsho Ketsueki | Malignant lymphoma arising after small cell lung carcinoma surgery/chemotherapy; treatment-resistant, no epirubicin efficacy signal. |

## US Market Information

Epirubicin currently has no marketing authorizations on record in this evidence pack (`total_licenses: 0`, `market_status: 未上市`). No product name, dosage form, or approved indication text is available to extract.

## Cytotoxicity

Epirubicin is an antineoplastic anthracycline (doxorubicin analog), confirmed directly in the evidence pack's own literature: "Epirubicin (4'-epidoxorubicin) is an antineoplastic agent derived from doxorubicin" (PMID 3005521).

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (Anthracycline / Topoisomerase II inhibitor) |
| Myelosuppression Risk | High — classic anthracycline myelosuppression; literature in this pack also documents elevated long-term risk of secondary AML/MDS after epirubicin-based adjuvant chemotherapy (PMID 15961765, 15905306, 12649100) |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions (not specified in this evidence pack) |
| Monitoring Items | CBC with differential, cardiac function/LVEF (anthracycline cardiotoxicity is documented in this pack — PMID 30231396, 17632683), liver function |
| Handling Protection | Standard cytotoxic drug handling precautions required; extravasation is a documented serious complication requiring prompt recognition (PMID 28062432) |

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug-interaction data are not available in this evidence pack; DDI query returned no results.)

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence for epirubicin in primary pulmonary lymphoma is L4 (mechanism/class-effect rationale only) — no clinical trials and no literature directly studying epirubicin in this specific lung-confined lymphoma subtype. The TFDA safety/label data gap (DG001, Blocking) also prevents this candidate from clearing the S1 safety screening stage.

**To proceed, the following is needed:**
- Resolve DG001 (TFDA label warnings/contraindications) before any S1 safety evaluation can proceed
- Resolve DG002 (confirmed DrugBank MOA record) to support the mechanistic rationale
- Confirm epirubicin's actual approved original indication(s), which are absent from this evidence pack
- Run a targeted literature/trial search using synonyms specific to pulmonary/pleural lymphoma (e.g., "pulmonary MALT lymphoma," "primary pulmonary DLBCL") rather than general lymphoma terms
- Note: within this same evidence pack, epirubicin's prediction for **small cell lung carcinoma** (rank 3) carries L1 evidence with completed Phase III RCTs and a "Proceed with Guardrails" recommendation — that candidate warrants comparative prioritization over this one
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

