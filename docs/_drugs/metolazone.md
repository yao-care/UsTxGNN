---
layout: default
title: Metolazone
parent: 僅模型預測 (L5)
nav_order: 918
evidence_level: L5
indication_count: 5
---

# Metolazone
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

# Metolazone: From Diuretic/Antihypertensive Use to Malignant Renovascular Hypertension

## One-Sentence Summary

Metolazone is a drug whose original approved indication and detailed mechanism of action are not documented in this evidence pack, though background pharmacological knowledge identifies it as a thiazide-like diuretic used for hypertension and edema. The TxGNN model predicts it may be effective for **malignant renovascular hypertension**, but this prediction currently has **0 clinical trials** and **0 publications** supporting it — it rests on the knowledge-graph score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on file (no TFDA/US license records); background knowledge: thiazide-like diuretic for hypertension/edema |
| Predicted New Indication | Malignant renovascular hypertension |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L5 |
| US Market Status | Not marketed (未上市) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, metolazone is part of the thiazide-like diuretic class, its efficacy in hypertension and edema management has been established, and mechanistically it may in principle be relevant to blood-pressure-related conditions such as malignant renovascular hypertension.

However, the mechanistic link here is indirect at best. Malignant hypertension is a hypertensive emergency requiring immediate blood pressure reduction, typically with intravenous antihypertensive agents — diuretics are not standard first-line therapy for this acute presentation. No clinical trials, registry entries, or publications currently connect metolazone to this specific indication; the prediction is generated purely by TxGNN's knowledge-graph embedding, without any corroborating mechanistic, preclinical, or clinical evidence.

A closely related candidate in the same prediction set — pulmonary hypertension owing to lung disease and/or hypoxia (rank 3) — has 20 supporting PubMed records, though these are largely general hypoxia-biology reviews rather than metolazone-specific studies, and still no clinical trials. This suggests the overall evidence base for repurposing metolazone into any of the five predicted indications remains preliminary.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

Metolazone is not currently marketed under any Taiwan or US regulatory record in this dataset (market status: 未上市; 0 total licenses). No NDA or product listing information is available.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication (malignant renovascular hypertension) is supported only by a TxGNN model score (L5), with zero clinical trials and zero literature citations. The proposed mechanism is also biologically weak, since malignant hypertension is managed with acute IV antihypertensives rather than diuretics.

**To proceed, the following is needed:**
- TFDA/FDA label data confirming metolazone's approved indications and formal MOA (currently a blocking data gap for safety review)
- Preclinical or mechanistic studies directly linking thiazide-like diuretics to malignant renovascular hypertension or hypertensive emergency management
- Drug interaction and contraindication data (currently unavailable) before any safety assessment can begin
- Consider evaluating the alternate candidate "pulmonary hypertension owing to lung disease and/or hypoxia" (rank 3, L4, 20 supporting publications) as a comparatively better-evidenced research priority, though it still lacks clinical trial support
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

