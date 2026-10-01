---
layout: default
title: Metolazone
parent: Model Prediction Only (L5)
nav_order: 919
evidence_level: L5
indication_count: 5
---

# Metolazone
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

# Metolazone: From Edema and Hypertension to Malignant Renovascular Hypertension

## One-Sentence Summary

Metolazone is a thiazide-like diuretic, originally used for volume overload (edema) and hypertension.
The TxGNN model predicts it may be effective for **malignant renovascular hypertension**, but this is a model prediction only, with **0 clinical trials** and **0 publications** supporting it.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Edema and hypertension (diuretic/antihypertensive use; the US license records provided contain no indication text) |
| Predicted New Indication | Malignant renovascular hypertension |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 (all listed entries are ANDA generics) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available in the record. Based on known pharmacology, metolazone inhibits the Na⁺/Cl⁻ cotransporter in the distal convoluted tubule. This reduces circulating volume and lowers blood pressure. It is also used with loop diuretics in volume-overloaded states, including reduced GFR.

The link to the new indication is weak. Malignant renovascular hypertension is driven by the renin-angiotensin system. Volume depletion from a diuretic could stimulate renin release further. Diuretics are also not a standard therapy for hypertensive emergencies. The prediction is plausible only as an extension of the drug's general antihypertensive use.

The other top TxGNN predictions are also unsupported:

- **Malignant hypertensive renal disease (99.84%):** the link is indirect, and aggressive volume depletion could worsen renal perfusion.
- **Pulmonary hypertension (two entries, 99.83%):** at most, diuretics offer symptomatic relief of right-heart volume overload. The 20 retrieved publications concern hypoxia biology in general (brain aging, cancer, multiple sclerosis, altitude) and never mention metolazone. They reflect keyword matching, not relevant evidence.
- **Braddock syndrome (99.78%):** no mechanistic rationale can be identified. This looks like a knowledge-graph artifact.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA076466 | Metolazone | Tablet (oral) | Sandoz Inc; Bryant Ranch Prepack |
| ANDA217563 | Metolazone | Tablet (oral) | Micro Labs Limited |
| ANDA213827 | Metolazone | Tablet (oral) | American Health Packaging |

Approved indication text is not included in the license records provided.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on the model score alone, with no trials or relevant literature. The stated mechanism (volume depletion in a renin-driven condition) argues against benefit rather than for it. The pulmonary hypertension literature count is a keyword artifact.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- A targeted search for metolazone in renovascular or malignant hypertension, or a supporting mechanistic study
- Route compatibility and similarity-to-original assessments, both still pending
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

