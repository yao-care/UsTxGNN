---
layout: default
title: Carboprost Tromethamine
parent: Model Prediction Only (L5)
nav_order: 498
evidence_level: L5
indication_count: 10
---

# Carboprost Tromethamine
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

# Carboprost Tromethamine: From Obstetric Use to Atypical Coarctation of Aorta

## One-Sentence Summary

Carboprost tromethamine is a prostaglandin F2-alpha (PGF2-alpha) analog and uterotonic, used for abortion and postpartum hemorrhage.
The TxGNN model predicts it may be effective for **atypical coarctation of aorta**, but **0 clinical trials** and **0 publications** support this prediction.
The high score most likely reflects knowledge-graph proximity rather than a real therapeutic mechanism.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the US license records (known clinically as a uterotonic for abortion and postpartum hemorrhage) |
| Predicted New Indication | Atypical coarctation of aorta |
| TxGNN Prediction Score | 99.99% (model rank 586) |
| Evidence Level | L5 (model prediction only) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 (the five listed below are ANDAs) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available for this drug. Based on known information, carboprost is a PGF2-alpha analog that stimulates uterine contraction, and its efficacy in obstetric use is established.

The predicted indication is a structural congenital vascular defect, which a drug is unlikely to treat. No plausible mechanistic link to carboprost was identified. The high TxGNN score most likely reflects knowledge-graph proximity to vascular and smooth-muscle nodes rather than a therapeutic mechanism. This prediction should be treated as a likely model artifact, not a repurposing opportunity.

### Other Top-10 Predictions

None of the other nine predictions has literature evidence, and only one has a linked trial. That trial (NCT04481503) is an observational study, not a test of carboprost.

| Rank | Predicted Indication | Score | Assessment |
|---|---|---|---|
| 2 | Aortic malformation | 99.98% | Structural defect. The only linked trial, [NCT04481503](https://clinicaltrials.gov/study/NCT04481503), is a non-interventional echocardiography study in women in labor and does not evaluate carboprost (relevance grade C). |
| 3 | Migraine with brainstem aura | 99.97% | PGF2-alpha agonism is more likely to provoke than relieve headache. |
| 4 | Migraine disorder | 99.96% | Same concern as rank 3. |
| 5 | Pulmonary hypertension | 99.93% | Likely opposite effect. PGF2-alpha causes pulmonary vasoconstriction, so this is a safety concern. |
| 6 | Non-syndromic esophageal malformation | 99.92% | Structural anomaly, likely a knowledge-graph artifact. |
| 7 | Kyphoscoliotic heart disease | 99.92% | Undefined link, and pulmonary vasoconstriction may be harmful. |
| 8 | Amenorrhea | 99.89% | Weak link, and luteolytic activity could be counterproductive. |
| 9 | Esophageal disease | 99.83% | No therapeutic rationale, and GI adverse effects are common. |
| 10 | Primary hereditary glaucoma | 99.69% | The most coherent prediction (see below). |

**Primary hereditary glaucoma** is the only biologically coherent prediction and is flagged as a research question. PGF2-alpha analogs such as latanoprost lower intraocular pressure via the FP receptor. However, carboprost is formulated for intramuscular obstetric use with significant systemic effects, so ophthalmic use would need an entirely new development path. Existing FP-agonist glaucoma drugs already cover this mechanism, which limits added value.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

Five of the 20 authorizations are listed. Approved indication text is not provided in the records.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA217198 | Carboprost Tromethamine | Injection, solution | Alembic Pharmaceuticals Inc. |
| ANDA216939 | Carboprost Tromethamine | Injection, solution | Eugia US LLC |
| ANDA215901 | Carboprost Tromethamine | Injection | ANI Pharmaceuticals, Inc. |
| ANDA216882 | Carboprost Tromethamine | Injection, solution | BE Pharmaceuticals Inc. |
| ANDA216897 | Carboprost Tromethamine | Injection, solution | OneSource Specialty Pharma Limited |

All listed products are injectables.

## Safety Considerations

Package insert warnings and contraindications are not available in the current data, and no drug-interaction records were found. Please refer to the package insert for safety information.

Points raised in the prediction analysis:
- **Pulmonary vasoconstriction**: PGF2-alpha analogs can raise pulmonary arterial pressure. This is relevant to the pulmonary hypertension and kyphoscoliotic heart disease predictions.
- **Gastrointestinal effects**: Nausea, vomiting and diarrhea are common.
- **Systemic exposure**: The intramuscular obstetric formulation has significant systemic effects.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction is a structural congenital defect with no mechanistic link, no trials and no literature (L5). The high TxGNN score is most likely a knowledge-graph artifact. Glaucoma is the only coherent hypothesis, and it is a research question with limited added value because FP-agonist drugs already exist.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- For the glaucoma hypothesis only: preclinical FP-receptor and ocular-tolerability data, and a feasibility assessment of a topical formulation
- Route-compatibility and similarity-to-original assessments, both currently pending

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

