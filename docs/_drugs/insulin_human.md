---
layout: default
title: Insulin Human
parent: 僅模型預測 (L5)
nav_order: 801
evidence_level: L5
indication_count: 10
---

# Insulin Human
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

# Insulin Human: From Diabetes Mellitus to Autoimmune Oophoritis

## One-Sentence Summary

Insulin human is the endogenous-identical hormone used as replacement therapy for diabetes mellitus. The TxGNN model predicts it may be effective for **Autoimmune Oophoritis**, but this direction is currently supported by **0 clinical trials** and **0 publications**, and the model's own rationale flags the score as a likely graph-connectivity artifact rather than a genuine mechanistic signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Diabetes Mellitus (general pharmacological knowledge; no Taiwan-specific label text available — drug is not currently marketed in Taiwan) |
| Predicted New Indication | Autoimmune Oophoritis |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L5 |
| Market Status (Taiwan) | ✗ Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this evidence pack (flagged as a High-severity data gap). Insulin human's established pharmacology is receptor-mediated glucose uptake and metabolic regulation via the insulin receptor — it has no known direct immunomodulatory action on ovarian tissue.

The model's own repurposing rationale is explicit that there is **no direct mechanistic link** between insulin and autoimmune oophoritis. Diabetes and premature ovarian failure can co-occur within autoimmune polyglandular syndrome (APS-2/APS-3), but this reflects shared autoimmune susceptibility across endocrine organs — not a causal pathway through which insulin treats ovarian autoimmunity. The evidence pack notes that insulin's very high connectivity within the knowledge graph (it links to a large number of endocrine/metabolic disease nodes) may itself be inflating the TxGNN score, independent of true biological relevance.

Given the absence of any supporting clinical trials, literature, or a plausible causal mechanism, this prediction should be treated as a graph-driven hypothesis rather than a clinically grounded repurposing candidate.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

Insulin human is currently **not marketed in Taiwan** (0 licenses on file; `taiwan_regulatory.market_status` = 未上市). No authorization records are available to summarize.

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug interaction data are not currently available for this candidate — TFDA label retrieval is flagged as a Blocking data gap that must be resolved before any safety-stage evaluation.)

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction carries a high TxGNN score but is unsupported by any clinical trial or literature evidence (Evidence Level L5), and the model's own rationale identifies the association as likely reflecting graph connectivity rather than a real mechanistic pathway between insulin and autoimmune oophoritis.

**To proceed, the following is needed:**
- TFDA label / warnings and contraindications data (currently a Blocking gap)
- Verified mechanism of action data for insulin human (currently a High-severity gap)
- Preclinical or mechanistic evidence specifically linking insulin signaling to ovarian autoimmune pathophysiology
- Any case reports, observational data, or trials directly studying insulin (or related endocrine replacement) in autoimmune oophoritis populations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

