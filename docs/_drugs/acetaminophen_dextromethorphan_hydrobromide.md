---
layout: default
title: Acetaminophen Dextromethorphan Hydrobromide
parent: 僅模型預測 (L5)
nav_order: 110
evidence_level: L5
indication_count: 0
---

# Acetaminophen Dextromethorphan Hydrobromide
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

# ACETAMINOPHEN + DEXTROMETHORPHAN HYDROBROMIDE: Repurposing Evaluation — Insufficient Data

## One-Sentence Summary

ACETAMINOPHEN + DEXTROMETHORPHAN HYDROBROMIDE is a well-known combination used in over-the-counter cold and flu remedies (analgesic/antipyretic + antitussive).
However, **no TxGNN repurposing predictions were generated** for this combination, most likely because the compound entry is not represented as a single node in the knowledge graph.
Due to missing regulatory data, mechanism of action, and predicted indications, **this candidate cannot proceed to evaluation at this time**.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Cold/flu symptom relief (analgesic, antipyretic, antitussive) — inferred from drug class; no formal indication text available |
| Predicted New Indication | None — TxGNN returned no predictions |
| TxGNN Prediction Score | N/A |
| Evidence Level | L5 (model prediction only — and none generated) |
| US Market Status | Not marketed (no licenses on record) |
| Number of NDAs | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known pharmacology:

- **Acetaminophen** inhibits prostaglandin synthesis centrally, providing analgesia and fever reduction. It does not have significant anti-inflammatory activity via COX inhibition in peripheral tissues.
- **Dextromethorphan hydrobromide** acts as a non-competitive NMDA receptor antagonist and sigma-1 receptor agonist, suppressing cough reflex centrally. It has also been investigated for neuroprotective and antidepressant properties.

The combination targets two distinct symptom pathways (pain/fever + cough), which is why it is standard in cold/flu products. Because the TxGNN knowledge graph maps individual drug nodes, combination INN entries may not resolve to a single graph node, explaining the absence of predictions.

No repurposing direction can be evaluated without predictions.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for this combination under TxGNN-predicted indications.

---

## Literature Evidence

Currently no related literature available for TxGNN-predicted indications.

---

## US Market Information

No US NDA licenses are recorded for this exact combination entry. Note that individual components (acetaminophen and dextromethorphan) are widely available under many OTC and Rx products in the US; the absence of records here reflects the way the combination INN was queried, not the absence of marketed products globally.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** Safety data (key warnings, contraindications, drug interactions) were not retrieved for this combination entry. Given that acetaminophen carries a well-known risk of **hepatotoxicity at high doses or in combination with alcohol**, and dextromethorphan carries risk of **serotonin syndrome when combined with MAOIs or serotonergic agents**, a full safety review is essential before any repurposing work proceeds.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN pipeline returned no predicted indications for this combination entry, and critical data including regulatory approval text, mechanism of action, and safety information are all absent. There is no actionable repurposing hypothesis to evaluate.

**To proceed, the following is needed:**

- **Resolve KG representation**: Determine whether the combination should be split into two individual INN queries (ACETAMINOPHEN and DEXTROMETHORPHAN HYDROBROMIDE separately) and re-run TxGNN predictions for each component
- **Retrieve MOA data**: Query DrugBank API for individual component entries to populate mechanism of action (DG002 — High severity)
- **Retrieve safety data**: Download and parse the package insert (DG001 — Blocking severity) to populate key warnings and contraindications before any S1 safety screening
- **Clarify regulatory scope**: Confirm whether the evaluation target is the combination product or one of the individual components
- **Re-run evidence collection**: Once predictions are available, re-trigger ClinicalTrials.gov and PubMed collectors for each predicted indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

