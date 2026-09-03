---
layout: default
title: Plerixafor
parent: 僅模型預測 (L5)
nav_order: 1056
evidence_level: L5
indication_count: 7
---

# Plerixafor
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

Using the report-writing instructions in the prompt (no additional skill needed for this content-generation task) — drafting the report directly from the Evidence Pack.

# Plerixafor: From Stem Cell Mobilization to Indolent Plasma Cell Myeloma

## One-Sentence Summary

Plerixafor (DrugBank DB06809) is a CXCR4 antagonist whose established clinical use — evident throughout the trial evidence in this pack — is mobilizing hematopoietic stem cells for transplantation. The TxGNN model's top-ranked prediction is **Indolent Plasma Cell Myeloma**, but this specific candidate is currently supported by **0 clinical trials** and **0 publications** — it is a pure model-driven hypothesis with no direct evidence yet.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no NDA/license on file for this jurisdiction (0 licenses); structured original-indication data is a documented gap |
| Predicted New Indication | Indolent Plasma Cell Myeloma |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action data for plerixafor is not available in structured form (flagged as a High-severity Data Gap, DG002). However, the trial evidence collected elsewhere in this pack consistently describes plerixafor as a **CXCR4 antagonist** that blocks the SDF-1α/CXCL12–CXCR4 axis, disrupting how blood and marrow cells are retained ("homed") within bone marrow niches — this is the mechanism repeatedly cited across the myeloid leukemia trial set (e.g., NCT01319864, PMID 22308295).

Plerixafor's well-documented clinical role, evident from trial descriptions in this pack, is mobilizing hematopoietic stem cells out of the bone marrow niche prior to autologous or allogeneic transplantation. The rationale for extending this to indolent plasma cell myeloma is that the **same CXCR4/CXCL12 axis governs plasma cell homing and survival within the bone marrow** — the malignant plasma cell's natural microenvironment. In theory, CXCR4 blockade could mobilize marrow-resident plasma cells and increase their sensitivity to concurrent therapy, mirroring the "chemosensitization via mobilization" strategy already tested extensively for AML (rank 7 in this pack, with 30 trials and 20 publications).

That said, this mechanistic link for indolent plasma cell myeloma is currently **theoretical only** — it has not been tested in any registered trial or published study, unlike the analogous AML hypothesis, which has substantial clinical evidence. This gap between mechanistic plausibility and actual evidence is the central caveat for this candidate.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

Plerixafor currently holds no license/NDA record in this jurisdiction (`market_status`: Not Marketed; `total_licenses`: 0). No product/dosage form data is available.

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug interaction data are not currently available in this pack — DG001, Blocking severity, marked as required for TFDA label sourcing before any S1 safety evaluation can proceed.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication (Indolent Plasma Cell Myeloma) is supported only by a TxGNN score and a mechanistic hypothesis — no clinical trials or literature exist to substantiate it (Evidence Level L5). Combined with the Blocking-severity gap in TFDA safety/label data (DG001), this candidate cannot advance past S0.

**To proceed, the following is needed:**
- TFDA/label safety data (warnings, contraindications) — Blocking gap, required before any S1 safety screen
- Formal mechanism-of-action documentation (DG002)
- At minimum, preclinical or case-level evidence directly linking plerixafor to plasma cell myeloma before this candidate can be re-scored
- **Portfolio note:** Rank 7 (Myeloid Leukemia) in this same pack has 30 clinical trials (including completed Phase 1/2 studies, e.g., NCT00906945, NCT01352650) and 20 publications on CXCR4-antagonist chemosensitization — this is a substantially stronger candidate and may warrant its own evaluation ahead of the plasma cell myeloma hypothesis.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

