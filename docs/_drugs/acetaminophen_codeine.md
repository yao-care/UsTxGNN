---
layout: default
title: Acetaminophen Codeine
parent: 僅模型預測 (L5)
nav_order: 108
evidence_level: L5
indication_count: 0
---

# Acetaminophen Codeine
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

# Acetaminophen + Codeine: Evaluation Incomplete — No Repurposing Prediction Available

## One-Sentence Summary

Acetaminophen + Codeine is a classic combination analgesic widely used worldwide for moderate to moderately severe pain management.
However, **the TxGNN model returned no repurposing predictions** for this combination drug entry, likely because the pipeline requires a single-ingredient DrugBank mapping that could not be resolved.
Without a prediction target, this report documents the data gaps that must be resolved before a full repurposing evaluation can proceed.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Unknown (no TFDA license records found; combination not registered in this system) |
| Predicted New Indication | None — TxGNN returned no predictions |
| TxGNN Prediction Score | N/A |
| Evidence Level | L5 (model prediction only — and none was produced) |
| US Market Status | 未上市 (Not marketed in Taiwan; US status not queried) |
| Number of NDAs | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

No prediction was generated, so a mechanistic bridge analysis cannot be completed.

Based on general pharmacological knowledge: Acetaminophen acts centrally and peripherally to inhibit prostaglandin synthesis (COX pathway), producing analgesia and antipyresis without significant anti-inflammatory effects at standard doses. Codeine is a prodrug converted to morphine via CYP2D6, acting on μ-opioid receptors to modulate pain perception. Together, they provide additive analgesia for moderate pain that is suboptimal for either agent alone.

TxGNN's knowledge graph operates on single-ingredient nodes mapped to DrugBank IDs. Because this entry is a **multi-ingredient combination** (`ACETAMINOPHEN; CODEINE`) without a resolved DrugBank ID, the prediction engine could not anchor to a graph node — resulting in zero outputs. Separating the two ingredients and running individual predictions would be the appropriate remediation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered (no predicted indication target to query against).

---

## Literature Evidence

Currently no related literature available (no predicted indication target to query against).

---

## US Market Information

No Taiwan license records found for this combination entry. The query returned 0 results from the TFDA database.

> **Note**: Acetaminophen + Codeine products are widely marketed internationally (e.g., Tylenol with Codeine No. 3/4 in the US under NDA 022450 and others), but this system did not retrieve those records. A direct US FDA query is recommended.

---

## Safety Considerations

Please refer to the package insert for safety information.

> Known class-level concerns for Acetaminophen + Codeine combinations include:
> - **Codeine (opioid)**: Risk of respiratory depression, dependence, and CYP2D6 ultra-rapid metabolizer toxicity; contraindicated in children post-tonsillectomy (FDA Black Box Warning issued 2013).
> - **Acetaminophen**: Hepatotoxicity risk with overdose or concurrent alcohol use; maximum daily dose 4 g (3 g in high-risk patients).
> - **DDI query**: Returned `not_found` — formal interaction screening could not be completed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN pipeline produced zero repurposing predictions because the combination drug entry could not be mapped to a DrugBank node — the fundamental input required for graph-based prediction is missing. There is no prediction to evaluate.

**To proceed, the following is needed:**

- [ ] **Split the combination into individual components**: Run separate TxGNN analyses for `ACETAMINOPHEN` (DrugBank: DB00316) and `CODEINE` (DrugBank: DB00318) to obtain individual predictions
- [ ] **Resolve DrugBank ID**: Confirm whether a combination-level DrugBank entry exists, or confirm the two-component approach above
- [ ] **Retrieve US FDA records**: Query openFDA NDA database directly for Acetaminophen+Codeine products to populate the regulatory table
- [ ] **Obtain MOA data**: Pull structured pharmacology from DrugBank API for both components (Data Gap DG002)
- [ ] **Obtain safety/warning data**: Download and parse prescribing information to fill DG001 (Blocking severity)
- [ ] **Re-run evidence collection**: Once a predicted indication is established, re-run ClinicalTrials.gov and PubMed collectors against the new target
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

