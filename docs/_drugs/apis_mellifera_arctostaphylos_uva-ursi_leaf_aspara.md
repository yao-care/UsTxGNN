---
layout: default
title: Apis Mellifera Arctostaphylos Uva-Ursi Leaf Aspara
parent: 僅模型預測 (L5)
nav_order: 385
evidence_level: L5
indication_count: 0
---

# Apis Mellifera Arctostaphylos Uva-Ursi Leaf Aspara
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

# Multi-Ingredient Botanical Complex: No Approved Indication — TxGNN Prediction Not Available

## One-Sentence Summary

This candidate is a 15-ingredient heterogeneous formula combining botanical extracts, animal-derived substances, and inorganic salts, with no established approved indication and no DrugBank ID on record.
Because the TxGNN knowledge graph requires a mapped DrugBank node to generate repurposing scores, **no prediction was produced** for this combination.
With zero supporting clinical trials or publications identified through the automated pipeline, this candidate cannot proceed under the current evaluation framework.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not established (no Taiwan approval found) |
| Predicted New Indication | No prediction generated |
| TxGNN Prediction Score | N/A |
| Evidence Level | L5 — Model prediction only; no actual studies identified |
| Taiwan Market Status | Not marketed (未上市) |
| Number of Approvals | 0 |
| Recommended Decision | Hold |

---

## Why No Prediction Was Generated

The TxGNN model maps drugs through their DrugBank identifiers to a biomedical knowledge graph. This candidate is assigned no DrugBank ID, because it is a composite of 15 heterogeneous ingredients rather than a single chemical entity:

| Category | Ingredients |
|----------|------------|
| Botanical extracts | Arctostaphylos uva-ursi leaf, Berberis vulgaris root bark, Chelidonium majus, Juniper berry, Populus tremuloides bark, Rhus aromatica root bark, Rubia tinctorum root, Saw palmetto, Solidago virgaurea flowering top, Taraxacum officinale |
| Vegetable / food-derived | Asparagus |
| Animal-derived | Apis mellifera (bee venom), Lytta vesicatoria (Spanish fly) |
| Inorganic salts | Magnesium chloride, Sodium chloride |

Without a unified drug node in the knowledge graph, TxGNN cannot compute a disease similarity score and no repurposing prediction is generated. Any indication assigned manually would be outside the evidence-based methodology this pipeline is designed to support.

At the ingredient level, several components have individual ethnobotanical or pharmacological precedents in the urological domain — Arctostaphylos uva-ursi and Solidago virgaurea for urinary tract support, Saw palmetto for benign prostatic hyperplasia, Juniper berry and Taraxacum officinale as diuretics — but these are single-ingredient observations and do not constitute a validated mechanistic basis for the combination as a whole.

---

## Safety Considerations

No consolidated safety data was retrievable for this combination formula. Before any further evaluation, the following ingredient-specific hazards require attention:

- **Lytta vesicatoria**: Contains cantharidin, a vesicant with a narrow toxic margin. Even low doses can cause severe mucosal irritation, nephrotoxicity, and haematuria. This is the single greatest safety concern in the formula.
- **Chelidonium majus**: Associated with drug-induced hepatotoxicity in published case reports; the European Medicines Agency has issued cautionary guidance on oral preparations.
- **Berberis vulgaris (berberine)**: Known CYP2D6 and CYP3A4 inhibitor; potential interactions with warfarin, cyclosporin, and other narrow-therapeutic-index drugs.
- **Rubia tinctorum root**: Contains lucidin, classified as a genotoxic carcinogen; oral use is restricted or prohibited in several jurisdictions.

Please review individual component safety profiles and applicable regulatory restrictions before any clinical consideration.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This candidate cannot be evaluated within the TxGNN repurposing framework because no DrugBank ID exists for the combination, yielding no prediction score, no indication mapping, and no evidence linkage. Independently, the presence of cantharidin (Lytta vesicatoria) and a genotoxic constituent (Rubia tinctorum) creates a significant pre-clinical safety burden that must be resolved before any development pathway is considered.

**To proceed, the following is needed:**

- **Reformulate the query at the ingredient level**: Submit individual active components (e.g., berberine from Berberis vulgaris, ursolic acid from Arctostaphylos uva-ursi) as separate TxGNN candidates to generate valid repurposing scores
- **Clarify product intent**: Determine whether this formulation is positioned as a homeopathic preparation, dietary supplement, or pharmaceutical drug — each carries different regulatory and evidence requirements
- **Resolve genotoxicity concern**: Obtain a formal genotoxicity assessment for the Rubia tinctorum and Chelidonium majus components before any clinical use is considered
- **Characterise cantharidin content**: Quantify the Lytta vesicatoria dose and cantharidin concentration; establish a safety margin relative to known toxic thresholds
- **Obtain product monograph or equivalent**: Retrieve the full prescribing information or manufacturer dossier to replace the current data gaps on MOA, approved indications, warnings, and contraindications
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

