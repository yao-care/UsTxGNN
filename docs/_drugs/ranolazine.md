---
layout: default
title: Ranolazine
parent: Model Prediction Only (L5)
nav_order: 1111
evidence_level: L5
indication_count: 1
---

# Ranolazine
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

# Ranolazine: From Chronic Angina to Nephrogenic Syndrome of Inappropriate Antidiuresis

## One-Sentence Summary

Ranolazine is an extended-release oral drug marketed in the US. It is generally known as a late sodium current inhibitor for chronic angina, though the supplied dataset lists no original indication.
The TxGNN model predicts it may be effective for **nephrogenic syndrome of inappropriate antidiuresis (NSIAD)**, but there are currently **0 clinical trials** and **0 publications** supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the supplied label data (chronic angina per general pharmacology) |
| Predicted New Indication | Nephrogenic syndrome of inappropriate antidiuresis |
| TxGNN Prediction Score | 99.65% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 (the listed licenses are generic ANDAs) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Ranolazine is generally known as a late sodium current inhibitor used for chronic angina. That comes from general pharmacology, not from the supplied dataset.

NSIAD is an ultra-rare genetic disorder. It is caused by gain-of-function variants in *AVPR2* (the vasopressin V2 receptor), which lead to water retention and hyponatremia. No established pathway links ranolazine to V2 receptor signaling, aquaporin-2 regulation, or renal water handling. No mechanistic link can be established from the supplied data.

The TxGNN score is very high, but it is a knowledge-graph prediction only and not clinical evidence. The graph path behind the score was not provided. A score this high for an ultra-rare disease with no supporting data suggests a possible graph-topology artifact, and the prediction should be reviewed before further investment.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA201046 | Ranolazine (Lupin Pharmaceuticals) | Tablet, film coated, extended release | — |
| ANDA210054 | Ranolazine (Ajanta Pharma USA) | Tablet, extended release | — |
| ANDA210188 | Ranolazine (NCS HealthCare of KY / Vangard Labs) | Tablet, extended release | — |
| ANDA211829 | Ranolazine (ScieGen Pharmaceuticals) | Tablet, film coated, extended release | — |

Only 4 of the 20 licenses were supplied, and none included approved indication text. The only route listed is oral.

## Safety Considerations

Please refer to the package insert for safety information. Drug interaction queries returned no results.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone. There are no clinical trials or publications, and no plausible mechanistic link between ranolazine and V2 receptor-mediated water retention. The high score for an ultra-rare disease may be a graph artifact. Safety data are also missing, which blocks safety screening.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- The TxGNN graph path and neighbors behind the NSIAD prediction, to check for a topology artifact
- Any preclinical or mechanistic evidence connecting ranolazine to AVPR2, aquaporin-2, or renal water handling
- The approved indication text for the US licenses, to document the original indication
- Route compatibility assessment (the predicted-indication route requirements are pending)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

