---
layout: default
title: Turpentine
parent: 僅模型預測 (L5)
nav_order: 1272
evidence_level: L5
indication_count: 1
---

# Turpentine
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

# Turpentine: From No Approved Indication to Multiple Endocrine Neoplasia

## One-Sentence Summary

> Turpentine is not an approved pharmaceutical product in Taiwan — it has historically been used only as a veterinary topical counterirritant and industrial solvent, with no established human indication.
> The TxGNN model predicts a possible association with **Multiple Endocrine Neoplasia**,
> but this prediction is currently supported by **0 clinical trials** and **0 publications**, and is not accompanied by any known mechanistic rationale.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | None approved — historically used as a veterinary topical anti-inflammatory/irritant and industrial solvent |
| Predicted New Indication | Multiple Endocrine Neoplasia |
| TxGNN Prediction Score | 99.60% |
| Evidence Level | L5 |
| US Market Status | Not marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, turpentine (a terpene mixture derived from pine resin) has no established human pharmacological indication and is not recorded in DrugBank with a defined MOA or drug target.

The TxGNN prediction for this candidate scored very high (0.996), but this score reflects statistical node-embedding similarity within the knowledge graph rather than any interpretable biological pathway. There is no known link between turpentine's chemical activity and the pathogenic mechanisms of multiple endocrine neoplasia (e.g., RET or MEN1 mutation pathways).

Given that turpentine has no history of systemic pharmacological use in humans and lacks any documented target relevant to endocrine tumorigenesis, the biological plausibility of this prediction is low. The high TxGNN score should be treated as a hypothesis-generating signal only, not as evidence of therapeutic relevance.

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
The prediction is based purely on TxGNN model output (Evidence Level L5) with no supporting clinical trials, literature, or plausible mechanistic link. Turpentine also has no approved human indication and no TFDA licensing in Taiwan, so there is no regulatory or clinical foundation to build on.

**To proceed, the following is needed:**
- TFDA-equivalent safety data (warnings/contraindications) — currently a **blocking data gap** preventing any S1 safety review
- Documented mechanism of action (MOA) data from DrugBank or primary literature
- Preclinical or mechanistic studies linking turpentine's chemical activity to endocrine tumor pathways
- At minimum, exploratory (non-clinical) evidence before considering any further evaluation stage
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

