---
layout: default
title: Deoxycholic Acid
parent: Model Prediction Only (L5)
nav_order: 583
evidence_level: L5
indication_count: 3
monitor_inn: "DEOXYCHOLIC ACID"
predicted_indications: ["autosomal dominant familial hematuria-retinal arteriolar tortuosity-contractures syndrome", "brain small vessel disease 1 with or without ocular anomalies", "diabetic nephropathy"]
last_modified_at: 2026-10-14
description: "Deoxycholic Acid: predicted new indication Diabetic nephropathy (evidence level L5). Approved use: Not available in the data compiled for this report"
---

# Deoxycholic Acid
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

# Deoxycholic Acid: From Submental Fat Reduction to Diabetic Nephropathy

## One-Sentence Summary

Deoxycholic acid is a secondary bile acid that was marketed in the US as an injectable (KYBELLA), but its US authorization is now cancelled and the approved indication text is not available in the data compiled for this report.
The TxGNN model predicts it may be relevant to **diabetic nephropathy** (the highest-scoring prediction with any supporting literature), but there are **0 clinical trials** and only **4 publications**, all indirect (preclinical or bile acid profiling studies).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the data compiled for this report |
| Predicted New Indication | Diabetic nephropathy (top-ranked prediction overall: autosomal dominant familial hematuria-retinal arteriolar tortuosity-contractures syndrome) |
| TxGNN Prediction Score | 99.32% for diabetic nephropathy (99.49% for the top-ranked rare disorder) |
| Evidence Level | L4 (diabetic nephropathy); L5 for the two top-ranked rare disorders |
| US Market Status | Cancelled only |
| Number of NDAs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Deoxycholic acid is a secondary bile acid. The data compiled for this report do not describe how it acts, so any mechanistic argument is inferential.

The three top-ranked predictions differ in plausibility:

- **Two rare COL4A1-related disorders** (ranks 1 and 2: the familial hematuria-retinal arteriolar tortuosity-contractures syndrome and brain small vessel disease 1). These have very high scores (about 99.5%) but no trials, no literature, and no known pathway link to deoxycholic acid. The predictions most likely reflect knowledge-graph topology rather than biology.
- **Diabetic nephropathy** (rank 3). Four recent papers (2021-2024) show that bile acid metabolism is altered in diabetic kidney disease, in both animal models and patients. Bile acid signaling (such as FXR and TGR5) is plausibly linked to renal inflammation, lipid handling, and oxidative stress. However, these papers appear to report bile acids as biomarkers or as changes accompanying other interventions (herbal granules, relaxin, nanoparticles), not deoxycholic acid as a treatment.

Deoxycholic acid is also a cytotoxic secondary bile acid (it destroys fat cells when injected). The direction of any effect in the kidney is therefore uncertain and could be harmful.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

The following publications relate to diabetic nephropathy. None tests deoxycholic acid as a therapy.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39384774](https://pubmed.ncbi.nlm.nih.gov/39384774/) | 2024 | Cohort (clinical metabolomic profiling) | Nutrition & Diabetes | Bile acid metabolism changes step by step in patients with diabetic kidney disease, in association with disease progression |
| [38377553](https://pubmed.ncbi.nlm.nih.gov/38377553/) | 2024 | Preclinical (nanoparticle) | ACS Biomaterials Science & Engineering | Orally absorbed nanoparticles to reduce oxidative stress and vasoconstriction in diabetic nephropathy |
| [36996678](https://pubmed.ncbi.nlm.nih.gov/36996678/) | 2023 | Preclinical (diabetic mouse model) | Biomedicine & Pharmacotherapy | Relaxin showed kidney-protective effects accompanied by increased bile acid levels in diabetic mice |
| [33378964](https://pubmed.ncbi.nlm.nih.gov/33378964/) | 2021 | Preclinical (animal model) | Biomedicine & Pharmacotherapy | QiDiTangShen granules altered gut microbiome and improved bile acid profiles in diabetic nephropathy mice |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA206333 (cancelled) | KYBELLA | Injection, solution | Not available |

## Safety Considerations

- **Drug Interactions**: 67 interactions were identified. The 20 listed in the compiled data are all rated Moderate. They mainly involve agents that affect bleeding or clotting, for example:
  - Antiplatelets: acetylsalicylic acid, clopidogrel, abciximab, cilostazol, cangrelor
  - Anticoagulants: apixaban, betrixaban, fondaparinux, dalteparin, bivalirudin, argatroban
  - Thrombolytics: alteplase, anistreplase
  - Radiolabelled antibodies: ibritumomab tiuxetan, tositumomab

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All predictions rest on model scores alone. The two highest-scoring rare disorders have no supporting evidence or biological rationale. Diabetic nephropathy has only indirect, preclinical or biomarker-level evidence, with no study of deoxycholic acid itself, and the product's US authorization is cancelled. Its cytotoxic nature raises the possibility of harm.

**To proceed, the following is needed:**
- Mechanism of action data for deoxycholic acid
- The FDA package insert (warnings, contraindications, and the original approved indication)
- Direct preclinical evidence testing deoxycholic acid, or its receptor pathways (FXR/TGR5), in diabetic kidney models
- A review of whether the toxicity profile and injectable-only route are compatible with a systemic or renal indication
- Evaluation of the rare COL4A1-related predictions only if a genuine biological link can first be established
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

