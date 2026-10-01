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

# Ranibizumab: From Anti-VEGF Retinal Therapy to Severe Nonproliferative Diabetic Retinopathy

## One-Sentence Summary

Ranibizumab is an intravitreal anti-VEGF antibody fragment marketed in the US. The source record does not list its original indications.
The TxGNN model predicts it may be effective for **severe nonproliferative diabetic retinopathy (NPDR)**.
This direction is supported by **6 related clinical trials** (including 1 completed Phase 3 randomized trial that directly tests ranibizumab in NPDR) and **20 publications**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the source data |
| Predicted New Indication | Severe nonproliferative diabetic retinopathy |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L1 (as scored in the Evidence Pack; see the caveat in the conclusion) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 6 (all are BLAs) |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the record. Based on known information, ranibizumab is an anti-VEGF Fab fragment that neutralizes VEGF-A.

VEGF drives retinal vascular permeability and neovascularization in diabetic retinopathy (DR). Blocking it can reduce DR severity and the risk of progression to vision-threatening complications. Anti-VEGF therapy is already established in diabetic eye disease, including diabetic macular edema (DME). Extending it to severe NPDR means treating earlier in the same disease process.

Two findings support the link:
- Serum and vitreous VEGF data in DR (PMID 36580154) support the rationale.
- The Phase 3 Pavilion trial (NCT04503551) tests ranibizumab directly in NPDR without macular edema.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04503551](https://clinicaltrials.gov/study/NCT04503551) | Phase 3 | Completed | 174 | Ranibizumab via Port Delivery System vs. monitoring in DR without center-involved DME. Most direct evidence; results published (PMID 40048178). |
| [NCT02634333](https://clinicaltrials.gov/study/NCT02634333) | Phase 3 | Completed | 399 | Anti-VEGF to prevent vision-threatening complications in high-risk eyes. Supports the class effect, but the agent may not be ranibizumab. |
| [NCT03452657](https://clinicaltrials.gov/study/NCT03452657) | Phase 3 | Unknown | 118 | Intravitreal ranibizumab vs. sham injections for preventing high-risk DR. Status unknown. |
| [NCT00444600](https://clinicaltrials.gov/study/NCT00444600) | Phase 3 | Completed | 691 | DRCR Protocol I: ranibizumab or triamcinolone plus laser in DME. Strong ranibizumab safety and efficacy data in diabetic eye disease, but the population is DME. |
| [NCT02834663](https://clinicaltrials.gov/study/NCT02834663) | Phase 4 | Completed | 25 | Six-month pilot of intravitreal ranibizumab for macular edema with NPDR. Looked at microaneurysm turnover and non-perfused retinal area. |
| [NCT05222633](https://clinicaltrials.gov/study/NCT05222633) | N/A | Unknown | 1000 | Real-world observation of anti-VEGF therapy across retinal diseases. Only weak supportive relevance. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40048178](https://pubmed.ncbi.nlm.nih.gov/40048178/) | 2025 | RCT | JAMA Ophthalmol | Pavilion trial: Port Delivery System with ranibizumab vs. monitoring in NPDR without macular edema. Tests continuous ranibizumab release as a less frequent regimen. |
| [39673354](https://pubmed.ncbi.nlm.nih.gov/39673354/) | 2024 | Systematic review / meta-analysis | Health Technol Assess | Anti-VEGF drugs vs. laser photocoagulation for DR. |
| [40347224](https://pubmed.ncbi.nlm.nih.gov/40347224/) | 2025 | Systematic review and economic analysis | Health Technol Assess | Economic follow-up of anti-VEGF vs. laser in proliferative and non-proliferative DR. |
| [32606578](https://pubmed.ncbi.nlm.nih.gov/32606578/) | 2020 | Post hoc analysis of RCT | Clin Ophthalmol | Predictors of early DR regression with ranibizumab in RIDE/RISE. |
| [36774994](https://pubmed.ncbi.nlm.nih.gov/36774994/) | 2023 | Post hoc analysis of RCT (meta-analysis) | Ophthalmol Retina | Effect of baseline DR severity on time to DME resolution with ranibizumab in phase III trials. |
| [36161830](https://pubmed.ncbi.nlm.nih.gov/36161830/) | 2022 | Post hoc analysis of RCT | BMJ Open Ophthalmol | Factors linked to DRSS changes with less frequent ranibizumab in the RIDE/RISE extension. |
| [35417296](https://pubmed.ncbi.nlm.nih.gov/35417296/) | 2022 | Post hoc analysis of RCT | Ophthalmic Surg Lasers Imaging Retina | Course of DR in untreated fellow eyes in RIDE/RISE. |
| [30234859](https://pubmed.ncbi.nlm.nih.gov/30234859/) | 2018 | Secondary analysis of RCT | Retina | DRCR.net Protocol I 5-year report on DR severity changes in eyes treated with ranibizumab for DME. |
| [37278412](https://pubmed.ncbi.nlm.nih.gov/37278412/) | 2023 | Simulation model | BMJ Open Ophthalmol | Long-term impact of proactive anti-VEGF treatment of severe NPDR vs. waiting for PDR. |
| [33966556](https://pubmed.ncbi.nlm.nih.gov/33966556/) | 2021 | Review | Expert Opin Biol Ther | Review of ranibizumab for DR. |

---

## US Market Information

The record lists 6 licenses, but only 3 distinct authorizations (two are duplicated). Approved indication text is not recorded for any of them.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| BLA125156 | LUCENTIS | Injection, solution | Genentech, Inc. |
| BLA761165 | CIMERLI | Injection, solution | Sandoz Inc |
| BLA761202 | Byooviz | Injection, solution | Harrow Eye, LLC |

---

## Safety Considerations

Package insert warnings and contraindications are not available in the record, and no drug-drug interaction data were found. Please refer to the package insert for safety information.

Points to watch, drawn from the evidence:
- Endophthalmitis and intraocular pressure changes after intravitreal injection.
- The burden of repeated intravitreal injections and follow-up visits.
- A possible lens-related signal: a small lens-opacity study (NCT01330797) and one case report of capsular block syndrome after ranibizumab injection (PMID 38476863). Neither is conclusive.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Anti-VEGF biology fits DR well, and a completed Phase 3 randomized trial (Pavilion) tests ranibizumab directly in NPDR. The Evidence Pack scores this L1. Strictly, though, only one completed Phase 3 trial directly tests ranibizumab in NPDR. The other Phase 3 trials are in DME, or in NPDR with an agent that is unconfirmed or not ranibizumab, so the evidence may be closer to L2.

**To proceed, the following is needed:**
- Confirm the current US label status for DR and the original approved indications, since the record contains no indication text.
- Obtain the package insert warnings and contraindications, and detailed mechanism of action data.
- Review the full Pavilion results (efficacy and safety) and a patient-selection plan based on DR severity.
- Plan for injection burden and monitoring of endophthalmitis and intraocular pressure.

The other nine predicted indications (cataract subtypes and hemorrhagic disease of newborn) have no plausible therapeutic rationale. They are recommended as **Hold**.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

