---
layout: default
title: Golodirsen
parent: 僅模型預測 (L5)
nav_order: 759
evidence_level: L5
indication_count: 4
---

# Golodirsen
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Golodirsen: From Duchenne Muscular Dystrophy to Distal Myopathy, Welander Type

## One-Sentence Summary

Golodirsen (DrugBank DB15593) is an antisense oligonucleotide developed for Duchenne Muscular Dystrophy patients amenable to exon 53 skipping. The TxGNN model predicts it may be effective for **Distal Myopathy, Welander Type**, but this prediction is currently supported by **0 clinical trials** and **0 publications**, and is not yet marketed in Taiwan.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Duchenne Muscular Dystrophy (exon 53-skipping amenable) — inferred from mechanistic description in the evidence pack; no formal Taiwan license record exists to confirm |
| Predicted New Indication | Distal Myopathy, Welander Type |
| TxGNN Prediction Score | 99.11% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| US Market Status | Not marketed (未上市) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not formally available in the drug record (flagged as a High-severity data gap, DG002). Based on the mechanistic notes accompanying this candidate, golodirsen is a sequence-specific antisense oligonucleotide that induces exon 53 skipping in the dystrophin gene, and is only effective in patients carrying mutations amenable to that specific exon skip.

Distal Myopathy, Welander Type is caused by mutations in *TIA1* (an RNA-binding protein), a pathway unrelated to dystrophin exon 53 splicing. The evidence pack's own mechanistic assessment concludes that the high TxGNN score most likely reflects graph-level proximity between "muscle disease" nodes in the knowledge graph, rather than a genuine pharmacological or genetic mechanism connecting golodirsen to this disease.

The same pattern holds for the three next-ranked candidates (nebulin-related early-onset distal myopathy, obsolete LGMD type 1C, and X-linked myopathy with postural muscle atrophy — scores 99.07%, 99.04%, and 99.02% respectively): each has a distinct, unrelated genetic etiology (*NEB*, *CAV3*, *VMA21*), and none has any clinical or literature support. Given golodirsen's mutation-specific, sequence-dependent mechanism, mechanistic extrapolation to any of these diseases is not currently supportable.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

Golodirsen has no approved licenses on record in this dataset (0 total licenses, market status: not marketed).

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug interaction data are not yet available — TFDA label data collection is flagged as a Blocking data gap, DG001, required before any safety pre-assessment can proceed.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This candidate rests entirely on a TxGNN similarity score (L5, S0) with no clinical trials, no literature, and no confirmed mechanistic link — the evidence pack's own rationale indicates the target diseases have genetic etiologies distinct from golodirsen's exon-53-specific mechanism, making it unlikely to be a true positive rather than a knowledge-graph artifact.

**To proceed, the following is needed:**
- TFDA/FDA label data (warnings, contraindications) to enable a baseline safety assessment (DG001)
- Confirmed mechanism of action from DrugBank or primary literature (DG002)
- Preclinical or case-level evidence specifically linking golodirsen (or exon-skipping ASOs generally) to *TIA1*-related distal myopathy pathology before any further evaluation of this or the other three ranked candidates
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

