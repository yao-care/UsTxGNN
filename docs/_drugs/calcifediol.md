---
layout: default
title: Calcifediol
parent: Model Prediction Only (L5)
nav_order: 486
evidence_level: L5
indication_count: 1
monitor_inn: "CALCIFEDIOL"
predicted_indications: ["renal tubular acidosis"]
last_modified_at: 2026-11-06
description: "Calcifediol: predicted new indication Renal tubular acidosis (evidence level L5). In the US: 2 FDA applications (1 active)"
---

# Calcifediol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

## Calcifediol: Renal tubular acidosis
{: .text-alpha }

## One-Sentence Summary

Calcifediol is the 25-hydroxylated form of vitamin D3, the main circulating vitamin D metabolite and the direct precursor of calcitriol.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Renal tubular acidosis |
| TxGNN Prediction Score | 0.9986 |
| Evidence Level | L5 |
| US Market Status | Marketed (active FDA-approved applications: 1 of 2) |
| Number of FDA Applications | 2 (active: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the FDA-approved prescribing information for calcifediol: "Calcifediol (25-hydroxyvitamin D 3 ) is a prohormone of the active form of vitamin D 3, calcitriol (1,25‑dihydroxyvitamin D 3 ). Calcifediol is converted to calcitriol by cytochrome P450 27B1 (CYP27B1), also called 1-alpha hydroxylase, primarily in the kidney." ([DailyMed: Rayaldee (calcifediol) prescribing information, OPKO Pharmaceuticals LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=6a95effd-32a5-46b6-a30e-7f4f9bf8cc77), label version 2024-01-19; accessed 2026-11-19.) Based on known pharmacology, calcifediol is the direct circulating precursor of calcitriol and the main biomarker of vitamin D status, so replenishing it in vitamin D deficiency is mechanistically plausible.

However, this is the drug's native physiological role, and the disease term is flagged as obsolete in the ontology. It should not be read as proof of benefit, and it is not a probability of success.

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

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism-of-action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Rayaldee (calcifediol) prescribing information, OPKO Pharmaceuticals LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=6a95effd-32a5-46b6-a30e-7f4f9bf8cc77) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

