---
layout: default
title: Oxaprozin
parent: Model Prediction Only (L5)
nav_order: 1000
evidence_level: L5
indication_count: 10
---

# Oxaprozin
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

# Oxaprozin: From an NSAID to Acromesomelic Dysplasia, Hunter-Thompson Type

## One-Sentence Summary

Oxaprozin is a nonsteroidal anti-inflammatory drug (NSAID) that inhibits COX-1 and COX-2, and it is currently marketed in the United States.
The TxGNN model predicts it may be effective for **acromesomelic dysplasia, Hunter-Thompson type**, but **0 clinical trials** and **0 publications** support this prediction.
The result rests on a knowledge-graph score alone and is not credible as a repurposing lead.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Acromesomelic dysplasia, Hunter-Thompson type |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 14 |
| Recommended Decision | Hold |

The supplied records do not include an approved indication for oxaprozin, so the original indication is omitted from this table.

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the record. Based on known information, oxaprozin is an NSAID that inhibits COX-1 and COX-2, so its effects are anti-inflammatory and analgesic.

The predicted disease is a rare genetic skeletal dysplasia caused by defects in the CDMP1/GDF5 pathway. COX inhibition does not address this underlying defect, and no plausible mechanistic link was identified. The score of 0.9998 (model rank 1140) is a knowledge-graph output with no trial or literature evidence behind it.

The other nine top predictions show the same pattern. Most are rare genetic or developmental disorders with no plausible link to COX inhibition, such as brachyolmia, pseudoachondroplasia and brachydactyly-syndactyly syndrome. Three are inflammatory-joint conditions where NSAIDs are a standard symptomatic class:

- **Rheumatoid factor-positive polyarticular juvenile idiopathic arthritis** (score 99.67%) is the most mechanistically coherent candidate. Oxaprozin may already carry labeling for juvenile arthritis, which would make it an existing use rather than repurposing. This must be checked against the label.
- **Spondyloarthropathy, susceptibility to** (99.93%) and **rheumatoid nodulosis** (99.73%) are supported only by class-level reasoning, not oxaprozin-specific data.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

The record lists 14 authorizations. The main ones are below; approved indication text was not provided for any of them.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA208633 | Oxaprozin | Tablet | Bryant Ranch Prepack |
| ANDA075845 | Oxaprozin | Tablet | St. Mary's Medical Park Pharmacy |
| ANDA075855 | Oxaprozin | Tablet, film coated | Bryant Ranch Prepack |
| ANDA075855 | Oxaprozin | Tablet, film coated | Proficient Rx LP |
| NDA217927 | Oxaprozin | Capsule | Ayurax, LLC |

All listed forms are oral.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score, with no trials, no literature and no plausible mechanistic link to a genetic skeletal dysplasia. The evidence level is L5, and the pipeline is still at stage S0.

**To proceed, the following is needed:**
- Package insert warnings and contraindications, which are a blocking gap for safety screening
- Detailed mechanism of action data (MOA) from DrugBank
- Confirmation of oxaprozin's approved indications, including whether juvenile arthritis is already labeled
- If the team wants to pursue this drug at all, re-evaluating the inflammatory-joint predictions (juvenile idiopathic arthritis, spondyloarthropathy) in place of the top-ranked skeletal dysplasia, along with a targeted literature and trial search for those conditions
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

