---
layout: default
title: Flortaucipir F-18
parent: Model Prediction Only (L5)
nav_order: 711
evidence_level: L5
indication_count: 10
---

# Flortaucipir F-18
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

# Flortaucipir F-18: From Diagnostic Tau PET Imaging to Anaphylaxis

## One-Sentence Summary

Flortaucipir F-18 is a PET radiotracer that binds tau aggregates in the brain. It is marketed in the US as TAUVID for diagnostic imaging, not as a treatment.
The TxGNN model predicts it may be effective for **anaphylaxis**, but **0 clinical trials** and **0 publications** support this, so the prediction is very likely a knowledge-graph artifact.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Diagnostic tau PET imaging (no approved indication text in the record) |
| Predicted New Indication | Anaphylaxis |
| TxGNN Prediction Score | 98.20% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

It is not, based on the available information. Detailed mechanism of action data is not available for this drug. Flortaucipir F-18 is a diagnostic radiotracer that binds tau aggregates. It has no known antiallergic, mast-cell-stabilizing or vasopressor activity.

The high score of 0.982 most likely comes from the structure of the knowledge graph. The drug has no curated mechanism and no original therapeutic indications, so the model may be relying on graph proximity rather than biology. A diagnostic tracer given in microdose amounts is also not a credible treatment for an acute emergency like anaphylaxis.

The other top predictions show the same pattern. Related allergy terms (food-dependent exercise-induced anaphylaxis, pseudoallergy) closely track the anaphylaxis signal. Hematologic malignancies (hairy cell leukemia and its variant, primary bone lymphoma, early T cell progenitor ALL) cluster together. Skin disease, hereditary neurocutaneous angioma and placental hemangioma make up the rest. All ten predictions are L5 (model prediction only), with no trials or publications, and none has a plausible therapeutic mechanism.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| NDA212123 | TAUVID | Injection, solution | Eli Lilly and Company |

## Safety Considerations

Please refer to the package insert for safety information.

For the placental hemangioma prediction, radiotracer exposure in pregnancy would raise safety concerns that would need separate assessment.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The anaphylaxis prediction has no clinical, literature or mechanistic support, and the drug is a diagnostic imaging agent with no therapeutic pharmacology. The score reflects a probable graph artifact and does not justify further investment.

**To proceed, the following is needed:**
- Mechanism of action data for flortaucipir F-18
- Package insert warnings and contraindications, currently a blocking gap for safety screening
- Any independent clinical or preclinical evidence linking the drug to anaphylaxis
- Route and dose compatibility assessment: a microdose injectable diagnostic versus the requirements of an acute anaphylaxis treatment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

