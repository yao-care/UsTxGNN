---
layout: default
title: Calcifediol
parent: Model Prediction Only (L5)
nav_order: 486
evidence_level: L5
indication_count: 2
monitor_inn: "CALCIFEDIOL"
predicted_indications: ["obsolete vitamin D deficiency", "renal tubular acidosis"]
last_modified_at: 2026-10-28
description: "Calcifediol: predicted new indication obsolete vitamin D deficiency (evidence level L5). Approved use: Not recorded in the local data"
---

# Calcifediol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

## Calcifediol: Vitamin D metabolite (25-hydroxyvitamin D3) → obsolete vitamin D deficiency
{: .text-alpha }

## One-Sentence Summary

Calcifediol is the 25-hydroxylated form of vitamin D3, the main circulating vitamin D metabolite and the direct precursor of calcitriol.
The TxGNN model predicts it may be useful for **obsolete vitamin D deficiency**, but **no clinical trials and no publications** were found in the data compiled for this report, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | obsolete vitamin D deficiency |
| TxGNN Prediction Score | 0.9999 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses: 1 of 1) |
| Number of NDAs | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. Based on known pharmacology, calcifediol is the direct circulating precursor of calcitriol and the main biomarker of vitamin D status, so replenishing it in vitamin D deficiency is mechanistically plausible.

However, this is the drug's native physiological role, and the disease term is flagged as obsolete in the ontology. The very high score (0.9999) most likely reflects this close pharmacological proximity rather than new repurposing evidence. It should not be read as proof of benefit, and it is not a probability of success.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA208010 | Rayaldee | Capsule, extended release (oral) | Not recorded in the local data |

The local records list one licence, a single-ingredient product from OPKO Pharmaceuticals LLC. The drug is marketed in the United States according to the local records.

## Safety Considerations

- **Drug Interactions**: 57 interactions were found in total. Examples include:
  - Major: cholecalciferol, calcitriol, burosumab
  - Moderate: thiazide diuretics (hydrochlorothiazide, chlorothiazide, chlorthalidone, bendroflumethiazide, benzthiazide), enzyme-inducing anticonvulsants and barbiturates (carbamazepine, fosphenytoin, amobarbital, butabarbital, butalbital), bile acid binders (cholestyramine, colesevelam, colestipol), aluminum hydroxide, digitoxin, topical calcipotriol and topical calcitriol
- **Conditions of concern for vitamin D therapy**: Hypercalcemia, nephrocalcinosis, hyperphosphatemia, hypervitaminosis, sarcoidosis, kidney stones (nephrolithiasis) and kidney disease appear among the disease associations that call for caution. These come from a relationship dataset, not from label text.

Label warnings and contraindications were not available. Please refer to the package insert for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting trials or publications (evidence level L5). It mostly restates calcifediol's known role in vitamin D status, and the disease term is obsolete, so it offers little new repurposing value.

**To proceed, the following is needed:**
- A current, non-obsolete disease definition for the target condition
- Clinical or observational studies that directly examine calcifediol in vitamin D deficiency
- FDA package insert warnings and contraindications
- Mechanism of action data
- A safety plan for hypercalcemia, kidney disease and the major drug interactions
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

