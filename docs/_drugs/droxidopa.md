---
layout: default
title: Droxidopa
parent: 僅模型預測 (L5)
nav_order: 631
evidence_level: L5
indication_count: 1
---

# Droxidopa
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

# Droxidopa: From Neurogenic Orthostatic Hypotension to Variably Protease-Sensitive Prionopathy

## One-Sentence Summary

Droxidopa is a synthetic amino acid precursor known pharmacologically to be converted into norepinephrine, with clinical use in neurogenic orthostatic hypotension (official original-indication data is not available in this Evidence Pack). The TxGNN model predicts it may be effective for **Variably Protease-Sensitive Prionopathy (VPSPr)**, but this prediction is currently supported by **0 clinical trials** and **0 publications** — it is a model-score-only signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Neurogenic orthostatic hypotension (based on known pharmacology only; TFDA-approved indication text unavailable — drug is not marketed in Taiwan) |
| Predicted New Indication | Variably Protease-Sensitive Prionopathy |
| TxGNN Prediction Score | 99.33% |
| Evidence Level | L5 |
| US Market Status | Not Marketed (未上市) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, droxidopa is a synthetic amino acid precursor that is converted by DOPA decarboxylase into norepinephrine, and its clinical use has centered on neurogenic orthostatic hypotension, an autonomic/neurovascular condition.

VPSPr is a rare, atypical prion disease characterized by variable protease-sensitivity of misfolded prion protein and progressive neurodegeneration. There is no established or biologically inferable mechanistic link between norepinephrine-precursor pharmacology and prion protein misfolding pathology.

The evidence pack's own rationale flags this explicitly: the high TxGNN score (0.993) most likely reflects a **topological artifact** in the knowledge graph — droxidopa and VPSPr may simply share proximity to "neurodegenerative disease" nodes — rather than genuine pharmacological plausibility. With no original-indication data, no MOA data, no trials, and no literature available to cross-validate, this mechanistic link should be treated as speculative and low-confidence.

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
This candidate rests entirely on a single TxGNN model score with no clinical trial, literature, original-indication, or MOA data to corroborate it. The evidence pack itself assesses the mechanistic link as likely a graph-topology artifact rather than a pharmacologically plausible signal, so it does not meet the bar to advance.

**To proceed, the following is needed:**
- Confirmed original indication and detailed mechanism of action (MOA) for droxidopa
- TFDA/original-market label warnings and contraindications (currently a Blocking data gap for safety screening)
- Independent preclinical or mechanistic evidence linking noradrenergic pathways to prion protein pathology, before any trial or literature search is expected to be productive
- Re-evaluation of the TxGNN graph signal to rule out topological bias before further investment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

