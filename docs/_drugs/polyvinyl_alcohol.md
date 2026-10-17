---
layout: default
title: Polyvinyl Alcohol
parent: Model Prediction Only (L5)
nav_order: 1063
evidence_level: L5
indication_count: 4
monitor_inn: "POLYVINYL ALCOHOL"
predicted_indications: ["congenital ichthyosiform erythroderma", "self-healing collodion baby", "lamellar ichthyosis", "bathing suit ichthyosis"]
last_modified_at: 2026-10-14
description: "Polyvinyl Alcohol: predicted new indication Congenital ichthyosiform erythroderma (evidence level L5). Approved use: Dry eye syndrome, xerophthalmia"
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

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

# Polyvinyl Alcohol: From Dry Eye Syndrome to Congenital Ichthyosiform Erythroderma

## One-Sentence Summary

Polyvinyl alcohol is a polymer used in lubricating eye drops, originally for dry eye syndrome (xerophthalmia).
The TxGNN model predicts it may be effective for **Congenital Ichthyosiform Erythroderma** (and three related ichthyosis conditions), but there are currently **0 clinical trials** and **0 publications** supporting this direction. This is a computational prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Dry eye syndrome, xerophthalmia (from the knowledge graph; no approved indication text on the US license record) |
| Predicted New Indication | Congenital ichthyosiform erythroderma |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L5 |
| US Market Status | Cancelled only |
| Number of NDAs | 1 |
| Recommended Decision | Hold |

Other predicted indications, all L5 and Hold:

| Rank | Predicted Indication | TxGNN Score |
|------|------|------|
| 2 | Self-healing collodion baby | 99.83% |
| 3 | Lamellar ichthyosis | 99.72% |
| 4 | Bathing suit ichthyosis | 99.54% |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, polyvinyl alcohol is a film-forming, hydrating polymer used as a lubricant in eye drops. Its benefit in dry eye comes from its moisture-retaining, protective properties, and mechanistically it might be applicable to dry, scaling skin conditions.

The predicted conditions are inherited disorders of skin keratinization (for example, mutations in TGM1, ALOXE3 or ALOX12B). A topical film-forming polymer could plausibly act as an occlusive or emollient layer and provide temporary relief of dryness and scaling. This would be symptomatic only and would not address the underlying genetic defect. There is also no data showing any advantage over established emollients and keratolytics.

Specific caveats for the other predictions:
- **Self-healing collodion baby:** the condition resolves on its own, so any benefit would be hard to separate from natural recovery. Use on neonates with impaired skin barrier also raises percutaneous absorption and safety questions that have not been evaluated.
- **Lamellar ichthyosis and bathing suit ichthyosis:** both are TGM1-related. Hydration and occlusion are standard supportive care, so the idea is conceptually consistent, but unsupported by data.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| M018 (cancelled) | Polyvinyl Alcohol (A-S Medication Solutions) | Solution / drops | Not stated on the license record |

The only US authorization is cancelled, and there are no currently valid licenses. This limits practical development.

## Safety Considerations

The data compiled for this report includes no label-based warnings or contraindications, and no drug interactions were found. Please refer to the package insert for safety information.

The knowledge graph links the drug to the following conditions as contraindication relationships. These come from a computational resource, not from label text, and should be verified:
- **Cardiovascular:** hypertension, heart disease, cardiovascular disease, coronary artery disease, sudden cardiac arrest, heart conduction disease, arteriosclerosis, atherosclerosis
- **Metabolic and endocrine:** diabetes mellitus, diabetic ketoacidosis, hyperthyroidism, Graves disease, thyrotoxicosis
- **Other:** benign prostatic hyperplasia, angle-closure glaucoma

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score, with no clinical trials or publications. The mechanistic link is speculative and symptomatic at best, and the only US authorization is cancelled.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Preclinical or clinical evidence of benefit in ichthyosis, compared with standard emollients
- Safety and percutaneous absorption assessment for topical use, especially in neonates with impaired skin barrier
- Assessment of route and formulation compatibility (the current product is an ophthalmic solution, while the predicted use is dermatological)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

