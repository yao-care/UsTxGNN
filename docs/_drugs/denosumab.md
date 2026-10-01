---
layout: default
title: Denosumab
parent: Model Prediction Only (L5)
nav_order: 582
evidence_level: L5
indication_count: 2
---

# Denosumab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

# Denosumab: From Bone Loss (Osteoporosis) to Severe Nonproliferative Diabetic Retinopathy

## One-Sentence Summary

Denosumab is an injectable biologic. The supplied data do not state its approved indications, but the linked studies describe its use for osteoporosis and for bone loss from androgen-deprivation therapy.
The TxGNN model predicts it may be effective for **severe nonproliferative diabetic retinopathy** with a very high score, but there are **0 clinical trials** and **0 publications** for this exact indication.
For the broader "diabetic retinopathy" prediction, there is only 1 ocular safety trial and 2 cohort-type publications, none of which test retinal efficacy.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the license data (inferred from linked studies: osteoporosis / bone loss) |
| Predicted New Indication | Severe nonproliferative diabetic retinopathy |
| TxGNN Prediction Score | 99.63% |
| Evidence Level | L5 (model prediction only) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 (listed licenses are BLAs) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the supplied data. Denosumab is generally known as an antibody against RANKL, a bone-remodeling signal. The link to diabetic retinopathy has not been assessed.

The one hypothesis on record is that RANKL/OPG signaling may play a role in vascular inflammation or calcification. Nothing in the supplied data supports it. The high TxGNN score (0.996) comes from the knowledge graph alone.

The literature found for the related "diabetic retinopathy" prediction concerns diabetes outcomes such as type 2 diabetes incidence, foot ulceration, and fracture risk. It does not concern retinal outcomes. The prediction should be treated as a hypothesis to test, not a supported finding.

---

## Clinical Trial Evidence

Currently no related clinical trials are registered for severe nonproliferative diabetic retinopathy.

For the broader prediction "diabetic retinopathy" (rank 2, TxGNN score 99.23%), one trial was found. It is not an efficacy test:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00925600](https://clinicaltrials.gov/study/NCT00925600) | Phase 3 | Completed | 769 | Placebo-controlled study of new or worsening lens opacifications in men with non-metastatic prostate cancer receiving denosumab for bone loss from androgen-deprivation therapy. It is an ocular safety study, graded C for relevance, and gives no direct evidence for diabetic retinopathy. |

---

## Literature Evidence

Currently no related literature is available for severe nonproliferative diabetic retinopathy.

For the broader prediction "diabetic retinopathy", two cohort-type publications were found. Their relevance to retinal outcomes is not yet assessed:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38899553](https://pubmed.ncbi.nlm.nih.gov/38899553/) | 2024 | Cohort (with systematic review and meta-analysis) | Diabetes, Obesity & Metabolism | Real-world analysis of denosumab for osteoporosis versus bisphosphonates. It looked at type 2 diabetes incidence and long-term complications, including retinopathy, but the supplied abstract gives no results. |
| [36960265](https://pubmed.ncbi.nlm.nih.gov/36960265/) | 2023 | Cohort | Cureus | Use of the FRAX fracture-risk tool in adults with type 2 diabetes. It has no retinal outcomes. |

---

## US Market Information

The supplied approved-indication text is empty for all listed licenses. Only the first five of 20 licenses were provided, and one is duplicated in the data. The four distinct products are:

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| BLA761439 | XTRENBO | Injection | Hikma Pharmaceuticals USA Inc. |
| BLA761398 | CONEXXENCE | Injection | Fresenius Kabi USA, LLC |
| BLA761362 | JUBBONTI | Injection | Sandoz Inc |
| BLA761404 | Denosumab-BMWO | Injection | CELLTRION USA, Inc. |

---

## Safety Considerations

Please refer to the package insert for safety information. No drug interactions were found in the queried data.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on the TxGNN model score, with no trials or publications for severe nonproliferative diabetic retinopathy. The only related trial is an ocular safety study, and the linked papers cover diabetes outcomes rather than retinal outcomes. Package insert and mechanism data are missing, so the candidate cannot move past S0.

**To proceed, the following is needed:**
- The package insert warnings and contraindications (a blocking gap)
- Mechanism of action data, to test whether RANKL/OPG signaling plausibly affects diabetic retinopathy
- Retinal-specific evidence, such as preclinical studies or a review of the retinopathy results in PMID 38899553
- A route-compatibility assessment (available and required routes are still pending)

*This report is for research reference only and is not medical advice. Repurposing candidates require clinical validation before any use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

