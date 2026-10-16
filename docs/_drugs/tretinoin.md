---
layout: default
title: Tretinoin
parent: Model Prediction Only (L5)
nav_order: 1257
evidence_level: L5
indication_count: 10
monitor_inn: "TRETINOIN"
predicted_indications: ["rheumatoid nodulosis", "rheumatoid factor-positive polyarticular juvenile idiopathic arthritis", "juvenile idiopathic arthritis", "juvenile chronic polyarthritis", "spondyloarthropathy, susceptibility to", "juvenile arthritis due to defect in LACC1", "osteoarthritis", "pseudoachondroplasia", "acromesomelic dysplasia, Hunter-Thompson type", "Quinquaud's folliculitis decalvans"]
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

# Tretinoin: From Acne and Acute Promyelocytic Leukemia to Rheumatoid Nodulosis

## One-Sentence Summary

Tretinoin is a retinoid originally used for acne, acute promyelocytic leukemia, acquired keratosis and palmoplantar keratoderma.
The TxGNN model predicts it may be effective for **rheumatoid nodulosis**, but **no clinical trials** and **no relevant publications** currently support this prediction.
The prediction is computational only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acne, acute promyelocytic leukemia, acquired keratosis, palmoplantar keratoderma (from the knowledge graph; no approved-indication text is available in the US license records) |
| Predicted New Indication | Rheumatoid nodulosis |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (no currently valid licenses) |
| Number of NDAs | 16 licenses in total (6 NDAs and 10 ANDAs), all cancelled |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Tretinoin is a retinoid (a vitamin A derivative) with established efficacy in acne and acute promyelocytic leukemia. Mechanistically, it may be applicable to rheumatoid nodulosis, but this has not been tested.

A plausible but unverified link is retinoid-mediated modulation of inflammation and of fibroblast and tissue remodeling. The high TxGNN score (0.998) reflects network proximity in the knowledge graph, not demonstrated efficacy. Rheumatoid nodulosis is also very different from the original indications (skin keratinization disorders and a blood cancer), so the similarity to the original use has not been established.

The other top predictions are mostly juvenile and rheumatoid-type arthritis conditions (for example rheumatoid factor-positive polyarticular juvenile idiopathic arthritis, juvenile idiopathic arthritis, and juvenile chronic polyarthritis) and skeletal dysplasias. None has trial or literature support. The pediatric and skeletal ones also raise safety concerns, because retinoids can harm bone growth.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for rheumatoid nodulosis.

For reference, the only publications retrieved for any top-ranked prediction concern osteoarthritis (rank 7), and neither supports tretinoin use:
- [34745498](https://pubmed.ncbi.nlm.nih.gov/34745498/) (2021): intra-articular PRP for knee osteoarthritis; unrelated to tretinoin.
- [18463343](https://pubmed.ncbi.nlm.nih.gov/18463343/) (2008): case report of adverse events after arsenic trioxide in acute promyelocytic leukemia; not relevant to osteoarthritis efficacy.

## US Market Information

All 16 US licenses are cancelled and no approved-indication text is on record. The five main ones are:

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA022070 | Tretinoin (Oceanside Pharmaceuticals) | Gel | Not recorded |
| NDA020475 | Retin-A MICRO (Bausch Health US LLC) | Gel | Not recorded |
| NDA209353 | Altreno (Bausch Health US, LLC) | Lotion | Not recorded |
| NDA021108 | Renova (Bausch Health US LLC) | Cream | Not recorded |
| NDA017955 | Retin-A (Bausch Health US, LLC) | Gel | Not recorded |

All listed products are topical (gel, cream, lotion). No systemic formulation appears in the data compiled for this report.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Differentiating agent (retinoid) used in acute promyelocytic leukemia; not a conventional cytotoxic |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

- **Knowledge-graph contraindication signals** (not label text) cover many conditions. Examples are:
  - Liver, kidney, pancreatic and gallbladder disease
  - Congestive heart failure
  - Diabetes mellitus and diabetic ketoacidosis
  - Osteoporosis
  - Inflammatory bowel disease and Crohn disease
  - Atopic eczema and sunburn
  - Psychiatric disorders (anxiety, psychotic and other mental disorders)
  - Adrenocortical insufficiency
  - Mycosis fungoides and primary cutaneous T-cell lymphoma
- **Drug Interactions**: 100 interactions were found. The major-level ones are:
  - Doxycycline
  - Tetracycline
  - Minocycline
  - Vitamin A

  Moderate-level interactions include aprepitant, clarithromycin and naltrexone. Levofloxacin is a minor interaction.
- **Pediatric and skeletal concern**: systemic retinoids can cause bone toxicity, including premature epiphyseal closure in growing children. This matters for the juvenile arthritis and skeletal dysplasia predictions.

Please refer to the package insert for full warnings and contraindications, which were not available for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests solely on a computational score. There are no clinical trials or supporting publications, and the evidence level is L5. Mechanism data, label safety data, and route compatibility are missing, and there is no active US license.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data (for example from DrugBank)
- Preclinical or mechanistic studies linking retinoic acid signaling to rheumatoid nodulosis
- An assessment of route and formulation compatibility, since the licensed products are topical and the predicted disease is systemic
- A review of systemic retinoid toxicity relevant to the predicted populations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

