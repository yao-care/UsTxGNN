---
layout: default
title: Antipyrine Apis Mellifera Calendula Officinalis Fl
parent: 僅模型預測 (L5)
nav_order: 335
evidence_level: L5
indication_count: 0
---

# Antipyrine Apis Mellifera Calendula Officinalis Fl
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

# Multi-Ingredient Homeopathic Complex (16 Components): Insufficient Data for Drug Repurposing Evaluation

## One-Sentence Summary

This product is a 16-ingredient homeopathic complex formula comprising Antipyrine, Apis mellifera, Calendula officinalis, Copaifera officinalis resin, Croton tiglium seed, Daphne mezereum bark, Delphinium staphisagria seed, Graphite, Histamine dihydrochloride, Kerosene, Lytta vesicatoria, Rhododendron tomentosum, Sodium chloride, Sulfur, Toxicodendron vernix, and Urtica urens.
The TxGNN model returned **no predicted new indications** for this compound, likely due to missing DrugBank ID and unmapped multi-component structure.
This product is currently **not marketed** in the US, and **no supporting evidence** (clinical trials or publications) was identified — evaluation cannot proceed without additional data.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not documented |
| Predicted New Indication | None (TxGNN returned no predictions) |
| TxGNN Prediction Score | N/A |
| Evidence Level | Not evaluable |
| US Market Status | Not marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available, and no DrugBank ID has been assigned to this formulation. The product is a multi-ingredient homeopathic complex — a class of formulations that does not map cleanly to TxGNN's drug node structure, which is anchored to individual DrugBank-registered chemical entities.

Based on the ingredient profile, several components are classical homeopathic constituents used traditionally for musculoskeletal pain, inflammatory conditions, and skin disorders (e.g., Apis mellifera for edema/stings, Urtica urens for burns/urticaria, Lytta vesicatoria for vesicant irritation, Calendula officinalis for wound healing). Antipyrine is the sole conventional pharmacological agent in the list, historically used as an analgesic and antipyretic.

Because TxGNN operates at the level of individual drug nodes mapped to DrugBank identifiers, a 16-ingredient mixture without a consolidated DrugBank ID cannot be evaluated as a single repurposing candidate. Each component would need to be assessed individually, or the formulation would need to be registered as a single entity before a meaningful prediction score can be generated.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

This product has no NDA or regulatory approval on record. It is not marketed in the US.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note on specific ingredient risks:** Although formal safety data is unavailable in this dataset, several raw ingredients in this formulation carry intrinsic toxicity concerns at pharmacological doses:
> - **Croton tiglium seed**: potent phorbol ester irritant; vesicant
> - **Daphne mezereum bark**: daphnetoxin content; potentially toxic if ingested in non-homeopathic quantities
> - **Lytta vesicatoria**: contains cantharidin; nephrotoxic and vesicant
> - **Toxicodendron vernix**: urushiol-containing; strong contact allergen
>
> At standard homeopathic dilutions (e.g., 6C, 30C), these risks are substantially attenuated. However, product-specific dilution information is not available in this dataset. A full prescribing information review is required before any clinical use assessment.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
TxGNN produced no repurposing predictions for this compound because the multi-ingredient homeopathic formulation lacks a DrugBank ID and does not correspond to any single drug node in the knowledge graph. Without a mapped drug entity, neither prediction scoring nor evidence retrieval is possible under the current pipeline architecture.

**To proceed, the following is needed:**

- **Determine regulatory identity**: Confirm whether this formulation corresponds to any marketed product (e.g., under a brand name) with an existing NDA or homeopathic OTC monograph registration in the US or EU.
- **Assign component-level DrugBank IDs**: For the pharmacologically active components (particularly Antipyrine, Histamine dihydrochloride), retrieve individual DrugBank IDs and run TxGNN predictions per component.
- **Obtain product-specific dilution information**: Without knowing the homeopathic dilution levels, safety and pharmacological relevance cannot be assessed.
- **Retrieve package insert / prescribing information**: Resolve Data Gaps DG001 (warnings/contraindications) and DG002 (MOA) to enable S1 safety screening.
- **Clarify intended indication**: If this formulation was submitted with a target indication in mind, that context should be provided to focus the repurposing analysis.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

