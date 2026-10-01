---
layout: default
title: Fluorometholone
parent: Model Prediction Only (L5)
nav_order: 722
evidence_level: L5
indication_count: 10
---

# Fluorometholone
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

# Fluorometholone: From Topical Ophthalmic Corticosteroid to Postinfectious Vasculitis

## One-Sentence Summary

Fluorometholone is a topical corticosteroid eye drop, marketed in the US as Flarex, FML and FML Forte.
The TxGNN model predicts it may be effective for **postinfectious vasculitis**, but **no clinical trials and no publications** currently support this specific prediction.

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Postinfectious vasculitis |
| TxGNN Prediction Score | 99.91% (model rank 3011) |
| Evidence Level | L5 (model prediction only) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 7 licenses (3 distinct NDA numbers) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available. Fluorometholone is a topical ophthalmic corticosteroid. Corticosteroids as a class suppress immune-mediated inflammation, and vasculitis after an infection is often immune-mediated. That is the only basis for the prediction.

The link is weak. Fluorometholone is formulated as eye drops with minimal systemic exposure, whereas vasculitis is a systemic disease that usually needs systemic immunosuppression. The high TxGNN score reflects a pattern in the knowledge graph, not clinical proof.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| NDA019079 | Flarex | Suspension / drops | Harrow Eye, LLC |
| NDA019079 | Flarex | Suspension / drops | Eyevance Pharmaceuticals |
| NDA019216 | FML Forte | Suspension / drops | Allergan, Inc. |
| NDA016851 | FML | Suspension / drops | Allergan, Inc. |
| NDA016851 | Fluorometholone | Solution / drops | Pacific Pharma, Inc. |

The source data lists no approved indication text for these licenses. All listed forms are ophthalmic drops.

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found. Steroid eye drops can raise intraocular pressure, which is relevant to any ocular repurposing.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction is supported only by the model score, with no trials or literature, and the mechanistic fit is weak for a systemic disease treated with a topical eye drop.

Other predictions for this drug have somewhat more support and may be better research questions:
- **Post-bacterial disorder:** a Phase 2 trial of adjunctive fluorometholone in bacterial corneal ulcers (NCT07308938, not yet recruiting) and a completed trachoma surgery adjunct study (NCT01949454).
- **Punctate epithelial keratoconjunctivitis:** two indirect publications (PMID 34011737, 35128186).

**To proceed, the following is needed:**
- The package insert warnings and contraindications, parsed from the FDA label
- Mechanism of action data (DrugBank)
- A route-compatibility assessment (topical ocular vs. systemic vasculitis)
- Any published evidence of fluorometholone in postinfectious vasculitis; without it, prioritize the ocular predictions above

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

