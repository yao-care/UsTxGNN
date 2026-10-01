---
layout: default
title: Arsenic Trioxide
parent: Model Prediction Only (L5)
nav_order: 417
evidence_level: L5
indication_count: 10
---

# Arsenic Trioxide
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

# Arsenic Trioxide: From Acute Promyelocytic Leukemia to Unclassified Myelodysplastic Syndrome

## One-Sentence Summary

Arsenic trioxide is an anticancer drug that the literature describes as approved for acute promyelocytic leukemia (APL).
The TxGNN model predicts it may be effective for **unclassified myelodysplastic syndrome**, with a very high score (99.93%).
However, **0 clinical trials** and **0 publications** were retrieved for this exact subtype, so this is a model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acute promyelocytic leukemia (from the literature in the pack; the US license records provided carry no indication text) |
| Predicted New Indication | Unclassified myelodysplastic syndrome |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, arsenic trioxide is a marketed injectable anticancer agent. Its efficacy in APL has been established, and mechanistically it may be applicable to myelodysplastic syndrome (MDS).

The parent disease, myelodysplastic syndrome, does show activity signals for arsenic trioxide. These signals cannot be attributed to the "unclassified" subtype. No trial or publication was retrieved that specifically enrolled this subtype, so the prediction currently rests on the model's graph proximity to MDS and related myeloid disorders.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA217413 | Arsenic Trioxide (Orbicular Pharmaceutical Technologies) | Injection, solution | Not listed |
| ANDA206228 | Arsenic trioxide (Zydus Lifesciences) | Injection, solution | Not listed |
| ANDA215059 | Arsenic Trioxide (Gland Pharma) | Injection | Not listed |
| ANDA209780 | Arsenic Trioxide (Nexus Pharmaceuticals) | Injection | Not listed |
| No number listed | Arsenicum Album 30X (Laboratoire Schmidt-Nagel) | Globule | Not listed |

Of the 20 authorizations, only the 5 main ones are shown.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Antineoplastic; apoptosis- and differentiation-inducing agent |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | CBC with differential, liver and renal function, electrolytes, ECG (QTc) |
| Handling Protection | Follow cytotoxic drug handling regulations |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is very high, but no trials or publications support this specific subtype (L5, screening stage S0). Any activity signal comes from the parent MDS entity, so it cannot yet support a decision on this subtype.

**To proceed, the following is needed:**
- Subtype-specific clinical or literature evidence for unclassified MDS.
- The FDA package insert warnings and contraindications, which are currently a blocking gap.
- Detailed mechanism of action data (MOA).

**Note on other candidates in the same pack:** "myelodysplastic syndrome" (rank 6) has much stronger support. It reaches L2 with multiple Phase 1/2 trials, including a completed Phase 1/2 study of 87 patients and two recruiting oral-arsenic studies. It is a better starting point for a Research Question than the unclassified subtype. No Phase 3 MDS-specific trial was found, and many of the trials were terminated with very small enrollment.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

