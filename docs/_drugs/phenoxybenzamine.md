---
layout: default
title: Phenoxybenzamine
parent: Model Prediction Only (L5)
nav_order: 1039
evidence_level: L5
indication_count: 2
---

# Phenoxybenzamine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

# Phenoxybenzamine: From an Alpha-Blocker (Original Indication Not Recorded) to Primary Hereditary Glaucoma

## One-Sentence Summary

Phenoxybenzamine is an oral capsule marketed in the US and generally described as an irreversible, non-selective alpha-adrenergic antagonist. The record has no approved indication text for it.
The TxGNN model predicts it may be useful for **primary hereditary glaucoma** (and, as a second prediction, **open-angle glaucoma**).
There are currently **0 clinical trials** and **0 publications** supporting this direction, so this is a model prediction only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded (all US license entries have empty indication text) |
| Predicted New Indication | Primary hereditary glaucoma |
| TxGNN Prediction Score | 99.55% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 5 (all listed as ANDA generic applications) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the input. Phenoxybenzamine is generally described as an irreversible, non-selective alpha-adrenergic antagonist. Adrenergic modulation could plausibly affect aqueous humor dynamics (production or outflow), which is the link the model may be exploiting. This mechanistic link has not been verified against retrieved evidence.

For **primary hereditary glaucoma**, the fit is unclear. This form is often driven by developmental or structural defects of the outflow pathway (for example, genes such as *CYP1B1* or *MYOC*), and alpha-blockade would not obviously correct such defects. The high graph score (99.55%) alone is not evidence of efficacy.

The second prediction, **open-angle glaucoma** (score 99.48%), is a more coherent hypothesis. Alpha-adrenergic antagonism could lower intraocular pressure through effects on aqueous production or outflow. It is still unverified. A targeted literature search on alpha-blocker effects on intraocular pressure is needed before either prediction advances.

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
| ANDA212568 | Phenoxybenzamine hydrochloride (Amneal Pharmaceuticals NY LLC) | Capsule | Not provided |
| ANDA215042 | Phenoxybenzamine Hydrochloride (Novitium Pharma LLC) | Capsule | Not provided |
| ANDA215600 | Phenoxybenzamine Hydrochloride (Aurobindo Pharma Limited) | Capsule | Not provided |
| ANDA215600 | Phenoxybenzamine Hydrochloride (Burel Pharmaceuticals, LLC) | Capsule | Not provided |
| ANDA215600 | Phenoxybenzamine Hydrochloride (NorthStar Rx LLC) | Capsule | Not provided |

All marketed products are oral capsules. No ophthalmic formulation is listed.

---

## Safety Considerations

Please refer to the package insert for safety information. No drug-interaction records were found for this drug.

Systemic hypotension is a known class concern for alpha-blockers. It would need review before any ocular use, especially since only an oral systemic form is marketed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model score alone (Evidence Level L5). There are no supporting trials or publications, and the mechanistic fit is weak for hereditary glaucoma and only plausible for open-angle glaucoma. Package-insert safety data are also missing, which blocks safety screening.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the FDA label (currently blocking)
- Detailed mechanism of action data (for example, from DrugBank)
- Targeted literature search on alpha-blocker effects on intraocular pressure and aqueous humor dynamics
- Review of systemic hypotension risk for an eye indication
- Assessment of route compatibility, since only an oral capsule is available and no ophthalmic formulation exists
- Prioritizing open-angle glaucoma over hereditary glaucoma for any follow-up evaluation

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

