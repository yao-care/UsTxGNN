---
layout: default
title: Activated Charcoal Anhydrous Dibasic Calcium Phosp
parent: 僅模型預測 (L5)
nav_order: 182
evidence_level: L5
indication_count: 0
---

# Activated Charcoal Anhydrous Dibasic Calcium Phosp
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

# Multi-Component Mixture: No TxGNN Repurposing Prediction Available

## One-Sentence Summary

This entry describes a 10-component mixture — including Activated Charcoal, Arsenic Triiodide, Equisetum Arvense, Oenanthe Aquatica Fruit, and other herbal/mineral ingredients — with no recorded original indications and no regulatory authorization in Taiwan.
No TxGNN repurposing prediction was generated for this combination, making a standard drug repurposing evaluation impossible at this time.
The profile is flagged **Hold** pending fundamental data remediation and safety clarification.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not recorded |
| Predicted New Indication | No prediction available |
| TxGNN Prediction Score | N/A |
| Evidence Level | Not evaluable — no prediction generated |
| Taiwan Market Status | Not marketed (TFDA query returned 0 results) |
| Number of Licenses | 0 |
| Recommended Decision | **Hold** |

---

## Composition Note

This entry is a **multi-component mixture** rather than a single active pharmaceutical ingredient. The 10 declared components are:

| # | Component | Category |
|---|-----------|----------|
| 1 | Activated Charcoal | Adsorbent / Excipient |
| 2 | Anhydrous Dibasic Calcium Phosphate | Excipient |
| 3 | Arsenic Triiodide (AsI₃) | Homeopathic mineral |
| 4 | Beef Lung | Biological ingredient |
| 5 | Equisetum Arvense Top (Horsetail) | Herbal |
| 6 | Oenanthe Aquatica Fruit (Water Dropwort) | Herbal ⚠️ |
| 7 | Silicon Dioxide | Excipient |
| 8 | Sulfur | Homeopathic mineral |
| 9 | Teucrium Scorodonia Flowering Top (Wood Sage) | Herbal |
| 10 | Tin (Stannum) | Homeopathic mineral |

This composition is consistent with a **homeopathic preparation**. TxGNN is designed for single-molecule active pharmaceutical ingredients and operates on a knowledge graph of individual drug–disease pairs. Multi-component homeopathic formulations fall outside the model's intended scope, which explains why no prediction was generated.

---

## Safety Considerations

Three ingredients in this mixture carry notable safety concerns that must be resolved before any further evaluation:

- **Oenanthe Aquatica Fruit (Water Dropwort) ⚠️**: Contains oenanthotoxin, a potent convulsant that acts as a GABA-A receptor antagonist. This plant has caused fatal poisoning in humans and livestock. Any preparation containing this ingredient requires explicit concentration/dilution disclosure and regulatory review before use.
- **Arsenic Triiodide (AsI₃)**: An arsenic-containing compound. While arsenic trioxide (As₂O₃) has an established antineoplastic use in acute promyelocytic leukemia (APL), arsenic triiodide is a distinct compound with no approved pharmaceutical indication and limited safety data. Systemic arsenic toxicity risk depends entirely on concentration.
- **Tin (Stannum)**: A heavy metal with systemic toxicity potential at non-homeopathic concentrations. No pharmacological data available for this entry.

All other safety fields (warnings, contraindications, drug interactions) returned no data. Please refer to the applicable product insert and regulatory guidelines for complete safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This entry cannot proceed through the standard TxGNN repurposing pipeline because it is a multi-component mixture with no individual active ingredient mappable to the model's drug node graph, no original indication on record, and at least one ingredient (Oenanthe Aquatica) with serious toxicity concerns that must be addressed before any repurposing work begins.

**To proceed, the following is needed:**

- **Clarify product category**: Confirm whether this is a registered homeopathic preparation and provide ingredient dilution levels (e.g., 6C, 30X). This determines applicable regulatory pathway and safety thresholds.
- **Resolve Oenanthe Aquatica safety concern**: Obtain concentration data and assess compliance with applicable toxic plant regulations before any further steps.
- **Identify the repurposing target**: If the intent is to evaluate a specific component (e.g., a single active molecule in this mixture), resubmit that ingredient as a separate single-drug evidence pack with its own DrugBank ID.
- **Obtain MOA data**: For any single-molecule candidate extracted from this mixture, query DrugBank or relevant pharmacological databases for mechanism of action.
- **Confirm regulatory scope**: Clarify whether Taiwan TFDA authorization is being sought and under which product category (pharmaceutical, OTC, or homeopathic).
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

