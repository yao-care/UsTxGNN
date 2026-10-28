---
layout: default
title: Eculizumab
parent: Model Prediction Only (L5)
nav_order: 640
evidence_level: L5
indication_count: 10
monitor_inn: "ECULIZUMAB"
predicted_indications: ["cyclic hematopoiesis", "autosomal recessive severe congenital neutropenia due to JAGN1 deficiency", "X-linked severe congenital neutropenia", "congenital neutropenia-myelofibrosis-nephromegaly syndrome", "adult idiopathic neutropenia", "autosomal recessive severe congenital neutropenia due to CXCR2 deficiency", "primary immunodeficiency syndrome due to p14 deficiency", "autosomal recessive severe congenital neutropenia due to CSF3R deficiency", "severe congenital neutropenia", "primary release disorder of platelets"]
last_modified_at: 2026-10-28
description: "Eculizumab: predicted new indication Cyclic hematopoiesis (cyclic neutropenia) (evidence level L5). Approved use: Paroxysmal nocturnal hemoglobinuria"
---

# Eculizumab
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

## Eculizumab: From Paroxysmal Nocturnal Hemoglobinuria to Cyclic Hematopoiesis
{: .text-alpha }

## One-Sentence Summary

Eculizumab is a complement C5 inhibitor, originally used to treat paroxysmal nocturnal hemoglobinuria and neuromyelitis optica.
The TxGNN model predicts it may be effective for **cyclic hematopoiesis**, but **no clinical trials** and **no directly relevant publications** currently support this prediction. It is a model-only (L5) signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Paroxysmal nocturnal hemoglobinuria; neuromyelitis optica (the US license records contain no indication text) |
| Predicted New Indication | Cyclic hematopoiesis (cyclic neutropenia) |
| TxGNN Prediction Score | 0.9997 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses: 3 of 3) |
| Number of NDAs | 3 (valid: 3) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. Based on known information, eculizumab is a monoclonal antibody against complement protein C5 that blocks terminal complement activation. Its efficacy in complement-mediated diseases such as paroxysmal nocturnal hemoglobinuria is established.

The predicted indication, however, has no established link to this mechanism. Cyclic neutropenia is caused by ELANE mutations that impair neutrophil production, and it is not a complement-mediated disease. The very high TxGNN score (0.9997) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

Other highly ranked predictions show the same pattern. They are all neutropenia or immunodeficiency disorders (for example severe congenital neutropenia, JAGN1, CXCR2 and CSF3R deficiencies, and X-linked neutropenia). These arise from defects in granulopoiesis, neutrophil mobilization or signaling, not terminal complement activity. The ranking therefore looks like a cluster of related hematologic conditions rather than independent, mechanism-backed leads.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

No literature was retrieved for cyclic hematopoiesis, the top-ranked prediction. Currently no related literature available for this indication.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| BLA125166 | SOLIRIS (Alexion Pharmaceuticals Inc.) | Injection, solution, concentrate | Not listed in the data (status: valid) |
| BLA761333 | BKEMV (Amgen Inc) | Injection, solution, concentrate | Not listed in the data (status: valid) |
| BLA761340 | EPYSQLI (Teva Pharmaceuticals USA, Inc.) | Injection, solution | Not listed in the data (status: valid) |

## Safety Considerations

- **Drug Interactions**: Four minor interactions were identified, all with human immunoglobulin G preparations (intravenous, subcutaneous, intramuscular, and intravenous plus subcutaneous).
- **Infection risk (from the evaluation of the predicted indications)**: Eculizumab increases the risk of meningococcal infection, which is an unfavorable consideration in neutropenic patients. Complement C5 inhibition could also add infection risk in immunodeficient hosts.

Label warnings and contraindications were not available in the data compiled for this report. Please refer to the package insert for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model score alone. There are no clinical trials and no relevant literature, and cyclic neutropenia is not a complement-driven disease. The safety profile (meningococcal infection risk in neutropenic patients) is unfavorable. Standard care options such as G-CSF and HSCT are already established for related neutropenic conditions.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism of action data (MOA)
- Preclinical or mechanistic evidence showing that terminal complement activity contributes to cyclic hematopoiesis or neutropenia pathology
- Targeted literature and trial searches by disease rather than by drug name
- Clarification of the cancelled status of all three US licenses and the current marketing situation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

