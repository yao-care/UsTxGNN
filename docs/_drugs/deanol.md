---
layout: default
title: Deanol
parent: 僅模型預測 (L5)
nav_order: 575
evidence_level: L5
indication_count: 1
---

# Deanol
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

# DEANOL: From Choline Precursor to Insomnia

## One-Sentence Summary

DEANOL (2-dimethylaminoethanol, DMAE) is an endogenous choline precursor with historical use as a nootropic supplement, but holds no formal regulatory approval on record.
The TxGNN model predicts it may be effective for **Insomnia**, achieving a high prediction score of **99.87%**;
however, **no clinical trials or published literature** currently support this repurposing direction, placing the evidence at the lowest possible level (L5).

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not established (no regulatory approval on record) |
| Predicted New Indication | Insomnia |
| TxGNN Prediction Score | 99.87% |
| Evidence Level | L5 |
| Market Status | ✗ Not marketed |
| Number of Approvals | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

DEANOL (2-dimethylaminoethanol, DMAE) is an endogenous compound and a known biosynthetic precursor to choline and, ultimately, acetylcholine (ACh). The cholinergic system plays a well-established role in regulating REM sleep — including the initiation of ponto-geniculo-occipital (PGO) waves and rapid eye movement activity. This mechanistic proximity between the cholinergic pathway and sleep regulation is the theoretical basis upon which TxGNN links DEANOL to insomnia.

However, this mechanistic bridge faces serious practical limitations. First, DMAE's blood-brain barrier penetration is limited and its in vivo conversion efficiency to ACh in the human central nervous system is very low, undermining its pharmacological relevance as a sleep modulator. Second, and more critically, clinical observations suggest that DMAE may actually worsen sleep onset — rather than improve it — due to its mild CNS stimulant properties. There are currently no polysomnography (PSG) data from human or animal studies that support a beneficial effect on insomnia.

The high TxGNN score (0.9987) most likely reflects the topological proximity between cholinergic nodes and sleep-related nodes in the knowledge graph, rather than indication-specific mechanistic or clinical evidence. This is a case where graph-based prediction outpaces empirical validation — the predicted association is structurally plausible but pharmacologically questionable.

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
There is no clinical trial or published literature evidence supporting DEANOL for insomnia, and its known pharmacological characteristics — mild CNS stimulation and poor central ACh conversion — suggest it may be mechanistically counterproductive for this indication.

**To proceed, the following is needed:**
- Mechanism of action (MOA) data, particularly CNS penetration studies and quantified in vivo ACh conversion efficiency
- Polysomnography (PSG) studies in animal models to objectively characterize any effect on sleep architecture
- Full safety profile: package insert warnings, contraindications, and drug interaction screening
- Regulatory status assessment in major markets (US FDA, EMA) to clarify whether any prior approvals exist under other indications
- Evaluation of whether any CNS-targeting formulation (e.g., lipophilic prodrug) could overcome the blood-brain barrier limitation before revisiting this prediction
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

