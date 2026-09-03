---
layout: default
title: Quinapril
parent: 僅模型預測 (L5)
nav_order: 1101
evidence_level: L5
indication_count: 5
---

# Quinapril
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

# Quinapril: From Hypertension to Malignant Renovascular Hypertension

## One-Sentence Summary

> Quinapril is an ACE inhibitor whose established pharmacological class is used to control systemic blood pressure by suppressing the renin-angiotensin-aldosterone system (RAAS).
> The TxGNN model predicts it may be effective for **Malignant Renovascular Hypertension**,
> but currently **0 clinical trials** and **0 publications** support this specific direction — the prediction is model-generated only, and the underlying mechanism rationale itself flags a known safety concern rather than a clear therapeutic opportunity.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension (ACE inhibitor drug class); no locally approved indication text on file — drug is currently unmarketed in this jurisdiction |
| Predicted New Indication | Malignant Renovascular Hypertension |
| TxGNN Prediction Score | 99.86% (rank 4328) |
| Evidence Level | L5 (model prediction only, no clinical trials or literature) |
| Market Status | ✗ Not Marketed |
| Number of Licenses | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for quinapril is not present in this evidence pack (Data Gap DG002, High severity). Based on the pharmacological class information included in the repurposing rationale, quinapril is an ACE inhibitor that lowers systemic blood pressure by suppressing the RAAS pathway.

There is a theoretical mechanistic link between this mode of action and malignant renovascular hypertension, since the disease's pathophysiology (renal artery stenosis) itself drives pathological RAAS overactivation. On the surface, this makes ACE inhibition seem mechanistically relevant.

However, this same evidence pack explicitly notes a critical caveat: in patients with bilateral renal artery stenosis or stenosis of a functionally solitary kidney, ACE inhibitors sharply reduce glomerular filtration pressure and are considered a **relative contraindication** rather than a treatment option. Bilateral disease must be ruled out before cautious use is even considered. In other words, this "predicted indication" largely reflects a well-known drug-disease safety interaction rather than a novel therapeutic opportunity — the mechanistic rationale argues for caution, not efficacy.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

No marketing authorization records available. Quinapril is currently unmarketed in this jurisdiction (0 licenses on file).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- Evidence Level is L5 — this is a model prediction with zero supporting clinical trials or literature for the top-ranked indication.
- The mechanistic rationale itself identifies a known safety risk: ACE inhibitors are relatively contraindicated in bilateral renal artery stenosis/functional single-kidney stenosis, which is the core pathology of malignant renovascular hypertension. This suggests the prediction may reflect a risk scenario rather than a genuine repurposing opportunity.
- Critical safety data (label warnings, contraindications, DDI) are entirely missing (Data Gap DG001, **Blocking**) — the candidate cannot proceed even to an S1 safety pre-screening step.
- Quinapril currently has 0 marketing licenses in this jurisdiction, so no confirmed regulatory or supply pathway exists locally.

**To proceed, the following is needed:**
- TFDA (or equivalent regulator) label PDF acquisition and parsing to obtain warnings/contraindications (DG001)
- DrugBank-sourced structured MOA data to support mechanism-linkage analysis (DG002)
- Renal function/nephrology-specific safety data for populations with renal artery stenosis
- Independent confirmation of whether "malignant renovascular hypertension" should be treated as a contraindicated population rather than a candidate indication before further evaluation

**Note:** Ranks 2–5 of the predicted indications (malignant hypertensive renal disease, pulmonary hypertension owing to lung disease/hypoxia, pulmonary hypertension with unclear multifactorial mechanism, Braddock syndrome) all carry the same L5/Hold status. One (rank 3) is supported only by 20 literature hits that appear to be spurious keyword matches on "hypoxia" unrelated to quinapril or ACE inhibitors, and another (rank 5, Braddock syndrome) has no known biological link to the RAAS pathway. This reinforces that the current prediction set should not move forward without substantial additional evidence.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

