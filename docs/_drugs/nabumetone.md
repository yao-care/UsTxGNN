---
layout: default
title: Nabumetone
parent: Model Prediction Only (L5)
nav_order: 949
evidence_level: L5
indication_count: 10
---

# Nabumetone
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

# Nabumetone: From NSAID Anti-Inflammatory Therapy to Acromesomelic Dysplasia, Hunter-Thompson Type

## One-Sentence Summary

Nabumetone is an NSAID prodrug whose active metabolite (6-MNA) inhibits COX enzymes. The TxGNN model predicts it may be effective for **acromesomelic dysplasia, Hunter-Thompson type**, a rare genetic skeletal disorder. **No clinical trials and no publications** currently support this prediction, and no plausible mechanistic link has been identified.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the US licence data provided (NSAID, COX inhibitor) |
| Predicted New Indication | Acromesomelic dysplasia, Hunter-Thompson type |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 (the listed licences are ANDA generics) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Nabumetone is an NSAID prodrug, and its active metabolite 6-MNA inhibits COX enzymes and prostaglandin synthesis.

For this predicted indication, the mechanistic link is weak. Acromesomelic dysplasia, Hunter-Thompson type, is a genetic skeletal dysplasia related to CDMP1/GDF5 growth-factor signaling. COX inhibition does not address that defect. The high TxGNN score (0.9999) is a graph-based prediction with no clinical or literature support in the provided data, so it should not be read as evidence of efficacy.

Among the top 10 predictions, only **spondyloarthropathy, susceptibility to** (rank 8, score 99.94%) has a biologically plausible rationale. NSAIDs are class-level first-line therapy for spondyloarthritis. This rationale comes from general pharmacology, not from supplied evidence, so it also remains L5. It is flagged as a research question.

Other predictions with only a symptomatic or speculative link:
- **Pseudoachondroplasia**: an NSAID may relieve joint pain but would not modify the underlying pathology.
- **Rheumatoid nodulosis**: an NSAID may relieve joint symptoms but is not known to resolve nodules.
- **Myosclerosis**: the link is speculative.

The remaining predictions (brachyolmia, brachyolmia-amelogenesis imperfecta syndrome, colobomatous microphthalmia-rhizomelic dysplasia syndrome, brachydactyly-syndactyly syndrome, WHIM syndrome) have no plausible link.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA078420 | Nabumetone | Tablet | Proficient Rx LP |
| ANDA078671 | Nabumetone | Tablet, film coated | Northwind Health Company, LLC |
| ANDA078420 | Nabumetone | Tablet | Westminster Pharmaceuticals, LLC |
| ANDA078671 | Nabumetone | Tablet, film coated | PD-Rx Pharmaceuticals, Inc. |
| ANDA091083 | Nabumetone | Tablet, film coated | Proficient Rx LP |

All listed forms are oral. In total, 20 licences are recorded and 5 are shown here.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on the TxGNN score, with no trials, no literature and no plausible mechanistic link to a GDF5-related skeletal dysplasia. The evidence level is L5 and the decision stage is S0.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- A targeted literature search for nabumetone in axial spondyloarthritis, the most plausible candidate in this set
- Any preclinical or clinical evidence for the rank-1 indication before it is reconsidered

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

