---
layout: default
title: Mecamylamine
parent: 僅模型預測 (L5)
nav_order: 890
evidence_level: L5
indication_count: 4
---

# Mecamylamine
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

# Mecamylamine: From Historical Antihypertensive Use to Malignant Renovascular Hypertension

## One-Sentence Summary

Mecamylamine has no confirmed original indication in this evidence pack (MOA and indication data are gaps); background pharmacological knowledge flags it as a historical ganglionic-blocking antihypertensive, unconfirmed by the sources provided here.
The TxGNN model predicts it may be effective for **Malignant Renovascular Hypertension**, but currently **0 clinical trials** and **0 publications** support this specific link — this is a model-only prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this pack (no licenses, no original_indications on file) |
| Predicted New Indication | Malignant Renovascular Hypertension |
| TxGNN Prediction Score | 99.14% |
| Evidence Level | L5 (model prediction only) |
| US Market Status | Not marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action (MOA) data is not available from DrugBank in this pack (flagged as a High-severity data gap). Based on general pharmacological background knowledge cited alongside the prediction — **not itself confirmed by any source in this evidence pack** — mecamylamine is a non-selective, non-competitive ganglionic nicotinic acetylcholine receptor (nAChR) antagonist, historically used as a postganglionic sympathetic blocker to treat severe hypertension before being superseded by better-tolerated antihypertensive classes.

Malignant renovascular hypertension is a renin-driven hypertensive emergency. Ganglionic blockade would mechanistically be expected to lower systemic vascular resistance and blood pressure regardless of the underlying renovascular trigger, which is the likely basis for the TxGNN association. However, this is an indirect, class-level argument rather than disease-specific evidence, and no clinical trial, trial registry, or literature record in this pack links mecamylamine to this indication.

The second-ranked prediction, "malignant hypertensive renal disease," carries an identical score and rationale, suggesting it may be a downstream/overlapping disease-ontology term rather than an independent signal — this should be deduplicated before further evaluation.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## US Market Information

No marketing authorizations on record — mecamylamine is currently not marketed (0 licenses/NDAs).

## Safety Considerations

Please refer to the package insert for safety information. Note: the underlying label/warning data (TFDA-equivalent) is itself marked as a Blocking data gap in this pack, meaning safety screening (Stage S1) cannot currently be performed for this candidate.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is high (99.14%), but evidence level is L5 — no clinical trials, ICTRP registrations, or literature support the top-ranked indication, the drug is not marketed anywhere, and the safety label data required to even begin an initial safety screen is a Blocking gap.

**To proceed, the following is needed:**
- TFDA-equivalent package insert (warnings/contraindications) — Blocking gap (DG001)
- Verified mechanism of action via DrugBank API — High-priority gap (DG002)
- Deduplication check between "malignant renovascular hypertension" and "malignant hypertensive renal disease" (identical score, likely overlapping ontology terms)
- Targeted literature/trial search specifically for mecamylamine + malignant/renovascular hypertension (current PubMed query for this exact term returned 0 results)
- Resolution of the DDI query status ("not_found") — unclear whether this reflects a true absence of interactions or a failed query
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

