---
layout: default
title: Tivozanib
parent: 僅模型預測 (L5)
nav_order: 1235
evidence_level: L5
indication_count: 10
---

# Tivozanib
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# TIVOZANIB: From Renal Cell Carcinoma to Endocervical Carcinoma

## One-Sentence Summary

> Tivozanib is a highly selective VEGFR-1/2/3 tyrosine kinase inhibitor originally approved for renal cell carcinoma.
> The TxGNN model predicts it may be effective for **Endocervical Carcinoma**,
> with **0 clinical trials** and **0 publications** currently supporting this direction — this is a pure model prediction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Renal Cell Carcinoma (per known approval history; no local license record available) |
| Predicted New Indication | Endocervical Carcinoma |
| TxGNN Prediction Score | 99.81% |
| Evidence Level | L5 |
| US Market Status | Not Marketed (未上市) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, structured mechanism-of-action data is not available in the evidence pack (flagged as a data gap). However, the repurposing rationale indicates that tivozanib is a highly selective VEGFR-1/2/3 tyrosine kinase inhibitor already approved for renal cell carcinoma, acting through inhibition of angiogenesis.

The proposed link to endocervical carcinoma rests on the general biological plausibility that anti-angiogenic therapy can be active across VEGF-driven tumor types — an analogy drawn to bevacizumab's established role in cervical cancer. However, this rationale is not specific to endocervical adenocarcinoma, and no direct clinical or preclinical evidence exists for this particular histologic subtype.

For the remaining nine candidates (ranks 2–10, all rare uterine ligament/cervical adenocarcinoma variants), the evidence pack explicitly notes that these are extremely rare tumor entities with no biomarker, epidemiological, or treatment-response literature — the association derives solely from knowledge-graph embedding similarity, not biological validation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

Tivozanib currently has **no marketing authorization records** in this jurisdiction (market status: 未上市 / Not Marketed; total licenses: 0). No license table can be generated from available data.

---

## Cytotoxicity

Tivozanib is an antineoplastic agent (VEGFR-1/2/3 tyrosine kinase inhibitor, approved for renal cell carcinoma), so this section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (VEGFR tyrosine kinase inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All 10 predicted indications are supported only by TxGNN model scores (L5 evidence) with zero clinical trials or literature. Additionally, a Blocking data gap exists for local warnings/contraindications (DG001), and the drug is not currently marketed in this jurisdiction, preventing any safety pre-screening (S1).

**To proceed, the following is needed:**
- Local (e.g., TFDA) label PDF with warnings, contraindications, and precautions (resolve DG001)
- Structured mechanism-of-action data via DrugBank API (resolve DG002)
- Primary literature or preclinical data specifically evaluating VEGFR inhibition in endocervical/cervical adenocarcinoma subtypes
- Confirmation of drug availability/import pathway given current "not marketed" status
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

