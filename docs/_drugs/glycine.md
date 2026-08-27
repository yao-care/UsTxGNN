---
layout: default
title: Glycine
parent: 僅模型預測 (L5)
nav_order: 757
evidence_level: L5
indication_count: 2
---

# Glycine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# GLYCINE: From Unspecified Indication to Nasal Cavity Disease

## One-Sentence Summary

Glycine (DrugBank DB00145) has no original indication or mechanism-of-action data available in the current evidence pack, and it is not marketed in the reference jurisdiction. The TxGNN model predicts potential efficacy for **Nasal Cavity Disease** with a high score, but this prediction is currently backed by only **1 clinical trial** — which on review turns out to be unrelated to both glycine and nasal disease — and **no supporting literature**.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (no data provided) |
| Predicted New Indication | Nasal Cavity Disease |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L5 |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for glycine is not available, and no original indication is recorded in this evidence pack, so the pharmacological rationale for repurposing cannot be assessed.

The only clinical trial linked to this prediction (NCT01806675) was reviewed and found to be a PET/MRI imaging study of αvβ3 integrin expression as an angiogenesis biomarker in glioblastoma, gynecological cancer, and renal cell carcinoma patients — it has no relationship to glycine or to nasal cavity disease and was flagged as a false algorithmic match rather than genuine supporting evidence.

Because both the mechanistic basis and the clinical evidence are absent, the TxGNN score of 99.85% should be read as a graph-based statistical association only, not as a signal with any known biological plausibility for this indication.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01806675](https://clinicaltrials.gov/study/NCT01806675) | Phase 1/2 | Completed | 25 | PET/MRI imaging of ¹⁸F-FPPRGD2 uptake (αvβ3 integrin expression) in cancer patients on antiangiogenic therapy. Not related to glycine or nasal cavity disease — assessed as an unrelated false match, does not support this indication. |

## Literature Evidence

Currently no related literature available

## US Market Information

Not marketed in the reference jurisdiction; no license/NDA records available (0 licenses on file).

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The TxGNN score is high, but the sole cited clinical trial is unrelated to both the drug and the predicted indication, and no supporting literature exists — the evidence level is L5 (model prediction only), consistent with the decision stage S0 assessment.
- Absent mechanism-of-action and original-indication data, there is no pharmacological basis to corroborate the graph-based prediction.

**To proceed, the following is needed:**
- TFDA label warnings/contraindications — currently a **blocking** data gap that prevents entry into the S1 safety pre-assessment
- Mechanism of action (MOA) data for glycine (DrugBank query)
- Confirmed original indication(s) for glycine
- Genuine clinical or mechanistic evidence connecting glycine to nasal cavity disease (the current trial match should be excluded as irrelevant)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

