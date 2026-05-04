---
layout: default
title: Arnica Montana Root Calcium Fluoride Calcium Iodid
parent: 僅模型預測 (L5)
nav_order: 364
evidence_level: L5
indication_count: 0
---

# Arnica Montana Root Calcium Fluoride Calcium Iodid
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

# Multi-Component Botanical/Homeopathic Combination: Insufficient Data for Repurposing Analysis

## One-Sentence Summary

This candidate is a complex 8-component botanical and mineral formula — including Arnica montana, Horse chestnut, Hedera helix, and Conium maculatum — with no registered indications and no US regulatory approval. The TxGNN model returned **no predicted indications** for this combination, as the multi-component structure prevented knowledge graph mapping. Without DrugBank linkage or a defined original indication, a standard repurposing evaluation cannot be completed at this stage.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not established (no registered indications found) |
| Predicted New Indication | None — TxGNN returned no predictions |
| TxGNN Prediction Score | N/A |
| Evidence Level | Unassessable (model prediction not generated) |
| US Market Status | Not marketed |
| Number of NDAs | 0 |
| Recommended Decision | **Hold** |

---

## Why No Prediction Was Generated

This candidate contains 8 distinct components:

| Component | Class | Known Pharmacological Role |
|-----------|-------|--------------------------|
| Arnica montana root | Botanical | Anti-inflammatory, wound healing |
| Calcium fluoride | Mineral | Homeopathic (connective tissue) |
| Calcium iodide | Mineral salt | Homeopathic |
| Clematis recta flowering top | Botanical | Homeopathic (rheumatic conditions) |
| Conium maculatum flowering top | Botanical | Alkaloid-bearing; historically sedative/antispasmodic |
| Hedera helix flowering twig | Botanical | Anti-inflammatory, traditionally respiratory |
| Horse chestnut | Botanical | Aescin — venous insufficiency, anti-edema |
| Scrophularia nodosa whole | Botanical | Traditional anti-inflammatory, lymphatic |

The TxGNN model requires a single DrugBank ID to anchor the drug entity in the knowledge graph and generate disease-probability scores. Because this candidate is a multi-component formula with no unified DrugBank entry, the pipeline could not produce scored repurposing predictions.

Individually, several components have documented pharmacological rationale — Horse chestnut (Aesculus hippocastanum) has the strongest evidence base, with clinical data in **chronic venous insufficiency**. Arnica montana has anti-inflammatory and hematoma-resolving properties. The overall combination profile is consistent with a homeopathic or standardized complex herbal preparation targeting venous, lymphatic, or soft-tissue conditions — but this remains a pharmacological inference, not a model-derived prediction.

---

## Safety Considerations

Standard safety databases returned no interactions or warnings for this combination as a whole. However, one component warrants special attention:

- **Conium maculatum** (poison hemlock) contains coniine and related piperidine alkaloids. Even in diluted homeopathic formulations, the presence of this ingredient requires clarification of the actual dose and preparation standard before any clinical use.
- **Hedera helix** may cause contact sensitization in some individuals.
- No drug–drug interaction data is available for this combination from standard pharmacological sources.

Please refer to individual component monographs and applicable homeopathic/herbal regulatory guidance for full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN pipeline could not generate repurposing predictions because the multi-component combination lacks a unified knowledge graph entity. Without a defined original indication and with critical MOA and safety data absent, this candidate cannot proceed through standard repurposing evaluation.

**To proceed, the following is needed:**

- **Decompose the combination**: Run TxGNN predictions for each individual botanical component (e.g., Horse chestnut → Aesculus hippocastanum → DrugBank DB13566 equivalent) to identify which ingredient drives repurposing signal
- **Clarify formulation type**: Confirm whether this is a homeopathic preparation (highly diluted, regulated under different standards) or a standardized herbal extract — these follow entirely different evidence and regulatory pathways
- **Obtain product label**: Retrieve the original monograph or package insert to establish the intended indication and dosing context
- **Safety review for Conium maculatum**: Determine the actual alkaloid content and concentration before any clinical consideration
- **Resubmit individual components**: Once individual DrugBank IDs are confirmed, rerun the evidence pack pipeline per ingredient and aggregate results
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

