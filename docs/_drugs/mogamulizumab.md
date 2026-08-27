---
layout: default
title: Mogamulizumab
parent: 僅模型預測 (L5)
nav_order: 938
evidence_level: L5
indication_count: 7
---

# Mogamulizumab
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

# Mogamulizumab: From Cutaneous T-Cell Lymphoma/ATL to Prostatic Urethra Urothelial Carcinoma

## One-Sentence Summary

Mogamulizumab is an anti-CCR4 monoclonal antibody; within this evidence pack it is referenced (in the rationale notes, not in a confirmed regulatory record) as approved for cutaneous T-cell lymphoma (CTCL) and adult T-cell leukemia-lymphoma (ATL). The TxGNN model predicts it may be effective for **prostatic urethra urothelial carcinoma**, but this is currently supported by **0 clinical trials** and **0 publications** — the prediction is model-score only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on file in this pack (`taiwan_regulatory.licenses` is empty); rationale text for other candidates references Mogamulizumab's known use in CTCL/ATL |
| Predicted New Indication | Prostatic urethra urothelial carcinoma |
| TxGNN Prediction Score | 99.44% (rank 12,947) |
| Evidence Level | L5 |
| US Market Status | Not Marketed (未上市) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack (flagged as a High-severity data gap, DG002). Based on the rationale notes attached to other candidate indications in this pack, Mogamulizumab is described as a monoclonal antibody targeting CCR4, which depletes CCR4⁺ regulatory T cells (Tregs) and induces antibody-dependent cellular cytotoxicity (ADCC) — a mechanism used to strengthen anti-tumor immune activity in its known indications (CTCL/ATL, T-cell malignancies).

The link to prostatic urethra urothelial carcinoma is a purely topological inference from the TxGNN knowledge graph, grounded in similarity between "urothelial carcinoma-type" tumors and diseases characterized by immune checkpoint/Treg exhaustion signatures — not in any direct biological or clinical evidence. Urothelial carcinoma of the prostatic urethra is mechanistically distinct from the T-cell lymphomas Mogamulizumab currently targets, and no trial, case report, or preclinical study in this pack bridges that gap.

Because `original_indications` is empty and `original_moa` is a data gap, a rigorous mechanism-to-mechanism comparison cannot be completed. This prediction should be read as a hypothesis-generating signal only, not as evidence of biological plausibility.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## US Market Information

No marketing authorization records are currently available — `taiwan_regulatory.market_status` is "未上市" (Not Marketed) with 0 total licenses on file.

---

## Cytotoxicity

Mogamulizumab is an antineoplastic monoclonal antibody (indicated per the pack's rationale notes for CTCL/ATL, both malignancies), so this section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Immunotherapy (anti-CCR4 monoclonal antibody, ADCC-mediated Treg depletion) — not a conventional cytotoxic agent |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction sits at evidence level L5 (model prediction only) with zero supporting trials or literature across all queried sources (ClinicalTrials.gov, ICTRP, PubMed). A Blocking-severity data gap (DG001 — TFDA label warnings/contraindications) also prevents this candidate from entering the S1 safety pre-screen.

**To proceed, the following is needed:**
- TFDA/FDA label data (warnings, contraindications) to clear the Blocking data gap (DG001)
- Confirmed mechanism of action and original indication record for Mogamulizumab (DG002)
- Any preclinical or case-level evidence linking CCR4/Treg-targeted therapy to prostatic urethra urothelial carcinoma before further investment
- Note: 6 additional TxGNN-predicted indications in this pack (kidney pelvis sarcomatoid transitional cell carcinoma, infiltrating bladder urothelial carcinoma sarcomatoid variant, renal pelvis papillary urothelial carcinoma, HHV-8-related tumor, ectomesenchymoma, malignant cutaneous granular cell skin tumor) carry the same L5/Hold status and the same evidence gaps
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

