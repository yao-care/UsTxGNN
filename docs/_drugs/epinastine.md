---
layout: default
title: Epinastine
parent: Model Prediction Only (L5)
nav_order: 659
evidence_level: L5
indication_count: 2
---

# Epinastine
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

# Epinastine: From Allergic Conjunctivitis to Rosacea Conjunctivitis

## One-Sentence Summary

Epinastine is an antihistamine eye drop, marketed in the US for allergic conjunctivitis.
The TxGNN model predicts it may be effective for **rosacea conjunctivitis**, but **0 clinical trials** and **0 publications** currently support this specific prediction, so it rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Allergic conjunctivitis (ophthalmic use; the license record has no indication text) |
| Predicted New Indication | Rosacea conjunctivitis |
| TxGNN Prediction Score | 99.57% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 1 (listed as ANDA090951) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the database. Based on known information, epinastine is an H1 receptor antagonist with mast cell stabilizing activity. Its efficacy in allergic conjunctivitis is established, so it may relieve symptoms such as itching in other inflamed eye conditions.

The link to rosacea conjunctivitis is weak. Ocular rosacea is driven mainly by meibomian gland dysfunction, eyelid inflammation, and microbial or *Demodex* factors, with little histamine involvement. An antihistamine could at most ease itch or irritation, and it would not treat the underlying disease. The very high model score therefore reflects a network-level association, not a supported biological rationale.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA090951 | Epinastine Hydrochloride (Somerset Therapeutics, LLC) | Solution/drops | Not listed in the source record |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a very high model score but no trials or literature, and the ocular rosacea mechanism has little histamine involvement. It is a prediction-only candidate at evidence level L5.

**To proceed, the following is needed:**
- Any preclinical or clinical evidence linking epinastine to ocular rosacea, such as symptom-relief studies (itch, irritation)
- Detailed mechanism of action data (MOA)
- The US package insert warnings and contraindications, to complete safety screening
- Confirmation of the approved indication text for the marketed ophthalmic product
- Consideration of the second-ranked prediction, **allergic urticaria**. It has 2 completed post-marketing surveillance studies (about 5,800 patients, observational) and supporting literature, reaching L3. Its status as true repurposing should be confirmed against regional labeling, since oral epinastine is already marketed for allergic conditions elsewhere.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

