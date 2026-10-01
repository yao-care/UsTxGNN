---
layout: default
title: Meloxicam
parent: Model Prediction Only (L5)
nav_order: 895
evidence_level: L5
indication_count: 10
---

# Meloxicam
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

# Meloxicam: From Arthritis Treatment to Acromesomelic Dysplasia, Hunter-Thompson Type

## One-Sentence Summary

Meloxicam is a preferential COX-2 inhibitor (NSAID) that is widely marketed in the US as an oral tablet, and it is generally used for arthritis pain and inflammation.
The TxGNN model ranks **acromesomelic dysplasia, Hunter-Thompson type** as its top new-indication prediction.
There are **0 clinical trials** and **0 publications** supporting it, and the mechanism does not fit, so this is a graph-based prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Acromesomelic dysplasia, Hunter-Thompson type |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 (all listed licenses are ANDA generics) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

It is not, on current evidence. Detailed mechanism of action data for meloxicam is not in the Evidence Pack. From general pharmacology, meloxicam preferentially inhibits COX-2 and reduces prostaglandin-driven pain and inflammation.

Acromesomelic dysplasia, Hunter-Thompson type is a genetic skeletal dysplasia caused by loss of function in the CDMP1/GDF5 pathway. A COX-2 inhibitor cannot correct that defect. The high TxGNN score reflects graph proximity only, not a plausible biological link.

The other top-10 predictions show the same pattern. Most are rare genetic syndromes with no plausible link to COX-2 inhibition (brachyolmia, WHIM syndrome, and others). Three are more plausible than the top-ranked prediction:

| Rank | Predicted Indication | Score | Assessment |
|------|------|------|------|
| 6 | Spondyloarthropathy, susceptibility to | 99.52% | Biologically plausible (NSAIDs are standard symptomatic therapy). It is a genetic susceptibility term, not a treatable clinical entity, so evidence should be re-collected for axial spondyloarthritis. |
| 8 | RF-positive polyarticular juvenile idiopathic arthritis | 99.44% | Plausible, with L4 evidence. The only candidate with any literature, and it is class-level and indirect. |
| 5 | Pseudoachondroplasia | 99.81% | Weak and indirect. At most symptomatic joint pain relief. |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for the top-ranked indication.

For reference, the only publication in the pack is attached to rank 8 (JIA):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25057265](https://pubmed.ncbi.nlm.nih.gov/25057265/) | 2014 | Cohort (inferred from title) | Pediatric rheumatology online journal | Phase 4 registry on the long-term safety of celecoxib versus nonselective NSAIDs in JIA. Class-level data with no meloxicam-specific efficacy. |

## US Market Information

The pack lists 20 licenses, all tablets. The five main ones are below. Approved indication text is not provided in the pack.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA077920 | Meloxicam | Tablet | AiPing Pharmaceutical, Inc |
| ANDA077927 | Meloxicam | Tablet | REMEDYREPACK INC. |
| ANDA077918 | Meloxicam | Tablet | Aphena Pharma Solutions - Tennessee, LLC |
| ANDA217579 | Meloxicam | Tablet | XLCare Pharmaceuticals, Inc. |
| ANDA077929 | Meloxicam | Tablet | Northwind Health Company, LLC |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction has no clinical or literature support and no plausible mechanistic link, because meloxicam cannot correct a CDMP1/GDF5 genetic defect. The score is a graph artifact, and the evidence level is L5.

**To proceed, the following is needed:**
- Obtain the FDA package insert (warnings, contraindications, approved indications) to unblock safety screening
- Retrieve mechanism of action data from DrugBank
- Re-target evidence collection to the more plausible candidates: axial spondyloarthritis (rank 6) and JIA (rank 8, including meloxicam-specific pediatric data)
- Do not advance the top-ranked genetic skeletal dysplasia without new mechanistic or clinical evidence

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

