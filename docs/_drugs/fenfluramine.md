---
layout: default
title: Fenfluramine
parent: 僅模型預測 (L5)
nav_order: 698
evidence_level: L5
indication_count: 4
---

# Fenfluramine
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

# Fenfluramine: From Epilepsy Syndromes to Proximal 16p11.2 Microdeletion Syndrome

## One-Sentence Summary

Fenfluramine is a serotonin-releasing/5-HT2C agonist agent whose established use is in severe epilepsy syndromes (Dravet syndrome, Lennox-Gastaut syndrome); it is **not marketed** under the regulatory data in this evidence pack. The TxGNN model predicts a possible link to **proximal 16p11.2 microdeletion syndrome**, but this prediction is supported by **zero clinical trials and zero publications** — it is a model-score-only signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not formally recorded in this evidence pack (no license data); background text indicates use in Dravet syndrome and Lennox-Gastaut syndrome |
| Predicted New Indication | Proximal 16p11.2 microdeletion syndrome |
| TxGNN Prediction Score | 99.93% (rank 2543 among all candidates) |
| Evidence Level | L5 |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data from DrugBank is flagged as a data gap in this evidence pack. Based on the available rationale text, fenfluramine is known as a serotonin-releasing agent / 5-HT2C receptor agonist, pharmacologically established for seizure control in Dravet syndrome and Lennox-Gastaut syndrome.

Proximal 16p11.2 microdeletion syndrome is a copy-number-variant genomic disorder whose clinical presentation can include obesity, autism-spectrum features, and (in some patients) seizures. The overlap with fenfluramine's known pharmacology appears to be indirect — likely mediated through shared graph nodes such as "obesity" (fenfluramine's historical appetite-suppressant use) or "seizure" — rather than a mechanism that addresses the syndrome's underlying genetic cause.

Given this, the high TxGNN score most likely reflects graph-distance proximity through these intermediate nodes rather than a direct causal pathway. The mid-tier overall rank (2543) relative to the score's near-ceiling value further suggests limited specificity for this particular disease-drug pair.

It is also worth noting that the other top-ranked predictions for this drug in the current evidence pack (hypervitaminosis, obsolete hypertelorism, frontorhiny) are explicitly flagged in their own rationale text as mechanistically implausible or likely graph noise — this pattern raises the bar for what independent evidence would be needed before treating the 16p11.2 prediction as more than a hypothesis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

Fenfluramine is not marketed under the regulatory data available (0 licenses on record); no authorization or product information is available to summarize.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests entirely on a TxGNN model score (L5) with no corroborating clinical trials or literature, and the proposed mechanistic link is indirect (via shared graph nodes rather than a disease-specific pathway). Combined with a Blocking data gap on TFDA safety labeling, this candidate does not meet the threshold to advance past S0.

**To proceed, the following is needed:**
- TFDA package insert warnings/contraindications (DG001, Blocking) — required before any S1 safety screening
- Confirmed mechanism-of-action data from DrugBank (DG002, High)
- Independent literature/mechanistic search specifically on serotonergic agents in 16p11.2 microdeletion syndrome (obesity or seizure sub-phenotypes)
- Formal confirmation of fenfluramine's original approved indication(s) and licensing status, currently absent from this evidence pack
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

