---
layout: default
title: Acetaminophen Dextromethorphan Hydrobromide Doxyla
parent: 僅模型預測 (L5)
nav_order: 112
evidence_level: L5
indication_count: 0
---

# Acetaminophen Dextromethorphan Hydrobromide Doxyla
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

# Acetaminophen / Dextromethorphan / Doxylamine / Pseudoephedrine: Cold & Flu Combination — Repurposing Assessment

## One-Sentence Summary

This four-component combination (acetaminophen, dextromethorphan HBr, doxylamine succinate, pseudoephedrine) is a classic multi-symptom cold and flu remedy targeting fever, cough, nasal congestion, and sleep disruption.
The TxGNN model was unable to generate a repurposing prediction for this combination — no DrugBank ID is available for the combination as a whole, and the `predicted_indications` array returned empty.
Due to the complete absence of prediction output and multiple critical data gaps in this Evidence Pack, this candidate **cannot be meaningfully evaluated at this time**.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Multi-symptom cold & flu relief (fever, cough, nasal congestion, sleep disruption) |
| Predicted New Indication | None — TxGNN returned no predictions |
| TxGNN Prediction Score | N/A |
| Evidence Level | N/A — No prediction generated |
| US Market Status | Not marketed (as this exact 4-component combination) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

No NDA records were found for this exact four-component combination in the regulatory database.

> **Note:** Each individual component is widely available in the US as an OTC active ingredient — for example, similar combinations are sold under brand names such as NyQuil Severe. The 0-record result reflects the database query finding no registration under this specific multi-ingredient string. A brand-name or NDA-level search may yield results.

---

## Safety Considerations

Please refer to the package insert for safety information.

> This combination contains four pharmacologically active components with distinct and overlapping safety profiles. Key areas warranting review before any repurposing work include:
> - **Doxylamine succinate** (sedating antihistamine): CNS depression risk, additive sedation with other CNS-active agents
> - **Pseudoephedrine** (sympathomimetic decongestant): cardiovascular stimulant effects, hypertension risk, contraindicated in MAO inhibitor users
> - **Dextromethorphan HBr** (NMDA antagonist / σ-1 agonist): serotonin syndrome risk at high doses or with serotonergic drugs
> - **Acetaminophen**: hepatotoxicity risk at overdose or in patients with liver impairment or alcohol use

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
TxGNN returned no repurposing predictions for this entry, and both DrugBank mapping and safety data are absent — the minimum prerequisites for a repurposing evaluation are not met.

**To proceed, the following is needed:**

- **Decompose the combination:** Assign individual DrugBank IDs to each of the four components (acetaminophen, dextromethorphan, doxylamine, pseudoephedrine) and re-run TxGNN predictions on each ingredient separately
- **Identify any brand NDA:** Determine whether a specific brand-name product (e.g., NyQuil Severe, Vicks Formula 44, or equivalent) holds an NDA, and re-query the regulatory database by brand name or active ingredient list
- **Retrieve full prescribing information:** Download FDA-approved labeling (package insert PDF) from FDA.gov to populate key warnings, contraindications, and drug interaction data
- **Clarify analysis scope:** Decide whether the research question targets the combination as a unit (e.g., exploring the DXM component for CNS indications) or individual components — this determines the correct TxGNN query strategy
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

