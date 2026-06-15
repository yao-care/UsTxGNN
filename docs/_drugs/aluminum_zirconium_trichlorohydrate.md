---
layout: default
title: Aluminum Zirconium Trichlorohydrate
parent: 僅模型預測 (L5)
nav_order: 312
evidence_level: L5
indication_count: 0
---

# Aluminum Zirconium Trichlorohydrate
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

# Aluminum Zirconium Trichlorohydrate: Insufficient Data for Drug Repurposing Evaluation

## One-Sentence Summary

Aluminum Zirconium Trichlorohydrate is a compound primarily used as an antiperspirant active ingredient in personal care products; it has no registered pharmaceutical indications in Taiwan and no DrugBank ID was successfully retrieved.
The TxGNN model did not generate any repurposing predictions for this compound, likely because the necessary pharmacological identifiers and indication data required as model inputs are absent.
Three critical data gaps — DrugBank ID, mechanism of action, and safety profile — must be resolved before a meaningful repurposing evaluation can proceed.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | None recorded (primarily used as antiperspirant ingredient) |
| Predicted New Indication | None generated |
| TxGNN Prediction Score | N/A |
| Evidence Level | L5 — No predictions generated |
| Market Status (Taiwan) | Not marketed |
| Number of Approved Licenses | 0 |
| Recommended Decision | **Hold** |

---

## Why No Prediction Was Generated

Aluminum Zirconium Trichlorohydrate is a coordination complex of aluminum, zirconium, and chloride ions used in over-the-counter antiperspirant formulations. It acts primarily by forming a gel plug within the eccrine sweat ducts, physically reducing perspiration output — a mechanism that is topical and local rather than systemic.

The TxGNN knowledge graph model requires two anchors to generate repurposing predictions: a valid **DrugBank ID** (to map the compound onto the drug node in the knowledge graph) and at least one **registered pharmaceutical indication** (to establish the drug's existing position in the disease network). Neither condition is met here. The query log confirms that while DrugBank was successfully queried, no DrugBank ID was extracted — suggesting the compound may exist under a variant name or may not be indexed as a systemic pharmaceutical entity.

Without these anchors, the model has no basis on which to compute disease-similarity scores or traverse treatment pathways, and therefore produces no candidate indications. This is a data pipeline failure, not evidence of absence of repurposing potential.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No TxGNN repurposing predictions were generated because the compound lacks the required DrugBank ID and registered pharmaceutical indications needed for model input; the evaluation cannot proceed until these identifiers are established.

**To proceed, the following is needed:**

- **Resolve DrugBank mapping**: Search DrugBank under variant names (e.g., *Aluminum Zirconium Tetrachlorohydrex Gly*, *AZT complex*) or CAS number (57158-29-9) to obtain a valid DrugBank ID
- **Clarify compound scope**: Confirm whether this evaluation targets the antiperspirant ingredient itself or a novel pharmaceutical formulation/delivery of the compound
- **Retrieve mechanism of action**: Query DrugBank API or primary literature once the correct compound entry is identified
- **Obtain safety data**: Download and parse the TFDA package insert PDF to extract warnings, contraindications, and drug interactions (currently Blocking severity per DG001)
- **Re-run TxGNN pipeline**: After DrugBank ID is confirmed and at least one pharmacological indication is registered, re-submit to the prediction pipeline
- **Consider reclassification**: If the compound is determined to function exclusively as a cosmetic/topical agent with no systemic absorption, it may be out of scope for the drug repurposing programme and should be flagged for exclusion
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

