---
layout: default
title: Acacia Dealbata Pollen Acer Negundo Pollen Acer Sa
parent: 僅模型預測 (L5)
nav_order: 56
evidence_level: L5
indication_count: 0
---

# Acacia Dealbata Pollen Acer Negundo Pollen Acer Sa
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

# Multi-Allergen Extract (85 Components): Repurposing Assessment Not Available

## One-Sentence Summary

This entry is a complex mixture of 85 plant-derived allergen components — primarily aeroallergen pollens plus several botanical extracts — most likely formulated as an allergen immunotherapy or allergy skin-testing preparation.
The TxGNN model returned **no predicted indications**, because the multi-component nature of this product prevented a DrugBank node match and therefore blocked knowledge-graph traversal entirely.
This candidate requires **data remediation and pipeline reclassification** before any repurposing assessment can proceed.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available |
| Predicted New Indication | None — no TxGNN predictions generated |
| TxGNN Prediction Score | N/A |
| Evidence Level | L5 — insufficient for assessment |
| US Market Status | Not marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why No Prediction Was Generated

TxGNN operates by traversing a biomedical knowledge graph in which every drug is anchored to a **single DrugBank node**. This product consists of **85 distinct plant-derived components** — no unified DrugBank ID could be assigned, so the model had no starting node and produced zero predictions.

The 85 components fall into two broad categories:

**Aeroallergen pollens (~75 components)**
Tree pollens (Acacia, Acer/maple, Betula/birch, Carya/hickory, Fraxinus/ash, Juglans/walnut, Juniperus/cedar, Liquidambar, Morus/mulberry, Olea/olive, Pinus/pine, Platanus/sycamore, Populus/cottonwood, Quercus/oak, Salix/willow, Taxodium, Ulmus/elm, and others), grass pollens (Anthoxanthum, Avena, Distichlis, Holcus, Paspalum, Poa/bluegrass, Secale/rye, Sorghum, Triticum/wheat, Zea/corn), and weed pollens (Ambrosia/ragweed species ×7, Amaranthus ×4, Artemisia/sagebrush, Atriplex, Bassia, Chenopodium, Cyclachaena, Eupatorium, Plantago/plantain, Rumex, Salsola/Russian thistle, Solidago/goldenrod, Urtica/nettle, Xanthium).

**Botanical/herbal extracts (~10 components)**
Baptisia tinctoria root, Echinacea angustifolia root, Phytolacca americana root, Goldenseal, Myrrh, Nasturtium officinale, Urtica urens (whole plant), Broussonetia papyrifera pollen, Melaleuca quinquenervia pollen, Schinus molle pollen.

Products of this composition are typically used for **subcutaneous allergen immunotherapy** (allergy desensitization injections) or **allergy skin-prick testing** — a regulated biological product category that is architecturally incompatible with small-molecule repurposing pipelines like TxGNN.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This candidate cannot be evaluated through the TxGNN repurposing pipeline because it is a multi-component allergen biological rather than a discrete drug entity; the absence of a DrugBank node means zero predictions were generated, leaving no basis for an evidence-based repurposing assessment.

**To proceed, the following is needed:**

- **Candidate reclassification**: Determine whether this product should be **excluded from the TxGNN pipeline** entirely, or decomposed so that individual pharmacologically active components (e.g., Echinacea angustifolia, Goldenseal/Hydrastis canadensis, Phytolacca americana) are each analyzed as separate candidates with their own DrugBank IDs
- **Pipeline exclusion filter**: Add upstream logic to detect entries with semicolon-delimited multi-component INNs (as seen in `candidate_id: TW-UNKNOWN-multi`) and route them to a separate triage workflow before evidence pack generation
- **Original indication documentation**: Confirm the intended product use (allergen immunotherapy vs. allergy diagnostic testing vs. herbal combination supplement) from the manufacturer's package insert or regulatory filing
- **Individual component evaluation**: Botanicals with established DrugBank entries — such as Echinacea and Goldenseal — may be viable repurposing candidates when assessed independently; consider splitting these into separate candidate records
- **Data gap resolution (DG001, DG002)**: Package insert warnings and MOA data cannot be retrieved until product identity is clarified; both remain blocking until reclassification is complete
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

