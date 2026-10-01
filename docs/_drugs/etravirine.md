---
layout: default
title: Etravirine
parent: Model Prediction Only (L5)
nav_order: 686
evidence_level: L5
indication_count: 10
---

# Etravirine
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

# Etravirine: From HIV-1 Infection to Feline Acquired Immunodeficiency Syndrome

## One-Sentence Summary

Etravirine is an oral non-nucleoside reverse transcriptase inhibitor (NNRTI) used to treat HIV-1 infection.
The TxGNN model predicts it may be effective for **feline acquired immunodeficiency syndrome (FIV)**, a veterinary disease.
This prediction has **0 clinical trials** and **0 publications** behind it, so it rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV-1 infection (the US label text is not included in the Evidence Pack) |
| Predicted New Indication | Feline acquired immunodeficiency syndrome |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 16 licenses (NDA and ANDA generics combined) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available. Etravirine is an HIV-1 NNRTI, and its efficacy against human HIV-1 is established. The model links it to feline AIDS because both diseases sit close together in the knowledge graph, under the "immunodeficiency virus" node.

The mechanistic basis is weak. Feline immunodeficiency virus (FIV) reverse transcriptase is generally not susceptible to NNRTIs, so a direct antiviral effect is unlikely. The high score (99.98%) most likely reflects the shared graph neighborhood rather than real pharmacology.

The indication is also veterinary, so it falls outside the human drug-development pathway.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA022187 | Intelence (Janssen Products LP) | Tablet | — |
| ANDA219152 | Etravirine (Bionpharma Inc.) | Tablet | — |
| ANDA215402 | Etravirine (Carnegie Pharmaceuticals LLC) | Tablet | — |
| ANDA215402 | Etravirine (Leading Pharma, LLC) | Tablet | — |

Only oral tablets are listed. The source data does not include approved indication text.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This prediction is model output only, with no trials or literature. Its mechanistic basis is weak because FIV reverse transcriptase is generally not NNRTI-susceptible, and the indication is veterinary.

Two other predictions for this drug have somewhat more support (both L3). They are congenital HIV (rank 4) and AIDS-related complex (rank 5). Both largely overlap with etravirine's existing HIV indication, so they are not true repurposing. The Friedreich ataxia Phase 2 trial (NCT04273165) is a separate repurposing signal and does not support any of the predictions here.

**To proceed, the following is needed:**
- Any in vitro evidence of etravirine activity against FIV reverse transcriptase, before further investment
- The US package insert (indications, warnings, contraindications, drug interactions)
- Mechanism of action data from DrugBank (DB06414)
- Confirmation that the prediction has a human-medicine development path, given the veterinary indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

