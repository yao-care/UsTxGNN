---
layout: default
title: Activated Charcoal Arsenic Triiodide Oenanthe Aqua
parent: 僅模型預測 (L5)
nav_order: 209
evidence_level: L5
indication_count: 0
---

# Activated Charcoal Arsenic Triiodide Oenanthe Aqua
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

# Multi-Component Preparation: Insufficient Data for Drug Repurposing Evaluation

## One-Sentence Summary

This candidate consists of a nine-ingredient mixture — including Activated Charcoal, Arsenic Triiodide, Oenanthe Aquatica Fruit, Oryctolagus Cuniculus Lung, Silicon Dioxide, Sulfur, Thyme, Tin, and Tribasic Calcium — with characteristics consistent with a homeopathic combination product.
The TxGNN model was **unable to generate any repurposing prediction** for this candidate, as no DrugBank ID could be mapped and no original indications were registered in Taiwan.
Without a valid prediction target, a standard repurposing evaluation cannot proceed.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | None on record |
| Predicted New Indication | None generated |
| TxGNN Prediction Score | N/A |
| Evidence Level | N/A (No prediction generated) |
| US Market Status | Not marketed |
| Number of NDAs | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Unavailable?

The TxGNN pipeline relies on mapping each drug's active ingredient to a DrugBank node in the knowledge graph. For this candidate, no DrugBank ID was successfully assigned (`drugbank_id: null`), which prevents the model from locating the compound within the graph and computing traversal-based repurposing scores.

The ingredient list points toward a homeopathic combination product. Homeopathic preparations are typically not catalogued as discrete entities in DrugBank because their active fractions are defined by dilution series rather than by molecular structure. As a result, standard SMILES-based or target-based lookups return no match, and the deep-learning prediction pathway is also blocked.

Currently, detailed mechanism of action data is unavailable. Without a clear pharmacological target or established efficacy evidence in any approved indication, the mechanistic rationale for any new indication cannot be assessed.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

No US approvals (NDAs) on record for this candidate.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note — Arsenic Triiodide component:** Although this mixture is presumed homeopathic (ultra-dilute), the nominal presence of arsenic triiodide warrants flagging. In pharmaceutical concentrations, arsenic-containing compounds carry significant toxicity (hepatotoxicity, cardiotoxicity, QTc prolongation). If this product is ever reformulated or evaluated at non-homeopathic concentrations, a full arsenic-specific safety assessment will be mandatory.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
TxGNN could not map this multi-ingredient candidate to the knowledge graph, so no repurposing prediction was generated; without a target indication, the evaluation pipeline cannot advance beyond this point.

**To proceed, the following is needed:**

- **DrugBank ID resolution**: Attempt per-ingredient lookups for each of the nine components individually (e.g., Arsenious acid → DB01169 for arsenic trioxide; Silicea → separate search) to determine whether any single ingredient can anchor a prediction.
- **Original indication clarification**: Identify the product's approved or traditional use (likely a respiratory or detoxification indication for homeopathic preparations of this type) to establish a baseline for comparison.
- **Regulatory classification**: Confirm whether the product is classified as a homeopathic medicine, traditional herbal product, or conventional pharmaceutical in the target jurisdiction, as this determines which regulatory and safety frameworks apply.
- **MOA documentation**: If individual ingredients are pursued, document their pharmacological mechanisms before initiating any repurposing analysis.
- **Safety dossier**: Obtain the full prescribing information (especially for the arsenic triiodide fraction) before any clinical or preclinical forward planning.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

