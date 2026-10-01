---
layout: default
title: Triprolidine
parent: Model Prediction Only (L5)
nav_order: 1266
evidence_level: L5
indication_count: 7
---

# Triprolidine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
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

# Triprolidine: From Antihistamine (Labeled Indication Not Recorded) to Allergic Urticaria

## One-Sentence Summary

Triprolidine is a first-generation H1-receptor antagonist (antihistamine) that is marketed in the US in oral liquid products. The TxGNN model predicts it may be effective for **allergic urticaria** with a very high score, but **no clinical trials and no publications** currently support this specific drug-disease pair, so it remains a research question.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Allergic urticaria |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 (model prediction only) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 4 |
| Recommended Decision | Hold |

The record has no approved indication text, so the original indication is omitted here.

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in DrugBank for this drug. Based on known pharmacology, triprolidine is a first-generation H1-receptor antagonist. In allergic urticaria, histamine released from mast cells drives wheals and itch, so blocking the H1 receptor is mechanistically plausible.

H1 antihistamines are the standard first-line drug class for urticaria. The very high TxGNN score probably reflects this class effect rather than any triprolidine-specific finding.

This is a class-level inference only. No studies of triprolidine in allergic urticaria were retrieved, and the original indication is not recorded in the Evidence Pack.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

For context, the second-ranked prediction, **cold urticaria**, has one indirect publication: [PMID 2901993](https://pubmed.ncbi.nlm.nih.gov/2901993/) (1988, Dermatologica). It is a double-blind crossover RCT in 18 patients showing that acrivastine, a triprolidine derivative, reduced wheal area versus placebo and was more effective than cyproheptadine. It did not test triprolidine itself.

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| M012 | HISTEX | Syrup | Not specified in record |
| M012 | HISTEX PD Drops New Formulation | Syrup | Not specified in record |
| M012 | TRIPROLIDINE HYDROCHLORIDE (Westminster Pharmaceuticals) | Syrup | Not specified in record |
| M012 | Childrens PediaClear PD | Liquid | Not specified in record |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is mechanistically sensible because H1 blockade is a standard approach in urticaria. However, the evidence level is L5, with no trials, no literature, and no mechanism or safety data in the record. This is not enough to support further investment.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- A targeted literature search for triprolidine in urticaria, including single-ingredient and combination products
- Confirmation of the labeled indications of the four US products
- Consideration of cold urticaria (rank 2) as a better-supported alternative direction, since it has indirect RCT evidence from a structural analog
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

