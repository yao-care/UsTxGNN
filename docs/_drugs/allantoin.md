---
layout: default
title: Allantoin
parent: Model Prediction Only (L5)
nav_order: 224
evidence_level: L5
indication_count: 8
monitor_inn: "ALLANTOIN"
predicted_indications: ["severe nonproliferative diabetic retinopathy", "acrodermatitis chronica atrophicans", "neonatal dermatomyositis", "acne keloid", "secondary interstitial lung disease specific to childhood associated with a connective tissue disease", "amyopathic dermatomyositis", "hydroa vacciniforme, familial", "exanthem (disease)"]
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

# Allantoin: From Psoriasis and Dermatitis to Severe Nonproliferative Diabetic Retinopathy

## One-Sentence Summary

Allantoin is a topical skin-care ingredient, listed in the knowledge graph for psoriasis, seborrheic dermatitis and related skin conditions.
The TxGNN model predicts it may be effective for **severe nonproliferative diabetic retinopathy**,
but **0 clinical trials** and **0 publications** currently support this direction, so it remains a model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Psoriasis, parapsoriasis, seborrheic dermatitis, pityriasis simplex, dermatitis, seborrheic keratosis (from the knowledge graph; no approved indication text is available in the US license records) |
| Predicted New Indication | Severe nonproliferative diabetic retinopathy |
| TxGNN Prediction Score | 99.56% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (no currently valid listings) |
| Number of NDAs | 4 (all cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Allantoin is known as a topical keratolytic and wound-healing agent used in dermatologic and skin-care products, and nothing in the data compiled for this report connects it to retinal microvascular disease.

The high TxGNN score is a knowledge-graph prediction only. Using allantoin for diabetic retinopathy would require systemic or intravitreal delivery, which is far from its topical dermatologic profile. The prediction is therefore not mechanistically supported at this time.

**Other predicted indications (all L5, all Hold):**

| Rank | Predicted Disease | TxGNN Score | Comment |
|------|------|------|------|
| 2 | Acrodermatitis chronica atrophicans | 99.50% | Late-stage Lyme skin manifestation. Causal treatment is antibiotics, so at most symptomatic skin care is conceivable. |
| 3 | Neonatal dermatomyositis | 99.48% | Immune-mediated disease. No immunomodulatory mechanism documented, and neonatal safety is unassessed. |
| 4 | Acne keloid | 99.48% | The most biologically plausible, since allantoin is used in scar products. The link is still hypothetical. |
| 5 | Secondary childhood interstitial lung disease with connective tissue disease | 99.44% | No pulmonary activity documented. Pediatric safety and lung delivery are unaddressed. |
| 6 | Amyopathic dermatomyositis | 99.43% | Skin-limited presentation overlaps with allantoin's dermatologic scope, but the underlying autoimmune process would not be addressed. |
| 7 | Hydroa vacciniforme, familial | 99.23% | Rare photosensitive disorder. At most non-specific symptomatic benefit. |
| 8 | Exanthem (disease) | 99.10% | Non-specific rash. Any benefit would be limited to skin soothing. |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| M016 | Earthmed Sport massage oil | Oil | Not specified (cancelled) |
| M017 | Walgreens Advanced Scar Gel | Gel | Not specified (cancelled) |
| 505G(a)(3) | TriDerma Protect Heal Non Greasy Barrier Cream | Cream | Not specified (cancelled) |
| nan | LESONEL FEMININE FOAMING WASH | Liquid | Not specified (cancelled) |

All four listings are cancelled, and none is a currently valid product.

## Safety Considerations

The package insert warnings and contraindications could not be retrieved for this report, so please refer to the package insert for safety information.

The knowledge graph links allantoin to the following contraindication-related conditions. These come from graph edges rather than label text and should be verified:
- **Metabolic and porphyria disorders**: inherited porphyria, porphyrin metabolism disease, porphyria, G6PD deficiency, glycogen storage disease, cystinuria, galactosemia
- **Organ disease**: kidney disease, pyoureter, hematologic disease, liver disease, gallbladder disease
- **Skin conditions**: folliculitis, seborrheic dermatitis, dermatitis

Note that seborrheic dermatitis and dermatitis appear both as original indications and as graph contraindications, an inconsistency that needs clarification.

No drug interaction records were found.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a knowledge-graph score, with no clinical trials, no literature, and no established mechanism. The drug is a topical dermatologic agent with no valid US listings, and the proposed retinal use would need a completely different delivery route.

**To proceed, the following is needed:**
- Mechanism of action data (MOA) for allantoin
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Resolution of the inconsistency between original indications and graph contraindications
- Route-compatibility assessment for each predicted indication
- For a more plausible lead such as acne keloid, a dedicated preclinical or small pilot study before any recommendation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

