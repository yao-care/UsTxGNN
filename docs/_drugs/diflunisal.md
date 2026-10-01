---
layout: default
title: Diflunisal
parent: Model Prediction Only (L5)
nav_order: 606
evidence_level: L5
indication_count: 10
---

# Diflunisal
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

# Diflunisal: From NSAID Pain and Arthritis Therapy to Acromesomelic Dysplasia, Hunter-Thompson Type

## One-Sentence Summary

Diflunisal is a salicylate-derived NSAID (COX inhibitor) marketed in the US as generic tablets. The TxGNN model predicts it may be effective for **acromesomelic dysplasia, Hunter-Thompson type**, but **no clinical trials and no publications** support this prediction. The link most likely reflects knowledge-graph proximity rather than a real mechanism.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the pack (approved-indication text is empty); diflunisal is generally used as an NSAID for pain and arthritis |
| Predicted New Indication | Acromesomelic dysplasia, Hunter-Thompson type |
| TxGNN Prediction Score | 99.99% (model rank 548) |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 7 (the listed licenses are ANDAs) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the pack. Diflunisal is an NSAID that inhibits COX-1 and COX-2 and reduces prostaglandin-mediated inflammation and pain.

The predicted disease is a monogenic skeletal dysplasia driven by the CDMP1/GDF5 pathway, which controls chondrogenic signaling. COX inhibition has no known effect on this pathway. I found **no plausible mechanistic link**. The high score most likely comes from the drug sitting close to musculoskeletal nodes in the knowledge graph, not from a causal relationship. Because the disease is a structural genetic defect, an NSAID could at most relieve secondary pain and would not modify the disease.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

The pack lists 5 of the 7 licenses. Approved-indication text was not provided for any of them.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA202845 | Dolobid (INA Pharmaceutics Inc) | Tablet, film coated | Not provided |
| ANDA203547 | Diflunisal (Zydus Lifesciences Limited) | Tablet | Not provided |
| ANDA202845 | Diflunisal (Heritage Pharmaceuticals / Avet Pharmaceuticals) | Tablet, film coated | Not provided |
| ANDA073673 | Diflunisal (Teva Pharmaceuticals USA) | Tablet, film coated | Not provided |
| ANDA203547 | Diflunisal (Zydus Pharmaceuticals USA) | Tablet | Not provided |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is no clinical or literature evidence (L5, model prediction only). The mechanism is implausible, since an NSAID does not act on GDF5/CDMP1 signaling. The score is most likely a graph-topology artifact.

Among the other top-10 predictions, **ankylosing spondylitis** has the most support (L3). It rests mainly on a 1986 comparison of diflunisal and phenylbutazone (PMID 3524970). NSAIDs are already established therapy for that disease, so it is a label-status question rather than a new repurposing finding. It is a better candidate for follow-up than the rank 1 prediction.

**To proceed, the following is needed:**
- Package insert warnings and contraindications, to complete safety screening
- Mechanism of action data from DrugBank
- Approved-indication text for the US labels
- For the ankylosing spondylitis lead: full-text review of PMID 3524970 to confirm randomization, blinding and sample size
- For the rank 1 disease: no action until independent preclinical or clinical evidence appears

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

