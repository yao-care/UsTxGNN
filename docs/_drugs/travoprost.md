---
layout: default
title: Travoprost
parent: Model Prediction Only (L5)
nav_order: 1253
evidence_level: L5
indication_count: 10
monitor_inn: "TRAVOPROST"
predicted_indications: ["visceral calciphylaxis", "arterial thoracic outlet syndrome", "venous thoracic outlet syndrome", "neurogenic thoracic outlet syndrome", "vascular disease", "angiodysplasia of stomach", "blue toe syndrome", "lymphangiectasis", "idiopathic spontaneous coronary artery dissection", "hemangioendothelioma"]
last_modified_at: 2026-10-14
description: "Travoprost: predicted new indication Visceral calciphylaxis (evidence level L5). Approved use: Open-angle glaucoma"
---

# Travoprost
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

## Travoprost: From Open-Angle Glaucoma to Visceral Calciphylaxis
{: .text-alpha }

## One-Sentence Summary

Travoprost is a prostaglandin F2-alpha analog (FP receptor agonist) originally used to lower eye pressure in open-angle glaucoma and ocular hypertension.
The TxGNN model predicts it may be effective for **visceral calciphylaxis**, but **no clinical trials and no publications** support this specific prediction.
The model's other top-ranked predictions are likewise unsupported, so this report treats the result as a computational signal only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Open-angle glaucoma; ocular hypertension |
| Predicted New Indication | Visceral calciphylaxis |
| TxGNN Prediction Score | 1.0000 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses: 9 of 9) |
| Number of NDAs | 9 (valid: 9) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data was not available in the data compiled for this report. Based on known pharmacology, travoprost is a prostaglandin F2-alpha analog that acts on the FP receptor. In glaucoma it lowers eye pressure mainly by increasing uveoscleral outflow. It also has vasoactive properties.

The link between the original and predicted indications is weak. Visceral calciphylaxis (calcific uremic arteriolopathy) is a disease of small-vessel calcification and clotting, usually seen in kidney failure. No plausible mechanistic connection to FP receptor agonism has been established. Topical eye drops also produce minimal systemic exposure, so meaningful effects on visceral blood vessels are unlikely.

The model's high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. The same applies to the other top predictions: arterial, venous and neurogenic thoracic outlet syndromes, angiodysplasia of the stomach, blue toe syndrome, lymphangiectasis, spontaneous coronary artery dissection and hemangioendothelioma. None has any supporting clinical evidence.

## Clinical Trial Evidence

Currently no related clinical trials are registered for visceral calciphylaxis.

For reference, the broader prediction "vascular disease" (rank 5) was matched to 10 travoprost trials. These are nearly all studies in glaucoma or ocular hypertension, linked only through keywords such as hyperemia. None tests travoprost as a treatment for a vascular disease. The most relevant is shown below.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00308945](https://clinicaltrials.gov/study/NCT00308945) | Phase 4 | Completed | 20 | Compared travoprost and latanoprost effects on retinal vascular diameter and choroidal blood flow in glaucoma patients; an ocular blood-flow study, not a vascular disease treatment |

## Literature Evidence

Currently no related literature is available for visceral calciphylaxis.

For reference, the only publication linked to a specific vascular-type prediction (hemangioendothelioma, rank 10) is an adverse-event report:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [19107053](https://pubmed.ncbi.nlm.nih.gov/19107053/) | 2008 | Case report (adverse event) | Journal francais d'ophtalmologie | Uveal effusion with subtotal exudative retinal detachment induced by topical travoprost in a patient with Sturge-Weber-Krabbe syndrome. This is a safety signal, not evidence of benefit. |

## US Market Information

All nine US authorizations are valid, and the approved-indication text was not available for any of them. The five below are examples.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA021994 | Travatan Z (Sandoz) | Solution/drops | Not available |
| NDA218010 | iDose TR (Glaukos) | Implant | Not available |
| ANDA218159 | Travoprost Ophthalmic Solution (Glenmark) | Solution/drops | Not available |
| ANDA214687 | Travoprost ophthalmic solution (Alembic) | Solution/drops | Not available |
| ANDA203431 | Travoprost (Apotex) | Solution | Not available |

## Safety Considerations

Package insert warnings and contraindications were not available in the data compiled for this report. Please refer to the package insert for safety information.

- **Disease associations flagged in the knowledge graph (not label text):** uveitis, iris disease, ciliary body disease, panuveitis, iritis, cystoid macular edema and macular retinal edema. These are ocular inflammatory or macular conditions where prostaglandin analogs warrant caution.
- **Drug interactions:** 49 potential interactions were recorded, all with an "Unknown" severity level. Examples include calcitriol, pantoprazole, sucralfate, morphine, metformin, omeprazole, prednisone, simvastatin, and acetylsalicylic acid. Severity has not been characterized.
- **Safety signal in vascular pathology:** The case report of uveal effusion in a patient with Sturge-Weber-Krabbe syndrome suggests caution in patients with abnormal vasculature.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model output alone (L5). There are no trials or publications for visceral calciphylaxis, and no plausible mechanism links an ocular FP receptor agonist to calcific small-vessel disease. All nine US licenses are valid, and topical ocular dosing gives little systemic exposure.

**To proceed, the following is needed:**
- Mechanism-of-action data and a credible biological hypothesis linking FP receptor signaling to vascular calcification or calciphylaxis
- Preclinical studies (for example, vascular calcification models) showing a benefit
- Evaluation of a route and formulation that would achieve systemic exposure, since the current licenses cover ocular products only
- FDA package insert warnings and contraindications, to complete safety screening
- Characterization of the severity of the 49 listed drug interactions, especially in dialysis or kidney-failure patients, who are the main population with calciphylaxis
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

