---
layout: default
title: Finasteride
parent: 僅模型預測 (L5)
nav_order: 708
evidence_level: L5
indication_count: 6
---

# Finasteride
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Finasteride: From an Undocumented Original Indication to Ambras Type Hypertrichosis Universalis Congenita

## One-Sentence Summary

Finasteride's original approved indication is not documented in the current evidence pack (mechanism of action and original indication are both flagged as data gaps). The TxGNN model's top-ranked prediction links Finasteride to **Ambras Type Hypertrichosis Universalis Congenita**, but this association is currently supported by **0 clinical trials** and **0 publications**, and the mechanistic review flags it as a likely knowledge-graph false positive rather than a biologically grounded signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in available data |
| Predicted New Indication | Ambras type hypertrichosis universalis congenita |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| US Market Status | Not marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for Finasteride in this evidence pack, and its original approved indication is likewise undocumented. What is known generally is that Finasteride's pharmacology centers on inhibition of type II 5α-reductase, reducing conversion of testosterone to dihydrotestosterone (DHT).

Ambras type hypertrichosis universalis congenita is a rare congenital disorder of generalized excess hair growth, mechanistically linked to genetic rearrangements on chromosome 8q. Critically, this condition is classified as **non-androgen-dependent** — its hair-growth pathway does not rely on DHT signaling, which is the pathway Finasteride modulates.

Given this, the mechanistic review for this specific candidate concludes that the link is not biologically well-supported: the TxGNN score of 0.9999 most likely reflects graph-embedding similarity between hair-related disease nodes rather than a genuine pharmacological relationship. No clinical trial or literature evidence has been identified to counter this concern, which is why the evidence level is scored L5 (model prediction only) and the recommendation is **Hold**.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This prediction has zero supporting clinical trials and zero supporting publications (L5, model-prediction-only), and the underlying disease mechanism (non-androgen-dependent hypertrichosis) does not align well with Finasteride's 5α-reductase/DHT mechanism. The evidence review itself flags the TxGNN score as a likely embedding-similarity artifact rather than a genuine signal.

**To proceed, the following is needed:**
- Original approved indication and mechanism of action (MOA) data for Finasteride (currently missing — DG002, High severity)
- FDA label warnings/contraindications (currently missing — DG001, Blocking; required before any safety pre-screening can proceed)
- Independent pharmacological review confirming whether any androgen-dependent subtype of hypertrichosis could plausibly respond to 5α-reductase inhibition
- If further repurposing work on the hair-growth axis is desired, note that a separate TxGNN candidate — **hypertrichosis (disease)** (rank 2, score 99.99%, evidence level L4) — has some supporting literature and one related clinical trial, and may warrant its own dedicated evaluation rather than pursuing the Ambras syndrome candidate further
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

