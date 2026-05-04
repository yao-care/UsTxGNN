---
layout: default
title: Aluminum Zirconium Trichlorohydrex Gly
parent: 僅模型預測 (L5)
nav_order: 299
evidence_level: L5
indication_count: 0
---

# Aluminum Zirconium Trichlorohydrex Gly
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

# Aluminum Zirconium Trichlorohydrex Gly: Insufficient Data for Repurposing Evaluation

## One-Sentence Summary

Aluminum Zirconium Trichlorohydrex Gly is an aluminum-zirconium complex salt widely used as an active ingredient in topical antiperspirant cosmetic formulations, functioning by temporarily blocking sweat ducts.
The TxGNN model returned **no predicted new indications** for this compound, and no original pharmaceutical indications are recorded in this Evidence Pack.
As a result, this report cannot proceed to a standard repurposing evaluation — a data remediation step is required before further analysis.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No pharmaceutical indication recorded |
| Predicted New Indication | None (TxGNN returned no candidates) |
| TxGNN Prediction Score | N/A |
| Evidence Level | L5 — Model returned no prediction |
| US Market Status | Not Marketed (no TFDA licenses found) |
| Number of NDAs | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

No prediction is available to evaluate. Aluminum Zirconium Trichlorohydrex Gly is primarily known as a cosmetic/OTC antiperspirant active — it is not registered as a pharmaceutical drug in the queried databases, which likely explains the absence of TxGNN output.

Currently, detailed mechanism of action data is not available. Based on known information, Aluminum Zirconium Trichlorohydrex Gly belongs to the aluminum salt antiperspirant class. Its primary mechanism involves precipitation of aluminum-protein complexes within eccrine sweat ducts, forming a physical obstruction that reduces perspiration. Whether this mechanism has any meaningful pharmacological application beyond topical antiperspirant use remains unexplored in the current dataset.

Without a TxGNN prediction and without a registered pharmaceutical indication as an anchor, there is no mechanistic repurposing hypothesis to evaluate at this stage.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for this compound in a pharmaceutical repurposing context.

---

## Literature Evidence

Currently no related literature available in the Evidence Pack. Literature search was not triggered due to absence of predicted indications.

---

## US Market Status

No authorizations found. The TFDA query on 2026-03-24 returned 0 results for this compound.

---

## Safety Considerations

Please refer to the package insert for safety information.

No drug interaction data was found (DDI query returned `not_found`). No key warnings or contraindications are available in the current dataset.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Evidence Pack contains no predicted indications, no original pharmaceutical indication, no mechanism of action data, and no safety data — the minimum conditions for a repurposing evaluation are not met. This compound appears to exist in regulatory databases as a cosmetic ingredient rather than a pharmaceutical drug, which likely caused the TxGNN pipeline to return an empty candidate list.

**To proceed, the following is needed:**

- **Confirm compound identity**: Verify whether this compound is intended as a pharmaceutical agent or a cosmetic active; if cosmetic, reassess whether repurposing evaluation is applicable.
- **DrugBank lookup**: The query log notes 1 DrugBank result — retrieve and parse the DrugBank entry to obtain DrugBank ID, categories, MOA, and any therapeutic associations.
- **Re-run TxGNN with correct DrugBank ID**: If a valid DrugBank ID is obtained, re-execute the TxGNN prediction pipeline using the standardized identifier.
- **TFDA/FDA package insert**: Download and parse available safety documentation (DG001) to populate warnings and contraindications before any S1 safety screening.
- **Re-evaluate evidence level**: Only after a TxGNN prediction candidate is available can an evidence-level determination (L1–L5) and Go/Hold/Proceed-with-Guardrails recommendation be made.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

