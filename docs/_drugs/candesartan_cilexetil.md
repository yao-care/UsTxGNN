---
layout: default
title: Candesartan Cilexetil
parent: Model Prediction Only (L5)
nav_order: 490
evidence_level: L5
indication_count: 5
---

# Candesartan Cilexetil
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Candesartan Cilexetil: From Hypertension to Malignant Hypertensive Renal Disease

## One-Sentence Summary

Candesartan cilexetil is an oral tablet marketed in the US. The supplied record lists no approved indication text, but the drug is generally known as an angiotensin II type 1 receptor blocker used for hypertension. The TxGNN model predicts it may be useful for **malignant hypertensive renal disease**, but there are **0 clinical trials** and **0 publications** supporting this direction, so it remains a model-only hypothesis.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the supplied record (generally known use: hypertension, from external knowledge) |
| Predicted New Indication | Malignant hypertensive renal disease |
| TxGNN Prediction Score | 99.68% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 licenses (NDA and ANDA combined) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on general knowledge, not on the supplied data, candesartan is an angiotensin II type 1 (AT1) receptor blocker with antihypertensive and kidney-protective use. Mechanistically, it may be applicable to hypertensive kidney disease.

Two cautions apply:

- The prediction may overlap with existing hypertension labeling rather than represent true repurposing.
- Malignant hypertension is a hypertensive emergency, so an oral ARB is unlikely to be a first-line treatment.

The same score (99.68%) was also given to malignant renovascular hypertension. This suggests the two predictions share a graph neighborhood rather than being independent signals.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

The record contains no approved-indication text for these licenses, so that column is omitted. 5 of 20 licenses are shown.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| NDA020838 | Candesartan cilexetil | Tablet | Golden State Medical Supply, Inc. |
| ANDA210302 | Candesartan cilexetil | Tablet | Alembic Pharmaceuticals Inc. |
| ANDA209119 | Candesartan cilexetil | Tablet | Alembic Pharmaceuticals Limited |
| ANDA078702 | Candesartan cilexetil | Tablet | Mylan Pharmaceuticals Inc. |
| ANDA203813 | Candesartan | Tablet | Macleods Pharmaceuticals Limited |

The only available route is oral (tablet).

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found in the supplied data.

One caution comes from general ARB knowledge rather than the supplied label data. ARBs carry a known safety concern in bilateral renal artery stenosis, which is relevant to the renovascular hypertension prediction and needs specific review.

## Other Predictions in the Record

| Predicted Indication | Score | Evidence | Comment |
|------|------|------|------|
| Malignant renovascular hypertension | 99.68% | None | ARB blockade is plausible, but renal artery stenosis safety needs review |
| Pulmonary hypertension, unclear multifactorial mechanism | 99.67% | None | Heterogeneous category, weak single rationale |
| Pulmonary hypertension owing to lung disease and/or hypoxia | 99.67% | 20 retrieved papers, all generic hypoxia literature | None appear to address candesartan or this indication, so they were not counted as evidence. Vasodilation and hypotension in hypoxemic lung disease is a theoretical concern |
| Braddock syndrome | 99.56% | None | No plausible mechanistic link evident; may be a graph-topology artifact |

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is model-only (L5) with no trials or publications. The original indication and mechanism data are missing from the record, and the predicted disease is a hypertensive emergency where an oral ARB is unlikely to be first-line.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Approved indication text and mechanism of action data from DrugBank
- A targeted literature and trial search on candesartan in malignant hypertension and hypertensive nephropathy
- A check of whether the indication already falls under existing hypertension labeling
- Renal safety review, including bilateral renal artery stenosis, before any further step

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

