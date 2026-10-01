---
layout: default
title: Flurandrenolide
parent: Model Prediction Only (L5)
nav_order: 726
evidence_level: L5
indication_count: 10
---

# Flurandrenolide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Flurandrenolide: From Topical Corticosteroid-Responsive Skin Conditions to Vulvar Inverted Follicular Keratosis

## One-Sentence Summary

Flurandrenolide is a medium-potency topical corticosteroid marketed in the US as tape, cream, and lotion. The supplied data lists no approved-indication text.
The TxGNN model predicts it may be effective for **vulvar inverted follicular keratosis**, but there are currently **0 clinical trials** and **0 publications** supporting this direction. The prediction is model-only (Evidence Level L5).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the supplied US license data (topical corticosteroid class, generally used for inflammatory skin conditions) |
| Predicted New Indication | Vulvar inverted follicular keratosis |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 6 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, flurandrenolide is a topical corticosteroid. Its anti-inflammatory and immunosuppressive effects come from glucocorticoid receptor activity, which is a drug-class property rather than something confirmed in the supplied data.

The mechanistic fit for the predicted indication is weak. Inverted follicular keratosis is a benign epithelial lesion, not primarily an inflammatory skin disease. A corticosteroid is therefore unlikely to act on its underlying cause. The very high TxGNN score (0.997) is a model output only. No trial, publication, or drug-specific mechanistic evidence backs it.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA016455 | CORDRAN (Almirall, LLC) | Tape | Not provided in source data |
| NDA012806 | CORDRAN (INA Pharmaceutics, Inc) | Cream | Not provided in source data |
| ANDA207133 | Flurandrenolide (Bryant Ranch Prepack) | Lotion | Not provided in source data |
| ANDA207133 | Flurandrenolide (Padagis Israel Pharmaceuticals Ltd) | Lotion | Not provided in source data |

The source lists 6 licenses in total, but the records contain only 5 entries. One of them (NDA012806) appears twice, so the table shows it once.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score. There is no clinical or literature evidence, and a corticosteroid has a weak mechanistic rationale for a benign epithelial lesion. Safety and label information are also missing.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (blocking gap)
- Mechanism of action data (for example, from DrugBank)
- Evidence for this specific indication, such as case reports, dermatology literature, or registered trials
- Route and formulation compatibility assessment for vulvar use
- Consider prioritizing other predictions with a more plausible class-level rationale, such as the lichen planus variants and alopecia areata. These also have no drug-specific evidence yet and remain research questions.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

