---
layout: default
title: Desonide
parent: Model Prediction Only (L5)
nav_order: 587
evidence_level: L5
indication_count: 10
---

# Desonide
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

# Desonide: From Inflammatory Skin Conditions to Polyp of Vocal Cord

## One-Sentence Summary

Desonide is a low-potency topical corticosteroid marketed in the US as creams, lotions and ointments. The supplied license records do not include its approved indication text.
The TxGNN model predicts it may be effective for **polyp of vocal cord**, but **0 clinical trials** and **0 publications** currently support this direction, so this is a model prediction only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the supplied license records (desonide is a low-potency topical corticosteroid) |
| Predicted New Indication | Polyp of vocal cord |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 (all shown are ANDA generic approvals) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Desonide is a low-potency topical corticosteroid, so a general anti-inflammatory effect is the only plausible rationale. No desonide-specific data was supplied to support it for this condition.

The top 10 TxGNN predictions are all polyp-type lesions at very different sites: vocal cord, middle ear, external auditory canal, frontal sinus, ureter, vulva, uterus and others. The scores are nearly identical (99.90–99.91%). This pattern suggests the model is picking up a broad "corticosteroid and polyp" association rather than a desonide-specific signal.

The main problem for vocal cord polyps is delivery. Desonide is marketed only as topical dermatologic products (cream, lotion, ointment), and these cannot reach the vocal cord. Vocal cord polyps are also usually managed with voice therapy or surgery. Route compatibility has not been assessed.

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
| ANDA073548 | Desonide (Northstar Rx) | Cream | Not provided in the record |
| ANDA213632 | Desonide (Alembic) | Lotion | Not provided in the record |
| ANDA210198 | Desonide (Bryant Ranch Prepack) | Cream | Not provided in the record |
| ANDA074254 | Desonide (Northstar Rx) | Ointment | Not provided in the record |
| ANDA210198 | Desonide (Viona) | Cream | Not provided in the record |

Of the 20 licenses in total, only the first 5 are listed here.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model output alone (L5). There are no trials or publications, and the mechanism data is missing. The marketed topical products cannot plausibly reach the predicted sites, and the polyp types are highly diverse. Safety information also has not been collected.

**To proceed, the following is needed:**
- Package insert warnings and contraindications, which block any safety screening
- Mechanism of action data (e.g., from DrugBank)
- Approved indication text for the US licenses
- A route-of-administration assessment for the predicted sites
- Evidence of local corticosteroid use in polyp disease, followed by a literature search focused on the most accessible sites (external auditory canal, vulva)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

