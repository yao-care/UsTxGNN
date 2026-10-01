---
layout: default
title: Emicizumab
parent: Model Prediction Only (L5)
nav_order: 649
evidence_level: L5
indication_count: 10
---

# Emicizumab
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

# Emicizumab: From Hemophilia A to Pseudo-von Willebrand Disease

## One-Sentence Summary

Emicizumab is a bispecific antibody that mimics activated factor VIII. Per the literature in the Evidence Pack, it was approved for congenital hemophilia A.
The TxGNN model predicts it may be effective for **pseudo-von Willebrand disease** (platelet-type von Willebrand disease), but **no clinical trials and no publications** support this prediction, so it is a model-only signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Congenital hemophilia A (from the literature; the license indication text in the data is empty) |
| Predicted New Indication | Pseudo-von Willebrand disease |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 6 (all under a single BLA, BLA761083) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data for emicizumab is not available in the Evidence Pack. From the related literature, emicizumab bridges factor IXa and factor X and mimics the cofactor function of activated factor VIII. It is therefore a coagulation-cascade agent.

Platelet-type (pseudo) von Willebrand disease is a different kind of disorder. It is caused by a gain-of-function defect in platelet GPIb-alpha, which leads to platelet clearance. Emicizumab does not target this pathway.

Both diseases are bleeding disorders, which may explain the high model score. However, the mechanistic link is weak, and the score alone is not enough to support a repurposing case.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| BLA761083 | Hemlibra (Genentech, Inc.) | Injection, solution | Not listed in the source data |

The source data lists this same authorization five times. It is shown once here.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The high TxGNN score (99.99%) for pseudo-von Willebrand disease is not supported by any trial or publication. The disease involves a platelet defect that emicizumab's mechanism does not address.

**To proceed, the following is needed:**
- Mechanistic evidence that a FVIIIa mimetic could compensate for the platelet GPIb-alpha defect
- Case reports or preclinical data in platelet-type von Willebrand disease
- The package insert warnings and contraindications, which are still missing
- A safety review of thrombotic risk

**Note on other candidates:** Among the other predictions, **acquired coagulation factor deficiency** (rank 5) has much stronger support. It has a Phase 3 single-arm trial (AGEHA, PMID 36696195) and a Phase 2 single-arm trial (GTH-AHA-EMI, PMID 37858328), both in acquired hemophilia A. It is rated L2 with a "Proceed with Guardrails" recommendation. That evidence applies only to acquired hemophilia A, not to acquired factor deficiencies in general. It is worth a separate report.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

