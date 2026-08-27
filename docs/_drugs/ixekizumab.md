---
layout: default
title: Ixekizumab
parent: 僅模型預測 (L5)
nav_order: 823
evidence_level: L5
indication_count: 10
---

# Ixekizumab
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

# Ixekizumab: From Psoriatic Arthritis / Axial Spondyloarthritis to Rheumatoid Vasculitis

## One-Sentence Summary

Ixekizumab is an IL-17A-targeting monoclonal antibody; the clinical trial and literature evidence embedded in this pack show it is an established treatment for psoriatic arthritis and axial spondyloarthritis (Taltz), though no TFDA-approved indication text is available because the drug is **not yet marketed in Taiwan**. The TxGNN model's top-ranked prediction is **Rheumatoid Vasculitis**, but this is currently supported by only **1 clinical trial** (indirect relevance, not yet recruiting) and **0 publications** — evidence is minimal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available from Taiwan regulatory data (未上市). Based on trial/literature evidence in this pack, ixekizumab (IL-17A inhibitor) is established for psoriatic arthritis and axial spondyloarthritis |
| Predicted New Indication | Rheumatoid Vasculitis |
| TxGNN Prediction Score | 97.53% |
| Evidence Level | L5 |
| Taiwan Market Status | 未上市 (Not Marketed) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (drug.original_moa = Data Gap). Based on evidence embedded elsewhere in this pack, ixekizumab is a high-affinity monoclonal antibody that selectively neutralizes interleukin-17A (IL-17A), a cytokine central to the pathogenesis of psoriasis, psoriatic arthritis, and axial spondyloarthritis — indications with extensive Phase 3 trial support (see the "vertebral disease" / "inflammatory spondylopathy" evidence below).

For the top-ranked candidate, **rheumatoid vasculitis**, the evidence pack's own rationale states that "IL-17A's role in rheumatoid vasculitis lacks clear literature support; existing RV pathology centers on immune-complex deposition and TNF/B-cell pathways, and the causal link to IL-17A inhibition is weak — this is a KG score-driven hypothesis" rather than an established mechanistic connection. Only one indirectly-relevant, not-yet-recruiting Phase 2 trial (NCT07138898, on perioperative immunosuppressant management in shoulder arthroplasty, grade C relevance) exists, and no supporting literature was found.

**Data quality caveat**: Several other high-scoring candidates in this pack (e.g., "inflammatory spondylopathy" rank 6, "vertebral disease" rank 9) show strong L1/Phase-3-level evidence, but their own rationale text flags that these are very likely **already-approved indications** (axSpA/PsA) surfacing as "novel predictions" only because `drug.original_indications` is empty in this dataset — not genuine repurposing opportunities. This should be corrected at the data source before further use.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT07138898](https://clinicaltrials.gov/study/NCT07138898) | Phase 2 | Not Yet Recruiting | 80 | Assesses rheumatologic flares, pain/functional outcomes, and surgical complications in rheumatology patients undergoing shoulder arthroplasty, comparing preoperative immunosuppressant-holding strategies; not a direct ixekizumab-in-RV efficacy trial (relevance grade C, indirect) |

---

## Literature Evidence

Currently no related literature available.

---

## Taiwan Market Information

Ixekizumab currently has no TFDA drug license on record (0 NDAs; market status: 未上市/Not Marketed).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence for ixekizumab in rheumatoid vasculitis is at the model-prediction-only stage (L5) — a single indirect, not-yet-recruiting trial and no supporting literature. The mechanistic rationale itself is described as weak and KG-score-driven rather than biologically established.

**To proceed, the following is needed:**
- TFDA package insert / warnings and contraindications (currently blocking — DG001)
- DrugBank-confirmed mechanism of action (currently High-severity gap — DG002)
- A confirmed, TFDA-independent record of ixekizumab's actual approved indications (drug.original_indications is empty, which is also causing already-approved indications like axSpA/PsA to misleadingly appear as "predictions")
- Mechanistic or preclinical evidence specifically linking IL-17A inhibition to rheumatoid vasculitis pathology
- At minimum one enrolling/completed clinical trial directly testing ixekizumab in rheumatoid vasculitis before advancing past Hold
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

