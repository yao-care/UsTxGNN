---
layout: default
title: Amiloride
parent: Model Prediction Only (L5)
nav_order: 326
evidence_level: L5
indication_count: 6
---

# Amiloride
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

# Amiloride: From Oral Potassium-Sparing Diuretic to Malignant Hypertensive Renal Disease

## One-Sentence Summary

Amiloride is an oral tablet diuretic that is currently marketed in the United States. The TxGNN model predicts it may be effective for **malignant hypertensive renal disease**, with a score of 99.82%. However, there are **0 clinical trials** and **0 publications** for this indication, so the prediction rests on the model alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Malignant hypertensive renal disease |
| TxGNN Prediction Score | 99.82% |
| Evidence Level | L5 (model prediction only) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 4 (1 NDA and 3 ANDA-type authorizations) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

The source MOA field for this drug is not available. Based on the drug-level analysis, amiloride blocks the epithelial sodium channel (ENaC). It has a mild antihypertensive, potassium-sparing effect. This is plausible for volume-dependent hypertension, so the link to a hypertensive kidney condition is understandable.

There is an important caveat. Malignant hypertension with renal involvement is a hypertensive emergency, and it is normally managed with rapid-acting agents. A mild oral diuretic is unlikely to be a primary therapy. It could at most play a supporting role. The 0.998 score reflects knowledge-graph proximity, not confirmed clinical benefit.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA070346 | Amiloride Hydrochloride | Tablet | Bryant Ranch Prepack |
| ANDA070346 | Amiloride Hydrochloride | Tablet | Endo USA, Inc. |
| ANDA079133 | Amiloride Hydrochloride | Tablet | Sigmapharm Laboratories, LLC |
| NDA018200 | Amiloride Hydrochloride | Tablet | Padagis US LLC |

All products are oral tablets. The approved indication text was not available in the records provided.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting trials or literature (L5). The proposed condition is a hypertensive emergency, for which a mild oral diuretic is an unlikely primary therapy.

Among the other predicted indications in this Evidence Pack, only **chronic pulmonary heart disease** (rank 6, score 99.68%) reached the S1 "Research Question" stage. It has indirect heart-failure studies (L4) and a hyperkalemia safety signal that would need assessment. If the team wants to prioritize one direction for amiloride, that one is more promising than this rank 1 prediction.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (blocking for safety screening)
- Mechanism of action data from DrugBank
- A targeted literature search on amiloride in malignant or hypertensive nephrosclerosis
- Clinical input on whether an add-on role is realistic in a hypertensive emergency setting
- Hyperkalemia and renal function risk assessment, since potassium retention matters in kidney disease
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

