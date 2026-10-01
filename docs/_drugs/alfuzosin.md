---
layout: default
title: Alfuzosin
parent: Model Prediction Only (L5)
nav_order: 220
evidence_level: L5
indication_count: 10
---

# Alfuzosin
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

# Alfuzosin: From Benign Prostatic Hyperplasia to Ambras Type Hypertrichosis Universalis Congenita

## One-Sentence Summary

Alfuzosin is a marketed alpha-1 adrenergic blocker. It acts on prostatic and bladder-neck smooth muscle and is generally used for benign prostatic hyperplasia (BPH) symptoms.
The TxGNN model predicts it may be effective for **Ambras type hypertrichosis universalis congenita**, but there are **0 clinical trials** and **0 publications** supporting this direction. The high score looks like a graph-embedding artifact rather than clinical support.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Evidence Pack (BPH per general drug knowledge) |
| Predicted New Indication | Ambras type hypertrichosis universalis congenita |
| TxGNN Prediction Score | 99.999% (model rank 47) |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 16 authorizations (the ones listed are generic ANDAs) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Based on known information, alfuzosin is a selective (uroselective) alpha-1 adrenergic antagonist. It relaxes smooth muscle in the prostate and bladder neck.

The original and predicted indications have little in common. Ambras syndrome is a rare congenital disorder of hair-follicle development. Alpha-1 signaling has no known role in it, and blockade is not expected to change hair growth.

The near-1.0 score most likely reflects graph proximity to other hair-related disease nodes. The other hair-related predictions (hypertrichosis, hair shaft abnormality, trichomegaly, hypotrichosis) show the same pattern. This prediction is not mechanistically reasonable on current information.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

(The 20 publications retrieved for the rank 3 prediction, a periodontal malformation syndrome, are general periodontitis literature. None mention alfuzosin, so they do not support any indication.)

## US Market Information

The Evidence Pack lists no approved-indication text for any of these products.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA079060 | Alfuzosin Hydrochloride | Tablet, film coated, extended release | Rising Pharma Holdings, Inc. |
| ANDA079057 | Alfuzosin Hydrochloride | Tablet, extended release | Northwind Health Company, LLC |
| ANDA079060 | Alfuzosin Hydrochloride | Tablet, film coated, extended release | Aurobindo Pharma Limited |
| ANDA090284 | Alfuzosin Hydrochloride | Tablet, extended release | Aphena Pharma Solutions - Tennessee, LLC |
| ANDA079057 | Alfuzosin Hydrochloride | Tablet, extended release | Bryant Ranch Prepack |

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found in the Evidence Pack.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is no clinical or literature evidence, and no plausible mechanistic link between alpha-1 blockade and congenital hair-follicle development. The evidence level is L5, so the score reflects model prediction only.

**To proceed, the following is needed:**
- A credible mechanistic hypothesis linking alpha-1 adrenergic signaling to the disease, supported by preclinical data
- Detailed mechanism of action data (MOA) and package insert warnings and contraindications
- Review of the other top-10 predictions for this drug. All are also L5 and lack a plausible mechanism, so none is a strong repurposing candidate on current evidence

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

