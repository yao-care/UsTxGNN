---
layout: default
title: Acetaminophen Dextromethorphan Hydrobromide Tripro
parent: 僅模型預測 (L5)
nav_order: 118
evidence_level: L5
indication_count: 0
---

# Acetaminophen Dextromethorphan Hydrobromide Tripro
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

# ACETAMINOPHEN / DEXTROMETHORPHAN / TRIPROLIDINE: Cold Symptom Combination — No Repurposing Prediction Available

## One-Sentence Summary

This is a three-component OTC cold and flu combination product containing a pain reliever/antipyretic (acetaminophen), a cough suppressant (dextromethorphan hydrobromide), and a first-generation antihistamine (triprolidine), commonly used to relieve cold symptoms such as fever, cough, and runny nose.

The TxGNN model returned **no predicted new indications** for this combination query, and the drug has **no marketing authorization** in Taiwan (US regulatory data not applicable). At this stage, there is **insufficient data to perform a drug repurposing evaluation**.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Cold & flu symptom relief (fever, cough, rhinorrhea) — based on known pharmacology of the three components |
| Predicted New Indication | None (TxGNN returned no predictions) |
| TxGNN Prediction Score | N/A |
| Evidence Level | L5 — Model prediction not available; no supporting studies identified |
| US Market Status | Not marketed in Taiwan; US status not queried |
| Number of NDAs | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

No TxGNN prediction was returned for this drug combination. This is likely because the query was submitted as a multi-component string (`ACETAMINOPHEN; DEXTROMETHORPHAN HYDROBROMIDE; TRIPROLIDINE`) rather than as individual DrugBank-mapped entities. The TxGNN knowledge graph operates on single drug nodes identified by DrugBank ID; combination strings without a corresponding DrugBank ID cannot be matched to the graph.

Each component has well-characterised pharmacology individually:
- **Acetaminophen** inhibits prostaglandin synthesis centrally (COX-3), producing analgesia and antipyresis.
- **Dextromethorphan HBr** is a non-opioid NMDA receptor antagonist and sigma-1 receptor agonist that suppresses the cough reflex.
- **Triprolidine** is a first-generation H1 antihistamine that reduces rhinorrhea and sneezing.

Running three separate TxGNN queries (one per component) and cross-referencing the results would be the appropriate next step to identify any repurposing signals.

---

## US Market Information

No marketing authorizations were found for this combination in Taiwan. No US NDA data was queried in this Evidence Pack.

---

## Safety Considerations

No safety data (warnings, contraindications, or drug interactions) is currently available for this combination entry. Before any further evaluation, the following should be retrieved:

- Package insert warnings and contraindications from the original manufacturers of each component.
- Drug–drug interaction profile for the three-way combination (particularly dextromethorphan's known interactions with MAOIs and serotonergic agents, and triprolidine's CNS depressant interactions).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN pipeline returned no predictions because this entry was submitted as a multi-component combination string without a DrugBank ID, which the knowledge graph cannot process. There is no Taiwan market presence to anchor a regulatory pathway, and safety data has not been retrieved.

**To proceed, the following is needed:**

- **Decompose the query**: Run TxGNN predictions separately for acetaminophen (DB00316), dextromethorphan (DB00514), and triprolidine (DB00786) using their individual DrugBank IDs.
- **Retrieve MOA data**: Query DrugBank API for each component's mechanism of action to support mechanistic plausibility analysis.
- **Retrieve safety data**: Download package inserts from TFDA or FDA for each active ingredient to populate warnings and contraindications.
- **Confirm regulatory scope**: Clarify whether the repurposing target is the fixed-dose combination or one of the individual components, as this determines the regulatory and IP strategy.
- **Re-run the Evidence Pack**: Once DrugBank IDs are resolved and individual predictions are available, re-generate this report.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

