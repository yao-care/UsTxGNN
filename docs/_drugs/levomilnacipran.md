---
layout: default
title: Levomilnacipran
parent: Model Prediction Only (L5)
nav_order: 856
evidence_level: L5
indication_count: 6
---

# Levomilnacipran
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

# Levomilnacipran: From Major Depressive Disorder to Benign Paroxysmal Torticollis of Infancy

## One-Sentence Summary

Levomilnacipran is a serotonin-norepinephrine reuptake inhibitor (SNRI) marketed in the US as Fetzima for adult major depressive disorder.
The TxGNN model predicts it may be effective for **benign paroxysmal torticollis of infancy**, but this rests on the model score alone: **0 clinical trials** and **0 publications** were found for this indication.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Major depressive disorder in adults (from published literature; the license records contain no indication text) |
| Predicted New Indication | Benign paroxysmal torticollis of infancy |
| TxGNN Prediction Score | 99.53% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 4 license records, all under a single NDA (NDA204168) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the Evidence Pack. The literature describes levomilnacipran as an SNRI, the more active enantiomer of milnacipran. Its efficacy in adult major depressive disorder is established.

The predicted condition is a self-limiting movement disorder of infancy, related to the migraine spectrum. We found no plausible link between serotonin-norepinephrine reuptake inhibition and this condition in the data provided. No infant safety data exist for levomilnacipran. The high graph score (0.995) is best read as a likely artifact of the knowledge graph, not a mechanistic signal.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA204168 (4 records) | Fetzima (Allergan, Inc.) | Capsule, extended release (oral) | Not stated in the license records |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has only a model score behind it: no trials, no literature, no plausible mechanism, and no infant safety data. It should not advance to safety screening in its current form.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications, which are currently missing and block safety screening
- Mechanism-of-action data from DrugBank
- A drug-specific mechanistic rationale for this indication, plus any case reports or trials
- Pediatric and infant safety data, since the target population is infants
- Consider prioritising other predictions for this drug. Melancholia and neurotic depression (both L4, Research Question) have indirect depression-level literature. Agoraphobia and dysthymic disorder have class-level plausibility but no drug-specific evidence.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

