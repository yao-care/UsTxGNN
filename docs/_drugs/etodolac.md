---
layout: default
title: Etodolac
parent: Model Prediction Only (L5)
nav_order: 683
evidence_level: L5
indication_count: 10
---

# Etodolac
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

# Etodolac: From a Marketed NSAID to Acromesomelic Dysplasia, Hunter-Thompson Type

## One-Sentence Summary

Etodolac is a marketed COX-inhibiting NSAID (non-steroidal anti-inflammatory drug), used for pain and rheumatic diseases.
The TxGNN model predicts it may be effective for **acromesomelic dysplasia, Hunter-Thompson type**, a rare genetic skeletal disorder.
**No clinical trials and no publications** currently support this prediction, so it rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Acromesomelic dysplasia, Hunter-Thompson type |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 (model prediction only) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 (generic ANDA licenses) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the dataset. Etodolac is a known NSAID that inhibits cyclooxygenase (COX), with reported selectivity for COX-2. It reduces prostaglandin-mediated inflammation and pain, and is widely used in rheumatoid arthritis, osteoarthritis, ankylosing spondylitis and other pain states.

Acromesomelic dysplasia, Hunter-Thompson type is a genetic skeletal dysplasia that affects growth. Its cause is a defect in skeletal development, not inflammation. COX inhibition has no plausible disease-modifying effect on this defect. At most, an NSAID could relieve secondary pain, and no retrieved evidence supports even that.

The high TxGNN score is therefore best read as a statistical association in the knowledge graph, not a mechanistically grounded hypothesis. It should not be treated as a credible repurposing lead without new supporting evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

Etodolac has 20 licenses on record. All are generic (ANDA) products, and five are shown below. The dataset does not list approved indication text for them. Available oral forms are film-coated tablet, capsule, tablet, and extended-release tablet.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA075074 | Etodolac | Tablet, film coated | Advanced Rx of Tennessee, LLC |
| ANDA076004 | Etodolac | Tablet, film coated | Bryant Ranch Prepack |
| ANDA076004 | Etodolac | Tablet, film coated | Apotex Corp. |
| ANDA208834 | Etodolac | Tablet, film coated | Advanced Rx Pharmacy of Tennessee, LLC |
| ANDA075126 | Etodolac | Capsule | ANI Pharmaceuticals, Inc. |

## Safety Considerations

Please refer to the package insert for safety information. No drug-interaction records were found in the dataset.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical trials or literature behind it, and there is no plausible mechanistic link between COX inhibition and this genetic skeletal dysplasia. It should not advance on the model score alone.

**Other predictions for etodolac in this run:**
- **Ankylosing spondylitis** (score 99.93%) has the strongest support, at evidence level L3. Support consists of reviews, open-label studies and post-marketing data. NSAIDs are also guideline-recommended first-line therapy for axial spondyloarthritis. No Phase 3 RCT of etodolac in AS was found. This is a much better candidate to pursue than the top-ranked prediction.
- **Inflammatory spondylopathy** (99.86%, L4) is supported only indirectly, through the AS evidence.
- The remaining predictions (rank 1–5 and 7–9) are L5, prediction-only, and also on Hold.

**To proceed, the following is needed:**
- The FDA package insert (warnings, contraindications, approved indications) to allow safety screening
- Mechanism of action data from DrugBank
- Any preclinical or clinical evidence linking etodolac to this condition, without which the prediction should remain deprioritised
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

