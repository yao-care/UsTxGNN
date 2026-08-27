---
layout: default
title: Mecasermin
parent: 僅模型預測 (L5)
nav_order: 890
evidence_level: L5
indication_count: 5
---

# Mecasermin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Mecasermin: From Severe Primary IGF-1 Deficiency to Monosomy X

## One-Sentence Summary

> Mecasermin (recombinant human IGF-1) is a growth-factor replacement therapy; DrugBank record confirms the compound but no approved-indication text is on file for this market. The TxGNN model predicts a possible link to **Monosomy X** (Turner syndrome), but this is a pure knowledge-graph inference with **zero supporting clinical trials or literature**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in this evidence pack (no Taiwan/US license on file). Per the drug's own repurposing rationale, mecasermin is a recombinant IGF-1 originally developed for severe primary IGF-1 deficiency (Laron-type growth hormone insensitivity) |
| Predicted New Indication | Monosomy X (Turner syndrome) |
| TxGNN Prediction Score | 99.59% |
| Evidence Level | L5 (model prediction only, no clinical or literature support) |
| US Market Status | Not marketed |
| Number of NDAs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (drug-level MOA is marked as a data gap, DG002). Based on known information, mecasermin is a recombinant human IGF-1 (rhIGF-1) molecule that acts downstream of the growth hormone receptor, replacing IGF-1 directly rather than stimulating its endogenous production.

Turner syndrome (monosomy X) commonly presents with growth retardation and a partial growth-hormone-resistant phenotype, and the GH-IGF1 axis is an established target for growth-promoting therapy in this population — which gives the prediction a plausible physiological rationale. However, the evidence pack itself flags this link as an indirect, graph-based association only ("需先查證是否已有真實世界文獻，本次收集未涵蓋"), with no clinical trial or publication data collected to confirm it.

Notably, a lower-ranked candidate in this same evidence pack — *growth hormone insensitivity syndrome with immune dysregulation 2* (rank 3, score 99.06%) — sits mechanistically much closer to mecasermin's known original use (it belongs to the same GHR/STAT5 signaling-defect disease family the drug was designed to bypass), but it likewise has no clinical trial or literature evidence in this dataset. Two other candidates (esophageal varices, with/without bleeding) are assessed in the source rationale as likely false positives driven by an indirect comorbidity association (low IGF-1 as a *consequence* of cirrhosis, not a treatment target) and are not further discussed here.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

Please refer to the package insert for safety information. Note: TFDA label warnings/contraindications and formal DDI data are currently unavailable and are flagged in the source evidence pack as a **Blocking** data gap (DG001) that prevents this candidate from entering safety pre-screening (S1).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is high, but the evidence level is L5 — a pure TxGNN model output with no clinical trials, no literature, and no route-compatibility data. Combined with a Blocking-severity gap in TFDA safety/label data, this candidate cannot yet proceed past the research-question stage.

**To proceed, the following is needed:**
- TFDA package insert / label warnings and contraindications (DG001, blocking)
- DrugBank/API-sourced mechanism of action detail (DG002)
- A dedicated literature and real-world-evidence search for IGF-1 use in Turner syndrome (not covered by this data collection run)
- Route-compatibility assessment (currently "pending")
- Consider evaluating the mechanistically closer candidate (GH insensitivity syndrome with immune dysregulation) in parallel, as it aligns more directly with mecasermin's known biology
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

