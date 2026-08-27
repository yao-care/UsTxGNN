---
layout: default
title: Landiolol
parent: 僅模型預測 (L5)
nav_order: 833
evidence_level: L5
indication_count: 6
---

# Landiolol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Landiolol: From an Undocumented Original Indication to Lingual-Facial-Buccal Dyskinesia

## One-Sentence Summary

> Landiolol's original approved indication is not recorded in the current evidence pack (data gap), though it is known from the collected rationale notes to be an ultra-short-acting, highly β1-selective adrenergic antagonist (pharmacologically similar to esmolol).
> The TxGNN model's top-ranked prediction is **Lingual-Facial-Buccal Dyskinesia**, but this is supported by **0 clinical trials** and **0 publications** — and the evidence pack's own mechanistic rationale explicitly flags this specific link as biologically strained (the disorder is primarily dopaminergic, not adrenergic).
> This candidate should be treated as an unvalidated model signal only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in current evidence pack (no original indications or MOA on file) |
| Predicted New Indication | Lingual-Facial-Buccal Dyskinesia |
| TxGNN Prediction Score | 99.11% |
| Evidence Level | L5 (model prediction only, no clinical trials or literature) |
| Market Status (Taiwan) | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for Landiolol is not confirmed in this evidence pack (flagged as a High-severity data gap). However, the rationale notes attached to other candidates in this same prediction set describe Landiolol as an ultra-short-acting, highly selective β1-adrenergic receptor antagonist, pharmacologically comparable to esmolol and administered only by IV infusion with a half-life of minutes.

No original indication is recorded, so the usual comparison between "proven original use" and "predicted new use" cannot be made here — this is a genuine gap, not an omission.

For the top-ranked candidate specifically, the evidence pack's own repurposing rationale argues **against** mechanistic plausibility: lingual-facial-buccal dyskinesia is understood to arise primarily from chronic dopamine-receptor blockade (e.g., antipsychotic-induced tardive dyskinesia), a pathway centered on the dopaminergic system rather than adrenergic β1 signaling. The rationale text itself characterizes the β1-antagonist link to this disorder as having "no clear mechanistic association" — a high TxGNN score without a coherent pharmacological story. By contrast, a lower-ranked candidate in this same set (primary orthostatic tremor, rank 6) has a more conventional mechanistic basis, since β-blockers are established treatment for tremor disorders — though it is also unsupported by any trial or literature evidence and limited by Landiolol's IV-only, ultra-short-acting profile, which is unsuited to chronic outpatient management.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Taiwan Market Information

Landiolol currently holds no Taiwan marketing authorizations (market status: not marketed; 0 licenses on file).

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug-interaction data are all currently unavailable in this evidence pack; a Blocking-severity gap has been flagged for TFDA label/warning data.)

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- All six ranked candidates in this prediction set carry Evidence Level L5 (model score only, zero supporting trials or literature) and are staged at S0. For the top-ranked candidate, the mechanistic rationale documented in the evidence pack itself argues against plausibility rather than for it.
- A Blocking-severity data gap (TFDA warnings/contraindications) currently prevents this candidate from even entering the S1 safety pre-screen.

**To proceed, the following is needed:**
- TFDA label data (warnings, contraindications) — required before any S1 safety evaluation can begin (Blocking gap)
- Verified mechanism-of-action data from DrugBank (High-severity gap)
- Preclinical or mechanistic studies linking β1-adrenergic blockade to the proposed movement-disorder pathway, given the documented dopaminergic (not adrenergic) basis of the top-ranked indication
- Consider re-evaluating whether a mechanistically stronger candidate from this set (e.g., primary orthostatic tremor) merits prioritization over the raw TxGNN top rank
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

