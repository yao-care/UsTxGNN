---
layout: default
title: Pegfilgrastim
parent: 僅模型預測 (L5)
nav_order: 1020
evidence_level: L5
indication_count: 2
---

# Pegfilgrastim
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

# Pegfilgrastim: From [Original Indication Unavailable] to Severe Nonproliferative Diabetic Retinopathy

## One-Sentence Summary

Pegfilgrastim (DrugBank ID: DB00019) is a PEGylated long-acting G-CSF analog; original indication data is currently unavailable in this evidence pack.
The TxGNN model predicts it may be effective for **Severe Nonproliferative Diabetic Retinopathy**,
but this prediction is currently supported by **0 clinical trials** and **0 publications** — it is a model-only inference with no empirical evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (no license data in Taiwan/US regulatory records) |
| Predicted New Indication | Severe Nonproliferative Diabetic Retinopathy |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L5 |
| US Market Status | 未上市 (Not marketed) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in structured form, but based on known pharmacology, pegfilgrastim is a PEGylated long-acting analog of G-CSF (granulocyte colony-stimulating factor). Its established mechanism is stimulating proliferation and differentiation of granulocyte precursor cells in bone marrow, and promoting mobilization of bone marrow stem cells/endothelial progenitor cells (EPCs) into circulation.

The theoretical link to diabetic retinopathy is indirect: EPC mobilization is sometimes associated with vascular repair pathways, which the TxGNN knowledge graph appears to have picked up as a similarity signal. However, this connection runs in a potentially **concerning direction rather than a therapeutic one** — G-CSF's pro-angiogenic properties could theoretically worsen pathological neovascularization in proliferative or severe nonproliferative diabetic retinopathy, rather than treat it. There is no clinical or preclinical evidence supporting a therapeutic hypothesis in this direction; the mechanistic rationale is speculative and the safety direction is ambiguous at best.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## US Market Information

No license/authorization records are available for pegfilgrastim in this evidence pack (market status: 未上市, total licenses: 0).

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: `safety.key_warnings`, `safety.contraindications`, and `safety.ddi` are all marked as Data Gap or not found in this evidence pack — this is a Blocking data gap per DG001, meaning safety evaluation (S1 stage) cannot proceed until TFDA label warnings/contraindications are obtained.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This prediction is L5 evidence level — a model-only inference with zero supporting clinical trials or literature, and the proposed mechanistic link runs against the known pro-angiogenic risk profile of G-CSF agents in a retinal neovascular disease context. There is currently no basis to advance this candidate beyond hypothesis generation.

**To proceed, the following is needed:**
- TFDA (or equivalent) label warnings and contraindications (blocking gap, DG001) before any safety screening can begin
- Documented mechanism of action (MOA) data from DrugBank or primary literature (DG002)
- Preclinical or observational evidence directly evaluating G-CSF/pegfilgrastim in diabetic retinopathy, specifically addressing the theoretical risk of exacerbating pathological neovascularization
- Confirmation of original approved indication(s), which are currently missing from the regulatory record
- Given the potential safety signal (pro-angiogenic mechanism vs. retinal neovascular disease), any future evaluation should explicitly include an ophthalmology/retinal safety risk assessment before considering further development
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

