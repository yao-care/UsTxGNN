---
layout: default
title: Meclizine
parent: Model Prediction Only (L5)
nav_order: 893
evidence_level: L5
indication_count: 6
---

# Meclizine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

# Meclizine: From Motion Sickness to Allergic Urticaria

## One-Sentence Summary

Meclizine is an oral antihistamine-class drug marketed in the US, and its product labels (e.g., "Motion Sickness Relief", Dramamine) point to motion sickness use.
The TxGNN model predicts it may be effective for **allergic urticaria**,
but there are currently **0 clinical trials** and **0 publications** supporting this specific prediction, so it rests on model prediction alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Motion sickness (inferred from product names; no approved indication text was supplied) |
| Predicted New Indication | Allergic urticaria |
| TxGNN Prediction Score | 99.67% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 licenses in total (mix of NDA, ANDA and OTC monograph products) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Meclizine is generally known as a first-generation H1 antihistamine, and its efficacy in its original use is established. Mechanistically, it may be applicable to histamine-mediated conditions such as allergic urticaria. This link is inferred from drug class and is not supported by data in the Evidence Pack.

Allergic urticaria is driven by histamine release, and H1 antihistamines are the standard drug class for it. That makes the prediction biologically plausible. The very high TxGNN score (0.997) is a model output only. It is not confirmation of clinical benefit.

Better-characterized antihistamines are already available for urticaria. Any development case for meclizine would need to show a clear advantage over them.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for allergic urticaria.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| M009 | Dramamine Less Drowsy Meclizine Hydrochloride | Tablet | — |
| NDA010721 | Meclizine Hydrochloride | Tablet | — |
| ANDA213957 | Meclizine Hydrochloride | Tablet | — |
| part336 | Motion Sickness Relief | Tablet, chewable | — |
| M009 | Meclizine Hydrochloride | Tablet, chewable | — |

Approved indication text was not included in the supplied records. All available forms are oral (tablet, chewable tablet, film-coated tablet).

---

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found in the supplied data.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is mechanistically plausible but has no supporting trials or literature (L5, model prediction only). The next-ranked candidate, common cold, has one linked trial (NCT01537471), but it studies pre-pulse inhibition rather than the cold, so it gives no support either. Meclizine would also have to compete with established antihistamines for urticaria.

**To proceed, the following is needed:**
- Mechanism of action data (e.g., H1 receptor affinity and anticholinergic profile)
- Package insert warnings and contraindications for safety screening
- A literature and trial search specific to meclizine in urticaria
- A comparison against standard antihistamines for urticaria to define any differentiated value
- Approved indication text for the US labels, to confirm the original indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

