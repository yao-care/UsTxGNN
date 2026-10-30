---
layout: default
title: Human C1-Esterase Inhibitor
parent: Model Prediction Only (L5)
nav_order: 772
evidence_level: L5
indication_count: 4
monitor_inn: "HUMAN C1-ESTERASE INHIBITOR"
predicted_indications: ["severe nonproliferative diabetic retinopathy", "primary release disorder of platelets", "diabetic retinopathy", "pseudo-von Willebrand disease"]
last_modified_at: 2026-10-30
description: "Human C1-Esterase Inhibitor: predicted new indication Severe nonproliferative diabetic retinopathy (evidence level L5). Approved use: Not stated in the available license data"
---

# Human C1-Esterase Inhibitor
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

## Human C1-Esterase Inhibitor: From Hereditary Angioedema Prophylaxis to Severe Nonproliferative Diabetic Retinopathy
{: .text-alpha }

## One-Sentence Summary

Human C1-esterase inhibitor is a plasma-derived protease inhibitor. The data compiled for this report do not list an approved indication for it.
The TxGNN model predicts it may be effective for **severe nonproliferative diabetic retinopathy**.
So far there are **0 clinical trials** and **0 publications** supporting this direction, so the prediction rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the available license data |
| Predicted New Indication | Severe nonproliferative diabetic retinopathy |
| TxGNN Prediction Score | 0.9961 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses: 1 of 1) |
| Number of FDA Applications | 1 (valid: 1) |
| Recommended Decision | Hold |

Other predicted indications, all L5 with no supporting studies:

| Rank | Predicted Indication | TxGNN Score |
|------|------|------|
| 2 | Primary release disorder of platelets | 0.9931 |
| 3 | Diabetic retinopathy | 0.9925 |
| 4 | Pseudo-von Willebrand disease | 0.9909 |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data are not available. Based on general knowledge, C1-esterase inhibitor regulates the kallikrein-kinin system, the complement cascade, and vascular permeability. This is a hypothesis and was not validated with the data compiled for this report.

Plasma kallikrein activity has been implicated in retinal vascular leakage and macular edema in diabetic eye disease. If C1-esterase inhibitor dampens kallikrein-kinin and complement-driven inflammation, it could in theory affect diabetic retinopathy. The generic "diabetic retinopathy" prediction (rank 3) overlaps with the severe nonproliferative subtype (rank 1) and shares the same evidence gap.

The other two predictions are weaker:
- **Primary release disorder of platelets:** the drug acts on contact, complement, and coagulation/fibrinolytic proteases, which could in theory influence platelets. No supporting data exist, and any hemostatic effect would need careful thrombotic-risk assessment.
- **Pseudo-von Willebrand disease:** this is a platelet GP1BA gain-of-function defect. No clear mechanistic path from C1-esterase inhibition to correcting it was identified, so the prediction is likely a network-association artifact.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| BLA125267 (cancelled) | Cinryze (Takeda Pharmaceuticals America, Inc.) | Injection, powder, lyophilized, for solution | Not stated in the available data |

---

## Safety Considerations

**Drug Interactions:** 41 interactions were recorded, including 1 Major and many Moderate. Examples:
- **Major:** Carfilzomib
- **Moderate (androgens):** Oxandrolone, Oxymetholone, Stanozolol, Testosterone, Danazol
- **Moderate (estrogens and hormonal agents):** Ethinylestradiol, Estradiol, Conjugated estrogens, Esterified estrogens, Diethylstilbestrol, Drospirenone
- **Moderate (thrombolytics):** Alteplase, Anistreplase
- **Moderate (erythropoiesis-stimulating agents):** Erythropoietin, Darbepoetin alfa

Only 20 of the 41 interactions were available for review. Many of these agents carry thrombotic risk, which is relevant for a protease inhibitor of the coagulation and fibrinolytic systems.

Please refer to the package insert for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All four predictions are L5: high model scores with no clinical or literature support. The only US license is cancelled, and the label's warnings and mechanism data are missing. The platelet-related predictions in particular have no plausible mechanistic basis.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data
- A literature and preclinical review of the kallikrein-kinin link to diabetic retinopathy, beginning with the retinal indications
- A thrombotic-risk assessment before considering any platelet-related indication
- Clarification of the drug's approved indication and current regulatory status
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

