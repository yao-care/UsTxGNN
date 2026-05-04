---
layout: default
title: Acetaminophen Dextromethorphan Hydrobromide Phenyl
parent: 僅模型預測 (L5)
nav_order: 115
evidence_level: L5
indication_count: 0
---

# Acetaminophen Dextromethorphan Hydrobromide Phenyl
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

# ACETAMINOPHEN / DEXTROMETHORPHAN / PHENYLEPHRINE / TRIPROLIDINE: Multi-Component Cold & Flu Combination — No TxGNN Prediction Generated

## One-Sentence Summary

This is a fixed-dose combination of four active ingredients — acetaminophen, dextromethorphan HBr, phenylephrine HCl, and triprolidine — classically used together for symptomatic relief of cold and flu.
TxGNN did not generate any new indication predictions for this combination, most likely because the product has no unified DrugBank ID, which is required for knowledge graph traversal.
Without a prediction target, no repurposing pathway can be assessed at this stage, and a **Hold** decision is recommended until individual ingredient-level analysis is completed.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Cold & flu symptomatic relief (inferred from ingredient profile) |
| Predicted New Indication | N/A — no prediction generated |
| TxGNN Prediction Score | N/A |
| Evidence Level | N/A |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | **Hold** |

---

## Why No Prediction Was Generated

This combination consists of four pharmacologically distinct active ingredients:

| Ingredient | Drug Class | Primary Action |
|---|---|---|
| Acetaminophen | Analgesic / Antipyretic | Inhibits central prostaglandin synthesis |
| Dextromethorphan HBr | Antitussive | NMDA receptor antagonist; sigma-1 agonist |
| Phenylephrine HCl | Sympathomimetic decongestant | Alpha-1 adrenergic agonist; shrinks nasal mucosa |
| Triprolidine | First-generation H1 antihistamine | Blocks histamine H1 receptors; reduces rhinorrhea/sneezing |

Together these form a standard OTC multi-symptom cold and flu remedy. TxGNN performs repurposing analysis on **individual drugs** via their DrugBank IDs. Because this submission is a combination product with no unified DrugBank ID (`drugbank_id: null`), the knowledge graph has no single node to traverse — and therefore generates no predictions.

To unlock repurposing analysis, each ingredient must be evaluated independently.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for this combination as a TxGNN-predicted repurposing candidate.

---

## Literature Evidence

Currently no related literature available for TxGNN-predicted new indications for this combination.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** No safety data was available in this Evidence Pack. Each of the four components carries its own distinct safety profile — particularly dextromethorphan (serotonin syndrome risk with MAOIs) and phenylephrine (cardiovascular effects in hypertensive patients) — and these must be reviewed individually before any repurposing work proceeds.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
TxGNN could not generate any predictions because this combination product lacks the unified DrugBank ID required for knowledge graph analysis. There is no prediction to evaluate, and the US market status shows zero approved authorizations.

**To proceed, the following is needed:**

- **Decompose the combination** into its four individual active ingredients and submit each separately to the TxGNN pipeline
- **Obtain DrugBank IDs** for each ingredient: acetaminophen (DB00316), dextromethorphan (DB00514), phenylephrine (DB00388), triprolidine (DB00792) — confirm mappings via DrugBank API
- **Retrieve US FDA labeling** (NDA or OTC monograph) to populate approved indication and safety fields
- **Collect DDI and warning data** from individual ingredient package inserts before proceeding to any safety screen
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

