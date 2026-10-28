---
layout: default
title: Carboprost Tromethamine
parent: Model Prediction Only (L5)
nav_order: 498
evidence_level: L5
indication_count: 10
monitor_inn: "CARBOPROST TROMETHAMINE"
predicted_indications: ["atypical coarctation of aorta", "aortic malformation", "migraine with brainstem aura", "migraine disorder", "pulmonary hypertension", "non-syndromic esophageal malformation", "kyphoscoliotic heart disease", "amenorrhea (disease)", "esophageal disease", "primary hereditary glaucoma"]
last_modified_at: 2026-10-14
description: "Carboprost Tromethamine: predicted new indication Atypical coarctation of aorta (evidence level L5). Approved use: Not stated in the data compiled for this report (the drug is known as…"
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

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Carboprost Tromethamine: From Obstetric Use to Atypical Coarctation of Aorta
{: .text-alpha }

## One-Sentence Summary

Carboprost tromethamine is a prostaglandin F2alpha analog marketed in the US as an injectable (Hemabate and generics). The TxGNN model predicts it may be effective for **atypical coarctation of aorta**, but **no clinical trials and no publications** currently support this prediction, and the biological rationale is weak. The prediction rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the data compiled for this report (the drug is known as an injectable uterotonic used in obstetrics) |
| Predicted New Indication | Atypical coarctation of aorta |
| TxGNN Prediction Score | 0.9999 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses on record: at least 13) |
| Number of NDAs | 13 licenses listed (1 NDA, 12 ANDAs), all cancelled |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the compiled data. Based on known pharmacology, carboprost is a 15-methyl analog of prostaglandin F2alpha. It acts on FP receptors to cause smooth muscle contraction in the uterus, blood vessels and bronchi.

For atypical coarctation of aorta, there is no plausible mechanistic rationale. It is a structural congenital defect, and an FP agonist would not correct it. Vasoconstriction could even be harmful. In neonates with ductal-dependent lesions, the relevant prostaglandin is PGE1, not PGF2alpha. The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence, rather than a true therapeutic link.

**Other predictions reviewed (all prediction-only, L5, Hold):**

| Rank | Predicted Indication | Score | Assessment |
|---|------|------|------|
| 2 | Aortic malformation | 0.9998 | Structural defect; no response expected to an FP agonist |
| 3 | Migraine with brainstem aura | 0.9997 | PGF2alpha agonism is not an established therapy; the drug commonly causes headache, nausea and vomiting |
| 4 | Migraine disorder | 0.9996 | Expected to be pro-nociceptive or neutral |
| 5 | Pulmonary hypertension | 0.9993 | Carboprost can raise pulmonary arterial pressure; this is a safety concern, not an opportunity |
| 6 | Non-syndromic esophageal malformation | 0.9992 | Structural and surgically managed; no pharmacologic link |
| 7 | Kyphoscoliotic heart disease | 0.9992 | Benefit implausible, harm possible |
| 8 | Amenorrhea | 0.9989 | Biologically closest (reproductive system), but no recognized treatment pathway; pregnancy must be excluded |
| 9 | Esophageal disease | 0.9983 | Drug typically causes GI adverse effects |
| 10 | Primary hereditary glaucoma | 0.9969 | FP agonist class precedent (latanoprost, etc.) is real, but would need a dedicated ocular formulation; systemic use is not appropriate |

Of these, glaucoma has the strongest class-based mechanistic rationale, but it would require a new topical formulation and preclinical work.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

The drug is marketed, with 13 valid licenses. No approved indication text is available in the data compiled for this report. Up to 5 main authorizations are shown:

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA017989 | Hemabate (Pharmacia & Upjohn) | Injection, solution | Not available (valid) |
| ANDA217198 | Carboprost Tromethamine (Alembic) | Injection, solution | Not available (valid) |
| ANDA216939 | Carboprost Tromethamine (Eugia US) | Injection, solution | Not available (valid) |
| ANDA215901 | Carboprost Tromethamine (ANI Pharmaceuticals) | Injection | Not available (valid) |
| ANDA211941 | Carboprost Tromethamine (Dr. Reddy's) | Injection, solution | Not available (valid) |

## Safety Considerations

Package insert warnings and contraindications were not available in the compiled data, and no drug-drug interaction or knowledge-graph contraindication records were found. Please refer to the package insert for safety information.

From the mechanism-of-action review of the predicted indications, the following points are worth noting:
- Carboprost can cause bronchoconstriction and pulmonary vasoconstriction, and may raise pulmonary arterial pressure. This is directly relevant to the pulmonary hypertension and kyphoscoliotic heart disease predictions.
- Exogenous PGF2alpha analogs commonly cause nausea, vomiting, diarrhea and headache.
- Pregnancy must be excluded before any use in a reproductive indication such as amenorrhea.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All ten predictions are model output only (L5), with no clinical trials or literature. For the top predictions (aortic and esophageal malformations, migraine, pulmonary hypertension), the drug's FP-agonist mechanism is irrelevant or potentially harmful. The drug is marketed in the US, with 13 valid licenses.

**To proceed, the following is needed:**
- FDA package insert warnings, contraindications and approved indications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- If any direction is pursued, glaucoma is the only one with class precedent, and it would require a dedicated ocular formulation and preclinical studies
- Confirmation of current market and supply status, given that the drug is marketed with 13 valid licenses
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

