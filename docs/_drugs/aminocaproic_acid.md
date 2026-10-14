---
layout: default
title: Aminocaproic Acid
parent: Model Prediction Only (L5)
nav_order: 327
evidence_level: L5
indication_count: 1
---

# Aminocaproic Acid
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

# Aminocaproic Acid: From Bleeding Control (Antifibrinolytic Therapy) to Severe Nonproliferative Diabetic Retinopathy

## One-Sentence Summary

Aminocaproic acid is an antifibrinolytic drug, used to control bleeding caused by excessive breakdown of blood clots. The TxGNN model predicts it may be effective for **severe nonproliferative diabetic retinopathy**, but **no clinical trials and no publications** currently support this direction, so the prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the compiled license data (the antifibrinolytic use is based on general knowledge of the drug class) |
| Predicted New Indication | Severe nonproliferative diabetic retinopathy |
| TxGNN Prediction Score | 99.27% |
| Evidence Level | L5 (model prediction only) |
| US Market Status | Cancelled only (no active licenses) |
| Number of NDAs | 13 (all cancelled; 1 NDA and 12 ANDAs) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, aminocaproic acid is a lysine analog that inhibits plasminogen activation and plasmin activity, which reduces the breakdown of fibrin clots.

A possible link to diabetic retinopathy is that this action could limit bleeding from fragile new blood vessels in the retina. It might also influence fibrinolytic and extracellular-matrix remodeling pathways in the retina.

This link is hypothetical. It comes only from the high TxGNN score, with no supporting mechanistic or clinical data. There is also a safety concern: antifibrinolytic therapy carries a theoretical risk of thrombosis, and people with diabetes already have elevated vascular risk. Similarity to the original indication and route compatibility have not yet been assessed.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA015197 (cancelled) | Aminocaproic Acid (Hikma Pharmaceuticals USA Inc.) | Tablet | Not stated |
| ANDA212492 (cancelled) | Aminocaproic acid (Major Pharmaceuticals) | Tablet | Not stated |
| ANDA213928 (cancelled) | Aminocaproic Acid (Carnegie Pharmaceuticals, LLC) | Tablet | Not stated |
| ANDA071192 (cancelled) | Aminocaproic Acid (Medical Purchasing Solutions, LLC) | Injection, solution | Not stated |
| ANDA216464 (cancelled) | Aminocaproic Acid (Camber Pharmaceuticals, Inc.) | Solution | Not stated |

All 13 licenses compiled for this drug are cancelled. Available dosage forms were oral tablets, injectable solutions, and other solutions.

## Safety Considerations

- **Disease associations from the knowledge graph (not label text):** The TxGNN knowledge graph links aminocaproic acid with contraindications in kidney disease, pyoureter, liver disease, gallbladder disease, disseminated intravascular coagulation, purpura fulminans (including acquired), and thrombotic disease. These come from model-derived data and should be verified against the official label.
- **Drug interactions:** The interaction query returned 75 entries. Most have an unknown severity level. The ones with a **moderate** level are:
  - Alteplase
  - Anistreplase

  This is expected, since thrombolytics and antifibrinolytics act in opposite directions. Other listed interacting drugs, with unknown severity, include morphine, omeprazole, lansoprazole, vancomycin, simvastatin, epinephrine, hydrocortisone, and acetylsalicylic acid.

Please refer to the package insert for warnings and contraindications from the label, which were not available for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests solely on a high model score (L5). No trials or publications support it, the mechanistic link is hypothetical, and the thrombotic risk is a particular concern in diabetic patients. In addition, all US licenses for this drug are cancelled.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- A literature and trial search for antifibrinolytics in diabetic retinopathy or retinal and vitreous hemorrhage
- Preclinical evidence of benefit in retinal models
- Assessment of route compatibility (for example, whether a systemic or intravitreal route would be needed) and similarity to the original indication
- A thrombotic risk assessment for diabetic patients
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

