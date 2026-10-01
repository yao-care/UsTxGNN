---
layout: default
title: Benzoyl Peroxide
parent: Model Prediction Only (L5)
nav_order: 450
evidence_level: L5
indication_count: 4
---

# Benzoyl Peroxide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

# Benzoyl Peroxide: From Acne to Vulvar Inverted Follicular Keratosis

## One-Sentence Summary

Benzoyl peroxide is a topical agent sold in the US mainly as an over-the-counter acne treatment. The approved indication text is blank in the data, so acne is inferred from product names.
The TxGNN model predicts it may be effective for **vulvar inverted follicular keratosis**, but this is a model prediction only, with **0 clinical trials** and **0 publications** supporting it.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acne (inferred from product names; no approved indication text in the data) |
| Predicted New Indication | Vulvar inverted follicular keratosis |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 (listed under authorization number M006) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Benzoyl peroxide is a topical keratolytic and antibacterial agent with established use in acne, and mechanistically it might apply to follicular skin conditions. However, no mechanistic link to vulvar inverted follicular keratosis is supported by the data provided.

Vulvar inverted follicular keratosis is a benign follicular lesion. The score of 0.999 is a model output, not clinical evidence. It ranks 2,736th among all model predictions, and no trials or publications were retrieved to back it.

The other predicted indications for this drug are also weak. Two have no plausible mechanism (2-hydroxyethyl methacrylate sensitization and acrodermatitis chronica atrophicans). Acne keloid has only indirect support and may partly reflect overlap with the existing acne use.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| M006 | Neutrogena On-the-Spot Acne Treatment (Kenvue Brands LLC) | Cream | Acne treatment (per product name) |
| M006 | Acne Med 5% (Face Reality, LLC) | Gel | Acne treatment (per product name) |
| M006 | Acne Treatment (CVS Pharmacy, Inc.) | Gel | Acne treatment (per product name) |
| M006 | 24 Hour Acne Serum (Drmtlgy, LLC) | Gel | Acne treatment (per product name) |
| M006 | Acne Cleanser (Meijer, Inc.) | Cream | Acne treatment (per product name) |

Other marketed forms in the data include liquid, soap, suspension, and lotion.

## Safety Considerations

- **Contact sensitization signal**: One of the model's other predictions is 2-hydroxyethyl methacrylate sensitization. Benzoyl peroxide is itself a known contact sensitizer. This signal should be read as a possible adverse-reaction concern, not as a treatment opportunity.
- Package insert warnings, contraindications, and interaction data were not available in the data provided. Please refer to the package insert for safety information.
- Any use on vulvar skin would need a specific mucosal and irritation assessment, which has not been evaluated.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model output alone (L5), with no trials, no literature, and no supported mechanism. The safety data are missing, which blocks progression past the initial screening stage.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (blocking data gap)
- Mechanism of action data for benzoyl peroxide
- A targeted literature search for vulvar inverted follicular keratosis and related follicular lesions
- Clinical expert review of whether a treatment rationale exists, and of local tolerability on vulvar skin
- Approved indication text for the listed products, to confirm the original indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

