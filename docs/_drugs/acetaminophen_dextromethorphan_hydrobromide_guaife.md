---
layout: default
title: Acetaminophen Dextromethorphan Hydrobromide Guaife
parent: 僅模型預測 (L5)
nav_order: 113
evidence_level: L5
indication_count: 0
---

# Acetaminophen Dextromethorphan Hydrobromide Guaife
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

# ACETAMINOPHEN / DEXTROMETHORPHAN / GUAIFENESIN / PSEUDOEPHEDRINE: Combination Cold Relief Agent — No Repurposing Prediction Generated

---

## One-Sentence Summary

This four-component OTC combination (analgesic + antitussive + expectorant + decongestant) is a classic cold and flu symptom-relief product widely used globally.
The TxGNN model **did not generate any new indication predictions** for this combination — most likely because TxGNN operates on single molecular entities, and this multi-ingredient compound lacks a unified DrugBank ID.
Due to the absence of predictions, Taiwan regulatory data, and safety records, **no repurposing evaluation can be completed at this stage**.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Cold/flu symptom relief (analgesic, antitussive, expectorant, nasal decongestant — based on known pharmacology of the four components) |
| Predicted New Indication | None (TxGNN returned no predictions) |
| TxGNN Prediction Score | N/A |
| Evidence Level | L5 — Model prediction unavailable; no supporting studies identified |
| US Market Status | Not marketed in Taiwan (0 licenses on record) |
| Number of NDAs | 0 |
| Recommended Decision | **Hold** |

---

## Why No Prediction Was Generated

This entry contains **four distinct active pharmaceutical ingredients** rather than a single molecular entity:

| Component | Drug Class | Role in Combination |
|-----------|-----------|---------------------|
| Acetaminophen | Analgesic / Antipyretic | Reduces fever and pain |
| Dextromethorphan HBr | Antitussive (NMDA antagonist) | Suppresses cough reflex |
| Guaifenesin | Expectorant | Thins and loosens mucus |
| Pseudoephedrine | Sympathomimetic decongestant | Reduces nasal congestion |

TxGNN is designed to generate predictions for **individual drug nodes** in its knowledge graph, each identified by a unique DrugBank ID. Because this combination has no single DrugBank ID (`drugbank_id: null`), the model cannot map it to the graph and therefore produces no repurposing candidates.

To run a meaningful TxGNN analysis, each component would need to be evaluated **individually**, and any overlapping predictions across all four components could then be considered combinatorial opportunities.

---

## Safety Considerations

Please refer to the package insert for safety information.

> No warning, contraindication, or drug-drug interaction data was retrieved for this combination entry. Each component individually carries well-known safety profiles (e.g., pseudoephedrine contraindicated in hypertension; acetaminophen risk in hepatic impairment; dextromethorphan interaction with MAO inhibitors), but these could not be formally captured under the current `drugbank_id: null` query pathway.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
TxGNN cannot process multi-ingredient combinations without individual DrugBank node identifiers; zero predictions were generated, and Taiwan regulatory and safety records are both absent, making a repurposing evaluation impossible at this stage.

**To proceed, the following is needed:**

- **Decompose the combination**: Run TxGNN separately for each of the four components using their individual DrugBank IDs:
  - Acetaminophen → DB00316
  - Dextromethorphan → DB00514
  - Guaifenesin → DB00806
  - Pseudoephedrine → DB00852
- **Aggregate component-level predictions**: Identify diseases that appear in the top predictions for two or more components simultaneously, as these represent the most actionable combinatorial repurposing signals
- **Retrieve Taiwan regulatory status per component**: Each ingredient may have individual TFDA licenses even if the fixed-dose combination does not
- **Obtain safety data**: Query DrugBank API per component to retrieve MOA, warnings, contraindications, and DDI profiles
- **Determine regulatory pathway**: If a repurposing candidate is identified, clarify whether it requires a new NDA for the combination or whether individual component data is sufficient for bridging
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

