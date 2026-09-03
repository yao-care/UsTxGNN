---
layout: default
title: Ranibizumab
parent: 僅模型預測 (L5)
nav_order: 1109
evidence_level: L5
indication_count: 10
---

# Ranibizumab
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

# Ranibizumab: From Neovascular Age-Related Macular Degeneration to Severe Nonproliferative Diabetic Retinopathy

## One-Sentence Summary

> Ranibizumab is an anti-VEGF Fab fragment originally developed for neovascular (wet) age-related macular degeneration and diabetic macular edema.
> The TxGNN model predicts it may also be effective for **Severe Nonproliferative Diabetic Retinopathy (NPDR)**,
> with **6 clinical trials** (including completed Phase 3/4 studies) and **19 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on local regulatory record (market status: Not Marketed); internationally approved for neovascular (wet) age-related macular degeneration and diabetic macular edema |
| Predicted New Indication | Severe Nonproliferative Diabetic Retinopathy |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L1 |
| US Market Status | ✗ Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack (flagged as a High-severity data gap pending DrugBank verification). Based on established pharmacological knowledge, ranibizumab is a recombinant humanized monoclonal antibody Fab fragment that binds and neutralizes vascular endothelial growth factor A (VEGF-A), thereby suppressing pathological retinal neovascularization and vascular permeability.

Severe NPDR and the drug's established indications (wet AMD, diabetic macular edema) sit on the same disease continuum: VEGF-driven retinal vascular dysfunction. Severe NPDR is the immediate precursor stage to proliferative diabetic retinopathy (PDR) and frequently coexists with diabetic macular edema, the condition ranibizumab is already used to treat. This is not a cross-mechanism extrapolation — it is a direct extension of the drug's core anti-VEGF activity to an earlier stage of the same underlying vascular pathology.

This mechanistic plausibility is reinforced by late-phase clinical development already underway: a completed Phase 3 trial of the Port Delivery System with ranibizumab specifically in NPDR without macular edema (NCT04503551, completed 2026), and the 2025 Pavilion RCT (PMID 40048178) comparing continuous intraocular ranibizumab release against monitoring alone in NPDR. Taken together, the evidence suggests severe NPDR is a plausible and actively investigated label-extension candidate rather than a speculative model artifact.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02834663](https://clinicaltrials.gov/study/NCT02834663) | Phase 4 | Completed | 25 | Intravitreal ranibizumab effects on microaneurysm turnover and non-perfused retinal area in NPDR with DME |
| [NCT00444600](https://clinicaltrials.gov/study/NCT00444600) | Phase 3 | Completed | 691 | Large RCT: ranibizumab ± laser vs triamcinolone ± laser for diabetic macular edema |
| [NCT02634333](https://clinicaltrials.gov/study/NCT02634333) | Phase 3 | Completed | 399 | Anti-VEGF therapy for prevention of vision-threatening complications in high-risk diabetic retinopathy |
| [NCT03452657](https://clinicaltrials.gov/study/NCT03452657) | Phase 3 | Unknown | 118 | Intravitreous ranibizumab vs sham for prevention of high-risk DR progression |
| [NCT05222633](https://clinicaltrials.gov/study/NCT05222633) | N/A | Unknown | 1000 | Real-world observational study of anti-VEGF therapy across neovascular retinal diseases (includes PDR) |
| [NCT04503551](https://clinicaltrials.gov/study/NCT04503551) | Phase 3 | Completed | 174 | Port Delivery System with ranibizumab in diabetic retinopathy without center-involved macular edema |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40048178](https://pubmed.ncbi.nlm.nih.gov/40048178/) | 2025 | RCT | JAMA Ophthalmology | Pavilion trial: Port Delivery System with ranibizumab vs monitoring in NPDR without macular edema |
| [39673354](https://pubmed.ncbi.nlm.nih.gov/39673354/) | 2024 | Systematic Review/Meta-analysis | Health Technology Assessment | Anti-VEGF drugs vs laser photocoagulation for diabetic retinopathy |
| [40347224](https://pubmed.ncbi.nlm.nih.gov/40347224/) | 2025 | Systematic Review/Economic Analysis | Health Technology Assessment | Anti-VEGF vs laser photocoagulation for DR, including economic evaluation |
| [36774994](https://pubmed.ncbi.nlm.nih.gov/36774994/) | 2023 | RCT (post-hoc) | Ophthalmology Retina | Baseline DR severity predicts time to DME resolution with ranibizumab in Phase 3 trials |
| [30234859](https://pubmed.ncbi.nlm.nih.gov/30234859/) | 2018 | RCT (DRCR.net Protocol I, 5-yr) | Retina | Changes in diabetic retinopathy severity with ranibizumab treatment for DME |
| [28448655](https://pubmed.ncbi.nlm.nih.gov/28448655/) | 2017 | RCT (secondary analysis) | JAMA Ophthalmology | 2-year change in DR severity comparing aflibercept, bevacizumab, and ranibizumab |
| [32606578](https://pubmed.ncbi.nlm.nih.gov/32606578/) | 2020 | RCT (post-hoc, RIDE/RISE) | Clinical Ophthalmology | Predictors of early diabetic retinopathy regression with ranibizumab |
| [35417296](https://pubmed.ncbi.nlm.nih.gov/35417296/) | 2022 | RCT (post-hoc, RIDE/RISE) | Ophthalmic Surgery, Lasers & Imaging Retina | Natural course of DR progression in untreated fellow eyes |
| [36161830](https://pubmed.ncbi.nlm.nih.gov/36161830/) | 2022 | RCT (open-label extension, RIDE/RISE) | BMJ Open Ophthalmology | Effect of less frequent ranibizumab dosing on DR Severity Scale scores |
| [33966556](https://pubmed.ncbi.nlm.nih.gov/33966556/) | 2021 | Review | Expert Opinion on Biological Therapy | Overview of ranibizumab's role in treating diabetic retinopathy |

---

## US Market Information

Currently not marketed in this jurisdiction — no license records are on file (total_licenses = 0).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Severe NPDR represents an L1 evidence-level candidate — supported by multiple completed Phase 3 RCTs and systematic reviews — with a mechanistic link to ranibizumab's existing anti-VEGF activity so direct it amounts to a natural extension along the diabetic retinopathy severity spectrum rather than a novel mechanistic hypothesis. However, this jurisdiction currently has no marketing authorization, formal MOA documentation, or label safety data on file for this drug.

**To proceed, the following is needed:**
- TFDA/local label warnings and contraindications (currently blocking — DG001)
- Formal MOA documentation via DrugBank API (DG002)
- Regulatory pathway assessment given the drug is not currently marketed locally
- Safety monitoring plan for repeat intravitreal dosing in an NPDR population (endophthalmitis, intraocular pressure, thromboembolic risk)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

