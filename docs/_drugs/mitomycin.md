---
layout: default
title: Mitomycin
parent: 僅模型預測 (L5)
nav_order: 936
evidence_level: L5
indication_count: 10
---

# Mitomycin
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

# Mitomycin: From Gastrointestinal Cancer to Solid Pseudopapillary Carcinoma of Pancreas

## One-Sentence Summary

> Mitomycin (Mitomycin C) is a DNA-crosslinking antineoplastic antibiotic historically used in gastrointestinal cancer chemotherapy regimens.
> The TxGNN model predicts it may be effective for **Solid Pseudopapillary Carcinoma of Pancreas**,
> but this specific prediction is currently supported by **0 clinical trials** and **0 publications** — it is a pure knowledge-graph inference.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no regulatory license record exists for this drug in the current dataset |
| Predicted New Indication | Solid Pseudopapillary Carcinoma of Pancreas |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L5 |
| US Market Status | ✗ Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for mitomycin is not available in this evidence pack (flagged as a data gap). Based on known drug-class information referenced elsewhere in this same evidence pack (see rank 8 rationale), mitomycin is a DNA cross-linking antineoplastic antibiotic that has historically been used as a component of combination chemotherapy regimens (e.g., FAM: 5-FU/Adriamycin/Mitomycin) for gastrointestinal malignancies, including pancreatic cancer.

For the top-ranked prediction, solid pseudopapillary carcinoma of pancreas, the TxGNN knowledge-graph similarity score is very high (99.86%), but no clinical trial or literature evidence currently links mitomycin to this specific tumor subtype. It is also worth noting for clinical context that solid pseudopapillary carcinoma is generally a low-grade, surgically curable pancreatic tumor, and systemic cytotoxic chemotherapy is not standard first-line management — this makes the mechanistic rationale for this particular candidate weaker than for other candidates in the same prediction set.

Notably, a lower-ranked candidate in this same evidence pack — "malignant exocrine pancreas neoplasm" (rank 8) — has materially stronger supporting evidence (L3, two literature citations including a review on exocrine pancreatic cancer chemotherapy), since mitomycin has documented historical use in general pancreatic exocrine cancer regimens. Reviewers may wish to prioritize that candidate over the top-ranked one when deciding where to invest further evaluation effort.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## US Market Information

Not marketed — no license records are available (market status: Not Marketed; total licenses: 0).

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (DNA cross-linking antineoplastic antibiotic / alkylating-like agent) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (solid pseudopapillary carcinoma of pancreas) is supported only by a TxGNN similarity score (L5, S0) with no clinical trial or literature corroboration, and a blocking data gap exists for TFDA/FDA label warnings and contraindications, which prevents progression to safety initial screening (S1). The drug also has no current NDA/marketing record in this dataset.

**To proceed, the following is needed:**
- TFDA/FDA package insert data (warnings, contraindications) to clear the blocking data gap (DG001)
- Verified mechanism of action data from DrugBank or primary literature (DG002)
- Consider re-scoping evaluation priority toward rank 8 ("malignant exocrine pancreas neoplasm"), which already has L3 evidence and Research Question status
- Clinical trial or preclinical mechanistic studies specific to solid pseudopapillary carcinoma before any further advancement
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

