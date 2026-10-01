---
layout: default
title: Tretinoin
parent: Model Prediction Only (L5)
nav_order: 1257
evidence_level: L5
indication_count: 10
---

# Tretinoin
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

# Tretinoin: From Topical Retinoid Use to Rheumatoid Nodulosis

## One-Sentence Summary

Tretinoin is a retinoid that is currently marketed in the US as topical gel, lotion, and cream products.
The TxGNN model predicts it may be effective for **rheumatoid nodulosis**, but **no clinical trials and no publications** were retrieved for this prediction.
This is a model-only signal (Evidence Level L5) and should be treated as a hypothesis, not a development candidate.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the retrieved US label data |
| Predicted New Indication | Rheumatoid nodulosis |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, tretinoin is a retinoid, and retinoid signaling influences immune and inflammatory pathways. Mechanistically it might be applicable to inflammatory arthritis-related conditions, but this link is indirect.

The high TxGNN score most likely reflects proximity in the knowledge graph to inflammatory arthritis nodes, not a validated mechanism. Retinoic acid is known to modulate T-cell differentiation (Treg/Th17 balance), which is conceptually relevant to autoimmune joint disease. No trial, preclinical study, or publication was retrieved to confirm that this applies to rheumatoid nodulosis.

Most of the top-ranked predictions fall in the same area: juvenile idiopathic arthritis (JIA) and its synonyms, spondyloarthropathy, and rare skeletal dysplasias. Several of these are pediatric or skeletal conditions, where retinoid skeletal toxicity is a particular concern.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

All five listed products are topical or lotion formulations. The retrieved data contains no indication text for them.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA218246 | Tretinoin (Aurobindo Pharma Limited) | Gel | Not listed in retrieved data |
| NDA022070 | Tretinoin (Oceanside Pharmaceuticals) | Gel | Not listed in retrieved data |
| ANDA217588 | Tretinoin (Encube Ethicals, Inc.) | Gel | Not listed in retrieved data |
| NDA020475 | Retin-A MICRO (Bausch Health US LLC) | Gel | Not listed in retrieved data |
| NDA209353 | Altreno (Bausch Health US, LLC) | Lotion | Not listed in retrieved data |

---

## Safety Considerations

Please refer to the package insert for safety information. No drug-interaction records were found.

The prediction-level assessments raise these points:
- **Skeletal toxicity**: Retinoid excess is associated with premature epiphyseal closure, hyperostosis, and enthesopathy-like changes. This matters for the pediatric arthritis and spondyloarthropathy predictions.
- **Teratogenicity**: Tretinoin is teratogenic.
- **Route mismatch**: All US products found are topical, and route compatibility with a systemic joint or nodule indication has not been assessed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone, with no trials, no literature, and no mechanistic data for rheumatoid nodulosis. The skeletal-toxicity profile of retinoids and the topical-only product forms make the rationale unfavorable.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (currently blocking safety screening)
- Mechanism of action data from DrugBank
- A literature and trial search specific to rheumatoid nodulosis, plus preclinical evidence on retinoid effects in nodule formation
- A route and exposure assessment (topical versus systemic)

**Other predicted indications worth noting:**
- **Osteoarthritis (rank 7, L4, "Research Question")**: This is the only prediction with a relevant evidence base. It is genetic and preclinical, with no clinical trials. The evidence conflicts in direction. ALDH1A2 variant data (PMID 36542696) and a GWAS-to-drug analysis (PMID 37418291) suggest that raising retinoic acid signaling may help. A 2025 study of retinoic acid-induced osteoarthritis (PMID 40564983) suggests that exogenous retinoic acid may harm cartilage. It is hypothesis-generating only, and dose, route, and local versus systemic exposure must be clarified first.
- **Quinquaud's folliculitis decalvans (rank 10, L4, Hold)**: The only retrieved item is a case report on folliculitis spinulosa decalvans, a different entity. It does not support tretinoin and may be a name-matching artifact.
- **JIA cluster (ranks 2–4, 6)**: "Juvenile idiopathic arthritis," "juvenile chronic polyarthritis," and the RF-positive polyarticular subtype overlap and should be consolidated for review.

*This report is for research reference only and does not constitute medical advice. Predicted candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

