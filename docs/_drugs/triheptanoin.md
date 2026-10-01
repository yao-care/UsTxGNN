---
layout: default
title: Triheptanoin
parent: Model Prediction Only (L5)
nav_order: 1262
evidence_level: L5
indication_count: 10
---

# Triheptanoin
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

# Triheptanoin: From an Anaplerotic Metabolic Therapy to Tetanic Cataract

## One-Sentence Summary

Triheptanoin is an odd-chain triglyceride sold in the US as DOJOLVI, a metabolic energy-substrate therapy.
The TxGNN model predicts it may be effective for **tetanic cataract**, and for several other cataract subtypes with the same score.
There are **0 clinical trials** and **0 publications** supporting this prediction, so it rests on the model alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not provided in the supplied regulatory data |
| Predicted New Indication | Tetanic cataract |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the supplied data. Triheptanoin is an anaplerotic odd-chain triglyceride that supplies propionyl-CoA and succinyl-CoA to the TCA cycle. It is marketed as DOJOLVI by Ultragenyx. The approved indication text is empty in the data. From general knowledge outside the Evidence Pack, DOJOLVI is labeled for long-chain fatty acid oxidation disorders, but this should be confirmed against the label.

The link to tetanic cataract, a lens opacity associated with hypocalcemia, is speculative. A metabolic substrate could in theory affect lens energy metabolism, but no data support this. The top 5 predictions (tetanic, type 2 diabetes–associated, mature, craniostenosis and immature cataract) share an identical score of 0.99975. This suggests the signal comes from a shared knowledge-graph neighborhood rather than a disease-specific association.

Other predicted indications fall into two groups:
- **Other cataract subtypes:** diabetic, cortical, nuclear senile and senile cataract score 99.97%. None has supporting trials or literature.
- **Antithrombin deficiency type 2:** a hereditary coagulation disorder (score 99.97%) with no apparent biological link to triheptanoin.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA213687 | DOJOLVI (Ultragenyx Pharmaceutical Inc.) | Liquid | Not stated in the supplied data |

---

## Safety Considerations

Please refer to the package insert for safety information. The DDI query returned no interactions, and warning and contraindication data were not available.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical or preclinical support (L5, stage S0). The tied scores across the cataract subtypes point to a graph-level artifact rather than a disease-specific signal. Safety data are also missing, which blocks safety screening.

**To proceed, the following is needed:**
- The FDA package insert (warnings, contraindications, approved indication), which is currently a blocking gap
- Mechanism of action data from DrugBank
- Preclinical evidence on lens metabolism or cataract models
- A route and formulation compatibility assessment for any ocular use
- A literature and trial search outside the current dataset
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

