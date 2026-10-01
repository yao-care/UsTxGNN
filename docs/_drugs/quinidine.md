---
layout: default
title: Quinidine
parent: Model Prediction Only (L5)
nav_order: 1102
evidence_level: L5
indication_count: 1
---

# Quinidine
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

# Quinidine: From Cardiac Arrhythmia to Nephrogenic Syndrome of Inappropriate Antidiuresis

## One-Sentence Summary

Quinidine is a class Ia antiarrhythmic that has long been marketed in the United States as oral tablets and capsules. The TxGNN model predicts it may be effective for **nephrogenic syndrome of inappropriate antidiuresis (NSIAD)**. Currently there are **0 clinical trials** and **0 publications** supporting this direction, so the prediction rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Cardiac arrhythmia (class Ia antiarrhythmic; the supplied license records contain no indication text) |
| Predicted New Indication | Nephrogenic syndrome of inappropriate antidiuresis |
| TxGNN Prediction Score | 99.27% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 9 (all are generic ANDA filings) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the supplied record. Quinidine is known as a class Ia antiarrhythmic that blocks sodium and potassium channels and also inhibits CYP2D6. Its efficacy in arrhythmia is established, but nothing in the supplied data links these actions to the kidney's handling of water.

NSIAD is caused by gain-of-function variants in the vasopressin V2 receptor gene (*AVPR2*), or in some cases by GNAS-related signaling changes. These drive water retention independent of vasopressin. Quinidine does not act at the V2 receptor or downstream of it, so a mechanistic link is not apparent.

The high score (0.993) most likely reflects indirect proximity in the knowledge graph, such as shared ion-channel or cAMP/aquaporin-related neighbours, rather than a validated mechanism. Because NSIAD arises from constitutive receptor activation, an agent that does not act on this pathway is not expected to help.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

The supplied record lists 9 licenses in total. Five are shown below, and the same authorization number appears under several manufacturers.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA089338 | Quinidine Gluconate (Golden State Medical Supply) | Tablet, extended release | Not provided |
| ANDA088072 | Quinidine Sulfate (Epic Pharma, LLC) | Tablet | Not provided |
| ANDA089338 | Quinidine Gluconate (Richmond Pharmaceuticals, Inc.) | Tablet, extended release | Not provided |
| ANDA212589 | Quinidine Gluconate (Eywa Pharma Inc) | Tablet, extended release | Not provided |
| ANDA089338 | Quinidine Gluconate (Sun Pharmaceutical Industries, Inc.) | Tablet, extended release | Not provided |

All listed products are oral: extended-release tablets, tablets, capsules and gelatin-coated capsules.

---

## Safety Considerations

- **Cardiac risk**: Quinidine can prolong the QT interval, which would need to be weighed against any speculative benefit.
- **Drug interactions**: Quinidine inhibits CYP2D6, so interactions with other CYP2D6 substrates are a concern. The interaction database query returned no records.

Please refer to the package insert for full warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only support is a model score. There are no trials or publications, and no plausible link between quinidine's ion-channel activity and V2 receptor signaling in NSIAD. The safety cost (QT prolongation, CYP2D6 interactions) in a rare, often pediatric-onset disorder is not justified without evidence.

**To proceed, the following is needed:**
- Mechanism of action data for quinidine, and a documented pathway connecting it to V2 receptor or downstream cAMP/aquaporin signaling
- Preclinical evidence (for example, cell-based assays with gain-of-function *AVPR2* variants)
- Package insert warnings and contraindications for a formal safety screen
- A literature and trial search for NSIAD treatments, to confirm no relevant precedent exists
- Assessment of route compatibility and pediatric dosing feasibility

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

