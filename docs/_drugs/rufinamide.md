---
layout: default
title: Rufinamide
parent: Model Prediction Only (L5)
nav_order: 1138
evidence_level: L5
indication_count: 5
---

# Rufinamide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

# Rufinamide: From Antiseizure Therapy to Febrile Infection-Related Epilepsy Syndrome

## One-Sentence Summary

Rufinamide is a marketed antiseizure medication. The provided data does not list its approved indication text.
The TxGNN model predicts it may be effective for **febrile infection-related epilepsy syndrome (FIRES)**, but **0 clinical trials** and **0 publications** currently support this prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the provided data (generally known as an antiseizure drug) |
| Predicted New Indication | Febrile infection-related epilepsy syndrome |
| TxGNN Prediction Score | 99.57% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 (the listed licenses are generic ANDAs) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, rufinamide is an antiseizure sodium-channel modulator. Its use in seizure disorders is established, and mechanistically it may be applicable to FIRES. This link cannot be verified from the provided data.

FIRES is a severe, refractory epilepsy syndrome. The high score likely reflects the drug's similarity to other antiseizure drugs in the knowledge graph, not disease-specific evidence.

The model also ranked four other epilepsy-related conditions highly. All have no trials or publications, and three share the identical score of 99.44%, which suggests a shared graph-neighborhood signal.

| Rank | Predicted Indication | TxGNN Score | Evidence Level |
|------|------|------|------|
| 2 | Perioral myoclonia with absences | 99.51% | L5 |
| 3 | Photosensitive occipital lobe epilepsy | 99.44% | L5 |
| 4 | Cryptogenic late-onset epileptic spasms | 99.44% | L5 |
| 5 | Atypical childhood epilepsy with centrotemporal spikes | 99.44% | L5 |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA216841 | Rufinamide | Suspension | NorthStar Rx LLC |
| ANDA217230 | Rufinamide | Tablet, film coated | Aurobindo Pharma Limited |
| ANDA204988 | Rufinamide | Tablet, film coated | Hikma Pharmaceuticals USA Inc. |
| ANDA211388 | Rufinamide | Suspension | Bionpharma Inc. |

Approved indication text is not included in the provided data. Available forms are oral tablets and suspension.

## Safety Considerations

Please refer to the package insert for safety information. No drug-interaction records were found in the queried source.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model score alone, with no clinical trials, no literature, and no verified mechanism. FIRES is a severe, refractory condition, so an unsupported prediction should not be acted on.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data (for example from DrugBank) to assess the mechanistic link to FIRES
- Approved indication text, to define the original indication
- A search for case reports, case series, or registered trials of rufinamide in FIRES
- A route and formulation compatibility assessment for FIRES treatment settings

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

