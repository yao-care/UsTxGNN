---
layout: default
title: Abaloparatide
parent: Model Prediction Only (L5)
nav_order: 40
evidence_level: L5
indication_count: 4
monitor_inn: "ABALOPARATIDE"
predicted_indications: ["non-syndromic esophageal malformation", "esophageal disease", "amenorrhea (disease)", "esophageal ulcer"]
last_modified_at: 2026-10-30
description: "Abaloparatide: predicted new indication Non-syndromic esophageal malformation (evidence level L5). Approved use: Postmenopausal osteoporosis at high risk for fracture"
---

# Abaloparatide
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

## Abaloparatide: From Osteoporosis to Non-Syndromic Esophageal Malformation
{: .text-alpha }

## One-Sentence Summary

Abaloparatide is an injectable PTH-related peptide analog marketed in the US as Tymlos, used for osteoporosis in postmenopausal women at high fracture risk.
The TxGNN model predicts it may be effective for **non-syndromic esophageal malformation**, but this is a purely computational prediction with **0 clinical trials** and **0 publications** supporting it.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Postmenopausal osteoporosis at high risk for fracture (from pharmacology data; the license record has no indication text) |
| Predicted New Indication | Non-syndromic esophageal malformation |
| TxGNN Prediction Score | 0.9984 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses: 1 of 1) |
| Number of FDA Applications | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, abaloparatide is a PTHrP(1-34) analog that activates the PTH1 receptor (PTH1R) and has a bone anabolic effect. Its efficacy in osteoporosis was shown in a Phase 3 trial (NCT01343004), where it reduced new fractures versus placebo and showed less hypercalcemia than teriparatide.

No plausible mechanistic link to esophageal malformation can be established. This is a congenital, structural, developmental condition, and adult pharmacological therapy is unlikely to correct it. The high score (0.9984) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

Other predictions for this drug are similarly weak:

| Predicted Indication | TxGNN Score | Assessment |
|------|------|------|
| Esophageal disease | 0.9975 | Broad, non-specific category. No data link PTH1R agonism to esophageal pathology. |
| Amenorrhea | 0.9972 | Driven by hypothalamic-pituitary-ovarian axis dysfunction, on which abaloparatide has no established action. At most, it might support bone health in hypoestrogenic amenorrhea, which is not treatment of the condition itself. |
| Esophageal ulcer | 0.9902 | No known gastroprotective or mucosal-repair mechanism. |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA208743 (cancelled) | Tymlos (Radius Health, Inc.) | Injection, solution | Not listed in the license record |

## Safety Considerations

- **Drug Interactions** (3 records found):
  - Calcitriol (topical): Moderate
  - Calcipotriol (topical): Moderate
  - PTH1 receptor: pharmacological target record (not an interaction with a severity rating)

Please refer to the package insert for warnings and contraindications. The knowledge graph lists no contraindicated diseases for this drug.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All four predictions rest on model scores alone, with no trials or literature and no plausible biological link between PTH1R agonism and the predicted conditions. The only US license is cancelled, and warnings and contraindications are not available.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (blocking for safety screening)
- Detailed mechanism of action data
- A mechanistic rationale connecting PTH1R signaling to the predicted esophageal or gynecologic conditions
- Any preclinical or clinical evidence in the predicted indications
- Route and formulation compatibility assessment (the drug is available only as an injection)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

