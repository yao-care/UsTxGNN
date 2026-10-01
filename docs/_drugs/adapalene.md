---
layout: default
title: Adapalene
parent: Model Prediction Only (L5)
nav_order: 213
evidence_level: L5
indication_count: 1
---

# Adapalene
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

# Adapalene: From Acne to Elevated Plasma Zinc

## One-Sentence Summary

Adapalene is a topical retinoid, generally used for acne, and is marketed in the US as a gel, cream and swab.
The TxGNN model predicts it may be effective for **elevated plasma zinc**, but there are **0 clinical trials** and **0 publications** supporting this direction.
The prediction is model-only and has no mechanistic or clinical support.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the source record (adapalene is generally used topically for acne) |
| Predicted New Indication | Zinc, elevated plasma |
| TxGNN Prediction Score | 99.51% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 (the listed licenses are ANDAs) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the source record. Adapalene is a topical retinoid that selectively activates retinoic acid receptors (RAR-beta/gamma), and its use in acne is well established.

We found no credible link between this mechanism and the predicted indication. "Elevated plasma zinc" is a laboratory finding rather than a disease, and no known pathway connects retinoid receptor signaling to lowering plasma zinc. Topical use also means low systemic exposure, which weakens any plausible effect on plasma zinc.

The very high TxGNN score (0.995) is most likely a knowledge-graph association artifact rather than a therapeutic signal. This prediction should be treated as a low-plausibility hypothesis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA204593 | Adapalene (CALL INC. dba Rochester Pharmaceuticals) | Swab | Not listed in source record |
| ANDA090824 | Adapalene (Bryant Ranch Prepack) | Cream | Not listed in source record |
| ANDA090962 | Adapalene (YYBA CORP) | Gel | Not listed in source record |
| ANDA091314 | Adapalene (Glenmark Therapeutics Inc., USA) | Gel | Not listed in source record |
| ANDA215940 | Adapalene (Rugby Laboratories, Inc.) | Gel | Not listed in source record |

The record contains 20 licenses in total; the 5 above are shown.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score (L5), with no trials, no literature and no plausible mechanism. Topical dosing and the nature of the "disease" (a lab value) make a therapeutic effect on plasma zinc unlikely.

**To proceed, the following is needed:**
- A plausible biological pathway linking retinoid receptor signaling to zinc homeostasis
- Evidence that elevated plasma zinc is a clinically meaningful treatment target
- Systemic exposure data for topical adapalene
- The FDA package insert (warnings and contraindications) and the approved indication text
- DrugBank mechanism-of-action data
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

