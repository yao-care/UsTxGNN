---
layout: default
title: Tirzepatide
parent: Model Prediction Only (L5)
nav_order: 1233
evidence_level: L5
indication_count: 10
---

# Tirzepatide
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

# Tirzepatide: From Type 2 Diabetes and Obesity to Gout

## One-Sentence Summary

Tirzepatide is a dual GIP/GLP-1 receptor agonist, marketed in the US as Mounjaro and Zepbound and used for type 2 diabetes and obesity.
The TxGNN model predicts it may be effective for **gout** (score 96.75%), but **0 clinical trials** and **0 publications** were retrieved for this indication, so the prediction is unsupported by data.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the source data (approved indication text is empty). The retrieved literature describes tirzepatide as used for type 2 diabetes and obesity. |
| Predicted New Indication | Gout |
| TxGNN Prediction Score | 96.75% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 license records (the 5 listed entries carry 2 distinct NDA numbers) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the source data. Tirzepatide is known to be a dual GIP/GLP-1 receptor agonist, and its effectiveness in obesity and type 2 diabetes is well established.

The only plausible route to gout is indirect. Substantial weight loss may lower serum urate in people with obesity, and obesity is a recognised risk factor for gout. No trial, publication, or other data was retrieved to support this. The high score may simply reflect proximity in the knowledge graph. Treat this as a hypothesis, not evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| NDA215866 | Mounjaro | Injection, solution | Eli Lilly and Company |
| NDA217806 | Zepbound | Injection, solution | Eli Lilly and Company |

The approved indication text is empty in the source data. Both products are injectable solutions.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The model score is high, but there are no trials or publications for gout. The only mechanism proposed (weight loss lowering urate) is speculative and unsupported by the data provided. The evidence level is L5, which is model prediction only.

**To proceed, the following is needed:**
- Gout-specific evidence, such as observational data on serum urate or gout flares in tirzepatide-treated patients, or a registered trial
- Mechanism-of-action data from DrugBank
- Package insert warnings and contraindications from the FDA label

**Note on other predictions:** In this pack, **osteoarthritis** (rank 2, score 95.92%) is the best-supported candidate, at L4 with a "Research Question" recommendation. [NCT06191848](https://clinicaltrials.gov/study/NCT06191848) is a Phase 4 randomized, placebo-controlled trial in obesity with knee osteoarthritis (n=352). It is still recruiting and has no results yet. If the team wants a lead indication to prioritise, osteoarthritis is stronger than gout. The evidence is for obesity-associated knee OA, not OA in general.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

