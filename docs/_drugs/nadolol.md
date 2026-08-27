---
layout: default
title: Nadolol
parent: 僅模型預測 (L5)
nav_order: 949
evidence_level: L5
indication_count: 5
---

# Nadolol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Nadolol: From Hypertension (Original Indication Undocumented) to Malignant Hypertensive Renal Disease

## One-Sentence Summary

Nadolol (DB01203) is a non-selective beta-adrenergic blocker; no approved indication text is available in this evidence pack, and the drug is currently **not marketed in Taiwan** (0 licenses). The TxGNN model predicts it may be effective for **Malignant Hypertensive Renal Disease**, but this prediction is supported by **0 clinical trials** and **0 publications** — it rests entirely on the network prediction score.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented — no Taiwan license on file and `original_indications` is empty in this evidence pack |
| Predicted New Indication | Malignant Hypertensive Renal Disease |
| TxGNN Prediction Score | 99.59% |
| Evidence Level | L5 (model prediction only, no trials or literature) |
| Taiwan Market Status | 未上市 (Not marketed) |
| Number of Licenses | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not populated in `drug.original_moa` (flagged as a High-severity data gap, DG002). Based on the TxGNN-generated rationale accompanying this candidate, nadolol is described as a non-selective beta-adrenergic blocker that lowers systemic blood pressure by reducing cardiac output and suppressing renin secretion.

Malignant hypertensive renal disease is a hypertensive-emergency phenotype with acute renal injury. In principle, a systemic blood-pressure-lowering mechanism is directionally compatible with this condition's treatment goal. However, the rationale itself flags an important fit-for-purpose mismatch: this clinical scenario typically requires titratable intravenous antihypertensives for rapid control, whereas nadolol is a long-acting oral agent (half-life 20–24 hours) — not a conventional treatment choice for an acute emergency. No clinical trial, trial registry, or publication record accompanies this candidate; the prediction is derived solely from the TxGNN network score (0.9959).

It is also worth noting that a tied-score sibling candidate (pulmonary hypertension owing to lung disease/hypoxia, rank 3) did return 20 PubMed records, but on review those papers concern hypoxia physiology, neurodegeneration, and tumor metabolism — none address nadolol or beta-blocker therapy in pulmonary hypertension. This illustrates a keyword-similarity artifact in the retrieval rather than genuine supporting evidence, and reinforces that the malignant-hypertensive-renal-disease candidate above should be read as an unvalidated network prediction only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Taiwan Market Information

Nadolol currently holds no marketing license in Taiwan (0 licenses on record); no approved indication text, product name, or dosage form is available to report.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No clinical trials or relevant literature support nadolol's use in malignant hypertensive renal disease; the candidate is Evidence Level L5 (prediction-only). The drug is also unmarketed in Taiwan with no labeling/safety data on file (TFDA warnings/contraindications are a Blocking data gap, DG001), and the drug's pharmacokinetic profile (long-acting oral) is a poor mechanistic fit for an acute hypertensive-emergency indication.

**To proceed, the following is needed:**
- TFDA/international package insert with warnings and contraindications (resolves Blocking gap DG001)
- Confirmed original indication and mechanism-of-action documentation (resolves High-severity gap DG002)
- Preclinical or clinical evidence specific to malignant hypertensive renal disease (or its close variant, malignant renovascular hypertension)
- Drug-drug interaction data, currently returned "not found"
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

