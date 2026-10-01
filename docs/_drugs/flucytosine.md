---
layout: default
title: Flucytosine
parent: Model Prediction Only (L5)
nav_order: 714
evidence_level: L5
indication_count: 1
---

# Flucytosine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

# Flucytosine: From Antifungal Therapy to Bone Paget Disease

## One-Sentence Summary

Flucytosine is an oral antifungal prodrug that is marketed in the United States as generic capsules.
The TxGNN model predicts it may be effective for **bone Paget disease**, but **no clinical trials and no publications** currently support this direction, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Bone Paget disease |
| TxGNN Prediction Score | 99.04% |
| Evidence Level | L5 (model prediction only) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 licenses (the five listed below are all ANDAs) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the source record. Flucytosine is known as an antifungal prodrug: fungal cytosine deaminase converts it to 5-fluorouracil, which disrupts fungal RNA and DNA synthesis. Mammalian cells have little of this enzyme, so the drug has no known direct effect on human cells.

Paget disease of bone is driven by dysregulated osteoclast activity (for example, SQSTM1 variants) and is treated with bisphosphonates. Flucytosine has no known effect on osteoclast or osteoblast biology, so **no credible mechanistic link to Paget disease has been established**. A pyrimidine-antimetabolite pathway in the knowledge graph may explain the association, but this is speculative and untested.

The high score (99.04%, model rank 20,705) is a knowledge-graph prediction only. It should not be read as clinical support.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA212632 | Flucytosine | Capsule | Heritage Pharmaceuticals Inc. d/b/a Avet Pharmaceuticals Inc. |
| ANDA201566 | Flucytosine | Capsule | Sigmapharm Laboratories, LLC |
| ANDA204652 | Flucytosine | Capsule | AvPAK |
| ANDA204652 | Flucytosine | Capsule | Lupin Pharmaceuticals, Inc. |

Only oral capsules are listed.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting trials or literature (Evidence Level L5). There is also no plausible biological link between an antifungal prodrug and osteoclast-driven Paget disease, whose standard treatment is bisphosphonates. Current data do not justify further investment.

**To proceed, the following is needed:**
- Package insert warnings and contraindications, which are currently missing and block safety screening
- Detailed mechanism of action and original indication data from DrugBank
- Preclinical or mechanistic evidence linking flucytosine or its metabolite to bone remodelling
- Any published or registered studies in Paget disease of bone
- A route and dosage-form compatibility assessment (not yet performed)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

