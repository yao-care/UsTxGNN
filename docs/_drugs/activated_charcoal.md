---
layout: default
title: Activated Charcoal
parent: 僅模型預測 (L5)
nav_order: 154
evidence_level: L5
indication_count: 0
---

# Activated Charcoal
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

# Activated Charcoal: Repurposing Evaluation — Insufficient Data for Analysis

## One-Sentence Summary

Activated charcoal (active ingredient: charcoal, medicinal) is a well-established agent used in emergency medicine for acute poisoning and drug overdose management.
The current Evidence Pack contains **no TxGNN repurposing predictions**, likely due to a mapping or pipeline gap at the prediction stage,
and **no regulatory authorizations** are on record, preventing a standard repurposing evaluation from being completed at this time.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not recorded in this Evidence Pack |
| Predicted New Indication | No predictions available |
| TxGNN Prediction Score | N/A |
| Evidence Level | N/A — no model predictions returned |
| US Market Status | No authorizations on record |
| Number of NDAs | 0 |
| Recommended Decision | **Hold** |

---

## Why This Report Cannot Be Completed

There are two root causes blocking a standard repurposing evaluation:

**1. No TxGNN predictions returned.**
The `predicted_indications` array is empty. This typically occurs when the drug's DrugBank ID (`DB09278`) fails to match any node in the TxGNN knowledge graph, or when the prediction run was not triggered for this candidate. Without at least one predicted indication, the core sections of this report — mechanism analysis, clinical trial evidence, and literature evidence — cannot be populated.

**2. No regulatory data on record.**
The regulatory query against the FDA database returned 0 results for "ACTIVATED CHARCOAL." Activated charcoal is primarily used as a hospital emergency agent and may be registered under a different INN variant, a combination product, or as a medical device / OTC product not captured by the current query pipeline. This also means original indication data is unavailable.

---

## Safety Considerations

No safety data is currently available for this candidate in the Evidence Pack. Please refer to the package insert and standard emergency medicine references for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
With zero predicted indications and no original indication data, there is no repurposing hypothesis to evaluate. The evidence pack is structurally incomplete and cannot support any go/no-go recommendation.

**To proceed, the following is needed:**

- **Re-run TxGNN prediction** — Verify that `DB09278` exists as a node in `data/external/drugbank_vocab.csv`. If absent, the drug was filtered out during the DrugBank mapping step; check whether the INN variant "ACTIVATED CHARCOAL" maps to an alternate DrugBank entry (e.g., `DB09278` vs. `DB13257`).
- **Confirm INN normalization** — Query the normalizer with alternate forms: `"Activated Charcoal"`, `"Charcoal, Activated"`, `"Medicinal Charcoal"` to rule out a name-matching failure.
- **Retrieve MOA data** — Query DrugBank API for `DB09278` to populate `original_moa`; this is required for mechanism-relevance analysis (currently flagged as DG002, severity: High).
- **Retrieve regulatory warnings** — Download and parse the package insert PDF from the relevant regulatory authority to fill safety warnings and contraindications (currently flagged as DG001, severity: Blocking).
- **Verify market status** — Confirm whether activated charcoal is registered under a different product category (e.g., OTC, hospital-use only, or medical device) that is excluded from the current regulatory query scope.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

