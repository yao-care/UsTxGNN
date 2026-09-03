---
layout: default
title: Mercuric Iodide
parent: 僅模型預測 (L5)
nav_order: 902
evidence_level: L5
indication_count: 10
---

# Mercuric Iodide
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

# Mercuric Iodide: From No Approved Indication to Ventricular Tachycardia

## One-Sentence Summary

> Mercuric Iodide (DrugBank DB04445) has no recorded approved indication and is not currently marketed in Taiwan or the US.
> The TxGNN model predicts it may be effective for **Ventricular Tachycardia**,
> but this prediction is currently supported by **0 clinical trials** and **0 publications**, and the compound's known pharmacology (mercury-ion cardiotoxicity) points in the opposite direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | No approved indication on record |
| Predicted New Indication | Ventricular Tachycardia |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| US Market Status | 未上市 (Not Marketed) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available for Mercuric Iodide, and no approved original indication exists in the source registries — the compound is not currently marketed under any NDA in Taiwan or the US. This makes the usual "original indication → new indication" mechanistic bridge impossible to construct from regulatory data alone.

The only mechanistic signal available comes from the model's own repurposing rationale, and it argues against therapeutic plausibility rather than for it: mercury ions are known to interfere with cardiac ion channels and are associated with cardiotoxicity, which is the opposite of a therapeutic antiarrhythmic effect. This pattern repeats across all ten of the top TxGNN-predicted indications for this compound (ventricular tachycardia, bundle branch block, atrial tachycardia, atrial fibrillation, etc.) — every one is scored L5 (model prediction only, no clinical or literature support), and for two of them (idiopathic neonatal atrial flutter, incessant infant ventricular tachycardia) the annotated rationale explicitly flags heavy-metal toxicity risk in neonatal/infant populations as a safety red flag rather than a treatment rationale.

Taken together, this looks like a high embedding-similarity artifact of the knowledge graph rather than a biologically grounded repurposing signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

Please refer to the package insert for safety information. Note: this compound has no active Taiwan/US marketing authorization, so no current package insert exists — TFDA label/warning data (data gap DG001) remains an unresolved blocking gap for any safety assessment.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- No original indication, no confirmed MOA, and zero clinical or literature evidence exist for the predicted indication; the evidence level is L5 (model score only), and the compound's known mercury-ion cardiotoxicity mechanistically contradicts an antiarrhythmic use rather than supporting one.

**To proceed, the following is needed:**
- TFDA label / warnings & contraindications data (blocking gap DG001)
- Verified mechanism of action from DrugBank or primary literature (gap DG002)
- Preclinical or mechanistic studies establishing any plausible cardiac-therapeutic pathway
- Any clinical trial or case-report evidence in ventricular tachycardia or related arrhythmias before further evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

