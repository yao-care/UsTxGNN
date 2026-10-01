---
layout: default
title: Abaloparatide
parent: Model Prediction Only (L5)
nav_order: 40
evidence_level: L5
indication_count: 4
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

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Abaloparatide: From Osteoporosis to Non-Syndromic Esophageal Malformation

## One-Sentence Summary

Abaloparatide is an injectable peptide marketed in the US as Tymlos, used for osteoporosis in postmenopausal women.
The TxGNN model predicts it may be effective for **non-syndromic esophageal malformation**, but this is a model prediction only, with **0 clinical trials** and **0 publications** supporting it.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Osteoporosis in postmenopausal women (the license record in the source data lists no indication text) |
| Predicted New Indication | Non-syndromic esophageal malformation |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the source record. Based on known information, abaloparatide is a PTHrP-analog that acts as a PTH1R agonist, and it is used as a bone-anabolic agent in osteoporosis.

No mechanistic link to the predicted indication has been established. Non-syndromic esophageal malformation is a congenital structural defect, and it is unlikely that a bone-anabolic peptide given to adults could correct it. The high score (0.998) reflects a graph-based association in the TxGNN knowledge graph and is not backed by any trial or publication.

The model also ranked three related terms: esophageal disease (99.75%), amenorrhea (99.72%) and esophageal ulcer (99.02%). All have L5 evidence and no supporting studies. The esophageal disease score likely comes from neighboring esophageal terms. For amenorrhea, any link would be indirect (bone loss) and speculative, and the drug's target population differs. For esophageal ulcer, no evidence suggests that PTH1R agonism promotes mucosal healing.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA208743 | Tymlos (Radius Health, Inc.) | Injection, solution | Not listed in the source data |

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found for this drug.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone (L5, stage S0), with no trials, no literature and no plausible mechanism linking a bone-anabolic PTH1R agonist to a congenital esophageal defect.

**To proceed, the following is needed:**
- Package insert warnings and contraindications, which are currently missing and block safety screening
- Detailed mechanism-of-action data and the approved indication text from DrugBank and the US label
- Any preclinical or clinical evidence linking PTH1R signaling to esophageal development or repair
- A route and population compatibility assessment for the predicted indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

