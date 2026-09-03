---
layout: default
title: Tirzepatide
parent: 僅模型預測 (L5)
nav_order: 1233
evidence_level: L5
indication_count: 10
---

# Tirzepatide
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

# Tirzepatide: From GIP/GLP-1 Metabolic Therapy to Gout

## One-Sentence Summary

> Tirzepatide is a dual GIP/GLP-1 receptor agonist; detailed original indication licensing data is not available in the current evidence pack, and the drug is not yet marketed in this jurisdiction.
> The TxGNN model's top-ranked prediction is **Gout**, but this association is currently **model-prediction only**, with **0 clinical trials** and **0 publications** identified in the evidence pack.
> A stronger-evidenced signal for **Osteoarthritis** (rank 2, 2 clinical trials incl. a Phase 4 RCT, 16 publications) was also identified and may warrant separate evaluation.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — `original_indications` is empty and `original_moa` is a data gap in the current evidence pack; drug is not yet marketed |
| Predicted New Indication | Gout |
| TxGNN Prediction Score | 96.75% |
| Evidence Level | L5 |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for Tirzepatide is not available in this evidence pack. Based on mechanistic notes accompanying the predictions, Tirzepatide is a dual GIP (glucose-dependent insulinotropic polypeptide) / GLP-1 (glucagon-like peptide-1) receptor agonist, a class primarily associated with weight loss, improved insulin sensitivity, and reduced systemic inflammation.

The rationale for the gout prediction is purely theoretical: GIP/GLP-1 agonism-driven weight loss and reduced insulin resistance could, in principle, lower uric acid production or improve uric acid excretion. However, this is described in the evidence pack itself as an "indirect association inferred by the knowledge-graph algorithm," with **no direct mechanistic study or clinical observation** currently supporting a Tirzepatide–gout link.

By contrast, the same evidence pack contains a substantially better-supported signal for **osteoarthritis** (rank 2, score 95.92%, Evidence Level L2), including an actively recruiting Phase 4 RCT specifically designed to test Tirzepatide in obesity-associated knee osteoarthritis (NCT06191848). This suggests the weight-loss/anti-inflammatory mechanism is biologically plausible for musculoskeletal/metabolic-adjacent conditions, but for gout specifically that mechanism remains unverified.

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
The top-ranked prediction (gout) is supported only by TxGNN model output (Evidence Level L5, Decision Stage S0), with zero clinical trials and zero literature identified. There is currently no mechanistic, preclinical, or clinical evidence directly linking Tirzepatide to gout, so this candidate does not meet the threshold to proceed.

**To proceed, the following is needed:**
- Direct mechanistic or preclinical evidence linking GIP/GLP-1 agonism to urate metabolism/excretion
- Confirmation of Tirzepatide's original indication and MOA data (currently marked as data gaps) to properly assess mechanistic plausibility
- TFDA/regional label warnings and contraindications, currently a blocking data gap (DG001) for any safety pre-assessment
- **Note:** The rank-2 candidate, osteoarthritis, shows meaningfully stronger evidence (L2, S2, an active Phase 4 RCT, and 16 supporting publications) and may be a more suitable candidate for near-term evaluation instead of gout
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

