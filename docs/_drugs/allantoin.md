---
layout: default
title: Allantoin
parent: Model Prediction Only (L5)
nav_order: 224
evidence_level: L5
indication_count: 8
---

# Allantoin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **8** 
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

# Allantoin: From Topical Skin Protection to Severe Nonproliferative Diabetic Retinopathy

## One-Sentence Summary

Allantoin is a topical skin protectant and keratolytic agent, found mainly in scar-care and skin-care products.
The TxGNN model predicts it may be effective for **severe nonproliferative diabetic retinopathy**, but there are currently **0 clinical trials** and **0 publications** for this indication, so the prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the license data (marketed as a topical skin protectant and scar-care ingredient) |
| Predicted New Indication | Severe nonproliferative diabetic retinopathy |
| TxGNN Prediction Score | 99.56% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 licenses in total (the listed examples are OTC monograph or 505G numbers, not NDAs) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Allantoin is used in topical products for skin protection, softening and wound or scar care. It has no known ocular or retinal vascular activity.

Diabetic retinopathy is a microvascular disease of the retina, which is biologically far from the skin conditions allantoin is used for. The high score (rank 10,909 in the model) most likely reflects proximity in the knowledge graph rather than a real pharmacological link. No plausible mechanism was identified.

Route compatibility has not been assessed. All listed products are topical or skin-applied (gel, cream, oil), and none is designed for ocular or systemic delivery.

For context, the other top predictions are also mostly skin-related conditions (for example acne keloidalis and acrodermatitis chronica atrophicans). Only the rank 8 prediction, exanthem, has any registered trials, and those are indirect (see Conclusion).

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| M016 | Earthmed Sport massage oil | Oil | Not stated |
| M017 | Walgreens Advanced Scar Gel | Gel | Not stated |
| 505G(a)(3) | TriDerma Protect Heal Non Greasy Barrier Cream | Cream | Not stated |
| M016 | Meijer Scar Gel | Gel | Not stated |
| M016 | Mederma for Kids | Gel | Not stated |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a very high model score but no trials, no literature and no plausible mechanism for a retinal disease. A topical skin product is also an unlikely fit for this indication. The only predicted indication with any trial data is exanthem (rank 8: three non-phase-specific or terminated trials of multi-ingredient products, with n=5 to 159). That evidence is indirect and cannot isolate allantoin's contribution.

**To proceed, the following is needed:**
- Mechanism of action data (for example from DrugBank) and any biological link to retinal microvascular disease
- Package insert warnings and contraindications, which are needed before any safety screening
- A route-compatibility assessment (topical products versus ocular or systemic delivery)
- A literature search specific to allantoin and diabetic retinopathy, since none was found
- If the team wants to pursue a skin indication instead, verification that allantoin is actually present in the products tested in the rank 8 trials
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

