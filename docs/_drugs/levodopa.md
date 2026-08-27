---
layout: default
title: Levodopa
parent: 僅模型預測 (L5)
nav_order: 854
evidence_level: L5
indication_count: 1
---

# Levodopa
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

# Levodopa: From Parkinson's Disease to Rasmussen Subacute Encephalitis

## One-Sentence Summary

Levodopa is a dopamine precursor originally established for treating dopamine-deficiency conditions such as Parkinson's disease. The TxGNN model predicts it may be effective for **Rasmussen Subacute Encephalitis**, but this prediction is currently supported by **0 clinical trials** and **0 publications** — the evidence base consists solely of the model's topological score, and the accompanying mechanistic review flags this as a likely false-positive prediction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Parkinson's disease / dopa-responsive dystonia (established clinical use per mechanistic rationale below; not sourced from Taiwan license data, as none exists) |
| Predicted New Indication | Rasmussen Subacute Encephalitis |
| TxGNN Prediction Score | 99.06% (model rank 20,416) |
| Evidence Level | L5 (model prediction only — no clinical or literature support) |
| Market Status (Taiwan) | Not marketed |
| Number of Licenses (Taiwan) | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for this candidate is not currently available (data gap). Based on known pharmacology, Levodopa is a dopamine precursor that is converted to dopamine by dopa decarboxylase; its only well-established clinical role is replacing nigrostriatal dopamine deficiency, as in Parkinson's disease and certain dopa-responsive dystonias.

Rasmussen encephalitis, by contrast, is a rare, chronic, unilateral inflammatory disease of the cerebral cortex in children, driven by T-cell-mediated autoimmune attack (involving anti-GluR3 and related glutamate-receptor antibodies and cytotoxic T-lymphocyte infiltration). It has no known nigrostriatal degeneration component and no established relationship to dopaminergic pathways.

No pharmacological literature currently links dopamine replacement therapy to the inflammatory/autoimmune mechanisms underlying Rasmussen encephalitis. The high TxGNN score most likely reflects topological proximity between Levodopa and "encephalitis/neurodegeneration"-type disease nodes in the knowledge graph (e.g., via shared neighbor nodes such as "central nervous system disease" or "epilepsy") rather than a genuine biological mechanism. This prediction should be treated as a **potential false positive** with low mechanistic plausibility.

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
This candidate has no supporting clinical trials or literature (Evidence Level L5, model prediction only), and the model's own mechanistic review assesses the biological link between dopamine replacement and Rasmussen encephalitis's autoimmune/inflammatory pathology as implausible — consistent with a topological false positive rather than a genuine repurposing signal.

**To proceed, the following is needed:**
- TFDA-approved label warnings/contraindications (currently blocking — data gap DG001)
- Confirmed mechanism-of-action data via DrugBank (data gap DG002)
- Preclinical or mechanistic studies establishing any plausible link between dopaminergic signaling and Rasmussen encephalitis's T-cell-mediated autoimmune process
- At minimum, case-report or observational evidence in Rasmussen encephalitis before this candidate can advance beyond S0
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

