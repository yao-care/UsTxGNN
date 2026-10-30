---
layout: default
title: Levomilnacipran
parent: Model Prediction Only (L5)
nav_order: 856
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-30
monitor_inn: "LEVOMILNACIPRAN"
predicted_indications: ["benign paroxysmal torticollis of infancy", "agoraphobia", "neurotic disorder"]
description: "Levomilnacipran: predicted new indication Benign paroxysmal torticollis of infancy (evidence level L5). Approved use: Not recorded in the local data"
---

# Levomilnacipran
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

## Levomilnacipran: Benign paroxysmal torticollis of infancy
{: .text-alpha }

## One-Sentence Summary

Levomilnacipran is a serotonin-norepinephrine reuptake inhibitor (SNRI), originally used to treat major depressive disorder and related depressive and anxiety conditions.
The TxGNN model predicts it may be effective for **benign paroxysmal torticollis of infancy**, but currently there are **0 clinical trials** and **0 publications** supporting this specific prediction. It rests on model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Benign paroxysmal torticollis of infancy |
| TxGNN Prediction Score | 0.9953 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses: 1 of 1) |
| Number of FDA Applications | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. Based on known information, levomilnacipran is an SNRI. Its efficacy in major depressive disorder has been established, and it is the more active enantiomer of milnacipran.

Benign paroxysmal torticollis of infancy is an episodic pediatric disorder related to the migraine spectrum and possibly to channelopathies (e.g., CACNA1A). A link to serotonin and norepinephrine reuptake inhibition is speculative. The very high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

There is also a population mismatch. The condition occurs in infants, while levomilnacipran has no pediatric approval for this use, which is a major safety barrier.

**Other predictions in the same run (for context):**

| Rank | Predicted Indication | Score | Evidence Level | Comment |
|---|---|---|---|---|
| 2 | Agoraphobia | 0.9953 | L5 | Plausible class-level link (SNRIs/SSRIs in anxiety and panic disorders), but no levomilnacipran-specific data |
| 6 | Neurotic disorder | 0.9919 | L5 | Outdated, nonspecific category; prediction only |

Of these, agoraphobia and dysthymic disorder have a more credible mechanistic rationale than the top-ranked prediction. Melancholia and neurotic depression largely overlap with the existing indication rather than representing true repurposing.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for benign paroxysmal torticollis of infancy.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA204168 | Fetzima | Capsule, extended release (oral) | Status: valid (Allergan, Inc.) |

## Safety Considerations

- **Contraindications (knowledge-graph edges, not label text)**: angle-closure glaucoma (also listed as closed-angle glaucoma).
- **Drug Interactions**: 100 interactions were found. Major-level examples include:
  - Bupropion
  - Clarithromycin
  - Lorcaserin
  - Phentermine
  - Diethylpropion
  - Fenfluramine
  - Dexfenfluramine
  - Dolasetron
  - Palonosetron

  Moderate-level examples include epinephrine, ephedrine, morphine, acetylsalicylic acid and isometheptene. Many of the major interactions involve other serotonergic or sympathomimetic agents, so serotonin-related and cardiovascular risks deserve attention.

Please refer to the package insert for warnings and contraindications, which were not available in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a very high model score, but there are no clinical trials or literature, and the mechanistic link is speculative. The target population (infants) adds a major safety barrier, and the only US license on record is cancelled.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism-of-action data (e.g., from DrugBank)
- Any clinical or preclinical evidence linking SNRIs to benign paroxysmal torticollis of infancy
- Consideration of a better-supported alternative, such as agoraphobia or dysthymic disorder, for class-extrapolation research
- Pediatric safety assessment if infant use is ever considered
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

