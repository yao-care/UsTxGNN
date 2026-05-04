---
layout: default
title: Acebutolol
parent: 僅模型預測 (L5)
nav_order: 64
evidence_level: L5
indication_count: 2
---

# Acebutolol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Acebutolol: Drug Repurposing Evaluation — No Predicted Indications Available

## Summary

Acebutolol (DrugBank ID: DB01193) is a beta-adrenergic blocking agent historically associated with cardiovascular indications such as hypertension and cardiac arrhythmias. The TxGNN model **did not generate any repurposing predictions** for this drug in the current evaluation run, and the drug is not marketed in Taiwan. Combined with missing mechanism of action and safety data, a full repurposing evaluation cannot be completed at this stage.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available in current data |
| Predicted New Indication | None — TxGNN returned no predictions |
| TxGNN Prediction Score | N/A |
| Evidence Level | N/A |
| Taiwan Market Status | Not marketed |
| Number of Licenses | 0 |
| Recommended Decision | **Hold** |

---

## Why No Predictions Were Generated

Currently, confirmed original indication data and detailed mechanism of action data are not available in this Evidence Pack. Based on known pharmacological literature, acebutolol belongs to the cardioselective beta-1 adrenergic blocker class, with the distinguishing property of partial agonist activity (intrinsic sympathomimetic activity, ISA). It is typically indicated for hypertension and ventricular arrhythmias.

The absence of TxGNN predictions may stem from one or more of the following causes:

1. **Knowledge graph mapping gap** — acebutolol may not have been successfully linked to its DrugBank node or disease nodes during the prediction run, resulting in no candidate pairs being scored.
2. **Indication overlap** — the model's training data may already reflect acebutolol's established cardiovascular indications, meaning no novel repurposing signal was detected above the threshold.
3. **Data completeness** — without confirmed original indications loaded into the pipeline, the model may have lacked sufficient context to generate candidates.

The DrugBank query did return one record (`result_count: 1`), confirming the drug exists in the knowledge base. The gap is therefore in the pipeline's ability to translate that record into scored predictions, not in the drug's basic identifiability.

---

## Clinical Trial Evidence

Currently no related clinical trials registered — no predicted indications to evaluate.

---

## Literature Evidence

Currently no related literature available — no predicted indications to evaluate.

---

## Taiwan Market Information

Acebutolol is currently not marketed in Taiwan. No license records exist in the Taiwan FDA database.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN pipeline returned no predicted indications for acebutolol, and two blocking data gaps — missing MOA and missing safety/contraindication data — prevent the standard repurposing evaluation from proceeding. Until these gaps are resolved and the prediction pipeline is re-run, there is no actionable repurposing candidate to assess.

**To proceed, the following is needed:**

- **Resolve DG002 (MOA):** Query the DrugBank API for acebutolol's mechanism of action, pharmacodynamics, and drug targets to populate the MOA field.
- **Resolve DG001 (Safety):** Locate and parse the package insert PDF (if available from TFDA, EMA, or the original US NDA) to extract key warnings and contraindications.
- **Confirm original indications:** Retrieve approved indication text from an authoritative source (e.g., FDA label, DrugBank clinical data) so the pipeline has a valid starting indication to anchor predictions.
- **Investigate prediction pipeline coverage:** Verify whether acebutolol's DrugBank ID (`DB01193`) is present and correctly linked in the TxGNN knowledge graph node list (`data/node.csv`); if absent, add it and re-run `run_kg_prediction.py`.
- **Re-run TxGNN prediction** after the above gaps are resolved to determine whether repurposing candidates emerge.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

