---
layout: default
title: Racepinephrine
parent: Model Prediction Only (L5)
nav_order: 1104
evidence_level: L5
indication_count: 7
monitor_inn: "RACEPINEPHRINE"
predicted_indications: ["primary hereditary glaucoma", "hypotrichosis simplex of the scalp", "open-angle glaucoma", "congenital hypotrichosis milia", "diffuse alopecia areata", "alopecia", "headache disorder"]
---

# Racepinephrine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
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

# Racepinephrine: From an Unspecified Original Indication to Primary Hereditary Glaucoma

## One-Sentence Summary

Racepinephrine is a racemic form of epinephrine, an adrenergic agonist. The data compiled for this report do not list an approved indication for it.
The TxGNN model predicts it may be effective for **primary hereditary glaucoma**, but **no clinical trials and no publications** currently support this prediction, so it rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (the only US license has no indication text) |
| Predicted New Indication | Primary hereditary glaucoma |
| TxGNN Prediction Score | 99.58% |
| Evidence Level | L5 |
| US Market Status | Cancelled only |
| Number of NDAs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for racepinephrine is not available in the compiled data. Based on known information, racepinephrine is a racemic mixture of epinephrine and a non-selective adrenergic agonist. Epinephrine and related adrenergic agents have historically been used topically to lower intraocular pressure by changing aqueous humor dynamics (increased outflow, reduced production). This gives a general mechanistic rationale for glaucoma.

The caveat is that primary hereditary (developmental) glaucoma is typically managed surgically. No trials or publications were found for this specific form. The high TxGNN score is a model prediction only, and the product's US license is cancelled.

**Other predicted indications (all L5, no trials or literature):**

| Predicted Indication | TxGNN Score | Assessment |
|------|------|------|
| Hypotrichosis simplex of the scalp | 99.57% | No clear mechanistic link; the condition is gene-driven |
| Open-angle glaucoma | 99.56% | Most biologically plausible; worth a literature review (Research Question) |
| Congenital hypotrichosis milia | 99.55% | No mechanistic rationale; likely network similarity only |
| Diffuse alopecia areata | 99.48% | Autoimmune disease; no relevant mechanism, and vasoconstriction may be counterproductive |
| Alopecia | 99.40% | No supported mechanism |
| Headache disorder | 99.01% | Speculative; sympathomimetics more often cause or worsen headache |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| M012 | BeC Racepinephrine (Blue Echo Care LLC; cancelled) | Liquid | Not specified |

Other dosage forms recorded for the drug are solution and aerosol spray.

## Safety Considerations

- **Disease associations flagged in the knowledge graph** (graph-derived contraindication links, not label text): hypertension and hypertensive disorder, diabetes mellitus, diabetic ketoacidosis, benign prostatic hyperplasia, coronary artery disease, angle-closure (closed-angle) glaucoma, hyperthyroidism, Graves disease, thyrotoxicosis, peripheral vascular disease, intermittent claudication, peripheral arterial disease, and intracranial arteriosclerosis.
- **Drug Interactions**: 56 interactions were identified in total. Of the 20 listed in the compiled data, most are Moderate or Minor.
  - **Moderate**: other sympathomimetics and stimulants (epinephrine including topical, ephedrine, phenylephrine, isometheptene, diethylpropion, phentermine, fenfluramine, sibutramine), formoterol, methylene blue, and inhaled rapid-acting insulin.
  - **Minor**: corticosteroids (hydrocortisone, prednisone, prednisolone, dexamethasone, betamethasone, budesonide, triamcinolone, beclomethasone).

Please refer to the package insert for label warnings and contraindications, which were not available in the compiled data.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All seven predicted indications are supported by model prediction only (L5), with no trials or literature. The product's US license is cancelled. Several flagged disease associations, including angle-closure glaucoma, hypertension, and coronary artery disease, are relevant to systemic and ocular use. Open-angle glaucoma is the most plausible of the predictions and merits a literature review as a research question, but there is no basis to advance.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data
- A systematic literature review of adrenergic agents for open-angle and hereditary glaucoma, compared with current standard therapies
- A clear original indication and a route and formulation assessment for any ophthalmic use
- A review of the systemic exposure risks, given the 56 drug interactions
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

