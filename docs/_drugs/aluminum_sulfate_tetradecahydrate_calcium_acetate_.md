---
layout: default
title: Aluminum Sulfate Tetradecahydrate Calcium Acetate 
parent: 僅模型預測 (L5)
nav_order: 293
evidence_level: L5
indication_count: 0
---

# Aluminum Sulfate Tetradecahydrate Calcium Acetate 
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

# Aluminum Sulfate Tetradecahydrate + Calcium Acetate Monohydrate: Insufficient Data for Repurposing Analysis

## One-Sentence Summary

Aluminum Sulfate Tetradecahydrate combined with Calcium Acetate Monohydrate is a topical astringent combination used in dermatology (e.g., modified Burow's solution) for skin conditions such as contact dermatitis and fungal infections.
However, **TxGNN returned no predicted repurposing indications** for this compound combination, and the drug has **no registered products in Taiwan**.
As a result, a standard evidence-based repurposing evaluation cannot be completed at this time.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Topical astringent use (dermatitis, skin irritation) — not formally registered in Taiwan |
| Predicted New Indication | None — TxGNN returned no predictions |
| TxGNN Prediction Score | N/A |
| Evidence Level | L5 — No supporting studies identified |
| US Market Status | Not marketed in Taiwan (0 registered licenses) |
| Number of NDAs | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

No TxGNN prediction was generated for this drug. This typically occurs for one of three reasons:

1. **The compound is not in the TxGNN knowledge graph** — The combination "Aluminum Sulfate Tetradecahydrate + Calcium Acetate Monohydrate" may not map to a DrugBank node (DrugBank ID is absent in this Evidence Pack), preventing the model from traversing the drug–disease network.

2. **The drug acts locally rather than systemically** — Topical astringents work by precipitating surface proteins and contracting tissue locally. They have negligible systemic absorption, which limits the biological plausibility of systemic repurposing and may cause the model to yield no candidates above threshold.

3. **Mechanism of action data is unavailable** — Without MOA annotation, the model cannot infer mechanistic links to candidate diseases.

Currently, no repurposing direction can be evaluated.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
TxGNN produced no predicted indications, there is no Taiwan regulatory approval history, and both MOA and safety data are absent. There is no basis on which to evaluate a new indication at this time.

**To proceed, the following is needed:**

- **Resolve DrugBank ID mapping**: Query DrugBank for each component individually (aluminum sulfate, calcium acetate) to obtain node IDs, then re-run TxGNN prediction.
- **Clarify intended formulation route**: If the intended use is topical only, systemic repurposing analysis is likely not applicable; redirect evaluation toward topical indication expansion instead.
- **Obtain MOA data**: Retrieve mechanism of action from DrugBank or primary literature for each active ingredient.
- **Confirm original registered indication**: Identify the approved indication in any jurisdiction (US, EU, Japan) to establish the repurposing baseline.
- **Re-run evidence collection**: Once a target indication is identified, collect ClinicalTrials.gov registrations and PubMed literature to determine evidence level.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

