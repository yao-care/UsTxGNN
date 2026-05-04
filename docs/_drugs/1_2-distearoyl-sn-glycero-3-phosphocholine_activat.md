---
layout: default
title: 1 2-Distearoyl-Sn-Glycero-3-Phosphocholine Activat
parent: 僅模型預測 (L5)
nav_order: 11
evidence_level: L5
indication_count: 0
---

# 1 2-Distearoyl-Sn-Glycero-3-Phosphocholine Activat
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

# Multi-Ingredient Complex (13 Components): No Original Indication — No Predicted New Indication

## One-Sentence Summary

This candidate is a 13-component mixture whose ingredients span activated charcoal, classical homeopathic botanicals (Gelsemium sempervirens, Sepia officinalis, Staphisagria), mineral salts, and a phospholipid carrier (DSPC). It is **not marketed in any jurisdiction covered by this system**, carries no DrugBank ID, and the TxGNN pipeline returned **zero predicted indications** — meaning no repurposing signal could be generated. This record cannot proceed to standard evaluation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | None on record |
| Predicted New Indication | None — TxGNN returned no output |
| TxGNN Prediction Score | N/A |
| Evidence Level | L5 (model prediction only) — but no prediction was produced |
| US Market Status | Not marketed |
| Number of NDAs | 0 |
| Recommended Decision | **Hold** |

---

## Why No Prediction Was Generated

The TxGNN model requires a **single active pharmaceutical ingredient (INN)** that can be mapped to a DrugBank node within the knowledge graph. This submission provided a 13-ingredient string as a single INN:

> 1,2-DISTEAROYL-SN-GLYCERO-3-PHOSPHOCHOLINE; ACTIVATED CHARCOAL; CICHORIUM INTYBUS FLOWER; CINCHONA BARK; DELPHINIUM STAPHISAGRIA SEED; FERROSOFERRIC PHOSPHATE; GELSEMIUM SEMPERVIRENS ROOT; PHOSPHORIC ACID; POTASSIUM PHOSPHATE, UNSPECIFIED FORM; ROSA CANINA FLOWER; SEPIA OFFICINALIS JUICE; SODIUM CHLORIDE; VITIS VINIFERA FLOWERING TOP

Because DrugBank lookup returned no matching entity (`drugbank_id: null`), the KG and DL prediction pipelines had no graph node to start from. The result is a structurally empty Evidence Pack — **no indications, no safety data, no MOA, no clinical trials, no literature**.

From the ingredient profile, this appears to be a **homeopathic or complementary-medicine multi-component preparation**. Several components (Gelsemium sempervirens, Sepia officinalis, Staphisagria, Cinchona bark) are classical homeopathic materia medica with no conventional pharmacological MOA recognized in standard drug databases.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The pipeline cannot evaluate a multi-ingredient string as a single drug entity; no DrugBank mapping, no TxGNN prediction, and no safety data exist for this submission.

**To proceed, the following is needed:**

- **Decompose the mixture**: Submit each of the 13 components individually as separate INN queries. Each ingredient that has a DrugBank ID can then be processed through the TxGNN pipeline independently.
- **Clarify the product type**: Confirm whether this is a registered homeopathic product, a nutraceutical, or a combination drug — the applicable regulatory and evidence framework differs significantly.
- **Obtain product dossier**: If a specific branded product exists, locate its package insert to establish the claimed indication, dosage, and safety warnings before attempting any repurposing analysis.
- **Prioritize pharmacologically active components**: Among the 13, Cinchona bark (source of quinine/quinidine) and DSPC (phospholipid carrier) have conventional pharmacological profiles and would be the most tractable candidates for TxGNN analysis.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

