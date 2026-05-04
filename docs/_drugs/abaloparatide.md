---
layout: default
title: Abaloparatide
parent: 僅模型預測 (L5)
nav_order: 40
evidence_level: L5
indication_count: 4
---

# Abaloparatide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Abaloparatide (DB05084): Drug Repurposing Evaluation — Pending TxGNN Prediction

## One-Sentence Summary

Abaloparatide is a synthetic parathyroid hormone-related protein (PTHrP) analog, known from published literature to be used in the treatment of osteoporosis in postmenopausal women at high risk for fracture. The current Evidence Pack contains **no TxGNN repurposing predictions** for this candidate, and two critical data gaps — mechanism of action and safety profile — remain unresolved. A full repurposing evaluation cannot proceed until these gaps are addressed and predictions are generated.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Osteoporosis in postmenopausal women at high risk for fracture *(based on published knowledge; not captured in Evidence Pack)* |
| Predicted New Indication | No prediction available |
| TxGNN Prediction Score | N/A |
| Evidence Level | L5 — No repurposing prediction generated; no linked studies |
| US Market Status | Not marketed *(per Evidence Pack; contradicts known FDA approval — see note below)* |
| Number of NDAs | 0 *(per Evidence Pack)* |
| Recommended Decision | **Hold** |

> **Data Note**: The Evidence Pack records 0 licenses and "未上市" (not marketed). However, Abaloparatide (Tymlos®) received US FDA approval (NDA 208743) in April 2017. This discrepancy suggests a data retrieval issue in the regulatory query pipeline, not an actual absence of approval. This must be corrected before regulatory-based assessment can proceed.

---

## Why is This Prediction Reasonable?

No repurposing prediction is currently available for Abaloparatide from the TxGNN model, so a mechanism-to-indication rationale cannot be formally evaluated at this stage.

Currently, detailed mechanism of action data is not available in the Evidence Pack. Based on published knowledge, Abaloparatide is a 34-amino-acid PTHrP analog that acts as a selective agonist at the PTH1 receptor (PTH1R). It preferentially activates the cAMP/PKA signaling pathway over the PKC pathway, thereby stimulating osteoblast-mediated bone formation while producing less hypercalcemia than full PTH agonists. This anabolic bone mechanism is the basis for its use in postmenopausal osteoporosis.

Mechanistically, PTH1R signaling plays roles beyond bone metabolism — it is expressed in kidney, vascular tissue, and cartilage — creating a plausible biological basis for potential repurposing into conditions such as hypoparathyroidism, fracture healing acceleration, or select metabolic bone disorders. However, no TxGNN-derived prediction currently defines a specific repurposing target for formal evaluation.

---

## Clinical Trial Evidence

Currently no related clinical trials are registered for a repurposing indication — no predicted indication is available from the TxGNN pipeline to anchor an evidence search.

---

## Literature Evidence

Currently no related literature is available for a repurposing indication — evidence collection is pending generation of a TxGNN repurposing target.

---

## US Market Information

No marketing authorization records were returned in the current Evidence Pack.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|----------------------|--------------|-------------|---------------------|
| *(not captured)* | *(not captured)* | *(not captured)* | *(not captured)* |

> **Action Required**: The regulatory query returned 0 results, which conflicts with known FDA approval status. The pipeline should re-query the FDA database for NDA 208743 (Tymlos®, abaloparatide 80 mcg/dose subcutaneous injection) and re-run the regulatory ingestion step.

---

## Safety Considerations

Please refer to the package insert for safety information.

> Both safety data items (key warnings and contraindications) are flagged as data gaps with **Blocking** severity. The DDI query also returned no results. No safety assessment can be conducted until the package insert is retrieved and parsed (see DG001 below).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN pipeline has produced no repurposing predictions for Abaloparatide in this Evidence Pack version, and both safety and mechanism data are missing — making a repurposing evaluation impossible at this stage. All three pillars of evaluation (efficacy signal, mechanism plausibility, and safety profile) are currently unresolvable.

**To proceed, the following is needed:**

- **DG001 (Blocking)** — Retrieve and parse the FDA package insert PDF for Abaloparatide to extract key warnings, contraindications, and boxed warnings; this is the single highest priority item before any safety-gated decision
- **DG002 (High)** — Query the DrugBank API for DB05084 to retrieve the confirmed mechanism of action (PTH1R agonist pathway) and pharmacological categories
- **Regulatory pipeline fix** — Re-run the FDA regulatory query; confirm NDA 208743 (Tymlos®) is correctly ingested; update `market_status` and `licenses` fields accordingly
- **TxGNN re-run** — After data gaps are resolved, re-execute the TxGNN prediction pipeline for DB05084 to generate top-ranked repurposing candidates
- **Evidence collection** — Once a predicted indication is confirmed, trigger clinical trial (ClinicalTrials.gov / ICTRP) and literature (PubMed) collection for that target
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

