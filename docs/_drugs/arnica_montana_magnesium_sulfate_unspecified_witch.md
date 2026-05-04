---
layout: default
title: Arnica Montana Magnesium Sulfate Unspecified Witch
parent: 僅模型預測 (L5)
nav_order: 361
evidence_level: L5
indication_count: 0
---

# Arnica Montana Magnesium Sulfate Unspecified Witch
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

# Arnica Montana / Magnesium Sulfate / Witch Hazel: Drug Repurposing Evaluation Report

## One-Sentence Summary

This submission covers a three-component combination product — Arnica Montana, Magnesium Sulfate (Unspecified), and Witch Hazel — typically used as a topical preparation for minor musculoskeletal complaints and skin irritation.
The TxGNN model was **unable to generate repurposing predictions** for this candidate, as no DrugBank ID could be resolved and no approved indications are on record in the US market.
Without an anchor compound or mapped indication, a meaningful evidence-level assessment cannot be performed at this time.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No approved indication on record |
| Predicted New Indication | No prediction available |
| TxGNN Prediction Score | N/A |
| Evidence Level | L5 – Model prediction not generated |
| US Market Status | Not marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why No Prediction Was Generated

The TxGNN knowledge graph operates by linking a compound's DrugBank ID to disease nodes in a biomedical knowledge graph. Three issues prevent prediction for this submission:

**1. Multi-component botanical combination.** The submitted string "ARNICA MONTANA; MAGNESIUM SULFATE, UNSPECIFIED; WITCH HAZEL" represents three distinct substances — a plant extract, an inorganic salt, and a tannin-rich astringent. TxGNN is designed for single-compound queries; multi-ingredient strings without a resolved common INN cannot be mapped to a single knowledge-graph node.

**2. No DrugBank ID resolved.** The DrugBank query returned one result but could not assign a DrugBank ID (`null`). Without this anchor, neither KG-based nor deep-learning-based prediction can proceed.

**3. No approved indication to anchor.** Because `original_indications` is empty, the model has no seed indication from which to compute similarity to other disease nodes.

> **What is this combination typically used for?**
> In over-the-counter and compounded topical formulations, this combination is historically applied for:
> - Bruising and minor blunt trauma (Arnica Montana — anti-inflammatory flavonoids)
> - Muscle soreness and minor sprains (Magnesium Sulfate — osmotic, muscle-relaxant effect when absorbed transdermally)
> - Minor skin irritation and hemorrhoids (Witch Hazel — astringent tannins, vasoconstriction)
>
> None of these uses have resulted in a formal FDA NDA/OTC monograph registration under this combined string.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for this combination under the submitted name.

---

## Literature Evidence

Currently no related literature available via automated query for this exact combination string.

---

## Safety Considerations

No DDI interactions were identified in the database query. Formal warning and contraindication data is not available via automated pipeline for this candidate.

Please refer to the individual component package inserts for safety information:
- **Arnica Montana**: Not for use on broken skin; oral ingestion toxic; avoid in allergy to Asteraceae family.
- **Magnesium Sulfate**: Systemic risk (hypermagnesemia) in renal impairment if applied to large wound surfaces.
- **Witch Hazel**: Generally well-tolerated topically; contains trace ethanol in most preparations.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
TxGNN cannot produce a repurposing prediction without a resolvable single-compound DrugBank ID and a mapped indication. This submission does not meet the minimum data requirements for pipeline processing.

**To proceed, the following is needed:**

- **Decompose the submission** — Resubmit each component (Arnica Montana, Magnesium Sulfate, Witch Hazel) as separate single-compound queries to allow individual TxGNN scoring.
- **Resolve DrugBank IDs** — Arnica Montana maps to DrugBank DB13104; Magnesium Sulfate to DB00653; Witch Hazel (Hamamelis virginiana) to DB13690. These should be used as query anchors.
- **Define a target indication** — If a specific repurposing direction (e.g., wound healing, post-surgical ecchymosis) is of clinical interest, provide it as a seed indication to direct the search.
- **Confirm regulatory scope** — Clarify whether the goal is a topical OTC product, a compounded formulation, or a novel systemic application; this determines which regulatory pathway applies.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

