---
layout: default
title: Dutasteride
parent: Model Prediction Only (L5)
nav_order: 636
evidence_level: L5
indication_count: 10
---

# Dutasteride
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

# Dutasteride: From Benign Prostatic Hyperplasia to Ambras Type Hypertrichosis Universalis Congenita

## One-Sentence Summary

Dutasteride is an oral 5-alpha reductase inhibitor. The Evidence Pack does not list its original indication, but the drug is generally known for benign prostatic hyperplasia (BPH).
The TxGNN model predicts it may be effective for **Ambras type hypertrichosis universalis congenita**.
**No clinical trials and no publications** support this prediction, and no plausible mechanism was identified.

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Ambras type hypertrichosis universalis congenita |
| TxGNN Prediction Score | 99.998% (rank 159) |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 (ANDA generics) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Dutasteride inhibits 5-alpha reductase types 1 and 2, which lowers dihydrotestosterone (DHT). Detailed mechanism data and the original indication are not available in the source data, so the link to the labeled use could not be checked.

The prediction is hard to justify mechanistically. Ambras syndrome is a congenital hypertrichosis linked to a chromosome 8q regulatory rearrangement affecting *TRPS1*. It is not driven by androgens or DHT. The high score probably reflects proximity to hair-related nodes in the knowledge graph rather than a real therapeutic relationship.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

The five main authorizations are below. The approved-indication text is empty in the source data.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA209909 | Dutasteride | Capsule, liquid filled | A-S Medication Solutions |
| ANDA209909 | Dutasteride | Capsule, liquid filled | NuCare Pharmaceuticals, Inc. |
| ANDA203118 | Dutasteride | Capsule | Amneal Pharmaceuticals LLC |
| ANDA204376 | Dutasteride | Capsule, liquid filled | Marksans Pharma Limited |
| ANDA206574 | Dutasteride | Capsule, liquid filled | Bryant Ranch Prepack |

All listed products are oral.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone (L5). There are no trials and no literature. Ambras syndrome is not a DHT-dependent condition, so no credible mechanism supports dutasteride here.

Other top-10 candidates are no stronger:
- Rank 3 (malformation syndrome with a periodontal component) has 20 publications, but they are general periodontitis papers that never mention dutasteride.
- Rank 8 (diffuse alopecia areata) is the only candidate labeled a research question. Its single item is an indirect review of androgenetic alopecia in women, and alopecia areata is autoimmune.

**To proceed, the following is needed:**
- The original indication and mechanism of action from DrugBank, plus the package insert warnings and contraindications
- A drug-specific literature search for dutasteride and hypertrichosis, as opposed to disease-keyword matching
- Clarification of the disease mapping, especially "diffuse alopecia areata" versus androgenetic alopecia
- Any further work should be limited to androgen-related hair disorders, and only if the mapping is confirmed

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

