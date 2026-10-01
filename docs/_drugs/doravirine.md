---
layout: default
title: Doravirine
parent: Model Prediction Only (L5)
nav_order: 622
evidence_level: L5
indication_count: 3
---

# Doravirine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

# Doravirine: From HIV-1 Infection to Feline Acquired Immunodeficiency Syndrome

## One-Sentence Summary

Doravirine is an oral non-nucleoside reverse transcriptase inhibitor (NNRTI) marketed in the US as PIFELTRO for HIV-1 infection.
The TxGNN model predicts it may be effective for **feline acquired immunodeficiency syndrome (FIV)**,
but there are currently **0 clinical trials** and **0 publications** supporting this prediction, and the mechanistic link is weak.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV-1 infection (the US license records contain no indication text; this is taken from the drug class and the pack's rationale notes) |
| Predicted New Indication | Feline acquired immunodeficiency syndrome |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L5 (model prediction only) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 2 license records (both under NDA210806) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, doravirine is an NNRTI, a class that blocks HIV-1 reverse transcriptase. Its efficacy in HIV-1 is the basis for the prediction. Mechanistically, it could apply to feline immunodeficiency virus (FIV) only if FIV reverse transcriptase were also inhibited by this class.

The relationship between the two diseases is that both are lentiviral immunodeficiency infections. The very high TxGNN score reflects proximity to other retroviral diseases in the knowledge graph, not verified activity.

The class-level rationale is weak. FIV reverse transcriptase is generally reported to be insensitive to NNRTIs, and the binding pocket differs from that of HIV-1. The prediction therefore needs direct enzymatic or in vitro validation before it can be taken seriously.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA210806 | PIFELTRO (Merck Sharp & Dohme LLC) | Tablet, film coated (oral) | — |
| NDA210806 | PIFELTRO (A-S Medication Solutions) | Tablet, film coated (oral) | — |

## Safety Considerations

No warnings or contraindications are available in the provided data, and the drug interaction query returned no results.
Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model score alone, with no trials or publications for feline immunodeficiency syndrome. FIV reverse transcriptase is generally reported to be insensitive to NNRTIs, which undermines the mechanistic case. The other two predictions for this drug (simian immunodeficiency virus infection and a rare neurodevelopmental disorder) are also at Hold. SIV is likewise expected to be intrinsically resistant to NNRTIs. The neurodevelopmental disorder has no credible mechanistic link and is likely a knowledge-graph artifact.

**To proceed, the following is needed:**
- Enzymatic and in vitro testing of doravirine against FIV reverse transcriptase
- Any doravirine-specific animal-model or veterinary data
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism of action data from DrugBank
- Approved indication text for the US licenses
- Route compatibility assessment for the target species
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

