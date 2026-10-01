---
layout: default
title: Diroximel Fumarate
parent: Model Prediction Only (L5)
nav_order: 614
evidence_level: L5
indication_count: 10
---

# Diroximel Fumarate
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

# Diroximel Fumarate: From an Unspecified Original Indication to Diabetic Cataract

## One-Sentence Summary

Diroximel fumarate is marketed in the US as Vumerity (an oral capsule from Biogen), but the supplied data does not list an approved indication.
The TxGNN model predicts it may be effective for **diabetic cataract**,
but **0 clinical trials** and **0 publications** currently support this direction, so it is a model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the supplied data (approved indication text is empty) |
| Predicted New Indication | Diabetic cataract |
| TxGNN Prediction Score | 99.999% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available, and the approved indication is also missing from the supplied data. The prediction therefore cannot be tied to a documented original use.

One hypothesis, which comes from outside the supplied data and is unverified: diroximel fumarate is a prodrug of monomethyl fumarate, an Nrf2 pathway activator. Oxidative stress and polyol-pathway injury are involved in diabetic lens opacity, so an antioxidant mechanism could plausibly be relevant. No trial or publication supports this link.

The score should be read with caution. Nine of the ten top predictions are cataract or diabetic eye conditions, including rare subtypes such as tetanic and craniostenosis cataract. This suggests the score largely reflects proximity to a cluster of cataract nodes in the knowledge graph rather than drug-specific biology.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA211855 | Vumerity | Capsule (oral) | Not provided in the supplied data |

## Other Predicted Indications

All have TxGNN scores of about 99.999% and evidence level L5, with no trials or literature.

| Rank | Predicted Indication | Recommendation | Comment |
|------|------|------|------|
| 2 | Diabetic retinopathy | Research Question | Same unverified Nrf2 hypothesis (oxidative stress and inflammation in the retina) |
| 3 | Severe nonproliferative diabetic retinopathy | Hold | Subtype, covered by the diabetic retinopathy question |
| 4 | Tetanic cataract | Hold | No plausible link, likely a graph artifact |
| 5 | Immature cataract | Hold | Generic stage, no drug-specific evidence |
| 6 | Craniostenosis cataract | Hold | Rare syndromic cataract, likely a graph artifact |
| 7 | Nuclear senile cataract | Hold | Speculative oxidative-stress link only |
| 8 | Cortical cataract | Hold | Likely graph proximity only |
| 9 | Diabetes mellitus type 2 associated cataract | Hold | Overlaps with diabetic cataract |
| 10 | Mature cataract | Hold | Advanced stage, usually treated surgically |

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found in the queried data.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on the model score alone (L5), with no trials, no literature, and no mechanism of action or original indication in the data. The similarity of the top-ranked predictions suggests a knowledge-graph cluster effect rather than drug-specific evidence.

**To proceed, the following is needed:**
- The Vumerity package insert (approved indication, warnings, contraindications), which is blocking for safety screening
- Mechanism of action data (for example from DrugBank)
- Preclinical evidence that Nrf2 activation affects diabetic lens or retinal injury
- A literature and trial search for diabetic cataract and diabetic retinopathy
- Assessment of whether the oral route is suitable for an ocular indication

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

