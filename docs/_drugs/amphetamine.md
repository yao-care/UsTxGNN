---
layout: default
title: Amphetamine
parent: Model Prediction Only (L5)
nav_order: 334
evidence_level: L5
indication_count: 5
---

# Amphetamine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

# Amphetamine: From ADHD and Narcolepsy to Faciodigitogenital Syndrome

## One-Sentence Summary

Amphetamine is a central nervous system stimulant marketed in the US, and the published literature in the pack describes its use for ADHD and narcolepsy.
The TxGNN model predicts it may be effective for **Faciodigitogenital Syndrome** (a rare X-linked developmental disorder) with a very high score.
This prediction has **0 clinical trials** and **0 publications** supporting it, so it is a model output only.

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Faciodigitogenital syndrome |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is currently not available in the Evidence Pack. Amphetamine acts as a monoamine-releasing stimulant, and its efficacy in attention and arousal disorders is established. The supplied license records do not include approved-indication text.

No plausible link connects the two conditions. Faciodigitogenital syndrome is a rare developmental disorder linked to the FGD1 gene, and nothing in the supplied data suggests that dopamine or norepinephrine release would affect it. The score of 99.97% is best treated as a knowledge-graph artifact until independent evidence appears.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form |
|---------|------|------|
| ANDA211861 | Amphetamine Sulfate (Solco Healthcare US, LLC) | Tablet |
| NDA204326 | Amphetamine Extended-Release (Neos Therapeutics, LP) | Tablet, orally disintegrating |
| ANDA200166 | Amphetamine Sulfate (Bryant Ranch Prepack) | Tablet |
| ANDA212901 | Amphetamine Sulfate (Bryant Ranch Prepack) | Tablet |
| ANDA211139 | Amphetamine Sulfate (Amneal Pharmaceuticals NY LLC) | Tablet |

The 20 authorizations include both NDAs and ANDAs. All available forms are oral (tablet, orally disintegrating tablet, extended-release tablet).

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone. There are no trials or publications, and no mechanistic link to a rare FGD1-related developmental disorder.

**To proceed, the following is needed:**
- Package insert warnings and contraindications, which are currently missing and block safety screening
- Detailed mechanism of action data
- Any independent biological or clinical evidence connecting monoamine release to FGD1-related pathology
- Review of the other TxGNN predictions for this drug. "Specific developmental disorder" (rank 3) likely overlaps with ADHD and neurodevelopmental conditions, so it may be a better research question. Trichotillomania and postural orthostatic tachycardia syndrome appear in the literature as stimulant adverse effects, not benefits.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

