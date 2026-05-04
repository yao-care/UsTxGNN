---
layout: default
title: Acetaminophen Dexbrompheniramine
parent: 僅模型預測 (L5)
nav_order: 109
evidence_level: L5
indication_count: 0
---

# Acetaminophen Dexbrompheniramine
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

# Acetaminophen + Dexbrompheniramine: From Cold & Allergy Relief to [No TxGNN Predictions Available]

## One-Sentence Summary

Acetaminophen is a widely used analgesic and antipyretic; dexbrompheniramine is a first-generation H1 antihistamine. Together, this fixed-dose combination is typically used to relieve symptoms of the common cold and seasonal allergies (e.g., runny nose, sneezing, minor aches, and fever).

The TxGNN model returned **no predicted new indications** for this combination, and the drug is **not currently marketed in the United States**. Without active TxGNN predictions and with multiple blocking data gaps, a formal repurposing analysis cannot be completed at this stage.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Cold & allergy symptom relief (analgesic + antihistamine combination; not formally recorded in this Evidence Pack) |
| Predicted New Indication | None — TxGNN returned no predictions |
| TxGNN Prediction Score | N/A |
| Evidence Level | L5 (no predictions, no supporting studies identified) |
| US Market Status | Not marketed |
| Number of NDAs | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

No TxGNN repurposing prediction was generated for this drug combination. Therefore, a mechanism-based justification for a new indication cannot be provided at this time.

For reference, the two components have distinct pharmacological profiles:

- **Acetaminophen** acts centrally to inhibit prostaglandin synthesis and modulate descending serotonergic pain pathways. It is one of the most broadly used analgesics and antipyretics globally.
- **Dexbrompheniramine** is the active dextrorotatory enantiomer of brompheniramine and competitively blocks peripheral H1 histamine receptors, reducing allergic and cold-related symptoms such as rhinorrhea and sneezing.

Currently, detailed mechanism of action data is not available from this Evidence Pack. To support a future repurposing hypothesis for this combination, DrugBank API data (remediation flagged as DG002) should be retrieved to populate the full MOA profile.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for this combination as a repurposing candidate.

---

## Literature Evidence

Currently no related literature available for this combination as a repurposing candidate.

---

## US Market Information

This drug combination holds **no US NDA approvals** on record in this Evidence Pack. It is classified as **not marketed** in the United States.

Note: Individual components (acetaminophen and dexbrompheniramine) are available in various OTC products in the US (e.g., Dimetapp Cold & Allergy, Alka-Seltzer Plus), but the specific combination as a fixed-dose prescription or OTC product has no documented NDA entry in this dataset.

---

## Safety Considerations

Please refer to the package insert for safety information.

> The Evidence Pack contains no safety data for this combination. Two data gaps have been flagged as requiring remediation before safety assessment can proceed:
>
> - **DG001 (Blocking)** — TFDA prescribing information (warnings/contraindications) has not been retrieved. This must be resolved before the S1 safety screen can be initiated.
> - **DG002 (High)** — Mechanism of action data from DrugBank is missing, which limits mechanistic risk assessment.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model produced no repurposing predictions for this combination, and both critical safety and MOA data are absent. There is currently no actionable signal to evaluate.

**To proceed, the following is needed:**

- **Resolve DG001 (Blocking):** Download and parse the TFDA package insert PDF to populate warnings and contraindications — this is required before any safety screen.
- **Resolve DG002 (High):** Query the DrugBank API for both acetaminophen and dexbrompheniramine to retrieve full MOA data, enabling mechanistic analysis.
- **Re-run TxGNN prediction:** Verify whether the query was submitted correctly (the drug INN contains a semicolon separator — confirm the pipeline correctly handles combination drug entries). If the combination was not recognized as a valid entity, query each component individually.
- **Confirm drug identity:** The `drugbank_id` field is null; map each component to its respective DrugBank ID (e.g., acetaminophen → DB00316, dexbrompheniramine → DB01246) to enable downstream evidence collection.
- Once the above steps are complete, re-generate the Evidence Pack and re-evaluate.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

