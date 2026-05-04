---
layout: default
title: 2-Butoxyethyl Laurate Chelidonium Majus Whole Gels
parent: 僅模型預測 (L5)
nav_order: 18
evidence_level: L5
indication_count: 0
---

# 2-Butoxyethyl Laurate Chelidonium Majus Whole Gels
{: .fs-9 }

證據等級: **L5** | 預測適應症: **0** 個
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

# Multi-Component Homeopathic Mixture: Insufficient Data for Repurposing Evaluation

## One-Sentence Summary

This candidate consists of a seven-ingredient combination — including botanical/homeopathic components (Chelidonium majus, Gelsemium sempervirens, Strychnos nux-vomica, Sulfur) and excipients (2-Butoxyethyl laurate, Glycerin, Sodium carbonate) — with no registered market authorization in the United States.
The TxGNN model returned **no predicted indications** for this candidate, and **no clinical trials or literature** have been identified.
Due to the absence of a unified DrugBank ID, mechanism-of-action data, and regulatory history, this candidate cannot proceed through standard repurposing evaluation at this time.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | None on record |
| Predicted New Indication | None (TxGNN returned no predictions) |
| TxGNN Prediction Score | N/A |
| Evidence Level | L5 (model prediction only) → effectively below L5: no prediction generated |
| US Market Status | ✗ Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

No TxGNN prediction is available for this candidate, so a mechanism-based repurposing rationale cannot be constructed.

The ingredient list suggests a **homeopathic or naturopathic combination product**. Key components include:

- **Chelidonium majus** (greater celandine): traditionally used in European herbal medicine for hepatobiliary complaints and wart treatment
- **Gelsemium sempervirens** (yellow jasmine): used in classical homeopathy for flu-like neurological symptoms, anxiety, and headache
- **Strychnos nux-vomica** (nux vomica): a homeopathic staple for digestive hypersensitivity, irritability, and hangover-like states; contains strychnine alkaloids at pharmacologically sub-threshold homeopathic dilutions
- **Sulfur**: a classical homeopathic "polychrest" associated with skin and metabolic presentations
- **2-Butoxyethyl laurate, Glycerin, Sodium carbonate**: excipients or formulation aids

Because the product is a multi-ingredient mixture without a single active pharmaceutical ingredient (API) traceable to DrugBank, the TxGNN knowledge graph — which operates on individual drug nodes — was unable to generate a repurposing score. This is a structural limitation of the model for combination homeopathic products, not a data quality failure per se.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for this combination.

---

## Literature Evidence

Currently no related literature available for this specific combination.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note on Strychnos nux-vomica**: At conventional (non-homeopathic) doses, nux vomica contains strychnine, which is a potent glycine-receptor antagonist with a narrow therapeutic index. If this product is intended for administration at pharmacologically active concentrations, a dedicated strychnine toxicity review is required before any clinical use.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model produced no repurposing predictions for this multi-ingredient homeopathic mixture, and there is no US market authorization, no identifiable DrugBank node, and no supporting clinical or preclinical literature. The candidate cannot be evaluated under the standard repurposing framework without foundational data.

**To proceed, the following is needed:**

- **Identify the active entity**: Determine which single ingredient (if any) is the pharmacologically active component and retrieve its DrugBank ID; only then can TxGNN generate a meaningful repurposing score
- **Obtain regulatory history**: Check TFDA, EMA, or any regional authority for prior approvals of this or a closely related formulation
- **Clarify intended concentration**: For nux vomica and gelsemium, confirm whether the formulation uses homeopathic dilutions (e.g., 6C, 30C) or pharmacologically active concentrations — this is prerequisite for any safety review
- **Collect MOA data**: Query DrugBank and primary literature for each individual ingredient separately
- **Reassess TxGNN eligibility**: If a single dominant API can be identified, re-run the TxGNN pipeline under that drug node
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

