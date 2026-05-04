---
layout: default
title: Acetaminophen Dextromethorphan Hydrobromide Diphen
parent: 僅模型預測 (L5)
nav_order: 111
evidence_level: L5
indication_count: 0
---

# Acetaminophen Dextromethorphan Hydrobromide Diphen
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

# Acetaminophen / Dextromethorphan Hydrobromide / Diphenhydramine: No Repurposing Predictions Available

## One-Sentence Summary

Acetaminophen / Dextromethorphan Hydrobromide / Diphenhydramine is a three-component OTC combination typically used for cold and flu symptom relief — covering fever, cough, and nasal congestion or sleep disturbance.
The TxGNN model returned **no predicted new indications** for this combination drug entry.
Evaluation cannot proceed substantively until predictions are generated and missing data gaps are resolved.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Cold and flu symptom relief (analgesic/antipyretic + antitussive + antihistamine) |
| Predicted New Indication | None available |
| TxGNN Prediction Score | N/A |
| Evidence Level | N/A — no predictions generated |
| Taiwan Market Status | 未上市 (Not marketed) |
| Number of Licensed Products | 0 |
| Recommended Decision | Hold |

---

## Why No Predictions Were Generated

This Evidence Pack contains an empty `predicted_indications` array, which means the TxGNN pipeline did not produce any repurposing candidates for this drug entry. Two likely reasons account for this:

**1. Multi-component combination string was used as the query key.**
TxGNN's knowledge graph maps individual chemical entities (single INN) to DrugBank nodes. The compound query string `"ACETAMINOPHEN; DEXTROMETHORPHAN HYDROBROMIDE; DIPHENHYDRAMINE"` does not match any single node in the knowledge graph, so no score is computed. The three ingredients would need to be queried individually.

**2. No DrugBank ID was resolved.**
The `drugbank_id` field is `null`, confirming that entity resolution failed. Without a valid DrugBank node, neither the KG-based method nor the DL-based method can produce predictions.

The DrugBank query log shows one result was returned (`result_count: 1`), but this data was not propagated into the Evidence Pack — likely a pipeline parsing issue that should be investigated.

---

## Taiwan Market Information

No licensed products were found in the Taiwan regulatory database for this combination string. This may reflect:

- The combination is not registered as a fixed-dose combination product in Taiwan
- The query was run against the full combination name rather than individual ingredients

Individual active ingredients (acetaminophen, dextromethorphan, diphenhydramine) are widely available as separate or smaller combination OTC products in Taiwan under various brand names, but these are not captured in the current query.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model produced no repurposing predictions for this entry because the combination drug string could not be resolved to a DrugBank node. There is no prediction basis, no original indication data in the Evidence Pack, and no MOA data — making a repurposing evaluation impossible at this stage.

**To proceed, the following is needed:**

- **Disaggregate the query:** Re-run the TxGNN pipeline for each active ingredient separately — `ACETAMINOPHEN` (DB00316), `DEXTROMETHORPHAN` (DB00514), and `DIPHENHYDRAMINE` (DB01075) — to obtain individual prediction scores and ranked disease candidates
- **Resolve the DrugBank data gap:** The DrugBank collector returned 1 result but it was not populated into the Evidence Pack; trace the pipeline step and fix the data propagation error
- **Retrieve MOA for each ingredient:** Query DrugBank API for mechanism of action of all three components to enable mechanistic plausibility analysis
- **Clarify target market:** Confirm whether the regulatory query should target Taiwan (TFDA) or another jurisdiction, and rerun with individual ingredient names
- **Obtain package insert safety data:** Download and parse the TFDA package insert PDF to fill the blocking data gap (DG001) before any safety screening can proceed
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

