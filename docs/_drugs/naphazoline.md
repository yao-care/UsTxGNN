---
layout: default
title: Naphazoline
parent: Model Prediction Only (L5)
nav_order: 953
evidence_level: L5
indication_count: 10
---

# Naphazoline
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

# Naphazoline: From Topical Decongestant to Hypotrichosis Simplex of the Scalp

## One-Sentence Summary

Naphazoline is a topical vasoconstrictor sold in nasal spray and liquid products. Its label indication text was not included in the data received.
The TxGNN model predicts it may be effective for **hypotrichosis simplex of the scalp**, but **0 clinical trials** and **0 publications** support this prediction.
It is a model-only prediction, and known pharmacology argues against it.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the license records (generally a topical decongestant) |
| Predicted New Indication | Hypotrichosis simplex of the scalp |
| TxGNN Prediction Score | 99.83% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Naphazoline is generally known as an alpha-adrenergic imidazoline agonist that constricts blood vessels when applied topically. That is why it is used in nasal and ocular decongestant products.

This mechanism does not plausibly support hair growth. Reduced scalp blood flow would, if anything, work against it. The very high TxGNN score is most likely a knowledge-graph artifact, meaning shared gene or pathway neighbors rather than real pharmacology.

The other top predictions point the same way:
- Several are hair-related (alopecia, diffuse alopecia areata, hypotrichosis milia).
- Hypertrichosis is predicted too, which is the opposite direction to the alopecia predictions.
- Both suggest a nonspecific similarity signal, not a real effect.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

The license records contain no approved indication text. The 5 main authorizations of 20 are listed below.

| Authorization Number | Product Name | Dosage Form |
|---------|------|------|
| M012 | SERYNTH FAST RELIEF NASAL | Spray |
| M012 | SKAPEMED ORIGINAL NASAL | Liquid |
| M012 | Seacall Nasal Spray. | Spray |
| M012 | DERMFREE ORIGINAL NASAL | Spray |
| M012 | Nazal | Liquid |

All marketed forms are sprays, liquids, or solution/drops. None is a scalp product.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model score alone. No trials or literature support it, and vasoconstrictor pharmacology gives no reason to expect a hair-growth benefit. The available formulations are also not scalp-directed.

**To proceed, the following is needed:**
- The US package insert (warnings, contraindications), which is a blocking gap for safety screening
- Detailed mechanism of action data (MOA) from DrugBank
- Any preclinical or clinical evidence for naphazoline specifically in hair disorders
- A route and formulation feasibility check for scalp application
- Consideration of other candidates. The scored predictions (e.g., open-angle glaucoma) have equally weak support, and the periodontitis literature retrieved for one of them is generic disease-term matching, not naphazoline evidence.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

