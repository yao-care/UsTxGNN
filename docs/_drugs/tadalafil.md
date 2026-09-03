---
layout: default
title: Tadalafil
parent: 僅模型預測 (L5)
nav_order: 1192
evidence_level: L5
indication_count: 8
---

# Tadalafil
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

# Tadalafil: From PDE5-Inhibitor Indications to Ambras Type Hypertrichosis Universalis Congenita

## One-Sentence Summary

Tadalafil is a PDE5 inhibitor whose known approved uses include pulmonary arterial hypertension (PAH), among other conditions referenced in the evidence pack. The TxGNN model predicts it may be effective for **Ambras type hypertrichosis universalis congenita**, a rare congenital chromosomal disorder — but this prediction is currently supported by **0 clinical trials** and **0 publications**, and the evidence pack's own mechanistic review flags it as a likely knowledge-graph noise signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not fully documented in this evidence pack; pulmonary arterial hypertension (PAH) is referenced as an approved use of Tadalafil elsewhere in the pack |
| Predicted New Indication | Ambras type hypertrichosis universalis congenita |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 (model prediction only, no supporting trials or literature) |
| US Market Status | Not Marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for Tadalafil is not available in this evidence pack (flagged as a High-severity data gap). Based on the mechanistic notes embedded in the evidence pack's own rationale, Tadalafil is understood to act as a **PDE5 inhibitor**, working through the cGMP-NO pathway to regulate vascular smooth muscle tone — the mechanism underlying its known PAH indication.

However, there is **no established biological relationship** between this pathway and Ambras type hypertrichosis universalis congenita, which is a rare congenital chromosomal disorder affecting hair follicle distribution, not vascular or smooth-muscle physiology. The evidence pack's mechanistic assessment explicitly states that no known pathophysiological link exists between PDE5 inhibition and this condition.

Given the absence of any clinical trials, literature, or mechanistic rationale, and the pack's own conclusion, this prediction should be treated as a **likely false-positive signal**, characteristic of TxGNN scoring artifacts that occur for rare-disease nodes with low graph connectivity (i.e., few real-world edges cause disproportionately high similarity scores). This prediction does not currently meet the bar for further mechanistic or clinical justification.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## US Market Information

No marketing authorization records are available for Tadalafil in this dataset. Regulatory status is currently recorded as **Not Marketed**, with 0 total licenses on file.

---

## Safety Considerations

Please refer to the package insert for safety information. Note: TFDA label warnings/contraindications are currently a **Blocking** data gap (DG001) — this must be resolved before any safety (S1) screening can proceed for this drug.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite an extremely high TxGNN score (99.98%), there is zero clinical trial or literature support, and the evidence pack's own mechanistic review concludes there is no plausible biological connection between Tadalafil's PDE5-inhibitor mechanism and Ambras type hypertrichosis. This pattern is consistent with a rare-disease knowledge-graph noise artifact rather than a genuine repurposing signal.

**To proceed, the following is needed:**
- TFDA/regulatory label warnings and contraindications (Blocking gap — required before any safety evaluation)
- Detailed MOA documentation for Tadalafil from DrugBank or equivalent source
- Any preclinical or mechanistic literature directly connecting PDE5 inhibition to hair follicle biology, if this hypothesis is to be pursued further

**Additional note:** Among the other candidates in this evidence pack, **kyphoscoliotic heart disease** (rank 7) shows more mechanistic plausibility — it involves potential cor pulmonale/pulmonary hypertension overlapping with Tadalafil's established PAH mechanism — though it likewise currently lacks direct clinical or literature evidence and is flagged only as a research question. This may warrant a separate, targeted evaluation rather than being pursued under the current top-ranked (noise) prediction.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

