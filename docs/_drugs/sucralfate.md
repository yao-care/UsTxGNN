---
layout: default
title: Sucralfate
parent: 僅模型預測 (L5)
nav_order: 1184
evidence_level: L5
indication_count: 2
---

# Sucralfate
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Sucralfate: From Duodenal Ulcer to Duodenogastric Reflux

## One-Sentence Summary

> Sucralfate is a mucosal-protective agent classically used for **duodenal ulcer** treatment.
> The TxGNN model predicts it may be effective for **Duodenogastric Reflux**,
> but currently **no clinical trials and no literature** support this direction — the signal comes from the prediction model alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Duodenal ulcer (mucosal protectant) — not captured in local license data; drug is not currently marketed in Taiwan |
| Predicted New Indication | Duodenogastric Reflux |
| TxGNN Prediction Score | 99.37% |
| Evidence Level | L5 |
| Taiwan Market Status | ✗ Not Marketed |
| Number of Licenses | 0 |
| Recommended Decision | Hold |

*A second candidate, duodenal obstruction, scored nearly as high (99.30%, rank 15586) with the same lack of clinical/literature support.*

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for this candidate is not available in the current evidence pack (flagged as a High-severity data gap requiring a DrugBank API lookup). Based on generally known pharmacology, sucralfate is an aluminum sucrose octasulfate complex that, under acidic gastric/duodenal conditions, polymerizes and binds to proteinaceous exudate at sites of mucosal injury, forming a protective barrier. Its established efficacy in duodenal ulcer relies on this local, non-systemic cytoprotective action rather than acid suppression.

Duodenogastric reflux involves exposure of the gastric mucosa to duodenal contents (bile acids, pancreatic enzymes), which can injure the mucosal lining in a manner mechanistically similar to peptic ulceration. The anatomical overlap (duodenum/stomach) and the shared theme of "mucosal barrier disruption" make it plausible that a barrier-forming agent effective in duodenal ulcer could also reduce mucosal injury from duodenogastric reflux. The second predicted indication, duodenal obstruction, sits in the same anatomical region and reinforces that the model is detecting a duodenum-centric signal rather than an isolated association — but this remains a mechanistic hypothesis, not a validated one.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Taiwan Market Information

This drug is currently **not marketed in Taiwan** (0 licenses on record), so no local approved-indication text or authorization numbers are available to compare against the predicted indication.

---

## Safety Considerations

Please refer to the package insert for safety information. Note: TFDA label warnings and contraindications for this drug are a flagged **Blocking** data gap (DG001) — this must be resolved before any safety evaluation (S1 stage) can proceed. No drug-drug interaction records were found in the queried database.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the TxGNN model score (L5 evidence) with zero clinical trials or literature, and the drug is not currently marketed in Taiwan. Combined with a Blocking-severity gap on label warnings/contraindications, there is not enough evidence to proceed even under guardrails.

**To proceed, the following is needed:**
- TFDA label warnings and contraindications (DG001, blocking — resolve first)
- Confirmed mechanism of action via DrugBank API (DG002)
- Targeted literature/clinical trial search for sucralfate in duodenogastric reflux and duodenal obstruction
- Since the drug has no existing Taiwan license, a regulatory pathway assessment for introducing/repurposing it locally
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

