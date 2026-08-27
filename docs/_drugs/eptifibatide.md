---
layout: default
title: Eptifibatide
parent: 僅模型預測 (L5)
nav_order: 663
evidence_level: L5
indication_count: 10
---

# Eptifibatide
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

# Eptifibatide: From Acute Coronary Syndrome to Rheumatoid Arthritis

## One-Sentence Summary

Eptifibatide is a GPIIb/IIIa (integrin αIIbβ3) platelet aggregation inhibitor, historically used in acute coronary syndromes and percutaneous coronary intervention. The TxGNN model predicts it may be effective for **Rheumatoid Arthritis**, but this direction currently has **0 clinical trials** and **0 publications** supporting it — it is a model-score-only prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acute coronary syndrome (ACS) / unstable angina — inferred from supporting literature in this evidence pack; no formal license record exists because the drug is not marketed in this jurisdiction |
| Predicted New Indication | Rheumatoid Arthritis |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| US Market Status | ✗ Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Eptifibatide is a reversible GPIIb/IIIa (integrin αIIbβ3) antagonist that inhibits platelet aggregation. Literature in this evidence pack (e.g., PMID 17916103) describes it as "an effective treatment for patients with acute coronary syndromes (ACS)," consistent with its known antiplatelet role in cardiovascular disease.

Rheumatoid arthritis, however, is primarily an autoimmune/inflammatory synovitis-driven disease. Per the evidence pack's own mechanistic assessment, RA pathology has no clear, direct link to platelet GPIIb/IIIa inhibition — the rationale explicitly notes mechanistic plausibility is low, and the ranking is driven by the TxGNN model score alone rather than any corroborating clinical or literature signal.

Notably, this same evidence pack contains other eptifibatide-disease pairs with far stronger, mechanistically coherent support — particularly hemoglobinopathy/sickle cell disease (vascular occlusion via platelet activation), which has a completed Phase 1/2 RCT and four supporting publications. The rheumatoid arthritis candidate should be read in that context as the weakest-evidenced of the top-ranked predictions, not the strongest.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

Eptifibatide is not currently marketed in this jurisdiction (0 licenses on record); no NDA or product authorization data is available.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The rheumatoid arthritis prediction is supported only by a TxGNN model score, with zero clinical trials or literature and a mechanistic rationale rated as weak by the evidence pack itself. Combined with a blocking data gap on TFDA safety warnings/contraindications, there is no basis for even a preliminary safety assessment (S0 stage).

**To proceed, the following is needed:**
- TFDA/FDA label data — warnings and contraindications (currently a blocking data gap, DG001)
- Formal mechanism-of-action documentation for eptifibatide (currently a high-severity data gap, DG002)
- Any preclinical or mechanistic studies specifically linking GPIIb/IIIa inhibition to RA pathophysiology
- Consider evaluating **hemoglobinopathy** (rank 7 in this same pack) as a separate, better-supported repurposing candidate — it has L2 evidence with a completed Phase 1/2 RCT and four supporting publications, versus no evidence for rheumatoid arthritis
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

