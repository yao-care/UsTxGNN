---
layout: default
title: Avatrombopag
parent: Model Prediction Only (L5)
nav_order: 431
evidence_level: L5
indication_count: 9
monitor_inn: "AVATROMBOPAG"
predicted_indications: ["marcothrombocytopenia with mitral valve insufficiency", "hereditary thrombocytopenia with normal platelets", "transient neonatal thrombocytopenia", "dense granule disease", "amyotrophic lateral sclerosis", "bilateral parasagittal parieto-occipital polymicrogyria", "lower motor neuron syndrome with late-adult onset", "Mills syndrome", "monomelic amyotrophy"]
last_modified_at: 2026-11-24
description: "Avatrombopag: predicted new indication marcothrombocytopenia with mitral valve insufficiency (evidence level L5). In the US: 2 FDA applications (2 active)"
---

# Avatrombopag
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

## Avatrombopag: thrombopoietin receptor agonist → marcothrombocytopenia with mitral valve insufficiency
{: .text-alpha }

## One-Sentence Summary

Avatrombopag is a thrombopoietin receptor (TPO-R) agonist that stimulates platelet production.
The TxGNN model predicts it may be effective for **marcothrombocytopenia with mitral valve insufficiency**,
but currently there are **0 clinical trials** and **0 publications** supporting this direction, so this is a model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | marcothrombocytopenia with mitral valve insufficiency |
| TxGNN Prediction Score | 1.0000 |
| Evidence Level | L5 |
| US Market Status | Marketed (active FDA-approved applications: 2 of 2) |
| Number of FDA Applications | 2 (active: 2) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

ChEMBL (EMBL-EBI) records the mechanism of action of avatrombopag as: Thrombopoietin receptor agonist ([ChEMBL CHEMBL2103883 (avatrombopag): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL2103883), CC BY-SA 3.0; accessed 2026-11-19.) Based on known pharmacology, avatrombopag is a thrombopoietin receptor agonist that stimulates megakaryocyte proliferation and platelet production.

A plausible link to inherited macrothrombocytopenia exists only if platelet production is impaired while the TPO-R pathway remains intact. In that case, stimulating thrombopoiesis could raise platelet counts. The mitral valve insufficiency component of the predicted condition, however, is unrelated to the drug's mechanism.

The TxGNN score is very high, but no clinical trials or publications support it. This should be treated as a hypothesis only.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

<!-- licenses:begin -->

| Application / NDC | Product | Holder | Dosage form | Status |
|------|------|------|------|------|
| NDA210238 | DOPTELET | AKARX INC | Tablet; oral | Valid |
| NDA219696 | DOPTELET SPRINKLE | AKARX INC | Granule; oral | Valid |

<!-- licenses:end -->

## Safety Considerations

**Drug Interactions**: 52 interactions are recorded, among them several rated Major, including:
- Fosphenytoin
- Carbamazepine
- Carfilzomib
- Dabrafenib
- Enzalutamide
- Fluconazole
- Imatinib

Moderate-level interactions include clarithromycin, cobicistat, atazanavir, gemfibrozil and fenofibrate, among others.

For warnings and contraindications, please refer to the package insert.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on the model score alone, with no clinical trials or literature directly studying this condition (Evidence Level L5). The disease label is also a composite that includes a valve condition unrelated to the drug's mechanism.

**To proceed, the following is needed:**
- Clarification of the disease definition and its genetic basis
- Preclinical or clinical evidence that the TPO-R pathway is intact and responsive in this condition
- Package insert warnings and contraindications for a formal safety review
- Detailed mechanism of action data
- Safety and dosing assessment in the relevant patient population

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [ChEMBL CHEMBL2103883 (avatrombopag): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL2103883) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

