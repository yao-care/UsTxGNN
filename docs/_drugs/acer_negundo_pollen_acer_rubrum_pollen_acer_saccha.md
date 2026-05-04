---
layout: default
title: Acer Negundo Pollen Acer Rubrum Pollen Acer Saccha
parent: 僅模型預測 (L5)
nav_order: 67
evidence_level: L5
indication_count: 0
---

# Acer Negundo Pollen Acer Rubrum Pollen Acer Saccha
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

# Multi-Allergen Extract Panel: Allergy Immunotherapy — No TxGNN Repurposing Prediction Available

## One-Sentence Summary

This product is a complex multi-component allergen extract panel comprising 55 distinct biological materials (tree pollens, grass pollens, weed pollens, house dust, and botanical extracts), classically used in allergy skin testing and allergen-specific immunotherapy.
The TxGNN model was **unable to generate any repurposing predictions** for this candidate — likely because the multi-ingredient composition cannot be mapped to a single DrugBank node, which is required for graph-based prediction.
As a result, **no clinical trial or publication evidence** supporting a new indication is available from this pipeline run.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Allergy skin testing / Allergen immunotherapy (inferred from component composition) |
| Predicted New Indication | — (No prediction generated) |
| TxGNN Prediction Score | — |
| Evidence Level | L5 — Model prediction only; no actual predictions produced |
| US Market Status | Not marketed (no US licenses found) |
| Number of NDAs | 0 |
| Recommended Decision | **Hold** |

---

## Why No Prediction Was Generated

This candidate presents a fundamental structural incompatibility with the TxGNN pipeline:

**1. Compound composition barrier.** TxGNN's knowledge graph operates on single-entity drug nodes identified by a DrugBank ID. This product contains 55 co-listed active ingredients (allergen extracts from maple, birch, oak, ragweed, timothy grass, house dust, and others). No single DrugBank ID could be assigned (`drugbank_id: null`), preventing graph traversal and disease-link scoring.

**2. Biological nature of components.** The ingredients are biological extracts used to provoke or modulate immune responses in diagnostic and desensitisation settings — not small-molecule drugs with defined target–pathway interactions. The knowledge graph's drug–protein–disease edges are not well-populated for such biological allergen mixtures.

**3. Missing MOA data.** Mechanism of action data is unavailable, further limiting any mechanistic bridging analysis between components and candidate disease nodes.

For these reasons, the pipeline returned zero predicted indications, which is an expected outcome for this type of complex biological product rather than a data collection failure.

---

## US Market Information

No US approvals were found in the queried dataset. This product is recorded as **not marketed** with **0 licenses**.

> Note: Allergen extract panels in the United States are typically regulated under the biologics pathway (BLA) by FDA's Center for Biologics Evaluation and Research (CBER), not as conventional NDAs. A targeted search of CBER-licensed allergen products may yield relevant market data not captured by the current NDA-focused query.

---

## Safety Considerations

Please refer to the package insert for safety information.

> General class considerations for allergen extract products: anaphylaxis risk during skin testing or immunotherapy is a well-recognised class effect. Products containing Histamine Dihydrochloride serve as positive controls in diagnostic panels. Gelsemium sempervirens root and Schoenocaulon officinale seed are botanicals with known toxicity profiles at therapeutic doses and warrant special handling attention.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN pipeline produced no repurposing predictions for this candidate because the multi-allergen extract composition cannot be represented as a single knowledge-graph node. This is a pipeline limitation, not a clinical judgement that the product has no value — allergen immunotherapy is a well-established treatment category.

**To proceed, the following is needed:**

- **Decompose the query**: Re-run TxGNN predictions individually for high-priority single components (e.g., Ambrosia artemisiifolia [ragweed], Phleum pratense [timothy grass], Betula papyrifera [birch]) that have defined DrugBank entries, to assess whether any single allergen has repurposing potential.
- **Clarify clinical intent**: Determine whether the goal is to evaluate this panel as a diagnostic tool, an immunotherapy product, or to identify individual components with novel therapeutic applications.
- **CBER biologics search**: Query FDA's CBER allergen product licence database to identify existing approvals and approved indications for comparable multi-allergen panels.
- **MOA data collection**: Retrieve mechanism data from DrugBank for individual identifiable components.
- **Safety data collection**: Obtain package insert warnings and contraindications from the originating manufacturer or FDA labelling database.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

