---
layout: default
title: Raloxifene
parent: 僅模型預測 (L5)
nav_order: 1105
evidence_level: L5
indication_count: 4
---

# Raloxifene
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

# Raloxifene: Original Indication Undocumented — Predicted for Duodenal Ulcer

## One-Sentence Summary

> Raloxifene (DB00481) is a known selective estrogen receptor modulator (SERM), but its original approved indication and mechanism of action are not available in the current evidence pack.
> The TxGNN model predicts a possible link to **Duodenal Ulcer**, with a prediction score of 99.72%,
> but this is currently supported by **0 clinical trials** and **0 publications** — the prediction rests on the model alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (no approved indication text in current data) |
| Predicted New Indication | Duodenal Ulcer |
| TxGNN Prediction Score | 99.72% |
| Evidence Level | L5 |
| Market Status | Not marketed (Taiwan) |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for Raloxifene is not available in this evidence pack. Based on general pharmacological knowledge, Raloxifene is classified as a SERM, a class of drugs that modulate estrogen receptor activity in various tissues. No original indication data was provided, so a direct comparison between "original indication" and "predicted new indication" cannot be made at this time.

Critically, the evidence pack's own rationale flags this prediction as mechanistically unsupported: there is no known physiological pathway connecting SERM activity to duodenal ulcer pathogenesis (which is typically driven by *H. pylori* infection, NSAID use, or acid hypersecretion). The high TxGNN score (0.997, rank 75) likely reflects an indirect or noisy connection within the knowledge graph rather than a genuine biological relationship.

The same pattern holds across the other three top-ranked predictions for this drug (hypoalphalipoproteinemia, duodenal obstruction, duodenogastric reflux) — all score highly (>0.995) but have zero supporting trials or literature, and only hypoalphalipoproteinemia has even a weak theoretical rationale (estrogen receptor modulation's known effect on lipid metabolism). None of the four candidates currently rises above model-prediction-only status.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Market Information

No marketing authorizations are currently on record for Raloxifene in this jurisdiction (total licenses: 0; status: not marketed).

---

## Safety Considerations

Please refer to the package insert for safety information.

*Note: The TFDA label/warnings and contraindications for this drug are marked as a **Blocking** data gap (DG001) — this must be resolved before any safety evaluation (S1 stage) can proceed.*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported by TxGNN model output alone (L5), with no clinical trials, literature, or established mechanistic pathway linking Raloxifene to duodenal ulcer. Combined with the absence of Taiwan marketing status and missing safety documentation, there is currently no basis to advance this candidate.

**To proceed, the following is needed:**
- TFDA label / package insert (warnings, contraindications) — currently blocking (DG001)
- Confirmed mechanism of action (MOA) data via DrugBank — currently high-priority gap (DG002)
- Independent literature or preclinical evidence establishing a plausible mechanistic link to duodenal ulcer, or reassessment of whether this candidate reflects genuine biology vs. knowledge-graph artifact
- If pursuing the alternative candidate (hypoalphalipoproteinemia), targeted literature search on SERM effects on lipid metabolism, since this has marginally stronger theoretical grounding
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

