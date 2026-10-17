---
layout: default
title: Amphetamine
parent: Model Prediction Only (L5)
nav_order: 334
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Amphetamine: predicted new indication Faciodigitogenital syndrome (evidence level L5). Approved use: Attention deficit hyperactivity disorder, narcolepsy and obesity"
monitor_inn: "AMPHETAMINE"
predicted_indications: ["faciodigitogenital syndrome", "chondromyxoid fibroma", "trichotillomania", "postural orthostatic tachycardia syndrome"]
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

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

# Amphetamine: From Attention Deficit Hyperactivity Disorder to Faciodigitogenital Syndrome

## One-Sentence Summary

Amphetamine is a central nervous system stimulant, originally used to treat attention deficit hyperactivity disorder (ADHD), narcolepsy and obesity.
The TxGNN model predicts it may be effective for **Faciodigitogenital Syndrome**, but there are currently **0 clinical trials** and **0 publications** supporting this prediction.
The prediction is a computational signal only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Attention deficit hyperactivity disorder, narcolepsy and obesity (from the knowledge graph; no approved indication text is available in the US license records) |
| Predicted New Indication | Faciodigitogenital syndrome |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (all licenses cancelled) |
| Number of NDAs | 10 (2 NDAs and 8 ANDAs) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, amphetamine is a stimulant that promotes the release of dopamine and noradrenaline and blocks their reuptake. Its efficacy in ADHD and narcolepsy is established.

Faciodigitogenital syndrome (Aarskog-Scott syndrome) is a rare X-linked developmental disorder caused by variants in the *FGD1* gene. Amphetamine's monoamine mechanism has no established connection to this underlying pathology. At most, it might have a speculative symptomatic effect on associated attention or behavioural features, and the data compiled for this report do not support even that.

The very high TxGNN score therefore reflects a pattern in the knowledge graph rather than a demonstrated biological link. It should be treated as a hypothesis to be tested, not as evidence of efficacy.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for faciodigitogenital syndrome.

## US Market Information

All 10 licenses are listed as cancelled, and no approved indication text is recorded for them.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA211861 | Amphetamine Sulfate (Solco Healthcare) | Tablet | Not recorded |
| NDA204326 | Amphetamine Extended-Release (Neos Therapeutics) | Orally disintegrating tablet | Not recorded |
| ANDA200166 | Amphetamine Sulfate (Bryant Ranch Prepack) | Tablet | Not recorded |
| ANDA212901 | Amphetamine Sulfate (Bryant Ranch Prepack) | Tablet | Not recorded |
| NDA210526 | Dyanavel XR (NextWave Pharmaceuticals) | Extended-release tablet | Not recorded |

## Safety Considerations

- **Contraindications (knowledge graph associations, not label text)**: The knowledge graph links amphetamine to contraindications in the following groups:
  - Cardiovascular: hypertension.
  - Neurological and psychiatric: epilepsy, anxiety disorders, bipolar disorder, psychotic disorders (including schizophrenia-spectrum disorders).
  - Respiratory: chronic obstructive pulmonary disease.
  - Hepatic and renal: liver disease or failure, hepatic encephalopathy and coma, kidney disease.
  - Metabolic and blood-related: diabetes mellitus with diabetic ketoacidosis, porphyria, thrombocytopenia, neutropenia and agranulocytosis.
  - Other: gallbladder disease, open-angle glaucoma.
- **Drug Interactions**: 90 interactions are recorded. Examples:
  - **Major**: bupropion, fenfluramine.
  - **Moderate**: epinephrine, ephedrine, lorcaserin, isometheptene, eliglustat, and several proton pump inhibitors and antacids (such as omeprazole, esomeprazole, aluminum hydroxide and calcium carbonate).
- **Other concerns**: Case reports describe stimulant-induced trichotillomania with amphetamine products. In postural orthostatic tachycardia syndrome, amphetamine could worsen tachycardia and palpitations.

Please refer to the package insert for the full warnings, because label warnings and contraindications were not available in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score, with no clinical trials or literature for this condition. No plausible mechanistic link to the *FGD1*-related pathology has been identified, and all US licenses are cancelled. The safety profile, with many knowledge-graph contraindications and major drug interactions, is demanding.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the FDA label, which block safety screening.
- Mechanism of action data (for example, from DrugBank).
- Evidence of a mechanistic link between amphetamine and the biology of faciodigitogenital syndrome, or clinical data in this population.
- A check of whether the cancelled license status reflects actual market withdrawal.

## Other Predicted Indications (for Reference)

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Decision | Note |
|------|------|------|------|------|------|
| 2 | Chondromyxoid fibroma | 99.91% | L5 | Hold | No plausible mechanism; likely a false-positive prediction |
| 3 | Specific developmental disorder | 99.91% | L4 | Hold | Only preclinical, review and hypothesis papers; no trials in this population |
| 4 | Trichotillomania | 99.47% | L4 | Hold | Case reports show amphetamine may cause the condition, a safety signal rather than an opportunity |
| 5 | Postural orthostatic tachycardia syndrome | 99.27% | L5 | Hold | No evidence; risk of worsening tachycardia |
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

