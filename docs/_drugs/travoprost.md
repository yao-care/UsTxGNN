---
layout: default
title: Travoprost
parent: Model Prediction Only (L5)
nav_order: 1253
evidence_level: L5
indication_count: 10
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

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Travoprost: From Open-Angle Glaucoma / Ocular Hypertension to Visceral Calciphylaxis

## One-Sentence Summary

Travoprost is a topical prostaglandin F2-alpha analog used as eye drops (and an intracameral implant) for open-angle glaucoma and ocular hypertension.
The TxGNN model predicts it may be effective for **visceral calciphylaxis**, but **0 clinical trials** and **0 publications** currently support this prediction, so it rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Open-angle glaucoma / ocular hypertension (the US license records contain no indication text, so this is taken from the trial and rationale data) |
| Predicted New Indication | Visceral calciphylaxis |
| TxGNN Prediction Score | 99.9998% (saturated, so it does not discriminate between candidates) |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 18 (including generic ANDAs) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the record. Travoprost is known to be a selective FP receptor agonist. It lowers intraocular pressure by increasing aqueous humor outflow.

Visceral calciphylaxis involves vascular calcification and microvascular occlusion with tissue ischemia. No plausible mechanistic link to FP receptor agonism was identified. Topical ocular dosing also gives very low systemic exposure, which makes a systemic vascular effect unlikely. The prediction is therefore best read as a model artifact rather than a mechanism-supported hypothesis.

The other top-ranked predictions share this weakness: three forms of thoracic outlet syndrome, angiodysplasia of stomach, blue toe syndrome, lymphangiectasis and spontaneous coronary artery dissection. All have no trials or literature and no mechanistic rationale.

Two further predictions have some indirect material, but none of it shows benefit:
- **Vascular disease (rank 5):** 14 trials are listed, all in glaucoma or ocular hypertension. None has a vascular disease endpoint. They concern ocular tolerability, including conjunctival hyperemia, and in one case retinal and choroidal blood flow.
- **Hemangioendothelioma (rank 10):** two publications concern glaucoma in Sturge-Weber syndrome. One is a case report of travoprost-induced uveal effusion, which is a possible safety signal rather than therapeutic evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered for visceral calciphylaxis.

## Literature Evidence

Currently no related literature available for visceral calciphylaxis.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA218159 | Travoprost Ophthalmic Solution | Solution/drops | Glenmark Pharmaceuticals Inc |
| ANDA214687 | Travoprost ophthalmic solution | Solution/drops | Alembic Pharmaceuticals Limited |
| ANDA210458 | Travoprost Ophthalmic Solution USP, 0.004% | Solution/drops | Alembic Pharmaceuticals Inc. |
| ANDA203767 | Travoprost Ophthalmic | Solution | Micro Labs Limited |
| NDA218010 | iDose TR | Implant | Glaukos Corporation |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical or literature support and no plausible mechanism. The TxGNN score is saturated, so it adds little information, and topical ocular dosing is unlikely to reach affected tissue. The related trials in the pack all test the approved glaucoma indication.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Confirmed mechanism of action from DrugBank
- A literature search for any preclinical rationale linking FP receptor signaling to vascular calcification or calciphylaxis
- A route and exposure assessment, since the available forms are ocular only
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

