---
layout: default
title: Alfuzosin
parent: 僅模型預測 (L5)
nav_order: 220
evidence_level: L5
indication_count: 10
---

# Alfuzosin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# ALFUZOSIN: From Benign Prostatic Hyperplasia to Ambras Type Hypertrichosis Universalis Congenita

## One-Sentence Summary

Alfuzosin is a selective alpha-1 adrenergic receptor antagonist primarily used to relieve the urinary symptoms of benign prostatic hyperplasia (BPH).
The TxGNN model predicts it may be effective for **Ambras Type Hypertrichosis Universalis Congenita** with a prediction score of **99.999%**,
however there are currently **no clinical trials** and **no publications** supporting this direction — this is a model-inference-only finding.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Benign Prostatic Hyperplasia (BPH) / Lower Urinary Tract Symptoms (LUTS) |
| Predicted New Indication | Ambras Type Hypertrichosis Universalis Congenita |
| TxGNN Prediction Score | 99.999% |
| Evidence Level | L5 |
| US Market Status | Not marketed (no license records found in dataset) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known pharmacological information, alfuzosin is a selective alpha-1 adrenergic receptor antagonist. It works by blocking alpha-1 receptors in the smooth muscle of the prostate and bladder neck, thereby relieving urinary outflow obstruction in BPH. Alpha-1 receptors are also present in other tissues including dermal arrector pili muscles, vascular smooth muscle, and the central nervous system.

Ambras syndrome (hypertrichosis universalis congenita of the Ambras type) is a genetic disorder caused by pericentromeric structural rearrangements of chromosome 8, leading to constitutive overexpression of genes that drive generalized excessive hair growth. The disease mechanism is structural and genomic, not receptor-mediated. While alpha-1 receptors are present in arrector pili muscles — which control hair follicle orientation — antagonizing these receptors has no known capacity to correct or reverse a chromosomal gene-dosage defect driving hair overgrowth.

The high TxGNN prediction score most likely reflects graph network neighborhood similarity: in the TxGNN knowledge graph, alfuzosin's node may cluster near dermatological disease nodes due to indirect biological associations, rather than a direct pharmacological mechanism. This is explicitly a model inference artifact, not a mechanistic prediction. The mechanistic link is considered weak, and no translational pathway from alpha-1 blockade to treatment of Ambras syndrome has been described in the literature.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All ten predicted indications for alfuzosin are rated L5 (model prediction only) with no supporting clinical trials or directly relevant publications. For the top-ranked indication, Ambras syndrome, the underlying disease is caused by a chromosomal structural defect, and there is no established mechanism by which alpha-1 receptor blockade could address this pathology.

**To proceed, the following is needed:**
- Detailed MOA data from DrugBank to confirm the receptor pharmacology profile (currently a High-severity data gap)
- FDA package insert warnings and contraindications (currently a Blocking data gap — required before any safety assessment)
- Drug-drug interaction data (currently not found in the database)
- Verification of US FDA market status — alfuzosin (UroXatral®) is known to have received FDA approval for BPH, but this pipeline recorded 0 licenses, suggesting a data ingestion gap that should be resolved
- Pre-clinical mechanistic evidence that alpha-1 receptor blockade has any biologically plausible effect on hair follicle biology in genetically driven hypertrichosis before this line of research is reconsidered
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

