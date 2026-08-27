---
layout: default
title: Lebrikizumab
parent: 僅模型預測 (L5)
nav_order: 841
evidence_level: L5
indication_count: 10
---

# Lebrikizumab
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

# Lebrikizumab: From [Indication Not on Record] to Severe Nonproliferative Diabetic Retinopathy

## One-Sentence Summary

> Lebrikizumab is a monoclonal antibody that selectively inhibits interleukin-13 (IL-13); no approved original indication is on record in this evidence pack, and the drug is not marketed in Taiwan.
> The TxGNN model's top-ranked prediction is **Severe Nonproliferative Diabetic Retinopathy** (score 97.94%), but this candidate has **0 clinical trials** and **0 publications** supporting it — the model's own rationale states the score likely reflects structural similarity to other anti-inflammatory biologics in the knowledge graph rather than a real mechanistic signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no approved indication on record (`original_indications` empty; not marketed in Taiwan) |
| Predicted New Indication | Severe Nonproliferative Diabetic Retinopathy |
| TxGNN Prediction Score | 97.94% |
| Evidence Level | L5 |
| Market Status (TFDA) | 未上市 (Not marketed) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for Lebrikizumab in this evidence pack (flagged as a High-severity data gap). Based on information embedded elsewhere in the pack, Lebrikizumab is a high-affinity IgG4 monoclonal antibody that selectively binds and neutralizes IL-13, blocking the IL-4Rα/IL-13Rα1 signaling complex — a mechanism well documented in the evidence collected for other candidate indications in this pack (notably dermatitis, rank #5).

For this specific top-ranked prediction, however, the pack's own repurposing rationale is explicit and skeptical: *"There is no evidence supporting a relationship between IL-13 inhibition and the progression of diabetic retinopathy. The high TxGNN score likely arises from structural similarity in the knowledge graph to other anti-inflammatory biologics, rather than genuine mechanistic or clinical evidence."*

IL-13-driven Th2 inflammation is not an established pathway in diabetic retinal microvascular disease, which is instead driven primarily by hyperglycemia-induced VEGF signaling, oxidative stress, and vascular permeability changes. No preclinical, observational, or clinical data in this pack bridge that gap. This prediction should be treated as a pure knowledge-graph score, not a mechanistically grounded hypothesis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

Lebrikizumab is not marketed in Taiwan (0 licenses on record); no authorization data is available.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a TxGNN model score with no corroborating clinical trials, literature, or plausible mechanistic link — evidence level L5, decision stage S0. The rationale text accompanying this prediction directly questions its own validity, attributing the score to structural artifacts in the knowledge graph rather than a real biological signal.

**To proceed, the following is needed:**
- Confirmed original indication and MOA data (currently marked Blocking/High-severity data gaps — TFDA label and DrugBank MOA lookup)
- Preclinical or mechanistic studies establishing any link between IL-13 inhibition and diabetic retinal microvascular disease
- Re-evaluation against lower-ranked candidates in this same evidence pack that have substantially stronger support: **dermatitis** (rank #5 — 29 trials, 20 publications, multiple completed Phase 3 RCTs) reflects the drug's well-established IL-13 biology, and **psoriasis** (rank #9 — L4, decision stage S1, "Research Question") has partial mechanistic and literature support worth independent follow-up.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

