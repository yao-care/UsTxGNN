---
layout: default
title: Acer Negundo Pollen Acer Saccharum Pollen Ailanthu
parent: 僅模型預測 (L5)
nav_order: 70
evidence_level: L5
indication_count: 0
---

# Acer Negundo Pollen Acer Saccharum Pollen Ailanthu
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

# Multi-Allergen Pollen Extract Mixture: Evaluation Incomplete — No TxGNN Prediction Available

## One-Sentence Summary

This candidate is a complex multi-allergen immunotherapy mixture comprising 75+ pollen, root, and botanical extracts, classically used in allergen immunotherapy for allergic rhinitis and related hypersensitivity conditions.
However, the TxGNN model was unable to generate any repurposing predictions for this compound — most likely because the mixture has no DrugBank ID and cannot be mapped onto the knowledge graph.
Without a model prediction as the anchor, **this evaluation cannot proceed to evidence assessment**.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Allergic rhinitis / allergen immunotherapy (inferred from drug composition; no regulatory record found) |
| Predicted New Indication | None — TxGNN returned no predictions |
| TxGNN Prediction Score | N/A |
| Evidence Level | N/A (no prediction to evaluate) |
| US Market Status | Not marketed |
| Number of NDAs | 0 |
| Recommended Decision | **Hold** |

---

## Why No Prediction is Available

This drug entry is composed of **75 individual allergen components** — spanning tree pollens (oak, birch, ash, maple), grass pollens (ryegrass, Kentucky bluegrass, oats), weed pollens (ragweed, mugwort, pigweed), and botanical extracts (Echinacea, Goldenseal, Myrrh, Fenugreek Leaf, Phytolacca americana root, Baptisia tinctoria root).

Such multi-component allergen mixtures are not registered as a single entity in DrugBank (`drugbank_id: null`), which means the TxGNN knowledge graph has no node corresponding to this combination. Without a valid DrugBank anchor, the prediction pipeline returns an empty result — this is a **structural data gap**, not a finding of no repurposing potential.

Additionally, this mixture has no Taiwan TFDA or US NDA/BLA regulatory record, and no original indication text is available in structured form. The full data pipeline (TFDA lookup → DDI check → DrugBank enrichment → TxGNN scoring) failed at every layer.

---

## US Market Information

No regulatory authorizations found. This product is not currently registered or marketed in the evaluated regulatory database.

---

## Safety Considerations

Please refer to individual component package inserts for safety information. As a multi-allergen immunotherapy mixture, general cautions for allergen extracts include risk of anaphylaxis, local injection site reactions, and systemic allergic reactions. No structured DDI or contraindication data was retrieved for this combination.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This candidate cannot be evaluated through the standard TxGNN repurposing pipeline because it is a multi-component allergen mixture without a DrugBank ID, which prevents knowledge graph mapping and model scoring. Without a prediction, there is no repurposing hypothesis to assess.

**To proceed, the following is needed:**

- **Disaggregate the components**: Identify whether any single active ingredient (e.g., Echinacea, Goldenseal) has its own DrugBank ID and submit individual candidates for TxGNN scoring.
- **Clarify clinical intent**: Determine whether this mixture is intended as a diagnostic allergen panel, an immunotherapy desensitization product, or a combination botanical supplement — each has a different regulatory and evidence pathway.
- **Obtain DrugBank mapping**: If the goal is to evaluate the allergen immunotherapy class broadly, query DrugBank for individual allergen components separately.
- **Supplement regulatory record**: Confirm whether any single-component products derived from this mixture hold NDA/BLA approvals (e.g., standardized grass pollen extracts).
- **Re-submit as single-ingredient candidates**: Once individual components are mapped, re-run the TxGNN pipeline per component to generate repurposing predictions.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

