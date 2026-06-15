---
layout: default
title: Arnica Montana Root Matricaria Recutita Tribasic C
parent: 僅模型預測 (L5)
nav_order: 408
evidence_level: L5
indication_count: 0
---

# Arnica Montana Root Matricaria Recutita Tribasic C
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

# ARNICA MONTANA ROOT / MATRICARIA RECUTITA / TRIBASIC CALCIUM: Insufficient Data for Repurposing Assessment

## One-Sentence Summary

This evidence pack covers a multi-ingredient combination of botanical and mineral components (Arnica montana root, Matricaria recutita, and tribasic calcium). No predicted new indications were returned by the TxGNN model, and the combination is not currently registered in Taiwan. Meaningful drug repurposing analysis cannot be completed without additional regulatory, mechanistic, and clinical data.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No approved indication on record |
| Predicted New Indication | None returned by TxGNN |
| TxGNN Prediction Score | N/A |
| Evidence Level | Below L5 — no model output, no clinical studies |
| Taiwan Market Status | Not marketed (未上市) |
| Number of Licenses | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

No TxGNN prediction was generated for this combination, so there is no candidate indication to evaluate.

This combination consists of three distinct components: *Arnica montana* root (a traditional anti-inflammatory herb), *Matricaria recutita* (chamomile, with known mild anti-inflammatory and spasmolytic properties), and tribasic calcium (a calcium salt used as a supplement or excipient). The mixture does not correspond to a single registered drug entity in standard pharmacological databases, and no DrugBank ID was found.

Without a DrugBank node in the knowledge graph, TxGNN cannot perform link prediction, which explains the empty `predicted_indications` output. Before any repurposing analysis can proceed, the combination must be decomposed into individual active ingredients and each mapped independently to DrugBank identifiers.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for this combination as a unified entity.

---

## Literature Evidence

Currently no related literature available for this combination under TxGNN evidence collection.

---

## Taiwan Market Information

This product has no registered licenses in Taiwan. No authorization records available.

---

## Safety Considerations

Please refer to the package insert for safety information. No DDI records were found in the interaction database, and no regulatory warnings or contraindications are available for this combination under the current query.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN pipeline returned no prediction output because the combination could not be mapped to a knowledge graph node. There is no repurposing candidate to evaluate at this stage.

**To proceed, the following is needed:**

- **Decompose the combination**: Assess each active ingredient individually — query DrugBank separately for *Arnica montana* extracts, *Matricaria recutita* (bisabolol / apigenin), and calcium carbonate/phosphate.
- **Obtain DrugBank IDs**: Without a valid `drugbank_id`, the KG-based prediction pipeline has no entry point.
- **Clarify the product's intended use**: Determine whether this is a homeopathic, dietary supplement, or conventional pharmaceutical product, as regulatory pathways differ.
- **Gather mechanism of action data**: Once individual components are mapped, document MOA (e.g., COX inhibition for arnica, GABA modulation for chamomile) to support mechanistic plausibility analysis.
- **Re-run TxGNN**: After DrugBank mapping is established, re-submit each component for independent repurposing prediction, then assess the combination-level evidence.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

