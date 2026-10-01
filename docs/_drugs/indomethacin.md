---
layout: default
title: Indomethacin
parent: Model Prediction Only (L5)
nav_order: 795
evidence_level: L5
indication_count: 10
---

# Indomethacin
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

# Indomethacin: From an Established NSAID to Brachydactyly-Syndactyly Syndrome

## One-Sentence Summary

Indomethacin is a marketed non-steroidal anti-inflammatory drug (NSAID) that inhibits COX-1 and COX-2.
The TxGNN model predicts it may be effective for **brachydactyly-syndactyly syndrome**, but there are **0 clinical trials** and **0 publications** for this indication.
The prediction rests on the model score alone and no plausible mechanistic link has been identified.

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Brachydactyly-syndactyly syndrome |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the source record. Based on general pharmacology, indomethacin is a non-selective COX-1/COX-2 inhibitor that reduces prostaglandin synthesis. That makes it useful for inflammation, pain, and fever.

Brachydactyly-syndactyly syndrome is a congenital limb malformation with a genetic and developmental basis. There is no known inflammatory driver that COX inhibition would address. The high score (0.9997) most likely reflects graph proximity in the knowledge graph, not a biological rationale.

Overall, this prediction is not mechanistically supported, and the evidence is model output only.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

Five of the 20 authorizations are listed below. The source data does not include approved indication text for these products.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|------|
| ANDA091240 | Indomethacin | Capsule | Bryant Ranch Prepack |
| ANDA091240 | Indomethacin | Capsule | XLCare Pharmaceuticals Inc. |
| ANDA201807 | Indomethacin | Capsule, extended release | Proficient Rx LP |
| ANDA073314 | INDOCIN | Suppository | Zyla Life Sciences US Inc. |
| ANDA091276 | INDOMETHACIN | Capsule | DIRECT RX |

Available routes are oral (capsule, extended-release capsule) and other (suppository).

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This is an L5 prediction with no trials, no literature, and no plausible mechanism. Congenital limb malformation is not expected to respond to COX inhibition.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Any mechanistic or preclinical evidence linking prostaglandin pathways to this syndrome

**Note on other predictions:** Among the top 10 predictions, only juvenile idiopathic arthritis (rank 8, L3) has meaningful literature support. That support is mostly old NSAID literature, including a 1978 double-blind trial comparing ketoprofen and indomethacin in children, and it points to symptomatic relief rather than disease modification. It is better evaluated as a separate research question against current JIA guidelines and pediatric safety data (GI, renal, and bleeding risks).

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

