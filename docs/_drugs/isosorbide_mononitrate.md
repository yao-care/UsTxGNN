---
layout: default
title: Isosorbide Mononitrate
parent: Model Prediction Only (L5)
nav_order: 816
evidence_level: L5
indication_count: 10
---

# Isosorbide Mononitrate
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

# Isosorbide Mononitrate: From Angina Prevention to Hypertrichosis

## One-Sentence Summary

Isosorbide mononitrate is an oral organic nitrate vasodilator. The Evidence Pack contains no indication text for it, so its use in angina prevention comes from general drug knowledge.
The TxGNN model predicts it may be effective for **hypertrichosis (excessive hair growth)**, but this is a model prediction only, with **0 clinical trials** and **0 publications** supporting it.
The mechanistic link is not credible: excessive hair growth would more plausibly be an adverse-effect signal than a treatment target.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Evidence Pack (generally used for angina prevention) |
| Predicted New Indication | Hypertrichosis (disease) |
| TxGNN Prediction Score | 99.995% (rank 269) |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 (NDA and ANDA authorizations combined) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Isosorbide mononitrate is an organic nitrate. Drugs in this class act as nitric oxide (NO) donors, activating soluble guanylate cyclase (sGC) to relax vascular smooth muscle. This vasodilation is the basis of its established cardiovascular use.

The predicted indication is a hair-growth excess phenotype. No mechanistic link can be established from the provided data. Nothing connects nitrate vasodilation or NO signaling to the biology of hypertrichosis. If anything, the prediction looks more like a potential adverse-effect signal than a therapeutic opportunity.

The score is high, but it comes from knowledge-graph patterns alone. It is not backed by trials, literature, or a known mechanism, so it should be treated as a hypothesis-generating signal at best.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA210822 | Isosorbide Mononitrate | Tablet, extended release | Chartwell RX, LLC |
| ANDA210918 | Isosorbide Mononitrate | Tablet, extended release | Ingenus Pharmaceuticals, LLC |
| NDA020215 | Isosorbide mononitrate | Tablet | Proficient Rx LP |
| ANDA075522 | Isosorbide Mononitrate | Tablet, extended release | NuCare Pharmaceuticals, Inc. |
| ANDA210918 | Isosorbide Mononitrate | Tablet, extended release | Aphena Pharma Solutions - Tennessee, LLC |

Both listed forms are oral. The Evidence Pack does not include approved indication text for these authorizations.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical trials, no literature, and no plausible mechanism, so it stays at evidence level L5. The predicted disease is also more consistent with a side-effect signal than a treatment target. Related predictions for this drug (Ambras syndrome, alopecia, hypotrichosis and others) are equally unsupported. The only candidate with indirect biological support is **pulmonary arterial hypertension**, ranked 10th at evidence level L4. Its support is preclinical and hemodynamic studies in other populations, with no PAH patient data. It is better treated as a separate research question than as support for this hypertrichosis prediction.

**To proceed, the following is needed:**
- Mechanism of action data from DrugBank, to allow a proper mechanistic-link analysis
- Package insert warnings and contraindications, which are needed before any safety screening
- Approved indication text for the US authorizations, to confirm the original indication
- A pharmacovigilance check of whether hair-growth changes are reported with isosorbide mononitrate, to test the adverse-effect-signal interpretation
- Any human or preclinical study linking nitrate or NO-sGC signaling to hair follicle biology. Without one, this prediction should not advance.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

