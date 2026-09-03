---
layout: default
title: Orlistat
parent: 僅模型預測 (L5)
nav_order: 996
evidence_level: L5
indication_count: 1
---

# Orlistat
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

# Orlistat: From Obesity Management to Hypervitaminosis

## One-Sentence Summary

> Orlistat is a pancreatic lipase inhibitor originally used for weight management, working by blocking dietary fat absorption in the gut.
> The TxGNN model predicts a mechanistic association with **Hypervitaminosis** (fat-soluble vitamin excess),
> but this is currently based on **model prediction alone**, with no supporting clinical trials or literature identified in this evidence pack.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (no data provided) |
| Predicted New Indication | Hypervitaminosis |
| TxGNN Prediction Score | 99.42% |
| Evidence Level | L5 |
| US Market Status | Not marketed (未上市) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not directly available in this evidence pack (marked as a data gap), but the repurposing rationale supplied alongside the prediction describes orlistat as a **pancreatic lipase inhibitor** that blocks intestinal hydrolysis and absorption of dietary fat.

The proposed link to hypervitaminosis is unusual in direction: orlistat's well-documented side effect is *malabsorption/deficiency* of fat-soluble vitamins (A, D, E, K), not excess. The rationale itself frames this as a hypothesis derived by reversing a known adverse-effect pathway — if blocking fat absorption reduces fat-soluble vitamin uptake, it could theoretically be relevant to conditions of vitamin **excess** rather than deficiency. This is explicitly noted as **not the original design intent** of the drug, and the high TxGNN score likely reflects the model detecting the existing orlistat–fat-soluble-vitamin pharmacological connection in the knowledge graph, rather than an independent, validated new mechanism.

Given the inverted logic (deficiency-causing drug proposed for an excess condition) and the complete absence of clinical trial or literature evidence, the mechanistic plausibility should be treated as speculative pending expert pharmacological review.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## US Market Information

No licenses on file — the drug is currently not marketed (未上市) with 0 registered authorizations.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: TFDA label warnings/contraindications and drug interaction data are marked as blocking data gaps in this evidence pack and could not be included.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests solely on a TxGNN model score (L5, no clinical trials or literature), the drug is not currently marketed in this jurisdiction, and the mechanistic rationale is a speculative reversal of a known adverse effect rather than an established or plausible therapeutic pathway.

**To proceed, the following is needed:**
- TFDA label warnings/contraindications (blocking data gap — required before any S1 safety review)
- Verified mechanism of action (MOA) documentation from DrugBank
- Independent pharmacological/expert review of the deficiency-vs-excess mechanistic logic before pursuing further evidence collection
- Literature or preclinical search specifically targeting orlistat and fat-soluble vitamin excess conditions
- Confirmation of original approved indication(s), currently missing from this evidence pack
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

