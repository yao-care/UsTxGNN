---
layout: default
title: Vismodegib
parent: Model Prediction Only (L5)
nav_order: 1294
evidence_level: L5
indication_count: 10
---

# Vismodegib
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

# Vismodegib: From Basal Cell Carcinoma to Medulloblastoma with Extensive Nodularity

## One-Sentence Summary

Vismodegib is an oral Hedgehog pathway inhibitor, known from the literature to be approved for advanced basal cell carcinoma (BCC).
The TxGNN model predicts it may be effective for **medulloblastoma with extensive nodularity (MBEN)**,
but there are currently **0 clinical trials** and **0 publications** linked to this prediction, so it rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Locally advanced or metastatic basal cell carcinoma (not stated in the license record; taken from the literature) |
| Predicted New Indication | Medulloblastoma with extensive nodularity |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the structured drug record. From the literature, vismodegib binds Smoothened (SMO) and blocks the Hedgehog signaling pathway. This pathway is the main oncogenic driver of basal cell carcinoma.

MBEN is a medulloblastoma subtype that is typically associated with sonic hedgehog (SHH) pathway activation. That fits SMO inhibition, so the prediction is plausible, but it is unproven.

MBEN occurs mainly in infants and young children. SMO inhibitors carry a known risk of growth-plate toxicity in this age group, which could limit use. The prediction needs a dedicated literature and trial search before it can advance.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA203388 | ERIVEDGE (Genentech, Inc.) | Capsule (oral) | Not listed in the input |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (Hedgehog/SMO inhibitor), not a conventional cytotoxic |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

- **Class toxicities (from the evidence pack rationale)**: muscle spasm, alopecia, dysgeusia, and teratogenicity need risk management.
- **Pediatric risk**: Hedgehog inhibitors carry a risk of premature growth-plate closure. This matters here because MBEN mainly affects infants and young children.

Please refer to the package insert for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a very high model score and a plausible SHH-pathway link. However, no trials or publications support it, and the likely patient population (infants and young children) raises a known growth-plate safety concern.

**To proceed, the following is needed:**
- A dedicated literature and clinical trial search on vismodegib or SMO inhibitors in MBEN and SHH-subgroup medulloblastoma
- The package insert warnings and contraindications, which are currently missing
- An assessment of pediatric growth-plate toxicity
- Detailed mechanism of action data from DrugBank

**Other predicted indications:**
- **Xeroderma pigmentosum** has case-report evidence (Evidence Level L4). Vismodegib was used there to treat BCC, not the underlying DNA-repair defect.
- **Skin cancer** has Phase 2 trials (Evidence Level L2). It is probably an existing BCC indication rather than true repurposing, so verify it against the label.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

