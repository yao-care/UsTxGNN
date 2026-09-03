---
layout: default
title: Trifarotene
parent: 僅模型預測 (L5)
nav_order: 1260
evidence_level: L5
indication_count: 2
---

# Trifarotene
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

# Trifarotene: From Acne Vulgaris to Zinc, Elevated Plasma

## One-Sentence Summary

> Trifarotene is a topical retinoid publicly known for the treatment of acne vulgaris.
> The TxGNN model predicts it may be relevant to **Zinc, Elevated Plasma**,
> but this prediction is currently supported by **0 clinical trials** and **0 publications** — it is a model-only signal with no corroborating evidence.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Acne vulgaris (topical retinoid) — not present in evidence pack, based on public drug information |
| Predicted New Indication | Zinc, Elevated Plasma |
| TxGNN Prediction Score | 99.40% (rank 13,778) |
| Evidence Level | L5 |
| US Market Status | Not marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a High-severity data gap, DG002). Based on publicly known information, trifarotene is a retinoic acid receptor gamma (RAR-γ) selective agonist used topically for acne vulgaris. Its efficacy in that original indication is well established, but no mechanistic pathway data is currently available in this evidence pack to explain a plausible link between RAR-γ agonism and elevated plasma zinc levels.

The model's own repurposing rationale fields for this candidate are marked `pending`, meaning TxGNN has not yet generated an explanatory mechanistic narrative for this pairing. Without literature, clinical trial data, or MOA-based reasoning, the connection between the original and predicted indications cannot currently be substantiated beyond the raw prediction score.

It is worth noting that the second-ranked candidate, **pyogenic arthritis-pyoderma gangrenosum-acne syndrome (PAPA syndrome)** (score 99.32%, rank 15,213), has a more intuitive phenotypic overlap with the original indication, since acne is a defining feature of PAPA syndrome. This candidate may warrant separate evaluation even though it falls outside the scope of the rank-1 prediction covered here.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

No marketing authorization is currently on file for trifarotene in this dataset (0 licenses, market status: Not marketed).

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: TFDA/FDA label warnings and contraindications are marked as a Blocking data gap (DG001) — this prevents any formal safety review of this candidate.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This candidate has no clinical trial or literature evidence (L5, model-prediction-only), the drug has no confirmed marketing status in this dataset, and safety labeling data required for even a preliminary safety screen is missing (Blocking gap DG001). There is insufficient basis to advance this prediction.

**To proceed, the following is needed:**
- TFDA/FDA package insert data (warnings, contraindications) — resolves DG001, required before any S1 safety screen
- Mechanism of action (MOA) data — resolves DG002, needed to assess mechanistic plausibility
- Literature or preclinical search specifically on trifarotene and zinc metabolism/homeostasis
- Confirmation of current US marketing status and license details
- Consider evaluating the rank-2 candidate (PAPA syndrome) in parallel, given its stronger phenotypic rationale
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

