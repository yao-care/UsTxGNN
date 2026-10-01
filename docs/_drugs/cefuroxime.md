---
layout: default
title: Cefuroxime
parent: Model Prediction Only (L5)
nav_order: 509
evidence_level: L5
indication_count: 10
---

# Cefuroxime
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

# Cefuroxime: From Bacterial Infections to Polyclonal Hyperviscosity Syndrome

## One-Sentence Summary

Cefuroxime is a second-generation cephalosporin antibiotic that acts against bacteria.
The TxGNN model predicts it may be effective for **polyclonal hyperviscosity syndrome**, but there are **0 clinical trials** and **0 publications** supporting this direction, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the source data (bacterial infections, based on the drug class) |
| Predicted New Indication | Polyclonal hyperviscosity syndrome |
| TxGNN Prediction Score | 99.76% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 (the listed licenses are ANDA generics) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Cefuroxime is a beta-lactam cephalosporin, and this class inhibits bacterial cell wall synthesis. Its efficacy in bacterial infections is well established.

This prediction is hard to support mechanistically. Polyclonal hyperviscosity syndrome is caused by excess polyclonal immunoglobulin thickening the blood, which is not a bacterial target. The score of 99.76% is a graph-based output with no trials or literature behind it. The same score appears for hyperamylasemia (rank 2), which suggests score saturation rather than a specific signal for this disease.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA065048 | Cefuroxime (Hikma Pharmaceuticals USA Inc.) | Injection, powder, for solution | Not provided in source data |
| ANDA065308 | Cefuroxime Axetil (NorthStar Rx LLC) | Tablet | Not provided in source data |
| ANDA065308 | Cefuroxime Axetil (REMEDYREPACK INC.) | Tablet, film coated | Not provided in source data |
| ANDA065308 | Cefuroxime Axetil (Preferred Pharmaceuticals Inc.) | Tablet, film coated | Not provided in source data |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This indication has no clinical trials, no literature and no plausible mechanism, so a high model score alone cannot justify further investment.

**To proceed, the following is needed:**
- A credible mechanistic hypothesis linking cefuroxime to hyperviscosity, plus preclinical or clinical evidence
- The approved indication list and safety sections from the FDA package insert (the original indication is currently blank)
- Cefuroxime's mechanism of action data from DrugBank

**Note on other candidates:** The same pack contains a much stronger candidate, **urinary tract infection** (rank 6, L3, Proceed with Guardrails). It has a large real-world cefuroxime axetil study (NCT03020940, n=100,000) and cohort and comparative studies, but no confirmed Phase 3 RCT. It is likely an existing approved use rather than true repurposing, so it should be evaluated in its own report.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

