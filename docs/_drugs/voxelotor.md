---
layout: default
title: Voxelotor
parent: 僅模型預測 (L5)
nav_order: 1297
evidence_level: L5
indication_count: 7
---

# Voxelotor
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Voxelotor: From Sickle Cell Disease to Hereditary Thrombocytopenia (Low-Confidence Signal)

## One-Sentence Summary

> Voxelotor is a hemoglobin oxygen-affinity modulator originally used for sickle cell disease.
> The TxGNN model predicts a possible link to **Hereditary Thrombocytopenia with Normal Platelets**,
> but this prediction is supported by **0 clinical trials** and **0 publications**, and the drug's own mechanistic rationale explicitly argues against biological plausibility.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (no approved indications on record) |
| Predicted New Indication | Hereditary Thrombocytopenia with Normal Platelets |
| TxGNN Prediction Score | 99.58% |
| Evidence Level | L5 |
| US Market Status | 未上市 (Not marketed in this jurisdiction) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on the repurposing rationale notes accompanying the prediction, voxelotor is known to act as a hemoglobin oxygen-affinity modulator that forms a reversible covalent bond with sickle hemoglobin (HbS), inhibiting its polymerization — its approved target is hemoglobin/erythrocytes, not platelet biology.

The predicted new indication — hereditary thrombocytopenia — involves platelet production or granule function pathways that have no known mechanistic overlap with voxelotor's hemoglobin-targeted action. The evidence pack itself notes that this high TxGNN score likely reflects a co-occurrence bias from graph proximity between "hematologic disease" nodes in the knowledge graph, rather than a genuine mechanistic relationship. All seven predicted indications in this pack (ranks 1–7) share this same limitation: each is a distinct platelet or blood disorder with no plausible link to voxelotor's actual pharmacology, and none carries any supporting clinical or literature evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## US Market Information

Voxelotor is not currently marketed in this jurisdiction (0 licenses on record).

## Safety Considerations

Please refer to the package insert for safety information.

*Note: TFDA label warnings/contraindications and detailed MOA data are flagged as data gaps (DG001: Blocking, DG002: High) in this Evidence Pack and require remediation before any safety evaluation (S1 stage) can proceed.*

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is based solely on TxGNN graph-model output (L5, rank 10,382) with zero supporting clinical trials or literature, and the drug's own mechanistic rationale explicitly states there is no known biological pathway connecting voxelotor's hemoglobin-targeted action to platelet-related disorders. This pattern repeats across all seven ranked candidates in this evidence pack, suggesting the signal reflects knowledge-graph node proximity rather than a genuine repurposing hypothesis.

**To proceed, the following is needed:**
- TFDA label warnings/contraindications (DG001 — blocking, required before any S1 safety review)
- Detailed mechanism of action data from DrugBank (DG002)
- Independent mechanistic or preclinical evidence linking hemoglobin oxygen-affinity modulation to platelet count/function
- If pursued, prioritize indication #5 (thrombocytopenia, broad category) only if a specific safety signal (e.g., post-marketing platelet count changes) can be substantiated — otherwise this candidate list does not warrant further investment at this time
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

