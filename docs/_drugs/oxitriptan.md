---
layout: default
title: Oxitriptan
parent: Model Prediction Only (L5)
nav_order: 1003
evidence_level: L5
indication_count: 1
monitor_inn: "OXITRIPTAN"
predicted_indications: ["insomnia (disease)"]
---

# Oxitriptan
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

# Oxitriptan: From an Unspecified Original Indication to Insomnia

## One-Sentence Summary

Oxitriptan (5-hydroxytryptophan, 5-HTP) is the immediate precursor of serotonin. No approved indication is recorded for it in the US data compiled for this report.
The TxGNN model predicts it may be effective for **insomnia**, with a very high score.
Currently there are **0 clinical trials** and **0 publications** supporting this direction, so the prediction rests on model output and biochemical reasoning alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | No approved indication text available |
| Predicted New Indication | Insomnia |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L5 |
| US Market Status | Cancelled only |
| Number of NDAs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available. Based on general biochemistry, oxitriptan is the direct intermediate between tryptophan and serotonin. Serotonin is in turn a precursor of melatonin, so a plausible path to sleep regulation exists (5-HTP → serotonin → melatonin, plus serotonergic modulation of sleep-wake circuits).

The original indication is not documented in the compiled data, so the relationship between the original and new indication cannot be assessed. The link to insomnia rests on this biochemical reasoning and the high TxGNN score (0.999), not on retrieved clinical or literature evidence.

Serotonergic effects on sleep are also complex. Depending on dose, timing, and receptor subtype they can either promote or disrupt sleep, so the direction of benefit is uncertain.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Not available | 5-HTP Phenolic (Energique, Inc.) | Liquid | Not stated (status: cancelled) |

## Safety Considerations

- **Drug Interactions**: 17 interactions were identified, 10 of them Major.
  - **Major**:
    - Serotonergic and weight-loss agents: lorcaserin, fenfluramine, sibutramine.
    - 5-HT3 antagonists (antiemetics): dolasetron, palonosetron, ondansetron, granisetron.
    - Other agents: methylene blue, doxepin (oral and topical), procarbazine.
  - **Moderate**: morphine, codeine, hydrocodone, cyproheptadine, ozanimod, ifosfamide.

Many of the Major interactions involve serotonergic agents, so serotonin-related toxicity is a likely concern when combining. For other safety information, please refer to the package insert.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is very high, but there are no clinical trials or publications behind it (Evidence Level L5). The mechanism of action data is missing, and the only US authorization is cancelled. Label warnings and contraindications are also unavailable, which blocks safety screening.

**To proceed, the following is needed:**
- Package insert warnings and contraindications
- Curated mechanism of action data
- A literature and trial search for 5-HTP in insomnia and sleep disorders
- Clarification of the original approved indication
- Assessment of route and dosage form compatibility
- A serotonergic interaction risk plan for the many Major interactions
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

