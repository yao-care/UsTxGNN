---
layout: default
title: Tramadol
parent: 僅模型預測 (L5)
nav_order: 1246
evidence_level: L5
indication_count: 10
---

# Tramadol
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

# Tramadol: From Opioid Analgesic to Acromesomelic Dysplasia, Hunter-Thompson Type

## One-Sentence Summary

Tramadol is a centrally-acting opioid analgesic (μ-opioid receptor agonist plus norepinephrine/serotonin reuptake inhibitor) used broadly for moderate to moderately severe pain; no Taiwan license or original-indication text is on record in this evidence pack.
The TxGNN model's top-ranked prediction is **Acromesomelic Dysplasia, Hunter-Thompson Type**, a rare GDF5-related skeletal disorder,
but this ranking is supported by **0 clinical trials** and **0 publications**, and the evidence pack itself flags the mechanistic link as biologically implausible.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (no TFDA license record; tramadol is generally used as an opioid analgesic for moderate–severe pain) |
| Predicted New Indication | Acromesomelic Dysplasia, Hunter-Thompson Type |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| Taiwan Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for tramadol was not available in this evidence pack (flagged as a High-severity data gap). Based on generally established pharmacology, tramadol is a weak μ-opioid receptor agonist combined with inhibition of norepinephrine and serotonin reuptake, and is used clinically for pain management.

Acromesomelic Dysplasia, Hunter-Thompson Type, however, is a rare monogenic skeletal dysplasia caused by GDF5 mutations, with a pathology rooted in cartilage/bone development rather than pain signaling or inflammation. The evidence pack's own rationale states there is **no disease-modifying mechanistic relationship** between tramadol's analgesic pathway and this disorder, and attributes the high TxGNN score to embedding-space clustering of skeletal/joint-related diseases rather than genuine pharmacological plausibility.

Of the ten predictions reviewed, only rank 7 (**juvenile idiopathic arthritis**) has any supporting literature, and even that is indirect (name co-occurrence rather than tramadol-specific studies). The remaining nine, including the top-ranked prediction, are unsupported by any clinical trial or publication evidence and are explicitly characterized as likely KG noise.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

No approved license records are available — tramadol is currently **not marketed** in Taiwan per this evidence pack (0 licenses on file).

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (Acromesomelic Dysplasia, Hunter-Thompson Type, score 99.99%) has zero clinical trial or literature support and is explicitly assessed in the evidence rationale as lacking pharmacological plausibility — the evidence level is L5 (model prediction only), which does not meet the bar for further clinical evaluation.

**To proceed, the following is needed:**
- TFDA label warnings/contraindications (DG001, Blocking) — required before any S1 safety screening
- Tramadol mechanism-of-action data from DrugBank (DG002, High)
- If pursuing a repurposing candidate from this drug, consider redirecting attention to rank 7 (juvenile idiopathic arthritis), which has indirect literature support and a "Research Question" designation, and would require tramadol-specific pediatric pain studies to substantiate
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

