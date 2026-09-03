---
layout: default
title: Methocarbamol
parent: 僅模型預測 (L5)
nav_order: 909
evidence_level: L5
indication_count: 10
---

# Methocarbamol
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

# Methocarbamol: From Muscle Spasm to Cauda Equina Syndrome

## One-Sentence Summary

> Methocarbamol is a centrally acting skeletal muscle relaxant traditionally used to relieve muscle spasm–related pain.
> The TxGNN model predicts it may be effective for **Cauda Equina Syndrome**, with a prediction score of **99.98%**,
> but **no clinical trials or literature currently support this direction**, and the evidence pack's own mechanistic analysis argues against biological plausibility.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Muscle spasm–related pain (based on known drug classification; no TFDA-approved label text on file) |
| Predicted New Indication | Cauda Equina Syndrome |
| TxGNN Prediction Score | 99.98% (global model rank #1109) |
| Evidence Level | L5 (model prediction only, no clinical/literature support) |
| Market Status (Taiwan) | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for methocarbamol is not available in this evidence pack (flagged as a High-severity data gap, DG002). Based on known pharmacology, methocarbamol is a centrally acting skeletal muscle relaxant, believed to work primarily through general CNS depression rather than a direct effect on muscle fibers; it is used clinically only to relieve pain associated with acute, painful musculoskeletal conditions.

The evidence pack's own repurposing rationale, however, argues **against** applying this mechanism to cauda equina syndrome (CES): CES is a neurosurgical emergency caused by mechanical compression of the cauda equina nerve roots, not by muscle spasm. A centrally acting muscle relaxant can at most provide symptomatic relief and cannot alter the underlying compressive pathology — meaning there is no mechanistic basis for using methocarbamol to *treat* CES, only a theoretical role as an adjunct for spasm-related discomfort. This prediction should therefore be read as a knowledge-graph similarity signal rather than a mechanistically grounded hypothesis.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

Methocarbamol currently has **0 marketing authorizations on file** and is not marketed in Taiwan (`market_status: 未上市`). No license records are available to summarize approved indications or dosage forms.

## Other Candidates in This Batch

This evidence pack evaluated 10 TxGNN-predicted indications for methocarbamol; all were scored **L5 / Hold**, with no supporting clinical trials and only incidental (non-supportive) literature hits:

| Rank | Predicted Indication | Score | Assessment |
|------|----------------------|-------|------------|
| 2 | Irritable bowel syndrome | 99.98% | No known GI smooth-muscle mechanism |
| 3 | Panuveitis | 99.96% | No anti-inflammatory/immune mechanism |
| 4 | Anaphylaxis | 99.96% | 1 unrelated review (spider-bite management, incidental co-mention); no antihistamine/vasoactive mechanism |
| 5 | Iris disease | 99.94% | No ocular mechanism |
| 6 | Uveitis | 99.93% | No anti-inflammatory mechanism |
| 7 | Ventricular tachycardia | 99.93% | 1 unrelated veterinary case report (lamotrigine toxicosis); no cardiac conduction mechanism |
| 8 | Food-dependent exercise-induced anaphylaxis | 99.93% | No mast-cell mechanism |
| 9 | Conjunctivitis | 99.93% | No antimicrobial/anti-inflammatory mechanism |
| 10 | "Obsolete bundle branch block" | 99.93% | Flagged as an obsolete disease-ontology term — likely knowledge-graph noise, not a real candidate |

## Safety Considerations

Please refer to the package insert for safety information. **Note:** TFDA label warnings/contraindications are a Blocking data gap (DG001) — this precludes any safety pre-screening (S1) until resolved.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All 10 predicted indications rest solely on TxGNN embedding similarity (L5), with zero supporting clinical trials and no relevant literature. For the top candidate, cauda equina syndrome, the evidence pack's own mechanistic analysis concludes there is no plausible pharmacological basis for treatment benefit. Combined with a Blocking gap in TFDA safety/label data and the drug's non-marketed status in Taiwan, there is no basis to advance any candidate in this batch.

**To proceed, the following is needed:**
- TFDA label (warnings, contraindications) — resolves Blocking gap DG001
- Confirmed mechanism of action from DrugBank/primary literature — resolves DG002
- Independent mechanistic or preclinical evidence linking methocarbamol to any of the 10 predicted indications before further clinical evidence review
- Re-query "obsolete bundle branch block" against current disease ontologies to confirm it is a data artifact and exclude it from future scoring rounds
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

