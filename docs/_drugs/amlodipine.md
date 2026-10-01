---
layout: default
title: Amlodipine
parent: Model Prediction Only (L5)
nav_order: 329
evidence_level: L5
indication_count: 10
---

# Amlodipine
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

# Amlodipine: From Hypertension to Brain Stem Infarction

## One-Sentence Summary

Amlodipine is a dihydropyridine L-type calcium channel blocker, generally used to treat hypertension. The indication text in the source data is empty, so this is not confirmed from the labels provided.
The TxGNN model predicts it may be effective for **brain stem infarction**, but **0 clinical trials** and **0 publications** currently support this specific prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the source data (licence indication text is empty); generally used as an antihypertensive |
| Predicted New Indication | Brain stem infarction |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 (the listed licences are ANDAs) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, amlodipine is a dihydropyridine calcium channel blocker whose vasodilating, blood-pressure-lowering effect is well established, and mechanistically it may be applicable to ischaemic cerebrovascular disease.

Brain stem infarction is a vascular event. Blood pressure control and vascular protection are plausible links to it. However, no trials, literature or mechanistic data were retrieved for this exact indication. The high model score (99.94%) is therefore a hypothesis, not evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA206367 | Amlodipine besylate | Tablet | Exelan Pharmaceuticals, Inc. |
| ANDA078021 | Amlodipine Besylate | Tablet | Aurobindo Pharma Limited |
| ANDA078226 | Amlodipine Besylate | Tablet | Cardinal Health 107, LLC |
| ANDA077955 | Amlodipine Besylate | Tablet | Cipla USA Inc. |
| ANDA203245 | Amlodipine Besylate | Tablet | A-S Medication Solutions |

Amlodipine is also available as an oral solution. The approved indication text was not provided for these licences.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on the model score alone (Evidence Level L5). No trials or publications support amlodipine in brain stem infarction, and the safety and mechanism data are incomplete.

Two other predicted indications have more evidence and may deserve review first:
- **Intracerebral hemorrhage** (L2): the completed Phase 3 TRIDENT trial ([NCT02699645](https://clinicaltrials.gov/study/NCT02699645), n=1671) tests a triple antihypertensive combination. Amlodipine's independent effect cannot be isolated, and results were not provided.
- **Cerebral artery occlusion** (L4): rodent stroke studies report neuroprotective effects, with no human efficacy data.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (currently a blocking gap)
- Mechanism of action data from DrugBank
- A targeted search for trials and literature on amlodipine in brain stem infarction
- Human efficacy data, or a decision to prioritise the intracerebral hemorrhage direction instead
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

