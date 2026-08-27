---
layout: default
title: Methylphenidate
parent: 僅模型預測 (L5)
nav_order: 915
evidence_level: L5
indication_count: 4
---

# Methylphenidate
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

# Methylphenidate: From ADHD to Faciodigitogenital Syndrome

## One-Sentence Summary

Methylphenidate is a dopamine/norepinephrine reuptake inhibitor widely known as a stimulant used for ADHD, though this evidence pack contains no formal license or indication record for it. The TxGNN model's top-ranked prediction is **Faciodigitogenital Syndrome** (Aarskog syndrome, an X-linked congenital developmental disorder), but this prediction is currently supported by **0 clinical trials** and **0 publications** — it is a pure knowledge-graph link with no mechanistic or empirical backing.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available from license data (0 licenses on file); methylphenidate is generally known as an ADHD stimulant, but original indication/MOA data for this pack is a data gap |
| Predicted New Indication | Faciodigitogenital Syndrome (Aarskog syndrome) |
| TxGNN Prediction Score | 99.998% |
| Evidence Level | L5 |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (data gap). Based on general knowledge, methylphenidate is a central nervous system stimulant that inhibits dopamine and norepinephrine reuptake, and it is best known as a treatment for ADHD.

Faciodigitogenital syndrome (Aarskog syndrome) is an X-linked genetic developmental disorder affecting facial, digital, and genital morphology, caused by mutations unrelated to catecholaminergic signaling. There is no known pathophysiological overlap between a monoamine reuptake inhibitor and a structural/genetic developmental syndrome.

The evidence pack itself states this directly: the mechanistic link is unverifiable, and the high TxGNN score (rank 147 of the model's overall output) reflects only a graph-embedding association, not any clinical or biological plausibility. This candidate should be treated as a low-confidence model artifact rather than a genuine repurposing hypothesis.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## US Market Information

No marketing authorization records are on file for this drug in this dataset (0 licenses, market status: Not Marketed).

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction carries the highest TxGNN score among this drug's candidates but has zero supporting clinical trials or literature and no plausible mechanistic connection between methylphenidate's catecholaminergic action and a genetic developmental syndrome. This is a model-only (L5) signal and does not meet the threshold to advance.

**To proceed, the following is needed:**
- TFDA label warnings/contraindications data (currently blocking — DG001)
- Confirmed mechanism of action (MOA) data from DrugBank (DG002)
- Any preclinical or case-level evidence specifically linking methylphenidate to Aarskog syndrome, before further evaluation is warranted
- Note: this drug's rank-3 candidate ("specific developmental disorder," L2/S2, Proceed with Guardrails) has substantially stronger clinical and literature support and may warrant a separate, higher-priority evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

