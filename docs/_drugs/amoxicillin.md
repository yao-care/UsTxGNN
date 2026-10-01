---
layout: default
title: Amoxicillin
parent: Model Prediction Only (L5)
nav_order: 333
evidence_level: L5
indication_count: 8
---

# Amoxicillin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **8** 
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

# Amoxicillin: From Bacterial Infections to Polyclonal Hyperviscosity Syndrome

## One-Sentence Summary

Amoxicillin is a beta-lactam antibacterial widely marketed in the United States for bacterial infections.
The TxGNN model predicts it may be effective for **polyclonal hyperviscosity syndrome**, with a very high score (99.63%).
However, there are **0 clinical trials** and **0 publications** supporting this specific prediction, so it rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bacterial infections (general use of the antibacterial class; approved indication text was not supplied in the data) |
| Predicted New Indication | Polyclonal hyperviscosity syndrome |
| TxGNN Prediction Score | 99.63% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, amoxicillin is a beta-lactam antibacterial, its efficacy in bacterial infections is well established, but no mechanistic route to polyclonal hyperviscosity syndrome has been identified.

Polyclonal hyperviscosity syndrome is a non-infectious protein and hematologic disorder. Antibacterial cell-wall inhibition has no obvious connection to it. The high TxGNN score (0.996) is a model output only and should not be read as evidence of efficacy.

The same pattern appears in the other top predictions (hyperamylasemia, congenital analbuminemia, premalignant hematological disease). They share nearly identical scores and lack supporting studies, which suggests a general model tendency rather than a drug-specific signal.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA065271 | Amoxicillin | Capsule | American Health Packaging |
| ANDA064076 | Amoxicillin | Capsule | REMEDYREPACK INC. |
| ANDA065334 | Amoxicillin | Powder, for suspension | Proficient Rx LP |
| ANDA065387 | Amoxicillin | Powder, for suspension | NuCare Pharmaceuticals, Inc. |
| ANDA065325 | Amoxil | Powder, for suspension | DirectRx |

Approved indication text was not provided for these authorizations. All five are generic (ANDA) approvals, and 20 authorizations exist in total. Available forms include oral capsules, film-coated tablets, and powder for suspension.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical trials, no literature, and no plausible mechanism. The target is a non-infectious hematologic condition unrelated to amoxicillin's antibacterial action. Amoxicillin is safe to obtain and widely available, but that does not justify pursuing this indication.

**To proceed, the following is needed:**
- Mechanism of action data (MOA) and an explicit hypothesis linking it to polyclonal hyperviscosity syndrome
- FDA package insert warnings and contraindications (a blocking gap for safety screening)
- Any preclinical or clinical signal for this indication
- Route and dosage-form compatibility assessment

Among the other predictions, rank 6 (monoclonal gammopathy) and rank 8 (septicemic plague) have some literature. Neither is amoxicillin-specific efficacy evidence. The monoclonal gammopathy papers show indirect antibiotic-responsive lymphoproliferative disease. The plague papers are mostly in vitro or animal work, and standard plague treatment uses other antibiotic classes. Both would need expert review before any follow-up.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

