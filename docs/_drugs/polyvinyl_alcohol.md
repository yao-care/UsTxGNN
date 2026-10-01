---
layout: default
title: Polyvinyl Alcohol
parent: Model Prediction Only (L5)
nav_order: 1063
evidence_level: L5
indication_count: 4
---

# Polyvinyl Alcohol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

# Polyvinyl Alcohol: From Ocular Lubrication to Congenital Ichthyosiform Erythroderma

## One-Sentence Summary

Polyvinyl alcohol is a water-soluble, film-forming polymer sold in the US as a lubricating eye drop.
The TxGNN model predicts it may be effective for **congenital ichthyosiform erythroderma**, a rare inherited skin disorder.
The prediction has **0 clinical trials** and **0 publications** behind it, so it rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Ocular lubrication (inferred from product names such as "Lubricating Eye Drops"; no approved indication text is on file) |
| Predicted New Indication | Congenital ichthyosiform erythroderma |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L5 (model prediction only) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 licenses on record |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, polyvinyl alcohol is a film-forming polymer used mainly as an ophthalmic lubricant and as a pharmaceutical excipient. Its role in eye drops is to coat the surface and keep it moist.

The link to ichthyosis is speculative. A topical film could in theory limit water loss through the skin and soften hyperkeratotic (thickened, scaly) skin. Existing emollients and keratolytics already do this, and nothing suggests polyvinyl alcohol adds benefit. The very high TxGNN score (99.90%) most likely reflects closeness in the knowledge graph to generic polymer or emollient nodes, not a demonstrated therapeutic effect.

The model also ranked three related conditions: self-healing collodion baby (99.83%), lamellar ichthyosis (99.72%) and bathing suit ichthyosis (99.54%). All are at the same L5 level with no trials or literature. For collodion baby, a synthetic polymer film on newborn skin would also raise safety questions.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

The five entries below are the main authorizations of the 20 on record. None has approved indication text on file, so the indication column reflects the product names only.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| M018 | Polyvinyl Alcohol (A-S Medication Solutions) | Solution/drops | Not stated (ophthalmic product) |
| M018 | Rugby Polyvinyl Alcohol 1.4% Lubricating Eye Drops | Solution/drops | Not stated (lubricating eye drops) |
| M018 | Rugby Lubricating Drops | Solution/drops | Not stated (lubricating eye drops) |
| M018 | Polyvinyl Alcohol (AvPAK) | Solution/drops | Not stated (ophthalmic product) |
| M018 | Walgreens Soothing Eye Relief Lubricant Eye Drops | Solution/drops | Not stated (lubricant eye drops) |

---

## Safety Considerations

Please refer to the package insert for safety information.

The rationale notes one open concern: applying a synthetic polymer film to neonatal skin, as in collodion baby, would need dedicated safety evaluation. Every marketed product is an eye-drop formulation, so no skin-route product or safety data exists for this use.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical trials, no literature and no established mechanism, and it sits at the lowest evidence level (L5). Existing emollients and keratolytics already address the same skin problem. The high TxGNN score alone does not justify moving forward.

**To proceed, the following is needed:**
- Mechanism of action data for polyvinyl alcohol, to test whether a barrier effect is plausible in ichthyosis
- Package insert warnings and contraindications
- A skin-route (topical) formulation and a route compatibility assessment, since all current products are eye drops
- Preclinical or small exploratory studies of skin barrier function against standard emollients
- A neonatal safety assessment before any consideration of self-healing collodion baby
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

