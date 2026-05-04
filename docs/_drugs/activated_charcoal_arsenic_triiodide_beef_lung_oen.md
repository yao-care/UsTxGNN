---
layout: default
title: Activated Charcoal Arsenic Triiodide Beef Lung Oen
parent: 僅模型預測 (L5)
nav_order: 207
evidence_level: L5
indication_count: 0
---

# Activated Charcoal Arsenic Triiodide Beef Lung Oen
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

# Activated Charcoal / Arsenic Triiodide / 7-Herb-Mineral Combination (9-Component Preparation): No Repurposing Predictions Available

## One-Sentence Summary

This evidence pack covers a 9-ingredient preparation combining activated charcoal, arsenic triiodide, beef lung, three herbal components (Oenanthe aquatica fruit, Teucrium scorodonia flowering top), and three mineral/excipient components (silicon dioxide, sulfur, tin, tribasic calcium), with no documented approved indication in any reviewed regulatory database.
The TxGNN model returned **no predicted new indications** for this preparation, and **no clinical trials or publications** were identified.
This evaluation cannot proceed further until foundational data gaps are resolved.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | None documented |
| Predicted New Indication | None |
| TxGNN Prediction Score | N/A |
| Evidence Level | L5 — no actual studies; model prediction unavailable |
| US Market Status | Not marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence pack contains no predicted indications, no regulatory approval, no mechanism of action data, and no supporting clinical or preclinical literature — making any repurposing evaluation impossible at this stage.

**To proceed, the following is needed:**

- **Resolve DG001 (Blocking):** Retrieve the product's package insert (仿單) from the TFDA website to establish approved indication, warnings, and contraindications — this is a prerequisite before any safety screening can begin.
- **Resolve DG002 (High):** Query DrugBank for the mechanism of action of each active ingredient, especially arsenic triiodide (note: distinguish from the FDA-approved arsenic trioxide / Trisenox), to determine whether TxGNN can generate a meaningful repurposing signal.
- **Clarify preparation type:** The combination of herbal, mineral, and biological components (beef lung) is characteristic of a homeopathic or traditional formulation. Confirm whether standard evidence-based drug repurposing methodology applies, or whether an alternative evaluation framework is required.
- **Re-run TxGNN pipeline:** Once each active ingredient has a confirmed DrugBank ID and INN, run predictions per ingredient separately. Multi-ingredient mixtures without a single DrugBank ID cannot be processed as a unit by TxGNN.
- **Re-generate Evidence Pack (v5):** After the above steps, regenerate this report with complete inputs.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

