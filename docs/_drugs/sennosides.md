---
layout: default
title: Sennosides
parent: 僅模型預測 (L5)
nav_order: 1155
evidence_level: L5
indication_count: 6
---

# Sennosides
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

# Sennosides: From Constipation to Hypotrichosis Simplex of the Scalp

## One-Sentence Summary

> Sennosides is an anthraquinone-derived stimulant laxative pharmacologically used to treat constipation.
> The TxGNN model predicts a possible association with **Hypotrichosis Simplex of the Scalp** (score 99.29%),
> but this prediction is currently supported by **no clinical trials** and **no published literature**,
> and the evidence pack's own mechanistic review found no biological plausibility for this link.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in regulatory data (drug not marketed in Taiwan); based on known pharmacology, Sennosides is used as a stimulant laxative for constipation |
| Predicted New Indication | Hypotrichosis Simplex of the Scalp |
| TxGNN Prediction Score | 99.29% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| Market Status | Not Marketed (未上市) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (Data Gap). Based on known pharmacological class information, Sennosides is an anthraquinone-class stimulant laxative that irritates the colonic mucosa and promotes intestinal motility and fluid/electrolyte secretion — its proven use is limited to constipation management.

The predicted new indication, hypotrichosis simplex of the scalp, is a hair follicle growth disorder with pathways related to keratinocyte cycling and androgen receptor signaling. According to the evidence pack's own mechanistic analysis, **there is no known biological connection** between a stimulant laxative's mode of action and hair follicle biology. This appears to be a purely data-driven (embedding-similarity) prediction from TxGNN, without any supporting biological rationale.

The same pattern holds across the other five ranked predictions in this evidence pack (congenital hypotrichosis milia, diffuse alopecia areata, open-angle glaucoma, primary hereditary glaucoma, alopecia) — all are labeled L5/Hold, and each rationale explicitly states no known mechanistic link to Sennosides. Two clinical trials were nominally associated with the "alopecia" prediction (NCT03082560, NCT05348343), but on review neither trial involves Sennosides as an intervention — they were flagged as database keyword-overlap noise rather than actual supporting evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

Sennosides is currently **not marketed** in Taiwan (0 licenses on file); no authorization records are available for review.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: TFDA label warnings/contraindications are a Blocking data gap (DG001) — this candidate cannot proceed to safety pre-screening (S1) until this is resolved.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This candidate rests solely on a TxGNN embedding-similarity score (L5) with zero corroborating clinical trials or literature, and the evidence pack's own mechanistic review — across all six ranked predictions — found no plausible biological link between Sennosides' laxative mechanism and any predicted indication. The two clinical trials superficially matched to "alopecia" were confirmed irrelevant on inspection.

**To proceed, the following is needed:**
- Confirmed MOA data from DrugBank (currently Data Gap, High severity)
- TFDA label warnings/contraindications (currently Data Gap, Blocking — required before any S1 safety screening)
- Independent preclinical or mechanistic evidence establishing a biological rationale before this candidate can advance beyond S0
- If no such rationale emerges, this candidate should be deprioritized in favor of higher-evidence-level TxGNN predictions for this drug, if any exist
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

