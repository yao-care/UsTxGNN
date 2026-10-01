---
layout: default
title: Ketoprofen
parent: Model Prediction Only (L5)
nav_order: 826
evidence_level: L5
indication_count: 10
---

# Ketoprofen
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

# Ketoprofen: From NSAID Pain and Inflammation Therapy to Acromesomelic Dysplasia, Hunter-Thompson Type

## One-Sentence Summary

Ketoprofen is a non-steroidal anti-inflammatory drug (NSAID) that is marketed in the US as oral capsules.
The TxGNN model predicts it may be effective for **acromesomelic dysplasia, Hunter-Thompson type**,
but there are currently **0 clinical trials** and **0 publications** supporting this prediction, so it rests on the model score alone and is likely a knowledge-graph artifact.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the license records; ketoprofen is generally used as an NSAID for pain and inflammation |
| Predicted New Indication | Acromesomelic dysplasia, Hunter-Thompson type |
| TxGNN Prediction Score | 99.98% (model rank 841) |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 5 (all listed as ANDA generic applications) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack. Based on known information, ketoprofen is a non-selective COX inhibitor, and its anti-inflammatory and analgesic effects are well established. Mechanistically, however, this does not translate to the predicted new indication.

Acromesomelic dysplasia, Hunter-Thompson type, is a skeletal dysplasia related to CDMP1/GDF5. It is a genetic disorder of bone growth, not an inflammatory disease. No plausible link between COX inhibition and this condition was identified. The very high score (99.98%) is therefore probably a knowledge-graph artifact rather than a real biological signal.

The other top-ranked predictions show the same pattern. Ranks 2 to 7 are also rare skeletal or developmental disorders, such as brachyolmia and pseudoachondroplasia, with no evidence behind them. The only prediction with any supporting logic is **spondyloarthropathy, susceptibility to** (rank 8). NSAIDs are established first-line symptomatic therapy for spondyloarthritis and reactive arthritis, but that would be class-level symptom control, not novel repurposing. Its single retrieved item (PMID 20470931, a narrative review of reactive arthritis) is only indirect evidence for ketoprofen itself.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

The license records do not include approved indication text.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA074014 | Orudis | Capsule | Allegis Pharmaceuticals, Inc. |
| ANDA074014 | Ketoprofen (3 listings) | Capsule | Misemer Pharmaceuticals, Inc. |
| ANDA075679 | Ketoprofen | Capsule, extended release | Mylan Pharmaceuticals Inc. |

All products are oral formulations.

## Safety Considerations

Please refer to the package insert for safety information. No warnings, contraindications, or drug interaction data were retrieved for this drug.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction has no clinical trials or literature and no plausible mechanistic link. It is a bone-growth genetic disorder, which COX inhibition would not be expected to alter. Nothing supports moving it forward.

**To proceed, the following is needed:**
- The FDA package insert warnings and contraindications, which are missing and block safety screening
- Mechanism of action data from DrugBank
- If any follow-up is pursued, refocus on **spondyloarthropathy** (rank 8), where the question is compound-specific efficacy and safety versus other NSAIDs, starting with a targeted literature search and trial registry review
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

