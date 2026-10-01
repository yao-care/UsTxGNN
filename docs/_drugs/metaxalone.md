---
layout: default
title: Metaxalone
parent: Model Prediction Only (L5)
nav_order: 904
evidence_level: L5
indication_count: 3
---

# Metaxalone
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

# Metaxalone: From Skeletal Muscle Relaxant Use to Infectious Otitis Media

## One-Sentence Summary

Metaxalone is an oral, centrally acting skeletal muscle relaxant. The TxGNN model predicts it may be effective for **infectious otitis media**, but there are currently **0 clinical trials** and **0 publications** supporting this direction. This is a model-only prediction with no mechanistic or clinical support.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not captured in the record. The license entries carry no indication text, so the entry above rests on the drug's known class (skeletal muscle relaxant). |
| Predicted New Indication | Infectious otitis media |
| TxGNN Prediction Score | 99.06% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 (the listed entries are ANDA generic authorizations) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Metaxalone is a centrally acting skeletal muscle relaxant, but its specific molecular target is unclear in the source record.

The link between the original use and the predicted indication is weak. Infectious otitis media is a bacterial or viral middle-ear infection. Metaxalone has no known antimicrobial, anti-inflammatory, or Eustachian-tube-related activity that would plausibly treat it. The high TxGNN score (0.9906, rank 20,353) is a computational output only. The two other top predictions, endocarditis (99.02%) and endocardial fibroelastosis (99.00%), also have no mechanistic link and no clinical or literature evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA203399 | Metaxalone | Tablet | Advanced Rx of Tennessee, LLC |
| ANDA207466 | Metaxalone | Tablet | ScieGen Pharmaceuticals, Inc. |
| ANDA207466 | Metaxalone | Tablet | ScieGen Pharmaceuticals, Inc. |
| ANDA204770 | Metaxalone | Tablet | Doc Rx |
| ANDA207466 | Metaxalone | Tablet | BluePoint Laboratories |

The only route of administration in the record is oral (tablet).

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on the TxGNN model score. There is no mechanistic link, no registered trial, and no publication, so it sits at evidence level L5 (stage S0). Safety data, including warnings and contraindications, are also missing.

**To proceed, the following is needed:**
- Package insert warnings and contraindications, downloaded and parsed from the FDA website. This blocks the S1 safety screening.
- Mechanism of action data for metaxalone, for example from DrugBank.
- Approved indication text for the listed licenses.
- A plausible biological rationale linking metaxalone to middle-ear infection. Preclinical or mechanistic evidence would be needed before considering clinical investigation.
- Route compatibility and similarity-to-original assessments, both currently pending.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

