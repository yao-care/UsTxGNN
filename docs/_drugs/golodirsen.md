---
layout: default
title: Golodirsen
parent: Model Prediction Only (L5)
nav_order: 759
evidence_level: L5
indication_count: 4
---

# Golodirsen
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

# Golodirsen: From Duchenne Muscular Dystrophy to Distal Myopathy, Welander Type

## One-Sentence Summary

Golodirsen (Vyondys 53) is an antisense oligonucleotide that skips exon 53 of the DMD gene. The source record leaves the original indication blank, but this use is known for Duchenne muscular dystrophy.
The TxGNN model predicts it may be effective for **distal myopathy, Welander type**, but **0 clinical trials** and **0 publications** currently support this direction, so it remains a model-only prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Duchenne muscular dystrophy amenable to exon 53 skipping (the approved-indication text is blank in the source record; this is from general knowledge) |
| Predicted New Indication | Distal myopathy, Welander type |
| TxGNN Prediction Score | 99.11% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the source record. From general knowledge, golodirsen is a phosphorodiamidate morpholino oligomer. Its sequence binds DMD exon 53 pre-mRNA and induces exon skipping, which allows a shortened dystrophin protein to be produced.

**The mechanistic link is weak.** Welander distal myopathy is linked to a recurrent TIA1 variant, a different gene with a different disease mechanism. Golodirsen's sequence is specific to DMD exon 53 and would not act on TIA1 transcripts. The high score (0.991) most likely reflects that both are muscle diseases and sit close together in the knowledge graph. It does not indicate a shared target or pathway.

The other three predictions show the same pattern: none has a direct mechanistic link.
- **Nebulin-related early-onset distal myopathy (99.07%)**: This is an NEB-gene disease. Exon skipping is a class-level concept, but any NEB approach would need a newly designed, gene-specific oligonucleotide.
- **Obsolete autosomal dominant limb-girdle muscular dystrophy type 1C (99.04%)**: This is a caveolinopathy caused by CAV3 variants. The disease term is obsolete, so its mapping to a current disease entity should be checked first.
- **X-linked myopathy with postural muscle atrophy (99.02%)**: This is caused by VMA21 variants that impair V-ATPase assembly and autophagy, unrelated to dystrophin restoration.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA211970 | Vyondys 53 (Sarepta Therapeutics, Inc.) | Injection | Not provided in the source record |

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found for this drug.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a knowledge-graph score, with no clinical trials or publications. The mechanism is also incompatible: golodirsen's sequence is specific to DMD exon 53 and does not target TIA1.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data confirmed from DrugBank
- Any preclinical evidence, or a gene-specific oligonucleotide design, showing a plausible link to the TIA1 variant
- Confirmation of the current disease entity for the obsolete LGMD1C term, if that prediction is reviewed further
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

