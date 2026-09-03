---
layout: default
title: Thyrotropin Alfa
parent: 僅模型預測 (L5)
nav_order: 1225
evidence_level: L5
indication_count: 10
---

# Thyrotropin Alfa
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

# Thyrotropin Alfa: From Thyroid Cancer Follow-Up to Migraine Disorder

## One-Sentence Summary

> Thyrotropin alfa (recombinant human TSH) is currently used only as a diagnostic stimulation agent for post-thyroidectomy follow-up in differentiated thyroid cancer patients.
> The TxGNN model's top prediction is **Migraine Disorder**, but this direction is currently supported by **0 clinical trials** and **0 publications** — the score reflects knowledge-graph embedding similarity only, with no mechanistic, clinical, or literature evidence behind it.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack (no license records); known use is diagnostic TSH stimulation for post-thyroidectomy thyroid cancer follow-up |
| Predicted New Indication | Migraine Disorder |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 (model prediction only) |
| US Market Status | ✗ Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | **Hold** |

## Why is This Prediction Reasonable?

Currently, structured mechanism of action data is marked as a data gap. However, contextual information included in this evidence pack indicates that thyrotropin alfa (recombinant human TSH) acts on TSH receptors on thyroid follicular cells, stimulating thyroid hormone synthesis and iodine uptake. Clinically it is used exclusively as a diagnostic stimulation agent — not a therapeutic agent — for follow-up in patients who have undergone thyroidectomy for differentiated thyroid cancer.

There is no known or plausible mechanistic link between the TSH receptor/thyroid axis and migraine pathophysiology (trigeminovascular system, CGRP signaling). The evidence pack's own mechanistic assessment for this candidate explicitly states the high TxGNN score arises purely from knowledge-graph embedding similarity, with no supporting mechanism. The same applies to the #2–#9 ranked candidates (migraine with brainstem aura, Raynaud disease, migraine susceptibility, atrophoderma vermiculata, ulerythema ophryogenesis, pulmonary hypertension, kyphoscoliotic heart disease, POTS) — all are rated L5 with no clinical trial or literature support, and several (e.g., pulmonary hypertension) are flagged as potentially contradictory, since inducing a hyperthyroid-like state could theoretically worsen the target condition rather than treat it.

Notably, the only candidate in this evidence pack with substantive evidence — **hyperthyroidism** (rank 10, L2, 2 completed Phase 2 trials, 9 publications) — is itself a mechanistic contradiction: thyrotropin alfa is a TSH receptor **agonist** that would be expected to induce, not treat, hyperthyroidism. The two cited trials actually studied rhTSH as a pretreatment adjunct before radioiodine therapy for benign goiter, not as hyperthyroidism treatment, and the cited literature concerns interferon-alfa-induced thyroid dysfunction — unrelated to this drug. This underscores that none of the top-10 candidates currently constitute a mechanistically or clinically supported repurposing opportunity.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

No marketing authorization records exist for this drug in the reviewed jurisdiction. Market status is recorded as **Not Marketed**, with **0** total licenses on file.

## Safety Considerations

Please refer to the package insert for safety information. Key warnings, contraindications, and drug interaction data are currently not available in this evidence pack (flagged as a Blocking data gap pending TFDA label acquisition).

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication (migraine disorder) has no clinical trial or literature evidence and no plausible mechanistic rationale — it is a pure model-score artifact (L5/S0). The only evidence-supported candidate in the top 10 (hyperthyroidism) is mechanistically contradictory to the drug's pharmacology. No candidate in this pack currently meets the threshold to advance past initial screening.

**To proceed, the following is needed:**
- Structured MOA data from DrugBank (currently a High-severity data gap)
- TFDA/FDA label warnings and contraindications (currently a Blocking data gap — required before any safety pre-assessment)
- Re-screening of lower-ranked TxGNN candidates for mechanistically plausible, evidence-backed indications, since the current top 10 are dominated by L5 predictions or mechanism-contradictory matches
- If pursuing further, prioritize candidates with independent mechanistic rationale over embedding similarity alone
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

