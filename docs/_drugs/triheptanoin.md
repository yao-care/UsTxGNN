---
layout: default
title: Triheptanoin
parent: 僅模型預測 (L5)
nav_order: 1262
evidence_level: L5
indication_count: 10
---

# Triheptanoin
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

# Triheptanoin: Exploratory Signal Toward Tetanic Cataract (Unverified)

## One-Sentence Summary

> Triheptanoin's original indication is not documented in this evidence pack (no Taiwan/US license records exist for this drug). The TxGNN model predicts a possible association with **Tetanic Cataract**, but this is a **pure algorithmic prediction with zero supporting clinical trials or literature**, and the model's own rationale states there is no known mechanistic link.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no license/indication records in evidence pack |
| Predicted New Indication | Tetanic Cataract |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 (model prediction only, no actual studies) |
| US Market Status | Not marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for Triheptanoin, and no original indication information has been provided in this evidence pack either. What is known, per the evidence pack's own `repurposing_rationale`, is that Triheptanoin is an anaplerotic medium-chain triglyceride used to supplement energy metabolism in fatty acid oxidation disorders.

The model's rationale explicitly states there is **no direct mechanistic connection** between this metabolic pathway and lens protein pathology underlying cataract formation. The high TxGNN score likely arises from indirect co-occurrence of metabolic nodes in the knowledge graph rather than a biologically grounded hypothesis — this is described in the evidence pack as "純演算法推論" (pure algorithmic inference).

Notably, 9 of the top 10 predicted indications for this drug are cataract subtypes (tetanic, diabetic, mature, immature, cortical, nuclear senile, senile, craniostenosis) that cluster at nearly identical scores (~99.97–99.98%) and adjacent ranks (1161–1282). This pattern — a single disease cluster dominating the top predictions with no differentiating evidence — is a signature of a generic embedding-space artifact rather than a specific, validated signal. The 10th prediction (antithrombin deficiency type 2) is biologically unrelated to any of the cataract predictions, further suggesting the ranked list reflects proximity in graph embedding space rather than a coherent pharmacological hypothesis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

Triheptanoin has no license records in this evidence pack (`total_licenses: 0`, market status: not marketed). No approved indication text is available for comparison.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: Key warnings, contraindications, and drug-drug interaction data are all flagged as blocking data gaps (DG001) in this evidence pack — TFDA label warnings/contraindications have not yet been retrieved, and no DDI database match was found.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This is an L5-only prediction with no clinical trials, no literature, and no mechanistic plausibility per the model's own rationale — it also sits within a cluster of near-duplicate cataract predictions that suggests a graph-embedding artifact rather than a genuine signal. Combined with a **Blocking** data gap on safety labeling (DG001) and the drug's non-marketed status, there is currently no basis to advance this candidate past S0.

**To proceed, the following is needed:**
- Resolve DG001: retrieve TFDA/FDA label warnings and contraindications (blocking; required before any S1 safety screen)
- Resolve DG002: obtain confirmed mechanism of action data from DrugBank/primary literature
- Independent mechanistic or preclinical rationale connecting anaplerotic fatty acid metabolism to cataract pathophysiology (currently absent)
- At minimum one preclinical or observational study before considering re-scoring above L5
- Re-evaluate whether the cataract cluster (ranks 1–9) reflects a true shared signal or a single embedding artifact before treating any individual cataract subtype as a distinct hypothesis
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

