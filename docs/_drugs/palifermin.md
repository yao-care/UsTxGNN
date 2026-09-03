---
layout: default
title: Palifermin
parent: 僅模型預測 (L5)
nav_order: 1009
evidence_level: L5
indication_count: 6
---

# Palifermin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Palifermin: From Severe Oral Mucositis to Primary Platelet Release Disorder

## One-Sentence Summary

> Palifermin (recombinant human keratinocyte growth factor) was originally used to prevent severe oral mucositis in patients with hematologic malignancies undergoing myelotoxic therapy.
> The TxGNN model predicts it may be effective for **Primary Release Disorder of Platelets**,
> but currently only **1 clinical trial** (indirectly relevant) and **no dedicated publications** support this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Severe oral mucositis in patients with hematologic malignancies receiving myelotoxic therapy (based on known drug profile; not captured in the current regulatory dataset) |
| Predicted New Indication | Primary Release Disorder of Platelets |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L4 |
| Taiwan Market Status | 未上市 (Not marketed) |
| Number of Licenses | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, structured mechanism of action data is not available in this evidence pack. Based on known pharmacology, palifermin is a recombinant human keratinocyte growth factor (rhKGF/FGF7) that binds FGFR2b to promote epithelial cell proliferation and mucosal repair. Its efficacy in reducing severe oral mucositis in patients undergoing myelotoxic therapy for hematologic malignancies (including hematopoietic stem cell transplantation) is well established.

The only supporting clinical trial identified (NCT06859424) is a platform study evaluating post-transplant cyclophosphamide-based GVHD prophylaxis in mismatched unrelated donor peripheral blood stem cell transplant recipients — a population where palifermin may appear as supportive mucositis prophylaxis, not as a therapy directed at platelet release function. The overlap between the original indication and the predicted indication is therefore driven by **shared patient population** (hematologic malignancy / transplant recipients), not by a shared pharmacological mechanism.

Mechanistically, the KGF–FGFR2b epithelial repair pathway has no established connection to platelet granule release physiology, which underlies primary platelet release disorder. The evidence pack's own rationale explicitly flags this as an indirect/co-occurrence association rather than direct therapeutic evidence, and the trial's relevance grade is rated "C" (population overlap only, mechanism unrelated).

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06859424](https://clinicaltrials.gov/study/NCT06859424) | Phase 2 | Recruiting | 358 | Platform trial comparing GVHD prophylaxis drug combinations after mismatched unrelated donor PBSC transplant; palifermin, if used, would serve as supportive mucositis prophylaxis rather than a platelet-directed therapy (relevance grade: C) |

---

## Literature Evidence

Currently no related literature available.

---

## Taiwan Market Information

Palifermin is not currently marketed in Taiwan (0 authorizations on file; market status: 未上市).

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: TFDA label warnings/contraindications are flagged as a Blocking data gap — see Conclusion below.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction sits at Evidence Level L4, supported only by a single clinical trial with grade-C (indirect/population-overlap) relevance and no dedicated literature. No mechanistic link between the KGF/FGFR2b epithelial repair pathway and platelet granule release function has been established. All five other predicted indications in this pack (Glanzmann thrombasthenia, pseudo-von Willebrand disease, constitutional thrombocytopenia, collagen receptor defect bleeding diathesis, Scott syndrome) are Evidence Level L5 — model prediction only, with no supporting trials or literature.

**To proceed, the following is needed:**
- TFDA label warnings/contraindications (Blocking gap, DG001)
- Structured DrugBank MOA data (High-priority gap, DG002)
- Preclinical/mechanistic studies directly linking FGF/KGF signaling to platelet biology
- Dedicated clinical evidence in platelet release disorder populations, rather than incidental co-occurrence in transplant/GVHD trials
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

