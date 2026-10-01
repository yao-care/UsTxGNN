---
layout: default
title: Ceftazidime
parent: Model Prediction Only (L5)
nav_order: 507
evidence_level: L5
indication_count: 10
---

# Ceftazidime
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

# Ceftazidime: From Bacterial Infections to Polyclonal Hyperviscosity Syndrome

## One-Sentence Summary

Ceftazidime is a third-generation cephalosporin antibiotic that is marketed in the United States as an injectable.
The TxGNN model predicts it may be effective for **polyclonal hyperviscosity syndrome**, but there are **0 clinical trials** and **0 publications** supporting this direction, and no plausible mechanism links the two.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bacterial infections (the US license records provide no indication text) |
| Predicted New Indication | Polyclonal hyperviscosity syndrome |
| TxGNN Prediction Score | 99.51% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 11 (the listed licenses are ANDAs) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the record. Ceftazidime is a bactericidal beta-lactam that inhibits bacterial cell wall synthesis, and its efficacy in bacterial infections is well established.

That mechanism does not extend to the predicted indication. Polyclonal hyperviscosity syndrome is caused by excess immunoglobulin raising blood viscosity, and it has no bacterial target for ceftazidime to act on. The very high TxGNN score (99.51%) reflects a pattern in the knowledge graph, not a biological or clinical rationale.

This prediction should therefore be treated as a likely false positive until independent evidence appears.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

The license records do not include approved indication text, so that column is omitted.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA064032 | TAZICEF | Injection, powder, for solution | Hospira, Inc. |
| ANDA062640 | Ceftazidime | Injection, powder, for solution | WG Critical Care, LLC |
| ANDA062640 | Ceftazidime | Injection, powder, for solution | Sagent Pharmaceuticals |
| ANDA062662 | TAZICEF | Injection, powder, for solution | Hospira, Inc. |

Ceftazidime is available only as an injectable in the US records.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting trials or literature and no plausible mechanism, so it does not justify further investment as it stands.

**To proceed, the following is needed:**
- Independent evidence of a biological link between ceftazidime and hyperviscosity from excess immunoglobulin. Without it, the prediction should be deprioritized.
- The original indication text and package insert warnings and contraindications for ceftazidime.
- Review of other ceftazidime predictions in the same Evidence Pack, which have stronger support:
  - **Urinary tract infection** (L2): the trials mostly involve ceftazidime-avibactam or other combinations, so they support the class more than ceftazidime alone. Proceed only with stewardship, culture-guided use and renal dose adjustment.
  - **Infectious otitis media** (L3): several small, older pediatric studies of ceftazidime in Pseudomonas-related chronic suppurative otitis media.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

