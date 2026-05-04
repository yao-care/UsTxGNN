---
layout: default
title: Acalabrutinib
parent: 僅模型預測 (L5)
nav_order: 61
evidence_level: L5
indication_count: 0
---

# Acalabrutinib
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

# Acalabrutinib: BTK Inhibitor — No TxGNN Repurposing Predictions Available

## One-Sentence Summary

Acalabrutinib (Calquence) is a second-generation Bruton's tyrosine kinase (BTK) inhibitor approved by the US FDA for Chronic Lymphocytic Leukemia (CLL/SLL) and Mantle Cell Lymphoma (MCL).
The current Evidence Pack (v4, data cutoff 2026-04-19) returned **no TxGNN repurposing predictions**, which means no candidate new indications can be evaluated at this time.
The pipeline is incomplete — key inputs including MOA data and regulatory data are missing — and this report serves as a **data gap summary** rather than a full repurposing evaluation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Chronic Lymphocytic Leukemia / Mantle Cell Lymphoma (US FDA approved; not registered in Taiwan) |
| Predicted New Indication | None — Evidence Pack returned no predictions |
| TxGNN Prediction Score | N/A |
| Evidence Level | N/A (pipeline did not complete) |
| US Market Status | Not marketed in Taiwan (未上市) |
| Number of Taiwan Licenses | 0 |
| Recommended Decision | **Hold** — rerun pipeline after resolving data gaps |

---

## Why Is No Prediction Available?

The TxGNN pipeline requires at least one validated drug–disease link from the regulatory data source to anchor a prediction. Because Acalabrutinib has **zero TFDA licenses**, the local regulatory layer returned no approved indications, leaving the knowledge graph without a starting node for this drug.

Additionally, two upstream data gaps were flagged before prediction even began:

1. **MOA data is missing** — DrugBank API was queried successfully (result count = 1), but the mechanism of action field was not populated in the Evidence Pack. Without this, the mechanistic plausibility module cannot run.
2. **TFDA package insert warnings/contraindications are missing** — the safety pre-screening step (S1 Safety Gate) was blocked before any candidate could be evaluated.

Until these two blockers are resolved, no repurposing candidates will flow through the pipeline.

---

## US Market Information

Acalabrutinib has **no Taiwan FDA registrations**. The drug is marketed globally as **Calquence** (AstraZeneca) and is approved by the US FDA, EMA, and several other regulators for haematological malignancies, but has not obtained TFDA approval as of the data cutoff.

No license table is shown because there are no entries to display.

---

## Safety Considerations

No safety data was available in the current Evidence Pack (key warnings, contraindications, and drug–drug interactions were all unresolved). Please refer to the Calquence US prescribing information and EMA SmPC for current safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Evidence Pack is structurally incomplete — the TxGNN prediction step never ran because the drug has no local regulatory anchor and upstream data gaps blocked the safety gate. There is nothing to evaluate at this stage.

**To proceed, the following is needed:**

- **[Blocking — DG001]** Download the TFDA package insert PDF for Calquence (or a generic/imported equivalent if one exists) and parse warnings and contraindications; alternatively, use the US FDA label as a proxy to unblock the safety gate
- **[High — DG002]** Resolve the MOA data gap by querying the DrugBank API directly for DB11703 and extracting the mechanism of action text (Acalabrutinib is a covalent BTK inhibitor — this data exists in DrugBank and should be retrievable)
- **[Pipeline]** Once MOA and safety data are populated, rerun the full TxGNN pipeline; the drug has a well-characterised B-cell signalling mechanism that may generate predictions in autoimmune, inflammatory, or other haematological indications
- **[Regulatory]** Confirm whether any parallel import or clinical trial IND application exists under TFDA that might provide a local regulatory anchor for the prediction model
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

