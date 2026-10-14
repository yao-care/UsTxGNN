---
layout: default
title: Ranibizumab
parent: Model Prediction Only (L5)
nav_order: 1109
evidence_level: L5
indication_count: 10
---

# Ranibizumab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Ranibizumab: From Diabetic Retinopathy and Macular Degeneration to Severe Nonproliferative Diabetic Retinopathy

## One-Sentence Summary

Ranibizumab is an anti-VEGF antibody fragment, originally used for retinal diseases such as macular degeneration and diabetic macular edema.
The TxGNN model predicts it may be effective for **severe nonproliferative diabetic retinopathy**,
with **0 registered clinical trials** and **19 publications** currently supporting this direction. The prediction is largely adjacent to an existing indication (diabetic retinopathy is already among the original indications), so it is closer to an indication extension than a true repurposing.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Diabetic retinopathy, macular degeneration, diabetic macular edema, retinopathy of prematurity and related retinal diseases (approved indication text is not available in the US license records) |
| Predicted New Indication | Severe nonproliferative diabetic retinopathy |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L1 (based on literature only; see note below) |
| US Market Status | Cancelled only (all 4 licenses listed as cancelled) |
| Number of NDAs | 4 (BLA licenses) |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known information, ranibizumab is an anti-VEGF antibody fragment. VEGF drives retinal vascular permeability and neovascularization in diabetic retinopathy, and VEGF levels are elevated in the vitreous and serum of affected eyes. This is a direct mechanistic match.

Diabetic retinopathy is already among the drug's original indications, so severe nonproliferative disease is a more specific stage of a condition the drug is already linked to. Post hoc analyses of the RIDE/RISE Phase 3 trials report regression of retinopathy severity with ranibizumab. The ranibizumab Port Delivery System has also been studied in nonproliferative diabetic retinopathy without macular edema (the PAVILION randomized trial, published 2025).

**Evidence-level caveat:** The clinical trial registry data compiled for this report contain no trials for this indication. The L1 grading therefore relies on literature titles only, and the primary trial reports should be verified before the grade is relied upon.

## Clinical Trial Evidence

Currently no related clinical trials registered in the data compiled for this report. The evidence comes from published literature, including reports of RIDE/RISE, DRCR.net Protocol I and PAVILION.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40048178](https://pubmed.ncbi.nlm.nih.gov/40048178/) | 2025 | RCT (Phase 3) | JAMA Ophthalmology | PAVILION: Port Delivery System with ranibizumab vs monitoring in nonproliferative diabetic retinopathy without macular edema |
| [32606578](https://pubmed.ncbi.nlm.nih.gov/32606578/) | 2020 | Post hoc analysis of RCT | Clinical Ophthalmology | Predictors of early diabetic retinopathy regression with ranibizumab in RIDE/RISE |
| [36774994](https://pubmed.ncbi.nlm.nih.gov/36774994/) | 2023 | Post hoc analysis / meta-analysis | Ophthalmology Retina | Baseline retinopathy severity and time to macular edema resolution with ranibizumab in Phase 3 trials |
| [28427069](https://pubmed.ncbi.nlm.nih.gov/28427069/) | 2017 | Review of RCT | Developments in Ophthalmology | Lessons from DRCR.net Protocol I (ranibizumab with prompt or deferred laser vs triamcinolone vs sham) |
| [33966556](https://pubmed.ncbi.nlm.nih.gov/33966556/) | 2021 | Review | Expert Opinion on Biological Therapy | Ranibizumab is effective in diabetic retinopathy, including diabetic macular edema |
| [42219053](https://pubmed.ncbi.nlm.nih.gov/42219053/) | 2026 | Systematic review / meta-analysis | European Journal of Pharmacology | Sustained ranibizumab port delivery in diabetic retinopathy and diabetic macular edema |
| [40347224](https://pubmed.ncbi.nlm.nih.gov/40347224/) | 2025 | Systematic review and economic analysis | Health Technology Assessment | Anti-VEGF drugs compared with laser photocoagulation for diabetic retinopathy |
| [39673354](https://pubmed.ncbi.nlm.nih.gov/39673354/) | 2025 | Systematic review / meta-analysis | Health Technology Assessment | Anti-VEGF drugs compared with laser photocoagulation for diabetic retinopathy |
| [36161830](https://pubmed.ncbi.nlm.nih.gov/36161830/) | 2022 | Open-label extension analysis | BMJ Open Ophthalmology | Effect of less frequent ranibizumab on retinopathy severity scale scores in RIDE/RISE |
| [28448655](https://pubmed.ncbi.nlm.nih.gov/28448655/) | 2017 | Secondary analysis of RCT | JAMA Ophthalmology | Change in diabetic retinopathy through 2 years with aflibercept, bevacizumab and ranibizumab |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| BLA125156 | LUCENTIS (Genentech) | Injection, solution | Not available (status: cancelled) |
| BLA761197 | Susvimo (Genentech) | Injection, solution | Not available (status: cancelled) |
| BLA761165 | CIMERLI (Sandoz) | Injection, solution | Not available (status: cancelled) |
| BLA761202 | Byooviz (Harrow Eye) | Injection, solution | Not available (status: cancelled) |

## Safety Considerations

- **Contraindications (from the knowledge graph, not label text):** eye infectious disease and conjunctivitis.
- **Related safety signal in the literature:** a case report describes capsular block syndrome after an intravitreal ranibizumab injection (PMID 38476863).

Package insert warnings and drug interaction data were not available in the data compiled for this report. Please refer to the package insert for full safety information.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Ranibizumab has a direct mechanistic fit for diabetic retinopathy, and the literature includes a Phase 3 randomized trial (PAVILION) plus RIDE/RISE and DRCR.net analyses. However, no registered trials were found in the compiled data, the indication is already close to the original one, and package insert safety data and US market status (all licenses cancelled) are unresolved.

**To proceed, the following is needed:**
- Verify the primary reports of PAVILION and RIDE/RISE and confirm the L1 grading, since no registry trials were captured
- Obtain the FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Obtain mechanism of action data from DrugBank
- Clarify the current US regulatory status, since all four BLA licenses are listed as cancelled
- Define a monitoring plan for intravitreal injection risks, including infection, given the knowledge-graph contraindications

**Other predicted indications:** The remaining predictions (diabetic and other cataract types, craniostenosis cataract, tetanic cataract, hemorrhagic disease of newborn) lack a plausible anti-VEGF mechanism and have only indirect or no evidence. The suggested decision for all of them is **Hold**.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

