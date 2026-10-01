---
layout: default
title: Atazanavir
parent: Model Prediction Only (L5)
nav_order: 421
evidence_level: L5
indication_count: 6
---

# Atazanavir
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

# Atazanavir: From HIV-1 Infection to Feline Acquired Immunodeficiency Syndrome

## One-Sentence Summary

Atazanavir is an HIV-1 protease inhibitor used in antiretroviral therapy.
The TxGNN model predicts it may be effective for **feline acquired immunodeficiency syndrome (FIV)**, a veterinary condition,
but currently there are **0 clinical trials** and **0 publications** supporting this specific prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV-1 infection (inferred from the drug class; the license records contain no indication text) |
| Predicted New Indication | Feline acquired immunodeficiency syndrome |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 17 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, atazanavir is an HIV-1 protease inhibitor. It blocks the maturation of infectious virions, and its efficacy in HIV-1 treatment is well established.

FIV is a lentivirus related to HIV, so protease inhibition is mechanistically plausible. However, FIV protease differs structurally from HIV-1 protease, so cross-species activity is unverified. The prediction is model-only, with no trial or literature support in the dataset.

FIV is an animal disease with no human clinical relevance. The high score is best read as a knowledge-graph relationship (a related virus and a shared drug target class), not as a signal for human repurposing.

Two other predictions in the same list carry real evidence: "AIDS related complex" (rank 5) and "congenital human immunodeficiency virus" (rank 6). Both are HIV-1 conditions, so they are essentially on-label use or close extensions rather than true repurposing.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

The record lists 17 authorizations in total. The main distinct authorizations are below. Approved indication text is blank in the source records.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| NDA021567 | REYATAZ | Capsule, gelatin coated | E.R. Squibb & Sons, L.L.C. |
| ANDA212278 | Atazanavir | Capsule | Camber Pharmaceuticals, Inc. |
| ANDA204806 | Atazanavir Sulfate | Capsule | Aurobindo Pharma Limited |

Available dosage forms across products include oral capsules, tablets and a powder.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on model output (L5). It has no trials or literature, and the target condition is a veterinary disease with no human clinical relevance. The mechanistic link is plausible but unverified.

**To proceed, the following is needed:**
- Mechanism of action data (MOA) from DrugBank
- FDA package insert warnings and contraindications, which are currently missing
- Any in vitro or animal evidence of atazanavir activity against FIV protease. Without it, no veterinary development case exists.
- For human-relevant work, shift focus to ranks 5 and 6. Completed Phase 3 trials support these, but they should be treated as on-label HIV-1 use. For congenital HIV, the perinatal population and neonatal hyperbilirubinemia risk need to be checked against the full trial records.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

