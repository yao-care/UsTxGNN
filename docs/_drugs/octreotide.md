---
layout: default
title: Octreotide
parent: Model Prediction Only (L5)
nav_order: 982
evidence_level: L5
indication_count: 2
---

# Octreotide
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

# Octreotide: From an Established Somatostatin Analogue to Vulvar Inverted Follicular Keratosis

## One-Sentence Summary

Octreotide is a somatostatin analogue that is marketed in the United States, mainly as injectable products.
The TxGNN model predicts it may be effective for **vulvar inverted follicular keratosis**, but there are currently **0 clinical trials** and **0 publications** supporting this direction.
This is a model-only prediction, and the mechanistic rationale is weak.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Vulvar inverted follicular keratosis |
| TxGNN Prediction Score | 99.58% |
| Evidence Level | L5 (model prediction only) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Octreotide acts mainly on somatostatin receptors SSTR2 and SSTR5, producing antisecretory and antiproliferative effects. Detailed mechanism-of-action data and original indication text are not available in the supplied data.

The data do not support a mechanism linking somatostatin receptor signaling to a benign follicular keratinocyte lesion. The high score (99.58%) may reflect knowledge-graph proximity to related skin-lesion nodes rather than a biological rationale. Inverted follicular keratosis is a benign lesion usually managed by excision, so the need for a systemic peptide is also questionable.

The second-ranked prediction, **seborrheic keratosis** (score 99.55%), has the same weaknesses. It is typically driven by FGFR3/PIK3CA somatic mutations and has effective local treatments. Any link, such as SSTR expression in skin or IGF-1 axis suppression, would be speculative. It is likely a knowledge-graph artifact, and a systemic injectable peptide has an unfavorable benefit-risk profile for a common benign condition. It also has no clinical trials or literature.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

The 20 authorizations include generic (ANDA) and brand (NDA) products. The main ones are:

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA076330 | Octreotide Acetate | Injection, solution | Hikma Pharmaceuticals USA Inc. |
| ANDA090834 | Octreotide Acetate | Injection, solution | Sagent Pharmaceuticals |
| NDA213224 | BYNFEZIA Pen | Injection | Sun Pharmaceutical Industries, Inc. |
| ANDA216839 | Octreotide Acetate | Injection, solution | Glenmark Pharmaceuticals Inc., USA |
| ANDA216807 | Octreotide Acetate | Injection, solution | Gland Pharma Limited |

Available dosage forms are injection (solution) and a delayed-release oral capsule. Approved indication text is not included in the supplied data.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on the TxGNN score alone, with no clinical trials, no literature, and no supported mechanism. The target conditions are benign and have effective local treatments, so a systemic injectable peptide is hard to justify.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism-of-action data (for example, from DrugBank) and the approved indication text
- Preclinical or observational evidence of somatostatin receptor involvement in the target lesion
- A route-compatibility assessment, since systemic injection versus topical or local delivery is unresolved
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

