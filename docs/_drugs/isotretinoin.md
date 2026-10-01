---
layout: default
title: Isotretinoin
parent: Model Prediction Only (L5)
nav_order: 817
evidence_level: L5
indication_count: 2
---

# Isotretinoin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

# Isotretinoin: From Severe Acne to Malignant Renovascular Hypertension

## One-Sentence Summary

Isotretinoin is an oral retinoid marketed in the US as capsules. The supplied data does not state its approved indication, but it is generally known for severe recalcitrant nodular acne.
The TxGNN model predicts it may be effective for **malignant renovascular hypertension** (and the closely related malignant hypertensive renal disease), but there are currently **0 clinical trials** and **0 publications** supporting this direction. This is a model-only signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the supplied data (all approved-indication fields are empty); generally known as severe recalcitrant nodular acne |
| Predicted New Indication | Malignant renovascular hypertension |
| TxGNN Prediction Score | 99.01% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Isotretinoin is a retinoid, and retinoids act through RAR/RXR nuclear receptor signaling. One speculative link is that this signaling may influence regulation of the renin-angiotensin system, which has some preclinical support. Nothing in the supplied data verifies it.

The original and predicted indications are unrelated. Acne is a dermatological condition, and malignant renovascular hypertension is a severe cardiovascular and renal condition. Isotretinoin has no known antihypertensive use. The 0.990 score comes from knowledge-graph proximity alone, with no trial or literature support.

The second predicted indication, **malignant hypertensive renal disease**, has an identical score (0.990) and is closely related to the first. Both are probably driven by the same neighboring nodes in the knowledge graph, so they should be read as **one signal, not two independent lines of evidence**.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

The supplied licenses carry no approved-indication text, so that column is omitted. 5 of the 20 licenses are shown below.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA218194 | Isotretinoin | Capsule | Aurobindo Pharma Limited |
| ANDA211568 | Isotretinoin | Capsule | Zydus Pharmaceuticals USA Inc. |
| ANDA216633 | Isotretinoin | Capsule | Zydus Lifesciences Limited |
| NDA021951 | Isotretinoin | Capsule | Sun Pharmaceutical Industries, Inc. |
| ANDA216633 | Isotretinoin | Capsule | Zydus Pharmaceuticals USA Inc. |

All products are oral. Listed forms are capsule, liquid-filled capsule, and gelatin-coated capsule.

---

## Safety Considerations

Please refer to the package insert for safety information. No warnings or contraindications were supplied, and the drug-interaction query returned no results.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a knowledge-graph score. There are no trials or literature, no documented mechanism, and no known antihypertensive use. The two predicted indications are effectively one signal.

**To proceed, the following is needed:**
- The FDA package insert (warnings, contraindications, and any risk-management requirements). This is a blocking gap for safety screening.
- Mechanism of action data (for example from DrugBank) to test the speculative retinoid–renin-angiotensin link.
- A systematic literature search for isotretinoin/retinoids and hypertension or renal vascular effects, plus a check of clinical trial registries.
- A route and dosage-form compatibility assessment against the target indication.
- A review of whether the target indication is clinically plausible for an oral retinoid.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

