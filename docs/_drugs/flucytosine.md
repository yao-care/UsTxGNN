---
layout: default
title: Flucytosine
parent: 僅模型預測 (L5)
nav_order: 714
evidence_level: L5
indication_count: 1
---

# Flucytosine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Flucytosine: From Fungal Infection to Bone Paget Disease

## One-Sentence Summary

> Flucytosine (5-FC) is a systemic antifungal agent whose original indication data is not included in this evidence pack.
> The TxGNN model predicts it may be effective for **Bone Paget Disease**,
> but currently **0 clinical trials** and **0 publications** support this direction — the prediction rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in evidence pack (no licenses or indication text provided) |
| Predicted New Indication | Bone Paget Disease |
| TxGNN Prediction Score | 99.04% |
| Evidence Level | L5 |
| US Market Status | 未上市 (Not marketed) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack (`original_moa` is flagged as a data gap). Based on general pharmacological knowledge, Flucytosine (5-FC) is a cytosine nucleoside analogue that is selectively converted by fungal (and some bacterial) cytosine deaminase into 5-fluorouracil (5-FU), which then inhibits thymidylate synthase and disrupts nucleic acid synthesis. Its clinical selectivity depends on human cells largely lacking this conversion enzyme.

Bone Paget disease, by contrast, is a disorder of excessive osteoclast activity and disordered bone remodeling. Standard treatments (bisphosphonates, calcitonin) act on osteoclast-mediated bone resorption pathways, which have no established mechanistic overlap with the antifungal/antimetabolite pathway of 5-FC/5-FU.

Given the absence of original MOA documentation and the lack of any supporting trials or literature, this prediction cannot currently be validated on mechanistic grounds. The high TxGNN score (99.04%) likely reflects an indirect knowledge-graph connection (e.g., a drug–gene–disease path) rather than a direct causal mechanism, and would require manual review of the underlying knowledge-graph path before further credence can be given to it.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## US Market Information

No licenses are currently on record for this drug in the evidence pack (market status: 未上市 / Not marketed; total licenses: 0).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is based solely on the TxGNN model score (L5 evidence level), with no supporting clinical trials, literature, or established mechanistic link between Flucytosine's antifungal activity and Paget's disease pathophysiology. There is insufficient evidence to advance this candidate at this time.

**To proceed, the following is needed:**
- Manual review of the underlying knowledge-graph path that produced this prediction, to determine whether an indirect biological rationale exists
- Original mechanism of action (MOA) documentation for Flucytosine
- Original indication and regulatory licensing data (currently absent from the evidence pack)
- TFDA label warnings/contraindications (currently blocking safety review per DG001)
- Any preclinical or in vitro data exploring 5-FC/5-FU activity in bone remodeling or osteoclast biology, should such data emerge
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

