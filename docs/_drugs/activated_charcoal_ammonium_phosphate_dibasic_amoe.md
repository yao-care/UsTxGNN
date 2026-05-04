---
layout: default
title: Activated Charcoal Ammonium Phosphate Dibasic Amoe
parent: 僅模型預測 (L5)
nav_order: 176
evidence_level: L5
indication_count: 0
---

# Activated Charcoal Ammonium Phosphate Dibasic Amoe
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

# Multi-Component Herbal/Homeopathic Combination: Insufficient Data for TxGNN Evaluation

## One-Sentence Summary

This submission contains a complex eight-component combination (Activated Charcoal, Ammonium Phosphate Dibasic, Amoeba Proteus, Arsenic Trioxide, Cinchona Officinalis Bark, Garlic, Veratrum Album Root, and Wormwood) with no approved indications on record.
The TxGNN model returned **no predicted new indications** for this combination, as it could not be matched to a single DrugBank entity.
Without a valid prediction score or supporting evidence, no repurposing pathway can be assessed at this time.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | None on record |
| Predicted New Indication | None (TxGNN returned no predictions) |
| TxGNN Prediction Score | N/A |
| Evidence Level | L5 — model prediction only, but no prediction was generated |
| US Market Status | Not marketed |
| Number of NDAs | 0 |
| Recommended Decision | **Hold** |

---

## Why No Prediction Was Generated

The TxGNN model operates on single, well-defined DrugBank entities. This submission lists **eight distinct active ingredients** under a single query string, including:

- **Activated Charcoal** — a non-specific GI adsorbent used in poisoning management
- **Arsenic Trioxide** — a known antineoplastic agent (APL treatment)
- **Cinchona Officinalis Bark** — the botanical source of quinine (antimalarial)
- **Wormwood** — the botanical source of artemisinin (antimalarial)
- **Veratrum Album Root / Amoeba Proteus** — classical homeopathic ingredients with no established pharmacological mechanism
- **Garlic / Ammonium Phosphate, Dibasic** — nutritional/mineral supplement components

Because no unified DrugBank ID exists for this combination, the TxGNN knowledge graph could not identify a node to generate repurposing candidates. The combination profile suggests a **homeopathic or alternative remedy preparation** rather than a conventional pharmaceutical entity.

---

## US Market Information

No FDA/NDA authorizations are on record for this combination. The product is currently **not marketed**.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** Arsenic trioxide (one component of this combination) carries well-documented Black Box Warnings including QT prolongation, APL differentiation syndrome, and hepatotoxicity. If this combination is to be further evaluated, the arsenic trioxide component must be assessed against standard oncology safety protocols regardless of formulation context.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN pipeline could not process this multi-ingredient string as a single drug entity, resulting in zero predictions and zero evidence. Without a defined pharmacological target or DrugBank mapping, repurposing evaluation cannot proceed.

**To proceed, the following is needed:**

- Clarify whether this is a **fixed-dose combination product** with a single regulatory submission, or a list of individual components requiring separate analysis.
- If a specific active ingredient (e.g., Arsenic Trioxide, Artemisinin from Wormwood, or Quinine from Cinchona) is the intended repurposing candidate, **resubmit that single INN** to the TxGNN pipeline to obtain a valid prediction score.
- Obtain a DrugBank ID for the lead compound before re-running the evidence collection workflow.
- If this is a **homeopathic product**, note that TxGNN is not designed for homeopathic formulations; standard repurposing methodology does not apply.
- Retrieve product package insert (if any) to document safety data for Arsenic Trioxide component.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

