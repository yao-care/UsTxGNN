---
layout: default
title: Anamirta Cocculus Seed Gelsemium Sempervirens Root
parent: 僅模型預測 (L5)
nav_order: 340
evidence_level: L5
indication_count: 0
---

# Anamirta Cocculus Seed Gelsemium Sempervirens Root
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

# Multi-Component Homeopathic Combination: Insufficient Data for Repurposing Analysis

## One-Sentence Summary

This submission contains a multi-ingredient botanical/homeopathic combination (Anamirta cocculus seed, Gelsemium sempervirens root, Sodium borate, Tobacco leaf, Toxicodendron pubescens leaf, Wood creosote) with no approved indications on record and no US market presence.
The TxGNN pipeline returned **no predicted new indications** for this combination, as the compound has no DrugBank ID mapping and no original indication to anchor the repurposing model.
**No evidence-based repurposing assessment can be completed** at this time.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | None on record |
| Predicted New Indication | None (TxGNN returned no candidates) |
| TxGNN Prediction Score | N/A |
| Evidence Level | L5 — Model prediction only, but no candidates generated |
| US Market Status | Not marketed |
| Number of NDAs | 0 |
| Recommended Decision | **Hold** |

---

## Why No Prediction Was Generated

This combination product could not be processed by the TxGNN repurposing pipeline for three structural reasons:

**1. No DrugBank ID.** The TxGNN knowledge graph anchors drug nodes via DrugBank IDs. This combination has no assigned DrugBank ID, so no node exists in the graph from which disease edges can be predicted.

**2. Multi-component botanical formulation.** The six ingredients (Anamirta cocculus seed, Gelsemium sempervirens root, Sodium borate, Tobacco leaf, Toxicodendron pubescens leaf, Wood creosote) are characteristic of a homeopathic combination product. Homeopathic formulations are typically prepared at high dilutions and are not represented as individual chemical entities in pharmacological databases used by TxGNN.

**3. No original indication anchor.** The repurposing model uses the original approved indication as a biological reference point. With zero approved indications in the regulatory database, the similarity-based propagation across the knowledge graph cannot be initialised.

---

## US Market Information

No authorisations found. This product is not registered in the US database queried.

---

## Safety Considerations

Please refer to the package insert for safety information.

> No drug interaction data, key warnings, or contraindications were retrieved for this combination. All safety fields returned no data during the 2026-03-24 query run.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN pipeline produced zero repurposing candidates because this multi-ingredient homeopathic combination lacks the foundational data (DrugBank ID, approved indication, mechanistic profile) required for knowledge-graph traversal. Proceeding without these inputs would produce outputs with no scientific validity.

**To proceed, the following is needed:**

- **Clarify product identity**: Determine whether this is a registered homeopathic product (e.g., an OTC homeopathic remedy) and obtain the corresponding NDC or product code, which may enable a different lookup path.
- **DrugBank mapping**: Query each of the six individual botanical ingredients separately in DrugBank (e.g., Gelsemium sempervirens alkaloids such as gelsemine; picrotoxin from Anamirta cocculus) to obtain individual DrugBank IDs for component-level analysis.
- **Define primary active ingredient**: If the product has a dominant pharmacologically active component, run a single-ingredient TxGNN query on that component to generate a candidate list.
- **Identify original therapeutic use**: Locate any labelling, traditional use documentation, or homeopathic monograph to establish an indication anchor for model initialisation.
- **Regulatory clarification**: Confirm whether this product falls under homeopathic drug regulations (FDA CPG 400.400 or equivalent), as this affects which evidence standards apply.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

